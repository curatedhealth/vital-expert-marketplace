#!/usr/bin/env python3
"""Tests for assemble_report.py. Run: python3 test_assemble_report.py"""
import copy
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble_report as ar  # noqa: E402

FIX = HERE.parent / "evals" / "dd-integrated-report" / "fixtures"
TEMPLATE = HERE.parent / "templates" / "integrated-diligence-report.md"


class Work:
    """A temporary copy of a fixture folder that a test can edit."""

    def __init__(self, scenario="all-clear"):
        self.dir = Path(tempfile.mkdtemp())
        shutil.copytree(FIX / scenario, self.dir / "w")
        self.dir = self.dir / "w"

    def load(self, name):
        return json.loads((self.dir / name).read_text())

    def save(self, name, obj):
        (self.dir / name).write_text(json.dumps(obj))

    def edit(self, name, fn):
        o = self.load(name)
        fn(o)
        self.save(name, o)

    def run(self, **kw):
        return ar.run(str(self.dir / "manifest.json"), **kw)

    def asset(self, **kw):
        return self.run(**kw)["assets"][0]


def ws(a, code):
    return next(w for w in a["workstreams"] if w["code"] == code)


class TestPointers(unittest.TestCase):
    def test_walk_by_index_and_id(self):
        o = {"rows": [{"id": "R1", "x": 1}, {"id": "R2", "x": 2}], "a": {"b": [5, 6]}}
        self.assertEqual(ar.walk_path(o, "rows[1].x"), (True, 2))
        self.assertEqual(ar.walk_path(o, "rows[R2].x"), (True, 2))
        self.assertEqual(ar.walk_path(o, "a.b[0]"), (True, 5))

    def test_walk_failures(self):
        o = {"rows": [{"id": "R1"}], "a": 1}
        for p in ("rows[3]", "rows[R9]", "zzz", "a.b", "rows.x"):
            self.assertFalse(ar.walk_path(o, p)[0], p)

    def test_root_pointer_and_manifest_pointer(self):
        w = Work("missing-output")
        a = w.asset()
        self.assertTrue(all(g["pointer"].startswith("MANIFEST:") for g in a["open_gaps"]))
        _, stores = ar.load_manifest(str(w.dir / "manifest.json"))
        s = stores[0]
        self.assertTrue(s.resolve("A:")[0])
        self.assertTrue(s.resolve("MANIFEST:E")[0])
        self.assertFalse(s.resolve("MANIFEST:A")[0])
        self.assertFalse(s.resolve("Z:rows")[0])


