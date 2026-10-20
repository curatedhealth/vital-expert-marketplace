#!/usr/bin/env python3
"""Check a description of the person's economic model against one body's rule set.

Usage:
  python3 model_check.py --spec model.json --body NICE_ROUTINE [--body HAS ...]
                         [--thresholds 20000 30000] [--as-of 2026-10-19]

Bodies: NICE_ROUTINE, NICE_EARLY, ESF, HAS, IQWIG, ICER_PHTI, BIA, CHEERS.
The spec is a JSON object written from the person's model report (see
references/economic-case-checklist.md for the fields). A field the spec does not
hold prints [GAP]; the script never fills one in.

Prints, per item: id, status (shown, not shown, departure, [GAP], not applicable),
what was found, and the row id. Then the arithmetic on the person's numbers:
incremental ratio, net monetary benefit and switching values at thresholds the
person passes. Thresholds are the person's; the body's written ranges are printed
as context with their rows, never compared.

Rules as read on 19 October 2026 (references/health-economics-methods-research.md).
"""
import argparse
import json
import sys

GAP = "[GAP]"
PMG51_DATE = "2026-08-27"  # HE-057


def g(spec, path):
    cur = spec
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur or cur[part] is None:
            return None
        cur = cur[part]
    return cur


# Rows that rest on a published paper ([PAPER] in the research file or in
# references/economic-case-checklist.md): the DOI travels with the row id.
PAPER_DOI = {**{f"HE-{n:03d}": "[PAPER] DOI 10.1177/23814683211061097" for n in range(1, 15)},
             **{f"HE-{n:03d}": "[PAPER] DOI 10.1016/j.jval.2013.08.2291, abstract only" for n in range(18, 25)}}


def with_doi(rows):
    out = []
    for r in [x.strip() for x in rows.split(",")]:
        out.append(f"{r} ({PAPER_DOI[r]})" if r in PAPER_DOI else r)
    return ", ".join(out)


def row(item, status, found, rows):
    return {"item": item, "status": status, "found": found, "rows": with_doi(rows)}


def low(v):
    return str(v).strip().lower() if v is not None else None


def check_rate(item, spec, fields, expected, rows, extra=""):
    vals = [g(spec, f) for f in fields]
    if any(v is None for v in vals):
        return row(item, GAP, "rate not stated in the material", rows)
    if all(abs(float(v) - expected) < 1e-9 for v in vals):
        return row(item, "shown", f"{vals} percent", rows)
    return row(item, "departure", f"{vals} percent against {expected} percent{extra}", rows)


