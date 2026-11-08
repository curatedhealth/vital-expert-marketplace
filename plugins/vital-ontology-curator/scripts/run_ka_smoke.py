#!/usr/bin/env python3
"""Known-answer smoke for Curator enrichment gates (KA_ENRICHMENT_W1)."""

from __future__ import annotations

import sys
from pathlib import Path

MCPS = Path(__file__).resolve().parents[3]  # .../mcps/ontology_curator
sys.path.insert(0, str(MCPS.parent))

from ontology_curator.fast_track import evaluate_record_eligibility
from ontology_curator.scope_cards import opportunity_score
from ontology_curator.service import CuratorService
from ontology_curator.store import MemoryStore

WS = "a8c4e2f1-9b70-4d3e-8a15-6f2c0d91e447"
TEN = "025a2054-1b30-4db9-8c33-b03cad5d43ca"


def main() -> int:
    svc = CuratorService(MemoryStore())
    ent = {"__entitlement__": {"tenantId": TEN, "userId": "u1"}}

    # KA-CUR-VP-01
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

    # KA-CUR-PRIV-01
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

    # KA-CUR-ODI-01
    assert opportunity_score(8, 4) == 12

    # KA-CUR-APQC-01 — incomplete scope → not fast-track eligible
    incomplete = {
        "source_type_code": "regulator",
        "support_status": "supported",
        "grade": "primary",
        "licence_status": "open",
        "interested_party": False,
        "source_location": "https://example.gov/x",
        "subject_family": "ph",
        "subject_code": "PH-01",
        "vp_code": "VP-PH-1",
        "measure_kind": "process_performance",
        "body": {"public_flag": "public", "apqc": {"unit": "days"}},
    }
    elig = evaluate_record_eligibility(incomplete)
    assert elig["eligible"] is False, elig
    assert any("apqc_scope_incomplete" in r for r in elig["reasons"]), elig

    # Polymorphic read smoke
    svc.store.insert_record(
        {
            "record_id": "ph-smoke",
            "version": 1,
            "tenant_id": TEN,
            "workspace_id": WS,
            "state": "approved",
            "statement": "ok",
            "subject_family": "ph",
            "subject_code": "PH-01",
            "vp_code": "VP-PH-1",
            "vd_code": "",
            "measure_kind": "process_performance",
            "grade": "secondary",
            "provenance": "outside",
        }
    )
    read = svc.curator_evidence_for_driver(
        {**ent, "workspace_id": WS, "subject_family": "ph", "subject_code": "PH-01"}
    )
    assert read.get("count") == 1, read

    # KA-CUR-COV-01 — declared scope pack coverage_ratio
    svc.store.upsert_watch_item(
        {
            "watch_id": "ka-cov-1",
            "tenant_id": TEN,
            "workspace_id": WS,
            "subject_canonical_id": "PH-01",
            "subject_family": "ph",
            "subject_code": "PH-01",
            "required_vp_code": "VP-PH-1",
            "measure_kind": "process_performance",
            "priority": 10,
            "active": True,
            "note": "[scope_pack]",
        }
    )
    m = svc.curator_enrichment_metrics({**ent, "workspace_id": WS})
    assert m.get("coverage_denominator") == "declared_watch_scope_pack", m
    assert m.get("declared_scope_pack_total", 0) >= 1, m
    assert m.get("coverage_ratio") is not None, m

    print("KA smoke PASS (VP, PRIV, ODI, APQC, polymorphic-read, coverage-ratio)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
