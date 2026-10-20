#!/usr/bin/env python3
"""Subgroup performance check for a binary clinical model, run on the person's own scored data.

Commands
  groups   per-group counts, outcome rate, sensitivity, specificity, PPV, NPV, FNR, FPR,
           selection rate and calibration-in-the-large (mean score vs observed rate),
           each rate with a 95% Wilson interval; differences against the reference group the
           person names; the impossibility flag when outcome rates differ (DA-119).
  rule     applies the person's own rule (for example "sensitivity:0.05" = a group may sit at
           most 0.05 below the reference) and prints, for every group that does not meet it,
           the computed number of extra numerator events that would bring it within the rule.
  words    counts a short answer against the 450-word cap (calls list and Source/Rows columns
           left out).

Nothing here sets a threshold. The decision threshold, the reference group, the metric and the
allowed difference are the person's; without them the script reports values and says
"not given". Groups the person marks as not visible in the data are printed as [GAP] and never
reported as tested.

Input CSV: one row per case with a group column, a 0/1 outcome column and a score column
(probability 0 to 1) or a 0/1 prediction column.
"""
import argparse
import csv
import math
import re
import sys

CAP = 450
METRICS = {
    # name: (numerator key, denominator key, direction note)
    "sensitivity": ("tp", "pos"),
    "specificity": ("tn", "neg"),
    "ppv": ("tp", "pred_pos"),
    "npv": ("tn", "pred_neg"),
    "fnr": ("fn", "pos"),
    "fpr": ("fp", "neg"),
    "selection_rate": ("pred_pos", "n"),
}
HIGHER_IS_BETTER = {"sensitivity", "specificity", "ppv", "npv"}


def wilson(k, n, z=1.96):
    if n == 0:
        return None
    p = k / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, centre - half), min(1.0, centre + half)


def fmt(x, nd=3):
    return "n/a" if x is None else f"{x:.{nd}f}"


def load(a):
    rows = list(csv.DictReader(open(a.data, newline="", encoding="utf-8")))
    if not rows:
        sys.exit("empty file")
    for col in (a.group_col, a.label_col):
        if col not in rows[0]:
            sys.exit(f"column '{col}' not in file; columns are {list(rows[0])}")
    if a.pred_col is None and a.score_col is None:
        sys.exit("give --score-col with --threshold, or --pred-col")
    if a.score_col and a.threshold is None and a.pred_col is None:
        print("Decision threshold: not given. Scores are summarized for calibration only; "
              "error rates need the threshold you use in practice (yours to set).")
    return rows


def tally(rows, a):
    groups, missing_group, skipped = {}, 0, 0
    for r in rows:
        g = (r.get(a.group_col) or "").strip()
        try:
            y = int(float(r[a.label_col]))
        except (ValueError, TypeError):
            skipped += 1
            continue
        score = None
        if a.score_col:
            try:
                score = float(r[a.score_col])
            except (ValueError, TypeError):
                score = None
        if a.pred_col:
            try:
                p = int(float(r[a.pred_col]))
            except (ValueError, TypeError):
                skipped += 1
                continue
        elif a.threshold is not None and score is not None:
            p = 1 if score >= a.threshold else 0
        else:
            p = None
        if not g:
            missing_group += 1
            g = "(group not recorded)"
        d = groups.setdefault(g, dict(n=0, pos=0, neg=0, tp=0, tn=0, fp=0, fn=0,
                                      pred_pos=0, pred_neg=0, score_sum=0.0, score_n=0))
        d["n"] += 1
        d["pos" if y == 1 else "neg"] += 1
        if score is not None:
            d["score_sum"] += score
            d["score_n"] += 1
        if p is not None:
            d["pred_pos" if p == 1 else "pred_neg"] += 1
            if y == 1 and p == 1:
                d["tp"] += 1
            elif y == 1:
                d["fn"] += 1
            elif p == 1:
                d["fp"] += 1
            else:
                d["tn"] += 1
    return groups, missing_group, skipped


