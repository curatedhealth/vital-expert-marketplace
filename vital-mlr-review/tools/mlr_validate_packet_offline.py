#!/usr/bin/env python3
"""Offline CLI for mlr_validate_packet. Label READY-local / not tool-checked. Never approves."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from runtime import run_tool  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="READY offline: mlr_validate_packet")
    parser.add_argument(
        "--args-json",
        default="-",
        help="JSON object of tool args, or - to read stdin (default)",
    )
    parser.add_argument(
        "--file",
        help="Read args JSON from a file instead of --args-json/stdin",
    )
    ns = parser.parse_args()
    if ns.file:
        raw = Path(ns.file).read_text(encoding="utf-8")
    elif ns.args_json == "-":
        raw = sys.stdin.read() or "{}"
    else:
        raw = ns.args_json
    try:
        args = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "gaps": [f"invalid JSON: {exc}"]}, indent=2))
        return 2
    if not isinstance(args, dict):
        print(json.dumps({"ok": False, "gaps": ["args must be a JSON object"]}, indent=2))
        return 2
    result = run_tool("mlr_validate_packet", args)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("ok") is not False else 1


if __name__ == "__main__":
    raise SystemExit(main())
