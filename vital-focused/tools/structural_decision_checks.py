#!/usr/bin/env python3
"""Print structural gaps for a FOCUSED local session."""

from __future__ import annotations

import argparse
import json
import sys
sys.dont_write_bytecode = True  # read-only hosts: never write __pycache__
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.session_io import load_session  # noqa: E402
from lib.stage_checks import structural_gaps  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    args = p.parse_args()
    row = load_session(args.session)
    gaps = structural_gaps(row)
    print(json.dumps({"session_id": row["session_id"], "gaps": gaps, "ok": not gaps}, indent=2))
    return 0 if not gaps else 2


if __name__ == "__main__":
    raise SystemExit(main())
