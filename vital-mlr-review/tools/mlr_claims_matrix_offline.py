#!/usr/bin/env python3
"""Build / validate a claims-matrix JSON structure offline. Uses align heuristics."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from runtime import run_tool  # noqa: E402
from contract import LIABILITY_LINE  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="READY offline claims matrix helper")
    p.add_argument("--file", help="JSON with claims[], jurisdictions, authorized_use_*")
    p.add_argument("--args-json", default="-")
    ns = p.parse_args()
    raw = Path(ns.file).read_text(encoding="utf-8") if ns.file else (
        sys.stdin.read() if ns.args_json == "-" else ns.args_json
    )
    args = json.loads(raw or "{}")
    claims = args.get("claims") or []
    if not claims:
        print(json.dumps({"ok": False, "gaps": ["claims[] required"]}, indent=2))
        return 1
    # Normalise claim strings for align tool
    claim_texts = []
    rows = []
    for i, c in enumerate(claims, start=1):
        if isinstance(c, str):
            text, meta = c, {}
        else:
            text = str(c.get("text") or c.get("claim") or "")
            meta = c
        claim_texts.append(text)
        rows.append(
            {
                "claim_id": meta.get("claim_id") or f"C-{i:03d}",
                "text": text,
                "type": meta.get("type") or "unspecified",
                "evidence_locator": meta.get("evidence_locator") or "[GAP]",
                "isi_pairing": meta.get("isi_pairing") or "[GAP]",
            }
        )
    align_args = {
        "claims": claim_texts,
        "jurisdictions": args.get("jurisdictions") or [],
        "authorized_use_by_jurisdiction": args.get("authorized_use_by_jurisdiction"),
        "authorized_use_text": args.get("authorized_use_text"),
    }
    align = run_tool("mlr_align_claims", align_args)
    # Merge align labels into rows
    by_claim: dict[str, list] = {}
    for r in align.get("results") or []:
        by_claim.setdefault(r.get("claim", ""), []).append(r)
    for row in rows:
        row["alignments"] = by_claim.get(row["text"], [])
        labels = {a.get("label") for a in row["alignments"]}
        if not row["alignments"]:
            row["status"] = "gap"
        elif "exceeds" in labels:
            row["status"] = "exceeds"
        elif "gap" in labels:
            row["status"] = "gap"
        elif "matches" in labels:
            row["status"] = "aligned"
        else:
            row["status"] = "no_authorization"
    out = {
        "tool": "mlr_claims_matrix_offline",
        "ok": align.get("ok") is True,
        "rows": rows,
        "align": align,
        "mode": "READY-local",
        "tool_checked": False,
        "liability_line": LIABILITY_LINE,
        "note": "Matrix is prep structure. Humans and chairs still judge; never approve.",
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