class TestStatus(unittest.TestCase):
    def test_all_clear_is_green_everywhere(self):
        a = Work().asset()
        self.assertEqual([w["proposed_status"] for w in a["workstreams"]], ["green"] * 9)
        self.assertEqual(a["conflicts"], [])
        self.assertEqual(len(a["conflict_checks"]), 11)

    def test_open_signoff_is_yellow(self):
        w = Work()
        w.edit("A.json", lambda o: o.update(reviewer=None))
        self.assertEqual(ws(w.asset(), "A")["proposed_status"], "yellow")

    def test_gap_is_yellow_and_listed_with_what_it_blocks(self):
        w = Work()
        w.edit("C.json", lambda o: o.update(gaps=[{"field": "f", "missing": "file wrapper", "why_it_matters": "FM cannot be read"}]))
        a = w.asset()
        self.assertEqual(ws(a, "C")["proposed_status"], "yellow")
        g = a["open_gaps"][0]
        self.assertEqual((g["workstream"], g["pointer"], g["missing"]), ("C", "C:gaps[0]", "file wrapper"))
        self.assertIn("D requires it", g["blocks"])

    def test_check_item_counts(self):
        w = Work()
        w.edit("E.json", lambda o: o.update(note="[CHECK] filed page not registered"))
        c = ws(w.asset(), "E")
        self.assertEqual(c["counts"]["check_items"], 1)
        self.assertEqual(c["proposed_status"], "yellow")

    def test_two_triggered_is_red_one_is_yellow(self):
        w = Work()
        w.edit("D.json", lambda o: o.update(failure_mode_screen=[{"id": "RL-01", "state": "triggered", "register_ref": "risks[K1]"}, {"id": "RL-02", "state": "not triggered"}]))
        self.assertEqual(ws(w.asset(), "D")["proposed_status"], "yellow")
        w.edit("D.json", lambda o: o["failure_mode_screen"].__setitem__(1, {"id": "RL-02", "state": "triggered", "register_ref": "risks[K1]"}))
        self.assertEqual(ws(w.asset(), "D")["proposed_status"], "red")

    def test_five_gaps_is_red(self):
        w = Work()
        w.edit("G.json", lambda o: o.update(gaps=[{"field": str(i), "missing": "m", "why_it_matters": "w"} for i in range(5)]))
        self.assertEqual(ws(w.asset(), "G")["proposed_status"], "red")

    def test_thresholds_override(self):
        w = Work()
        w.edit("G.json", lambda o: o.update(gaps=[{"field": "1", "missing": "m", "why_it_matters": "w"}]))
        self.assertEqual(ws(w.asset(thresholds={"red_gaps": 1}), "G")["proposed_status"], "red")
        self.assertEqual(ws(w.asset(), "G")["proposed_status"], "yellow")

    def test_rule_text_names_the_counts(self):
        w = Work()
        w.edit("G.json", lambda o: o.update(gaps=[{"field": "1", "missing": "m", "why_it_matters": "w"}]))
        self.assertIn("1 open GAP(s)", ws(w.asset(), "G")["rule_applied"])

    def test_confirmation_field_is_pending(self):
        a = Work().asset()
        self.assertTrue(all(x["deal_lead_confirmation"] == "PENDING" and x["deal_lead_status"] is None for x in a["workstreams"]))


class TestMissing(unittest.TestCase):
    def test_missing_outputs_are_gaps_with_consequence_and_routing(self):
        a = Work("missing-output").asset()
        for code in ("E", "G"):
            x = ws(a, code)
            self.assertFalse(x["present"])
            self.assertEqual(x["proposed_status"], "red")
            self.assertTrue(x["consequence"])
            self.assertTrue(x["route_to"])
        g = [g for g in a["open_gaps"] if g["kind"] == "missing output"]
        self.assertEqual(sorted(x["workstream"] for x in g), ["E", "G"])
        self.assertEqual(next(x for x in g if x["workstream"] == "G")["route_to"], "evaluate-market-opportunity-and-competitive-position")

    def test_report_still_assembles_and_says_what_is_blocked(self):
        a = Work("missing-output").asset()
        self.assertIn("2 workstream output(s) missing", a["answer"][1]["text"])
        self.assertIn("H requires it", next(g for g in a["open_gaps"] if g["workstream"] == "G")["blocks"])

    def test_null_path_equals_absent(self):
        w = Work()
        m = w.load("manifest.json")
        m["assets"][0]["outputs"]["G"] = None
        w.save("manifest.json", m)
        self.assertFalse(ws(w.asset(), "G")["present"])

    def test_missing_file_is_an_error(self):
        w = Work()
        (w.dir / "G.json").unlink()
        with self.assertRaises(ar.ReportError) as c:
            w.run()
        self.assertEqual(c.exception.code, "E_MANIFEST")


