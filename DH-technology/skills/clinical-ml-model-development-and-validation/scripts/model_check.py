#!/usr/bin/env python3
"""Checks and computations on the person's own model files (clinical-ml-model-development-and-validation).

Commands
  split     python3 model_check.py split --manifest MANIFEST.csv [--claim external|temporal|internal] [--groups sex,age_band]
  rules     python3 model_check.py rules --rules RULES.csv
  evaluate  python3 model_check.py evaluate --predictions PRED.csv [--criteria CRITERIA.json] [--groups sex,age_band]
  words     python3 model_check.py words ANSWER.md

Nothing here sets a threshold, an acceptance criterion or a fairness tolerance. Every
threshold comes from the person's criteria file; without one, values are reported and
nothing is marked met or not met. Row ids in the output refer to the research files in
references/ (DA, TM, CV rows).
"""
import argparse
import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import date

CAP = 450


# ---------- helpers ----------

def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        return None


def fmt(x, nd=3):
    if x is None:
        return "not computable"
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return "not computable"
    return f"{x:.{nd}f}"


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def auroc(y, p):
    pos = [pi for yi, pi in zip(y, p) if yi == 1]
    neg = [pi for yi, pi in zip(y, p) if yi == 0]
    n1, n0 = len(pos), len(neg)
    if n1 == 0 or n0 == 0:
        return None, None, n1, n0
    # rank-based (Mann-Whitney), ties get average ranks
    allv = sorted([(v, 1) for v in pos] + [(v, 0) for v in neg])
    ranks = [0.0] * len(allv)
    i = 0
    while i < len(allv):
        j = i
        while j + 1 < len(allv) and allv[j + 1][0] == allv[i][0]:
            j += 1
        r = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[k] = r
        i = j + 1
    rsum = sum(r for r, (_, lab) in zip(ranks, allv) if lab == 1)
    a = (rsum - n1 * (n1 + 1) / 2) / (n1 * n0)
    q1 = a / (2 - a)
    q2 = 2 * a * a / (1 + a)
    se = math.sqrt(max(0.0, (a * (1 - a) + (n1 - 1) * (q1 - a * a) + (n0 - 1) * (q2 - a * a)) / (n1 * n0)))
    return a, se, n1, n0


def logit(v):
    v = min(max(v, 1e-6), 1 - 1e-6)
    return math.log(v / (1 - v))


def sigmoid(x):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    e = math.exp(x)
    return e / (1 + e)


def calibration(y, p):
    """Calibration intercept (offset logit p, intercept only) and slope (y ~ a + b*logit p)."""
    if len(set(y)) < 2:
        return None, None
    lp = [logit(v) for v in p]
    # intercept with offset
    a = 0.0
    for _ in range(50):
        mu = [sigmoid(a + x) for x in lp]
        g = sum(yi - m for yi, m in zip(y, mu))
        h = sum(m * (1 - m) for m in mu)
        if h == 0:
            break
        step = g / h
        a += step
        if abs(step) < 1e-10:
            break
    citl = a
    # slope
    b0, b1 = 0.0, 1.0
    for _ in range(100):
        mu = [sigmoid(b0 + b1 * x) for x in lp]
        g0 = sum(yi - m for yi, m in zip(y, mu))
        g1 = sum((yi - m) * x for yi, m, x in zip(y, mu, lp))
        w = [m * (1 - m) for m in mu]
        h00 = sum(w)
        h01 = sum(wi * x for wi, x in zip(w, lp))
        h11 = sum(wi * x * x for wi, x in zip(w, lp))
        det = h00 * h11 - h01 * h01
        if abs(det) < 1e-12:
            return citl, None
        d0 = (h11 * g0 - h01 * g1) / det
        d1 = (-h01 * g0 + h00 * g1) / det
        b0 += d0
        b1 += d1
        if abs(d0) < 1e-10 and abs(d1) < 1e-10:
            break
    return citl, b1


