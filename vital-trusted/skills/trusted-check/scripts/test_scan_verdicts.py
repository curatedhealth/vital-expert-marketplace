#!/usr/bin/env python3
"""Tests for scan_verdicts.py. Run: python test_scan_verdicts.py"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_verdicts import CLOSING, scan  # noqa: E402

CLEAN = f"""TRUSTED check: HCP email copy from the agency, for doctors. Draft, not yet reviewed.

Before it goes, fix these 5 things. Your promotional review process decides whether it can be used.

Tangible        nothing flagged in what was checked
Rule-compliant  2 to fix
                "Most effective" compares with other treatments; nothing you supplied compares them directly.
Unbiased        1 to fix
Safe            not checked: no approved label was supplied for the tolerability statement
True            2 missing
                Confidence: 75% of the checked claims are supported by the passages you supplied. This is support from your sources, not proof the statements are true.
Ethical         off by choice
Defensible      uncleared draft

Open for a person
1. The draft mentions dizziness after the first dose. Pass it to your safety reporting procedure.

Off by choice: Safe, Ethical.
{CLOSING}
"""


def kinds(text):
    return sorted({hit["why"] for hit in scan(text)})


class ScanTests(unittest.TestCase):
    def test_clean_summary_has_no_hits(self):
        self.assertEqual(scan(CLEAN), [])

    def test_verdict_words_are_found(self):
        for phrase in ["Looks good to go.", "Safe to send.", "Fair balance: compliant.",
                       "The draft is accurate.", "Ready for approval.", "TRUSTED score: 86/100",
                       "All clear.", "It passed the check.", "Approved."]:
            with self.subTest(phrase=phrase):
                hits = [h for h in scan(phrase + "\n" + CLOSING) if h["kind"] == "verdict"]
                self.assertTrue(hits, phrase)

    def test_letter_words_are_allowed(self):
        text = "Safe            nothing flagged\nTrue            1 missing\nRule-compliant  1 to fix\nEthical         off by choice\n" + CLOSING
        self.assertEqual(scan(text), [])

    def test_negated_truth_is_allowed(self):
        text = "This is support from your sources, not proof the statements are true.\n" + CLOSING
        self.assertEqual(scan(text), [])

    def test_pass_it_to_is_allowed(self):
        text = "Pass it to your safety reporting procedure.\n" + CLOSING
        self.assertEqual(scan(text), [])

    def test_codes_are_found(self):
        for phrase in ["R · claims-and-label: 1", "See TR-H6.", "[GAP: not supplied — x — y]",
                       "T  Tangible  2 flags", "True · numbers: 3 figures looked at"]:
            with self.subTest(phrase=phrase):
                hits = [h for h in scan(phrase + "\n" + CLOSING) if h["kind"] == "code"]
                self.assertTrue(hits, phrase)

    def test_codes_allowed_in_detail_section(self):
        text = CLEAN + "\nDetail for reviewers\nTrue · numbers: 3 figures looked at, 1 differ from the source (not tool-checked)\n"
        self.assertEqual(scan(text), [])

    def test_missing_closing_statement(self):
        self.assertIn("closing statement missing or altered", kinds("Tangible  nothing flagged\n"))

    def test_altered_closing_statement(self):
        self.assertIn("closing statement missing or altered",
                      kinds("This check flags issues. It is not legal review.\n"))

    def test_closing_not_last(self):
        self.assertIn("closing statement is not the last line", kinds(CLOSING + "\nOne more line.\n"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
