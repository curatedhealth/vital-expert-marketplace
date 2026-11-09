#!/usr/bin/env python3
"""Fail if good examples contain forbidden approval phrases as positive claims.

Instructional templates may *name* forbidden phrases while forbidding them
(e.g. \"Not approved for use\", \"mlr_reviewed stays false\"). Those are scanned
only for bare positive hits without a negation cue on the same line.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from contract import FORBIDDEN_PATTERNS, FORBIDDEN_PHRASES  # noqa: E402

NEGATION = ("not ", "never ", "false", "refuse", "do not", "don't", "must not", "**false**")


def _positive_hit(line: str, phrase: str) -> bool:
    lower = line.lower()
    if phrase not in lower:
        return False
    return not any(n in lower for n in NEGATION)


def main() -> int:
    goods = list((ROOT / "skills").glob("*/examples/good-sourced-draft.md"))
    templates = list((ROOT / "templates").glob("*.md"))
    bad: list[str] = []

    for path in goods:
        text = path.read_text(encoding="utf-8").lower()
        for phrase in FORBIDDEN_PHRASES:
            if phrase in text:
                bad.append(f"{path}: {phrase}")
        for pattern in FORBIDDEN_PATTERNS:  # TEH-RDY-019
            for m in re.finditer(pattern, text):
                bad.append(f"{path}: {m.group(0)}")

    for path in templates:
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for phrase in FORBIDDEN_PHRASES:
                if _positive_hit(line, phrase):
                    bad.append(f"{path}:{i}: {phrase}")
            low = line.lower()
            for pattern in FORBIDDEN_PATTERNS:  # TEH-RDY-019, same negation cue as phrases
                for m in re.finditer(pattern, low):
                    if not any(n in low for n in NEGATION):
                        bad.append(f"{path}:{i}: {m.group(0)}")

    if bad:
        print("FORBIDDEN_HITS")
        print("\n".join(bad))
        return 1
    print(f"OK scanned {len(goods)} good drafts + {len(templates)} templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
