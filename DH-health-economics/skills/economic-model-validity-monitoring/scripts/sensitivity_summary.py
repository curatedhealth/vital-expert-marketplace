#!/usr/bin/env python3
# Origin: copied unchanged from economic-model-development/scripts/sensitivity_summary.py (dh-health-economics, 19 October 2026) so this skill stands alone.
"""Sensitivity summary for a model run with he_model.py: one-way ranges, switching values,
quadrant changes and named scenarios, all on ranges and scenarios the person supplies.

Why not tornado the ICER: a ratio jumps sign and quadrant when the incremental QALY
crosses zero, and a tornado ranks that as a small swing (measured on the connector's
risk-tornado, references/tools.md). This script works on net monetary benefit at the
person's threshold, which moves in a straight line for most inputs, and flags every
range in which the quadrant changes.

Input: the same model JSON as he_model.py, plus
  "sensitivity": {
     "comparison_arm": name (default: the first arm that is not the reference),
     "threshold": the person's value to judge net benefit at (default: first of thresholds),
     "ranges": {parameter: [low, high]}         number parameters
                {parameter: [[low list], [high list]]}  list parameters, one value per year
  }
  "scenarios": [{"name", "set": {parameter: value}, "discount": {...}, "horizon_years": n}]
               scenarios the person chose (HE-022 (DOI 10.1016/j.jval.2013.08.2291): chosen from the decision maker's perspective)

Output: a table sorted by swing in net monetary benefit, with low and high results,
whether net benefit changes sign in the range, the switching value when it does (the
input value at which net monetary benefit is zero, HE-077), and quadrant changes;
then one row per scenario. No range or scenario is invented: a parameter without a range
is reported as "no range given".

Usage: python3 sensitivity_summary.py model.json [--json]
"""
import argparse
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import he_model  # noqa: E402


def outcome(model, params, cmp_arm, ref_arm, L):
    arms = he_model.run_arms(model, params)
    a = next(x for x in arms if x["name"] == cmp_arm)
    r = next(x for x in arms if x["name"] == ref_arm)
    dc, dq = a["cost_disc"] - r["cost_disc"], a["qaly_disc"] - r["qaly_disc"]
    return {"d_cost": dc, "d_qaly": dq, "nmb": L * dq - dc if L else None, "quadrant": he_model.quadrant(dc, dq)}


