#!/usr/bin/env python3
"""Reads the person's own model records and monitoring logs (model-performance-and-drift-monitoring).

Commands
  records     python3 drift_check.py records --register REGISTER.csv --as-of YYYY-MM-DD [--rule RULE.json]
  drift       python3 drift_check.py drift --log LOG.csv --reference PERIOD [--thresholds TH.json] [--inputs lactate] [--groups sex]
  adaptation  python3 drift_check.py adaptation --log DECISIONS.csv --rules RULES.csv
  words       python3 drift_check.py words ANSWER.md

No threshold is built in. Drift, calibration, fairness and missing-data thresholds come
only from the person's thresholds file; without one, values and changes are reported and
no flag is raised. Row ids refer to the research files in references/ (DA, US, EU, TM rows).
"""
import argparse
import csv
import json
import math
import re
import sys
from collections import defaultdict
from datetime import date

CAP = 450


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pd(s):
    s = (s or "").strip()
    try:
        return date.fromisoformat(s[:10]) if s else None
    except ValueError:
        return None


def fmt(x, nd=3):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "not computable"
    return f"{x:.{nd}f}"


def blank(v):
    return not (v or "").strip()


# ---------- records ----------

def cmd_records(a):
    rows = read_csv(a.register)
    asof = pd(a.as_of)
    rule = json.load(open(a.rule, encoding="utf-8")) if a.rule else None
    req = set(rule.get("required", [])) if rule and not rule.get("proposed") else set()
    print(f"Model register: {a.register} ({len(rows)} model versions), read as of {a.as_of}.")
    if rule and rule.get("proposed"):
        print("Pass rule file is labeled proposed: not applied.")
    print("Pass rule: " + (f"{', '.join(sorted(req))} (written {rule.get('written_on', 'date not given')})" if req
                           else "not given [GAP]; flags are reported, nothing is marked pass or fail"))
    print("\n| Model | Version | In production | Flags | Against the pass rule |")
    print("|---|---|---|---|---|")
    summary = defaultdict(int)
    for r in rows:
        fl, failed = [], []
        prod = (r.get("in_production") or "").strip().lower() == "yes"
        if blank(r.get("intended_use")) or blank(r.get("decision_named")):
            fl.append("V1 no intended use or no decision named (old DH-01.04.3.1.1: do not validate 'clinical decision support' with no decision named)")
            failed += [x for x in ("intended_use", "decision_named") if x in req]
        ind = (r.get("test_set_independent") or "").strip().lower()
        if ind in ("", "not given", "none"):
            fl.append(f"V2 test set independence {ind or 'not given'} (DA-39 to DA-41; old DH-01.04.3.1.2: do not validate on the training rows)")
            if "test_set_independent" in req:
                failed.append("test_set_independent")
        mn, rd = pd(r.get("metric_named_on")), pd(r.get("run_date"))
        if blank(r.get("metric_prenamed")):
            fl.append("V3 no metric named before the run (old DH-01.04.3.1.3)")
            if "metric_prenamed_before_run" in req:
                failed.append("metric_prenamed_before_run")
        elif mn and rd and mn > rd:
            fl.append(f"V3 metric named {mn.isoformat()}, after the run of {rd.isoformat()} (old DH-01.04.3.1.3: do not add a metric after the run)")
            if "metric_prenamed_before_run" in req:
                failed.append("metric_prenamed_before_run")
        if blank(r.get("subgroup_reported")):
            fl.append("V4 no subgroup result recorded (DA-38, DA-43)")
            if "subgroup_reported" in req:
                failed.append("subgroup_reported")
        if blank(r.get("run_id")):
            fl.append("P1 no run id" + (" on a production model (old DH-01.04.2.2.1: a fail is a production model with no run id)" if prod else ""))
            if "run_id" in req:
                failed.append("run_id")
        if blank(r.get("approver")):
            fl.append("P2 no approver named")
            if "approver" in req:
                failed.append("approver")
        if prod and blank(r.get("watch_signal")):
            fl.append("W1 production model with no drift watch (old DH-01.04.2.2.2: note a model with no watch)")
            if "watch" in req:
                failed.append("watch")
        if not blank(r.get("watch_signal")) and blank(r.get("watch_threshold")):
            fl.append("W2 watch threshold not given")
        fired = pd(r.get("watch_fired_on"))
        if fired:
            if blank(r.get("action_taken")):
                fl.append(f"W3 watch fired {fired.isoformat()} with no action recorded"
                          + " (old DH-01.04.2.2.3: do not leave a fired watch with no action); open")
                summary["open_watches"] += 1
            else:
                fl.append(f"W4 watch fired {fired.isoformat()}; action recorded: {r.get('action_taken')}")
        verdict = "not assessed (pass rule not given)" if not req else (
            "fail: " + ", ".join(sorted(set(failed))) if failed else "pass")
        if req:
            summary["fail" if failed else "pass"] += 1
        print(f"| {r.get('model_id')} | {r.get('version')} | {'yes' if prod else 'no'} | {'; '.join(fl) or 'none'} | {verdict} |")
    if req:
        print(f"\nAgainst the person's rule: {summary['pass']} pass, {summary['fail']} fail.")
    print(f"Open fired watches with no action: {summary['open_watches']}.")
    print("Owners and actions for each miss are the person's (B1).")
    return 0