def metrics(y, p, thr):
    n = len(y)
    ev = sum(y)
    out = {"n": n, "events": ev, "event_rate": ev / n if n else None,
           "mean_p": sum(p) / n if n else None}
    out["oe"] = (ev / sum(p)) if n and sum(p) > 0 else None
    a, se, n1, n0 = auroc(y, p)
    out["auroc"] = a
    out["auroc_ci"] = (a - 1.96 * se, a + 1.96 * se) if a is not None else (None, None)
    out["brier"] = sum((pi - yi) ** 2 for yi, pi in zip(y, p)) / n if n else None
    out["citl"], out["slope"] = calibration(y, p)
    if thr is not None:
        tp = sum(1 for yi, pi in zip(y, p) if yi == 1 and pi >= thr)
        fn = sum(1 for yi, pi in zip(y, p) if yi == 1 and pi < thr)
        fp = sum(1 for yi, pi in zip(y, p) if yi == 0 and pi >= thr)
        tn = sum(1 for yi, pi in zip(y, p) if yi == 0 and pi < thr)
        out["counts"] = (tp, fp, fn, tn)
        out["sensitivity"] = tp / (tp + fn) if tp + fn else None
        out["sensitivity_ci"] = wilson(tp, tp + fn)
        out["specificity"] = tn / (tn + fp) if tn + fp else None
        out["specificity_ci"] = wilson(tn, tn + fp)
        out["ppv"] = tp / (tp + fp) if tp + fp else None
        out["npv"] = tn / (tn + fn) if tn + fn else None
        out["flagged_share"] = (tp + fp) / n if n else None
    return out


# ---------- split ----------

def cmd_split(a):
    rows = read_csv(a.manifest)
    groups = [g for g in (a.groups or "").split(",") if g]
    by_split = defaultdict(list)
    for r in rows:
        by_split[(r.get("split") or "not given").strip().lower()].append(r)
    print(f"Manifest: {a.manifest} ({len(rows)} records). Claim for the test set: {a.claim or 'not given'}.")
    print("\n| Split | Records | Patients | Sites | First date | Last date |")
    print("|---|---|---|---|---|---|")
    for s in sorted(by_split):
        rs = by_split[s]
        ds = [d for d in (parse_date(r.get("date")) for r in rs) if d]
        print(f"| {s} | {len(rs)} | {len({r.get('patient_id') for r in rs})} | "
              f"{', '.join(sorted({r.get('site','') for r in rs}))} | "
              f"{min(ds).isoformat() if ds else 'not given'} | {max(ds).isoformat() if ds else 'not given'} |")
    flags = []
    # S1 patient in more than one split
    pat = defaultdict(set)
    for r in rows:
        pat[r.get("patient_id")].add((r.get("split") or "").strip().lower())
    leak = sorted(p for p, ss in pat.items() if len(ss) > 1 and "test" in ss)
    if leak:
        flags.append(("S1", f"{len(leak)} patient(s) appear in the test split and in a development split "
                      f"(for example {', '.join(leak[:5])}); data leakage between development and test data "
                      "creates uncertainty about true performance (FDA AI-enabled device software draft, January 2025, DA-39)"))
    dev = [r for r in rows if (r.get("split") or "").strip().lower() in ("train", "tune", "tuning", "development")]
    test = by_split.get("test", [])
    if not test:
        flags.append(("S0", "no record is labeled 'test'; the locked test set is not identifiable [GAP]"))
    # S2 external claim
    if a.claim == "external" and test:
        shared = sorted({r.get("site") for r in test} & {r.get("site") for r in dev})
        if shared:
            flags.append(("S2", f"test set claimed external but shares site(s) {', '.join(shared)} with development data; "
                          "the draft says test data should generally come from sites different from those used to develop "
                          "the model (DA-41)"))
    # S3 temporal claim
    if a.claim == "temporal" and test:
        dmax = max((d for d in (parse_date(r.get("date")) for r in dev) if d), default=None)
        tmin = min((d for d in (parse_date(r.get("date")) for r in test) if d), default=None)
        if dmax and tmin and tmin <= dmax:
            flags.append(("S3", f"test set claimed temporal but its first date {tmin.isoformat()} is not after the last "
                          f"development date {dmax.isoformat()}; EMA's reflection paper asks for prospectively generated data "
                          "(future calendar time) for high-impact uses (DA-72)"))
    if a.claim in (None, "", "internal") and test:
        flags.append(("S4", "test set independence not claimed (internal testing only); CLAIM 2024 calls this 'internal "
                      "testing' (DA-86); whether external testing is needed is the person's call"))
    # S5 subgroups
    for g in groups:
        devv = Counter((r.get(g) or "not recorded") for r in dev)
        tst = Counter((r.get(g) or "not recorded") for r in test)
        print(f"\n| {g} | Development records | Test records |")
        print("|---|---|---|")
        for v in sorted(set(devv) | set(tst)):
            print(f"| {v} | {devv.get(v, 0)} | {tst.get(v, 0)} |")
        missing = sorted(v for v in devv if tst.get(v, 0) == 0)
        if missing:
            flags.append(("S5", f"{g} = {', '.join(missing)}: present in development data, absent from the test set; "
                          "write it as not validated [GAP] (old task DH-01.04.3.1.2 step 3; subgroup evaluation, DA-38, DA-43)"))
    print("\nFlags")
    if not flags:
        print("- none raised by this check")
    for code, msg in flags:
        print(f"- {code}: {msg}")
    print("\nWhether the test set is adequate is the person's call; this check reports facts about the manifest only.")
    return 0


