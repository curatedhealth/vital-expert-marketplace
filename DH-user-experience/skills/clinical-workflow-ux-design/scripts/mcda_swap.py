#!/usr/bin/env python3
"""Weighted ranking of design options the person scored, plus swap points.

Copied from the QMS design skill (qms-design-and-governance) and adapted to read
the saved call format used here.

Input: a JSON file holding {"alternatives": [{"id": ..., "scores": {criterion: 0-4}}],
"criteria_weights": {criterion: weight}} or a saved analytics.mcda call
(examples/live/mcda_alert_placement.json, which keeps them under arguments).

Output: the value per option computed as analytics.mcda does (sum of weight times
score / 4, times 100), a check against the connector response when the file holds one,
and, for each criterion and each pair of adjacent options, the weight on that criterion
at which the two would swap (other weights rescaled in proportion). The script never
creates a score or a weight: missing scores stop it.

Usage: python3 mcda_swap.py FILE [--markdown]
"""
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    args = data.get("arguments") or data.get("call", {}).get("arguments", data)
    response = data.get("response")
    return args["alternatives"], args.get("criteria_weights", {}), response


def check_inputs(alts, weights):
    problems = []
    crits = list(weights)
    if not crits:
        problems.append("no criteria_weights given: the person sets the weights")
    total = sum(weights.values())
    if crits and abs(total - 1) > 1e-6:
        problems.append(f"weights sum to {total:.4f}, not 1")
    for a in alts:
        for c in crits:
            s = a["scores"].get(c)
            if s is None:
                problems.append(f"{a['id']}: no score for {c} (ask the person; do not fill it)")
            elif not 0 <= s <= 4:
                problems.append(f"{a['id']}: score {s} for {c} is outside 0 to 4")
    return problems


def value(scores, weights):
    return sum(weights[c] * scores[c] / 4 for c in weights) * 100


def swap_weight(si, sj, weights, c):
    """Weight on criterion c at which options i and j have equal value, or None."""
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
    if 0 < t < 1 - 1e-9:
        return t
    return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    alts, weights, response = load(sys.argv[1])
    problems = check_inputs(alts, weights)
    if problems:
        print("Cannot rank:")
        for p in problems:
            print(" -", p)
        sys.exit(2)
    ranked = sorted(alts, key=lambda a: value(a["scores"], weights), reverse=True)
    print("| Rank | Option | Value (0 to 100) |")
    print("|---|---|---|")
    for i, a in enumerate(ranked, 1):
        print(f"| {i} | {a['id']} | {value(a['scores'], weights):.2f} |")
    if response:
        conn = {r["id"]: r["value_estimate"] for r in response.get("results", [])}
        diffs = [a["id"] for a in alts if a["id"] in conn and abs(conn[a["id"]] - value(a["scores"], weights)) > 0.01]
        print()
        print("Connector check: " + ("values match analytics.mcda" if not diffs else "differs for " + ", ".join(diffs)))
    print()
    print("| Pair (higher first) | Criterion | Current weight | Weight at which they swap |")
    print("|---|---|---|---|")
    found = False
    for hi, lo in zip(ranked, ranked[1:]):
        for c in weights:
            t = swap_weight(hi["scores"], lo["scores"], weights, c)
            if t is not None and abs(t - weights[c]) > 1e-9:
                found = True
                print(f"| {hi['id']} over {lo['id']} | {c} | {weights[c]:.2f} | {t:.2f} |")
    if not found:
        print("| none | | | no single-criterion weight change in 0 to 1 swaps adjacent options |")
    print()
    print("Scores and weights are the person's. Values rank only what was scored; they are not a recommendation.")


if __name__ == "__main__":
    main()
