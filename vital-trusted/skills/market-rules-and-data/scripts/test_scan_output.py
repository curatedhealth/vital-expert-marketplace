#!/usr/bin/env python3
"""Tests for scan_output.py. Run: python test_scan_output.py"""
import io
import json
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scan_output as so  # noqa: E402

UK_POST = """For UK healthcare professionals only.
Lumivra (lumivrastat) now offers once-monthly dosing.
Prescribing information is available via the link below.
Adverse events should be reported. Reporting forms and information can be found at [Yellow Card link].
"""

NOTES = """Payer raised a case: Mrs Anna Brunner, 67 years old, admitted 14/09/2026.
2 patients in canton X stopped treatment; n = 3 in the subgroup.
Overall 412 patients were enrolled.
Contact: a.brunner@example.org
"""


class Statements(unittest.TestCase):
    def test_uk_cues_found_and_missing(self):
        res = {e["element"]: e["cue_lines"] for e in so.scan_statements(UK_POST, "UK")}
        self.assertEqual(res["audience statement"], [1])
        self.assertEqual(res["prescribing information or where to find it"], [3])
        self.assertEqual(res["side-effect reporting statement"], [4])
        self.assertEqual(res["non-proprietary name"], [2])
        self.assertEqual(res["job code or reference"], [])
        self.assertEqual(res["date of preparation or last revision"], [])

    def test_market_lists_differ(self):
        uk = {e["element"] for e in so.scan_statements("", "UK")}
        ch = {e["element"] for e in so.scan_statements("", "CH")}
        self.assertIn("side-effect reporting statement", uk)
        self.assertNotIn("side-effect reporting statement", ch)
        self.assertIn("authorisation holder name and address", ch)

    def test_unknown_market_lists_only_company_elements(self):
        els = {e["element"] for e in so.scan_statements("", "unknown")}
        self.assertEqual(els, {"job code or reference", "date of preparation or last revision"})


class Data(unittest.TestCase):
    def setUp(self):
        self.hits = so.scan_data(NOTES, 10)
        self.kinds = [h["kind"] for h in self.hits]

    def test_finds_formats(self):
        for k in ("title followed by a name", "age", "date", "email address", "small count"):
            self.assertIn(k, self.kinds)

    def test_never_prints_full_identifier(self):
        blob = json.dumps(self.hits)
        self.assertNotIn("Brunner", blob)
        self.assertNotIn("a.brunner@example.org", blob)

    def test_small_count_cutoff(self):
        smalls = [h["snippet"] for h in self.hits if h["kind"] == "small count"]
        self.assertTrue(any(s.startswith("2 patients") for s in smalls))
        self.assertTrue(any("n = 3" in s for s in smalls))
        self.assertFalse(any("412" in s for s in smalls))

    def test_clean_text(self):
        self.assertEqual(so.scan_data("The payer asked about budget impact in year 2.", 10), [])


class Cli(unittest.TestCase):
    def test_json_output_has_notes(self):
        buf = io.StringIO()
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_tmp_test.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(NOTES)
        try:
            with redirect_stdout(buf):
                so.main([path, "--statements", "--data", "--market", "CH", "--json"])
        finally:
            os.remove(path)
        out = json.loads(buf.getvalue())
        self.assertIn("not a privacy threshold", out["data"]["small_count_note"])
        self.assertIn("does not make a text anonymous", out["data"]["note"])
        self.assertEqual(out["statements"]["market"], "CH")

    def test_no_verdict_words_in_fixed_text(self):
        fixed = " ".join(so.NOTES.values()) + so.DATA_NOTE + so.SMALL_NOTE
        for word in ("compliant", "approved", "anonymized", "safe to", "complete"):
            self.assertNotIn(word, fixed.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