def switching_value(model, base, name, lo, hi, cmp_arm, ref_arm, L, iters=80):
    """Bisection for NMB = 0 between lo and hi (number parameters only)."""
    def f(v):
        p = dict(base)
        p[name] = v
        return outcome(model, p, cmp_arm, ref_arm, L)["nmb"]
    flo, fhi = f(lo), f(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if (flo > 0) == (fhi > 0):
        return None
    a, b = lo, hi
    for _ in range(iters):
        m = (a + b) / 2
        fm = f(m)
        if (fm > 0) == (flo > 0):
            a, flo = m, fm
        else:
            b = m
    return (a + b) / 2


def run(model):
    s = model.get("sensitivity", {})
    ref = model.get("reference_arm", model["arms"][0]["name"])
    cmp_arm = s.get("comparison_arm") or next(a["name"] for a in model["arms"] if a["name"] != ref)
    th = model.get("thresholds", [])
    L = s.get("threshold", th[0] if th else None)
    base_params = model["parameters"]
    base = outcome(model, base_params, cmp_arm, ref, L)
    rows = []
    ranges = s.get("ranges", {})
    for name in base_params:
        if name not in ranges:
            rows.append({"parameter": name, "status": "no range given"})
            continue
        lo, hi = ranges[name]
        pl, ph = dict(base_params), dict(base_params)
        pl[name], ph[name] = lo, hi
        ol, oh = outcome(model, pl, cmp_arm, ref, L), outcome(model, ph, cmp_arm, ref, L)
        row = {"parameter": name, "base": base_params[name], "low": lo, "high": hi,
               "nmb_low": ol["nmb"], "nmb_high": oh["nmb"],
               "swing": abs(oh["nmb"] - ol["nmb"]) if L else None,
               "quadrant_low": ol["quadrant"], "quadrant_high": oh["quadrant"],
               "quadrant_changes": len({ol["quadrant"], oh["quadrant"], base["quadrant"]}) > 1}
        if L is not None:
            row["sign_change"] = (ol["nmb"] > 0) != (oh["nmb"] > 0) or ol["nmb"] == 0 or oh["nmb"] == 0
            if row["sign_change"] and not isinstance(lo, list):
                row["switching_value"] = switching_value(model, base_params, name, float(lo), float(hi), cmp_arm, ref, L)
        rows.append(row)
    ranged = sorted([r for r in rows if "swing" in r], key=lambda r: -(r["swing"] or 0))
    unranged = [r for r in rows if "swing" not in r]
    scen = []
    for sc in model.get("scenarios", []):
        m2 = copy.deepcopy(model)
        m2["parameters"].update(sc.get("set", {}))
        if "discount" in sc:
            m2["discount"] = {**m2.get("discount", {}), **sc["discount"]}
        if "horizon_years" in sc:
            m2["horizon_years"] = sc["horizon_years"]
        o = outcome(m2, m2["parameters"], cmp_arm, ref, L)
        icer = o["d_cost"] / o["d_qaly"] if o["d_qaly"] and (o["d_cost"] > 0) == (o["d_qaly"] > 0) and o["d_cost"] != 0 else None
        scen.append({"name": sc["name"], "changes": {k: v for k, v in sc.items() if k != "name"}, **o, "icer": icer})
    return {"comparison": f"{cmp_arm} vs {ref}", "threshold_from_person": L, "base": base,
            "one_way": ranged + unranged, "scenarios": scen}


def to_markdown(r):
    f = he_model.fmt
    L = r["threshold_from_person"]
    out = [f"# Sensitivity summary: {r['comparison']}",
           f"Net monetary benefit judged at the person's threshold: {f(L, 0) if L else 'none given [GAP]; only quadrants shown'}.",
           f"Base case: dCost {f(r['base']['d_cost'])}, dQALY {f(r['base']['d_qaly'], 4)}, {r['base']['quadrant']}, "
           f"net monetary benefit {f(r['base']['nmb']) if L else 'n/a'}.",
           "\n## One-way ranges (sorted by swing)\n",
           "| Parameter | Base | Low | High | NMB at low | NMB at high | Swing | Sign change | Switching value | Quadrant change |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for row in r["one_way"]:
        if row.get("status"):
            out.append(f"| {row['parameter']} | | | | | | | | | {row['status']} |")
            continue
        sv = row.get("switching_value")
        qc = f"yes: {row['quadrant_low']} to {row['quadrant_high']}" if row["quadrant_changes"] else "no"
        out.append(f"| {row['parameter']} | {row['base']} | {row['low']} | {row['high']} | {f(row['nmb_low'])} | "
                   f"{f(row['nmb_high'])} | {f(row['swing'])} | {'yes' if row.get('sign_change') else 'no'} | "
                   f"{f(sv, 4) if sv is not None else ('outside range' if not row.get('sign_change') else 'list input: not solved')} | {qc} |")
    if r["scenarios"]:
        out += ["\n## Scenarios the person chose\n", "| Scenario | Changes | dCost | dQALY | Quadrant | ICER | NMB |",
                "|---|---|---|---|---|---|---|"]
        for s in r["scenarios"]:
            out.append(f"| {s['name']} | {json.dumps(s['changes'])} | {f(s['d_cost'])} | {f(s['d_qaly'], 4)} | {s['quadrant']} | "
                       f"{f(s['icer'], 0) if s['icer'] is not None else 'see quadrant'} | {f(s['nmb']) if L else 'n/a'} |")
    out.append("\nA switching value is where net monetary benefit is zero at the person's threshold; it is not a verdict. "
               "Ranges and scenarios are the person's. Results are hypotheses on the inputs.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    with open(a.model) as fh:
        model = json.load(fh)
    try:
        r = run(model)
    except (ValueError, KeyError, ZeroDivisionError, StopIteration) as e:
        sys.exit(f"Input error: {e}")
    print(json.dumps(r, indent=1) if a.json else to_markdown(r))


if __name__ == "__main__":
    main()