# ---------- rules ----------

def cmd_rules(a):
    rows = read_csv(a.rules)
    print(f"Decision-rule table: {a.rules} ({len(rows)} decision points)")
    print("\n| Decision point | Tailoring variables | Options allowed | Options in rule | On missing data | Proximal outcome | Flags |")
    print("|---|---|---|---|---|---|---|")
    total = 0
    for r in rows:
        fl = []
        allowed = {x.strip() for x in (r.get("options_allowed") or "").split(";") if x.strip()}
        inrule = {x.strip() for x in (r.get("options_in_rule") or "").split(";") if x.strip()}
        miss = (r.get("option_on_missing") or "").strip()
        if not (r.get("tailoring_variables") or "").strip():
            fl.append("R0 no tailoring variable (TM80)")
        if not miss:
            fl.append("R1 no rule for missing tailoring data (TM89)")
        elif allowed and miss not in allowed:
            fl.append(f"R5 missing-data option '{miss}' is not an allowed option")
        if not (r.get("proximal_outcome") or "").strip():
            fl.append("R2 no proximal outcome (TM84)")
        if not (r.get("engagement_outcome") or "").strip():
            fl.append("R3 no engagement or fatigue outcome (TM87)")
        if not (r.get("measurement_validity") or "").strip():
            fl.append("R4 measurement validity of tailoring variables not stated (TM88)")
        extra = sorted(inrule - allowed) if allowed else []
        if extra:
            fl.append(f"R6 rule can deliver {', '.join(extra)}, outside the allowed options")
        if not allowed:
            fl.append("R7 allowed options not given")
        total += len(fl)
        print(f"| {r.get('decision_point','')} | {r.get('tailoring_variables','') or 'not given'} | "
              f"{'; '.join(sorted(allowed)) or 'not given'} | {'; '.join(sorted(inrule)) or 'not given'} | "
              f"{miss or 'not given'} | {r.get('proximal_outcome','') or 'not given'} | {'; '.join(fl) or 'none'} |")
    print(f"\n{total} flag(s). Flags are gaps in the specification against the JITAI components "
          "(Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM77 to TM89); they are not a safety verdict.")
    return 0


# ---------- evaluate ----------

