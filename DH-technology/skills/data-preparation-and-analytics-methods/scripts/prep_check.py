#!/usr/bin/env python3
"""Helper for data-preparation-and-analytics-methods (dh-technology).

Seven subcommands. None of them sets a threshold, a prior, a pass rule, a
metric or a decision: every number comes from the person's own files and
arguments. Flags are facts about the files, never verdicts. Standard library
only.

  cohort    Attrition table from the person's cohort steps (CSV: step, rule,
            n_remaining). Prints excluded counts and shares of the start count.
              python3 prep_check.py cohort --steps STEPS.csv
  features  Check a feature dictionary (CSV: feature, source_field,
            window_start_days, window_end_days, missing_code,
            available_at_decision, protected_input, outcome_derived). Window
            days are relative to the index time (negative = before). Flags F1
            to F7.
              python3 prep_check.py features --dict FEATURES.csv
  split     Check a data split (CSV: patient_id, site, subset). Counts per
            subset, patients in more than one subset, sites shared between
            development subsets and test subsets. Flags S1 to S3.
              python3 prep_check.py split --file SPLIT.csv [--test-names test,external_test]
  bayes     Beta-binomial posterior for a rate under the person's prior and any
            alternative priors they name; probability that the rate lies above
            (or below) the person's threshold; whether the person's decision
            rule gives the same answer under every prior.
              python3 prep_check.py bayes --successes 42 --n 120 --prior 1 1 \
                  --alt-prior 5 15 --threshold 0.3 [--decision-prob 0.9] [--direction above]
                  [--interval 0.95]   (equal-tailed interval level; state the level used)
  holdout   Performance on the person's held-out rows only (CSV: y_true 0/1,
            score, subset, optional group). AUROC, observed vs mean predicted
            rate, and, at the person's threshold only, sensitivity,
            specificity, PPV and NPV, per group. Flags H1 to H4.
              python3 prep_check.py holdout --file PRED.csv [--threshold 0.3] [--group-col group]
  forecast  Forecast against a naive baseline on the person's holdout periods
            (CSV: period, actual, forecast, lower, upper, split history or
            holdout). MAE of the forecast, MAE of the last-value (or seasonal)
            naive baseline, interval coverage. Flags FC1 to FC3.
              python3 prep_check.py forecast --file FC.csv [--season 0]
  words     Count a short answer against the 450-word cap. Leaves out the
            "Calls made" block (up to the record block, which is counted) and
            the Source and Rows columns.
              python3 prep_check.py words ANSWER.md
"""
import argparse
import csv
import math
import re
import sys

CAP = 450
PROTECTED = ("race", "color", "national origin", "ethnicity", "sex", "gender", "age", "disability")


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def blank(v):
    return v is None or str(v).strip() == "" or str(v).strip().lower() in ("not given", "na", "n/a")


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def pct(x):
    return "not computed" if x is None else f"{100 * x:.1f}%"


# ---------------------------------------------------------------- cohort
def cmd_cohort(a):
    rows = read_csv(a.steps)
    if not rows:
        print("No steps in the file.")
        return 1
    start = num(rows[0].get("n_remaining"))
    print("| Step | Rule (your words) | Remaining | Excluded at this step | Share of start excluded | Flags |")
    print("|---|---|---|---|---|---|")
    prev = None
    for r in rows:
        n = num(r.get("n_remaining"))
        fl = []
        if blank(r.get("rule")):
            fl.append("C2 rule not given")
        if n is None:
            fl.append("C3 count not given")
        exc = None
        if prev is not None and n is not None:
            exc = prev - n
            if exc < 0:
                fl.append("C1 count rises after an exclusion")
        share = (exc / start) if (exc is not None and start) else None
        print(f"| {r.get('step', '')} | {r.get('rule', '') or 'not given'} | "
              f"{'not given' if n is None else int(n)} | {'' if exc is None else int(exc)} | "
              f"{'' if share is None else pct(share)} | {', '.join(fl) or 'none'} |")
        if n is not None:
            prev = n
    if start and prev is not None:
        print(f"\nStart {int(start)}; final {int(prev)}; {pct((start - prev) / start)} of the start excluded in all.")
    print("Whether the cohort fits the intended use is the person's call.")
    return 0