class TestRevenueWorkstream(unittest.TestCase):
    """Ninth workstream R (revenue and price ranges): R-CONF-6 and R-CONF-7, added 7 November 2026."""

    def conflicts(self, a, rule, status="conflict"):
        return [k for k in a["conflicts"] if k["rule"] == rule and k["status"] == status]

    def test_conflict_scenario_has_both_new_rules(self):
        a = Work("conflict").asset()
        self.assertTrue(self.conflicts(a, "R-CONF-6"))
        self.assertTrue(self.conflicts(a, "R-CONF-7"))
        k = self.conflicts(a, "R-CONF-6")[0]
        self.assertIn("early launch 2029", k["detail"])
        self.assertEqual((k["left"]["workstream"], k["right"]["workstream"]), ("R", "B"))
        self.assertEqual(self.conflicts(a, "R-CONF-7")[0]["right"]["workstream"], "C")

    def test_all_clear_has_no_new_conflict(self):
        a = Work("all-clear").run()["assets"][0]
        self.assertFalse(self.conflicts(a, "R-CONF-6") or self.conflicts(a, "R-CONF-7"))
        checks = {c["rule"]: c["status"] for c in a["conflict_checks"]}
        self.assertEqual((checks["R-CONF-6"], checks["R-CONF-7"]), ("no conflict", "no conflict"))

    def test_missing_r_is_red_gap_and_pairs_not_comparable(self):
        w = Work("all-clear")
        m = w.load("manifest.json")
        m["assets"][0]["outputs"]["R"] = None
        w.save("manifest.json", m)
        a = w.asset()
        self.assertEqual(ws(a, "R")["proposed_status"], "red")
        checks = {c["rule"]: c["status"] for c in a["conflict_checks"]}
        self.assertEqual((checks["R-CONF-6"], checks["R-CONF-7"]), ("not comparable", "not comparable"))
        self.assertTrue(any(g["workstream"] == "R" and g["route_to"] == "forecast-revenue-and-price-ranges" for g in a["open_gaps"]))

    def test_exclusivity_year_matching_either_c_view_is_no_conflict(self):
        w = Work("all-clear")
        w.edit("R.json", lambda r: r["countries"][0].update(exclusivity_end_year=2038))
        a = w.asset()
        self.assertFalse(self.conflicts(a, "R-CONF-7"))
        w.edit("R.json", lambda r: r["countries"][0].update(exclusivity_end_year=2039))
        self.assertTrue(self.conflicts(w.asset(), "R-CONF-7"))

    def test_country_without_c_market_is_not_comparable_never_conflict(self):
        w = Work("all-clear")
        w.edit("R.json", lambda r: r["countries"].append({"country": "UK", "state": "computed", "launch_year": {"early": 2033, "mid": 2034, "late": 2036}, "exclusivity_end_year": 2040, "loe_applied": True}))
        a = w.asset()
        uk = [c for c in a["conflicts"] if c["rule"] == "R-CONF-7" and c["status"] == "not comparable"]
        self.assertEqual(len(uk), 1)
        self.assertFalse(self.conflicts(a, "R-CONF-7"))

    def test_gap_country_is_skipped(self):
        w = Work("conflict")
        w.edit("R.json", lambda r: r["countries"][0].update(state="GAP"))
        a = w.asset()
        self.assertFalse(self.conflicts(a, "R-CONF-6") or self.conflicts(a, "R-CONF-7"))


