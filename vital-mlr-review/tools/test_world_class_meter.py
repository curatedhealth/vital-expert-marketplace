"""Regression: world_class_meter must PASS for Pilot content grade."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
METER = PLUGIN / "scripts" / "world_class_meter.py"


class WorldClassMeter(unittest.TestCase):
    def test_meter_pass(self):
        proc = subprocess.run(
            [sys.executable, str(METER)],
            cwd=str(PLUGIN),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            proc.returncode,
            0,
            msg=f"world_class_meter FAILED:\n{proc.stdout}\n{proc.stderr}",
        )
        self.assertIn("GRADE: world-class-pilot-content", proc.stdout)


if __name__ == "__main__":
    unittest.main()
