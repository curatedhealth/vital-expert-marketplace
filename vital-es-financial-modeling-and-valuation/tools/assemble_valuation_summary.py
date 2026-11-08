#!/usr/bin/env python3
"""Assemble the valuation summary from the registers of the nine valuation skills (V1 to V9). Deterministic, offline, standard library only.

Usage: assemble_valuation_summary.py manifest.json [--out summary.json] [--md summary.md] [--thresholds client.json]
Exit 0 = assembled, 1 = hard error, 2 = usage or file error.

This is a plugin-level tool, not a competency. It adds no finding of its own: every line points to a register (skill code and results pointer); an unresolved pointer
fails. It recommends nothing and states no fairness or solvency view; a recommending, fairness or single-value sentence fails. The adopted valuation is HUMAN ONLY.
No network access. Statuses are proposed by a stated ENGINEERING RULE (team-set defaults, a client may override); they are not a standard. Deterministic.
Manifest: {"asset": str, "mode": "asset|company", "as_of": ISO date, "outputs": {"V1": path, ..., "V9": path}, "extra_lines": [{"text": str, "pointer": "V2:range"}],
           "prepared_by": str|null, "reviewed_by": str|null}. A skill code with no path is a GAP and its workstream is proposed red.
"""
import argparse
import json
import re
import sys
from pathlib import Path

CODES = {"V1": "build-dcf-model", "V2": "calculate-risk-adjusted-npv", "V3": "validate-valuation-assumptions", "V4": "design-valuation-scenarios", "V5": "analyze-valuation-sensitivity",
         "V6": "communicate-valuation-scenarios", "V7": "identify-comparable-transactions", "V8": "compare-deal-terms-to-benchmarks", "V9": "synthesize-market-standard-terms"}
REQUIRES = {"V2": ["V1"], "V5": ["V2", "V4"], "V6": ["V5"], "V8": ["V7"], "V9": ["V8", "V2"]}
DEFAULTS = {"yellow_if_gaps_at_least": 1, "yellow_if_triggered_at_least": 1, "red_if_gaps_at_least": 5, "red_if_triggered_at_least": 3}
HUMAN_ONLY = ["the choice of discount rate or rates", "the final probability of success", "the adopted valuation", "any fairness or solvency view", "deal terms"]
PHRASES = [(r"\bwe (strongly )?(recommend|advise|suggest)\b", "E_RECOMMEND"), (r"\bis recommended\b", "E_RECOMMEND"), (r"\bshould (sign|proceed|bid|pay|accept|offer|walk away|pass)\b", "E_RECOMMEND"),
           (r"\bfair (value|price|to)\b", "E_FAIRNESS"), (r"\bis (a )?fair\b", "E_FAIRNESS"), (r"\bundervalued\b", "E_FAIRNESS"), (r"\bovervalued\b", "E_FAIRNESS"), (r"\boverpa(y|ying|id)\b", "E_FAIRNESS"),
           (r"\bsolven(t|cy)\b", "E_FAIRNESS"), (r"\bfairness opinion\b", "E_FAIRNESS"), (r"\bthe (asset|deal|company) is worth\b", "E_POINT")]
PTR = re.compile(r"^(V[1-9]):[A-Za-z0-9_.\-\[\]]+$")


class Hard(Exception):
    def __init__(self, code, msg):
        super().__init__(f"{code}: {msg}")
        self.code = code


def check_text(label, text):
    for rx, code in PHRASES:
        if re.search(rx, text, re.I):
            raise Hard(code, f"{label}: recommends, gives a fairness or solvency view, or states one number as the value")


def find_ranges(results):
    out = {}
    for k, v in (results or {}).items():
        if isinstance(v, dict) and "low" in v and "high" in v and v["low"] != v["high"]:
            out[k] = v
    return out


