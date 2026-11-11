#!/usr/bin/env python3
"""Tests for ci_checks.py. Each check is run against a small temporary plugin tree.

Run: python3 test_ci_checks.py
"""

import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True

import ci_checks as c  # noqa: E402

SKILL = '''---
name: demo
description: "Checks demo files. Use it when a demo needs checking."
metadata:
  version: "0.3.4"
---

# Demo

## Files in this skill

Every file the skill ships, one per row, except this `SKILL.md`.

| File | What it is | When to use it |
|---|---|---|
| `tasks/one.md` | A task | Always |
'''


class Tree(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        self._old = (c.ROOT, c.SKILLS)
        c.ROOT = self.root
        c.SKILLS = os.path.join(self.root, "skills")
        self.write(".claude-plugin/plugin.json", json.dumps(
            {"name": "demo", "version": "0.3.4", "release_state": "Pilot", "description": "d"}))
        self.write("skills/demo/SKILL.md", SKILL)
        self.write("skills/demo/tasks/one.md", "# One\n\nSee `references/two.md`.\n")
        self.write("skills/demo/references/two.md", "# Two\n")
        self.write("skills/demo/references/method.md",
                   "# Method\n\n0. **Safety first (TR-H14).** Flag first.\n1. Pick the task.\n")
        # keep the Files table honest for the base tree
        self.write("skills/demo/SKILL.md", SKILL.replace(
            "| `tasks/one.md` | A task | Always |",
            "| `tasks/one.md` | A task | Always |\n| `references/two.md` | Notes | Always |\n| `references/method.md` | Method | Always |"))

    def tearDown(self):
        c.ROOT, c.SKILLS = self._old
        self.tmp.cleanup()

    def write(self, rel, text):
        path = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)

    def problems(self, fn):
        return fn()[0]


class BaseTreePasses(Tree):
    def test_every_check_passes_on_the_base_tree(self):
        for name, fn in c.CHECKS:
            self.assertEqual(self.problems(fn), [], name)


class FileCount(Tree):
    def test_over_cap_fails(self):
        old = c.MAX_FILES
        c.MAX_FILES = 3
        try:
            self.assertTrue(self.problems(c.check_file_count))
        finally:
            c.MAX_FILES = old


class Descriptions(Tree):
    def test_long_description_fails(self):
        self.write("skills/demo/SKILL.md", SKILL.replace("Checks demo files. Use it when a demo needs checking.", "x" * 1025))
        self.assertTrue(self.problems(c.check_descriptions))

    def test_exactly_at_cap_passes(self):
        self.write("skills/demo/SKILL.md", SKILL.replace("Checks demo files. Use it when a demo needs checking.", "x" * 1024))
        self.assertEqual(self.problems(c.check_descriptions), [])


class Versions(Tree):
    def test_old_version_fails(self):
        self.write("skills/demo/SKILL.md", SKILL.replace('"0.3.4"', '"0.1.0"'))
        self.assertTrue(self.problems(c.check_versions))

    def test_release_state_must_be_pilot(self):
        self.write(".claude-plugin/plugin.json", json.dumps(
            {"version": "0.3.4", "release_state": "Released"}))
        self.assertTrue(self.problems(c.check_versions))


class DependsOn(Tree):
    def test_unshipped_dependency_fails(self):
        self.write("skills/demo/tasks/one.md", "depends_on: [vital-core-atoms]\n")
        self.assertTrue(self.problems(c.check_depends_on))

    def test_shipped_dependency_passes(self):
        self.write("skills/demo/tasks/one.md", "depends_on: [demo]\n")
        self.assertEqual(self.problems(c.check_depends_on), [])


