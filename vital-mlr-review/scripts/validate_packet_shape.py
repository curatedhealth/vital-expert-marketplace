#!/usr/bin/env python3
"""Lightweight MLR packet shape check without network (deterministic).

Checks required top-level keys and separate medical/legal/regulatory chairs.
Prefer vital-mlr-review:mlr_validate_packet when vmlr_ is connected.
Exit 1 on shape errors.

Usage:
    python validate_packet_shape.py packet.json
    python validate_packet_shape.py --self-test
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_TOP = ("artefact_version", "jurisdictions", "chairs")
REQUIRED_CHAIRS = ("medical", "legal", "regulatory")


def validate(packet: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(packet, dict):
        return ["packet must be an object"]
    for key in REQUIRED_TOP:
        if key not in packet:
            errors.append(f"missing {key}")
    jurisdictions = packet.get("jurisdictions")
    if jurisdictions is not None and (
        not isinstance(jurisdictions, list) or not jurisdictions
    ):
        errors.append("jurisdictions must be a non-empty list")
    chairs = packet.get("chairs")
    if not isinstance(chairs, dict):
        errors.append("chairs must be an object with medical/legal/regulatory")
        return errors
    for name in REQUIRED_CHAIRS:
        if name not in chairs:
            errors.append(f"missing chairs.{name}")
            continue
        chair = chairs[name]
        if not isinstance(chair, dict):
            errors.append(f"chairs.{name} must be an object")
            continue
        if "decision" not in chair:
            errors.append(f"chairs.{name}.decision missing")
        if "findings" in chair and not isinstance(chair["findings"], list):
            errors.append(f"chairs.{name}.findings must be a list")
    # Blended single-reviewer shape is forbidden
    if "reviewer" in chairs or "blended" in chairs:
        errors.append("blended reviewer chair keys are forbidden — keep M/L/R separate")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        good = {
            "artefact_version": "v1",
            "jurisdictions": ["DE", "UK"],
            "chairs": {
                "medical": {"decision": "revise", "findings": []},
                "legal": {"decision": "approve", "findings": []},
                "regulatory": {"decision": "revise", "findings": []},
            },
        }
        assert validate(good) == []
        assert validate({"artefact_version": "v1"})
        print("self-test ok")
        return 0
    if len(argv) < 2:
        print("usage: validate_packet_shape.py <packet.json>", file=sys.stderr)
        return 2
    packet = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    errors = validate(packet)
    print(json.dumps({"errors": errors, "ok": not errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