# ---------------------------------------------------------------- features
def cmd_features(a):
    rows = read_csv(a.dict)
    print("| Feature | Source field | Window (days from index) | Missing code | Flags |")
    print("|---|---|---|---|---|")
    leak, prot = [], []
    for r in rows:
        fl = []
        if blank(r.get("source_field")):
            fl.append("F1 source field not given")
        ws, we = num(r.get("window_start_days")), num(r.get("window_end_days"))
        if ws is None or we is None:
            fl.append("F2 window not given")
        elif we > 0:
            fl.append("F3 window ends after the index time")
            leak.append(r["feature"])
        if blank(r.get("missing_code")):
            fl.append("F4 missing-value code not given")
        avail = (r.get("available_at_decision") or "").strip().lower()
        if avail != "yes":
            fl.append("F5 availability at decision time " + ("no" if avail == "no" else "not given"))
            if avail == "no" and r["feature"] not in leak:
                leak.append(r["feature"])
        if (r.get("protected_input") or "").strip().lower() == "yes" or \
                any(re.search(rf"\b{p}\b", (r.get("feature", "") + " " + r.get("source_field", "")).lower()) for p in PROTECTED):
            fl.append("F6 input measures a characteristic named in 45 CFR 92.210")
            prot.append(r["feature"])
        if (r.get("outcome_derived") or "").strip().lower() == "yes":
            fl.append("F7 derived from the outcome")
            if r["feature"] not in leak:
                leak.append(r["feature"])
        win = "not given" if (ws is None or we is None) else f"{ws:g} to {we:g}"
        print(f"| {r.get('feature', '')} | {r.get('source_field', '') or 'not given'} | {win} | "
              f"{r.get('missing_code', '') or 'not given'} | {', '.join(fl) or 'none'} |")
    print(f"\nCandidates to refuse (F3, F5 'no' or F7; the person decides): {', '.join(leak) or 'none'}.")
    print(f"Inputs a covered entity must identify and mitigate under 45 CFR 92.210 (F6): {', '.join(prot) or 'none'}.")
    return 0


# ---------------------------------------------------------------- split
def cmd_split(a):
    rows = read_csv(a.file)
    tests = {t.strip().lower() for t in a.test_names.split(",")}
    subsets, pat, site = {}, {}, {}
    for r in rows:
        s = (r.get("subset") or "").strip().lower() or "not given"
        subsets.setdefault(s, set()).add(r.get("patient_id"))
        pat.setdefault(r.get("patient_id"), set()).add(s)
        site.setdefault(s, set()).add((r.get("site") or "").strip() or "not given")
    print("| Subset | Rows | Patients | Sites |")
    print("|---|---|---|---|")
    for s in sorted(subsets):
        n_rows = sum(1 for r in rows if ((r.get("subset") or "").strip().lower() or "not given") == s)
        print(f"| {s} | {n_rows} | {len(subsets[s])} | {', '.join(sorted(site[s]))} |")
    multi = sorted(p for p, ss in pat.items() if len(ss) > 1)
    dev_sites = set().union(*[site[s] for s in site if s not in tests]) if any(s not in tests for s in site) else set()
    test_sites = set().union(*[site[s] for s in site if s in tests]) if any(s in tests for s in site) else set()
    shared = sorted(dev_sites & test_sites)
    print()
    print(f"S1 patients in more than one subset: {len(multi)}" + (f" ({', '.join(multi[:10])}{' ...' if len(multi) > 10 else ''})" if multi else ""))
    print(f"S2 sites in both development and test subsets: {', '.join(shared) or 'none'}")
    if "not given" in subsets:
        print("S3 rows without a subset label: " + str(sum(1 for r in rows if not (r.get('subset') or '').strip())))
    if not test_sites:
        print(f"No subset named {', '.join(sorted(tests))}; name the test subset with --test-names.")
    print("Whether the split is acceptable for the intended use is the person's call.")
    return 0


# ---------------------------------------------------------------- bayes
def betacf(a, b, x):
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
        c = 1.0 + aa / c if abs(c) > 1e-300 else 1e300
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
        c = 1.0 + aa / c if abs(c) > 1e-300 else 1e300
        de = d * c
        h *= de
        if abs(de - 1.0) < 3e-14:
            break
    return h


def ibeta(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lbt) * betacf(a, b, x) / a
    return 1.0 - math.exp(lbt) * betacf(b, a, 1 - x) / b


