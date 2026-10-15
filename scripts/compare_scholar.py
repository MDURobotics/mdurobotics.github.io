#!/usr/bin/env python3
"""Check a list of publications (e.g. copied from Google Scholar) against the site.

Input: one publication per line as `year|title` (see notes/scholar-2026-10.txt).
Each title ends up in one of four groups:
  shown     already on the publications page
  filtered  fetched from DiVA but filtered out (student thesis, manuscript, submitted)
  unlinked  in DiVA, but not linked to any member. Often a student thesis or a
            thesis without supervisor data; otherwise add `diva:` to
            publications_extra.yml
  absent    not in DiVA at all -> add by hand, or ignore if it is not ours

Usage: python3 scripts/compare_scholar.py notes/scholar-2026-10.txt [out.json]
Run scripts/fetch_publications.py first so _data/publications.json is current.
"""
import difflib
import json
import re
import sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
import fetch_publications as f  # noqa: E402


def same(a, b):
    a, b = f.norm(a), f.norm(b)
    return (a == b or (min(len(a), len(b)) > 25 and (a.startswith(b) or b.startswith(a)))
            or difflib.SequenceMatcher(None, a, b).ratio() > 0.9)


def main():
    src = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    shown = json.load(open("_data/publications.json", encoding="utf-8"))
    raw = {}
    for p in f.parse_yaml_list("_data/people.yml", "members"):
        ids = p.get("diva") or []
        for i in [ids] if isinstance(ids, str) else ids:
            raw.update((r["id"], r) for r in f.diva_search([[{"personId": i}]]))

    out = {"shown": [], "filtered": [], "unlinked": [], "absent": []}
    for line in open(src, encoding="utf-8"):
        if "|" not in line:
            continue
        year, title = line.rstrip("\n").split("|", 1)
        if any(same(title, p["title"]) for p in shown):
            out["shown"].append([year, title])
            continue
        r = next((r for r in raw.values() if same(title, r["title"])), None)
        if r:
            out["filtered"].append([year, title, f"{r['type']}/{r.get('genre')}/{r.get('status')}"])
            continue
        words = " ".join(re.findall(r"[A-Za-z0-9]{4,}", title)[:8])
        hit = next((h for h in f.diva_search([[{"freeText": words}]], rows=30) if same(title, h["title"])), None)
        if hit:
            authors = ", ".join(a.get("family", "") for a in hit.get("author", []))
            kind = f"{hit['type']}/{hit.get('genre')}/{hit.get('status')}"
            out["unlinked"].append([year, title, hit["id"], kind, authors[:60]])
        else:
            out["absent"].append([year, title])

    for group, items in out.items():
        print(f"\n## {group} ({len(items)})")
        if group != "shown":
            for it in items:
                print("  " + " | ".join(it))
    if out_path:
        json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
