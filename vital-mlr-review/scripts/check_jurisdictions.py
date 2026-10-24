#!/usr/bin/env python3
"""Fail closed when jurisdictions are missing or silently US-defaulted.

Reads a small JSON object with jurisdictions[]. Exit 1 on policy violations.

Usage:
    python check_jurisdictions.py context.json
    python check_jurisdictions.py --self-test
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def validate(ctx: dict) -> list[str]:
    errors: list[str] = []
    jurisdictions = ctx.get("jurisdictions")
    if not isinstance(jurisdictions, list) or not jurisdictions:
        errors.append("jurisdictions[] required — never invent US")
        return errors
    cleaned = [str(j).strip().upper() for j in jurisdictions if str(j).strip()]
    if not cleaned:
        errors.append("jurisdictions[] empty after normalize")
    if ctx.get("assumed_us_default") is True:
        errors.append("assumed_us_default is forbidden")
    if ctx.get("user_named_markets") is False and cleaned == ["US"]:
        errors.append("US-only without user_named_markets — refuse silent US default")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        assert validate({"jurisdictions": ["DE", "CH"]}) == []
        assert validate({"jurisdictions": []})
        assert validate({"jurisdictions": ["US"], "user_named_markets": False})
        assert validate({"jurisdictions": ["US"], "user_named_markets": True}) == []
        print("self-test ok")
        return 0
    if len(argv) < 2:
        print("usage: check_jurisdictions.py <context.json>", file=sys.stderr)
        return 2
    ctx = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    errors = validate(ctx)
    print(json.dumps({"errors": errors, "ok": not errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
