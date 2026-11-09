#!/usr/bin/env python3
"""Tests for faithfulness.py (counts by manual result, no percentage).

Run: python3 test_faithfulness.py
"""
import json
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "faithfulness.py")
BANNED = ("%", "percent", "supported", "unsupported", "contradicted", "unverifiable",
          "out_of_scope", "VERIFY")


def run(args, stdin=None):
    p = subprocess.run([sys.executable, "-I", SCRIPT] + args, input=stdin,
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


class Counts(unittest.TestCase):
    def test_counts_printed_back_with_zeros(self):
        code, out, _ = run(["--found", "4", "--partly", "1", "--not-found", "1", "--not-factual", "2"])
        self.assertEqual(code, 0)
        self.assertIn("6 factual claims", out)
        self.assertIn("Listed separately, not in the total: 2", out)
        self.assertIn("Your passage says something different", out)
        self.assertIn("Open items: 2", out)

    def test_no_percentage_and_no_tool_words(self):
        code, out, _ = run(["--found", "6", "--partly", "2", "--not-found", "1"])
        self.assertEqual(code, 0)
        for banned in BANNED:
            self.assertNotIn(banned, out.replace("No confidence figure", ""))
        self.assertIn("No confidence figure", out)
        self.assertIn("not tool-checked", out)

    def test_json_has_no_confidence_figure(self):
        code, out, _ = run(["--found", "3", "--json"])
        data = json.loads(out)
        self.assertIsNone(data["confidence_figure"])
        self.assertNotIn("faithfulness_percent", data)

    def test_words_file_reads_manual_words(self):
        words = ["Found in your passage", "Partly found: dose not in your passage",
                 "Not found in your passage", "Your passage says something different",
                 "No passage to compare with",
                 "Opinion, recommendation or definition"]
        code, out, _ = run(["--words-file", "-", "--json"], stdin=json.dumps(words))
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(sorted(data["counts"].values()), [1] * 6)
        self.assertEqual(data["open_items"], 4)

    def test_unknown_word_stops(self):
        code, _, err = run(["--words-file", "-"], stdin=json.dumps(["supported"]))
        self.assertNotEqual(code, 0)
        self.assertIn("Unknown manual result word", err)

    def test_recommendation_follows_most_serious_open_item(self):
        _, out, _ = run(["--found", "2", "--partly", "1", "--different", "1"])
        self.assertIn("Ask the person which is right", out)

    def test_no_open_items(self):
        _, out, _ = run(["--found", "3"])
        self.assertIn("No open items", out)

    def test_header_equals_sum_of_rows(self):
        _, out, _ = run(["--found", "5", "--partly", "1", "--not-found", "1",
                         "--no-passage", "1", "--not-factual", "1", "--json"])
        data = json.loads(out)
        factual = sum(v for k, v in data["counts"].items() if k != "not_factual")
        self.assertEqual(data["factual_claims"], factual)
        self.assertEqual(data["factual_claims"], 8)
        self.assertEqual(data["not_factual_listed_separately"], 1)

    def test_negative_count_stops(self):
        code, _, _ = run(["--found", "-1"])
        self.assertNotEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
