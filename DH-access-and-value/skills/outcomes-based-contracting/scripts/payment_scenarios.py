#!/usr/bin/env python3
"""Payment scenarios: what each risk-share design pays at a range of attainment rates.

Used by task A2 (risk-share options) and B1 (contract structuring) to make the payment
link of each design visible before anyone negotiates it. It computes; it does not choose.

Input: a JSON file with the person's designs and the attainment rates to test.

{
  "full_amount": 144.0,               # payment base per patient at full attainment (the person's figure).
                                      # For ACCESS this is the Medicare portion, 80 percent of the allowed
                                      # amount (BH initial $144 of $180), never the allowed amount itself
  "basis": "ACCESS BH initial Medicare portion",   # optional, printed with the table
  "currency": "USD",
  "patients": 1000,                   # optional, for totals
  "attainment_rates": [0.2, 0.4, 0.5, 0.7],
  "designs": [
    {"id": "withhold", "type": "withhold_proportional",
     "threshold": 0.5, "max_reduction": 0.5,
     "label": "ACCESS-style: proportional below threshold, reduction capped"},
    {"id": "de20", "type": "fixed_plus_outcome",
     "outcome_share": 0.2, "threshold": 0.5, "curve": "linear",
     "label": "Fixed part plus outcome-linked share"}
  ]
}

Design types
  withhold_proportional  factor = 1 at or above threshold; below it, attainment / threshold,
                         but never lower than 1 - max_reduction. (The ACCESS clinical outcome
                         adjustment: (OAR / OAT) x full payment, reduction capped at 50 percent.)
  fixed_plus_outcome     (1 - outcome_share) is always paid. The outcome share is paid times
                         a factor: "linear" = min(1, attainment / threshold); "step" = 1 at or
                         above threshold, else 0.

Every number in the input is the person's or a labeled public anchor. Output is a hypothesis
on those inputs, not a forecast or a price.

Usage: python3 payment_scenarios.py designs.json [--json]
"""
import argparse
import json
import sys


def factor(design, rate):
    kind = design["type"]
    threshold = float(design["threshold"])
    if threshold <= 0 or threshold > 1:
        raise ValueError(f"{design['id']}: threshold must be in (0, 1]")
    if kind == "withhold_proportional":
        max_red = float(design.get("max_reduction", 1.0))
        if rate >= threshold:
            return 1.0
        return max(1.0 - max_red, rate / threshold)
    if kind == "fixed_plus_outcome":
        share = float(design["outcome_share"])
        curve = design.get("curve", "linear")
        if curve == "linear":
            part = min(1.0, rate / threshold)
        elif curve == "step":
            part = 1.0 if rate >= threshold else 0.0
        else:
            raise ValueError(f"{design['id']}: unknown curve {curve}")
        return (1.0 - share) + share * part
    raise ValueError(f"{design['id']}: unknown design type {kind}")


def run(spec):
    full = float(spec["full_amount"])
    patients = spec.get("patients")
    rows = []
    for design in spec["designs"]:
        for rate in spec["attainment_rates"]:
            rate = float(rate)
            if not 0 <= rate <= 1:
                raise ValueError("attainment rates must be between 0 and 1")
            f = factor(design, rate)
            row = {
                "design": design["id"],
                "label": design.get("label", ""),
                "attainment": rate,
                "share_of_full": round(f, 4),
                "per_patient": round(full * f, 2),
                "at_risk_lost_per_patient": round(full * (1 - f), 2),
            }
            if patients:
                row["total"] = round(full * f * float(patients), 2)
            rows.append(row)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    with open(args.spec, encoding="utf-8") as fh:
        spec = json.load(fh)
    rows = run(spec)
    if args.json:
        json.dump(rows, sys.stdout, indent=2)
        print()
        return
    cur = spec.get("currency", "")
    basis = f" ({spec['basis']})" if spec.get("basis") else ""
    print(f"Hypothesis on the inputs given. Payment base per patient: {spec['full_amount']} {cur}{basis}.")
    head = "| Design | Attainment | Share of full | Per patient | Lost per patient |"
    if spec.get("patients"):
        head += " Total |"
    print(head)
    print("|" + "---|" * (head.count("|") - 1))
    for r in rows:
        line = (f"| {r['design']} | {r['attainment']:.0%} | {r['share_of_full']:.0%} | "
                f"{r['per_patient']:.2f} | {r['at_risk_lost_per_patient']:.2f} |")
        if "total" in r:
            line += f" {r['total']:.2f} |"
        print(line)


if __name__ == "__main__":
    main()
