#!/usr/bin/env python3
"""Heuristic ISI / fair-balance presence scan (offline). Not OPDP clearance."""

from __future__ import annotations

import argparse
import json
import re
import sys

ISI_MARKERS = (
    "important safety information",
    "isi",
    "please see",
    "full prescribing information",
    "brief summary",
    "contraindication",
    "boxed warning",
    "adverse reaction",
    "side effect",
)
BENEFIT_MARKERS = (
    "efficac",
    "improved",
    "reduc",
    "superior",
    "significant",
    "benefit",
)


def scan(text: str) -> dict:
    lower = text.lower()
    isi_hits = [m for m in ISI_MARKERS if m in lower]
    benefit_hits = [m for m in BENEFIT_MARKERS if m in lower]
    # crude prominence proxy: ISI first index vs benefit first index
    isi_pos = min((lower.find(m) for m in isi_hits if lower.find(m) >= 0), default=-1)
    ben_pos = min((lower.find(m) for m in benefit_hits if lower.find(m) >= 0), default=-1)
    flags: list[str] = []
    if benefit_hits and not isi_hits:
        flags.append("benefit_language_without_isi_markers")
    if isi_hits and ben_pos >= 0 and isi_pos > ben_pos + 800:
        flags.append("isi_appears_late_relative_to_benefits_heuristic")
    if re.search(r"approved for use|mlr approved|cleared for promotion", lower):
        flags.append("forbidden_approval_language")
    status = "revise" if flags else ("findings_only" if isi_hits else "human_gate_required")
    return {
        "tool": "check_isi_presence",
        "ok": "forbidden_approval_language" not in flags,
        "isi_markers_found": isi_hits,
        "benefit_markers_found": benefit_hits,
        "flags": flags,
        "suggested_mlr_status": status,
        "mode": "READY-local",
        "tool_checked": False,
        "note": "Heuristic only — net impression is a human / Regulatory judgment.",
        "liability_line": (
            "This prepares material for human MLR review. "
            "It is not medical, legal, or regulatory approval."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", help="Path to artefact text")
    p.add_argument("--text")
    ns = p.parse_args()
    if ns.file:
        text = open(ns.file, encoding="utf-8").read()
    else:
        text = ns.text or sys.stdin.read()
    out = scan(text)
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