def rate(d, m):
    num, den = METRICS[m]
    return (d[num] / d[den]) if d[den] else None, d[num], d[den]


def header(a):
    print(f"Dataset: {a.dataset_version or 'not given'} | Model: {a.model_version or 'not given'} | "
          f"Threshold: {a.threshold if a.threshold is not None else ('prediction column ' + a.pred_col if a.pred_col else 'not given')} | "
          f"Reference group: {a.reference or 'not given'}")


def cmd_groups(a):
    rows = load(a)
    groups, missing_group, skipped = tally(rows, a)
    gap = [g.strip() for g in (a.gap_groups or "").split(",") if g.strip()]
    header(a)
    print(f"Rows read: {len(rows)}; skipped (outcome or prediction unreadable): {skipped}; "
          f"group not recorded: {missing_group}")
    have_pred = any(d["pred_pos"] + d["pred_neg"] for d in groups.values())
    print()
    print("| Group | n | Outcome rate | Mean score | O/E | Sensitivity (95% CI) | Specificity (95% CI) | PPV | NPV | FNR | FPR | Selection rate |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for g in sorted(groups):
        d = groups[g]
        orate = d["pos"] / d["n"] if d["n"] else None
        ms = d["score_sum"] / d["score_n"] if d["score_n"] else None
        oe = (orate / ms) if (ms and orate is not None) else None
        cells = [g, str(d["n"]), fmt(orate), fmt(ms), fmt(oe, 2)]
        if have_pred:
            for m in ("sensitivity", "specificity"):
                v, k, n = rate(d, m)
                ci = wilson(k, n)
                cells.append(f"{fmt(v)} ({k}/{n}; {fmt(ci[0]) if ci else 'n/a'} to {fmt(ci[1]) if ci else 'n/a'})")
            for m in ("ppv", "npv", "fnr", "fpr", "selection_rate"):
                v, k, n = rate(d, m)
                cells.append(f"{fmt(v)} ({k}/{n})")
        else:
            cells += ["needs threshold"] * 7
        print("| " + " | ".join(cells) + " |")
    for g in gap:
        print(f"| {g} | [GAP]: not visible in this data; not tested | | | | | | | | | | |")
    print()
    # differences against the person's reference
    if a.reference and a.reference in groups and have_pred:
        ref = groups[a.reference]
        print(f"Differences against your reference group '{a.reference}' (group minus reference; ratio group/reference):")
        print("| Group | Metric | Group value | Reference value | Difference | Ratio |")
        print("|---|---|---|---|---|---|")
        for g in sorted(groups):
            if g == a.reference or g == "(group not recorded)":
                continue
            for m in ("sensitivity", "specificity", "ppv", "fpr", "fnr", "selection_rate"):
                v, _, _ = rate(groups[g], m)
                r0, _, _ = rate(ref, m)
                if v is None or r0 is None:
                    print(f"| {g} | {m} | {fmt(v)} | {fmt(r0)} | n/a | n/a |")
                    continue
                ratio = fmt(v / r0, 2) if r0 else "n/a"
                print(f"| {g} | {m} | {fmt(v)} | {fmt(r0)} | {v - r0:+.3f} | {ratio} |")
        print()
    elif a.reference and a.reference not in groups:
        print(f"Reference group '{a.reference}' not found in the data; differences not computed.")
    elif not a.reference:
        print("Reference group: not given. Differences are not computed; name the group you compare against.")
    # impossibility flag
    rates = {g: d["pos"] / d["n"] for g, d in groups.items() if d["n"] and g != "(group not recorded)"}
    if len(set(round(v, 6) for v in rates.values())) > 1:
        lo = min(rates, key=rates.get)
        hi = max(rates, key=rates.get)
        print(f"Outcome rates differ between groups ({lo} {rates[lo]:.3f}, {hi} {rates[hi]:.3f}). "
              "For any single threshold, a well-calibrated model will not have the same sensitivity and "
              "specificity for groups with different outcome rates (Paulus and Kent 2020, DA-119, "
              "DOI 10.1038/s41746-020-0304-9). Which criterion fits the decision is yours (DA-116).")
    print("No pass or fail is printed: the criterion, the allowed difference and the decision are yours.")
    return 0


def parse_rule(s):
    m = re.fullmatch(r"\s*([a-z_]+)\s*:\s*([0-9.]+)\s*", s or "")
    if not m or m.group(1) not in METRICS:
        sys.exit("rule must look like METRIC:MAX_DIFFERENCE, metric one of " + ", ".join(METRICS))
    return m.group(1), float(m.group(2))


def cmd_rule(a):
    rows = load(a)
    if not a.reference:
        print("Reference group: not given. Your rule compares groups against a reference you name; "
              "nothing is read against the rule.")
        return 1
    metric, allowed = parse_rule(a.rule)
    groups, _, _ = tally(rows, a)
    if a.reference not in groups:
        sys.exit(f"reference group '{a.reference}' not in data")
    header(a)
    ref_v, _, _ = rate(groups[a.reference], metric)
    worse_is_lower = metric in HIGHER_IS_BETTER
    side = "below" if worse_is_lower else "above"
    print(f"Your rule (as given): {metric} in a group may sit at most {allowed} {side} the reference "
          f"'{a.reference}' ({fmt(ref_v)}). Rule written on: {a.rule_date or 'not given'}.")
    print("| Group | Value | Reference | Gap on the harmful side | Your rule | Extra events that would meet it (computed) |")
    print("|---|---|---|---|---|---|")
    for g in sorted(groups):
        if g in (a.reference, "(group not recorded)"):
            continue
        d = groups[g]
        v, k, n = rate(d, metric)
        if v is None or ref_v is None:
            print(f"| {g} | n/a | {fmt(ref_v)} | n/a | not measurable | n/a |")
            continue
        gap = (ref_v - v) if worse_is_lower else (v - ref_v)
        if gap <= allowed + 1e-12:
            print(f"| {g} | {fmt(v)} ({k}/{n}) | {fmt(ref_v)} | {gap:+.3f} | met | none needed |")
        else:
            if worse_is_lower:
                need = math.ceil((ref_v - allowed) * n - k - 1e-9)
                what = f"{need} more of {n} ({k + need}/{n} = {(k + need) / n:.3f})"
            else:
                need = math.ceil(k - (ref_v + allowed) * n - 1e-9)
                what = f"{need} fewer of {n} ({k - need}/{n} = {(k - need) / n:.3f})"
            print(f"| {g} | {fmt(v)} ({k}/{n}) | {fmt(ref_v)} | {gap:+.3f} | not met | {what} |")
    print("Counts above are arithmetic on your data with the denominator held fixed; they are not a target.")
    return 0


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
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, rows not tied "
          "to the question; never a gap, a stop or the record line")
    return 1


def add_data_args(p):
    p.add_argument("--data", required=True)
    p.add_argument("--group-col", required=True)
    p.add_argument("--label-col", required=True)
    p.add_argument("--score-col")
    p.add_argument("--pred-col")
    p.add_argument("--threshold", type=float, help="the person's decision threshold; never defaulted")
    p.add_argument("--reference", help="the reference group the person names")
    p.add_argument("--dataset-version")
    p.add_argument("--model-version")
    p.add_argument("--gap-groups", help="comma-separated groups the person says are not visible in the data")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("groups")
    add_data_args(g)
    r = sub.add_parser("rule")
    add_data_args(r)
    r.add_argument("--rule", required=True, help="METRIC:MAX_DIFFERENCE, the person's rule")
    r.add_argument("--rule-date", help="date the person wrote the rule")
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"groups": cmd_groups, "rule": cmd_rule, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