def nice_routine(spec):
    out = []
    rc = g(spec, "reference_case")
    out.append(row("N1 Reference case", GAP if rc is None else ("shown" if rc else "not shown"),
                   f"reference_case={rc}", "HE-035"))
    et = low(g(spec, "evaluation_type"))
    if et is None:
        out.append(row("N2 Evaluation type", GAP, "not stated", "HE-073"))
    elif et in ("cost-utility", "cua", "cost-comparison", "cost comparison"):
        out.append(row("N2 Evaluation type", "shown", et, "HE-073"))
    else:
        out.append(row("N2 Evaluation type", "departure", f"{et}; NICE prefers cost-utility or cost-comparison", "HE-073"))
    cp = low(g(spec, "cost_perspective"))
    if cp is None:
        out.append(row("N3 Cost perspective", GAP, "not stated", "HE-037"))
    elif "nhs" in cp:
        out.append(row("N3 Cost perspective", "shown", cp, "HE-037"))
    else:
        out.append(row("N3 Cost perspective", "departure", f"{cp}; reference case is NHS and PSS", "HE-037"))
    pb = g(spec, "productivity_in_base")
    out.append(row("N4 Productivity", GAP if pb is None else ("departure" if pb else "shown"),
                   f"productivity_in_base={pb}", "HE-038"))
    hy, hj = g(spec, "horizon_years"), g(spec, "horizon_justified")
    if hy is None:
        out.append(row("N5 Time horizon", GAP, "horizon not stated", "HE-040"))
    else:
        out.append(row("N5 Time horizon", "shown" if hj else (GAP if hj is None else "not shown"),
                       f"{hy} years; justification {'given' if hj else 'not stated' if hj is None else 'not given'}", "HE-040"))
    om, ui = low(g(spec, "outcome_measure")), low(g(spec, "utility_instrument"))
    if om is None or ui is None:
        out.append(row("N6 Health effects", GAP, f"outcome={om}, instrument={ui}", "HE-043, HE-044"))
    elif "qaly" in om and "eq-5d" in ui:
        out.append(row("N6 Health effects", "shown", f"{om}, {ui}", "HE-043, HE-044"))
    else:
        out.append(row("N6 Health effects", "departure", f"{om}, {ui}", "HE-043, HE-044"))
    vs, tl = low(g(spec, "value_set")), g(spec, "topic_launched")
    if vs is None:
        out.append(row("N7 Value set", GAP, "value set not stated", "HE-058, HE-063"))
    elif tl is None:
        out.append(row("N7 Value set", GAP, f"{vs}; NICE topic launch date not known, so PMG51 applicability open", "HE-062, HE-063"))
    elif tl >= PMG51_DATE:
        ok = "uk" in vs and "5l" in vs
        out.append(row("N7 Value set", "shown" if ok else "departure",
                       f"{vs}; topic launched {tl}: UK 5L set required", "HE-058, HE-062"))
    else:
        ok = "3l" in vs
        out.append(row("N7 Value set", "shown" if ok else "departure",
                       f"{vs}; topic launched {tl}: ongoing topics map 5L to 3L", "HE-063"))
    mp = g(spec, "mapping")
    out.append(row("N8 Mapping", "not applicable" if mp is False else (GAP if mp is None else "departure"),
                   "no mapping" if mp is False else f"mapping={mp}; declare, describe, justify, show fit", "HE-045"))
    out.append(check_rate("N9 Discounting", spec, ["discount_costs", "discount_effects"], 3.5, "HE-047, HE-048",
                          "; 1.5 percent only if all three PMG36 criteria hold"))
    rr = [low(x) for x in (g(spec, "results_reported") or [])]
    if not rr:
        out.append(row("N10 Results", GAP, "results reported not stated", "HE-041"))
    else:
        has_icer = any("icer" in x for x in rr)
        has_nhb = any("net health benefit" in x or "nhb" in x for x in rr)
        out.append(row("N10 Results", "shown" if has_icer and has_nhb else "not shown",
                       f"ICER {'yes' if has_icer else 'no'}, net health benefit {'yes' if has_nhb else 'no'}", "HE-041"))
    ri = g(spec, "rapidly_iterating")
    if ri is None:
        out.append(row("N11 Switching values", GAP, "whether the technology iterates rapidly is not stated", "HE-077"))
    elif not ri:
        out.append(row("N11 Switching values", "not applicable", "not rapidly iterating (person's statement)", "HE-077"))
    else:
        sv = g(spec, "switching_value_reported")
        out.append(row("N11 Switching values", GAP if sv is None else ("shown" if sv else "not shown"), f"switching_value_reported={sv}", "HE-077"))
    return out


def nice_early(spec):
    out = nice_routine(spec)
    for item, field, rows in [("E1 Purpose", "early_use_objectives", "HE-068"),
                              ("E2 Approach", "simplified_approach", "HE-069"),
                              ("E3 Deviations discussed with NICE", "deviations_discussed", "HE-070"),
                              ("E4 Uncertainties resolvable within 3 years", "uncertainties_resolvable_3y", "HE-072")]:
        v = g(spec, field)
        out.append(row(item, GAP if v is None else ("shown" if v else "not shown"), f"{field}={v}", rows))
    return out


