import json
import unittest
from pathlib import Path

import assemble_valuation_summary as a

FX = Path(__file__).resolve().parent.parent / "evals" / "val-summary" / "fixtures"


def go(name, **kw):
    m = json.loads((FX / name).read_text())
    return a.assemble(m, FX, **kw)


class TestAssembler(unittest.TestCase):
    def test_all_clear(self):
        s = go("manifest-all.json")
        self.assertEqual({w["status"] for w in s["workstreams"]}, {"green"})
        self.assertEqual(s["conflicts"], [])
        self.assertEqual(s["adopted_valuation"], "HUMAN ONLY")
        self.assertIsNone(s["recommended_valuation"])
        self.assertEqual(len(s["answer"]), 3)

    def test_conflict_is_shown_not_reconciled(self):
        s = go("manifest-conflict.json")
        self.assertEqual(len(s["conflicts"]), 1)
        self.assertFalse(s["conflicts"][0]["reconciled"])

    def test_missing_output_is_red_gap_with_skill(self):
        s = go("manifest-missing-v7.json")
        w = {x["skill"]: x for x in s["workstreams"]}
        self.assertEqual(w["V7"]["status"], "red")
        self.assertTrue(any(g.get("run") == "identify-comparable-transactions" for g in s["gaps"]))
        self.assertIn("V8", [k for k in w])

    def test_hard_errors(self):
        for n, code in (("manifest-recommend.json", "E_RECOMMEND"), ("manifest-bad-pointer.json", "E_POINTER"), ("manifest-adopted.json", "E_ADOPT")):
            with self.assertRaises(a.Hard) as cm:
                go(n)
            self.assertEqual(cm.exception.code, code)

    def test_thresholds_override(self):
        s = go("manifest-all.json", thresholds={"yellow_if_gaps_at_least": 0, "red_if_gaps_at_least": 0})
        self.assertEqual({w["status"] for w in s["workstreams"]}, {"red"})

    def test_markdown_has_seven_sections(self):
        md = a.to_md(go("manifest-all.json"))
        for i in range(1, 8):
            self.assertIn(f"## {i}.", md)

    def test_no_network(self):
        src = Path(a.__file__).read_text()
        for bad in ("urllib", "requests", "socket", "http.client"):
            self.assertNotIn("import " + bad, src)


if __name__ == "__main__":
    unittest.main()
