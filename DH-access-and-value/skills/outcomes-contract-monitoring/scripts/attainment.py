#!/usr/bin/env python3
"""Outcome attainment under a contract's rules, with data completeness and the payment effect.

Used by tasks A1 (attainment tracking), A2 (data completeness) and B1 (performance review).
It applies the rules the person gives. It never sets a target, a threshold or an owner.

Inputs
  patients.csv  one row per patient (the person's data, de-identified). Columns:
                  patient_id
                  status            active | completed | lost | unaligned   (blank = active)
                  <m>_baseline      baseline value for measure m (blank = missing)
                  <m>_final         end-of-period value (blank = missing)
                  <m>_final_day     optional: day after start the final value was taken
                  <m>_self_report   optional: yes/no, whether the final value was self-reported
  rules.json    the contract's rules, in the person's numbers:
  {
    "mode": "patient_all_or_nothing",          # or "population_average"
    "measures": {
      "phq9": {"target": {"type": "reduction", "value": 5},
               "applies_if": {"baseline_min": 10},
               "target_below": {"type": "final_below", "value": 10},   # optional: target for a
                                       # baseline under baseline_min (ACCESS BH control target);
                                       # without it the measure is not required (not_applicable)
               "allow_self_report": true,
               "final_window_days": 425,
               "population_target": {"type": "mean_reduction", "value": 3},  # population mode only
               "weight": 0.5}                                                   # population mode only
    },
    "not_applicable": "drop_measure",           # patient below applies_if: measure not required
    "missing_counts_as": "failure",             # or "exclude" (patient leaves the denominator)
    "lost_in_denominator": true,                # lost / unaligned patients stay in the denominator
    "threshold": 0.5,                           # patient mode: share of patients that must succeed
    "payment": {"full_amount": 144, "currency": "USD", "patients_paid": 20,   # ACCESS: the Medicare portion
                # (80 percent of the allowed amount; BH initial $144 of $180), never the allowed amount
                "type": "withhold_proportional", "max_reduction": 0.5}
                # or {"type": "fixed_plus_outcome", "outcome_share": 0.2, "curve": "linear"}
                # population mode: {"type": "per_measure", "outcome_share": 0.2}
  }

Target types: reduction (baseline - final >= value), final_below (final < value),
pct_reduction ((baseline - final) / baseline >= value), any_of (list of conditions).

Output: completeness table, per-measure results, attainment rate under the contract's rules
and under the alternative treatment of missing data (sensitivity), and the payment factor.
Everything is a computation on the person's data and rules, not a finding about the product.

Usage: python3 attainment.py patients.csv rules.json [--json]
"""
import argparse
import csv
import json
import sys


def num(v):
    v = (v or "").strip()
    if v == "":
        return None
    return float(v)


def meets(target, base, final):
    t = target["type"]
    if t == "any_of":
        return any(meets(c, base, final) for c in target["conditions"])
    if t == "final_below":
        return final < target["value"]
    if base is None:
        return None
    if t == "reduction":
        return (base - final) >= target["value"]
    if t == "pct_reduction":
        return base != 0 and (base - final) / base >= target["value"]
    raise ValueError(f"unknown target type {t}")


def needs_baseline(target):
    if target["type"] == "any_of":
        return any(needs_baseline(c) for c in target["conditions"])
    return target["type"] != "final_below"


def measure_result(row, m, rule):
    """Return one of: met, not_met, missing_baseline, missing_final, out_of_window,
    self_report_not_allowed, not_applicable."""
    base = num(row.get(f"{m}_baseline"))
    final = num(row.get(f"{m}_final"))
    applies = rule.get("applies_if", {})
    target = rule["target"]
    if "baseline_min" in applies:
        if base is None:
            return "missing_baseline"
        if base < applies["baseline_min"]:
            if not rule.get("target_below"):
                return "not_applicable"
            target = rule["target_below"]
    if base is None and needs_baseline(target):
        return "missing_baseline"
    if final is None:
        return "missing_final"
    day = num(row.get(f"{m}_final_day"))
    if day is not None and "final_window_days" in rule and day > rule["final_window_days"]:
        return "out_of_window"
    sr = (row.get(f"{m}_self_report") or "").strip().lower()
    if sr in ("yes", "y", "true", "1") and not rule.get("allow_self_report", True):
        return "self_report_not_allowed"
    return "met" if meets(target, base, final) else "not_met"


