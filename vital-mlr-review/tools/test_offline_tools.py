"""Offline READY tools — parity smoke vs monorepo tool law."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from contract import FORBIDDEN_PHRASES, LIABILITY_LINE, TOOL_NAMES  # noqa: E402
from runtime import run_tool  # noqa: E402


class OfflineParity(unittest.TestCase):
    def test_surface_locked(self):
        self.assertIn("mlr_intake", TOOL_NAMES)
        self.assertEqual(len(TOOL_NAMES), 10)

    def test_intake_refuses_us_default(self):
        bad = run_tool(
            "mlr_intake",
            {"audience": "hcp", "channel": "promo", "artefact_version": "v1", "body": "x"},
        )
        self.assertFalse(bad["ok"])
        self.assertTrue(any("jurisdictions" in g for g in bad["gaps"]))

        ok = run_tool(
            "mlr_intake",
            {
                "jurisdictions": ["DE", "US"],
                "audience": "hcp",
                "channel": "promo",
                "artefact_version": "v1",
                "body": "Claim text",
                "authorized_use_by_jurisdiction": {
                    "DE": {"text": "Indicated for adults with X"},
                    "US": {"text": "Indicated for adults with X"},
                },
            },
        )
        self.assertTrue(ok["ok"])
        self.assertEqual(ok["mode"], "READY-local")
        self.assertFalse(ok.get("metered"))

    def test_list_and_get_rulesets(self):
        listed = run_tool("mlr_list_rulesets", {"audience": "hcp", "channel": "promo"})
        self.assertTrue(listed["ok"])
        ids = {p["ruleset_id"] for p in listed["packs"]}
        self.assertIn("mlr-us-hcp-promo-v0", ids)
        self.assertIn("mlr-de-hcp-promo-v0", ids)

        pack = run_tool(
            "mlr_get_ruleset",
            {"jurisdictions": ["DE", "UK"], "audience": "hcp", "channel": "promo"},
        )
        self.assertTrue(pack["ok"])
        self.assertIn("medical", pack["chairs"])

    def test_schema_and_validate_forbidden(self):
        schema = run_tool("mlr_get_packet_schema", {})
        self.assertTrue(schema["ok"])
        self.assertIn("schema", schema)

        packet = {
            "jurisdictions": ["US"],
            "ruleset_ids": ["mlr-us-hcp-promo-v0"],
            "mlr_status": "findings_only",
            "liability_line": LIABILITY_LINE,
            "chairs": {
                "medical": {
                    "chair": "medical",
                    "decision": "revise",
                    "artefact_version": "v1",
                    "findings": [
                        {
                            "claim_span": "x",
                            "severity": "major",
                            "rationale": "approved for use",  # forbidden
                            "applies_to": ["US"],
                        }
                    ],
                    "summary": "m",
                },
                "legal": {
                    "chair": "legal",
                    "decision": "revise",
                    "artefact_version": "v1",
                    "findings": [],
                    "summary": "l",
                },
                "regulatory": {
                    "chair": "regulatory",
                    "decision": "revise",
                    "artefact_version": "v1",
                    "findings": [],
                    "summary": "r",
                },
            },
        }
        bad = run_tool("mlr_validate_packet", {"packet": packet})
        self.assertFalse(bad["ok"])
        self.assertTrue(any("forbidden" in e for e in bad["errors"]))
        self.assertTrue(any(p in FORBIDDEN_PHRASES for p in FORBIDDEN_PHRASES))

    def test_align_compile_handoff(self):
        align = run_tool(
            "mlr_align_claims",
            {
                "jurisdictions": ["US"],
                "authorized_use_text": "Indicated for adults with type 2 diabetes",
                "claims": ["superior efficacy guaranteed"],
            },
        )
        self.assertTrue(align["ok"])
        self.assertEqual(align["results"][0]["label"], "exceeds")

        chairs = {
            "medical": {"decision": "revise", "findings": []},
            "legal": {"decision": "approve", "findings": []},
            "regulatory": {"decision": "revise", "findings": []},
        }
        compile_ = run_tool(
            "mlr_compile_checklist",
            {"chairs": chairs, "jurisdictions": ["US", "DE"]},
        )
        self.assertTrue(compile_["ok"])
        self.assertTrue(any(s.get("chairs_disagree") for s in compile_["conflict_slots"]))

        handoff = run_tool("mlr_handoff_verify", {"claims": ["claim A"]})
        self.assertTrue(handoff["ok"])
        self.assertFalse(handoff["called_verify"])

    def test_prep_record_local_write(self):
        packet = {
            "jurisdictions": ["DE"],
            "ruleset_ids": ["mlr-de-hcp-promo-v0"],
            "artefact_version": "v1",
            "mlr_status": "findings_only",
            "liability_line": LIABILITY_LINE,
            "chairs": {
                "medical": {
                    "chair": "medical",
                    "decision": "revise",
                    "artefact_version": "v1",
                    "findings": [],
                    "summary": "m",
                },
                "legal": {
                    "chair": "legal",
                    "decision": "revise",
                    "artefact_version": "v1",
                    "findings": [],
                    "summary": "l",
                },
                "regulatory": {
                    "chair": "regulatory",
                    "decision": "revise",
                    "artefact_version": "v1",
                    "findings": [],
                    "summary": "r",
                },
            },
        }
        refused = run_tool("mlr_build_prep_record", {"packet": packet})
        self.assertFalse(refused["ok"])

        with tempfile.TemporaryDirectory() as tmp:
            import os

            os.chdir(tmp)
            # re-import would keep old cwd sessions path — runtime uses Path.cwd() each call
            ok = run_tool(
                "mlr_build_prep_record",
                {"packet": packet, "cleared_by": {"name": "Ada Reviewer"}},
            )
            self.assertTrue(ok["ok"])
            self.assertIn("local_path", ok)
            path = Path(ok["local_path"])
            self.assertTrue(path.is_file())
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertIs(data["mlr_reviewed"], False)
            self.assertNotIn("approved for use", json.dumps(data).lower())


    def test_channel_isi_submission_helpers(self):
        from channel_intent_gate import gate
        from check_isi_presence import scan
        from check_submission_pack import check

        g = gate({
            "channel": "scientific_exchange",
            "proactive_or_reactive": "proactive",
            "offlabel_or_unlicensed": "yes",
            "body": "pipeline efficacy",
        })
        self.assertEqual(g["decision"], "human_gate_required")

        s = scan("Great efficacy. Important Safety Information: contraindications.")
        self.assertTrue(s["isi_markers_found"])

        bad = check({"audience": "hcp", "channel": "promo", "form_2253_filed": True})
        self.assertFalse(bad["ok"])
        self.assertIn("refuse_post_clearance_filing_fields_in_prep_pack", bad["flags"])

        ok = check({
            "jurisdictions": ["DE"],
            "audience": "hcp",
            "channel": "promo",
            "artefact_version": "v1",
            "body": "x",
            "authorized_use_text": "Indicated for adults",
            "claims_matrix_attached": True,
            "fair_balance_card_attached": True,
        })
        self.assertTrue(ok["ok"])


if __name__ == "__main__":
    unittest.main()
