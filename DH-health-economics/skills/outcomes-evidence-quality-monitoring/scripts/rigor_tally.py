#!/usr/bin/env python3
"""Tally the person's risk-of-bias judgments and apply the person's scoring rule.

Usage: python3 rigor_tally.py JUDGMENTS.csv RULE.json [--md OUT.md]

JUDGMENTS.csv columns: study_id, result_id, tool, domain, judgment, note
  tool: ROBINS-I (2016 published version) or RoB2
  judgment: the reviewer's level, in the tool's own words (see LEVELS)
RULE.json (the person's rule; see examples/illustrative_rule.json):
  {"overall": {"ROBINS-I": "least_favorable" | "custom", "RoB2": "least_favorable"},
   "points": {"Low": 3, ...}            optional, the person's points per level
   "domain_weights": {"confounding": 2}  optional, default weight 1
   "rule_owner": "name the person gave"}

Fixed by the sources (references/rigor-checks.md):
  ROBINS-I 2016 domains and levels ........ ES-75 (DOI 10.1136/bmj.i4919), ES-76
  ROBINS-I critical in any domain -> critical overall, exclude from synthesis ... ES-77
  RoB 2 domains and levels ................. ES-71, ES-73
  RoB 2 overall = least favorable domain ... ES-74
Not fixed by the sources and therefore the person's: the ROBINS-I overall level when no
domain is critical ([GAP] in the sourced rows), any points, weights or study score.
No validated quality score exists for CHEERS (HE-005) and GRADE is not a score (ES-94):
the script labels every score "your rule, not a validated score".
"""
import csv
import json
import sys
from collections import defaultdict

DOMAINS = {
    "ROBINS-I": ["confounding", "selection of participants", "classification of interventions",
                 "deviations from intended interventions", "missing data", "measurement of outcomes",
                 "selection of the reported result"],
    "RoB2": ["randomization process", "deviations from intended interventions", "missing outcome data",
             "measurement of the outcome", "selection of the reported result"],
}
LEVELS = {
    "ROBINS-I": ["Low", "Moderate", "Serious", "Critical"],  # least to most severe; "No information" separate
    "RoB2": ["Low", "Some concerns", "High"],
}
NOINFO = "No information"
GAP = "[GAP]"


def norm_tool(t):
    t = (t or "").replace(" ", "").upper()
    if t in ("ROBINS-I", "ROBINSI"):
        return "ROBINS-I"
    if t in ("ROB2", "ROB-2"):
        return "RoB2"
    return None


def overall(tool, judged, rule):
    levels = LEVELS[tool]
    known = [j for j in judged.values() if j in levels]
    notes = []
    missing = [d for d in DOMAINS[tool] if d not in judged]
    if missing:
        notes.append(f"domains not judged: {', '.join(missing)} {GAP}")
    if any(j == NOINFO for j in judged.values()):
        notes.append("one or more domains 'No information'")
    if tool == "ROBINS-I" and "Critical" in known:
        return "Critical", notes + ["critical in at least one domain: exclude from any synthesis (ES-77)"]
    if not known:
        return f"Not determinable {GAP}", notes
    worst = max(known, key=levels.index)
    if tool == "RoB2":
        extra = []
        if worst == "Some concerns" and sum(j == "Some concerns" for j in known) >= 2:
            extra = ["two or more domains 'Some concerns': ES-74 lets reviewers judge High overall; their call"]
        return worst, notes + ["least favorable domain (ES-74)"] + extra
    how = (rule.get("overall") or {}).get("ROBINS-I")
    if how == "least_favorable":
        return worst, notes + ["least favorable domain: your rule; the sourced rows fix only the critical case"]
    return f"Your rule not given {GAP} (least favorable domain would be {worst}, proposed)", notes


def run(rows, rule):
    by_result = defaultdict(dict)
    tools = {}
    problems = []
    for r in rows:
        tool = norm_tool(r.get("tool"))
        key = (r["study_id"].strip(), r["result_id"].strip())
        if tool is None:
            problems.append(f"{key}: tool '{r.get('tool')}' not recognized (ROBINS-I 2016 or RoB2) {GAP}")
            continue
        dom = r["domain"].strip().lower()
        j = r["judgment"].strip()
        if dom not in DOMAINS[tool]:
            problems.append(f"{key}: domain '{dom}' is not a {tool} domain")
            continue
        if j not in LEVELS[tool] and j != NOINFO:
            problems.append(f"{key}: level '{j}' is not a {tool} level")
            continue
        tools[key] = tool
        by_result[key][dom] = j

    points = rule.get("points") or {}
    weights = rule.get("domain_weights") or {}
    results = []
    for key, judged in by_result.items():
        tool = tools[key]
        ov, notes = overall(tool, judged, rule)
        score = None
        if points:
            got = [(points.get(j), weights.get(d, 1)) for d, j in judged.items() if points.get(j) is not None]
            unscored = [d for d, j in judged.items() if points.get(j) is None]
            if got and not unscored and len(judged) == len(DOMAINS[tool]):
                score = round(sum(p * w for p, w in got) / sum(w for _, w in got), 2)
            else:
                notes.append(f"score not computed: unscored or missing domains {GAP}")
        results.append({"study": key[0], "result": key[1], "tool": tool, "overall": ov,
                        "score": score, "notes": notes, "judged": judged})
    return results, problems


def to_md(results, problems, rule):
    owner = rule.get("rule_owner") or "owner not named"
    out = ["Rigor tally from your judgments", f"Scoring rule: yours ({owner}); not a validated score (HE-005, ES-94).", "",
           "| Study | Result | Tool | Overall | Score (your rule) | Notes |", "|---|---|---|---|---|---|"]
    for r in sorted(results, key=lambda x: (x["study"], x["result"])):
        out.append(f"| {r['study']} | {r['result']} | {r['tool']} | {r['overall']} | "
                   f"{r['score'] if r['score'] is not None else '-'} | {'; '.join(r['notes'])} |")
    counts = defaultdict(int)
    for r in results:
        label = "Your rule not given" if r["overall"].startswith("Your rule") else r["overall"].replace(" " + GAP, "")
        counts[label] += 1
    out += ["", "Overall levels across results: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))]
    if problems:
        out += ["", "Input problems:"] + [f"- {p}" for p in problems]
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    with open(sys.argv[1], newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    with open(sys.argv[2], encoding="utf-8") as fh:
        rule = json.load(fh)
    res, probs = run(rows, rule)
    md = to_md(res, probs, rule)
    if "--md" in sys.argv:
        with open(sys.argv[sys.argv.index("--md") + 1], "w", encoding="utf-8") as fh:
            fh.write(md + "\n")
    print(md)