class TestConflicts(unittest.TestCase):
    def conflicts(self, a, rule):
        return [k for k in a["conflicts"] if k["rule"] == rule and k["status"] == "conflict"]

    def test_conflict_scenario_has_all_five_rules(self):
        a = Work("conflict").asset()
        for r in ("R-CONF-1", "R-CONF-2", "R-CONF-3", "R-CONF-4", "R-CONF-5"):
            self.assertTrue(self.conflicts(a, r), r)

    def test_c1_launch_vs_exclusivity_sides_not_reconciled(self):
        k = self.conflicts(Work("conflict").asset(), "R-CONF-1")[0]
        self.assertIn("2034-05-08", k["left"]["text"])
        self.assertIn("2033-03-01", k["right"]["text"])
        self.assertEqual((k["left"]["workstream"], k["right"]["workstream"]), ("B", "C"))
        self.assertNotIn("recommend", json.dumps(k).lower())

    def test_c1_exclusivity_after_high_approval_is_no_conflict(self):
        a = Work().asset()
        self.assertFalse(self.conflicts(a, "R-CONF-1"))

    def test_c1_ends_before_earliest_approval(self):
        w = Work()
        w.edit("C.json", lambda o: o["dates"]["markets"]["US"]["effective"].update(effective_all_patents="2030-01-01"))
        k = self.conflicts(w.asset(), "R-CONF-1")[0]
        self.assertIn("on or before the earliest approval", k["detail"])

    def test_c1_min_years_threshold(self):
        w = Work()
        self.assertFalse(self.conflicts(w.asset(), "R-CONF-1"))
        self.assertTrue(self.conflicts(w.asset(thresholds={"min_years_remaining": 20}), "R-CONF-1"))

    def test_c1_not_comparable_without_b_range(self):
        w = Work()
        w.edit("B.json", lambda o: o.pop("timeline"))
        k = [k for k in w.asset()["conflicts"] if k["rule"] == "R-CONF-1"]
        self.assertEqual(k[0]["status"], "not comparable")

    def test_c2_route_not_listed(self):
        w = Work()
        w.edit("B.json", lambda o: o.update(assumptions={"route": "us_breakthrough", "review_months": 6}))
        self.assertIn("does not map", self.conflicts(w.asset(), "R-CONF-2")[0]["detail"])

    def test_c2_shorter_review_than_d_clock(self):
        w = Work()
        w.edit("B.json", lambda o: o.update(assumptions={"route": "us_standard", "review_months": 6}))
        self.assertIn("verified clock is 10", self.conflicts(w.asset(), "R-CONF-2")[0]["detail"])

    def test_c2_days_clock_converted(self):
        w = Work()
        w.edit("D.json", lambda o: o["routes"].append({"market": "EU", "route": "eu_standard", "disposition": "candidate", "clock": {"days": 210}}))
        w.edit("B.json", lambda o: o.update(assumptions={"route": "eu_standard", "review_months": 5}))
        self.assertTrue(self.conflicts(w.asset(), "R-CONF-2"))
        w.edit("B.json", lambda o: o.update(assumptions={"route": "eu_standard", "review_months": 7}))
        self.assertFalse(self.conflicts(w.asset(), "R-CONF-2"))

    def test_c2_not_comparable_without_assumptions(self):
        w = Work()
        w.edit("B.json", lambda o: o.pop("assumptions"))
        k = [k for k in w.asset()["conflicts"] if k["rule"] == "R-CONF-2"]
        self.assertEqual(k[0]["status"], "not comparable")

    def test_c3_supported_claim_with_no_basis(self):
        w = Work()
        w.edit("G.json", lambda o: o["differentiation"][0].update(basis=[]))
        self.assertIn("no basis", self.conflicts(w.asset(), "R-CONF-3")[0]["detail"])

    def test_c3_unresolved_row(self):
        k = self.conflicts(Work("conflict").asset(), "R-CONF-3")[0]
        self.assertIn("A-R9", k["detail"])

    def test_c3_f_reference_resolves(self):
        w = Work()
        w.edit("G.json", lambda o: o["differentiation"][0].update(basis=[{"kind": "mechanism_register", "ref": "F-P1"}]))
        self.assertFalse(self.conflicts(w.asset(), "R-CONF-3"))

    def test_c3_not_counted_claims_ignored(self):
        w = Work()
        w.edit("G.json", lambda o: o["differentiation"][0].update(state="not counted", basis=[]))
        self.assertFalse(self.conflicts(w.asset(), "R-CONF-3"))

    def test_c4_met_condition_on_gappy_owner(self):
        a = Work("conflict").asset()
        self.assertEqual(len(self.conflicts(a, "R-CONF-4")), 2)

    def test_c4_unmet_condition_on_gappy_owner_is_a_dependency(self):
        w = Work("conflict")
        w.edit("H.json", lambda o: [c.update(state="gap") for c in o["conditions"] if c["owner"].startswith("evaluate-market")])
        a = w.asset()
        self.assertFalse(self.conflicts(a, "R-CONF-4"))
        self.assertTrue([k for k in a["conflicts"] if k["status"] == "dependency"])

    def test_c4_met_condition_on_unsigned_owner(self):
        w = Work()
        w.edit("G.json", lambda o: o.update(reviewer=None))
        self.assertTrue(self.conflicts(w.asset(), "R-CONF-4"))

    def test_c5_licensor_missing_from_chain(self):
        k = self.conflicts(Work("conflict").asset(), "R-CONF-5")[0]
        self.assertIn("Harrowmere", k["left"]["text"])

    def test_c5_matching_licensor_is_clean(self):
        self.assertFalse(self.conflicts(Work().asset(), "R-CONF-5"))


