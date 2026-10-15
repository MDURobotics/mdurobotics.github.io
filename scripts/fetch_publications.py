#!/usr/bin/env python3
"""Build _data/publications.json for the publications page.

Three sources, merged and de-duplicated:
  1. Publications authored by lab members, fetched from MDU's DiVA by each
     member's DiVA person id (_data/people.yml).
  2. PhD and licentiate theses supervised by lab members. DiVA's person
     search only covers authorship, so these are found by a name search and
     kept when a member is listed as supervisor.
  3. Hand-added entries in _data/publications_extra.yml, for publications
     that are missing from DiVA or not linked to the right person there.
     A hand-added entry is dropped once DiVA has the same title or DOI.

Usage: python3 scripts/fetch_publications.py
Stdlib only, so it runs as-is in GitHub Actions.
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request

EXPORT_URL = "https://mdu.diva-portal.org/smash/export.jsf"
RECORD_URL = "https://mdu.diva-portal.org/smash/record.jsf?pid={}"

# CSL type (+ DiVA genre for theses) -> label shown on the site.
# Anything not listed is skipped: student theses, newspaper articles, and
# manuscripts (undated thesis chapters that usually also appear as papers).
TYPES = {
    "article-journal": "Journal article",
    "paper-conference": "Conference paper",
    "chapter": "Book chapter",
    "book": "Book",
    "report": "Report",
    ("thesis", "PhD dissertation"): "PhD thesis",
    ("thesis", "Licentiate dissertation"): "Licentiate thesis",
}
THESIS_GENRES = ("PhD dissertation", "Licentiate dissertation")


def parse_yaml_list(path, key):
    """Minimal parser for a top-level list of flat mappings, e.g. `members:`.

    Supports `- k: v` to start an item, `k: v` continuation lines, quoted
    scalars, inline lists `[a, "b"]` and `#` comments. Enough for our data
    files without adding a PyYAML dependency.
    """
    items, cur, inside = [], None, False
    for raw in open(path, encoding="utf-8"):
        line = re.sub(r"\s+#.*$", "", raw.rstrip("\n")) if not raw.lstrip().startswith("#") else ""
        if not line.strip():
            continue
        if not line.startswith((" ", "-")):
            inside = line.split(":", 1)[0].strip() == key
            continue
        if not inside:
            continue
        m = re.match(r"\s*-\s+(\w+):\s*(.*)$", line)
        if m:
            cur = {}
            items.append(cur)
        else:
            m = re.match(r"\s+(\w+):\s*(.*)$", line)
        if m and cur is not None:
            cur[m.group(1)] = parse_scalar(m.group(2).strip())
    return items


def parse_scalar(val):
    if val.startswith("["):
        return [v.strip().strip('"\'') for v in re.findall(r'"[^"]*"|\'[^\']*\'|[^,\[\]]+', val) if v.strip()]
    if re.fullmatch(r"\d+", val):
        return int(val)
    return val.strip('"\'')


def parse_json(text):
    """Parse DiVA JSON, which sometimes has invalid escapes (a lone backslash in a
    title) and raw control characters in strings."""
    fixed = re.sub(r'\\(["\\/bfnrtu])|\\', lambda m: m.group(0) if m.group(1) else "\\\\", text)
    return json.loads(fixed, strict=False)


def diva_search(aq, rows=5000):
    params = {
        "format": "csl_json",
        "aq": json.dumps(aq),
        "aqe": "[]",
        "aq2": "[[]]",
        "onlyFullText": "false",
        "noOfRows": str(rows),
        "sortOrder": "dateIssued_sort_desc",
    }
    url = EXPORT_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "mdurobotics.github.io publication sync"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return parse_json(r.read().decode("utf-8"))
        except Exception as e:  # network hiccup or DiVA maintenance
            if attempt == 2:
                raise RuntimeError(f"DiVA request {aq} failed: {e}") from e
            time.sleep(5 * (attempt + 1))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def person_name(a):
    return " ".join(x for x in (a.get("given"), a.get("family")) if x) or a.get("literal", "")


class Members:
    def __init__(self, people):
        self.people = people
        # Authors are often abbreviated, so match on first initial + family name
        self.keys = set()
        for p in people:
            given, family = p["name"].split(" ", 1)
            self.keys.add((norm(given)[:1], norm(family)))

    def is_author(self, a):
        return (norm(a.get("given"))[:1], norm(a.get("family"))) in self.keys

    def supervisor_names(self, rec):
        """Members listed as supervisors. Uses the full given name, since
        DiVA spells supervisors out and initials collide (Mikael/Martin)."""
        names = []
        for s in rec.get("supervisor", []):
            for p in self.people:
                given, family = p["name"].split(" ", 1)
                if norm(s.get("family")) == norm(family) and norm(s.get("given")).startswith(norm(given)):
                    names.append(p["name"])
        return names


def simplify(rec, members):
    kind = TYPES.get(rec.get("type")) or TYPES.get((rec.get("type"), rec.get("genre")))
    if not kind or rec.get("status") == "Submitted":  # under review, not published
        return None
    year = (rec.get("issued", {}).get("date-parts") or [[None]])[0][0]
    authors = [{"name": person_name(a), "member": members.is_author(a)} for a in rec.get("author", [])]
    pub = {
        "id": rec["id"],
        "type": kind,
        "year": int(year) if year else None,
        "title": rec.get("title", "").strip(),
        "authors": authors,
        "venue": rec.get("container-title") or rec.get("event") or rec.get("publisher") or "",
        "doi": rec.get("DOI"),
        "diva_url": RECORD_URL.format(rec["id"]),
    }
    supervisors = members.supervisor_names(rec) if rec.get("type") == "thesis" else []
    if supervisors and not any(a["member"] for a in authors):
        pub["supervisors"] = supervisors
    return pub


def manual_entry(e, members):
    authors = []
    for name in e.get("authors", []):
        # A plain name string has no given/family split, so try every split
        # ("Lennie | Carlén Eriksson" as well as "Lennie Carlén | Eriksson")
        parts = name.split()
        member = any(members.is_author({"given": " ".join(parts[:i]), "family": " ".join(parts[i:])})
                     for i in range(1, len(parts)))
        authors.append({"name": name, "member": member})
    return {
        "id": "manual:" + norm(e["title"])[:40],
        "type": e.get("type", "Conference paper"),
        "year": e.get("year"),
        "title": e["title"],
        "authors": authors,
        "venue": e.get("venue", ""),
        "doi": e.get("doi"),
        "url": e.get("url"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--people", default="_data/people.yml")
    ap.add_argument("--extra", default="_data/publications_extra.yml")
    ap.add_argument("--out", default="_data/publications.json")
    args = ap.parse_args()

    people = parse_yaml_list(args.people, "members")
    for p in people:
        if isinstance(p.get("diva"), str):
            p["diva"] = [p["diva"]]
    members = Members(people)
    records = {}

    # 1. Authored
    for p in people:
        for diva_id in p.get("diva") or []:
            recs = diva_search([[{"personId": diva_id}]])
            print(f"{p['name']} ({diva_id}): {len(recs)} authored", file=sys.stderr)
            records.update((r["id"], r) for r in recs)

    # 2. Supervised theses
    for p in people:
        recs = diva_search([[{"freeText": p["name"]}]])
        theses = [r for r in recs if r.get("type") == "thesis" and r.get("genre") in THESIS_GENRES
                  and p["name"] in members.supervisor_names(r)]
        print(f"{p['name']}: {len(theses)} supervised theses", file=sys.stderr)
        records.update((r["id"], r) for r in theses)

    # 3a. Hand-added references to existing DiVA records
    extras = parse_yaml_list(args.extra, "publications")
    for e in extras:
        if "diva" in e:
            hit = [r for r in diva_search([[{"freeText": e["diva"]}]], rows=10) if r["id"] == e["diva"]]
            if not hit:
                print(f"warning: {e['diva']} not found in DiVA", file=sys.stderr)
            records.update((r["id"], r) for r in hit)

    pubs = [s for s in (simplify(r, members) for r in records.values()) if s]

    # 3b. Hand-added descriptions, unless DiVA already has them
    known_titles = {norm(p["title"]) for p in pubs}
    known_dois = {p["doi"].lower() for p in pubs if p.get("doi")}
    for e in extras:
        if "diva" in e:
            continue
        if norm(e["title"]) in known_titles or (e.get("doi") or "").lower() in known_dois:
            print(f"now in DiVA, can be removed from {args.extra}: {e['title']}", file=sys.stderr)
            continue
        pubs.append(manual_entry(e, members))

    pubs.sort(key=lambda x: (-(x["year"] or 0), x["title"].lower()))
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(pubs, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Wrote {len(pubs)} publications to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