class Pointers(Tree):
    def test_missing_pointer_fails(self):
        self.write("skills/demo/tasks/one.md", "See `references/missing.md`.\n")
        self.assertTrue(self.problems(c.check_pointers))

    def test_cross_skill_pointer_resolves(self):
        self.write("skills/other/SKILL.md", SKILL.replace("demo", "other"))
        self.write("skills/other/references/x.md", "# X\n")
        self.write("skills/other/tasks/one.md", "# Other\n")
        self.write("skills/other/references/two.md", "# Other two\n")
        self.write("skills/demo/tasks/one.md", "See `../other/references/x.md`.\n")
        self.assertEqual(self.problems(c.check_pointers), [])

    def test_bare_file_name_resolves_from_file_folder(self):
        self.write("skills/demo/references/three.md", "# Three\n")
        self.write("skills/demo/references/two.md", "Also `three.md`.\n")
        self.assertEqual(self.problems(c.check_pointers), [])

    def test_user_supplied_files_are_not_pointers(self):
        self.write("skills/demo/tasks/one.md", "Run `tool --file draft.txt`.\n")
        self.assertEqual(self.problems(c.check_pointers), [])

    def test_urls_are_not_pointers(self):
        self.write("skills/demo/tasks/one.md", "https://example.org/references/nothing.md\n")
        self.assertEqual(self.problems(c.check_pointers), [])


class FilesTables(Tree):
    def test_unlisted_file_fails(self):
        self.write("skills/demo/templates/extra.md", "# Extra\n")
        self.assertTrue(self.problems(c.check_files_tables))

    def test_listed_but_missing_fails(self):
        os.remove(os.path.join(self.root, "skills/demo/references/two.md"))
        self.assertTrue(self.problems(c.check_files_tables))


class RepoPaths(Tree):
    def test_repo_path_fails(self):
        self.write("skills/demo/tasks/one.md", "See mcps/trusted/eval-kit for more.\n")
        self.assertTrue(self.problems(c.check_repo_paths))

    def test_url_with_docs_segment_passes(self):
        self.write("skills/demo/tasks/one.md", "https://example.org/docs/en/page\n")
        self.assertEqual(self.problems(c.check_repo_paths), [])


class VerifyWords(Tree):
    def test_tool_name_fails(self):
        self.write("skills/demo/tasks/one.md", "Call check_claim on each sentence.\n")
        self.assertTrue(self.problems(c.check_verify_words))

    def test_tool_name_in_do_not_use_rule_passes(self):
        self.write("skills/demo/tasks/one.md", "Never name check_claim in a reply.\n")
        self.assertEqual(self.problems(c.check_verify_words), [])

    def test_status_name_fails(self):
        self.write("skills/demo/tasks/one.md", "The result is `unsupported`.\n")
        self.assertTrue(self.problems(c.check_verify_words))

    def test_key_prefix_fails(self):
        self.write("skills/demo/tasks/one.md", "Use the key vvfy_abc.\n")
        self.assertTrue(self.problems(c.check_verify_words))

    def test_plain_verb_passes(self):
        self.write("skills/demo/tasks/one.md", "Please verify the date yourself.\n")
        self.assertEqual(self.problems(c.check_verify_words), [])

    def test_changelog_is_exempt(self):
        self.write("CHANGELOG.md", "Retired VERIFY and vvfy_ keys.\n")
        self.assertEqual(self.problems(c.check_verify_words), [])


class EmDash(Tree):
    def test_template_with_em_dash_fails(self):
        self.write("skills/demo/templates/card.md", "Label \u2014 value\n")
        self.assertTrue(self.problems(c.check_em_dash))

    def test_gap_marker_with_em_dash_fails(self):
        # 0.3.4: gap markers use semicolons; an em dash inside one is no longer exempt
        self.write("skills/demo/templates/card.md",
                   "[GAP: source \u2014 the page \u2014 the label]\n")
        self.assertTrue(self.problems(c.check_em_dash))

    def test_gap_marker_with_semicolons_passes(self):
        self.write("skills/demo/templates/card.md",
                   "[GAP: not supplied; the page; supply the label]\n")
        self.assertEqual(self.problems(c.check_em_dash), [])

    def test_em_dash_after_a_gap_marker_still_fails(self):
        self.write("skills/demo/templates/card.md", "[GAP: a \u2014 b \u2014 c] then \u2014 more\n")
        self.assertTrue(self.problems(c.check_em_dash))

    def test_em_dash_in_example_fails(self):
        self.write("skills/demo/examples/good.md", "Plain \u2014 words\n")
        self.assertTrue(self.problems(c.check_em_dash))

    def test_em_dash_in_a_task_is_out_of_scope(self):
        self.write("skills/demo/tasks/one.md", "Plain \u2014 words\n")
        self.assertEqual(self.problems(c.check_em_dash), [])


