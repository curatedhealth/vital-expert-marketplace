#!/usr/bin/env python3
"""Validate a chair findings JSON array has required fields (deterministic).

Does not judge clinical/legal merit. Exit 1 on shape errors.

Usage:
    python check_finding_shape.py findings.json
    python check_finding_shape.py --self-test
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = (
    "id",
    "chair",
    "severity",
    "rule_id",
    "claim_span",
    "issue",
    "recommended_action",
    "applies_to",
)
CHAIRS = {"medical", "legal", "regulatory"}
SEVERITIES = {"info", "minor", "major", "critical"}


def validate(payload) -> list[str]:
    errors: list[str] = []
    if isinstance(payload, dict) and "findings" in payload:
        findings = payload["findings"]
    else:
        findings = payload
    if not isinstance(findings, list):
        return ["root must be a list of findings or an object with findings[]"]
    for index, row in enumerate(findings):
        if not isinstance(row, dict):
            errors.append(f"[{index}] not an object")
            continue
        for key in REQUIRED:
            if key not in row:
                errors.append(f"[{index}] missing {key}")
        chair = row.get("chair")
        if chair is not None and chair not in CHAIRS:
            errors.append(f"[{index}] invalid chair {chair!r}")
        sev = row.get("severity")
        if sev is not None and sev not in SEVERITIES:
            errors.append(f"[{index}] invalid severity {sev!r}")
        applies = row.get("applies_to")
        if applies is not None and (not isinstance(applies, list) or not applies):
            errors.append(f"[{index}] applies_to must be a non-empty list")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        good = [
            {
                "id": "F1",
                "chair": "medical",
                "severity": "major",
                "rule_id": "DE-M-01",
                "claim_span": "faster onset",
                "issue": "exceeds FI",
                "recommended_action": "revise",
                "applies_to": ["DE"],
            }
        ]
        assert validate(good) == []
        assert validate([{"id": "x"}])
        print("self-test ok")
        return 0
    if len(argv) < 2:
        print("usage: check_finding_shape.py <findings.json>", file=sys.stderr)
        return 2
    payload = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    errors = validate(payload)
    print(json.dumps({"errors": errors, "ok": not errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
