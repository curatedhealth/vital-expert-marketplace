#!/usr/bin/env python3
"""Set options on a local FOCUSED session."""

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
    p.add_argument("--options-json", required=True, help='JSON list of {id,name} or strings')
    args = p.parse_args()
    row = load_session(args.session)
    raw = json.loads(args.options_json)
    options = []
    for item in raw:
        if isinstance(item, str):
            options.append({"id": item, "name": item})
        elif isinstance(item, dict):
            name = str(item.get("name") or item.get("id") or "").strip()
            oid = str(item.get("id") or name).strip()
            if name:
                options.append({"id": oid, "name": name})
    row["options"] = options
    stage = row["stages"].setdefault("widen_options", {"complete": False, "payload": {}, "notes": [], "gaps": [], "history": []})
    stage["payload"]["options"] = options
    stage["complete"] = len(options) >= 2
    stage["gaps"] = [] if stage["complete"] else ["need at least two options"]
    save_session(row, args.session)
    print(json.dumps({"session_id": row["session_id"], "option_count": len(options), "complete": stage["complete"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