class Duplicates(Tree):
    def test_identical_files_fail(self):
        self.write("skills/demo/references/a.md", "same\n")
        self.write("skills/demo/references/b.md", "same\n")
        self.assertTrue(self.problems(c.check_duplicates))


class Cli(Tree):
    def test_exit_code_follows_result(self):
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(c.main([]), 0)
            self.write("skills/demo/references/a.md", "same\n")
            self.write("skills/demo/references/b.md", "same\n")
            self.assertEqual(c.main(["--only", "duplicates"]), 1)



class AddedChecks(Tree):
    def test_safety_step_missing(self):
        self.write("skills/demo/references/method.md", "# Method\n\n1. Read the intake card.\n")
        self.assertTrue(self.problems(c.check_safety_first))

    def test_description_without_cue(self):
        self.write("skills/demo/SKILL.md", read_base(self).replace("Use it when a demo needs checking.", "I can check."))
        self.assertTrue(self.problems(c.check_frontmatter))

    def test_name_differs_from_folder(self):
        self.write("skills/demo/SKILL.md", read_base(self).replace("name: demo", "name: other"))
        self.assertTrue(self.problems(c.check_frontmatter))

    def test_extra_frontmatter_key(self):
        self.write("skills/demo/SKILL.md", read_base(self).replace("name: demo", "name: demo\nowner: x"))
        self.assertTrue(self.problems(c.check_frontmatter))

    def test_known_answer_requiring_gap(self):
        self.write("skills/demo/evals/known-answer/case-01.md",
                   '# Case\n\n```json\n{"must_include": ["[GAP:"]}\n```\n')
        self.assertTrue(self.problems(c.check_eval_rules))

    def test_known_answer_gap_in_drafted_deliverable_allowed(self):
        self.write("skills/demo/evals/known-answer/case-01.md",
                   '# Case\n\n```json\n{"gap_marker_expected_in": "drafted deliverable", "must_include": ["[GAP:"]}\n```\n')
        self.assertEqual(self.problems(c.check_eval_rules), [])

    def test_contradiction_phrase(self):
        self.write("skills/demo/references/two.md", "# Two\n\nRows apply, including when True is off.\n")
        self.assertTrue(self.problems(c.check_rule_contradictions))

    def test_exclamation_in_example(self):
        self.write("skills/demo/examples/one.md", "# Example\n\nGreat work here!\n")
        self.assertTrue(self.problems(c.check_voice))

    def test_derived_report_lists_points(self):
        self.write("skills/demo/examples/one.md", "# Example\n\nUp 4 percentage points.\n")
        self.assertEqual(len(c.report_derived_figures()), 1)



class FinalChecks(Tree):
    def test_safety_list_variant_fails(self):
        self.write("skills/demo/references/two.md", "# Two\n\nIf any input mentions a possible side effect, pregnancy exposure, overdose or product quality problem.\n")
        self.assertTrue(self.problems(c.check_safety_list))

    def test_safety_list_exact_passes(self):
        self.write("skills/demo/references/two.md", "# Two\n\nIf any input mentions a " + c.SAFETY_LIST + ".\n")
        self.assertEqual(self.problems(c.check_safety_list), [])

    def test_agent_without_description_fails(self):
        self.write("agents/a.md", "---\nname: a\n---\n# A\n")
        self.assertTrue(self.problems(c.check_agents))

def read_base(case):
    with open(os.path.join(case.root, "skills/demo/SKILL.md"), encoding="utf-8") as handle:
        return handle.read()

if __name__ == "__main__":
    unittest.main()
