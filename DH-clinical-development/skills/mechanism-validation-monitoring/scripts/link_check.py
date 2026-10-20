#!/usr/bin/env python3
"""Link-by-link mechanism check of one cohort against a check plan (mechanism-validation-monitoring A2).

Usage:
  python3 link_check.py --plan PLAN.json --data COHORT.csv [--version V] [--as-of YYYY-MM-DD] [--json]

The plan (shape: evals/files/check_plan_illustrative.json) lists links in reading order
(delivered, used, changed, outcome), each with a column (or column_pre and column_post),
an aggregation (mean, proportion_true, mean_change, proportion_at_least with "cut"),
a direction (">=" or "<="), the person's threshold, and whether it was prespecified.

What it does: filters rows to one version, computes each link's value with its n and
missing count, marks met or missed only when the link was prespecified and has a
threshold, lists every other link as "not scored" with the reason, repeats scored
links within the person's named subgroups (same threshold, labeled), warns when a
delivery or use link missed before later links are read (CS32), and counts met links
over measurable links. It never imputes, never invents a threshold, proxy or data cut
(without --as-of it prints "data cut not given"), flags links read at one time point
as levels, not changes, and the count is not a quality score. Every [PAPER] row it prints carries its DOI.
"""
import argparse
import csv
import json

DOI = {"CS32": "10.1007/s10488-010-0319-7", "TM57": "10.1037/hea0000161", "TM92": "10.1136/bmj.h1258"}
ORDER = {"delivered": 0, "used": 1, "changed": 2, "outcome": 3}
TRUE = {"1", "true", "yes", "y"}
FALSE = {"0", "false", "no", "n"}


def row(r):
    return f"{r}, DOI {DOI[r]}" if r in DOI else r


def num(v):
    if v is None:
        return None
    s = str(v).strip()
    if s == "":
        return None
    if s.lower() in TRUE:
        return 1.0
    if s.lower() in FALSE:
        return 0.0
    try:
        return float(s)
    except ValueError:
        return None


def compute(link, rows):
    agg = link.get("aggregation")
    if agg == "mean_change":
        vals = []
        for r in rows:
            a, b = num(r.get(link.get("column_pre"))), num(r.get(link.get("column_post")))
            vals.append(None if a is None or b is None else b - a)
    else:
        vals = [num(r.get(link.get("column"))) for r in rows]
    present = [v for v in vals if v is not None]
    n, missing = len(present), len(vals) - len(present)
    if n == 0:
        return None, n, missing
    if agg in ("mean", "mean_change"):
        return sum(present) / n, n, missing
    if agg == "proportion_true":
        return sum(1 for v in present if v == 1.0) / n, n, missing
    if agg == "proportion_at_least":
        cut = link.get("cut")
        if cut is None:
            return None, n, missing
        return sum(1 for v in present if v >= cut) / n, n, missing
    return None, n, missing


def verdict(link, value):
    if not link.get("prespecified"):
        return "not scored", f"measure not named in advance ({row('TM57')})"
    if link.get("threshold") is None:
        return "not scored", "no threshold set by the person"
    if value is None:
        return "not scored", "no usable data for this link"
    t, d = link["threshold"], link.get("direction", ">=")
    ok = value >= t if d == ">=" else value <= t
    return ("met" if ok else "missed"), f"{d} {t}"


