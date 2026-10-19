#!/usr/bin/env python3
"""Trial design checks. Checks only; never sets a target and never declares success.

A trial is a safe-to-fail experiment (EOS-L3 probe template) designed before it starts:
hypothesis, success signal (measure, baseline, target, direction), failure signal, stop rule,
time limit, exit condition; plus what the connector stores: the outcome served, a value range and
a cost-to-test range (low, mid, high, unit, basis; a point refused), and the measure's name,
baseline and owner. Adds two readings for the owner (skill practice, H): whether the cost-to-test
high end exceeds the value low end (the test may cost more than the worst case it protects), and
whether the target direction agrees with the baseline.

With "result": places a reported result against the target (reached / not reached); the owner
declares success later.

Input (JSON):
  {"option": "...", "owner_result": "Investigate first",
   "outcome": "...", "hypothesis": "...",
   "measure": {"name": "...", "unit": "...", "baseline": 300, "owner": "Head of Medical Writing",
               "direction": "reduce" | "increase", "target": 180},
   "failure_signal": "...", "stop_rule": "...", "time_limit": "12 weeks", "exit_condition": "...",
   "value": {"low": 0.4, "mid": 0.9, "high": 1.6, "unit": "EUR million per year", "basis": "..."},
   "cost_to_test": {"low": 0.05, "mid": 0.08, "high": 0.12, "unit": "EUR million", "basis": "..."},
   "result": 210}                                                   optional, after the trial

Usage:  python3 trial_check.py trial.json [--json]
"""

from __future__ import annotations

import json
import sys

RANGE_KEYS = ("low", "mid", "high", "unit", "basis")


def _range(label, block, problems):
    if not isinstance(block, dict):
        problems.append(f"{label}: a low, likely and high range with unit and basis is needed")
        return None
    missing = [k for k in RANGE_KEYS if block.get(k) in (None, "")]
    if missing:
        problems.append(f"{label}: missing {', '.join(missing)}")
        return None
    lo, mid, hi = block["low"], block["mid"], block["high"]
    if lo == hi:
        problems.append(f"{label}: a point estimate is refused (low equals high)")
    elif not (lo <= mid <= hi):
        problems.append(f"{label}: low, likely and high are out of order")
    return block


def evaluate(p):
    problems, notes = [], []
    for k, msg in [("outcome", "the outcome the trial serves"), ("hypothesis", "the hypothesis"),
                   ("failure_signal", "the failure signal"), ("stop_rule", "the stop rule"),
                   ("time_limit", "the time limit"), ("exit_condition", "the exit condition")]:
        if not str(p.get(k) or "").strip():
            problems.append(f"missing {msg}")
    m = p.get("measure") if isinstance(p.get("measure"), dict) else {}
    for k in ("name", "baseline", "owner", "target", "direction"):
        if m.get(k) in (None, ""):
            problems.append(f"measure: missing {k}")
    d = str(m.get("direction") or "").lower()
    b, t = m.get("baseline"), m.get("target")
    if isinstance(b, (int, float)) and isinstance(t, (int, float)):
        if d in ("reduce", "minimize", "eliminate") and t >= b:
            problems.append(f"target {t} is not below the baseline {b}, but the direction is '{d}'")
        if d in ("increase", "maximize") and t <= b:
            problems.append(f"target {t} is not above the baseline {b}, but the direction is '{d}'")
    v = _range("value", p.get("value"), problems)
    c = _range("cost to test", p.get("cost_to_test"), problems)
    if v and c and v.get("unit") and c.get("unit"):
        same_money = v["unit"].split()[0] == c["unit"].split()[0]
        per = lambda u: any(w in u.lower() for w in ("per year", "a year", "/year", "per month", "a month", "annual"))
        if same_money and per(v["unit"]) != per(c["unit"]):
            notes.append("one range is per period and the other is one-off: say which period the comparison uses (H)")
        if same_money and c["high"] > v["low"]:
            notes.append("the cost-to-test high end is above the value low end: the test may cost more than the worst case it protects (H)")
        if not same_money:
            notes.append("value and cost to test are in different units; compare them in one unit before reading the trade-off")
    res = p.get("result")
    placed = None
    if res is not None:
        if not isinstance(res, (int, float)) or not isinstance(t, (int, float)):
            problems.append("the result and the target must both be numbers to place the result")
        else:
            reached = res <= t if d in ("reduce", "minimize", "eliminate") else res >= t
            placed = "target reached" if reached else "target not reached"
    owner_result = p.get("owner_result")
    if owner_result not in (None, "Investigate first", "Proceed"):
        notes.append(f"trials are designed for 'Investigate first' (or 'Proceed' when the owner asks to test risk or reversibility); this option's result is '{owner_result}'")
    return {"ready_to_start": not problems, "problems": problems, "notes": notes, "result": placed,
            "stores_on_connector": ["outcome", "value", "cost_to_test", "measure name, baseline, owner"],
            "report_only": ["hypothesis", "target and direction", "failure signal", "stop rule", "time limit", "exit condition"],
            "rule": "Success is defined before the trial by the owner. This check never declares success; a placed result is reported, and the owner decides."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Not checked: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(r, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