def load(manifest, base):
    regs, gaps = {}, []
    outs = manifest.get("outputs") or {}
    for c in CODES:
        p = outs.get(c)
        if not p:
            gaps.append({"skill": c, "missing": f"no {CODES[c]} register supplied", "why_it_matters": "its workstream cannot be assessed and is proposed red", "run": CODES[c]})
            continue
        path = Path(p) if Path(p).is_absolute() else Path(base) / p
        try:
            reg = json.loads(path.read_text())
        except Exception as ex:
            raise Hard("E_FILE", f"{c}: {path}: {ex}")
        if reg.get("adopted_valuation") != "HUMAN ONLY":
            raise Hard("E_ADOPT", f"{c}: adopted_valuation must be exactly HUMAN ONLY")
        if reg.get("recommended_valuation") is not None:
            raise Hard("E_ADOPT", f"{c}: recommended_valuation must be null")
        if not (reg.get("results") or {}).get("pointer"):
            raise Hard("E_POINTER", f"{c}: results.pointer missing")
        for s in json.dumps(reg).split('"'):
            if len(s) > 20:
                check_text(c, s)
        regs[c] = reg
    return regs, gaps


def status(code, reg, th):
    if reg is None:
        return "red", "no register supplied"
    fm = reg.get("failure_mode_screen") or []
    trig = sum(1 for f in fm if f.get("state") == "triggered") + sum(1 for f in fm if f.get("state") == "cannot tell")
    g = len(reg.get("gaps") or [])
    if g >= th["red_if_gaps_at_least"] or trig >= th["red_if_triggered_at_least"]:
        return "red", f"{g} gaps, {trig} failure modes triggered or cannot tell"
    if g >= th["yellow_if_gaps_at_least"] or trig >= th["yellow_if_triggered_at_least"]:
        return "yellow", f"{g} gaps, {trig} failure modes triggered or cannot tell"
    return "green", "no gaps; no failure mode triggered"


def assemble(manifest, base=".", thresholds=None):
    th = dict(DEFAULTS, **(thresholds or {}))
    regs, gaps = load(manifest, base)
    ws = []
    for c in CODES:
        s, why = status(c, regs.get(c), th)
        row = {"skill": c, "name": CODES[c], "status": s, "basis": why, "pointer": f"{c}:{regs[c]['results']['pointer'].split(':', 1)[-1]}" if c in regs else None}
        miss = [r for r in REQUIRES.get(c, []) if r not in regs]
        if miss and c in regs:
            row["note"] = "built without " + ", ".join(miss) + " (its input is missing)"
        ws.append(row)
    for c, reg in regs.items():
        for g in reg.get("gaps") or []:
            gaps.append({"skill": c, "missing": g.get("missing") or g.get("field"), "why_it_matters": g.get("why_it_matters"), "pointer": f"{c}:gaps"})
    ranges = {c: find_ranges(reg.get("results")) for c, reg in regs.items()}
    model = next(((c, k, v) for c in ("V6", "V5", "V2", "V1") for k, v in ranges.get(c, {}).items() if c in regs), None)
    bench = next(((c, k, v) for c in ("V9", "V8") for k, v in ranges.get(c, {}).items() if c in regs), None)
    conflicts = []
    if model and bench and (model[2]["high"] < bench[2]["low"] or bench[2]["high"] < model[2]["low"]):
        conflicts.append({"rule": "model and benchmark ranges do not overlap", "side_a": {"pointer": f"{model[0]}:{model[1]}", "range": [model[2]["low"], model[2]["high"]]},
                          "side_b": {"pointer": f"{bench[0]}:{bench[1]}", "range": [bench[2]["low"], bench[2]["high"]]}, "reconciled": False, "note": "both sides shown; not averaged or merged"})
    lines = []
    if model:
        lines.append({"text": f"Model range {model[2]['low']} to {model[2]['high']} {model[2].get('unit', '')}".strip(), "pointer": f"{model[0]}:{model[1]}"})
    if bench:
        lines.append({"text": f"Benchmark range {bench[2]['low']} to {bench[2]['high']} {bench[2].get('unit', '')} (a different question; not merged)".strip(), "pointer": f"{bench[0]}:{bench[1]}"})
    for ex in manifest.get("extra_lines") or []:
        m = PTR.match(ex.get("pointer", ""))
        if not m or m.group(1) not in regs:
            raise Hard("E_POINTER", f"line has no resolvable pointer: {ex.get('text', '')[:60]!r}")
        check_text("extra line", ex.get("text", ""))
        lines.append(ex)
    decisions = [{"decision": d, "decider": "deal lead (BD head or investment lead)"} for d in HUMAN_ONLY]
    reds = [w["skill"] for w in ws if w["status"] == "red"]
    ans = [f"{len(regs)} of 9 valuation registers supplied; proposed red workstreams: {', '.join(reds) if reds else 'none'}.",
           (f"Model range {model[2]['low']} to {model[2]['high']} {model[2].get('unit', '')} [{model[0]}:{model[1]}]; it is a range, not a value." if model else "No model range is available; the valuation cannot be summarized."),
           f"{len(gaps)} open gaps; {len(conflicts)} conflicts shown side by side; the adopted valuation is HUMAN ONLY."]
    return {"asset": manifest.get("asset"), "mode": manifest.get("mode"), "as_of": manifest.get("as_of"), "answer": ans, "workstreams": ws, "lines": lines, "conflicts": conflicts, "gaps": gaps,
            "decisions": decisions, "adopted_valuation": "HUMAN ONLY", "recommended_valuation": None, "status": "UNSIGNED", "prepared_by": manifest.get("prepared_by"), "reviewed_by": manifest.get("reviewed_by"),
            "thresholds": th, "note": "Statuses are proposed by a stated engineering rule and are not a standard; the deal lead confirms them."}


