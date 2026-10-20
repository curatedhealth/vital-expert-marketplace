#!/usr/bin/env python3
"""Compare reach and outcomes across subgroups the person defines, from aggregate counts.

No patient-level data. One CSV row per subgroup with these columns:

  dimension      the grouping the person chose (for example "preferred language")
  subgroup       one value of that dimension (for example "Spanish"); use "Not recorded"
                 for people whose value is unknown
  eligible       people the change or program was meant to reach (denominator)
  reached        of those, people who used it, by the person's own definition of "reached"
  outcome_n      optional: of those reached, people with the outcome measured
  outcome_met    optional: of those measured, people who met the outcome the person defined

Usage:
  python equity_compare.py counts.csv --min-cell 11 --reference "preferred language=English" \
      [--reference "age band=18-44"] [--suppress-zero] [--json out.json]

--min-cell is required and is the person's rule (or their data provider's): any shown count
from 1 to min-cell minus 1 is suppressed. The script does not pick it. Suppression is applied
to the counts and to their complements (eligible minus reached, outcome_n minus outcome_met),
so a hidden count cannot be recovered by subtraction from a shown one. Within a dimension, if
only one subgroup is suppressed, the next smallest subgroup is also suppressed (complementary
suppression), because the dimension total is shown. Suppression is checked table by table:
if the person publishes several tables of the same population, or crosses two dimensions,
a hidden count may still be derivable across tables; that check stays with the person.

Output: rates with Wilson 95 percent intervals, the difference in percentage points and the
ratio against the reference subgroup the person names, and each subgroup's share of the eligible
and of the reached. No verdicts: whether a difference matters is the person's rule.
"""
import argparse
import csv
import json
import math
import sys

UNKNOWN = {"not recorded", "unknown", "missing", "not stated", "declined"}


def wilson(k, n, z=1.959964):
    if n == 0:
        return None, None
    p = k / n
    den = 1 + z * z / n
    center = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, center - half), min(1.0, center + half)


def to_int(v, field, row_no, optional=False):
    v = (v or "").strip()
    if v == "":
        if optional:
            return None
        sys.exit(f"Row {row_no}: '{field}' is empty. Every row needs eligible and reached counts.")
    try:
        x = int(v)
    except ValueError:
        sys.exit(f"Row {row_no}: '{field}' must be a whole count, got '{v}'. Rates and percentages are not accepted; give counts.")
    if x < 0:
        sys.exit(f"Row {row_no}: '{field}' is negative.")
    return x


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        need = {"dimension", "subgroup", "eligible", "reached"}
        missing = need - set(r.fieldnames or [])
        if missing:
            sys.exit(f"Missing columns: {', '.join(sorted(missing))}. Needed: dimension, subgroup, eligible, reached (outcome_n, outcome_met optional).")
        for i, row in enumerate(r, start=2):
            d = {
                "dimension": row["dimension"].strip(),
                "subgroup": row["subgroup"].strip(),
                "eligible": to_int(row["eligible"], "eligible", i),
                "reached": to_int(row["reached"], "reached", i),
                "outcome_n": to_int(row.get("outcome_n"), "outcome_n", i, optional=True),
                "outcome_met": to_int(row.get("outcome_met"), "outcome_met", i, optional=True),
            }
            if d["reached"] > d["eligible"]:
                sys.exit(f"Row {i}: reached ({d['reached']}) is larger than eligible ({d['eligible']}).")
            if (d["outcome_n"] is None) != (d["outcome_met"] is None):
                sys.exit(f"Row {i}: give both outcome_n and outcome_met, or neither.")
            if d["outcome_n"] is not None:
                if d["outcome_met"] > d["outcome_n"]:
                    sys.exit(f"Row {i}: outcome_met is larger than outcome_n.")
                if d["outcome_n"] > d["reached"]:
                    sys.exit(f"Row {i}: outcome_n is larger than reached; outcomes are counted among people reached.")
            d["unknown"] = d["subgroup"].lower() in UNKNOWN
            rows.append(d)
    if not rows:
        sys.exit("No rows.")
    return rows