class TestRankAndOptions(unittest.TestCase):
    def test_conflicts_rank_before_failure_modes(self):
        a = Work("conflict").asset()
        kinds = [r["kind"] for r in a["top_risks"]]
        self.assertTrue(kinds[0].startswith("conflict"))
        self.assertEqual(kinds[-1], "triggered failure mode")
        self.assertEqual([r["rank"] for r in a["top_risks"]], list(range(1, len(kinds) + 1)))

    def test_top_n_override(self):
        self.assertEqual(len(Work("conflict").asset(thresholds={"top_n": 2})["top_risks"]), 2)

    def test_h_not_met_condition_is_a_risk(self):
        w = Work()
        w.edit("H.json", lambda o: o["conditions"][0].update(state="not met", detail="2 class flags"))
        a = w.asset()
        self.assertTrue([r for r in a["top_risks"] if r["kind"] == "commercial condition not met"])

    def test_three_options_none_recommended(self):
        a = Work("conflict").asset()
        self.assertEqual([o["option"] for o in a["decision_options"]], ["sign", "sign with conditions", "do not sign"])
        self.assertTrue(all(o["recommended"] is False for o in a["decision_options"]))
        self.assertIsNone(a["recommended_option"])
        self.assertEqual(a["deal_lead_decision"], "PENDING (HUMAN ONLY)")

    def test_sign_conditions_unmet_when_open_items(self):
        sign = Work("conflict").asset()["decision_options"][0]["conditions_that_would_have_to_hold"]
        self.assertFalse(any(c["met"] for c in sign if "conflict" in c["condition"] or "GAP" in c["condition"]))

    def test_sign_conditions_met_when_clear(self):
        sign = Work().asset()["decision_options"][0]["conditions_that_would_have_to_hold"]
        self.assertTrue(all(c["met"] for c in sign[1:4]))

    def test_every_option_condition_has_a_pointer(self):
        for o in Work("conflict").asset()["decision_options"]:
            for key in ("conditions_that_would_have_to_hold", "conditions_precedent", "conditions_present"):
                for c in o.get(key, []):
                    self.assertTrue(c["pointers"])

    def test_report_text_never_recommends(self):
        rep = Work("conflict").run()
        md = ar.render_md(rep).lower()
        self.assertNotIn("we recommend", md)
        self.assertNotIn("recommended: true", json.dumps(rep).lower())


class TestAddedLines(unittest.TestCase):
    def check(self, lines):
        return Work().run(lines=lines)

    def test_valid_line_passes(self):
        r = self.check([{"text": "Row R1 is a randomized trial of 210 patients.", "pointers": ["A:rows[R1]"]}])
        self.assertEqual(len(r["added_lines"]), 1)

    def test_no_pointer_fails(self):
        with self.assertRaises(ar.ReportError) as c:
            self.check([{"text": "Evidence looks strong.", "pointers": []}])
        self.assertEqual(c.exception.code, "E_UNSUPPORTED")

    def test_bad_pointer_fails(self):
        with self.assertRaises(ar.ReportError) as c:
            self.check([{"text": "Trial size 210.", "pointers": ["A:rows[R7]"]}])
        self.assertEqual(c.exception.code, "E_POINTER")

    def test_invented_figure_fails(self):
        with self.assertRaises(ar.ReportError) as c:
            self.check([{"text": "The chance of approval is 90 percent.", "pointers": ["A:rows[R1]"]}])
        self.assertEqual(c.exception.code, "E_UNSUPPORTED")

    def test_recommendation_variants_fail(self):
        for t in ("We recommend signing.", "I advise to sign.", "The deal is safe to sign.", "This should proceed.", "We certify the position.", "The best option is to sign.", "Signing is recommended."):
            with self.assertRaises(ar.ReportError, msg=t) as c:
                self.check([{"text": t, "pointers": ["A:rows[R1]"]}])
            self.assertEqual(c.exception.code, "E_RECOMMEND", t)

    def test_unknown_status_word_in_a_register_fails(self):
        w = Work()
        w.edit("C.json", lambda o: o.update(gaps=[{"field": "x", "missing": "unknown", "why_it_matters": "w"}]))
        with self.assertRaises(ar.ReportError) as c:
            w.run()
        self.assertEqual(c.exception.code, "E_UNKNOWN")