def to_md(s):
    o = [f"# Valuation summary: {s['asset']}", "", f"As of {s['as_of']}. Status: {s['status']}. Adopted valuation: {s['adopted_valuation']}.", "", "## 1. Answer in three lines"] + [f"- {a}" for a in s["answer"]]
    o += ["", "## 2. Proposed workstream status", "| Skill | Workstream | Proposed status | Basis | Pointer |", "|---|---|---|---|---|"]
    o += [f"| {w['skill']} | {w['name']} | {w['status']} | {w['basis']}{'; ' + w['note'] if w.get('note') else ''} | {w['pointer'] or 'GAP'} |" for w in s["workstreams"]]
    o += ["", "## 3. Ranges and what they rest on"] + [f"- {l['text']} [{l['pointer']}]" for l in s["lines"]]
    o += ["", "## 4. Conflicts side by side"] + ([f"- {c['rule']}: {c['side_a']['pointer']} {c['side_a']['range']} against {c['side_b']['pointer']} {c['side_b']['range']}; {c['note']}" for c in s["conflicts"]] or ["- none by the stated rules"])
    o += ["", "## 5. Open gaps"] + ([f"- {g['skill']}: {g['missing']}. {g['why_it_matters']}" + (f" Run: {g['run']}." if g.get("run") else "") for g in s["gaps"]] or ["- none"])
    o += ["", "## 6. Decisions needed (human only)"] + [f"- {d['decision']}: {d['decider']}" for d in s["decisions"]]
    o += ["", "## 7. Sign-off", f"Prepared by: {s['prepared_by'] or '[not set]'}. Reviewed by: {s['reviewed_by'] or '[not set]'}. Status: {s['status']}.", "", f"_{s['note']}_"]
    return "\n".join(o) + "\n"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--out")
    ap.add_argument("--md")
    ap.add_argument("--thresholds")
    a = ap.parse_args(argv)
    try:
        mp = Path(a.manifest)
        man = json.loads(mp.read_text())
        th = json.loads(Path(a.thresholds).read_text()) if a.thresholds else None
    except Exception as ex:
        print(f"E_FILE: {ex}", file=sys.stderr)
        return 2
    try:
        s = assemble(man, mp.parent, th)
    except Hard as h:
        print(str(h), file=sys.stderr)
        return 1
    if a.out:
        Path(a.out).write_text(json.dumps(s, indent=1) + "\n")
    if a.md:
        Path(a.md).write_text(to_md(s))
    if not a.out and not a.md:
        print(json.dumps(s, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
