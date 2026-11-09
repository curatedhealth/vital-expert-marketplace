"""Unit tests for the TRUSTED offline tools. No network.

Remaining tools: split_claims, plain_reference, stamp_check_line. (The count script
faithfulness.py ships in skills/confidence-scoring/scripts with its own test.)
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import plain_reference  # noqa: E402
import split_claims  # noqa: E402
from stamp_check_line import letter_lines, parse_letter_spec  # noqa: E402

RETIRED = (
    "passage_support.py",
    "claim_structure.py",
    "score_source_offline.py",
    "format_citation.py",
    "render_report.py",
    "identify_source_id.py",
)


def run(script, args, stdin=None):
    return subprocess.run(
        [sys.executable, "-I", str(TOOLS / script), *args],
        input=stdin, capture_output=True, text=True,
    )


class SplitClaims(unittest.TestCase):
    def test_offsets_round_trip(self):
        text = "Alpha improved outcomes by 20%. Beta was unchanged, e.g. in older adults."
        result = split_claims.analyze(text)
        self.assertEqual(len(result["claims"]), 2)
        for c in result["claims"]:
            self.assertEqual(text[c["start"]:c["end"]], c["text"])
        self.assertEqual(result["method"], "manual split, not tool-checked")

    def test_self_test(self):
        proc = run("split_claims.py", ["--self-test"])
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_cli_json(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "t.txt"
            f.write_text("Alpha improved outcomes. Beta was unchanged.\n", encoding="utf-8")
            proc = run("split_claims.py", [str(f), "--json"])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertGreaterEqual(len(json.loads(proc.stdout)["claims"]), 2)


class PlainReference(unittest.TestCase):
    def test_uses_only_supplied_details(self):
        r = plain_reference.build({"authors": "Lee A", "title": "Trial of X", "year": 2024,
                                   "container": "J Med", "doi": "10.1000/xyz"})
        self.assertIn("Lee A", r["line"])
        self.assertIn("10.1000/xyz", r["line"])
        self.assertNotIn("Accessed", r["line"])
        self.assertNotIn("accessed", r["line"])

    def test_missing_fields_are_listed_not_filled(self):
        r = plain_reference.build({"title": "Untitled report"})
        for field in ("authors", "year", "identifier (DOI, PMID or URL)"):
            self.assertIn(field, r["missing"])
        self.assertNotIn("n.d.", r["line"])

    def test_source_kind_is_kept_in_line(self):
        r = plain_reference.build({"authors": "Ng P", "title": "Night checks",
                                   "container": "Invented Nursing Forum", "year": 2025,
                                   "type": "poster"})
        self.assertIn("Poster.", r["line"])
        r = plain_reference.build({"title": "Velunor at a glance", "publisher": "Northvale",
                                   "year": 2026, "type": "fact sheet",
                                   "url": "https://example.org/fs"})
        self.assertIn("Fact sheet.", r["line"])

    def test_kind_not_repeated_or_shown_for_articles(self):
        r = plain_reference.build({"title": "Trial of X", "container": "Congress abstract book",
                                   "year": 2025, "type": "abstract"})
        self.assertEqual(r["line"].lower().count("abstract"), 1)
        r = plain_reference.build({"authors": "Lee A", "title": "Trial of X", "year": 2024,
                                   "container": "J Med", "type": "article"})
        self.assertNotIn("Article", r["line"])

    def test_no_authors_asked_for_labels_and_fact_sheets(self):
        for kind in ("label", "fact sheet", "press release", "summary of product characteristics"):
            r = plain_reference.build({"title": "Doc", "publisher": "Northvale", "year": 2026,
                                       "type": kind, "url": "https://example.org/d"})
            self.assertNotIn("authors", r["missing"], kind)
        r = plain_reference.build({"title": "Doc", "container": "J", "year": 2026,
                                   "type": "poster"})
        self.assertIn("authors", r["missing"])

    def test_society_guideline_needs_no_journal(self):
        r = plain_reference.build({"authors": "National Society for Condition P",
                                   "title": "Treatment guideline", "version": "version 3",
                                   "published_online": "12 January 2026", "type": "guideline",
                                   "url": "https://example.org/guideline-p-v3"})
        self.assertNotIn("journal, publisher or website", r["missing"])
        self.assertEqual(r["missing"], [])
        r = plain_reference.build({"title": "Treatment guideline", "year": 2026,
                                   "type": "guideline", "url": "https://example.org/g"})
        self.assertIn("journal, publisher or website", r["missing"])

    def test_poster_presenter_labeled_presented_by(self):
        for key in ("presenter", "presented_by"):
            r = plain_reference.build({key: "Dr. Ines Varga", "container": "Fictional Infusion Congress",
                                       "type": "poster"})
            self.assertIn("Presented by Dr. Ines Varga.", r["line"], key)
            self.assertFalse(r["line"].startswith("Dr. Ines Varga"), key)
            self.assertIn("authors", r["missing"], key)
            self.assertEqual(r["ignored_fields"], [], key)

    def test_smpc_needs_no_identifier(self):
        for kind in ("SmPC", "summary of product characteristics", "label", "package leaflet"):
            r = plain_reference.build({"title": "Velunor SmPC", "publisher": "Northvale",
                                       "type": kind, "version": "revision April 2026"})
            self.assertNotIn("identifier (DOI, PMID or URL)", r["missing"], kind)
        r = plain_reference.build({"title": "Velunor SmPC", "type": "SmPC",
                                   "version": "revision April 2026"})
        self.assertNotIn("journal, publisher or website", r["missing"])
        r = plain_reference.build({"authors": "Lee A", "title": "Trial of X", "year": 2024,
                                   "container": "J Med", "volume": "1", "pages": "2"})
        self.assertIn("identifier (DOI, PMID or URL)", r["missing"])

    def test_label_revision_kept_as_given(self):
        for key in ("version", "revision"):
            r = plain_reference.build({"title": "Velunor SmPC", "publisher": "Northvale",
                                       "type": "SmPC", key: "revision April 2026"})
            self.assertIn("Revision April 2026.", r["line"], key)
            self.assertNotIn("year", r["missing"], key)
            self.assertEqual(r["ignored_fields"], [], key)

    def test_published_online_date_kept_whole(self):
        r = plain_reference.build({"authors": "Lee A", "title": "Trial of X", "container": "J Med",
                                   "year": 2026, "volume": "4", "pages": "1-9",
                                   "published_online": "3 March 2026", "doi": "10.1/x"})
        self.assertIn("Published online 3 March 2026.", r["line"])
        self.assertEqual(r["missing"], [])

    def test_supplied_year_in_any_form_is_never_missing(self):
        for extra in ({"date": "12 March 2026"}, {"published_online": "3 March 2026"},
                      {"version": "version 2, 2025"}):
            src = {"title": "Guide", "publisher": "Society", "type": "guideline",
                   "url": "https://example.org/g"}
            src.update(extra)
            r = plain_reference.build(src)
            self.assertNotIn("year", r["missing"], extra)
        r = plain_reference.build({"title": "Guide", "publisher": "Society", "type": "guideline",
                                   "date": "12 March 2026", "url": "https://example.org/g"})
        self.assertIn("12 March 2026", r["line"])
        r = plain_reference.build({"title": "Guide", "publisher": "Society", "type": "guideline",
                                   "version": "version 3.0", "url": "https://example.org/g"})
        self.assertIn("year", r["missing"])

    def test_cli_label(self):
        proc = run("plain_reference.py", ["-"], stdin=json.dumps([{"title": "T", "year": 2023}]))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("not tool-checked", proc.stdout)


class LetterLines(unittest.TestCase):
    def test_letter_words_and_true_has_own_line(self):
        out = letter_lines([
            parse_letter_spec("Tangible|usefulness|2 generic sentences"),
            parse_letter_spec("True|sources|3 claims with no source|second paragraph"),
        ])
        self.assertIn("Tangible · usefulness: 2 generic sentences (not tool-checked)", out["text"])
        self.assertIn("True · sources: 3 claims with no source (not tool-checked)", out["text"])
        self.assertIn("  second paragraph", out["text"])
        self.assertNotIn("Stamp:", out["text"])

    def test_codes_are_refused(self):
        with self.assertRaises(SystemExit):
            parse_letter_spec("T|sources|1 claim")

    def test_verdict_words_are_refused(self):
        for spec in ("Safe|patient safety|pass", "Unbiased|balance|2 items, compliant"):
            with self.assertRaises(SystemExit):
                parse_letter_spec(spec)

    def test_ready_phrases_are_refused(self):
        for phrase in ("ready to go", "good to go", "ready to send", "all set", "fine to send"):
            with self.assertRaises(SystemExit, msg=phrase):
                parse_letter_spec(f"Defensible|record|1 item, {phrase}")

    def test_hand_on_and_fine_print_are_not_verdicts(self):
        for spec in ("Safe|possible safety reports|1 to pass to your safety process",
                     "Tangible|fit for the reader|2 terms in fine print"):
            self.assertEqual(len(letter_lines([parse_letter_spec(spec)])["lines"]), 1)

    def test_not_run_line_has_no_label(self):
        out = letter_lines([parse_letter_spec("True|sources|not checked, no sources supplied")])
        self.assertEqual(out["lines"][0], "True · sources: not checked, no sources supplied")

    def test_no_tool_checked_option(self):
        proc = run("stamp_check_line.py", ["--mode", "verify", "--letter", "True|s|1 claim"])
        self.assertNotEqual(proc.returncode, 0)


class Suite(unittest.TestCase):
    def test_retired_tools_are_gone(self):
        for name in RETIRED:
            self.assertFalse((TOOLS / name).exists(), name)

    def test_no_network_imports(self):
        forbidden = ("urllib", "requests", "httpx", "aiohttp", "socket")
        for path in TOOLS.glob("*.py"):
            if path.name.startswith("test_"):
                continue
            text = path.read_text(encoding="utf-8")
            for name in forbidden:
                self.assertNotIn(f"import {name}", text)
                self.assertNotIn(f"from {name}", text)

    def test_no_percent_or_tool_status_names_in_tool_sources(self):
        for name in ("stamp_check_line.py",):
            text = (TOOLS / name).read_text(encoding="utf-8")
            for banned in ("faithfulness_percent", "tool-checked via", "Prove live MCP"):
                self.assertNotIn(banned, text, name)


if __name__ == "__main__":
    unittest.main()