def esf(spec):
    out = []
    v = g(spec, "expected_impacts_vs_current_care")
    out.append(row("S13 Expected impacts vs current care", GAP if v is None else ("shown" if v else "not shown"), f"{v}", "HE-086"))
    bp = g(spec, "bia.present")
    out.append(row("S17 BIA present", GAP if bp is None else ("shown" if bp else "not shown"), f"bia.present={bp}", "HE-087"))
    if bp:
        parts = ["population", "uptake", "technology_costs", "implementation_costs", "comparator_costs", "indirect_costs"]
        missing = [p for p in parts if not g(spec, f"bia.{p}")]
        unknown = [p for p in parts if g(spec, f"bia.{p}") is None]
        st = "shown" if not missing else (GAP if len(unknown) == len(missing) else "not shown")
        out.append(row("S17b BIA content (tiers B and C)", st, "missing: " + (", ".join(missing) or "none"), "HE-088"))
        cc = low(g(spec, "bia.cost_country"))
        out.append(row("S17c UK NHS and PSS costs", GAP if cc is None else ("shown" if cc in ("uk", "england", "nhs") else "not shown"),
                       f"costs from {cc}", "HE-089"))
    hf = g(spec, "higher_financial_risk")
    if hf is None:
        out.append(row("S18 Cost-effectiveness analysis", GAP, "higher financial risk not judged; the commissioner and owner judge it", "HE-090"))
    elif not hf:
        out.append(row("S18 Cost-effectiveness analysis", "not applicable", "owner judged not higher financial risk", "HE-090"))
    else:
        et = low(g(spec, "evaluation_type"))
        ok = et in ("cost-utility", "cua", "cost-consequences", "cca", "cost-comparison", "cost comparison")
        out.append(row("S18 Cost-effectiveness analysis", GAP if et is None else ("shown" if ok else "not shown"), f"{et}", "HE-090, HE-091"))
    return out


def has(spec):
    out = []
    cp = low(g(spec, "cost_perspective"))
    if cp is None:
        out.append(row("F1 Perspective", GAP, "not stated", "HE-103"))
    elif "collective" in cp:
        out.append(row("F1 Perspective", "shown", cp, "HE-103"))
    elif "societal" in cp:
        out.append(row("F1 Perspective", GAP, f"{cp} stated; whether it is the HAS collective perspective (all individuals or institutions affected) is not shown; check the methods section", "HE-103"))
    else:
        out.append(row("F1 Perspective", "departure", f"{cp}; a healthcare-system perspective must be justified", "HE-103"))
    et = low(g(spec, "evaluation_type"))
    out.append(row("F2 Evaluation type", GAP if et is None else ("shown" if et in ("cost-utility", "cua") else "departure"), f"{et}", "HE-104"))
    hy = g(spec, "horizon_years")
    if hy is not None and float(hy) <= 1:
        out.append(row("F3 Discounting", "not applicable", f"horizon {hy} years (12 months or less)", "HE-105"))
    else:
        out.append(check_rate("F3 Discounting", spec, ["discount_costs", "discount_effects"], 2.5, "HE-105",
                              "; rate falls after 30 years to a 1.5 percent floor"))
    ui, vs = low(g(spec, "utility_instrument")), low(g(spec, "value_set"))
    if ui is None or vs is None:
        out.append(row("F4 Utilities", GAP, f"instrument={ui}, value set={vs}", "HE-106"))
    else:
        ok = "eq-5d-5l" in ui and "fr" in vs
        out.append(row("F4 Utilities", "shown" if ok else "departure", f"{ui}, {vs}; French 5L set expected", "HE-106"))
    rr = [low(x) for x in (g(spec, "results_reported") or [])]
    if not rr:
        out.append(row("F5 Results", GAP, "not stated", "HE-107"))
    else:
        fr = any("frontier" in x for x in rr)
        out.append(row("F5 Results", "shown" if fr else "not shown", f"frontier {'yes' if fr else 'no'}; transfers between funders: check", "HE-107"))
    return out


