#!/usr/bin/env python3
"""Test find_source_cues.py against test_input.txt. Run: python3 test_find_source_cues.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from find_source_cues import scan  # noqa: E402

EXPECTED = {
    1: {"vague authority"},
    2: {"superlative or first"},
    3: {"unnamed regulator or guidance"},
    4: {"figure"},
    5: {"weak source type", "figure"},
    6: set(),
    7: {"incomplete citation"},
    8: set(),
    9: {"weak source type", "incomplete citation"},
    10: {"undated current"},
    11: set(),
    12: set(),
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