def small(x, k, suppress_zero):
    if x is None:
        return False
    if x == 0:
        return suppress_zero
    return x < k


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--min-cell", type=int, required=True, help="the person's small-cell rule: counts below this are suppressed")
    ap.add_argument("--reference", action="append", default=[], help='"dimension=subgroup", the comparison group the person chose; one per dimension')
    ap.add_argument("--suppress-zero", action="store_true", help="also suppress zero counts, if the person's rule says so")
    ap.add_argument("--json", help="write the results as JSON to this path")
    a = ap.parse_args()
    if a.min_cell < 1:
        sys.exit("--min-cell must be 1 or more.")

    rows = load(a.csv)
    refs = {}
    for r in a.reference:
        if "=" not in r:
            sys.exit(f"--reference '{r}' must look like \"dimension=subgroup\".")
        dim, sub = r.split("=", 1)
        refs[dim.strip()] = sub.strip()

    dims = []
    for r in rows:
        if r["dimension"] not in dims:
            dims.append(r["dimension"])

    k = a.min_cell
    # primary suppression
    for r in rows:
        cells = [r["eligible"], r["reached"], r["eligible"] - r["reached"]]
        rc = cells[:]
        if r["outcome_n"] is not None:
            oc = [r["outcome_n"], r["outcome_met"], r["outcome_n"] - r["outcome_met"]]
        else:
            oc = []
        r["reach_suppressed"] = any(small(x, k, a.suppress_zero) for x in rc)
        r["outcome_suppressed"] = r["reach_suppressed"] or any(small(x, k, a.suppress_zero) for x in oc)
        r["suppression"] = "primary" if r["reach_suppressed"] else ("primary (outcome only)" if r["outcome_suppressed"] and oc else "")

    notes = []
    # complementary suppression within each dimension (reach level)
    for dim in dims:
        grp = [r for r in rows if r["dimension"] == dim]
        sup = [r for r in grp if r["reach_suppressed"]]
        if len(sup) == 1:
            others = sorted([r for r in grp if not r["reach_suppressed"]], key=lambda r: r["eligible"])
            if others:
                o = others[0]
                o["reach_suppressed"] = True
                o["outcome_suppressed"] = True
                o["suppression"] = "complementary"
                notes.append(f"{dim}: '{o['subgroup']}' suppressed as a complement so that '{sup[0]['subgroup']}' cannot be derived from the total.")
        osup = [r for r in grp if r["outcome_suppressed"] and r["outcome_n"] is not None]
        if len(osup) == 1:
            others = sorted([r for r in grp if not r["outcome_suppressed"] and r["outcome_n"] is not None], key=lambda r: r["outcome_n"])
            if others:
                o = others[0]
                o["outcome_suppressed"] = True
                if not o["suppression"]:
                    o["suppression"] = "complementary (outcome only)"
                notes.append(f"{dim}: outcome for '{o['subgroup']}' suppressed as a complement.")

    totals = {}
    results = []
    for dim in dims:
        grp = [r for r in rows if r["dimension"] == dim]
        tot_e = sum(r["eligible"] for r in grp)
        tot_r = sum(r["reached"] for r in grp)
        unk = sum(r["eligible"] for r in grp if r["unknown"])
        totals[dim] = {"eligible": tot_e, "reached": tot_r, "not_recorded_eligible": unk,
                       "not_recorded_share": (unk / tot_e) if tot_e else None}
        ref_name = refs.get(dim)
        ref = None
        if ref_name is not None:
            m = [r for r in grp if r["subgroup"] == ref_name]
            if not m:
                sys.exit(f"Reference '{ref_name}' not found in dimension '{dim}'. Subgroups: {', '.join(r['subgroup'] for r in grp)}")
            ref = m[0]
            if ref["unknown"]:
                sys.exit(f"Reference for '{dim}' is a not-recorded group; choose a named subgroup.")
            if ref["reach_suppressed"]:
                notes.append(f"{dim}: the reference '{ref_name}' is suppressed, so no comparisons are shown for this dimension.")
        else:
            notes.append(f"{dim}: no reference named, so rates are shown without differences or ratios.")
        for r in grp:
            out = {"dimension": dim, "subgroup": r["subgroup"], "not_recorded": r["unknown"],
                   "suppression": r["suppression"] or None,
                   "is_reference": ref is not None and r is ref}
            if r["reach_suppressed"]:
                out.update({"eligible": None, "reached": None, "reach_rate": None})
            else:
                rate = r["reached"] / r["eligible"] if r["eligible"] else None
                lo, hi = wilson(r["reached"], r["eligible"])
                out.update({"eligible": r["eligible"], "reached": r["reached"], "reach_rate": rate,
                            "reach_ci95": [lo, hi],
                            "share_of_eligible": r["eligible"] / tot_e if tot_e else None,
                            "share_of_reached": r["reached"] / tot_r if tot_r else None})
                if ref is not None and not ref["reach_suppressed"] and r is not ref and not r["unknown"] and rate is not None:
                    rr = ref["reached"] / ref["eligible"]
                    out["reach_diff_pp"] = (rate - rr) * 100
                    out["reach_ratio"] = rate / rr if rr else None
            if r["outcome_n"] is not None:
                if r["outcome_suppressed"]:
                    out.update({"outcome_n": None, "outcome_met": None, "outcome_rate": None})
                else:
                    orate = r["outcome_met"] / r["outcome_n"] if r["outcome_n"] else None
                    lo, hi = wilson(r["outcome_met"], r["outcome_n"])
                    out.update({"outcome_n": r["outcome_n"], "outcome_met": r["outcome_met"],
                                "outcome_rate": orate, "outcome_ci95": [lo, hi],
                                "outcome_measured_share_of_reached": r["outcome_n"] / r["reached"] if r["reached"] else None})
                    if (ref is not None and ref["outcome_n"] and not ref["outcome_suppressed"] and r is not ref
                            and not r["unknown"] and orate is not None):
                        ro = ref["outcome_met"] / ref["outcome_n"]
                        out["outcome_diff_pp"] = (orate - ro) * 100
                        out["outcome_ratio"] = orate / ro if ro else None
            results.append(out)

    elig = {d: totals[d]["eligible"] for d in dims}
    if len(set(elig.values())) > 1:
        notes.append("Eligible totals differ between dimensions (" + "; ".join(f"{d}: {v}" for d, v in elig.items()) +
                     "). Check that every dimension counts the same population and period.")

    # print
    def pct(x):
        return "" if x is None else f"{x*100:.1f}%"

    def ci(c):
        return "" if not c or c[0] is None else f"{c[0]*100:.1f} to {c[1]*100:.1f}"

    print(f"Small-cell rule (the person's): counts from 1 to {k - 1} suppressed" + ("; zeros suppressed" if a.suppress_zero else "") + ".")
    print("Aggregate counts only. No verdicts: whether a difference matters is the person's rule.\n")
    for dim in dims:
        t = totals[dim]
        print(f"## {dim}")
        print(f"Eligible {t['eligible']}, reached {t['reached']}; not recorded: {t['not_recorded_eligible']} of eligible ({pct(t['not_recorded_share'])}). Reference: {refs.get(dim, 'none named')}.\n")
        print("| Subgroup | Eligible | Reached | Reach rate (95% CI) | Diff vs ref (pp) | Ratio | Share of eligible / of reached | Outcome met / measured | Outcome rate (95% CI) | Outcome diff (pp) | Suppression |")
        print("|---|---|---|---|---|---|---|---|---|---|---|")
        for o in [x for x in results if x["dimension"] == dim]:
            name = o["subgroup"] + (" (reference)" if o["is_reference"] else "") + (" (value not recorded)" if o["not_recorded"] and o["subgroup"].lower() != "not recorded" else "")
            if o["reach_rate"] is None and o["suppression"]:
                reach = "suppressed"
                el = re = "suppressed"
                share = ""
            else:
                reach = f"{pct(o['reach_rate'])} ({ci(o.get('reach_ci95'))})"
                el, re = str(o["eligible"]), str(o["reached"])
                share = f"{pct(o.get('share_of_eligible'))} / {pct(o.get('share_of_reached'))}"
            diff = "" if o.get("reach_diff_pp") is None else f"{o['reach_diff_pp']:+.1f}"
            ratio = "" if o.get("reach_ratio") is None else f"{o['reach_ratio']:.3f}"
            if "outcome_rate" in o:
                if o["outcome_rate"] is None and (o["outcome_n"] is None):
                    om, orate = "suppressed", "suppressed"
                else:
                    om = f"{o['outcome_met']} / {o['outcome_n']}"
                    orate = f"{pct(o['outcome_rate'])} ({ci(o.get('outcome_ci95'))})"
            else:
                om, orate = "not given", ""
            od = "" if o.get("outcome_diff_pp") is None else f"{o['outcome_diff_pp']:+.1f}"
            print(f"| {name} | {el} | {re} | {reach} | {diff} | {ratio} | {share} | {om} | {orate} | {od} | {o['suppression'] or ''} |")
        print()
    if notes:
        print("Notes:")
        for n in notes:
            print(f"- {n}")
    if a.json:
        with open(a.json, "w") as f:
            json.dump({"min_cell": k, "suppress_zero": a.suppress_zero, "references": refs,
                       "totals": totals, "results": results, "notes": notes}, f, indent=1)


if __name__ == "__main__":
    main()
