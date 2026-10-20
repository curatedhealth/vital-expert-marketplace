#!/usr/bin/env python3
# Origin: copied unchanged from economic-model-development/scripts/he_model.py (dh-health-economics, 19 October 2026) so this skill stands alone.
"""Transparent deterministic economic model runner (cost-utility and budget impact).

Runs only on numbers the person supplies. Every input is printed beside every result.
It never declares an intervention cost-effective: thresholds are the decision-maker's,
and the script reports the arithmetic at each threshold the person gives, nothing more.

Input: one JSON file (see examples/inputs/dcbti_model_illustrative.json).
  label, illustrative (true or false), currency, cost_year, perspective
  horizon_years           number of yearly cycles (t = 0, 1, ...)
  discount                {"costs": r, "effects": r, "first_year_discounted": false}
                          the rates and the timing convention are the person's choice;
                          references/reference-cases.md lists what each HTA body states
  parameters              {name: number or list (one value per year)}
  arms                    [{"name", "cost": expr or [expr per year], "qaly": expr or [...]}]
                          expressions use parameter names, t, + - * / ** ( ), min, max
  reference_arm           name of the arm all others are compared with (default: first)
  thresholds              the person's cost per QALY values, or [] for none
  budget_impact           optional: {"years", "eligible_population", "uptake",
                          "current_mix": [{"name", "share", "annual_cost_per_patient"}],
                          "new_cost_per_patient", "condition_cost_change_per_patient"}
                          values may be numbers, lists or expressions. The new technology
                          is assumed to displace the current mix in proportion to its
                          shares; the person confirms that assumption.

Output: markdown tables (default) or JSON (--json).

Arithmetic used (stated so a reviewer can replicate it, HE-024, DOI 10.1016/j.jval.2013.08.2291):
  discounted value in year t = value / (1 + r) ** k, with k = t + 1 if first_year_discounted
  else k = t. ICER = incremental cost / incremental QALY (HE-041), reported as a ratio only
  when both increments are positive or both negative, with the quadrant always named.
  Net health benefit at threshold L = dQALY - dCost / L; net monetary benefit = L * dQALY - dCost.
  Budget impact in year t = population * uptake * (new cost - weighted current-mix cost
  + condition cost change), undiscounted.

Usage: python3 he_model.py model.json [--json]
"""
import argparse
import ast
import json
import math
import operator
import sys

_BIN = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow}
_UNARY = {ast.USub: operator.neg, ast.UAdd: operator.pos}
_FUNCS = {"min": min, "max": max}