# ---------- drift ----------

def auroc(y, p):
    pos = [v for t, v in zip(y, p) if t == 1]
    neg = [v for t, v in zip(y, p) if t == 0]
    if not pos or not neg:
        return None
    allv = sorted([(v, 1) for v in pos] + [(v, 0) for v in neg])
    ranks, i = [0.0] * len(allv), 0
    while i < len(allv):
        j = i
        while j + 1 < len(allv) and allv[j + 1][0] == allv[i][0]:
            j += 1
        for k in range(i, j + 1):
            ranks[k] = (i + j) / 2 + 1
        i = j + 1
    rs = sum(r for r, (_, l) in zip(ranks, allv) if l == 1)
    return (rs - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))


def lg(v):
    v = min(max(v, 1e-6), 1 - 1e-6)
    return math.log(v / (1 - v))


def sg(x):
    return 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))


def slope(y, p):
    if len(set(y)) < 2:
        return None
    lp = [lg(v) for v in p]
    b0, b1 = 0.0, 1.0
    for _ in range(100):
        mu = [sg(b0 + b1 * x) for x in lp]
        g0 = sum(t - m for t, m in zip(y, mu))
        g1 = sum((t - m) * x for t, m, x in zip(y, mu, lp))
        w = [m * (1 - m) for m in mu]
        h00, h01, h11 = sum(w), sum(a * x for a, x in zip(w, lp)), sum(a * x * x for a, x in zip(w, lp))
        det = h00 * h11 - h01 * h01
        if abs(det) < 1e-12:
            return None
        d0, d1 = (h11 * g0 - h01 * g1) / det, (-h01 * g0 + h00 * g1) / det
        b0, b1 = b0 + d0, b1 + d1
        if abs(d0) < 1e-10 and abs(d1) < 1e-10:
            break
    return b1


def mean_sd(vals):
    if len(vals) < 2:
        return (vals[0] if vals else None), None
    m = sum(vals) / len(vals)
    return m, math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))


