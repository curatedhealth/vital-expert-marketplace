#!/usr/bin/env python3
"""Score a local FOCUSED session (person's weights/ratings + ±10 robustness)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.score_core import score_session  # noqa: E402
from lib.session_io import load_session  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    args = p.parse_args()
    row = load_session(args.session)
    out = score_session(row)
    print(json.dumps(out, indent=2))
    return 0 if out.get("scored") or out.get("gaps") else 1


if __name__ == "__main__":
    raise SystemExit(main())
