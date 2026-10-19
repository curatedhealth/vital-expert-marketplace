#!/usr/bin/env python3
"""Check an analytics.mcda ranking and find where adjacent options swap.

Input: a JSON file holding either
  - the saved live call file (examples/live/*.json): the first call named
    "analytics.mcda" is used, with its "arguments" and "results"; or
  - an object {"alternatives": [...], "criteria_weights": {...}} with the
    person's own scores and weights (optionally "results" from the tool).

What it does:
  1. Recomputes each option's value as the tool describes it
     (weighted sum on the 0 to 4 scale, scaled to 100) and compares it
     with the tool's value_estimate when one is present.
  2. Flags ties.
  3. For each adjacent pair in the ranking and each criterion, finds the
     weight at which the pair would swap if that criterion's weight moved
     and the other weights were kept in proportion. Only swap weights
     between 0 and 1 are reported.

The scores and weights are the person's. This script ranks nothing new and
proposes no score.

Usage: python3 mcda_swap_points.py FILE
"""
import json
import sys

TOL = 1e-9


def load(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if "calls" in data:
        for call in data["calls"]:
            if call.get("call") == "analytics.mcda":
                args = call["arguments"]
                return args["alternatives"], args["criteria_weights"], call.get("results")
        sys.exit("No analytics.mcda call in this file.")
    return data["alternatives"], data["criteria_weights"], data.get("results")


def value(scores, weights):
    return sum(weights[c] * scores.get(c, 0) for c in weights) / 4 * 100


def swap_weight(a, b, weights, crit):
    """Weight of crit at which value(a) == value(b), others in proportion."""
    w = weights[crit]
    d = {c: a.get(c, 0) - b.get(c, 0) for c in weights}
    total = sum(weights[c] * d[c] for c in weights)
    if abs(1 - w) < TOL:
        return None
    rest = (total - w * d[crit]) / (1 - w)  # average gap on the other criteria
    if abs(rest - d[crit]) < TOL:
        return None
    x = rest / (rest - d[crit])
    # Strictly inside (0, 1): at 0 or 1 the pair only ties on one criterion.
    if 1e-6 < x < 1 - 1e-6 and abs(x - w) > TOL:
        return x
    return None


def main(path):
    alts, weights, results = load(path)
    wsum = sum(weights.values())
    print(f"Weights sum to {wsum:.4f}" + ("" if abs(wsum - 1) < 1e-6 else "  WARNING: not 1"))
    tool = {r["id"]: r.get("value_estimate") for r in (results or [])}
    rows = []
    for alt in alts:
        v = value(alt["scores"], weights)
        rows.append((alt["id"], v, alt["scores"]))
    rows.sort(key=lambda r: -r[1])

    print("\nRanking (recomputed)")
    for oid, v, _ in rows:
        t = tool.get(oid)
        check = "" if t is None else ("  matches tool" if abs(t - v) < 0.01 else f"  TOOL SAYS {t}")
        print(f"  {v:6.2f}  {oid}{check}")

    print("\nAdjacent pairs")
    for (ia, va, sa), (ib, vb, sb) in zip(rows, rows[1:]):
        gap = va - vb
        if abs(gap) < 0.01:
            print(f"  TIE: '{ia}' and '{ib}' both {va:.2f}. The order between them is not decided by the scores.")
            continue
        print(f"  '{ia}' leads '{ib}' by {gap:.2f}.")
        found = False
        for crit in weights:
            x = swap_weight(sa, sb, weights, crit)
            if x is not None:
                found = True
                print(f"    swaps if '{crit}' weight moves from {weights[crit]:.2f} to {x:.2f} (others in proportion)")
        if not found:
            print("    no single weight change between 0 and 1 swaps them")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