def iqwig(spec):
    out = []
    cp = low(g(spec, "cost_perspective"))
    out.append(row("G1 Perspective", GAP if cp is None else ("shown" if "shi" in cp or "statutory" in cp else "departure"), f"{cp}", "HE-110"))
    r = check_rate("G2 Discounting", spec, ["discount_costs"], 3.0, "HE-111")
    sens = g(spec, "discount_sensitivity")
    r["found"] += f"; sensitivity {sens if sens is not None else 'not stated'} (0 and 5 expected)"
    out.append(r)
    bh = g(spec, "bia.horizon_years")
    out.append(row("G3 BIA at least 3 years", GAP if bh is None else ("shown" if float(bh) >= 3 else "not shown"), f"BIA horizon {bh}", "HE-112"))
    return out


def icer_phti(spec):
    out = []
    bp, bh = g(spec, "bia.present"), g(spec, "bia.horizon_years")
    if bp is None:
        out.append(row("P1 Budget impact first", GAP, "BIA not stated", "HE-121, HE-122"))
    elif not bp:
        out.append(row("P1 Budget impact first", "not shown", "no BIA", "HE-121, HE-122"))
    else:
        sc = g(spec, "bia.scenarios")
        out.append(row("P1 Budget impact first", "shown" if bh is not None and float(bh) >= 1 else GAP,
                       f"BIA horizon {bh} years; scenarios {sc}", "HE-121, HE-122"))
    pp = [low(x) for x in (g(spec, "bia.perspectives") or [])]
    out.append(row("P2 Perspectives", GAP if not pp else ("shown" if any("payer" in x or "plan" in x for x in pp) and any("user" in x or "patient" in x for x in pp) else "not shown"),
                   f"{pp}", "HE-123"))
    ce = g(spec, "comparative_effectiveness_source")
    out.append(row("P3 Clinical anchor", GAP if ce is None else "shown", f"{ce}", "HE-115"))
    return out


def bia(spec):
    out = []
    for item, fields, rows in [("B1 Elements", ["bia.population", "bia.mix_before_after"], "HE-019"),
                               ("B3 Decision-maker scenarios", ["bia.scenarios"], "HE-022"),
                               ("B4 Validation", ["bia.validated"], "HE-023"),
                               ("B5 Replicable reporting", ["bia.replicable"], "HE-024")]:
        vals = [g(spec, f) for f in fields]
        st = GAP if any(v is None for v in vals) else ("shown" if all(vals) else "not shown")
        out.append(row(item, st, ", ".join(f"{f}={v}" for f, v in zip(fields, vals)), rows))
    cc = g(spec, "bia.cost_country")
    tc = g(spec, "target_country")
    if cc is None or tc is None:
        out.append(row("B2 Local data", GAP, f"costs from {cc}, decision maker in {tc}", "HE-021"))
    else:
        out.append(row("B2 Local data", "shown" if low(cc) == low(tc) else "not shown", f"costs from {cc}, decision maker in {tc}", "HE-021"))
    return out


CHEERS = [("4", "item4", "HE-006"), ("8 to 10", "item8_10", "HE-007"), ("15", "item15", "HE-008"),
          ("16", "item16", "HE-009"), ("17", "item17", "HE-010"), ("19 and 20", "item19_20", "HE-011"),
          ("21 and 25", "item21_25", "HE-012"), ("24", "item24", "HE-013"), ("27 and 28", "item27_28", "HE-014")]


def cheers(spec):
    out = []
    for num, field, rows in CHEERS:
        v = g(spec, f"cheers.{field}")
        out.append(row(f"CHEERS item {num}", GAP if v is None else ("reported" if v else "not reported"), f"{field}={v}", rows))
    return out


BODIES = {"NICE_ROUTINE": nice_routine, "NICE_EARLY": nice_early, "ESF": esf, "HAS": has,
          "IQWIG": iqwig, "ICER_PHTI": icer_phti, "BIA": bia, "CHEERS": cheers}

