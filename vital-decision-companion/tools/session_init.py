#!/usr/bin/env python3
"""Create a local FOCUSED session JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.session_io import blank_session, default_session_path, save_session  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default="focused-sessions")
    p.add_argument("--out", default="")
    args = p.parse_args()
    row = blank_session()
    path = Path(args.out) if args.out else default_session_path(row["session_id"], args.root)
    save_session(row, path)
    print(json.dumps({"session_id": row["session_id"], "path": str(path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
