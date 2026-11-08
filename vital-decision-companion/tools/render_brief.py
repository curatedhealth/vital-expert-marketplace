#!/usr/bin/env python3
"""Compile a FOCUSED brief from a local session; missing fields → [GAP]."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.session_io import load_session  # noqa: E402
from lib.stage_checks import structural_gaps  # noqa: E402


def _gap(value: object) -> str:
    text = str(value or "").strip()
    return text if text else "[GAP]"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    args = p.parse_args()
    row = load_session(args.session)
    how = ((row.get("stages") or {}).get("how_to_decide") or {}).get("payload") or {}
    choice = row.get("choice") or {}
    impl = ((row.get("stages") or {}).get("implement") or {}).get("payload") or {}
    gaps = structural_gaps(row)
    lines = [
        "# Decision brief",
        "",
        f"**Statement:** {_gap(how.get('statement'))}",
        f"**Goal:** {_gap(how.get('goal'))}",
        f"**Decider:** {_gap(how.get('decider'))}",
        f"**Deadline:** {_gap(how.get('deadline'))}",
        "",
        "## Options considered",
    ]
    for opt in row.get("options") or []:
        lines.append(f"- {_gap(opt.get('name'))}")
    if not row.get("options"):
        lines.append("- [GAP]")
    lines += [
        "",
        "## Choice (person-authored)",
        f"- Chosen option: {_gap(choice.get('chosen_option'))}",
        f"- Authored by: {_gap(choice.get('authored_by'))}",
        f"- Confidence %: {_gap(choice.get('confidence_pct'))}",
        "",
        "## Implement",
        f"- Owner: {_gap(impl.get('owner') or (row.get('roles') or {}).get('decide'))}",
        f"- Review date: {_gap(impl.get('review_date'))}",
        "",
        "## Open gaps",
    ]
    if gaps:
        for g in gaps:
            lines.append(f"- {g['code']}: {g['message']}")
    else:
        lines.append("- none listed by structural checks")
    lines += ["", f"_Engine: {(row.get('meta') or {}).get('engine', 'FOCUSED-local')}_"]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
