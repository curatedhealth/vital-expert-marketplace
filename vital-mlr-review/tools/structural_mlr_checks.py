#!/usr/bin/env python3
"""Structural flags for MLR packets (missing chairs, versions, markets)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contract import CHAIRS, LIABILITY_LINE  # noqa: E402
from runtime import run_tool  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", required=True, help="Path to packet JSON")
    ns = p.parse_args()
    packet = json.loads(Path(ns.file).read_text(encoding="utf-8"))
    flags: list[str] = []
    if not packet.get("artefact_version") and not (
        isinstance(packet.get("chairs"), dict)
        and all((packet["chairs"].get(c) or {}).get("artefact_version") for c in CHAIRS)
    ):
        flags.append("missing_artefact_version")
    chairs = packet.get("chairs") if isinstance(packet.get("chairs"), dict) else {}
    for c in CHAIRS:
        if c not in chairs:
            flags.append(f"missing_chair:{c}")
    if not packet.get("jurisdictions"):
        flags.append("missing_jurisdictions")
    validation = run_tool("mlr_validate_packet", {"packet": packet})
    compile_ = run_tool("mlr_compile_checklist", {"chairs": chairs, "jurisdictions": packet.get("jurisdictions") or []})
    out = {
        "ok": validation.get("ok") is True and not flags,
        "structural_flags": flags,
        "validation": validation,
        "conflict_slots": compile_.get("conflict_slots"),
        "liability_line": LIABILITY_LINE,
        "mode": "READY-local",
        "tool_checked": False,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
