#!/usr/bin/env python3
"""Check a ranking of what the person scored: analytics.mcda or analytics.rice.

Input: a JSON file holding either a saved connector call ({"call": {"tool": ...,
"arguments": ...}, "response": ...}, as in examples/live/) or bare arguments
({"alternatives": [...], "criteria_weights": {...}} for MCDA, {"initiatives": [...]}
for RICE).

MCDA: recomputes each value as analytics.mcda does (sum of weight x score / 4, x 100),
compares with the connector response when present, and gives, for each criterion and
each pair of adjacent options, the weight on that criterion at which the two would swap
(other weights rescaled in proportion).

RICE: recomputes reach x impact x confidence / effort with confidence read as a percent
(the connector's observed behavior), flags impact values outside 0.25, 0.5, 1, 2, 3,
flags confidence given as a fraction (0 to 1), and compares with the response.

The script never creates a score, a weight or a RICE input. Missing numbers stop it.

Usage: python3 rank_check.py FILE
"""
import json
import sys

IMPACTS = {0.25, 0.5, 1, 2, 3}


def load(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    call = data.get("call", {})
    args = call.get("arguments", data)
    tool = call.get("tool", "")
    if not tool:
        tool = "analytics.rice" if "initiatives" in args else "analytics.mcda"
    return tool, args, data.get("response")


# ---------- MCDA ----------

def mcda_problems(alts, weights):
    problems = []
    if not weights:
        problems.append("no criteria_weights: the person sets the weights")
    total = sum(weights.values())
    if weights and abs(total - 1) > 1e-6:
        problems.append(f"weights sum to {total:.4f}, not 1")
    for a in alts:
        for c in weights:
            s = a.get("scores", {}).get(c)
            if s is None:
                problems.append(f"{a['id']}: no score for {c} (ask the person; do not fill it)")
            elif not 0 <= s <= 4:
                problems.append(f"{a['id']}: score {s} for {c} is outside 0 to 4")
    return problems


def mcda_value(scores, weights):
    return sum(weights[c] * scores[c] / 4 for c in weights) * 100


def swap_weight(si, sj, weights, c):
    """Weight on criterion c at which options i and j are equal, or None."""
    wc = weights[c]
    if wc >= 1:
        return None
    a = (si[c] - sj[c]) / 4
    rest_i = sum(weights[k] * si[k] / 4 for k in weights if k != c)
    rest_j = sum(weights[k] * sj[k] / 4 for k in weights if k != c)
    b = (rest_i - rest_j) / (1 - wc)
    if abs(b - a) < 1e-12:
        return None
    t = b / (b - a)
    return t if 0 < t < 1 - 1e-9 else None


def run_mcda(args, response):
    alts = args["alternatives"]
    weights = args.get("criteria_weights", {})
    problems = mcda_problems(alts, weights)
    if problems:
        print("Cannot rank:")
        for p in problems:
            print(" -", p)
        return 2
    ranked = sorted(alts, key=lambda a: mcda_value(a["scores"], weights), reverse=True)
    got = {}
    if response:
        got = {r["id"]: r.get("value_estimate") for r in response.get("results", [])}
    print("| Rank | Option | Value (0 to 100) | Connector value | Match |")
    print("|---|---|---|---|---|")
    for i, a in enumerate(ranked, 1):
        v = mcda_value(a["scores"], weights)
        g = got.get(a["id"])
        match = "" if g is None else ("yes" if abs(g - v) < 0.01 else "NO")
        print(f"| {i} | {a['id']} | {v:.2f} | {'' if g is None else g} | {match} |")
        if i > 1:
            prev = ranked[i - 2]
            if abs(mcda_value(prev["scores"], weights) - v) < 1e-9:
                print(f"|  | tie with {prev['id']} |  |  |  |")
    print()
    print("Swap points (weight on one criterion at which adjacent options trade places; other weights rescaled in proportion):")
    print("| Pair | Criterion | Current weight | Swap weight |")
    print("|---|---|---|---|")
    found = False
    for i in range(len(ranked) - 1):
        hi, lo = ranked[i], ranked[i + 1]
        for c in weights:
            t = swap_weight(hi["scores"], lo["scores"], weights, c)
            if t is not None:
                found = True
                print(f"| {hi['id']} over {lo['id']} | {c} | {weights[c]:.2f} | {t:.3f} |")
    if not found:
        print("| none | | | no single-criterion weight change swaps adjacent options |")
    return 0


# ---------- RICE ----------

def run_rice(args, response):
    inits = args["initiatives"]
    problems, notes = [], []
    for it in inits:
        for k in ("reach", "impact", "confidence", "effort"):
            if it.get(k) is None:
                problems.append(f"{it.get('id')}: no {k} (ask the person; do not fill it)")
        if it.get("impact") is not None and it["impact"] not in IMPACTS:
            notes.append(f"{it['id']}: impact {it['impact']} is not one of 0.25, 0.5, 1, 2, 3 (the connector accepted 1.5 without warning)")
        c = it.get("confidence")
        if c is not None and 0 < c <= 1:
            notes.append(f"{it['id']}: confidence {c} looks like a fraction; the connector reads confidence as a percent, so send {c * 100:g}")
        if it.get("effort") == 0:
            problems.append(f"{it['id']}: effort 0 cannot divide")
    if problems:
        print("Cannot rank:")
        for p in problems:
            print(" -", p)
        return 2
    def score(it):
        c = it["confidence"]
        c = c if c > 1 else c * 100  # treat a fraction as the percent the person meant
        return it["reach"] * it["impact"] * (c / 100) / it["effort"]
    got = {}
    if response:
        got = {r["id"]: r.get("score") for r in response.get("results", [])}
    ranked = sorted(inits, key=score, reverse=True)
    print("| Rank | Initiative | Score (confidence as percent) | Connector score | Match |")
    print("|---|---|---|---|---|")
    for i, it in enumerate(ranked, 1):
        s = score(it)
        g = got.get(it["id"])
        if g is None:
            match = ""
        elif abs(g - s) < 0.01:
            match = "yes"
        elif s and abs(g * 100 - s) < 0.01 * 100:
            match = "NO: connector score is 1/100 of this (confidence sent as a fraction)"
        else:
            match = "NO"
        print(f"| {i} | {it['id']} | {s:.2f} | {'' if g is None else g} | {match} |")
    if notes:
        print()
        print("Input notes:")
        for n in notes:
            print(" -", n)
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    tool, args, response = load(sys.argv[1])
    if "rice" in tool:
        return run_rice(args, response)
    return run_mcda(args, response)


if __name__ == "__main__":
    sys.exit(main())
