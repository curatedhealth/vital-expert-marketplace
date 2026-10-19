#!/usr/bin/env python3
"""Capability build plan checks. Checks only; never sets levels, owners or dates.

Plans from the strategic gap register (Strategic Readiness), not from a maturity assessment
(owner ruling 11, pending the maturity assessment rulings). For each capability in the register:
whether it is planned or explicitly deferred with a reason; for each plan: action (in the
person's words), owner (a role), the required level it aims for (from the register, 1 to 10),
a check date, and the delivery steps or options that wait for it. Flags: top gaps with no plan;
plans with no owner or date; options that need a gap closed first whose gap has no plan; a plan
that names a maturity level.

Input (JSON):
  {"register": [{"capability": "...", "current": 4.0, "required": 8.5, "weighted_gap": 58.5}, ...],
   "top_n": 3,
   "needed_by_options": {"Medical writing copilot": ["Structured content data and tagging"]},
   "plans": [{"capability": "...", "action": "...", "owner": "...", "target_required": 8.5,
              "check_on": "2027-03", "unblocks": ["Pilot of the copilot"]}],
   "deferred": [{"capability": "...", "reason": "..."}]}

Usage:  python3 build_plan_check.py plan.json [--json]
"""

from __future__ import annotations

import json
import re
import sys


def evaluate(p):
    reg = p.get("register") or []
    if not reg:
        raise ValueError("the strategic gap register is needed; run Strategic Readiness first")
    reg = sorted(reg, key=lambda r: -float(r.get("weighted_gap", 0)))
    top_n = int(p.get("top_n") or 3)
    top = [r["capability"] for r in reg[:top_n]]
    plans = {x.get("capability"): x for x in p.get("plans") or []}
    deferred = {x.get("capability"): x for x in p.get("deferred") or []}
    issues, rows = [], []
    for r in reg:
        c = r["capability"]
        pl, de = plans.get(c), deferred.get(c)
        row = {"capability": c, "weighted_gap": r.get("weighted_gap"), "top": c in top,
               "status": "planned" if pl else ("deferred" if de else "no plan"), "flags": []}
        if pl:
            for k, msg in (("action", "no action"), ("owner", "no owner"), ("check_on", "no check date")):
                if not str(pl.get(k) or "").strip():
                    row["flags"].append(msg)
            tr = pl.get("target_required")
            if tr is None:
                row["aim"] = f"{r.get('required')} (default: the register's required level)"
            if tr is not None and r.get("required") is not None and float(tr) != float(r["required"]):
                row["flags"].append(f"aims for {tr}, the register's required level is {r['required']}: record why")
            if re.search(r"\blevel\s*[1-5]\b|\bmaturity\b", str(pl.get("action", "")), re.I):
                row["flags"].append("names a maturity level; the maturity assessment is not in use yet")
        elif de:
            if not str(de.get("reason") or "").strip():
                row["flags"].append("deferred without a reason")
        elif c in top:
            row["flags"].append("top gap with no plan and no deferral")
        rows.append(row)
    for opt, needs in (p.get("needed_by_options") or {}).items():
        for c in needs:
            if c not in plans:
                issues.append(f"'{opt}' needs '{c}' closed first, and it has no plan")
    for c in plans:
        if c not in {r['capability'] for r in reg}:
            issues.append(f"plan for '{c}', which is not in the gap register")
    return {"rows": rows, "issues": issues,
            "rule": "Checks only. People choose the action, the owner and the date. Levels are the register's 1 to 10 scores, not maturity levels."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (ValueError, json.JSONDecodeError, OSError, KeyError) as exc:
        print(f"Not checked: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(r, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
