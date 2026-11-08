#!/usr/bin/env python3
"""Structural submission-pack completeness check (offline). Never approves or files."""

from __future__ import annotations

import argparse
import json
import sys

REQUIRED = (
    "jurisdictions",
    "audience",
    "channel",
    "artefact_version",
)


def check(args: dict) -> dict:
    missing: list[str] = []
    for key in REQUIRED:
        val = args.get(key)
        if val is None or val == "" or val == []:
            missing.append(key)
    if not args.get("body") and not args.get("artefact_id"):
        missing.append("body_or_artefact_id")
    if not args.get("authorized_use_by_jurisdiction") and not args.get("authorized_use_text"):
        missing.append("authorized_use_text_or_by_jurisdiction")

    flags: list[str] = []
    if args.get("claims_matrix_attached") is False:
        flags.append("claims_matrix_missing")
    if str(args.get("channel") or "").lower() in {"promo", "digital"} and args.get(
        "fair_balance_card_attached"
    ) is False:
        flags.append("fair_balance_card_missing_for_promo")

    # Explicitly never invent filing
    if args.get("form_2253_filed") or args.get("fda_submission_id"):
        flags.append("refuse_post_clearance_filing_fields_in_prep_pack")

    ok = not missing and "refuse_post_clearance_filing_fields_in_prep_pack" not in flags
    return {
        "tool": "check_submission_pack",
        "ok": ok,
        "missing_fields": missing,
        "flags": flags,
        "post_clearance_note": (
            "If US promo and company SOP requires Form 2253 after human clearance, "
            "a named human owns filing. READY does not file."
        ),
        "mode": "READY-local",
        "tool_checked": False,
        "metered": False,
        "liability_line": (
            "This prepares material for human MLR review. "
            "It is not medical, legal, or regulatory approval."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--args-json", default="-")
    p.add_argument("--file")
    ns = p.parse_args()
    raw = open(ns.file, encoding="utf-8").read() if ns.file else (
        sys.stdin.read() if ns.args_json == "-" else ns.args_json
    )
    args = json.loads(raw or "{}")
    out = check(args if isinstance(args, dict) else {})
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
