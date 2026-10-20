#!/usr/bin/env python3
"""Tests for scan_language.py. Run: python test_scan_language.py"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_language import scan  # noqa: E402


class ScanTests(unittest.TestCase):
    def phrases(self, text):
        return [h["phrase"].lower() for h in scan(text)]

    def test_campaign_copy(self):
        text = ("Psoriasis sufferers deserve better.\n"
                "Non-compliant patients lose out.\n"
                "Diabetics and the elderly are at risk.")
        p = self.phrases(text)
        self.assertIn("sufferers", p)
        self.assertIn("non-compliant", p)
        self.assertIn("diabetics", p)
        self.assertIn("the elderly", p)

    def test_substance_abuser_not_double_counted(self):
        hits = scan("Support for substance abusers in the community.")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["source"], "U9")

    def test_suffering_from(self):
        self.assertIn("suffering from", self.phrases("Patients suffering from eczema"))

    def test_quotes_marked(self):
        hits = scan('The patient said "I felt like an addict".')
        self.assertTrue(hits[0]["in_quotes"])

    def test_clean_text(self):
        self.assertEqual(scan("People with diabetes can talk to their pharmacist."), [])

    def test_identity_first_not_flagged(self):
        # "disabled people" is an accepted identity-first form; "disabled" as a verb is not about people.
        self.assertEqual(scan("Disabled people told us the button was disabled."), [])

    def test_the_disabled_flagged(self):
        self.assertIn("the disabled", self.phrases("Access for the disabled is limited."))


if __name__ == "__main__":
    unittest.main(verbosity=2)
