#!/usr/bin/env python3
"""Test find_claim_cues.py against test_input.txt. Run: python3 test_find_claim_cues.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from find_claim_cues import scan  # noqa: E402

EXPECTED = {
    1: {"comparison"},
    2: {"absolute or superlative"},
    3: {"population or line of therapy"},          # "first-line" must not count as "first"
    4: {"population or line of therapy"},
    5: {"device function"},
    6: {"promotional tone"},
    7: {"safety absolute"},
    8: set(),
    9: {"unapproved status"},
    10: {"comparison"},
    11: set(),
}


def main():
    text = open(os.path.join(HERE, "test_input.txt"), encoding="utf-8").read()
    got = {}
    for r in scan(text):
        got.setdefault(r["line"], set()).add(r["group"])
    failures = []
    for line, groups in EXPECTED.items():
        if got.get(line, set()) != groups:
            failures.append(f"line {line}: expected {sorted(groups)}, got {sorted(got.get(line, set()))}")
    if failures:
        print("FAILED")
        print("\n".join(failures))
        return 1
    print(f"OK: {len(EXPECTED)} lines matched expected cue groups")
    return 0


if __name__ == "__main__":
    sys.exit(main())
