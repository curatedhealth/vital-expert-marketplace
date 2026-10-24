#!/usr/bin/env python3
"""Scan text for MLR forbidden approval phrases (deterministic).

Run from a skill folder or pack host. Does not approve copy. Exit 1 on hits.

Usage:
    python check_forbidden_phrases.py path/to/draft.md
    python check_forbidden_phrases.py --self-test
    cat draft.md | python check_forbidden_phrases.py -
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

FORBIDDEN = (
    "approved for use",
    "mlr approved",
    "mlr_reviewed",
    "cleared for promotion",
    "regulator approved this copy",
    "fda approved this copy",
    "ema approved this copy",
    "mhra approved this copy",
)


def scan(text: str) -> list[str]:
    lower = text.lower()
    return [phrase for phrase in FORBIDDEN if phrase in lower]


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        assert scan("Ready for human review.") == []
        assert "mlr approved" in scan("This is MLR approved for brand.")
        print("self-test ok")
        return 0
    if len(argv) < 2:
        print("usage: check_forbidden_phrases.py <file|->", file=sys.stderr)
        return 2
    raw = sys.stdin.read() if argv[1] == "-" else Path(argv[1]).read_text(encoding="utf-8")
    hits = scan(raw)
    print(json.dumps({"hits": hits, "ok": not hits}, indent=2))
    return 1 if hits else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
