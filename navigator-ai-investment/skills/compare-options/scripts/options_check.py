#!/usr/bin/env python3
"""Option comparison: computes and checks; never scores, never chooses.

Mirrors the Navigator template nav.options (version 1) and engine: six criteria, whole numbers
1 to 10, equal weight per scorer; cost criteria count as 11 - x; composite = weight-normalized
mean (1 to 10); a baseline option is required; weight changes need a reason and the unadjusted
result is returned beside the adjusted one; ranked by composite, then median of scorers' own
composites, then id; spread of 3 or more flagged; fewer than three scorers indicative; owner's
view computed separately; sensitivity drops each scorer and moves each weight by -20% and +20%.
Owner ruling (19 October 2026): the baseline is a reference line, not a contender. Options are
ranked among themselves (the engine ranks the baseline too; the order of the other options is the
same); each option shows its difference from the baseline composite; sensitivity reads the leader
among the options. If the baseline scores above every option, that is reported plainly.

Input (JSON):
  {"options": [{"id": "b", "label": "Do it internally", "is_baseline": true},
               {"id": "a", "label": "Medical writing copilot"}, ...],
   "scores": [{"scorer_id": "CMO", "item_id": "a", "criterion_key": "outcome_fit", "value": 8}, ...],
   "weight_adjustments": [{"criterion_key": "risk", "weight": 2, "reason": "..."}],   optional
   "owner_scorer_id": "CMO"}                                                            optional

Usage:  python3 options_check.py input.json [--json]
"""

from __future__ import annotations

import json
import sys
from statistics import mean, median

CRITERIA = [
    ("outcome_fit", "Outcome fit", "benefit"),
    ("cost", "Cost", "cost"),
    ("time", "Time", "cost"),
    ("reversibility", "Reversibility", "benefit"),
    ("risk", "Risk", "cost"),
    ("governance_burden", "Governance burden", "cost"),
]
KEYS = [c[0] for c in CRITERIA]
DIRECTION = {c[0]: c[2] for c in CRITERIA}
LABEL = {c[0]: c[1] for c in CRITERIA}
SPREAD = 3


class CheckError(ValueError):
    pass


def _parse(payload):
    opts = payload.get("options")
    if not isinstance(opts, list) or len(opts) < 2:
        raise CheckError("options must list at least two options, one of them the baseline")
    labels, baselines = {}, []
    for i, o in enumerate(opts):
        if not isinstance(o, dict) or not o.get("id"):
            raise CheckError(f"options[{i}]: id is required")
        flag = o.get("is_baseline", False)
        if not isinstance(flag, bool):
            raise CheckError(f"options[{i}]: is_baseline must be true or false")
        labels[o["id"]] = o.get("label", o["id"])
        if flag:
            baselines.append(o["id"])
    if not baselines:
        raise CheckError("a baseline option is required (for example 'do nothing' or 'do it internally'); mark one with is_baseline: true")
    grid = {}
    for n, s in enumerate(payload.get("scores") or []):
        sid, it, k, v = s.get("scorer_id"), s.get("item_id"), s.get("criterion_key"), s.get("value")
        if not sid:
            raise CheckError(f"scores[{n}]: scorer_id is required")
        if it not in labels:
            raise CheckError(f"scores[{n}]: unknown option {it!r}")
        if k not in KEYS:
            raise CheckError(f"scores[{n}]: unknown criterion {k!r}; expected one of {KEYS}")
        if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 10:
            raise CheckError(f"scores[{n}]: value must be a whole number 1 to 10, got {v!r}")
        cell = grid.setdefault(sid, {}).setdefault(it, {})
        if k in cell:
            raise CheckError(f"scores[{n}]: {sid} scored {k} on {it} twice")
        cell[k] = v
    if not grid:
        raise CheckError("scores must be a non-empty list")
    missing = [f"{s} on {o}: {k}" for s in grid for o in labels for k in KEYS if k not in grid[s].get(o, {})]
    if missing:
        raise CheckError("every scorer must score every criterion for every option; nothing is filled in. Missing: " + "; ".join(missing))
    weights = {k: 1.0 for k in KEYS}
    adjustments = []
    seen = set()
    for i, a in enumerate(payload.get("weight_adjustments") or []):
        k, w, reason = a.get("criterion_key"), a.get("weight"), (a.get("reason") or "").strip()
        if k not in KEYS:
            raise CheckError(f"weight_adjustments[{i}]: unknown criterion {k!r}")
        if k in seen:
            raise CheckError(f"weight_adjustments[{i}]: {k} adjusted twice")
        if not reason:
            raise CheckError(f"weight_adjustments[{i}]: a weight change needs a reason")
        if isinstance(w, bool) or not isinstance(w, (int, float)) or w < 0:
            raise CheckError(f"weight_adjustments[{i}]: weight must be a number >= 0")
        seen.add(k)
        weights[k] = float(w)
        adjustments.append({"criterion": LABEL[k], "weight": w, "reason": reason})
    if sum(weights.values()) <= 0:
        raise CheckError("at least one weight must be above 0")
    return labels, baselines, grid, weights, adjustments