def evaluate(expr, params, t):
    """Evaluate a number, a list (indexed by t) or an arithmetic expression string."""
    if isinstance(expr, (int, float)):
        return float(expr)
    if isinstance(expr, list):
        if t >= len(expr):
            raise ValueError(f"list {expr} has no value for year index t={t}")
        return evaluate(expr[t], params, t)
    if not isinstance(expr, str):
        raise ValueError(f"cannot evaluate {expr!r}")
    tree = ast.parse(expr, mode="eval")

    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in _BIN:
            return _BIN[type(node.op)](ev(node.left), ev(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY:
            return _UNARY[type(node.op)](ev(node.operand))
        if isinstance(node, ast.Name):
            if node.id == "t":
                return float(t)
            if node.id not in params:
                raise ValueError(f"unknown name '{node.id}' in '{expr}'")
            return evaluate(params[node.id], params, t)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCS:
            return _FUNCS[node.func.id](*[ev(a) for a in node.args])
        raise ValueError(f"not allowed in expression: '{expr}' (use + - * / ** and names)")
    return ev(tree)


def discount_factor(rate, t, first_year_discounted):
    k = t + 1 if first_year_discounted else t
    return 1.0 / (1.0 + rate) ** k


def run_arms(model, params=None):
    params = params if params is not None else model["parameters"]
    years = int(model["horizon_years"])
    d = model.get("discount", {})
    rc, re_, fyd = float(d.get("costs", 0)), float(d.get("effects", 0)), bool(d.get("first_year_discounted", False))
    out = []
    for arm in model["arms"]:
        rows = []
        for t in range(years):
            c = evaluate(arm["cost"], params, t)
            q = evaluate(arm["qaly"], params, t)
            rows.append({"t": t, "cost": c, "qaly": q,
                         "cost_disc": c * discount_factor(rc, t, fyd),
                         "qaly_disc": q * discount_factor(re_, t, fyd)})
        out.append({"name": arm["name"], "years": rows,
                    "cost": sum(r["cost"] for r in rows), "qaly": sum(r["qaly"] for r in rows),
                    "cost_disc": sum(r["cost_disc"] for r in rows), "qaly_disc": sum(r["qaly_disc"] for r in rows)})
    return out


def quadrant(dc, dq):
    if dq > 0 and dc <= 0:
        return "dominant (more QALYs, same or lower cost)"
    if dq < 0 and dc >= 0:
        return "dominated (fewer QALYs, same or higher cost)"
    if dq > 0 and dc > 0:
        return "north-east (more QALYs, more cost)"
    if dq < 0 and dc < 0:
        return "south-west (fewer QALYs, lower cost)"
    return "no QALY difference (cost comparison only)"


def compare(arms, ref_name, thresholds):
    ref = next(a for a in arms if a["name"] == ref_name)
    res = []
    for a in arms:
        if a["name"] == ref_name:
            continue
        dc, dq = a["cost_disc"] - ref["cost_disc"], a["qaly_disc"] - ref["qaly_disc"]
        icer = dc / dq if dq != 0 and (dc > 0) == (dq > 0) and dc != 0 else None
        res.append({"arm": a["name"], "vs": ref_name, "d_cost": dc, "d_qaly": dq,
                    "quadrant": quadrant(dc, dq), "icer": icer,
                    "at_threshold": [{"threshold": L, "net_health_benefit": dq - dc / L,
                                      "net_monetary_benefit": L * dq - dc} for L in thresholds]})
    return res


def incremental_frontier(arms):
    """Fully incremental analysis: drop strict and extended dominance (HE-039)."""
    pts = sorted(arms, key=lambda a: (a["cost_disc"], -a["qaly_disc"]))
    notes = {}
    # strict dominance
    keep = []
    for a in pts:
        dom = next((b for b in pts if b is not a and b["cost_disc"] <= a["cost_disc"]
                    and b["qaly_disc"] >= a["qaly_disc"]
                    and (b["cost_disc"] < a["cost_disc"] or b["qaly_disc"] > a["qaly_disc"])), None)
        if dom:
            notes[a["name"]] = f"dominated by {dom['name']}"
        else:
            keep.append(a)
    # extended dominance
    changed = True
    while changed and len(keep) > 2:
        changed = False
        icers = [(keep[i]["cost_disc"] - keep[i - 1]["cost_disc"]) / (keep[i]["qaly_disc"] - keep[i - 1]["qaly_disc"])
                 for i in range(1, len(keep))]
        for i in range(len(icers) - 1):
            if icers[i] > icers[i + 1]:
                notes[keep[i + 1]["name"]] = "extendedly dominated"
                keep.pop(i + 1)
                changed = True
                break
    frontier = []
    for i, a in enumerate(keep):
        if i == 0:
            frontier.append({"arm": a["name"], "icer_vs_previous": None, "previous": None})
        else:
            p = keep[i - 1]
            frontier.append({"arm": a["name"], "previous": p["name"],
                             "icer_vs_previous": (a["cost_disc"] - p["cost_disc"]) / (a["qaly_disc"] - p["qaly_disc"])})
    return frontier, notes


def budget_impact(model, params=None):
    bia = model.get("budget_impact")
    if not bia:
        return None
    params = params if params is not None else model["parameters"]
    years = int(bia.get("years", model.get("horizon_years", 1)))
    rows, cum = [], 0.0
    for t in range(years):
        pop = evaluate(bia["eligible_population"], params, t)
        up = evaluate(bia["uptake"], params, t)
        mix = bia["current_mix"]
        share_sum = sum(float(m["share"]) for m in mix)
        if abs(share_sum - 1) > 1e-6:
            raise ValueError(f"current_mix shares sum to {share_sum}, not 1")
        mix_cost = sum(float(m["share"]) * evaluate(m["annual_cost_per_patient"], params, t) for m in mix)
        new = evaluate(bia["new_cost_per_patient"], params, t)
        cond = evaluate(bia.get("condition_cost_change_per_patient", 0), params, t)
        net = pop * up * (new - mix_cost + cond)
        cum += net
        rows.append({"t": t, "eligible_population": pop, "uptake": up, "patients_on_new": pop * up,
                     "current_mix_cost_per_patient": mix_cost, "new_cost_per_patient": new,
                     "condition_cost_change_per_patient": cond, "net_budget_impact": net, "cumulative": cum})
    return rows


def run(model):
    arms = run_arms(model)
    ref = model.get("reference_arm", model["arms"][0]["name"])
    th = [float(x) for x in model.get("thresholds", [])]
    out = {"label": model.get("label"), "illustrative": model.get("illustrative", False),
           "currency": model.get("currency"), "cost_year": model.get("cost_year"),
           "perspective": model.get("perspective"), "horizon_years": model["horizon_years"],
           "discount": model.get("discount", {}), "parameters": model["parameters"],
           "arms": arms, "comparisons": compare(arms, ref, th), "thresholds_from_person": th,
           "budget_impact": budget_impact(model)}
    if len(arms) > 2:
        out["frontier"], out["frontier_notes"] = incremental_frontier(arms)
    return out


def fmt(x, nd=2):
    if x is None:
        return "n/a"
    if isinstance(x, float) and (math.isinf(x) or math.isnan(x)):
        return str(x)
    return f"{x:,.{nd}f}"


def to_markdown(r):
    cur = r.get("currency") or "currency not stated [GAP]"
    L = []
    L.append(f"# Model run: {r.get('label')}")
    if r.get("illustrative"):
        L.append("ILLUSTRATIVE inputs: not any product's data.")
    L.append(f"Currency {cur}, cost year {r.get('cost_year') or '[GAP]'}; perspective: {r.get('perspective') or '[GAP]'}; "
             f"horizon {r['horizon_years']} years; discount costs {r['discount'].get('costs', 0)}, effects "
             f"{r['discount'].get('effects', 0)}, first year discounted: {r['discount'].get('first_year_discounted', False)}.")
    L.append("\n## Inputs (the person's)\n\n| Parameter | Value |\n|---|---|")
    for k, v in r["parameters"].items():
        L.append(f"| {k} | {v} |")
    L.append("\n## Totals per arm\n\n| Arm | Cost | QALYs | Cost discounted | QALYs discounted |\n|---|---|---|---|---|")
    for a in r["arms"]:
        L.append(f"| {a['name']} | {fmt(a['cost'])} | {fmt(a['qaly'], 4)} | {fmt(a['cost_disc'])} | {fmt(a['qaly_disc'], 4)} |")
    L.append("\n## Incremental results (discounted)\n\n| Arm vs reference | dCost | dQALY | Quadrant | ICER |\n|---|---|---|---|---|")
    for c in r["comparisons"]:
        L.append(f"| {c['arm']} vs {c['vs']} | {fmt(c['d_cost'])} | {fmt(c['d_qaly'], 4)} | {c['quadrant']} | "
                 f"{fmt(c['icer'], 0) if c['icer'] is not None else 'not a meaningful ratio; see quadrant'} |")
    if r["thresholds_from_person"]:
        L.append("\n## At the thresholds the person gave (arithmetic, not a verdict)\n\n| Arm | Threshold | Net health benefit (QALYs) | Net monetary benefit |\n|---|---|---|---|")
        for c in r["comparisons"]:
            for a in c["at_threshold"]:
                L.append(f"| {c['arm']} | {fmt(a['threshold'], 0)} | {fmt(a['net_health_benefit'], 4)} | {fmt(a['net_monetary_benefit'])} |")
    else:
        L.append("\nNo threshold given: net benefit not computed. Thresholds are the decision-maker's.")
    if r.get("frontier"):
        L.append("\n## Fully incremental analysis\n\n| Arm on frontier | Compared with | ICER |\n|---|---|---|")
        for f in r["frontier"]:
            L.append(f"| {f['arm']} | {f['previous'] or '(lowest cost)'} | {fmt(f['icer_vs_previous'], 0) if f['icer_vs_previous'] is not None else 'n/a'} |")
        for k, v in r["frontier_notes"].items():
            L.append(f"- {k}: {v}")
    if r.get("budget_impact"):
        L.append("\n## Budget impact (undiscounted, per year)\n\n| Year index | Population | Uptake | Patients on new | Current mix cost | New cost | Condition cost change | Net impact | Cumulative |\n|---|---|---|---|---|---|---|---|---|")
        for b in r["budget_impact"]:
            L.append(f"| {b['t']} | {fmt(b['eligible_population'], 0)} | {b['uptake']} | {fmt(b['patients_on_new'], 0)} | "
                     f"{fmt(b['current_mix_cost_per_patient'])} | {fmt(b['new_cost_per_patient'])} | "
                     f"{fmt(b['condition_cost_change_per_patient'])} | {fmt(b['net_budget_impact'])} | {fmt(b['cumulative'])} |")
        L.append("Assumption to confirm: the new technology displaces the current mix in proportion to its shares.")
    L.append("\nAll results are hypotheses on the inputs above. Whether any result is acceptable is the decision-maker's call.")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    with open(a.model) as f:
        model = json.load(f)
    try:
        r = run(model)
    except (ValueError, KeyError, ZeroDivisionError) as e:
        sys.exit(f"Input error: {e}")
    print(json.dumps(r, indent=1) if a.json else to_markdown(r))


if __name__ == "__main__":
    main()
