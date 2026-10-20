#!/usr/bin/env python3
"""Tally the 53 SPIRIT 2025 items and sub-items for a protocol draft.

Reads the item ids from references/spirit-2025-checklist.md (SP- rows), takes
the ids the person's facts fill (fully or partly) and the ids the person stated
not relevant, and prints the three counts (they always sum to 53) and every
open id once, grouped by SPIRIT section, for the short-mode answer.

The tally is bookkeeping only. Whether an item is filled or not relevant is
what the person's facts say; the script does not judge content.

Usage: python3 spirit_tally.py --filled "1a,3b,12,13" [--not-relevant "14b,32b"]
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKLIST = os.path.join(HERE, "..", "references", "spirit-2025-checklist.md")

def load_items():
    items = []
    for line in open(CHECKLIST, encoding="utf-8"):
        m = re.match(r"\|\s*SP-(\w+)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            section = m.group(2).split(":")[0].strip()
            items.append((m.group(1), section))
    return items

def parse(s, known):
    out = []
    for tok in [t.strip() for t in (s or "").split(",") if t.strip()]:
        tok = tok.removeprefix("SP-")
        if tok not in known:
            sys.exit(f"unknown SPIRIT id: {tok}")
        out.append(tok)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--filled", default="")
    ap.add_argument("--not-relevant", default="")
    a = ap.parse_args()
    items = load_items()
    ids = [i for i, _ in items]
    known = set(ids)
    filled = parse(a.filled, known)
    nr = parse(a.not_relevant, known)
    both = set(filled) & set(nr)
    if both:
        sys.exit(f"ids marked both filled and not relevant: {sorted(both)}")
    open_ids = [(i, s) for i, s in items if i not in filled and i not in nr]
    assert len(filled) + len(nr) + len(open_ids) == len(items)
    print(f"Items and sub-items: {len(items)}. Filled or partly filled: {len(set(filled))}. "
          f"Not relevant: {len(set(nr))}. Open: {len(open_ids)}.")
    groups = {}
    for i, s in open_ids:
        groups.setdefault(s, []).append(i)
    print("Open, by section: " + "; ".join(f"{s} {', '.join(v)}" for s, v in groups.items()) + ".")

if __name__ == "__main__":
    main()