def _composite(values, weights):
    tot = sum(weights.values())
    return sum(weights[k] * ((11 - values[k]) if DIRECTION[k] == "cost" else values[k]) for k in KEYS) / tot


def _rank(labels, grid, scorers, weights):
    rows = []
    for o in labels:
        means = {k: mean(grid[s][o][k] for s in scorers) for k in KEYS}
        comp = _composite(means, weights)
        med = median(_composite(grid[s][o], weights) for s in scorers)
        crit = {}
        flagged = []
        for k in KEYS:
            vals = [grid[s][o][k] for s in scorers]
            crit[LABEL[k]] = {"mean": round(means[k], 2), "range": [min(vals), max(vals)]}
            if max(vals) - min(vals) >= SPREAD:
                flagged.append(LABEL[k])
        rows.append({"id": o, "label": labels[o], "composite": round(comp, 4), "_med": round(med, 4),
                     "criteria": crit, "disagreement_on": flagged})
    rows.sort(key=lambda r: (-r["composite"], -r["_med"], r["id"]))
    for n, r in enumerate(rows, 1):
        r["rank"] = n
        r["median_of_scorer_composites"] = r.pop("_med")
        r["tie_on_composite"] = sum(1 for x in rows if x["composite"] == r["composite"]) > 1
    return rows


