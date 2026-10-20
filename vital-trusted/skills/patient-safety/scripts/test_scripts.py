#!/usr/bin/env python3
"""Tests for scan_safety_mentions.py and label_match.py. Run: python test_scripts.py

Fixtures are invented; "Corvelan" (corvelastat) is fictional.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import label_match  # noqa: E402
import scan_safety_mentions as ssm  # noqa: E402

DOCTOR_EMAIL = """Dear Medical Information,
What is the recommended dose of Corvelan in moderate renal impairment?
PS: one of my patients came out in a rash two weeks after starting Corvelan, and she has
since found out she is pregnant.
Dr. A. Weber"""

MR_TRANSCRIPT = """R3: Honestly it stopped working after a month for two of my patients.
R5: One pen jammed and the patient took a double dose by mistake.
R2: No complaints really, works well."""

LEAFLET_BAD = """Corvelan is completely safe and most people have no side effects.
You can stop taking it once you feel better. If you miss a dose, take two next time."""

LEAFLET_GOOD = """Like all medicines, Corvelan can cause side effects.
If you have any questions, talk to your doctor, nurse or pharmacist."""

LABEL = """4.2 Posology and method of administration
The recommended dose is 20 mg once daily.
Moderate renal impairment (creatinine clearance 30 to 50 mL/min): the recommended dose is 10 mg once daily.
Corvelan must not be used in patients with severe hepatic impairment (Child-Pugh C).
4.6 There are no data from the use of corvelastat in pregnant women."""

DRAFT = """The recommended dose is 20 mg once daily.
In patients with kidney problems the recommended dose is 5 mg once daily.
Corvelan should not be used in patients with severe hepatic impairment (Child-Pugh C).
Corvelan is safe to use with grapefruit juice and no dose adjustment is needed in children."""


class ScanSafety(unittest.TestCase):
    def kinds(self, text, patient=False):
        hits = ssm.scan(text, ssm.PATIENT_KINDS if patient else ssm.SAFETY_KINDS)
        return {h["kind"] for h in hits}

    def test_doctor_email_finds_side_effect_and_pregnancy(self):
        k = self.kinds(DOCTOR_EMAIL)
        self.assertIn("possible side effect", k)
        self.assertIn("pregnancy or breastfeeding", k)

    def test_transcript_finds_lack_of_effect_quality_and_overdose(self):
        k = self.kinds(MR_TRANSCRIPT)
        self.assertIn("lack of effect", k)
        self.assertIn("product quality", k)
        self.assertIn("overdose, misuse or abuse", k)

    def test_patient_bad_leaflet(self):
        k = self.kinds(LEAFLET_BAD, patient=True)
        self.assertIn("reassurance not to state unless the leaflet does", k)
        self.assertIn("advice about treatment", k)
        self.assertFalse(any(ssm.ROUTE.search(l) for l in LEAFLET_BAD.splitlines()))

    def test_patient_good_leaflet_has_route(self):
        self.assertTrue(any(ssm.ROUTE.search(l) for l in LEAFLET_GOOD.splitlines()))
        self.assertNotIn("advice about treatment", self.kinds(LEAFLET_GOOD, patient=True))


class LabelMatch(unittest.TestCase):
    def setUp(self):
        self.res = label_match.compare(LABEL, DRAFT)

    def by_start(self, start):
        return next(r for r in self.res if r["draft"].startswith(start))

    def test_verbatim(self):
        self.assertEqual(self.by_start("The recommended dose is 20").get("result"), "word for word")

    def test_changed_dose_is_close_with_number_diff(self):
        r = self.by_start("In patients with kidney")
        self.assertEqual(r["result"], "close")
        self.assertIn("5mg", r["numbers_only_in_draft"])
        self.assertIn("10mg", r["numbers_only_in_label"])

    def test_softened_contraindication_shows_term_diff(self):
        r = self.by_start("Corvelan should not")
        self.assertEqual(r["result"], "close")
        self.assertIn("must not", r["terms_only_in_label"])
        self.assertIn("should not", r["terms_only_in_draft"])

    def test_partial_quote_is_marked(self):
        r = label_match.compare(LABEL, "Corvelan must not be used in patients.")[0]
        self.assertEqual(r["result"], "word for word")
        self.assertTrue(r.get("part_of_longer_label_sentence"))

    def test_invented_statement_not_found(self):
        r = self.by_start("Corvelan is safe to use")
        self.assertEqual(r["result"], "not found in the supplied label")


if __name__ == "__main__":
    unittest.main(verbosity=2)
