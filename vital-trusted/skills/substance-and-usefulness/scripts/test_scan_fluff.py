#!/usr/bin/env python3
"""Tests for scan_fluff.py. Run: python scripts/test_scan_fluff.py"""

import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scan_fluff  # noqa: E402

BOARD = (
    "In today's rapidly evolving healthcare landscape, we continue to leverage synergies.\n"
    "Key stakeholders have shown strong interest and we expect listing soon.\n"
    "We may potentially see somewhat better uptake going forward.\n"
    "Tavrelo net sales were CHF 2.4 million in Q3 against a plan of CHF 2.9 million.\n"
    "Tavrelo net sales in Q3 were CHF 2.4 million, against plan of CHF 2.9 million.\n"
)


def kinds(text, **kw):
    return scan_fluff.scan(text, **kw)["counts"]


class ScanTests(unittest.TestCase):
    def test_buzzwords_found(self):
        hits = [h for h in scan_fluff.scan(BOARD)["hits"] if h["kind"] == "buzzword"]
        terms = sorted(h["term"] for h in hits)
        self.assertEqual(terms, ["landscape", "leverage", "synergies"])

    def test_opener_found(self):
        self.assertEqual(kinds(BOARD).get("throat-clearing opening"), 1)

    def test_vague_words(self):
        hits = [h["term"] for h in scan_fluff.scan(BOARD)["hits"] if h["kind"] == "vague word"]
        for t in ["key stakeholders", "strong", "soon", "going forward"]:
            self.assertIn(t, hits)
        # "stakeholders" inside "key stakeholders" is not counted twice
        self.assertNotIn("stakeholders", hits)

    def test_stacked_hedges(self):
        self.assertEqual(kinds(BOARD).get("stacked hedges"), 1)

    def test_near_duplicate(self):
        dups = [h for h in scan_fluff.scan(BOARD)["hits"] if h["kind"] == "near-duplicate"]
        self.assertEqual(len(dups), 1)
        self.assertEqual((dups[0]["line"], dups[0]["other_line"]), (4, 5))

    def test_clean_text(self):
        clean = ("Q3 net sales were CHF 2.4 million against plan of CHF 2.9 million.\n"
                 "The board is asked to approve two field hires by 15 November 2026.\n")
        self.assertEqual(kinds(clean), {})

    def test_word_boundaries(self):
        # "strongest" and "leveraged buyout" style variants: only exact listed forms hit
        c = kinds("The strongest signal came in week 2.")
        self.assertNotIn("vague word", c)
        c = kinds("The debt was leveraged.")
        self.assertEqual(c.get("buzzword"), 1)

    def test_hyphen_variants(self):
        hits = [h["term"] for h in scan_fluff.scan("This is a game changer.")["hits"]]
        self.assertTrue(any(t in ("game changer", "game-changer") for t in hits))
        self.assertEqual(kinds("It is end to end.").get("buzzword"), 1)

    def test_bullet_opener(self):
        self.assertEqual(kinds("- It is important to note that sales fell.").get(
            "throat-clearing opening"), 1)

    def test_threshold(self):
        a = "Payer review in canton X remains open on budget impact.\n"
        b = "Payer review remains open in canton X with budget concerns raised.\n"
        self.assertEqual(kinds(a + b, dup_threshold=0.5).get("near-duplicate"), 1)
        self.assertIsNone(kinds(a + b, dup_threshold=0.95).get("near-duplicate"))

    def test_cli_json_stdin(self):
        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scan_fluff.py")
        out = subprocess.run([sys.executable, "-I", script, "-", "--json"], input=BOARD,
                             capture_output=True, text=True, check=True).stdout
        data = json.loads(out)
        self.assertEqual(data["counts"]["buzzword"], 3)
        self.assertIn("prompts to read", data["note"])

    def test_cli_rejects_bad_threshold(self):
        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scan_fluff.py")
        r = subprocess.run([sys.executable, "-I", script, "-", "--dup-threshold", "2"],
                           input="x", capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
