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


    def test_cleared_by_h5_token_refusal(self):
        """TEH-RDY-004: MLR-H5 refuses AI / automation / placeholder owners, token-based."""
        from runtime import cleared_by_refusal

        refused = [
            "auto", "AUTO", "Automated", "automation", "system", "System auto", "assistant",
            "AI", "a.i.", "A.I. reviewer", "model", "bot", "MLR Bot", "chatbot", "ChatGPT",
            "gpt", "GPT-4", "gpt4o", "OpenAI", "claude", "Anthropic", "Copilot", "Gemini",
            "LLM", "agent", "n/a", "N / A", "tbd", "unknown", "", "   ",
            "Claude (acting on behalf of Dr. Weber)", "Dr. Weber via ChatGPT",
        ]
        for name in refused:
            self.assertIsNotNone(cleared_by_refusal(name), name)
        humans = [
            "Aileen", "Claudette", "Gaia", "Jordan Lee", "Dr. Anna Weber", "Maria A. Ibanez",
            "Talbot Abbot", "Modelski", "Augusto", "Nadia", "Botha", "Zoë Müller", "Kai",
        ]
        for name in humans:
            self.assertIsNone(cleared_by_refusal(name), name)

        packet = {
            "jurisdictions": ["DE"],
            "ruleset_ids": ["mlr-de-hcp-promo-v0"],
            "artefact_version": "v1",
            "liability_line": LIABILITY_LINE,
            "chairs": {
                c: {"chair": c, "decision": "revise", "artefact_version": "v1", "findings": [], "summary": c}
                for c in ("medical", "legal", "regulatory")
            },
        }
        for name in ("auto", "Claude (acting on behalf of Dr. Weber)", "N/A"):
            for cleared in ({"name": name}, name):
                out = run_tool("mlr_build_prep_record", {"packet": packet, "cleared_by": cleared})
                self.assertFalse(out["ok"], name)
                self.assertIsNone(out.get("record"))
                self.assertIn("MLR-H5", " ".join(out["errors"]))
        with tempfile.TemporaryDirectory() as tmp:
            import os

            prev = os.getcwd()
            os.chdir(tmp)
            try:
                ok = run_tool("mlr_build_prep_record", {"packet": packet, "cleared_by": {"name": "Aileen Claudette"}})
            finally:
                os.chdir(prev)
            self.assertTrue(ok["ok"])
            self.assertIs(ok["record"]["mlr_reviewed"], False)

    def test_prep_record_refuses_stand_in_packet(self):
        """TEH-RDY-017 (MLR-H1): stand-in packets / placeholder versions / flagged chairs are refused."""
        from runtime import stand_in_packet_refusal

        def pkt(version="v1", summary="m", **extra):
            chairs = {
                c: {"chair": c, "decision": "revise", "artefact_version": version, "findings": [], "summary": summary}
                for c in ("medical", "legal", "regulatory")
            }
            base = {"jurisdictions": ["DE"], "ruleset_ids": ["mlr-de-hcp-promo-v0"], "artefact_version": version,
                    "mlr_status": "findings_only", "liability_line": LIABILITY_LINE, "chairs": chairs}
            base.update(extra)
            return base

        for bad in (pkt(version="placeholder-v1"), pkt(summary="Stand-in chair packet, no findings"),
                    pkt(synthetic=True), pkt(version="TBD")):
            self.assertTrue(stand_in_packet_refusal(bad), bad)
            # Refusal returns before any local write, so no temp cwd is needed.
            out = run_tool("mlr_build_prep_record", {"packet": bad, "cleared_by": {"name": "Jordan Lee"}})
            self.assertFalse(out["ok"])
            self.assertIsNone(out["record"])
        for good in (pkt(), pkt(version="v0.9.1", summary="Medical: two findings on posology wording")):
            self.assertIsNone(stand_in_packet_refusal(good), good)

    def test_channel_gate_whole_word_field_based(self):
        """TEH-RDY-018: free text never sets channel or reactive posture; promo markers force a gate."""
        from channel_intent_gate import gate

        # Branded efficacy + ISI, a negated "unsolicited" in the body, no posture field -> never sciex.
        g = gate({
            "channel": "scientific_exchange",
            "body": "Branded efficacy slides with an ISI page. No unsolicited medical information request exists.",
        })
        self.assertNotIn(g["decision"], {"treat_as_scientific_exchange", "treat_as_med_info"})
        self.assertEqual(g["decision"], "human_gate_required")
        # Same content even with a declared reactive posture -> mismatch gate, not sciex.
        g = gate({"channel": "scientific_exchange", "proactive_or_reactive": "reactive",
                  "body": "Branded efficacy slides. Important Safety Information follows."})
        self.assertEqual(g["decision"], "human_gate_required")
        self.assertTrue(any("channel_content_mismatch" in r for r in g["rationale"]))
        # Unsolicited request answered with promotional material -> mismatch gate.
        g = gate({"channel": "promo", "proactive_or_reactive": "unsolicited", "body": "Product leave-behind"})
        self.assertEqual(g["decision"], "human_gate_required")
        self.assertTrue(any("channel_content_mismatch" in r for r in g["rationale"]))
        # Reactive posture claimed but request explicitly not documented -> not sciex.
        g = gate({"channel": "med_info", "proactive_or_reactive": "reactive",
                  "unsolicited_request_documented": False, "body": "response letter"})
        self.assertEqual(g["decision"], "human_gate_required")
        # Substring "promo" in free-text intent must not classify as promo.
        g = gate({"intent": "Gate promo vs scientific exchange for this packet before chairs."})
        self.assertEqual(g["decision"], "human_gate_required")
        self.assertIn("channel", g["gaps"])
        # Positive directions still work.
        g = gate({"channel": "med_info", "proactive_or_reactive": "reactive", "offlabel_or_unlicensed": "no",
                  "body": "Non-branded response to enquiry; unsolicited request on file."})
        self.assertEqual(g["decision"], "treat_as_med_info")
        g = gate({"channel": "scientific_exchange", "proactive_or_reactive": "reactive", "body": "Data on request."})
        self.assertEqual(g["decision"], "treat_as_scientific_exchange")
        g = gate({"channel": "promo", "proactive_or_reactive": "proactive",
                  "body": "Branded efficacy. Important Safety Information."})
        self.assertEqual(g["decision"], "treat_as_promo")
        # Existing output field names kept (optional fields may be added, TEH-RDY-057/058).
        self.assertLessEqual(
            {"tool", "ok", "decision", "rationale", "gaps", "mode", "tool_checked", "metered", "note", "liability_line"},
            set(g),
        )

    def test_channel_gate_derived_reactive_non_branded(self):
        """TEH-RDY-040: no declared channel, but derived gate fields (reactive with a documented
        request, non-branded, no product claims) allow a provisional classification."""
        from channel_intent_gate import gate

        base = {"proactive_or_reactive": "reactive", "unsolicited_request_documented": True,
                "branded": False, "product_claims_present": False,
                "body": "Recognizing early signs of a lung condition. Early referral allows earlier assessment."}
        g = gate(dict(base))
        self.assertEqual(g["decision"], "treat_as_med_info")
        self.assertIn("channel", g["gaps"])  # still provisional: a human declares the channel
        self.assertIn("offlabel_or_unlicensed", g["gaps"])
        self.assertFalse(g["ok"])
        g = gate(dict(base, offlabel_or_unlicensed="no"))
        self.assertEqual(g["decision"], "treat_as_med_info")
        self.assertEqual(g["gaps"], ["channel"])
        # A field that cannot be derived keeps the gate closed.
        for missing in ("unsolicited_request_documented", "branded", "proactive_or_reactive"):
            args = dict(base)
            args.pop(missing)
            self.assertEqual(gate(args)["decision"], "human_gate_required", missing)
        # Off-label content, branding or promo markers keep the human gate.
        self.assertEqual(gate(dict(base, offlabel_or_unlicensed="yes"))["decision"], "human_gate_required")
        self.assertEqual(gate(dict(base, branded=True))["decision"], "human_gate_required")
        self.assertEqual(gate(dict(base, body="Prescribe now. Important Safety Information."))["decision"],
                         "human_gate_required")
        # Existing output field names kept (optional fields may be added, TEH-RDY-057/058).
        self.assertLessEqual(
            {"tool", "ok", "decision", "rationale", "gaps", "mode", "tool_checked", "metered", "note", "liability_line"},
            set(g),
        )

    def test_render_board_pack_reads_schema_fields(self):
        """TEH-RDY-041: chair comments and findings come from the schema's own fields; no [GAP]
        when they are present."""
        from render_board_pack import render

        finding = {"id": "F1", "chair": "medical", "severity": "major", "rule_id": "R-1",
                   "claim_span": "works in all adults", "issue": "Population wider than label text",
                   "recommended_action": "Restrict to the labelled population", "applies_to": ["DE"]}
        chair = lambda name, findings=(): {"chair": name, "artefact_version": "v1", "ruleset_id": "rs-1",
                                           "decision": "revise" if findings else "abstain",
                                           "findings": list(findings), "comments": [f"{name} comment"],
                                           "gaps": []}
        packet = {"artefact_version": "v1", "jurisdictions": ["DE"], "ruleset_ids": ["rs-1"],
                  "chairs": {"medical": chair("medical", [finding]), "legal": chair("legal"),
                             "regulatory": chair("regulatory")},
                  "conflicts": [], "mlr_status": "revise", "liability_line": "x"}
        text = render(packet)
        self.assertIn("Population wider than label text", text)
        self.assertIn("Restrict to the labelled population", text)
        self.assertIn("R-1", text)
        self.assertIn("medical comment", text)
        chair_block = text.split("## Chair summaries", 1)[1].split("## Human gate reminders", 1)[0]
        self.assertNotIn("[GAP]", chair_block)
        # Wrapped forms read the same packet.
        self.assertEqual(render({"packet": packet}), text)
        self.assertEqual(render({"compile": packet, "status": "draft", "artefact_version": "v1"}), text)

    def test_render_board_pack_prints_packet_status(self):
        """TEH-RDY-041: the footer and status line print the packet's own status, never a default."""
        from render_board_pack import render

        for status in ("findings_only", "revise", "human_gate_required", "prep_complete"):
            text = render({"artefact_version": "v1", "jurisdictions": ["DE"], "ruleset_ids": ["rs-1"],
                           "chairs": {}, "conflicts": [], "mlr_status": status})
            self.assertIn(f"- Status: {status}", text)
            self.assertIn(f"READY-local · not tool-checked · {status} · humans approve", text)
            others = {"findings_only", "revise", "human_gate_required", "prep_complete"} - {status}
            for other in others:
                self.assertNotIn(other, text)
        missing = render({"jurisdictions": ["DE"]})
        self.assertIn("- Status: [GAP]", missing)
        self.assertNotIn("findings_only", missing)
        self.assertIn("[GAP] chair packet not supplied", missing)

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


    def test_header_chair_version_mismatch_refuses_prep_complete(self):
        """TEH-RDY-046: chair artefact_version must equal the packet header; mismatch is an error,
        each version reported exactly as supplied, and prep_complete is never derived or kept."""
        from render_board_pack import render

        def pkt(header, chair_version, status="prep_complete"):
            chairs = {c: {"chair": c, "artefact_version": chair_version, "ruleset_id": "mlr-de-hcp-promo-v0",
                          "decision": "approve", "findings": [], "comments": ["Final."], "gaps": []}
                      for c in ("medical", "legal", "regulatory")}
            return {"artefact_version": header, "jurisdictions": ["DE"], "ruleset_ids": ["mlr-de-hcp-promo-v0"],
                    "chairs": chairs, "conflicts": [], "mlr_status": status, "liability_line": LIABILITY_LINE}

        # Mismatch direction.
        bad = pkt("v3.0", "v0.9.1")
        val = run_tool("mlr_validate_packet", {"packet": bad})
        self.assertFalse(val["ok"])
        self.assertNotEqual(val["mlr_status"], "prep_complete")
        for c in ("medical", "legal", "regulatory"):
            self.assertIn(f"artefact_version mismatch: packet header v3.0 vs {c} v0.9.1", val["errors"])
        self.assertEqual(val["normalised_packet"]["artefact_version"], "v3.0")
        rec = run_tool("mlr_build_prep_record", {"packet": bad, "cleared_by": {"name": "Jordan Lee"}})
        self.assertFalse(rec["ok"])
        self.assertIsNone(rec["record"])
        comp = run_tool("mlr_compile_checklist", {"chairs": bad["chairs"], "jurisdictions": ["DE"],
                                                  "artefact_version": "v3.0"})
        slot = [s for s in comp["conflict_slots"] if s["topic"] == "artefact_version_mismatch"]
        self.assertEqual(len(slot), 1)
        self.assertIn("packet header v3.0", slot[0]["detail"])
        self.assertIn("medical v0.9.1", slot[0]["detail"])
        text = render(bad)
        self.assertIn("packet header v3.0 vs medical v0.9.1", text)
        self.assertIn("- Artefact version: v0.9.1", text)
        self.assertNotIn("prep_complete", text)
        # Match direction.
        good = pkt("v0.9.1", "v0.9.1", status=None)
        good.pop("mlr_status")
        val = run_tool("mlr_validate_packet", {"packet": good})
        self.assertTrue(val["ok"], val["errors"])
        self.assertEqual(val["mlr_status"], "prep_complete")
        self.assertFalse([e for e in val["errors"] if "mismatch" in e])
        comp = run_tool("mlr_compile_checklist", {"chairs": good["chairs"], "jurisdictions": ["DE"],
                                                  "artefact_version": "v0.9.1"})
        self.assertFalse([s for s in comp["conflict_slots"] if s["topic"] == "artefact_version_mismatch"])
        good["mlr_status"] = "prep_complete"
        text = render(good)
        self.assertNotIn("## Version check", text)
        self.assertIn("- Status: prep_complete", text)
        with tempfile.TemporaryDirectory() as tmp:
            import os
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                rec = run_tool("mlr_build_prep_record", {"packet": good, "cleared_by": {"name": "Jordan Lee"}})
            finally:
                os.chdir(cwd)
        self.assertTrue(rec["ok"])
        self.assertEqual(rec["record"]["artefact_version"], "v0.9.1")


    def test_failed_validation_status_follows_precedence(self):
        """TEH-RDY-050: validator and renderer derive a failed packet's status by precedence."""
        from render_board_pack import render

        def pkt(decisions, chair_version="v0.9", status=None):
            chairs = {}
            for c, d in zip(("medical", "legal", "regulatory"), decisions):
                findings = [] if d == "approve" else [{"claim_span": "x", "severity": "major",
                                                       "rationale": "r", "applies_to": ["DE"]}]
                chairs[c] = {"chair": c, "artefact_version": chair_version, "decision": d,
                             "findings": findings, "summary": f"{c} advisory"}
            return {"artefact_version": "v1.0", "jurisdictions": ["DE"], "ruleset_ids": ["mlr-de-hcp-promo-v0"],
                    "chairs": chairs, "mlr_status": status, "liability_line": LIABILITY_LINE}

        for decisions, expected in ((("revise", "approve", "approve"), "revise"),
                                    (("approve", "approve", "approve"), "revise"),
                                    (("abstain", "approve", "approve"), "human_gate_required")):
            val = run_tool("mlr_validate_packet", {"packet": pkt(decisions)})
            self.assertFalse(val["ok"])
            self.assertEqual(val["mlr_status"], expected, decisions)
        self.assertIn("- Status: revise", render(pkt(("approve",) * 3, status="prep_complete")))
        self.assertIn("- Status: human_gate_required", render(pkt(("abstain", "approve", "approve"), status="findings_only")))

    def test_intake_intent_vs_medium(self):
        """TEH-RDY-057: intent binds (market + audience + intent); a medium is recorded, never binds,
        never reads as an unrecognized channel. Intent words map transparently."""
        base = {"jurisdictions": ["UK"], "audience": "hcp", "artefact_version": "v0.1", "body": "x"}
        # Direction 1: a medium alone -> intent missing, bind-later ask, medium recorded, no coverage.
        for medium in ("email", "print", "digital display", "digital", "congress", "social media"):
            out = run_tool("mlr_intake", dict(base, channel=medium))
            self.assertFalse(out["ok"], medium)
            self.assertIn("channel", out["missing_fields"], medium)
            self.assertEqual(out["ruleset_coverage"], [], medium)
            self.assertEqual(out["medium"], medium)
            self.assertEqual(out["context"]["medium"], medium)
            self.assertIsNone(out["context"]["channel"])
            self.assertIn("binds once audience and channel are supplied", out["next"])
            self.assertNotIn("no rule pack for", out["next"])
            self.assertNotIn("neither a known intent", out["next"])
            self.assertFalse([c for c in out["ruleset_coverage"] if c["ruleset_id"]])
        # Direction 2: intent words map transparently and bind; a medium beside an intent never blocks.
        for words in ("promo", "promotional", "Promotional", "promotion", "promotional email"):
            out = run_tool("mlr_intake", dict(base, channel=words))
            self.assertTrue(out["ok"], words)
            self.assertEqual(out["context"]["channel"], "promo")
            self.assertIn("mlr-uk-hcp-promo-v0", [c["ruleset_id"] for c in out["ruleset_coverage"]])
            self.assertNotIn("binds once", out["next"])
            self.assertTrue([m for m in out["channel_mapping"] if m["read_as"] == "intent" and m["value"] == "promo"])
            if words.lower() != "promo":
                self.assertIn("read as intent promo", out["next"])
        both = run_tool("mlr_intake", dict(base, channel="promo", medium="email"))
        self.assertTrue(both["ok"])
        self.assertEqual(both["medium"], "email")
        self.assertIn("mlr-uk-hcp-promo-v0", [c["ruleset_id"] for c in both["ruleset_coverage"]])
        sx = run_tool("mlr_intake", dict(base, jurisdictions=["DE"], intent="scientific exchange", medium="congress"))
        self.assertEqual(sx["context"]["channel"], "scientific_exchange")
        self.assertEqual(sx["context"]["medium"], "congress")
        self.assertFalse([c for c in sx["ruleset_coverage"] if c["jurisdiction"] == "DE" and c["ruleset_id"]])
        self.assertIn("mlr-global-hcp-scientific_exchange-v0", [c["ruleset_id"] for c in sx["ruleset_coverage"]])
        # An intent with no pack is a specific gap, never another intent's pack (TEH-RDY-052 kept).
        mi = run_tool("mlr_intake", dict(base, channel="med_info"))
        self.assertFalse([c for c in mi["ruleset_coverage"] if c["ruleset_id"]])
        self.assertIn("[GAP] no rule pack for intent med_info in UK", [c["gap"] for c in mi["ruleset_coverage"]])
        # A value that is neither an intent nor a medium: specific gap, never mapped.
        odd = run_tool("mlr_intake", dict(base, channel="fax blast"))
        self.assertFalse(odd["ok"])
        self.assertNotIn("channel", odd["missing_fields"])
        self.assertIn("[GAP] no rule pack for intent fax blast in UK", [c["gap"] for c in odd["ruleset_coverage"]])
        self.assertFalse([c for c in odd["ruleset_coverage"] if c["ruleset_id"]])
        # Conflicting intents are never resolved by the tool.
        conf = run_tool("mlr_intake", dict(base, channel="promo", intent="scientific_exchange"))
        self.assertIn("channel", conf["missing_fields"])
        self.assertIn("conflict", conf["next"])
        # channel missing: still the bind-later line, no coverage (TEH-RDY-043 kept)
        none = run_tool("mlr_intake", base)
        self.assertEqual(none["ruleset_coverage"], [])
        self.assertIn("channel", none["missing_fields"])
        self.assertIn("binds once audience and channel are supplied", none["next"])
        # get_ruleset: a medium never binds; intent + medium binds.
        bad = run_tool("mlr_get_ruleset", {"jurisdictions": ["UK"], "audience": "hcp", "channel": "email"})
        self.assertFalse(bad["ok"])
        self.assertIn("medium", " ".join(bad["gaps"]))
        good = run_tool("mlr_get_ruleset", {"jurisdictions": ["UK"], "audience": "hcp", "channel": "promotional",
                                            "medium": "email"})
        self.assertTrue(good["ok"])
        self.assertIn("mlr-uk-hcp-promo-v0", good["ruleset_ids"])
        self.assertEqual(good["medium"], "email")
        lst = run_tool("mlr_list_rulesets", {"jurisdiction": "UK", "audience": "hcp", "channel": "print"})
        self.assertEqual(lst["medium"], "print")
        self.assertTrue(lst["packs"])

    def test_channel_gate_intent_vs_medium_and_status(self):
        """TEH-RDY-057/058: the gate never reads a medium as an unrecognized channel; its status follows
        the shared map (missing inputs -> findings_only; judgment -> human_gate_required)."""
        from channel_intent_gate import gate

        # Direction 1: medium only -> intent pending, not unrecognized, findings_only.
        for medium in ("print", "email", "digital display", "digital"):
            g = gate({"channel": medium, "body": "Slides attached."})
            self.assertIn("channel", g["gaps"], medium)
            self.assertNotIn("unrecognised_channel_or_intent", g["gaps"], medium)
            self.assertEqual(g["medium"], medium)
            self.assertEqual(g["status"], "findings_only", medium)
            self.assertEqual(g["status_basis"], "missing_inputs", medium)
            self.assertNotEqual(g["decision"], "treat_as_promo", medium)  # a medium never implies promo
        # No channel, no posture, content with no signal for any reading -> missing inputs, findings_only.
        # (Lane 11: content that carries a reading -- e.g. MI letter markers -- now gets a provisional
        # decision instead, owner ruling TEH-RDY-062; covered in test_channel_gate_provisional_users.)
        g = gate({"body": "Slides attached."})
        self.assertEqual((g["status"], g["status_basis"]), ("findings_only", "missing_inputs"))
        # Direction 2: intent words map transparently and classify.
        g = gate({"channel": "promotional", "proactive_or_reactive": "proactive", "body": "x"})
        self.assertEqual(g["decision"], "treat_as_promo")
        self.assertEqual((g["status"], g["status_basis"]), ("findings_only", "final"))
        self.assertTrue(any("read as promo" in r for r in g["rationale"]))
        g = gate({"channel": "scientific exchange", "proactive_or_reactive": "reactive", "medium": "congress",
                  "body": "Data on request."})
        self.assertEqual(g["decision"], "treat_as_scientific_exchange")
        self.assertEqual(g["medium"], "congress")
        # Medium plus derived fields still allows the provisional classification (TEH-RDY-040).
        g = gate({"channel": "email", "proactive_or_reactive": "reactive", "unsolicited_request_documented": True,
                  "branded": False, "product_claims_present": False, "body": "Recognizing early signs."})
        self.assertEqual(g["decision"], "treat_as_med_info")
        self.assertEqual((g["status"], g["status_basis"]), ("findings_only", "provisional"))
        # Judgment calls still gate (never softened).
        g = gate({"channel": "scientific_exchange", "proactive_or_reactive": "reactive",
                  "body": "Branded efficacy slides. Important Safety Information follows."})
        self.assertEqual((g["decision"], g["status"]), ("human_gate_required", "human_gate_required"))
        g = gate({"channel": "promo", "proactive_or_reactive": "unsolicited", "body": "Product leave-behind"})
        self.assertEqual(g["status"], "human_gate_required")
        g = gate({"channel": "scientific_exchange", "proactive_or_reactive": "proactive",
                  "offlabel_or_unlicensed": "yes", "body": "pipeline efficacy"})
        self.assertEqual(g["status"], "human_gate_required")
        # Free-text intent with two intent words is unmatched, never classified by substring.
        g = gate({"intent": "Gate promo vs scientific exchange for this packet before chairs."})
        self.assertIn("unrecognised_channel_or_intent", g["gaps"])
        self.assertEqual(g["status"], "findings_only")


    def test_channel_gate_mixed_content_is_human_gate(self):
        """TEH-RDY-061: promotional + medical-information content in one piece -> human gate with the
        conflicting elements quoted; incomplete (not mixed) content stays a missing input."""
        from channel_intent_gate import gate

        mixed_body = ("Product X delivers superior efficacy. Important Safety Information follows. "
                      "In response to your enquiry, the requested data are attached.")
        # Direction 1: mixed in supplied text -> human_gate_required, whatever intent is declared.
        for extra in ({}, {"channel": "promo", "proactive_or_reactive": "proactive"},
                      {"channel": "med_info", "proactive_or_reactive": "reactive"}):
            g = gate(dict(extra, body=mixed_body))
            self.assertEqual((g["decision"], g["status"], g["status_basis"]),
                             ("human_gate_required", "human_gate_required", "judgment"), extra)
            self.assertEqual(g["mixed_content"]["source"], "supplied_text")
            self.assertIn("In response to your enquiry, the requested data are attached.",
                          g["mixed_content"]["medical_information"])
            self.assertIn("Product X delivers superior efficacy.", g["mixed_content"]["promotional"])
            self.assertTrue(any(r.startswith("mixed_content:") for r in g["rationale"]))
        # Person's description of a mix (no text supplied) -> human gate, elements quoted from the description.
        g = gate({"mixed_content": True, "mixed_elements": ["branded claims", "MI letter fragments"]})
        self.assertEqual((g["status"], g["status_basis"]), ("human_gate_required", "judgment"))
        self.assertEqual(g["mixed_content"], {"source": "person_description",
                                              "elements": ["branded claims", "MI letter fragments"]})
        self.assertTrue(any('"MI letter fragments"' in r for r in g["rationale"]))
        # Direction 2: incomplete, not mixed -> rule 4 missing inputs (never a human gate on that ground).
        for args in ({"body": "Slides attached."}, {"channel": "print", "body": "x"}, {},
                     {"mixed_content": False, "body": "Slides attached."}):
            g = gate(args)
            self.assertEqual((g["status"], g["status_basis"]), ("findings_only", "missing_inputs"), args)
            self.assertIsNone(g["mixed_content"], args)
        # One reading only is not mixed: promo-only with declared promo stays treat_as_promo;
        # MI-only with declared med_info and reactive posture stays treat_as_med_info.
        g = gate({"channel": "promo", "proactive_or_reactive": "proactive",
                  "body": "Branded efficacy. Important Safety Information. For medical information call 0800."})
        self.assertEqual((g["decision"], g["status"]), ("treat_as_promo", "findings_only"))
        self.assertIsNone(g["mixed_content"])
        g = gate({"channel": "med_info", "proactive_or_reactive": "reactive",
                  "body": "In response to your enquiry, please find the requested information."})
        self.assertEqual((g["decision"], g["status"]), ("treat_as_med_info", "findings_only"))
        # Negated markers do not count as a mix.
        g = gate({"channel": "med_info", "proactive_or_reactive": "reactive",
                  "body": "Non-branded response to enquiry; no ISI."})
        self.assertIsNone(g["mixed_content"])
        self.assertEqual(g["status"], "findings_only")

    def test_channel_gate_provisional_users(self):
        """TEH-RDY-062: users unknown -> provisional content-based decision, findings_only, asks who will
        use it; never 'not classified' when the supplied content carries a reading."""
        from channel_intent_gate import gate

        deck = "Product X: superior efficacy versus placebo at week 24. Prescribe with confidence."
        # Direction 1: content carries a reading -> provisional decision, users pending and asked.
        g = gate({"users": "reps or MSLs, not decided", "body": deck})
        self.assertEqual((g["decision"], g["status"], g["status_basis"]),
                         ("treat_as_promo", "findings_only", "provisional"))
        self.assertIn("users", g["pending"])
        self.assertTrue(g["provisional_label"].startswith("provisional: treat as promotional — pending:"))
        self.assertIn("who will use it", g["provisional_label"])
        self.assertTrue(any("Who will use or present it" in q for q in g["questions"]))
        self.assertEqual(g["users"], "unknown")
        g = gate({"channel": "promo", "proactive_or_reactive": "proactive", "users": "undecided", "body": deck})
        self.assertEqual(g["provisional_label"], "provisional: treat as promotional — pending: who will use it")
        self.assertEqual(g["pending"], ["users"])
        g = gate({"branded": True, "product_claims_present": True, "users": "unknown"})
        self.assertEqual((g["decision"], g["status_basis"]), ("treat_as_promo", "provisional"))
        g = gate({"body": "In response to your enquiry, please find the requested information."})
        self.assertEqual((g["decision"], g["status_basis"]), ("treat_as_med_info", "provisional"))
        # Known users are recorded, never classify, and add no pending item.
        g = gate({"channel": "promo", "proactive_or_reactive": "proactive", "users": "sales reps", "body": deck})
        self.assertEqual((g["status_basis"], g["pending"], g["users"]), ("final", [], "sales reps"))
        # Direction 2: no signal for any reading -> still missing inputs (no invented reading).
        g = gate({"users": "undecided", "body": "Slides attached."})
        self.assertEqual((g["decision"], g["status"], g["status_basis"]),
                         ("human_gate_required", "findings_only", "missing_inputs"))
        self.assertIsNone(g["provisional_label"])
        self.assertIn("users", g["pending"])
        # Conflicting supplied facts still gate (never softened): reactive request answered with promo content;
        # off-label promotional content with no intent; MI letter content pushed proactively.
        self.assertEqual(gate({"proactive_or_reactive": "reactive", "users": "unknown", "body": deck})["status"],
                         "human_gate_required")
        self.assertEqual(gate({"offlabel_or_unlicensed": "yes", "users": "unknown", "body": deck})["status"],
                         "human_gate_required")
        self.assertEqual(gate({"proactive_or_reactive": "proactive",
                               "body": "In response to your enquiry, see attached."})["status"],
                         "human_gate_required")
        # A provisional decision is never a final one and the gate never approves.
        self.assertFalse(gate({"users": "unknown", "body": deck})["ok"])


    def test_channel_gate_provisional_reading(self):
        """TEH-RDY-064: when supplied content or the person's description carries a reading, the gate
        returns a provisional reading (optional `provisional_reading`), including non-promotional
        (disease awareness / corporate); decision values unchanged."""
        from channel_intent_gate import gate

        allowed = {"human_gate_required", "treat_as_promo", "treat_as_scientific_exchange", "treat_as_med_info"}
        label = "provisional: non-promotional (disease awareness / corporate) — pending:"
        # Direction 1a: unbranded disease-awareness slides, presenter unknown -> non-promotional provisional.
        g = gate({"users": "unknown", "body": "Unbranded disease awareness slides. Recognizing early signs."})
        self.assertEqual((g["status"], g["status_basis"]), ("findings_only", "provisional"))
        self.assertTrue(g["provisional_reading"].startswith(label), g["provisional_reading"])
        self.assertIn("who will use it", g["provisional_reading"])
        self.assertIn(g["decision"], allowed)
        # 1b: derived fields alone (unbranded, no product claims) carry the reading.
        g = gate({"branded": False, "product_claims_present": False})
        self.assertTrue(g["provisional_reading"].startswith(label))
        # 1c: person's description (no text) names the piece.
        g = gate({"described_as": "non-branded disease awareness deck", "users": "not decided"})
        self.assertTrue(g["provisional_reading"].startswith(label))
        g = gate({"described_as": "a med-info letter"})
        self.assertEqual((g["decision"], g["status_basis"]), ("treat_as_med_info", "provisional"))
        self.assertTrue(g["provisional_reading"].startswith("provisional: treat as medical information — pending:"))
        g = gate({"described_as": "scientific exchange deck"})
        self.assertEqual(g["decision"], "treat_as_scientific_exchange")
        # provisional_reading mirrors the provisional label for treat_as_* readings.
        g = gate({"users": "unknown", "body": "Product X: superior efficacy. Prescribe today."})
        self.assertEqual(g["provisional_reading"], g["provisional_label"])
        # Direction 2: no reading -> no provisional reading, still missing inputs.
        for args in ({"body": "Slides attached."}, {"described_as": "slides"}, {}):
            g = gate(args)
            self.assertEqual((g["status_basis"], g["provisional_reading"]), ("missing_inputs", None), args)
        # A description supporting two readings is mixed -> human gate (TEH-RDY-061), not provisional.
        g = gate({"described_as": "promotional leave-behind with MI letter fragments"})
        self.assertEqual((g["status"], g["provisional_reading"]), ("human_gate_required", None))
        g = gate({"described_as": "branded disease awareness deck"})
        self.assertEqual(g["status"], "human_gate_required")
        # Conflicting facts still gate; a description never becomes the declared intent; final stays final.
        self.assertEqual(gate({"described_as": "med-info letter", "proactive_or_reactive": "proactive"})["status"],
                         "human_gate_required")
        self.assertIn("channel", gate({"described_as": "med-info letter"})["gaps"])
        g = gate({"channel": "promo", "proactive_or_reactive": "proactive", "body": "Unbranded disease awareness."})
        self.assertEqual((g["decision"], g["status_basis"], g["provisional_reading"]), ("treat_as_promo", "final", None))
        # Off-label content never gets a non-promotional provisional reading.
        g = gate({"branded": False, "product_claims_present": False, "offlabel_or_unlicensed": "yes"})
        self.assertIsNone(g["provisional_reading"])


if __name__ == "__main__":
    unittest.main()
