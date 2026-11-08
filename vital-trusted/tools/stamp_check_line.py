#!/usr/bin/env python3
"""Stamp a consistent TRUSTED check-line for offline or live Prove runs.

Usage:
  python stamp_check_line.py --mode offline --skill claim-assessment
  python stamp_check_line.py --mode local --skill source-assessment --extra "3 sources scored"
  python stamp_check_line.py --mode verify --skill claim-assessment
"""

from __future__ import annotations

import argparse
import json

MODES = {
    "offline": "not tool-checked (offline tools)",
    "local": "local support, not tool-checked",
    "method": "method only, not tool-checked",
    "verify": "tool-checked via VITAL Verify",
}


def stamp(*, mode: str, skill: str, extra: str = "") -> dict:
    if mode not in MODES:
        raise SystemExit(f"Unknown mode {mode!r}; expected one of {', '.join(MODES)}")
    line = f"TRUSTED / {skill}: {MODES[mode]}"
    if extra.strip():
        line = f"{line}; {extra.strip()}"
    return {"check_line": line, "mode": mode, "skill": skill, "label": MODES[mode]}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", required=True, choices=sorted(MODES))
    ap.add_argument("--skill", required=True)
    ap.add_argument("--extra", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    out = stamp(mode=args.mode, skill=args.skill, extra=args.extra)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(out["check_line"])


if __name__ == "__main__":
    main()
