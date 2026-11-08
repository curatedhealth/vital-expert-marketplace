#!/usr/bin/env python3
"""Known-answer smoke for Curator enrichment gates."""

from __future__ import annotations

import sys
from pathlib import Path

MCPS = Path(__file__).resolve().parents[3]  # .../mcps/ontology_curator
sys.path.insert(0, str(MCPS.parent))

from ontology_curator.service import CuratorService
from ontology_curator.store import MemoryStore

WS = "a8c4e2f1-9b70-4d3e-8a15-6f2c0d91e447"
TEN = "025a2054-1b30-4db9-8c33-b03cad5d43ca"


def main() -> int:
    svc = CuratorService(MemoryStore())
    ent = {"__entitlement__": {"tenantId": TEN, "userId": "u1"}}
    refuse = svc.curator_propose_change(
        {
            **ent,
            "workspace_id": WS,
            "records": [
                {
                    "statement": "x",
                    "subject_family": "ph",
                    "subject_code": "PH-01",
                    "grade": "secondary",
                    "source_quote": "x",
                    "licence_status": "open",
                }
            ],
        }
    )
    assert refuse.get("error") == "missing_vp_code", refuse
    priv = svc.curator_capture_lead(
        {
            **ent,
            "workspace_id": WS,
            "leads": [
                {
                    "lead_type": "source",
                    "public_flag": "private",
                    "licence_status": "open",
                    "subject_canonical_id": "UNBOUND",
                    "subject_family": "unbound",
                    "source_quote": "x",
                    "source_url": "https://example.com",
                }
            ],
        }
    )
    assert priv["leads"][0].get("error") == "non_public_source_refused", priv
    assert 8 + max(8 - 4, 0) == 12
    print("KA smoke PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