MISSING = {"missing_baseline", "missing_final", "out_of_window", "self_report_not_allowed"}


def payment_factor(pay, rate, threshold):
    kind = pay["type"]
    if kind == "withhold_proportional":
        if rate >= threshold:
            return 1.0
        return max(1.0 - float(pay.get("max_reduction", 1.0)), rate / threshold)
    if kind == "fixed_plus_outcome":
        share = float(pay["outcome_share"])
        part = min(1.0, rate / threshold) if pay.get("curve", "linear") == "linear" else (1.0 if rate >= threshold else 0.0)
        return (1 - share) + share * part
    raise ValueError(f"unknown payment type {kind}")


def patient_mode(rows, rules, missing_as):
    measures = rules["measures"]
    lost_in = rules.get("lost_in_denominator", True)
    per_patient = []
    for r in rows:
        status = (r.get("status") or "active").strip().lower()
        res = {m: measure_result(r, m, rule) for m, rule in measures.items()}
        required = {m: v for m, v in res.items() if v != "not_applicable"}
        if status in ("lost", "unaligned") and not lost_in:
            outcome = "excluded (lost, rule keeps out of denominator)"
        elif not required:
            outcome = "no required measure"
        elif any(v in MISSING for v in required.values()):
            outcome = "failure (missing data)" if missing_as == "failure" else "excluded (missing data)"
        elif all(v == "met" for v in required.values()):
            outcome = "success"
        else:
            outcome = "failure (target not met)"
        per_patient.append({"patient_id": r.get("patient_id"), "status": status, "measures": res, "outcome": outcome})
    denom = [p for p in per_patient if p["outcome"].startswith(("success", "failure"))]
    succ = [p for p in denom if p["outcome"] == "success"]
    rate = len(succ) / len(denom) if denom else None
    return per_patient, len(succ), len(denom), rate


def population_mode(rows, rules):
    out = {}
    for m, rule in rules["measures"].items():
        changes, missing = [], 0
        for r in rows:
            res = measure_result(r, m, rule)
            if res == "not_applicable":
                continue
            if res in MISSING:
                missing += 1
                continue
            changes.append(num(r.get(f"{m}_baseline")) - num(r.get(f"{m}_final")))
        pt = rule.get("population_target")
        mean = sum(changes) / len(changes) if changes else None
        met = None
        if pt and mean is not None:
            if pt["type"] == "mean_reduction":
                met = mean >= pt["value"]
            else:
                raise ValueError(f"unknown population target {pt['type']}")
        out[m] = {"n_with_data": len(changes), "n_missing": missing,
                  "mean_reduction": round(mean, 2) if mean is not None else None,
                  "population_target": pt, "met": met, "weight": rule.get("weight")}
    return out


