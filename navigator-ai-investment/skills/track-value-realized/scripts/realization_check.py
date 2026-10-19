#!/usr/bin/env python3
"""Value realization checks. Computes and checks; never decides what a result means.

1. Each outcome the value depends on: measured result against its target (direction-aware):
   achieved / not achieved / not measured. A result without a source is not a measurement.
2. Realized value counts only if every outcome it depends on is achieved (unmet = zero, never
   partial). Otherwise the measured figure is shown as "not counted".
3. The counted figure is placed against the declared range exactly as the connector does:
   below (< low), inside, above (> high). Unit and period must match the range.

Input (JSON):
  {"range": {"low": 0.4, "mid": 0.9, "high": 1.6, "unit": "EUR million per year", "basis": "..."},
   "outcomes": [{"name": "...", "direction": "reduce", "baseline": 300, "target": 210,
                 "result": 200, "source": "team time log, Q3 2027"}],
   "realized": {"value": 1.1, "unit": "EUR million per year", "source": "finance, FY2027 actuals",
                "measured": true},
   "other_changes": ["..."]}                                    optional, owner-stated

Usage:  python3 realization_check.py input.json
"""

from __future__ import annotations

import json
import sys

LOWER = {"reduce", "minimize", "eliminate"}


def evaluate(p):
    problems, outcomes = [], []
    rng = p.get("range") or {}
    for k in ("low", "high", "unit"):
        if rng.get(k) in (None, ""):
            problems.append(f"declared range missing {k}: realized value cannot be placed")
    for o in p.get("outcomes") or []:
        name = o.get("name", "outcome")
        res, tgt, d = o.get("result"), o.get("target"), str(o.get("direction") or "").lower()
        if res is None or not str(o.get("source") or "").strip():
            status = "not measured"
        elif not isinstance(tgt, (int, float)) or not isinstance(res, (int, float)):
            status = "not measured"
            problems.append(f"{name}: result and target must be numbers")
        else:
            ok = res <= tgt if d in LOWER else res >= tgt
            status = "achieved" if ok else "not achieved"
        outcomes.append({"outcome": name, "status": status, "result": res, "target": tgt})
    if not outcomes:
        problems.append("no outcome given: value can only be counted against an outcome measured as achieved")
    all_met = bool(outcomes) and all(o["status"] == "achieved" for o in outcomes)
    rv = p.get("realized") or {}
    measured = rv.get("measured") is True and str(rv.get("source") or "").strip() != ""
    unit_ok = rv.get("unit") == rng.get("unit")
    if rv.get("value") is None:
        problems.append("no realized figure given")
    elif not measured:
        problems.append("the realized figure is not a measurement with a source: not counted")
    if rv.get("value") is not None and rng.get("unit") and not unit_ok:
        problems.append(f"realized figure is in '{rv.get('unit')}', the range in '{rng.get('unit')}'")
    counted, place = None, "[GAP]"
    if all_met and measured and unit_ok and rv.get("value") is not None and not any("declared range" in x for x in problems):
        counted = rv["value"]
        place = "below" if counted < rng["low"] else ("above" if counted > rng["high"] else "inside")
    elif rv.get("value") is not None and outcomes and not all_met:
        counted = 0
        place = "not counted: an outcome it depends on is not measured as achieved (unmet realizes zero)"
    return {"outcomes": outcomes, "all_outcomes_achieved": all_met, "counted_realized_value": counted,
            "measured_figure": rv.get("value"), "place_against_range": place,
            "other_changes_stated": p.get("other_changes") or [], "problems": problems,
            "rule": "Value counts only for outcomes measured as achieved; unmet realizes zero. Placement describes; the owner decides what it means."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (json.JSONDecodeError, OSError, TypeError) as exc:
        print(f"Not checked: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(r, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
