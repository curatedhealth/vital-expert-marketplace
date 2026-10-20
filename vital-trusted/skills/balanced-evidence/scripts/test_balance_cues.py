#!/usr/bin/env python3
"""Test balance_cues.py against test_draft.txt and test_material.txt.
Run: python3 test_balance_cues.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from balance_cues import report, scan  # noqa: E402

EXPECTED_GROUPS = {
    1: {"benefit"},
    2: {"benefit"},
    4: {"reassurance"},
    6: {"benefit", "selection"},
    7: {"benefit"},
    8: {"risk or limitation"},
}


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return f.read()


def main():
    draft = read("test_draft.txt")
    material = read("test_material.txt")
    failures = []

    got = {r["line"]: set(r["groups"]) for r in scan(draft)}
    for line, groups in EXPECTED_GROUPS.items():
        if got.get(line, set()) != groups:
            failures.append(f"line {line}: expected {sorted(groups)}, got {sorted(got.get(line, set()))}")
    extra = set(got) - set(EXPECTED_GROUPS)
    if extra:
        failures.append(f"unexpected cue lines: {sorted(extra)}")

    res = report(draft, material, window=3)
    unpaired = res["benefit lines with no risk or limitation nearby"]
    if unpaired != [1, 2]:
        failures.append(f"unpaired benefits: expected [1, 2], got {unpaired}")
    c = res["counts"]
    if (c["benefit lines"], c["risk or limitation lines"], c["reassurance lines"]) != (4, 1, 1):
        failures.append(f"counts: got {c}")
    miss = res["in the material, not in the draft"]
    if miss["studies"] != ["ZELORA-3"]:
        failures.append(f"missing studies: expected ['ZELORA-3'], got {miss['studies']}")
    if miss["time points"] != ["month 12", "week 52"]:
        failures.append(f"missing time points: expected ['month 12', 'week 52'], got {miss['time points']}")

    res1 = report(draft, None, window=1)
    if res1["benefit lines with no risk or limitation nearby"] != [1, 2, 6]:
        failures.append(f"window 1: got {res1['benefit lines with no risk or limitation nearby']}")

    if failures:
        print("FAILED")
        print("\n".join(failures))
        return 1
    print(f"OK: {len(EXPECTED_GROUPS)} cue lines, counts, unpaired benefits (window 3 and 1), "
          "missing study and time points all matched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