def evaluate(payload):
    labels, baselines, grid, weights, adjustments = _parse(payload)
    scorers = sorted(grid)
    contenders = {k: v for k, v in labels.items() if k not in baselines}
    if not contenders:
        raise CheckError("at least one option besides the baseline is needed")
    base_rows = _rank({k: labels[k] for k in baselines}, grid, scorers, weights)
    group = _rank(contenders, grid, scorers, weights)
    for r in group:
        r["vs_baselines"] = {b["label"]: round(r["composite"] - b["composite"], 2) for b in base_rows}
        r["beats_baseline"] = all(r["composite"] > b["composite"] for b in base_rows)
    unadjusted = _rank(contenders, grid, scorers, {k: 1.0 for k in KEYS}) if adjustments else None
    owner = payload.get("owner_scorer_id")
    owner_view = None
    if owner is not None:
        if owner not in grid:
            raise CheckError(f"owner {owner!r} has no scores")
        owner_view = {"options": [{"id": r["id"], "composite": r["composite"], "rank": r["rank"]} for r in _rank(contenders, grid, [owner], weights)],
                      "baseline": [{"id": r["id"], "composite": r["composite"]} for r in _rank({k: labels[k] for k in baselines}, grid, [owner], weights)]}
    leader = group[0]["id"]
    flips, n = [], 0
    crossings = []
    base_ids = list(baselines)

    def _crossed(variant, sc, w):
        rows = _rank(labels, grid, sc, w)
        comp = {r["id"]: r["composite"] for r in rows}
        for o in contenders:
            for b in base_ids:
                before = next(x["composite"] for x in group if x["id"] == o) > next(x["composite"] for x in base_rows if x["id"] == b)
                if (comp[o] > comp[b]) != before:
                    crossings.append({"variant": variant, "option": labels[o], "baseline": labels[b],
                                      "now": "above" if comp[o] > comp[b] else "at or below"})
    if len(scorers) >= 2:
        for s in scorers:
            n += 1
            new = _rank(contenders, grid, [x for x in scorers if x != s], weights)
            _crossed(f"without {s}", [x for x in scorers if x != s], weights)
            if new[0]["id"] != leader:
                flips.append({"variant": f"without {s}", "leader": labels[new[0]["id"]], "by_tie": new[0]["tie_on_composite"]})
    for k in KEYS:
        if weights[k] == 0:
            continue
        for f in (0.8, 1.2):
            n += 1
            new = _rank(contenders, grid, scorers, {**weights, k: weights[k] * f})
            _crossed(f"{LABEL[k]} weight x{f}", scorers, {**weights, k: weights[k] * f})
            if new[0]["id"] != leader:
                flips.append({"variant": f"{LABEL[k]} weight x{f}", "leader": labels[new[0]["id"]], "by_tie": new[0]["tie_on_composite"]})
    margin = round(group[0]["composite"] - group[1]["composite"], 4) if len(group) > 1 else None
    allrows = group + base_rows
    extremes = {}
    for k in KEYS:
        vals = [(r["criteria"][LABEL[k]]["mean"], r["label"]) for r in allrows]
        hi, lo = max(vals), min(vals)
        good, bad = (lo, hi) if DIRECTION[k] == "cost" else (hi, lo)
        extremes[LABEL[k]] = {"best": f"{good[1]} ({good[0]})", "worst": f"{bad[1]} ({bad[0]})"}
    return {"scorers": scorers, "indicative": len(scorers) < 3, "best_and_worst_per_criterion": extremes, "weights": {LABEL[k]: w for k, w in weights.items()},
            "weight_adjustments": adjustments, "group": group, "unadjusted": unadjusted, "owner_view": owner_view,
            "baseline": [{"label": r["label"], "composite": r["composite"], "criteria": r["criteria"]} for r in base_rows],
            "no_option_beats_every_baseline": all(not r["beats_baseline"] for r in group),
            "sensitivity": {"status": "close_call" if flips else "stable", "leader": labels[leader],
                            "leader_margin": margin, "variants_evaluated": n, "flips": flips,
                            "leader_test_meaningful": len(group) > 1,
                            "reference_line_crossings": crossings},
            "rule": "Computed from people's scores, equal weight per scorer. Cost, time, risk and governance "
                    "burden count as 11 minus the score. The ranking informs the owner's choice; it does not make it."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (CheckError, json.JSONDecodeError, OSError) as exc:
        print(f"Not computed: {exc}", file=sys.stderr)
        return 2
    if "--json" in argv:
        print(json.dumps(r, indent=2))
        return 0
    head = " | ".join(LABEL[k] for k in KEYS)
    print(f"| Rank | Option | {head} | Composite | Against the baselines | Disagreement |")
    print("|---|---|" + "---|" * len(KEYS) + "---|---|---|")
    for g in r["group"]:
        cells = " | ".join(str(g["criteria"][LABEL[k]]["mean"]) for k in KEYS)
        base = "; ".join(f"{d:+} vs {k}" for k, d in g["vs_baselines"].items())
        print(f"| {g['rank']} | {g['label']} | {cells} | {round(g['composite'], 2)}{' (tied)' if g['tie_on_composite'] else ''} | {base} | {', '.join(g['disagreement_on'])} |")
    for b in r["baseline"]:
        cells = " | ".join(str(b["criteria"][LABEL[k]]["mean"]) for k in KEYS)
        print(f"| ref | {b['label']} (baseline) | {cells} | {round(b['composite'], 2)} | reference line | |")
    print(f"\nScorers: {', '.join(r['scorers'])}." + (" Fewer than three: indicative." if r["indicative"] else ""))
    if r["no_option_beats_every_baseline"]:
        print("No option scores above every baseline.")
    s = r["sensitivity"]
    print("Best and worst per criterion, reference lines included: " + "; ".join(f"{k}: best {v['best']}, worst {v['worst']}" for k, v in r["best_and_worst_per_criterion"].items()))
    lead = s["status"] if s["leader_test_meaningful"] else "one option: no leader to test"
    print(f"Sensitivity ({s['variants_evaluated']} variants: each scorer left out, each weight -20% and +20%): {lead}. " + (f"Flips: {s['flips']}. " if s["flips"] else "")
          + (f"Reference-line crossings: {s['reference_line_crossings']}" if s["reference_line_crossings"] else "No option crosses a reference line."))
    if r["weight_adjustments"]:
        print(f"Weight changes: {r['weight_adjustments']}. Unadjusted ranking: {[x['label'] for x in r['unadjusted']]}")
    if r["owner_view"]:
        print(f"Owner's view (show after the group's): {r['owner_view']}")
    print(r["rule"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
