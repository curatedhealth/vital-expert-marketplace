#!/usr/bin/env python3
"""Tests for plain_language_scan.py and compare_numbers.py. Run: python test_scripts.py"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compare_numbers import compare, extract  # noqa: E402
from plain_language_scan import scan, split_sentences, syllables  # noqa: E402

CLINICIAN_LETTER = (
    "Orzenta is indicated for adults with moderate hypertension. In the pivotal randomized "
    "trial, the incidence of adverse events was comparable to placebo, and efficacy was "
    "maintained at week 52 in patients receiving concomitant therapy with an ACE inhibitor. "
    "Do not take it if your eGFR is <30 mL/min. "
    "There is nothing to worry about."
)

PLAIN_LETTER = (
    "Orzenta is a medicine for high blood pressure (hypertension). "
    "You take one tablet each morning. "
    "Tell your doctor or pharmacist about all the other medicines you take."
)


class PlainLanguageScanTests(unittest.TestCase):
    def test_sentence_split_keeps_decimals_and_eg(self):
        sents = split_sentences("Take 2.5 mg daily, e.g. with food. Then stop.")
        self.assertEqual(len(sents), 2)
        self.assertIn("2.5 mg", sents[0])

    def test_syllables_rough(self):
        self.assertEqual(syllables("tablet"), 2)
        self.assertGreaterEqual(syllables("hypertension"), 4)

    def test_clinician_letter_flags(self):
        r = scan(CLINICIAN_LETTER, max_words=20)
        terms = {t["term"] for t in r["clinician_terms"]}
        for expected in ["indicated for", "hypertension", "randomized", "incidence",
                         "adverse event", "placebo", "efficacy", "concomitant"]:
            self.assertIn(expected, terms)
        self.assertGreaterEqual(r["sentence_length"]["over_threshold"], 1)
        self.assertIn("<", r["symbols"])
        abbrevs = {a["abbreviation"]: a for a in r["abbreviations"]}
        self.assertIn("ACE", abbrevs)
        self.assertFalse(abbrevs["ACE"]["spelled_out_at_first_use"])
        self.assertIn("eGFR", abbrevs)
        tone = {t["term"] for t in r["tone_terms"]}
        self.assertIn("nothing to worry about", tone)

    def test_plain_letter_quiet(self):
        r = scan(PLAIN_LETTER, max_words=20)
        self.assertEqual(r["sentence_length"]["over_threshold"], 0)
        self.assertEqual(r["tone_terms"], [])
        self.assertEqual(r["symbols"], [])
        # Lay term first, medical term in brackets after: still listed, as a prompt.
        self.assertIn("hypertension", {t["term"] for t in r["clinician_terms"]})

    def test_abbreviation_spelled_out(self):
        r = scan("Your HbA1c (a blood test for average sugar) was taken. HbA1c fell.")
        a = {x["abbreviation"]: x for x in r["abbreviations"]}
        self.assertTrue(a["HbA1c"]["spelled_out_at_first_use"])
        self.assertEqual(a["HbA1c"]["count"], 2)
        r2 = scan("Chronic kidney disease (CKD) is common.")
        self.assertTrue(r2["abbreviations"][0]["spelled_out_at_first_use"])

    def test_no_score_given(self):
        r = scan(PLAIN_LETTER)
        self.assertNotIn("score", {k.lower() for k in r})


class CompareNumbersTests(unittest.TestCase):
    def test_locale_notation_is_not_a_change(self):
        src = "Take 2.5 mg twice daily. 1,200 patients; 12.0% vs 20.0%."
        tgt = "Nehmen Sie zweimal täglich 2,5 mg. 1.200 Patienten; 12,0 % vs. 20,0 %."
        r = compare(src, tgt, "en", "de")
        self.assertEqual(r["missing_from_translation"], [])
        self.assertEqual(r["added_in_translation"], [])
        self.assertEqual(r["unit_changes"], [])

    def test_changed_value_found(self):
        src = "Events fell from 9.0% to 6.0% by week 52."
        tgt = "Die Ereignisse sanken bis Woche 52 von 9,0 % auf 5,0 %."
        r = compare(src, tgt, "en", "de")
        self.assertEqual([m["value"] for m in r["missing_from_translation"]], [6])
        self.assertEqual([a["value"] for a in r["added_in_translation"]], [5])

    def test_unit_change_found(self):
        src = "The dose is 50 mg."
        tgt = "Die Dosis beträgt 50 µg."
        r = compare(src, tgt, "en", "de")
        self.assertEqual(len(r["unit_changes"]), 1)
        self.assertEqual(r["unit_changes"][0]["original_unit"], "mg")

    def test_rounding_found(self):
        src = "HR 0.66 (95% CI 0.45 to 0.97)"
        tgt = "HR 0,7 (95-%-KI 0,45 bis 0,97)"
        r = compare(src, tgt, "en", "de")
        self.assertIn(0.66, [m["value"] for m in r["missing_from_translation"]])
        self.assertIn(0.7, [a["value"] for a in r["added_in_translation"]])

    def test_swiss_apostrophe_grouping(self):
        r = compare("1,200 patients", "1'200 Patienten", "en", "de")
        self.assertEqual(r["missing_from_translation"], [])

    def test_extract_units_canonical(self):
        items = extract("5 mcg and 10 ml", "en")
        self.assertEqual([i["unit"] for i in items], ["µg", "mL"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