def completeness(rows, measures):
    table = {}
    for m in measures:
        c = {"patients": len(rows), "baseline_present": 0, "final_present": 0, "both_present": 0,
             "self_reported_final": 0, "out_of_window": 0}
        for r in rows:
            b, f = num(r.get(f"{m}_baseline")), num(r.get(f"{m}_final"))
            c["baseline_present"] += b is not None
            c["final_present"] += f is not None
            c["both_present"] += (b is not None and f is not None)
            if (r.get(f"{m}_self_report") or "").strip().lower() in ("yes", "y", "true", "1"):
                c["self_reported_final"] += 1
            if measure_result(r, m, measures[m]) == "out_of_window":
                c["out_of_window"] += 1
        table[m] = c
    status = {}
    for r in rows:
        s = (r.get("status") or "active").strip().lower()
        status[s] = status.get(s, 0) + 1
    return table, status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("patients")
    ap.add_argument("rules")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    with open(a.patients, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    with open(a.rules, encoding="utf-8") as fh:
        rules = json.load(fh)
    comp, status = completeness(rows, rules["measures"])
    report = {"completeness": comp, "status_counts": status, "mode": rules["mode"]}
    pay = rules.get("payment")
    if rules["mode"] == "patient_all_or_nothing":
        missing_as = rules.get("missing_counts_as", "failure")
        per, s, d, rate = patient_mode(rows, rules, missing_as)
        alt = "exclude" if missing_as == "failure" else "failure"
        _, s2, d2, rate2 = patient_mode(rows, rules, alt)
        report.update({"per_patient": per, "successes": s, "denominator": d, "attainment_rate": rate,
                       "threshold": rules.get("threshold"),
                       "sensitivity": {"missing_counts_as": alt, "successes": s2, "denominator": d2, "attainment_rate": rate2}})
        if pay and rate is not None:
            f = payment_factor(pay, rate, rules["threshold"])
            report["payment"] = {"factor": round(f, 4), "per_patient": round(pay["full_amount"] * f, 2)}
            if rate2 is not None:
                report["sensitivity"]["payment_factor"] = round(payment_factor(pay, rate2, rules["threshold"]), 4)
            if "patients_paid" in pay:
                report["payment"]["total"] = round(pay["full_amount"] * f * pay["patients_paid"], 2)
    elif rules["mode"] == "population_average":
        res = population_mode(rows, rules)
        report["measures"] = res
        if pay and pay.get("type") == "per_measure":
            share = float(pay["outcome_share"])
            paid = sum((v["weight"] or 0) for v in res.values() if v["met"])
            report["payment"] = {"factor": round((1 - share) + share * paid, 4)}
    else:
        raise ValueError("mode must be patient_all_or_nothing or population_average")

    if a.json:
        json.dump(report, sys.stdout, indent=2)
        print()
        return
    print("Computation on the person's data and rules. Not a finding about the product.\n")
    print("Completeness by measure")
    print("| Measure | Patients | Baseline present | Final present | Both | Self-reported final | Out of window |")
    print("|---|---|---|---|---|---|---|")
    for m, c in comp.items():
        print(f"| {m} | {c['patients']} | {c['baseline_present']} | {c['final_present']} | {c['both_present']} | {c['self_reported_final']} | {c['out_of_window']} |")
    print("\nStatus counts: " + ", ".join(f"{k} {v}" for k, v in sorted(status.items())))
    if rules["mode"] == "patient_all_or_nothing":
        print("\nPatient results")
        print("| Patient | Status | " + " | ".join(rules["measures"]) + " | Outcome |")
        print("|---|---|" + "---|" * len(rules["measures"]) + "---|")
        for p in report["per_patient"]:
            print(f"| {p['patient_id']} | {p['status']} | " + " | ".join(p["measures"][m] for m in rules["measures"]) + f" | {p['outcome']} |")
        r = report["attainment_rate"]
        sv = report["sensitivity"]
        print(f"\nAttainment under the contract's rules: {report['successes']} of {report['denominator']}"
              + (f" = {r:.1%}" if r is not None else " (no denominator)") + f"; threshold {report['threshold']:.0%}")
        if sv["attainment_rate"] is not None:
            print(f"If missing data were treated as '{sv['missing_counts_as']}': {sv['successes']} of {sv['denominator']} = {sv['attainment_rate']:.1%}")
        if "payment" in report:
            pm = report["payment"]
            line = f"Payment factor {pm['factor']:.0%}; per patient {pm['per_patient']:.2f} {pay.get('currency', '')}"
            if "total" in pm:
                line += f"; total {pm['total']:.2f}"
            print(line)
            if "payment_factor" in sv:
                print(f"Payment factor under the alternative missing-data treatment: {sv['payment_factor']:.0%}")
    else:
        print("\nPopulation results")
        print("| Measure | With data | Missing | Mean reduction | Target | Met |")
        print("|---|---|---|---|---|---|")
        for m, v in report["measures"].items():
            pt = v['population_target']
            pt_txt = f"{pt['type']} >= {pt['value']}" if pt else "no rule set"
            met = {True: "met", False: "not met", None: "not measurable"}[v['met']]
            print(f"| {m} | {v['n_with_data']} | {v['n_missing']} | {v['mean_reduction']} | {pt_txt} | {met} |")
        if "payment" in report:
            print(f"Payment factor {report['payment']['factor']:.0%}")


if __name__ == "__main__":
    main()
