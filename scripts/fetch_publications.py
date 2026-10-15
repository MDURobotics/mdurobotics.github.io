#!/usr/bin/env python3
"""Fetch lab members' publications from DiVA into _data/publications.json.

Reads DiVA person ids from _data/people.yml, downloads each person's
records as CSL-JSON from MDU's DiVA export API, merges and de-duplicates
them, and writes a compact list that _pages/publications.html renders.

Usage: python3 scripts/fetch_publications.py [--people FILE] [--out FILE]
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

def parse_people(path):
    """Minimal parser for the `members:` list in people.yml (avoids a PyYAML dependency)."""
    people, cur = [], None
    for raw in open(path, encoding="utf-8"):
        line = raw.split(" #", 1)[0].rstrip() if not raw.lstrip().startswith("#") else ""
        if not line.strip():
            continue
        m = re.match(r"\s*-\s+name:\s*(.+)$", line)
        if m:
            cur = {"name": m.group(1).strip().strip('"\''), "diva": []}
            people.append(cur)
            continue
        m = re.match(r"\s+(\w+):\s*(.+)$", line)
        if m and cur is not None:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("["):
                cur[key] = [v.strip().strip('"\'') for v in val.strip("[]").split(",") if v.strip()]
            else:
                cur[key] = val.strip('"\'')
    for p in people:
        if isinstance(p.get("diva"), str):
            p["diva"] = [p["diva"]]
    return people

def parse_json(text):
    """DiVA sometimes emits invalid escapes (e.g. a lone backslash in a title); double them."""
    fixed = re.sub(r'\\(["\\/bfnrtu])|\\', lambda m: m.group(0) if m.group(1) else "\\\\", text)
    return json.loads(fixed)

def fetch_person(diva_id):
    params = {
        "format": "csl_json",
        "aq": json.dumps([[{"personId": diva_id}]]),
        "aqe": "[]",
        "aq2": "[[]]",
        "onlyFullText": "false",
        "noOfRows": "5000",
        "sortOrder": "dateIssued_sort_desc",
    }
    url = EXPORT_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "mdurobotics.github.io publication sync"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return parse_json(r.read().decode("utf-8"))
        except Exception as e:  # network hiccup or DiVA maintenance
            if attempt == 2:
                raise RuntimeError(f"DiVA request for {diva_id!r} failed: {e}") from e
            time.sleep(5 * (attempt + 1))

def norm(s):
    return re.sub(r"[^a-z]", "", (s or "").lower())

def simplify(rec, member_keys):
    kind = TYPES.get(rec.get("type")) or TYPES.get((rec.get("type"), rec.get("genre")))
    if not kind:
        return None
    year = (rec.get("issued", {}).get("date-parts") or [[None]])[0][0]
    authors = []
    for a in rec.get("author", []):
        name = " ".join(x for x in (a.get("given"), a.get("family")) if x) or a.get("literal", "")
        member = (norm(a.get("given"))[:1], norm(a.get("family"))) in member_keys
        authors.append({"name": name, "member": member})
    venue = rec.get("container-title") or rec.get("event") or rec.get("publisher") or ""
    return {
        "id": rec["id"],
        "type": kind,
        "year": int(year) if year else None,
        "title": rec.get("title", "").strip(),
        "authors": authors,
        "venue": venue,
        "doi": rec.get("DOI"),
        "url": RECORD_URL.format(rec["id"]),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--people", default="_data/people.yml")
    ap.add_argument("--out", default="_data/publications.json")
    args = ap.parse_args()

    people = parse_people(args.people)
    # Highlight members in author lists: match on first initial + family name
    member_keys = set()
    for p in people:
        parts = p["name"].split()
        member_keys.add((norm(parts[0])[:1], norm(" ".join(parts[1:]))))

    records = {}
    for p in people:
        for diva_id in p.get("diva", []):
            recs = fetch_person(diva_id)
            print(f"{p['name']} ({diva_id}): {len(recs)} records", file=sys.stderr)
            for rec in recs:
                records[rec["id"]] = rec

    pubs = [s for s in (simplify(r, member_keys) for r in records.values()) if s]
    pubs.sort(key=lambda x: (-(x["year"] or 0), x["title"].lower()))
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(pubs, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Wrote {len(pubs)} publications to {args.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