def beta_ppf(a, b, q):
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if ibeta(a, b, mid) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cmd_bayes(a):
    k, n = a.successes, a.n
    if k < 0 or n <= 0 or k > n:
        print("Successes must lie between 0 and n.")
        return 1
    priors = [("your prior", a.prior)] + [(f"alternative {i + 1}", p) for i, p in enumerate(a.alt_prior or [])]
    print(f"Data: {k} of {n} ({k / n:.3f}). Priors are the person's; this run computes, it does not choose.")
    lv = a.interval
    print("| Prior | Beta(a, b) | Posterior mean | " + f"{100 * lv:g}% interval" + " | " +
          (f"Pr(rate {'>' if a.direction == 'above' else '<'} {a.threshold:g})" if a.threshold is not None else "Threshold") +
          (f" | Meets your rule Pr > {a.decision_prob:g}" if a.decision_prob is not None and a.threshold is not None else "") + " |")
    print("|---|---|---|---|---|" + ("---|" if a.decision_prob is not None and a.threshold is not None else ""))
    meets = []
    for name, (pa, pb) in priors:
        A, B = pa + k, pb + n - k
        mean = A / (A + B)
        lo, hi = beta_ppf(A, B, (1 - lv) / 2), beta_ppf(A, B, 1 - (1 - lv) / 2)
        if a.threshold is not None:
            p_above = 1 - ibeta(A, B, a.threshold)
            p = p_above if a.direction == "above" else 1 - p_above
            cell = f"{p:.3f}"
        else:
            p, cell = None, "threshold not given"
        extra = ""
        if a.decision_prob is not None and p is not None:
            m = p > a.decision_prob
            meets.append(m)
            extra = f" | {'yes' if m else 'no'}"
        print(f"| {name} | Beta({pa:g}, {pb:g}) | {mean:.3f} | {lo:.3f} to {hi:.3f} | {cell}{extra} |")
    if meets:
        print("\nYour rule gives the same answer under every prior listed." if len(set(meets)) == 1
              else "\nYour rule gives different answers under the priors listed: keep both results and say which prior reverses it.")
    if a.threshold is None:
        print("\nThreshold not given: no probability against a threshold is computed.")
    return 0


# ---------------------------------------------------------------- holdout
def auroc(pairs):
    pos = [s for y, s in pairs if y == 1]
    neg = [s for y, s in pairs if y == 0]
    if not pos or not neg:
        return None
    wins = 0.0
    for p in pos:
        for q in neg:
            wins += 1.0 if p > q else (0.5 if p == q else 0.0)
    return wins / (len(pos) * len(neg))


def cmd_holdout(a):
    rows = read_csv(a.file)
    held = {"test", "holdout", "external_test", "internal_test"}
    used = [r for r in rows if (r.get("subset") or "").strip().lower() in held]
    other = len(rows) - len(used)
    if other:
        print(f"H1 {other} rows are not in a held-out subset ({', '.join(sorted(held))}) and are left out of every figure below.")
    if not used:
        print("No held-out rows: nothing to report.")
        return 1
    groups = {"all": used}
    if a.group_col:
        for r in used:
            groups.setdefault(f"{a.group_col}={(r.get(a.group_col) or 'not given').strip()}", []).append(r)
    head = "| Group | n | Events | Observed rate | Mean predicted | AUROC |"
    sep = "|---|---|---|---|---|---|"
    if a.threshold is not None:
        head += " Sensitivity | Specificity | PPV | NPV |"
        sep += "---|---|---|---|"
    print(head)
    print(sep)
    rates = {}
    for g, rs in groups.items():
        pairs = [(int(float(r["y_true"])), float(r["score"])) for r in rs if num(r.get("score")) is not None and num(r.get("y_true")) is not None]
        n = len(pairs)
        ev = sum(y for y, _ in pairs)
        obs = ev / n if n else None
        mp = sum(s for _, s in pairs) / n if n else None
        au = auroc(pairs)
        rates[g] = obs
        line = f"| {g} | {n} | {ev} | {'' if obs is None else f'{obs:.3f}'} | {'' if mp is None else f'{mp:.3f}'} | {'not computable (one class only)' if au is None else f'{au:.3f}'} |"
        if a.threshold is not None:
            tp = sum(1 for y, s in pairs if y == 1 and s >= a.threshold)
            fn = sum(1 for y, s in pairs if y == 1 and s < a.threshold)
            tn = sum(1 for y, s in pairs if y == 0 and s < a.threshold)
            fp = sum(1 for y, s in pairs if y == 0 and s >= a.threshold)
            f = lambda x, y: "n/a" if (x + y) == 0 else f"{x / (x + y):.3f}"
            line += f" {f(tp, fn)} | {f(tn, fp)} | {f(tp, fp)} | {f(tn, fn)} |"
        print(line)
        if n and (ev == 0 or n - ev == 0):
            print(f"H3 {g}: only one outcome class in the held-out rows; AUROC and the error rates for the missing class cannot be computed.")
    if a.threshold is None:
        print("\nH2 threshold not given: sensitivity, specificity, PPV and NPV are not computed. The threshold is the person's.")
    sub = [v for k, v in rates.items() if k != "all" and v is not None]
    if len(sub) > 1 and max(sub) != min(sub):
        print("H4 outcome rates differ between groups: a calibrated model cannot have equal sensitivity and specificity "
              "at one threshold for both (Paulus and Kent 2020, DA-119, DOI 10.1038/s41746-020-0304-9). "
              "Which criterion fits the decision is the person's.")
    print("Whether this performance is acceptable is the person's call.")
    return 0