CONTEXT = {
    "NICE_ROUTINE": "Written ranges (context, not a test): PMG48 2.4.4 GBP 20,000 / 20,000 to 30,000 per QALY (HE-074); PMG36 GBP 25,000 / 35,000 (HE-050, HE-051). Open conflict; NICE decides.",
    "NICE_EARLY": "Written ranges (context, not a test): PMG48 2.4.4 GBP 20,000 / 20,000 to 30,000 per QALY (HE-074); PMG36 GBP 25,000 / 35,000 (HE-050, HE-051). Open conflict; NICE decides.",
    "HAS": "HAS sets no threshold in the passages read (HE-107).",
    "ICER_PHTI": "ICER-PHTI emphasizes budget impact over long-term cost-effectiveness (HE-121); its threshold price is ICER's computation and is not run here (HE-124).",
}


def arithmetic(spec, thresholds):
    lines = []
    dc, dq = g(spec, "inc_cost"), g(spec, "inc_qaly")
    cur = g(spec, "currency") or "[currency GAP]"
    if dc is None or dq is None:
        return ["Arithmetic: [GAP] incremental cost or incremental QALYs not supplied."]
    dc, dq = float(dc), float(dq)
    lines.append(f"Inputs (the person's or the paper's, as supplied): incremental cost {dc:,.2f} {cur}; incremental QALYs {dq:.4f}.")
    if dq == 0:
        lines.append("Incremental ratio: undefined (no QALY difference).")
    else:
        ratio = dc / dq
        if dc < 0 < dq:
            lines.append(f"Incremental ratio {ratio:,.0f} {cur} per QALY: lower cost and more QALYs on the point estimates; a negative ratio is not ranked against a threshold. Report the intervals.")
        else:
            lines.append(f"Incremental ratio: {ratio:,.0f} {cur} per QALY (point estimates).")
    ci = g(spec, "inc_cost_ci")
    if ci and len(ci) == 2 and float(ci[0]) < 0 < float(ci[1]):
        lines.append(f"Cost interval {ci[0]} to {ci[1]} includes zero: a claim of significantly lower or higher cost is not supported by this interval.")
    qci = g(spec, "inc_qaly_ci")
    if qci and len(qci) == 2 and float(qci[0]) < 0 < float(qci[1]):
        lines.append(f"QALY interval {qci[0]} to {qci[1]} includes zero.")
    rep = g(spec, "reported_icer")
    if rep is not None:
        lines.append(f"The source reports its own ratio: {rep}. Use the source's figure; a difference from the line above comes from rounded published point estimates or bootstrapping.")
    if thresholds:
        lines.append(f"Thresholds below are the person's, taken in the model's currency ({cur}).")
    for t in thresholds:
        nmb = dq * t - dc
        lines.append(f"At the person's threshold {t:,.0f} {cur}/QALY: net monetary benefit {nmb:,.2f} {cur} per patient. "
                     f"Net monetary benefit reaches zero if incremental cost rises to {dq * t:,.2f}, or if incremental QALYs fall to {dc / t:.4f} (switching values, other input held).")
    lines.append("All of the above are computations on supplied numbers (hypotheses), not a body's conclusion.")
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--body", action="append", required=True, choices=sorted(BODIES))
    ap.add_argument("--thresholds", nargs="*", type=float, default=[])
    ap.add_argument("--as-of", default="2026-10-19")
    a = ap.parse_args()
    spec = json.load(open(a.spec))
    print(f"Model check as of {a.as_of}; rules read 19 October 2026. Model: {spec.get('label', '[unnamed]')}")
    for b in a.body:
        res = BODIES[b](spec)
        print(f"\n== {b} ==")
        print("| Item | Status | Found | Row |\n|---|---|---|---|")
        for r in res:
            print(f"| {r['item']} | {r['status']} | {r['found']} | {r['rows']} |")
        counts = {}
        for r in res:
            counts[r["status"]] = counts.get(r["status"], 0) + 1
        print("Counts (not a score): " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
        if b in CONTEXT:
            print(CONTEXT[b])
    print("\n== Arithmetic ==")
    for line in arithmetic(spec, a.thresholds):
        print(line)


if __name__ == "__main__":
    sys.exit(main())
