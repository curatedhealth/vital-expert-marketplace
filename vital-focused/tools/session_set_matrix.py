#!/usr/bin/env python3
"""Set criteria and ratings on a local FOCUSED session."""

from __future__ import annotations

import argparse
import json
import sys
sys.dont_write_bytecode = True  # read-only hosts: never write __pycache__
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.session_io import load_session, save_session  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    p.add_argument("--criteria-json", default="")
    p.add_argument("--ratings-json", default="")
    p.add_argument("--scale-json", default="")
    args = p.parse_args()
    row = load_session(args.session)
    if args.criteria_json:
        row["criteria"] = json.loads(args.criteria_json)
    if args.ratings_json:
        row["ratings"] = json.loads(args.ratings_json)
    if args.scale_json:
        row["scale"] = json.loads(args.scale_json)
    save_session(row, args.session)
    print(
        json.dumps(
            {
                "session_id": row["session_id"],
                "criteria": len(row.get("criteria") or []),
                "ratings": len(row.get("ratings") or []),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
