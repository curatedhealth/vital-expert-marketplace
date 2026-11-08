#!/usr/bin/env python3
"""Unittest suite for FOCUSED offline tools (no network)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from lib.score_core import score_session
from lib.session_io import blank_session, load_session, save_session
from lib.stage_checks import structural_gaps
from stamp_focused_line import stamp


class SessionIoTests(unittest.TestCase):
    def test_round_trip(self) -> None:
        row = blank_session()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "s.focused.json"
            save_session(row, path)
            loaded = load_session(path)
            self.assertEqual(loaded["session_id"], row["session_id"])
            self.assertIn("how_to_decide", loaded["stages"])


class StructuralTests(unittest.TestCase):
    def test_missing_frame(self) -> None:
        gaps = structural_gaps(blank_session())
        codes = {g["code"] for g in gaps}
        self.assertIn("missing_statement", codes)
        self.assertIn("too_few_options", codes)


class ScoreTests(unittest.TestCase):
    def test_score_two_options(self) -> None:
        row = blank_session()
        row["options"] = [{"id": "A", "name": "A"}, {"id": "B", "name": "B"}]
        row["criteria"] = [
            {"name": "impact", "weight": 70, "direction": "higher_better"},
            {"name": "risk", "weight": 30, "direction": "lower_better"},
        ]
        row["ratings"] = [
            {"rater": "Alex", "option": "A", "criterion": "impact", "value": 5},
            {"rater": "Alex", "option": "A", "criterion": "risk", "value": 2},
            {"rater": "Alex", "option": "B", "criterion": "impact", "value": 3},
            {"rater": "Alex", "option": "B", "criterion": "risk", "value": 4},
        ]
        out = score_session(row)
        self.assertTrue(out["scored"], msg=json.dumps(out))
        self.assertEqual(len(out["raters"]), 1)
        ranked = out["raters"][0]["ranked"]
        self.assertEqual(len(ranked), 2)
        self.assertIn("robustness", out["raters"][0])
        # Never labels a winner field
        self.assertNotIn("winner", out)


class StampTests(unittest.TestCase):
    def test_local_stamp(self) -> None:
        s = stamp(mode="local", skill="tradeoff-score", extra="2 options")
        self.assertIn("FOCUSED / tradeoff-score", s["check_line"])
        self.assertIn("FOCUSED-local", s["check_line"])


if __name__ == "__main__":
    unittest.main()
