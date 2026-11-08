"""Unit tests for TRUSTED offline tools. No network."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

from claim_structure import structural_verdict  # noqa: E402
from format_citation import format_chicago, format_citation  # noqa: E402
from passage_support import decide  # noqa: E402
from render_report import generate_report  # noqa: E402
from score_source_offline import score_source  # noqa: E402
from stamp_check_line import stamp  # noqa: E402


class ToolsSuiteTests(unittest.TestCase):
    def test_structural_verdict_negation(self):
        out = structural_verdict(
            "Drug X improved survival",
            "Drug X did not improve survival versus placebo",
        )
        self.assertIsNotNone(out)
        self.assertIn(out[0], {"contradicted", "unsupported"})

    def test_score_source_offline_authority(self):
        scored = score_source(
            {
                "publisher": "U.S. Food and Drug Administration",
                "date": "2024-01-15",
                "title": "Label",
                "tier": "gold",
            },
            question="FDA label for product X",
            currency="not_checked",
        )
        self.assertGreater(scored["total"], 0)
        self.assertEqual(scored["axes"]["authority"], 25)
        self.assertIsNone(scored["axes"]["currency"])

    def test_format_chicago(self):
        line = format_chicago(
            {
                "publisher": "FDA",
                "date": "2024-06-01",
                "title": "Prescribing information",
                "official_url": "https://example.gov/x",
            }
        )
        self.assertIn("FDA", line)
        self.assertIn("2024", line)

    def test_format_citation_harvard(self):
        line = format_citation({"publisher": "EMA", "date": "2023", "title": "EPAR"}, "harvard")
        self.assertIn("EMA", line)
        self.assertIn("2023", line)

    def test_passage_support_high_overlap(self):
        out = decide(
            "The trial enrolled 120 patients",
            "The trial enrolled 120 patients at 14 sites.",
        )
        self.assertIn(out["status"], {"supported", "partial"})
        self.assertIn("not tool-checked", out["label"])

    def test_passage_support_empty_passage(self):
        out = decide("A claim", "")
        self.assertEqual(out["status"], "unverifiable")

    def test_stamp_check_line(self):
        out = stamp(mode="offline", skill="claim-assessment")
        self.assertIn("not tool-checked", out["check_line"])
        self.assertEqual(out["skill"], "claim-assessment")

    def test_render_report_evidence_table(self):
        findings = [
            {"claim": "X reduced Y by 20%", "status": "supported", "locator": "p.3", "rationale": "exact"},
            {"claim": "X is best in class", "status": "unsupported", "rationale": "not in passage"},
        ]
        out = generate_report(template="evidence-table", findings=findings)
        self.assertNotIn("error", out)
        self.assertIn("X reduced Y", out["markdown"])
        self.assertGreaterEqual(out["summary"]["open_items"], 1)

    def test_render_report_gap_list(self):
        findings = [{"claim": "unsupported claim", "status": "unsupported"}]
        out = generate_report(template="gap-list", findings=findings)
        self.assertIn("unsupported claim", out["markdown"])

    def test_split_claims_cli(self):
        text = TOOLS / "_tmp_claims.txt"
        text.write_text("Alpha improved outcomes. Beta was unchanged.\n", encoding="utf-8")
        try:
            proc = subprocess.run(
                [sys.executable, str(TOOLS / "split_claims.py"), str(text), "--json"],
                capture_output=True,
                text=True,
                check=True,
            )
            data = json.loads(proc.stdout)
            claims = data["claims"] if isinstance(data, dict) else data
            self.assertIsInstance(claims, list)
            self.assertGreaterEqual(len(claims), 2)
        finally:
            text.unlink(missing_ok=True)

    def test_identify_source_id_cli(self):
        proc = subprocess.run(
            [sys.executable, str(TOOLS / "identify_source_id.py"), "10.1000/xyz", "--json"],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(proc.stdout)
        self.assertEqual(data["use_first"]["kind"], "DOI")

    def test_faithfulness_cli(self):
        proc = subprocess.run(
            [
                sys.executable,
                str(TOOLS / "faithfulness.py"),
                "--source",
                "method",
                "--supported",
                "2",
                "--unsupported",
                "1",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(
            "not tool-checked" in proc.stdout.lower()
            or "method" in proc.stdout.lower()
            or "2" in proc.stdout
        )

    def test_no_network_imports(self):
        forbidden = ("urllib", "requests", "httpx", "aiohttp", "socket")
        for path in TOOLS.glob("*.py"):
            if path.name.startswith("test_"):
                continue
            text = path.read_text(encoding="utf-8")
            for name in forbidden:
                self.assertNotIn(f"import {name}", text)
                self.assertNotIn(f"from {name}", text)


if __name__ == "__main__":
    unittest.main()
