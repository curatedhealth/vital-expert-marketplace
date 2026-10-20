#!/usr/bin/env python3
"""Tests for chart_scale.py and find_framing_cues.py. Run: python test_scripts.py"""
import json
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable


def run(script, *args, stdin=None):
    r = subprocess.run([PY, "-I", os.path.join(HERE, script), *args],
                       input=stdin, capture_output=True, text=True)
    return r


class ChartScale(unittest.TestCase):
    def j(self, *args):
        r = run("chart_scale.py", *args, "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    def test_axis_from_80(self):
        d = self.j("--axis-min", "80", "--value", "84", "--value", "88")["bars"]
        self.assertAlmostEqual(d["actual_ratio"], 1.0476, places=3)
        self.assertEqual(d["displayed_ratio"], 2.0)
        self.assertAlmostEqual(d["actual_change_pct"], 4.76, places=2)
        self.assertEqual(d["displayed_change_pct"], 100.0)
        self.assertEqual(d["looks_larger_by"], 21.0)

    def test_axis_from_zero_no_distortion(self):
        d = self.j("--value", "84", "--value", "88")["bars"]
        self.assertEqual(d["looks_larger_by"], 1.0)

    def test_plotted_range_share(self):
        d = self.j("--axis-min", "80", "--axis-max", "90", "--value", "84", "--value", "88")["bars"]
        self.assertEqual(d["difference_share_of_plotted_range_pct"], 40.0)

    def test_value_below_axis_rejected(self):
        r = run("chart_scale.py", "--axis-min", "85", "--value", "84", "--value", "88")
        self.assertNotEqual(r.returncode, 0)

    def test_icons_both_dimensions(self):
        d = self.j("--value", "10", "--value", "20", "--icon-scaling", "both")["icons"]
        self.assertEqual(d["apparent_size_ratio"], 4.0)
        self.assertEqual(d["looks_larger_by"], 2.0)

    def test_icons_height_only(self):
        d = self.j("--value", "10", "--value", "20", "--icon-scaling", "height")["icons"]
        self.assertEqual(d["apparent_size_ratio"], 2.0)

    def test_cumulative(self):
        d = self.j("--cumulative", "410,805,1193")["cumulative"]
        self.assertEqual(d["per_period"], [410.0, 395.0, 388.0])
        self.assertEqual(d["periods_where_per_period_fell"], [2, 3])

    def test_needs_input(self):
        r = run("chart_scale.py")
        self.assertNotEqual(r.returncode, 0)


class FramingCues(unittest.TestCase):
    def j(self, text):
        r = run("find_framing_cues.py", "-", "--json", stdin=text)
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    def test_certainty_words(self):
        d = self.j("KELNA-1 proves Velostra is superior, a dramatic breakthrough.")
        words = {h["match"].lower() for h in d["hits"] if h["group"] == "certainty"}
        self.assertTrue({"proves", "superior", "dramatic", "breakthrough"} <= words)

    def test_stacked_hedges(self):
        d = self.j("Results may suggest that it could potentially reduce flares.")
        self.assertEqual(len(d["stacked_hedges"]), 1)
        self.assertGreaterEqual(d["stacked_hedges"][0]["hedges"], 3)

    def test_single_hedge_not_stacked(self):
        d = self.j("The subgroup result may reflect chance.")
        self.assertEqual(d["stacked_hedges"], [])

    def test_minimizing(self):
        d = self.j("Only 2% of patients had bleeding requiring hospitalization.")
        self.assertEqual(d["counts"]["minimizing"], 1)

    def test_interest_words(self):
        d = self.j("An independent study, funded by Example Pharma, and data on file.")
        words = {h["match"].lower() for h in d["hits"] if h["group"] == "interest"}
        self.assertTrue({"independent", "funded by", "data on file"} <= words)

    def test_significant_with_p_not_flagged(self):
        d = self.j("The difference was significant (p = 0.01).")
        self.assertEqual(d["counts"]["certainty"], 0)

    def test_statistically_significant_not_flagged(self):
        d = self.j("The difference was not statistically significant.")
        self.assertEqual(d["counts"]["certainty"], 0)

    def test_highly_significant_flagged(self):
        d = self.j("A highly significant reduction in flares.")
        self.assertGreaterEqual(d["counts"]["certainty"], 1)

    def test_clean_text(self):
        d = self.j("Flares occurred in 32% versus 47% of patients by week 24.")
        self.assertEqual(sum(d["counts"].values()), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
