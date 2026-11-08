#!/usr/bin/env python3
"""Build Navigator or Verify handoff JSON from a local session without calling MCP."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.session_io import load_session  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    p.add_argument("--target", choices=("navigator", "verify"), required=True)
    args = p.parse_args()
    row = load_session(args.session)
    if args.target == "navigator":
        packet = {
            "kind": "focused_navigator_handoff",
            "session_id": row["session_id"],
            "options": row.get("options") or [],
            "criteria": row.get("criteria") or [],
            "ratings": row.get("ratings") or [],
            "scale": row.get("scale"),
            "note": "Packet only — call Navigator decide_* / methods_* only if vont_ is present.",
        }
    else:
        packet = {
            "kind": "focused_verify_handoff",
            "session_id": row["session_id"],
            "claims": row.get("verify_claims") or [],
            "note": "Packet only — call qualify_source then check_claim only if vvfy_ is present.",
        }
    print(json.dumps(packet, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
