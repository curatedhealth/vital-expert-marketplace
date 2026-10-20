#!/usr/bin/env python3
"""Absolute and relative effects for a binary outcome, from supplied arm values.

Part of the VITAL TRUSTED skill grounded-statements (task TR-5.1.2).
Every output is derived from the values passed in; nothing is looked up.

Examples:
  python risk_metrics.py --treat-events 10 --treat-n 500 --ctrl-events 20 --ctrl-n 500
  python risk_metrics.py --treat-rate 0.02 --ctrl-rate 0.04 --check rrr=50 --check arr=2

--check takes a stated value from the draft: rr (ratio), rrr (%), arr (percentage
points), nnt (patients). The script reports whether the stated value matches the
derived value within a tolerance.
"""
import argparse
import json
import math
import sys


def arm_risk(events, n, rate, label):
    if rate is not None:
        if events is not None or n is not None:
            sys.exit(f"{label}: give either a rate or events and n, not both")
        if not 0 <= rate <= 1:
            sys.exit(f"{label}: rate must be between 0 and 1 (e.g. 0.12 for 12%)")
        return rate
    if events is None or n is None:
        sys.exit(f"{label}: give --{label}-events and --{label}-n, or --{label}-rate")
    if n <= 0 or events < 0 or events > n:
        sys.exit(f"{label}: events must be between 0 and n, and n above 0")
    return events / n


def derive(rt, rc):
    rd = rt - rc  # risk difference, treatment minus control (proportion)
    out = {
        "treatment_risk_pct": round(rt * 100, 4),
        "control_risk_pct": round(rc * 100, 4),
        "risk_difference_pct_points": round(rd * 100, 4),
        "relative_risk": None,
        "relative_risk_change_pct": None,
        "nnt_or_nnh": None,
        "direction": None,
        "note": "derived from supplied values",
    }
    if rc > 0:
        rr = rt / rc
        out["relative_risk"] = round(rr, 4)
        out["relative_risk_change_pct"] = round((rr - 1) * 100, 4)
    if rd == 0:
        out["direction"] = "no difference: NNT not defined"
    else:
        raw = 1 / abs(rd)
        out["nnt_or_nnh"] = {"rounded_up": math.ceil(raw - 1e-9), "unrounded": round(raw, 2)}
        out["direction"] = (
            "lower risk with treatment (NNT, if the outcome is harmful)"
            if rd < 0
            else "higher risk with treatment (NNH, if the outcome is harmful)"
        )
    return out


def check(stated, d):
    results = []
    for item in stated:
        if "=" not in item:
            sys.exit(f"--check needs key=value, got {item}")
        key, val = item.split("=", 1)
        key, val = key.strip().lower(), float(val.strip().rstrip("%"))
        if key == "rr":
            derived, tol = d["relative_risk"], 0.01
        elif key == "rrr":
            derived = None if d["relative_risk_change_pct"] is None else -d["relative_risk_change_pct"]
            tol = 0.5
        elif key == "arr":
            derived, tol = -d["risk_difference_pct_points"], 0.05
        elif key == "nnt":
            derived = None if d["nnt_or_nnh"] is None else d["nnt_or_nnh"]["rounded_up"]
            tol = 0.5
        else:
            sys.exit(f"unknown check key {key}; use rr, rrr, arr or nnt")
        ok = derived is not None and abs(derived - val) <= tol
        results.append({"check": key, "stated": val, "derived": derived,
                        "matches": ok})
    return results


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    for arm in ("treat", "ctrl"):
        p.add_argument(f"--{arm}-events", type=int)
        p.add_argument(f"--{arm}-n", type=int)
        p.add_argument(f"--{arm}-rate", type=float)
    p.add_argument("--check", action="append", default=[],
                   help="stated value from the draft, e.g. rrr=50, arr=2, rr=0.5, nnt=50")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    rt = arm_risk(a.treat_events, a.treat_n, a.treat_rate, "treat")
    rc = arm_risk(a.ctrl_events, a.ctrl_n, a.ctrl_rate, "ctrl")
    d = derive(rt, rc)
    res = {"derived": d, "checks": check(a.check, d)}

    if a.json:
        print(json.dumps(res, indent=2))
        return
    print("Derived from supplied values")
    print(f"  Treatment risk:   {d['treatment_risk_pct']}%")
    print(f"  Control risk:     {d['control_risk_pct']}%")
    print(f"  Risk difference:  {d['risk_difference_pct_points']} percentage points (treatment minus control)")
    if d["relative_risk"] is not None:
        print(f"  Relative risk:    {d['relative_risk']}")
        print(f"  Relative change:  {d['relative_risk_change_pct']}% (negative = reduction)")
    else:
        print("  Relative risk:    not defined (control risk is 0)")
    if d["nnt_or_nnh"]:
        print(f"  NNT/NNH:          {d['nnt_or_nnh']['rounded_up']} (unrounded {d['nnt_or_nnh']['unrounded']})")
    print(f"  Direction:        {d['direction']}")
    for c in res["checks"]:
        flag = "matches" if c["matches"] else "DIFFERS"
        print(f"  Check {c['check']}: stated {c['stated']}, derived {c['derived']} -> {flag}")


if __name__ == "__main__":
    main()