def run(plan, rows, version):
    excluded = 0
    if version:
        vrows = [r for r in rows if str(r.get("version", "")).strip() == version]
        excluded = len(rows) - len(vrows)
        rows = vrows
    links = sorted(plan["links"], key=lambda l: ORDER.get(l.get("type"), 9))
    results, first_upstream_miss = [], None
    for l in links:
        v, n, miss = compute(l, rows)
        res, why = verdict(l, v)
        results.append({"id": l["id"], "type": l.get("type"), "measure": l.get("measure"), "n": n, "missing": miss,
                        "value": None if v is None else round(v, 3), "result": res, "basis": why,
                        "proxy": bool(l.get("proxy"))})
        if res == "missed" and l.get("type") in ("delivered", "used") and first_upstream_miss is None:
            first_upstream_miss = l["id"]
    subgroup_results = []
    for sg in plan.get("subgroups", []):
        srows = [r for r in rows if str(r.get(sg["column"], "")).strip() == str(sg["value"])]
        for l in links:
            res0 = next(x for x in results if x["id"] == l["id"])
            if res0["result"] == "not scored":
                continue
            v, n, miss = compute(l, srows)
            res, why = verdict(l, v)
            subgroup_results.append({"subgroup": sg["name"], "id": l["id"], "n": n, "missing": miss,
                                     "value": None if v is None else round(v, 3), "result": res, "basis": why + " (same threshold as the whole cohort)"})
    scored = [r for r in results if r["result"] in ("met", "missed")]
    return {"version": version, "rows_used": len(rows), "rows_other_versions_excluded": excluded,
            "results": results, "subgroups": subgroup_results,
            "unmeasured": plan.get("unmeasured", []),
            "count": {"met": sum(1 for r in scored if r["result"] == "met"), "measurable": len(scored)},
            "first_upstream_miss": first_upstream_miss}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--version")
    ap.add_argument("--as-of", help="the data cut the person gave; never today's date")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    plan = json.load(open(a.plan))
    rows = list(csv.DictReader(l for l in open(a.data, newline="") if not l.startswith("#")))  # "#" lines are labels
    out = run(plan, rows, a.version)
    if a.json:
        print(json.dumps(out, indent=1))
        return
    label = plan.get("label", "")
    print(f"# Link-by-link check: {plan.get('product', 'unnamed')}" + (f" ({label})" if label else ""))
    print()
    print(f"- Version: {a.version or 'not given (not filtered); ask the person'}; rows used {out['rows_used']}; rows of other versions excluded {out['rows_other_versions_excluded']}")
    print(f"- Data cut: {a.as_of or 'not given; ask the person (never supply today’s date)'}; plan set {plan.get('plan_date') or 'not given'}, data read before the plan: {plan.get('data_read_before_plan', 'not given')}")
    print(f"- {out['count']['met']} of {out['count']['measurable']} measurable links met against the person's thresholds. Not a quality score.")
    print()
    print("| Link | Type | Measure | n | Missing | Value | Result | Basis |")
    print("|---|---|---|---|---|---|---|---|")
    for r in out["results"]:
        m = r["measure"] + (" (proxy named in advance)" if r["proxy"] else "")
        print(f"| {r['id']} | {r['type']} | {m} | {r['n']} | {r['missing']} | {r['value']} | {r['result']} | {r['basis']} |")
    levels = [l for l in plan["links"] if l.get("type") == "changed" and l.get("aggregation") != "mean_change" and l.get("column")]
    if levels:
        print()
        for l in levels:
            print(f"Level note: {l['id']} reads one column ({l['column']}); it is a level at that time point, not a change. A 'drop' or 'rise' cannot be computed from this file without a baseline column.")
    if out["first_upstream_miss"]:
        print()
        print(f"Reading note: {out['first_upstream_miss']} (delivery or use) missed. Later links cannot separate an ineffective mechanism from failed delivery ({row('CS32')}; {row('TM92')}).")
    if out["subgroups"]:
        print()
        print("## Subgroups the person named (context; same thresholds)")
        print()
        print("| Subgroup | Link | n | Missing | Value | Result |")
        print("|---|---|---|---|---|---|")
        for s in out["subgroups"]:
            print(f"| {s['subgroup']} | {s['id']} | {s['n']} | {s['missing']} | {s['value']} | {s['result']} |")
    if out["unmeasured"]:
        print()
        print("## Not measurable ([GAP], not scored)")
        for u in out["unmeasured"]:
            print(f"- {u.get('id')} ({u.get('type')}): {u.get('text')}; {u.get('reason')}")


if __name__ == "__main__":
    main()
