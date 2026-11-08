#!/usr/bin/env python3
"""Local claim-vs-passage support decision (offline check_claim lite).

Combines structural checks (claim_structure) with simple token overlap.
Never fetches sources. Never judges world-truth. Statuses are local-only and
must be labeled not tool-checked.

Statuses:
  supported | partial | unsupported | contradicted | unverifiable | out_of_scope

Usage:
  python passage_support.py --claim "X reduced Y by 20%" --passage "X reduced Y by 20% at week 12"
  python passage_support.py --json-file pair.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Allow running as script from tools/
sys.path.insert(0, str(Path(__file__).resolve().parent))
from claim_structure import structural_verdict  # type: ignore

LABEL = "local support, not tool-checked"
_STOP = {
    "the", "and", "for", "with", "that", "this", "from", "was", "were", "are",
    "been", "have", "has", "had", "into", "onto", "over", "under", "than",
}


def _tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]{3,}", text.lower()) if t not in _STOP}


def decide(claim: str, passage: str) -> dict:
    claim = (claim or "").strip()
    passage = (passage or "").strip()
    if not claim:
        return {"status": "unverifiable", "rationale": "Empty claim.", "label": LABEL}
    if not passage:
        return {
            "status": "unverifiable",
            "rationale": "No passage supplied; cannot check locally.",
            "label": LABEL,
        }

    structural_name = None
    structural_detail = None
    try:
        verdict = structural_verdict(claim, passage)
        if verdict:
            structural_name, structural_detail = verdict
    except Exception as exc:  # noqa: BLE001
        structural_name = "structure_error"
        structural_detail = type(exc).__name__

    if structural_name in {"contradicted", "unsupported", "out_of_scope"}:
        return {
            "status": structural_name,
            "rationale": f"Structural check: {structural_detail or structural_name}.",
            "label": LABEL,
            "structural": structural_name,
        }

    ct, pt = _tokens(claim), _tokens(passage)
    if not ct:
        return {"status": "out_of_scope", "rationale": "Claim has no content tokens.", "label": LABEL}

    overlap = len(ct & pt) / len(ct)
    if overlap >= 0.7:
        status = "supported"
        rationale = f"High token overlap ({overlap:.0%}) and no structural conflict."
    elif overlap >= 0.35:
        status = "partial"
        rationale = f"Partial token overlap ({overlap:.0%}); passage may miss claim details."
    else:
        status = "unsupported"
        rationale = f"Low token overlap ({overlap:.0%}); passage does not back the claim locally."

    return {
        "status": status,
        "rationale": rationale,
        "label": LABEL,
        "overlap": round(overlap, 3),
        "structural": structural_name,
        "structural_detail": structural_detail,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--claim", default="")
    ap.add_argument("--passage", default="")
    ap.add_argument("--json-file", help="JSON with claim/passage or list of pairs")
    args = ap.parse_args()

    if args.json_file:
        data = json.load(sys.stdin if args.json_file == "-" else open(args.json_file, encoding="utf-8"))
        if isinstance(data, list):
            out = [decide(item.get("claim", ""), item.get("passage", "")) for item in data]
        else:
            out = decide(data.get("claim", ""), data.get("passage", ""))
        print(json.dumps(out, indent=2))
        return

    print(json.dumps(decide(args.claim, args.passage), indent=2))


if __name__ == "__main__":
    main()