def cmd_drift(a):
    rows = read_csv(a.log)
    th = json.load(open(a.thresholds, encoding="utf-8")) if a.thresholds else {}
    if th.get("proposed"):
        print("Thresholds file is labeled proposed: not applied.")
        th = {}
    inputs = [x for x in (a.inputs or "").split(",") if x]
    groups = [x for x in (a.groups or "").split(",") if x]
    per = defaultdict(list)
    for r in rows:
        per[r["period"]].append(r)
    order = sorted(per)
    if a.reference not in per:
        print(f"Reference period {a.reference} not in the log [GAP]")
        return 1
    print(f"Prediction log: {a.log} ({len(rows)} predictions, periods {', '.join(order)}); reference period {a.reference}.")
    print("Thresholds: " + (f"the person's, written {th.get('written_on', 'date not given')}" if th
                            else "not given; changes are reported and no flag is raised"))
    thr = th.get("threshold")
    print("\nPerformance and calibration by period (outcomes known only)")
    print("| Period | Predictions | Outcomes known | Event rate | Mean predicted | O/E | AUROC | Calibration slope |"
          + (" Sensitivity at your threshold |" if thr is not None else "") + " Flags (your thresholds) |")
    print("|---|---|---|---|---|---|---|---|" + ("---|" if thr is not None else "") + "---|")
    stats = {}
    for k in order:
        rs = per[k]
        kn = [r for r in rs if not blank(r.get("y"))]
        y = [int(r["y"]) for r in kn]
        p = [float(r["p"]) for r in kn]
        ev = sum(y) / len(y) if y else None
        mp = sum(p) / len(p) if p else None
        oe = (sum(y) / sum(p)) if p and sum(p) else None
        au = auroc(y, p)
        sl = slope(y, p)
        se = None
        if thr is not None:
            tp = sum(1 for t, v in zip(y, p) if t == 1 and v >= thr)
            fn = sum(1 for t, v in zip(y, p) if t == 1 and v < thr)
            se = tp / (tp + fn) if tp + fn else None
        stats[k] = (ev, oe, au)
        fl = []
        if "oe_range" in th and oe is not None and not (th["oe_range"][0] <= oe <= th["oe_range"][1]):
            fl.append(f"O/E outside {th['oe_range'][0]} to {th['oe_range'][1]}")
        if "auroc_min" in th and au is not None and au < th["auroc_min"]:
            fl.append(f"AUROC below {th['auroc_min']}")
        print(f"| {k} | {len(rs)} | {len(kn)} | {fmt(ev)} | {fmt(mp)} | {fmt(oe, 2)} | {fmt(au)} | {fmt(sl, 2)} |"
              + (f" {fmt(se)} |" if thr is not None else "") + f" {'; '.join(fl) or 'none'} |")
    if inputs:
        print("\nInputs against the reference period (standardized mean difference; missing share)")
        print("| Input | Period | Mean | SD | Missing share | SMD vs reference | Flags (your thresholds) |")
        print("|---|---|---|---|---|---|---|")
        for inp in inputs:
            ref = [float(r[inp]) for r in per[a.reference] if not blank(r.get(inp))]
            rm, rsd = mean_sd(ref)
            for k in order:
                vals = [float(r[inp]) for r in per[k] if not blank(r.get(inp))]
                m, sd = mean_sd(vals)
                miss = 1 - len(vals) / len(per[k]) if per[k] else None
                smd = None
                if m is not None and rm is not None and sd and rsd:
                    smd = (m - rm) / math.sqrt((sd ** 2 + rsd ** 2) / 2)
                fl = []
                if "smd_max" in th and smd is not None and abs(smd) > th["smd_max"]:
                    fl.append(f"|SMD| above {th['smd_max']}")
                if "missing_max" in th and miss is not None and miss > th["missing_max"]:
                    fl.append(f"missing above {th['missing_max']}")
                print(f"| {inp} | {k} | {fmt(m, 2)} | {fmt(sd, 2)} | {fmt(miss)} | {fmt(smd, 2)} | {'; '.join(fl) or 'none'} |")
    if groups and thr is not None:
        print("\nBy group, latest period (outcomes known)")
        last = order[-1]
        print("| Group | n known | Event rate | AUROC | Sensitivity at your threshold |")
        print("|---|---|---|---|---|")
        for g in groups:
            for v in sorted({r.get(g) for r in per[last]}):
                kn = [r for r in per[last] if r.get(g) == v and not blank(r.get("y"))]
                y = [int(r["y"]) for r in kn]
                p = [float(r["p"]) for r in kn]
                tp = sum(1 for t, s in zip(y, p) if t == 1 and s >= thr)
                fn = sum(1 for t, s in zip(y, p) if t == 1 and s < thr)
                print(f"| {g}={v} | {len(kn)} | {fmt(sum(y)/len(y) if y else None)} | {fmt(auroc(y, p))} | "
                      f"{fmt(tp/(tp+fn) if tp+fn else None)} |")
    # pattern statement (facts only)
    r0, rl = stats[a.reference], stats[order[-1]]
    print("\nWhat moved between the reference and the latest period (facts, no verdict)")
    print(f"- event rate {fmt(r0[0])} to {fmt(rl[0])}; O/E {fmt(r0[1], 2)} to {fmt(rl[1], 2)}; AUROC {fmt(r0[2])} to {fmt(rl[2])}.")
    print("- Davis et al. 2017 (DOI 10.1093/jamia/ocx030, DA-92): recalibration is indicated for calibration drift "
          "with event-rate shift and stable discrimination; association or case-mix shifts need more. Whether "
          "discrimination is 'stable' here is the person's call on their own threshold.")
    unknown = sum(1 for r in per[order[-1]] if blank(r.get("y")))
    if unknown:
        print(f"- {unknown} predictions in {order[-1]} have no outcome yet; the period's performance is read on "
              "the outcomes known only (not given for the rest).")
    return 0


