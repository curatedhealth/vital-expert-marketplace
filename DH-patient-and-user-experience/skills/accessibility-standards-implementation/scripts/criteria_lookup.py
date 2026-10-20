#!/usr/bin/env python3
"""Look up WCAG success criteria and compare targets, from references/data/wcag_criteria.csv.

The table was extracted from the W3C WCAG 2.1 and 2.2 Recommendations; the 2.0 column is
derived (2.1 minus the 17 criteria new in 2.1). See references/wcag-criteria-additions.md.

Usage:
  python3 criteria_lookup.py find 2.5.8 "contrast"        # by number or words in the name
  python3 criteria_lookup.py target 2.2 AA                 # list what a target covers
  python3 criteria_lookup.py diff 2.1 AA 2.2 AA            # what moving between targets adds or drops
"""
import csv
import os
import sys

RANK = {"A": 1, "AA": 2, "AAA": 3}
HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, "..", "references", "data", "wcag_criteria.csv")


def load():
    with open(TABLE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def col(v):
    if v not in ("2.0", "2.1", "2.2"):
        sys.exit(f"version must be 2.0, 2.1 or 2.2, not {v}")
    return "level_" + v.replace(".", "_")


def covered(rows, version, level):
    c = col(version)
    if level not in RANK:
        sys.exit("level must be A, AA or AAA")
    return {r["sc"]: r for r in rows if r[c] and RANK[r[c]] <= RANK[level]}


def show(r):
    lv = ", ".join(f"{v}: {r['level_' + v.replace('.', '_')] or 'not in version'}" for v in ("2.0", "2.1", "2.2"))
    return f"{r['sc']} {r['name']} ({lv})"


def key(sc):
    return tuple(int(x) for x in sc.split("."))


def main():
    rows = load()
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "find":
        for q in sys.argv[2:]:
            hits = [r for r in rows if r["sc"] == q or q.lower() in r["name"].lower()]
            print(f"## {q}: {len(hits)} match(es)")
            for r in hits:
                print("- " + show(r))
    elif cmd == "target":
        v, lv = sys.argv[2], sys.argv[3]
        cov = covered(rows, v, lv)
        counts = {k: sum(1 for r in cov.values() if r[col(v)] == k) for k in RANK}
        print(f"## WCAG {v} Level {lv}: {len(cov)} criteria ({', '.join(f'{k} {n}' for k, n in counts.items() if n)})")
        for sc in sorted(cov, key=key):
            print(f"- {sc} {cov[sc]['name']} ({cov[sc][col(v)]})")
    elif cmd == "diff":
        v1, l1, v2, l2 = sys.argv[2:6]
        a, b = covered(rows, v1, l1), covered(rows, v2, l2)
        added = sorted(set(b) - set(a), key=key)
        dropped = sorted(set(a) - set(b), key=key)
        print(f"## From WCAG {v1} {l1} ({len(a)}) to WCAG {v2} {l2} ({len(b)})")
        print(f"Added ({len(added)}):")
        for sc in added:
            print("- " + show(b[sc]))
        print(f"Dropped ({len(dropped)}):")
        for sc in dropped:
            note = " (removed in 2.2; may still need testing where a 2.0 or 2.1 policy applies, UX-STD-08)" if sc == "4.1.1" else ""
            print("- " + show(a[sc]) + note)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