# ---------------------------------------------------------------- forecast
def cmd_forecast(a):
    rows = read_csv(a.file)
    hist = [r for r in rows if (r.get("split") or "").strip().lower() == "history"]
    hold = [r for r in rows if (r.get("split") or "").strip().lower() == "holdout"]
    if not hold:
        print("FC1 no holdout periods: accuracy on the fitted history is not reported.")
        return 1
    series = [num(r.get("actual")) for r in rows]
    idx0 = rows.index(hold[0])
    errs_f, errs_n, cov, cov_n = [], [], 0, 0
    print("| Period | Actual | Forecast | Naive baseline | Interval | Inside |")
    print("|---|---|---|---|---|---|")
    for i, r in enumerate(rows):
        if r not in hold:
            continue
        act, fc = num(r.get("actual")), num(r.get("forecast"))
        lag = a.season if a.season and a.season > 0 else 1
        base_i = idx0 - lag + ((i - idx0) % lag if a.season else 0)
        base = series[base_i] if 0 <= base_i < len(series) else None
        lo, hi = num(r.get("lower")), num(r.get("upper"))
        inside = ""
        if lo is not None and hi is not None and act is not None:
            cov_n += 1
            ok = lo <= act <= hi
            cov += ok
            inside = "yes" if ok else "no"
        if act is not None and fc is not None:
            errs_f.append(abs(act - fc))
        if act is not None and base is not None:
            errs_n.append(abs(act - base))
        print(f"| {r.get('period')} | {act} | {fc} | {base} | {'not given' if lo is None or hi is None else f'{lo:g} to {hi:g}'} | {inside} |")
    mae = lambda e: sum(e) / len(e) if e else None
    mf, mn = mae(errs_f), mae(errs_n)
    print(f"\nHoldout periods {len(hold)}; history periods {len(hist)}.")
    print(f"MAE forecast {'' if mf is None else f'{mf:.2f}'}; MAE naive baseline ({'seasonal, lag ' + str(a.season) if a.season else 'last history value'}) {'' if mn is None else f'{mn:.2f}'}.")
    if cov_n:
        print(f"Interval coverage on holdout: {cov} of {cov_n} ({pct(cov / cov_n)}); the nominal level is the person's to state.")
    else:
        print("FC2 interval not given on the holdout periods.")
    if mf is not None and mn is not None and mf >= mn:
        print("FC3 the forecast does not beat the naive baseline on this holdout (a fact, not a verdict).")
    print("Whether the forecast is fit for the decision is the person's call.")
    return 0


# ---------------------------------------------------------------- words
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
    c = sub.add_parser("cohort")
    c.add_argument("--steps", required=True)
    f = sub.add_parser("features")
    f.add_argument("--dict", required=True)
    s = sub.add_parser("split")
    s.add_argument("--file", required=True)
    s.add_argument("--test-names", default="test,external_test")
    b = sub.add_parser("bayes")
    b.add_argument("--successes", type=int, required=True)
    b.add_argument("--n", type=int, required=True)
    b.add_argument("--prior", type=float, nargs=2, required=True, metavar=("A", "B"))
    b.add_argument("--alt-prior", type=float, nargs=2, action="append", metavar=("A", "B"))
    b.add_argument("--threshold", type=float)
    b.add_argument("--decision-prob", type=float)
    b.add_argument("--direction", choices=["above", "below"], default="above")
    b.add_argument("--interval", type=float, default=0.95, help="interval level the person names; printed as given")
    h = sub.add_parser("holdout")
    h.add_argument("--file", required=True)
    h.add_argument("--threshold", type=float)
    h.add_argument("--group-col")
    fc = sub.add_parser("forecast")
    fc.add_argument("--file", required=True)
    fc.add_argument("--season", type=int, default=0)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"cohort": cmd_cohort, "features": cmd_features, "split": cmd_split, "bayes": cmd_bayes,
            "holdout": cmd_holdout, "forecast": cmd_forecast, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
