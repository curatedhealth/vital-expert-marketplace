#!/usr/bin/env python3
"""Render frame / options / criteria / ratings markdown from a session."""

from __future__ import annotations

import argparse
import sys
sys.dont_write_bytecode = True  # read-only hosts: never write __pycache__
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.session_io import load_session  # noqa: E402


def _gap(value: object) -> str:
    text = str(value or "").strip()
    return text if text else "not given yet"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    args = p.parse_args()
    row = load_session(args.session)
    how = ((row.get("stages") or {}).get("how_to_decide") or {}).get("payload") or {}
    lines = [
        "# FOCUSED worksheet",
        "",
        "## Frame",
        f"- Statement: {_gap(how.get('statement') or row.get('statement'))}",
        f"- Goal: {_gap(how.get('goal') or row.get('goal'))}",
        f"- Decider: {_gap(how.get('decider') or row.get('decider'))}",
        f"- Deadline: {_gap(how.get('deadline') or row.get('deadline'))}",
        "",
        "## Options",
    ]
    for opt in row.get("options") or []:
        lines.append(f"- {opt.get('name') or opt.get('id') or 'not given yet'}")
    if not row.get("options"):
        lines.append("- not given yet")
    lines += ["", "## Criteria"]
    for c in row.get("criteria") or []:
        lines.append(f"- {c.get('name')}: weight={c.get('weight', 'not given yet')} direction={c.get('direction', 'higher_better')}")
    if not row.get("criteria"):
        lines.append("- not given yet")
    lines += ["", "## Ratings"]
    for cell in row.get("ratings") or []:
        lines.append(
            f"- {cell.get('rater')}: {cell.get('option') or cell.get('option_id')} / {cell.get('criterion')} = {cell.get('value')}"
        )
    if not row.get("ratings"):
        lines.append("- not given yet")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
