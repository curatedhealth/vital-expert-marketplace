#!/usr/bin/env python3
"""Tests for faithfulness.py. Run: python3 test_faithfulness.py"""
import json
import re
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "faithfulness.py")


def run(args, stdin=None):
    p = subprocess.run([sys.executable, "-I", SCRIPT] + args, input=stdin,
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def run_json(args, stdin=None):
    code, out, err = run(args + ["--json"], stdin)
    if code != 0:
        raise AssertionError(f"exit {code}: {err}")
    return json.loads(out)


class Faithfulness(unittest.TestCase):
    def test_out_of_scope_left_out_of_denominator(self):
        r = run_json(["--source", "verify", "--supported", "6", "--partial", "2",
                      "--unsupported", "1", "--unverifiable", "1", "--out-of-scope", "3"])
        self.assertEqual(r["denominator"], 10)
        self.assertEqual(r["faithfulness_percent"], 70)  # (6 + 1) / 10, not 7 / 13
        self.assertEqual(r["statements_total"], 13)

    def test_concept_sketch_three_supported_one_unverifiable(self):
        r = run_json(["--source", "verify", "--supported", "3", "--unverifiable", "1"])
        self.assertEqual(r["faithfulness_percent"], 75)

    def test_round_half_up(self):
        # (0 + 0.5) / 4 = 12.5% -> 13 (half up), not 12 (half to even)
        r = run_json(["--source", "verify", "--partial", "1", "--unsupported", "3"])
        self.assertEqual(r["exact_percent"], 12.5)
        self.assertEqual(r["faithfulness_percent"], 13)

    def test_two_thirds(self):
        r = run_json(["--source", "verify", "--supported", "2", "--contradicted", "1"])
        self.assertEqual(r["faithfulness_percent"], 67)

    def test_all_supported(self):
        r = run_json(["--source", "verify", "--supported", "5"])
        self.assertEqual(r["faithfulness_percent"], 100)
        self.assertEqual(r["open_items"], {})

    def test_zero_denominator_only_out_of_scope(self):
        r = run_json(["--source", "verify", "--out-of-scope", "4"])
        self.assertIsNone(r["faithfulness_percent"])
        self.assertIn("not a factual statement", r["reason_no_figure"])

    def test_zero_denominator_nothing(self):
        r = run_json(["--source", "verify", "--supported", "0"])
        self.assertIsNone(r["faithfulness_percent"])
        self.assertIn("no factual statements", r["reason_no_figure"])

    def test_method_only_gives_no_figure(self):
        r = run_json(["--source", "method", "--supported", "4", "--unsupported", "1"])
        self.assertIsNone(r["faithfulness_percent"])
        self.assertIn("not tool-checked", r["reason_no_figure"])
        self.assertEqual(r["counts"]["supported"], 4)

    def test_source_is_required(self):
        code, _, _ = run(["--supported", "1"])
        self.assertNotEqual(code, 0)

    def test_json_list_of_strings_from_stdin(self):
        data = json.dumps(["supported", "Partial", "out-of-scope", "unverifiable"])
        r = run_json(["--source", "verify", "--json-file", "-"], stdin=data)
        self.assertEqual(r["denominator"], 3)
        self.assertEqual(r["faithfulness_percent"], 50)  # (1 + 0.5) / 3

    def test_json_findings_objects(self):
        data = {"findings": [{"claim": "a", "status": "supported"},
                             {"claim": "b", "status": "contradicted"}]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            path = f.name
        try:
            r = run_json(["--source", "verify", "--json-file", path])
        finally:
            os.unlink(path)
        self.assertEqual(r["faithfulness_percent"], 50)
        self.assertEqual(r["open_items"], {"contradicted": 1})
        self.assertIn("contradicts", r["recommendation"])

    def test_unknown_status_rejected(self):
        code, _, err = run(["--source", "verify", "--json-file", "-"], stdin='["true"]')
        self.assertNotEqual(code, 0)
        self.assertIn("Unknown status", err)

    def test_negative_count_rejected(self):
        code, _, _ = run(["--source", "verify", "--supported", "-1"])
        self.assertNotEqual(code, 0)

    def test_counts_and_json_together_rejected(self):
        code, _, _ = run(["--source", "verify", "--supported", "1", "--json-file", "-"], stdin="[]")
        self.assertNotEqual(code, 0)

    def test_recommendation_priority(self):
        r = run_json(["--source", "verify", "--partial", "2", "--unverifiable", "1"])
        self.assertIn("could not be checked", r["recommendation"])

    def test_text_output_has_no_verdict_words(self):
        code, out, _ = run(["--source", "verify", "--supported", "9", "--partial", "1"])
        self.assertEqual(code, 0)
        self.assertIn("Faithfulness 95%", out)
        low = out.lower()
        for word in ["pass", "fail", "safe", "approved", "compliant", "high confidence",
                     "good enough", "accurate", "ready to send"]:
            self.assertIsNone(re.search(r"\b" + word + r"\b", low), word)


if __name__ == "__main__":
    unittest.main(verbosity=2)
