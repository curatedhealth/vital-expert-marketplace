#!/usr/bin/env python3
"""Validate a chair findings JSON array has required fields (deterministic).

Does not judge clinical/legal merit. Exit 1 on shape errors.

Rule ids (TEH-RDY-025): every `rule_id` must exist in a ruleset file shipped under the
plugin's `rulesets/` folder, and the row's chair must match the finding's chair. A chair
never mints a rule id (for example a filing form name used as a rule id).

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


def _rulesets_dir() -> Path | None:
    """Find the plugin's rulesets/ folder (works from scripts/ and skills/<name>/scripts/)."""
    here = Path(__file__).resolve().parent
    for parent in [here, *here.parents][:5]:
        candidate = parent / "rulesets"
        if (candidate / "REGISTRY.json").is_file():
            return candidate
    return None


def known_rule_ids(rulesets: Path | None = None) -> dict[str, str]:
    """rule_id -> chair, read from every ruleset JSON (REGISTRY.json excluded)."""
    folder = rulesets if rulesets is not None else _rulesets_dir()
    ids: dict[str, str] = {}
    if folder is None:
        return ids
    for path in sorted(folder.glob("*.json")):
        if path.name == "REGISTRY.json":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for chair, rows in (data.get("chairs") or {}).items():
            for row in rows or []:
                rid = row.get("rule_id")
                if rid:
                    ids[str(rid)] = str(row.get("chair") or chair)
    return ids


def validate(payload, rule_ids: dict[str, str] | None = None) -> list[str]:
    errors: list[str] = []
    if rule_ids is None:
        rule_ids = known_rule_ids()
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
        rid = row.get("rule_id")
        if rid is not None and rule_ids:
            if str(rid) not in rule_ids:
                errors.append(f"[{index}] rule_id {rid!r} is not in any ruleset under rulesets/ (never mint a rule id)")
            elif chair in CHAIRS and rule_ids[str(rid)] != chair:
                errors.append(f"[{index}] rule_id {rid!r} belongs to the {rule_ids[str(rid)]} chair, not {chair}")
    if not rule_ids:
        errors.append("rulesets/ not found: cannot confirm rule ids exist")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        good = [
            {
                "id": "F1",
                "chair": "medical",
                "severity": "major",
                "rule_id": "DE-PROMO-MED-001",
                "claim_span": "faster onset",
                "issue": "exceeds FI",
                "recommended_action": "revise",
                "applies_to": ["DE"],
            }
        ]
        ids = known_rule_ids()
        assert ids, "rulesets/ not found"
        assert validate(good) == [], validate(good)
        assert validate([{"id": "x"}])
        minted = [dict(good[0], chair="regulatory", rule_id="FORM-2253", applies_to=["US"])]
        assert any("never mint" in e for e in validate(minted))
        wrong_chair = [dict(good[0], chair="legal")]
        assert any("belongs to the medical chair" in e for e in validate(wrong_chair))
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