# ---------- adaptation ----------

def cmd_adaptation(a):
    log = read_csv(a.log)
    rules = {r["decision_point"]: r for r in read_csv(a.rules)}
    print(f"Decision log: {a.log} ({len(log)} decisions); rule table: {a.rules}.")
    by = defaultdict(list)
    for r in log:
        by[r["decision_point"]].append(r)
    for dp, rs in by.items():
        spec = rules.get(dp)
        print(f"\n{dp}")
        if not spec:
            print("- no rule in the table for this decision point [GAP]")
            continue
        allowed = {x.strip() for x in (spec.get("options_allowed") or "").split(";") if x.strip()}
        onmiss = (spec.get("option_on_missing") or "").strip()
        outside = [r for r in rs if r["option_delivered"] not in allowed]
        dates = sorted({r["date"] for r in outside})
        print(f"- decisions: {len(rs)}; outside the allowed options ({'; '.join(sorted(allowed))}): {len(outside)}"
              + (f" on {', '.join(dates)} (options: {', '.join(sorted({r['option_delivered'] for r in outside}))})" if outside else ""))
        miss = [r for r in rs if (r.get("tailoring_missing") or "").lower() == "yes"]
        wrong = [r for r in miss if onmiss and r["option_delivered"] != onmiss]
        print(f"- tailoring data missing: {len(miss)} ({fmt(len(miss)/len(rs))}); delivered other than the missing-data rule "
              f"('{onmiss or 'not given'}'): {len(wrong)}")
        print("| Option delivered | Decisions | Proximal outcome rate | Engaged rate (prompts only) |")
        print("|---|---|---|---|")
        opts = defaultdict(list)
        for r in rs:
            opts[r["option_delivered"]].append(r)
        for o, orows in sorted(opts.items()):
            po = [int(r["proximal_outcome"]) for r in orows if not blank(r.get("proximal_outcome"))]
            en = [int(r["engaged"]) for r in orows if not blank(r.get("engaged"))]
            print(f"| {o} | {len(orows)} | {fmt(sum(po)/len(po) if po else None)} | {fmt(sum(en)/len(en) if en else None)} |")
        weeks = defaultdict(list)
        for r in rs:
            if not blank(r.get("engaged")):
                d = pd(r["date"])
                weeks[d.isocalendar()[1]].append(int(r["engaged"]))
        if weeks:
            print("- engaged rate by ISO week: " + "; ".join(f"week {k} {fmt(sum(v)/len(v))} (n={len(v)})" for k, v in sorted(weeks.items())))
        print("- option comparisons above are descriptive: options were chosen by the rule, not randomized, so a "
              "difference is not a causal effect; a micro-randomized trial estimates causal effects on proximal "
              "outcomes (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM90).")
    return 0


# ---------- words ----------

def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows", "source and rows (doi for [paper])")
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            low = [c.lower() for c in cells]
            if any(c in names for c in low):
                drop = {i for i, c in enumerate(low) if c in names}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop))
        else:
            if not line.strip():
                drop = set()
            out.append(line)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9.,'%()/-]*", "\n".join(out)))


def cmd_words(a):
    n = count_words(a.answer)
    print(f"{n} words")
    if n <= CAP:
        print("within the short-mode cap")
        return 0
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, "
          "rows not tied to the question; never a gap, a stop or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("records")
    r.add_argument("--register", required=True)
    r.add_argument("--as-of", required=True)
    r.add_argument("--rule")
    d = sub.add_parser("drift")
    d.add_argument("--log", required=True)
    d.add_argument("--reference", required=True)
    d.add_argument("--thresholds")
    d.add_argument("--inputs")
    d.add_argument("--groups")
    x = sub.add_parser("adaptation")
    x.add_argument("--log", required=True)
    x.add_argument("--rules", required=True)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"records": cmd_records, "drift": cmd_drift, "adaptation": cmd_adaptation, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
