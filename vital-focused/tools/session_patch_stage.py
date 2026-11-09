#!/usr/bin/env python3
"""Merge a stage payload into a local FOCUSED session."""

from __future__ import annotations

import argparse
import json
import sys
sys.dont_write_bytecode = True  # read-only hosts: never write __pycache__
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.session_io import STAGES, load_session, save_session  # noqa: E402

REQUIRED = {
    "how_to_decide": ("statement", "goal", "decider", "deadline"),
    "gather_intelligence": ("knowns", "unknowns", "disconfirming_question"),
    "make_decision": ("chosen_option", "authored_by"),
    "learning_loop": ("review_date", "success_signal", "authored_by"),
}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--session", required=True)
    p.add_argument("--stage", required=True, choices=STAGES)
    p.add_argument("--payload-json", required=True, help="JSON object of fields to merge")
    args = p.parse_args()
    row = load_session(args.session)
    payload = json.loads(args.payload_json)
    if not isinstance(payload, dict):
        raise SystemExit("payload-json must be an object")
    stage = row["stages"].setdefault(args.stage, {"complete": False, "payload": {}, "notes": [], "gaps": [], "history": []})
    stage["payload"].update(payload)
    req = REQUIRED.get(args.stage) or ()
    missing = [f for f in req if not str(stage["payload"].get(f) or "").strip()]
    stage["gaps"] = [f"missing:{f}" for f in missing]
    stage["complete"] = not missing
    if args.stage == "make_decision" and stage["payload"].get("chosen_option"):
        row["choice"] = {
            "chosen_option": stage["payload"].get("chosen_option"),
            "authored_by": stage["payload"].get("authored_by"),
            "confidence_pct": stage["payload"].get("confidence_pct"),
        }
    save_session(row, args.session)
    print(json.dumps({"session_id": row["session_id"], "stage": args.stage, "complete": stage["complete"], "gaps": stage["gaps"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