class TestModesAndRollup(unittest.TestCase):
    def test_company_mode_has_two_assets_and_rollup(self):
        r = Work("company-two-assets").run()
        self.assertEqual([a["asset"] for a in r["assets"]], ["FICTIONAL ZX-901", "FICTIONAL ZX-902"])
        m = {x["asset"]: x["statuses"] for x in r["rollup"]["matrix"]}
        self.assertEqual(m["FICTIONAL ZX-902"]["D"], "yellow")
        self.assertEqual(m["FICTIONAL ZX-901"]["D"], "green")

    def test_shared_company_register_is_used_by_each_asset(self):
        r = Work("company-two-assets").run()
        self.assertTrue(all(ws(a, "E")["present"] for a in r["assets"]))

    def test_dates_are_not_merged_across_assets(self):
        r = Work("company-two-assets").run()
        txt = [c["left"]["text"] for a in r["assets"] for c in a["conflict_checks"] if False]
        self.assertEqual(len(r["assets"]), 2)
        self.assertNotIn("merged", json.dumps(r["rollup"]))

    def test_asset_mode_rejects_two_assets(self):
        w = Work("company-two-assets")
        m = w.load("manifest.json")
        m["mode"] = "asset"
        w.save("manifest.json", m)
        with self.assertRaises(ar.ReportError) as c:
            w.run()
        self.assertEqual(c.exception.code, "E_MODE")

    def test_bad_mode_and_duplicate_names(self):
        w = Work()
        m = w.load("manifest.json")
        m["mode"] = "x"
        w.save("manifest.json", m)
        with self.assertRaises(ar.ReportError):
            w.run()
        w = Work("company-two-assets")
        m = w.load("manifest.json")
        m["assets"][1]["name"] = m["assets"][0]["name"]
        w.save("manifest.json", m)
        with self.assertRaises(ar.ReportError):
            w.run()

    def test_bad_date(self):
        w = Work()
        m = w.load("manifest.json")
        m["as_of"] = "07/11/2026"
        w.save("manifest.json", m)
        with self.assertRaises(ar.ReportError) as c:
            w.run()
        self.assertEqual(c.exception.code, "E_DATE")


class TestOutputShape(unittest.TestCase):
    def test_schema_validates_all_scenarios(self):
        sch = json.loads((HERE.parent / "templates" / "integrated-diligence-report.schema.json").read_text())
        for s in ("all-clear", "conflict", "missing-output", "company-two-assets"):
            ar.validate_schema(Work(s).run(), sch)

    def test_schema_rejects_a_recommendation(self):
        sch = json.loads((HERE.parent / "templates" / "integrated-diligence-report.schema.json").read_text())
        r = Work().run()
        r["assets"][0]["decision_options"][0]["recommended"] = True
        with self.assertRaises(ar.ReportError):
            ar.validate_schema(r, sch)
        r = Work().run()
        r["assets"][0]["recommended_option"] = "sign"
        with self.assertRaises(ar.ReportError):
            ar.validate_schema(r, sch)

    def test_three_answer_lines_each_with_pointers(self):
        a = Work("conflict").asset()
        self.assertEqual(len(a["answer"]), 3)
        self.assertTrue(all(l["pointers"] for l in a["answer"]))

    def test_every_pointer_in_the_report_resolves(self):
        w = Work("conflict")
        r = w.run()
        _, stores = ar.load_manifest(str(w.dir / "manifest.json"))
        ar.verify_pointers(r, stores)

    def test_tampered_pointer_is_caught(self):
        w = Work("conflict")
        r = w.run()
        r["assets"][0]["top_risks"][0]["pointers"] = ["A:rows[R99]"]
        _, stores = ar.load_manifest(str(w.dir / "manifest.json"))
        with self.assertRaises(ar.ReportError) as c:
            ar.verify_pointers(r, stores)
        self.assertEqual(c.exception.code, "E_POINTER")

    def test_markdown_headings_match_the_template(self):
        want = [l for l in TEMPLATE.read_text().splitlines() if re.match(r"^## \d\.", l)]
        got = [l for l in ar.render_md(Work().run()).splitlines() if re.match(r"^## \d\.", l)]
        norm = lambda ls: [re.sub(r"\s*\(.*?\)\s*$", "", x).strip() for x in ls]
        self.assertEqual([x.split(" (")[0] for x in got], [x.split(" (")[0] for x in want])

    def test_deterministic(self):
        self.assertEqual(json.dumps(Work("conflict").run(), sort_keys=True), json.dumps(Work("conflict").run(), sort_keys=True))

    def test_no_network_imports(self):
        src = (HERE / "assemble_report.py").read_text()
        for bad in ("import socket", "urllib", "requests", "http.client", "subprocess"):
            self.assertNotIn(bad, src)

    def test_human_only_fields_are_listed_not_scored(self):
        a = Work().asset()
        self.assertIn("fto_opinion", a["human_only_fields"]["C"])
        self.assertEqual(ws(a, "C")["proposed_status"], "green")

    def test_sign_off_block_unsigned_until_reviewed(self):
        w = Work()
        self.assertEqual(w.run()["sign_off"]["status"], "UNSIGNED")
        m = w.load("manifest.json")
        m["reviewed_by"] = "FICTIONAL reviewer"
        w.save("manifest.json", m)
        self.assertIn("DEAL-LEAD DECISION PENDING", w.run()["sign_off"]["status"])


