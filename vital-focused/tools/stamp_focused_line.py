#!/usr/bin/env python3
"""Stamp a FOCUSED check-line for local / synced / method-only runs."""

from __future__ import annotations

import argparse
import json

MODES = {
    "local": "FOCUSED-local (offline tools)",
    "synced": "FOCUSED-synced (Decision MCP special service)",
    "method": "not tool-checked (method only)",
    "offline": "not tool-checked (offline tools)",
}


def stamp(*, mode: str, skill: str, extra: str = "") -> dict:
    if mode not in MODES:
        raise SystemExit(f"Unknown mode {mode!r}; expected one of {', '.join(MODES)}")
    line = f"FOCUSED / {skill}: {MODES[mode]}"
    if extra.strip():
        line = f"{line} · {extra.strip()}"
    return {"check_line": line, "mode": mode, "skill": skill, "label": MODES[mode]}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mode", default="local", choices=sorted(MODES))
    p.add_argument("--skill", required=True)
    p.add_argument("--extra", default="")
    args = p.parse_args()
    print(json.dumps(stamp(mode=args.mode, skill=args.skill, extra=args.extra), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
