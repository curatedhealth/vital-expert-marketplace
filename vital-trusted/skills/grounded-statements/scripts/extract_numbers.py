#!/usr/bin/env python3
"""List every number in a text with its context, for matching against the source.

Part of the VITAL TRUSTED skill grounded-statements (task TR-5.1.2).

  python extract_numbers.py draft.txt
  python extract_numbers.py draft.txt --json
  cat draft.txt | python extract_numbers.py -

Each row: line, the number as written, kind (percent, ratio-like, count or other),
and the text around it. It also lists units (patients, weeks, mg...) that appear with
more than one value, so each can be traced to a named quantity in the
source. It does not judge correctness.
"""
import argparse
import json
import re
import sys
from collections import defaultdict

NUM = re.compile(
    r"(?<![\d.,])(?P<num>[<>≤≥~]?\s?\d{1,3}(?:,\d{3})+(?:\.\d+)?|[<>≤≥~]?\s?\d+(?:\.\d+)?)"
    r"(?P<unit>\s?(?:%|percent(?:age points?)?|pp|mg|g|kg|ml|mL|weeks?|months?|years?|days?|patients?))?",
    re.IGNORECASE,
)


def kind(num, unit):
    u = (unit or "").strip().lower()
    if u.startswith("percentage point") or u == "pp":
        return "percentage points"
    if u in ("%",) or u.startswith("percent"):
        return "percent"
    if u.startswith("patient"):
        return "count"
    if u:
        return "quantity"
    n = num.strip().lstrip("<>≤≥~").strip()
    if "." in n and not "," in n:
        try:
            if float(n) < 10:
                return "ratio-like or decimal"
        except ValueError:
            pass
    return "number"


def extract(text):
    rows = []
    for ln, line in enumerate(text.splitlines(), 1):
        for m in NUM.finditer(line):
            num, unit = m.group("num").strip(), m.group("unit")
            before = line[max(0, m.start() - 40): m.start()].strip()
            after = line[m.end(): m.end() + 40].strip()
            rows.append({
                "line": ln,
                "value": num + (unit or ""),
                "kind": kind(num, unit),
                "before": before,
                "after": after,
            })
    return rows


def repeated_labels(rows):
    """Same unit word (patients, weeks, mg...) with different values across the text.

    Not an error by itself (a trial has screened, randomized and analyzed counts), but
    each listed value should be traceable to a distinct, named quantity in the source.
    """
    seen = defaultdict(list)
    for r in rows:
        m = re.search(r"[A-Za-z]+$", r["value"])
        if m and r["kind"] in ("count", "quantity"):
            unit = m.group(0).lower().rstrip("s")
            num = r["value"][: m.start()].strip()
            if num not in seen[unit]:
                seen[unit].append(num)
    return {k: v for k, v in seen.items() if len(v) > 1}


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("path", help="text file, or - for stdin")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    rows = extract(text)
    rep = repeated_labels(rows)
    if a.json:
        print(json.dumps({"numbers": rows, "same_unit_different_values": rep}, indent=2,
                         ensure_ascii=False))
        return
    print(f"{len(rows)} numbers found\n")
    for r in rows:
        print(f"L{r['line']:<4} {r['value']:<18} {r['kind']:<22} ...{r['before']} [#] {r['after']}...")
    if rep:
        print("\nSame unit, different values (trace each to a named quantity in the source):")
        for k, v in rep.items():
            print(f"  '{k}': {', '.join(v)}")


if __name__ == "__main__":
    main()