class TestCli(unittest.TestCase):
    def run_cli(self, *a):
        return subprocess.run([sys.executable, str(HERE / "assemble_report.py"), *a], capture_output=True, text=True)

    def test_exit_0_and_files(self):
        w = Work()
        out, md = w.dir / "r.json", w.dir / "r.md"
        r = self.run_cli(str(w.dir / "manifest.json"), "--out", str(out), "--md", str(md))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(json.loads(out.read_text())["assets"])
        self.assertIn("## 1. The answer in three lines", md.read_text())

    def test_exit_1_on_recommendation(self):
        w = Work("attempts")
        r = self.run_cli(str(w.dir / "manifest.json"), "--lines", str(w.dir / "lines-recommend.json"))
        self.assertEqual(r.returncode, 1)
        self.assertIn("E_RECOMMEND", r.stderr)

    def test_exit_1_on_new_finding_and_no_pointer(self):
        w = Work("attempts")
        for f, code in (("lines-new-finding.json", "E_UNSUPPORTED"), ("lines-no-pointer.json", "E_UNSUPPORTED"), ("lines-bad-pointer.json", "E_POINTER")):
            r = self.run_cli(str(w.dir / "manifest.json"), "--lines", str(w.dir / f))
            self.assertEqual(r.returncode, 1, f)
            self.assertIn(code, r.stderr)

    def test_exit_0_on_ok_line(self):
        w = Work("attempts")
        self.assertEqual(self.run_cli(str(w.dir / "manifest.json"), "--lines", str(w.dir / "lines-ok.json")).returncode, 0)

    def test_exit_2_on_usage(self):
        self.assertEqual(self.run_cli().returncode, 2)

    def test_exit_1_on_missing_file(self):
        self.assertEqual(self.run_cli("/nonexistent/manifest.json").returncode, 1)

    def test_thresholds_file(self):
        w = Work()
        w.edit("G.json", lambda o: o.update(gaps=[{"field": "1", "missing": "m", "why_it_matters": "w"}]))
        (w.dir / "t.json").write_text(json.dumps({"red_gaps": 1}))
        out = w.dir / "r.json"
        self.assertEqual(self.run_cli(str(w.dir / "manifest.json"), "--thresholds", str(w.dir / "t.json"), "--out", str(out)).returncode, 0)
        self.assertEqual(ws(json.loads(out.read_text())["assets"][0], "G")["proposed_status"], "red")



class TestAnatomyPointer(unittest.TestCase):
    def test_pointer_syntax(self):
        ok = ar.ANATOMY_PTR
        for good in ("A:rows[R1]", "asset-1/B:probability.overall", "R:countries[US].peak_net_range"):
            self.assertTrue(ok.match(good), good)
        for bad in ("A:", "A:rows R1", "A rows", "A:rows/x", ":x"):
            self.assertFalse(ok.match(bad), bad)


if __name__ == "__main__":
    unittest.main()