def cmd_evaluate(a):
    rows = read_csv(a.predictions)
    crit = {}
    if a.criteria:
        crit = json.load(open(a.criteria, encoding="utf-8"))
    thr = crit.get("threshold")
    groups = [g for g in (a.groups or "").split(",") if g]
    proposed = bool(crit.get("proposed"))
    y = [int(r["y"]) for r in rows if (r.get("y") or "").strip() != ""]
    p = [float(r["p"]) for r in rows if (r.get("y") or "").strip() != ""]
    print(f"Predictions: {a.predictions} ({len(rows)} rows, {len(y)} with an outcome). "
          f"Operating threshold: {thr if thr is not None else 'not given'} (the person's).")
    if crit.get("metric_named_on"):
        print(f"Metrics named on: {crit['metric_named_on']}; run date: {crit.get('run_date', 'not given')}.")
        mn, rd = parse_date(crit.get("metric_named_on")), parse_date(crit.get("run_date"))
        if mn and rd and mn > rd:
            print("FLAG E1: a metric was named after the run; the old task says not to add a metric after the run "
                  "(DH-01.04.3.1.3).")
    res = {"all": metrics(y, p, thr)}
    for g in groups:
        vals = sorted({(r.get(g) or "not recorded") for r in rows})
        for v in vals:
            yy = [int(r["y"]) for r in rows if (r.get(g) or "not recorded") == v and (r.get("y") or "").strip() != ""]
            pp = [float(r["p"]) for r in rows if (r.get(g) or "not recorded") == v and (r.get("y") or "").strip() != ""]
            res[f"{g}={v}"] = metrics(yy, pp, thr)
    print("\n| Population | n | Events | Event rate | AUROC (95% CI) | O/E | Calibration intercept | Calibration slope | Brier |"
          + (" Sensitivity (95% CI) | Specificity (95% CI) | PPV | NPV |" if thr is not None else ""))
    print("|---|---|---|---|---|---|---|---|---|" + ("---|---|---|---|" if thr is not None else ""))
    for k, m in res.items():
        ci = m["auroc_ci"]
        line = (f"| {k} | {m['n']} | {m['events']} | {fmt(m['event_rate'])} | {fmt(m['auroc'])} "
                f"({fmt(ci[0])} to {fmt(ci[1])}) | {fmt(m['oe'], 2)} | {fmt(m['citl'], 2)} | {fmt(m['slope'], 2)} | {fmt(m['brier'])} |")
        if thr is not None:
            s, sc, sp, spc = m["sensitivity"], m["sensitivity_ci"], m["specificity"], m["specificity_ci"]
            line += (f" {fmt(s)} ({fmt(sc[0])} to {fmt(sc[1])}) | {fmt(sp)} ({fmt(spc[0])} to {fmt(spc[1])}) | "
                     f"{fmt(m['ppv'])} | {fmt(m['npv'])} |")
        print(line)
    print("\nMethods: AUROC by ranks with the Hanley and McNeil interval; proportions with Wilson intervals; "
          "calibration intercept with logit(p) as offset and slope from y on logit(p). These are computation methods, "
          "not rules from the research rows.")
    # acceptance criteria
    acc = crit.get("acceptance") or []
    print("\nAcceptance criteria (the person's)")
    if proposed:
        print("- criteria file is labeled proposed: not applied; nothing marked met or not met")
        acc = []
    if not acc:
        print("- not given: values reported, nothing marked met or not met")
    for c in acc:
        pop = c.get("population", "all")
        m = res.get(pop)
        val = m.get(c["metric"]) if m else None
        if val is None:
            print(f"- {c['metric']} {c['op']} {c['value']} on {pop}: not computable on this file")
            continue
        ok = {">=": val >= c["value"], "<=": val <= c["value"], ">": val > c["value"], "<": val < c["value"]}[c["op"]]
        print(f"- {c['metric']} {c['op']} {c['value']} on {pop}: observed {fmt(val)}, "
              f"{'met' if ok else 'not met'} (your criterion, written {crit.get('metric_named_on', 'date not given')})")
    # fairness
    if groups and thr is not None:
        for g in groups:
            keys = [k for k in res if k.startswith(g + "=")]
            rates = {k: res[k]["event_rate"] for k in keys if res[k]["event_rate"] is not None}
            if len(set(round(v, 3) for v in rates.values())) > 1:
                print(f"\nFairness note for {g}: outcome rates differ across groups "
                      f"({', '.join(f'{k} {fmt(v)}' for k, v in rates.items())}). For any single threshold, a "
                      "well-calibrated model will never have the same sensitivity and specificity for two groups with "
                      "different outcome rates (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119). Which "
                      f"criterion fits the decision is the person's: {crit.get('fairness_criterion', 'not given')}.")
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
    s = sub.add_parser("split")
    s.add_argument("--manifest", required=True)
    s.add_argument("--claim", choices=["external", "temporal", "internal"])
    s.add_argument("--groups")
    r = sub.add_parser("rules")
    r.add_argument("--rules", required=True)
    e = sub.add_parser("evaluate")
    e.add_argument("--predictions", required=True)
    e.add_argument("--criteria")
    e.add_argument("--groups")
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"split": cmd_split, "rules": cmd_rules, "evaluate": cmd_evaluate, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
