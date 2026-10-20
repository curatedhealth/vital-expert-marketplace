#!/usr/bin/env python3
"""Check an intervention specification for completeness and traceability.

Usage:
    python3 spec_check.py SPEC.json [--format text|json]

The specification is a JSON file the person (or task A2) writes. Shape:

{
  "product": "...", "version": "...",
  "claims": [{"id": "C1", "text": "...", "status": "sourced|gap|refused",
              "source": {"ref": "DOI or URL", "passage": "...", "locator": "..."},
              "population": "..."}],
  "program_theory": {"components": [...], "mechanisms": [...], "context": [...],
                     "proximal_outcomes": [...], "distal_outcome": "..."},
  "tidier": {"1": "text", "2": "text", ..., "11": "text"},
  "decision_rules": [{"id": "R1", "decision_point": "...", "tailoring_variables": [...],
                      "options": [...], "rule": "...", "missing_data": "...",
                      "claim_ids": ["C1"]}],
  "limits": [{"id": "L1", "not_covered": "...", "behavior_off": "...", "reopen_owner": "..."}]
}

A field holding "[GAP]", "", null or a missing key is open. "N/A" is accepted
for TIDieR items only (TM36). A TIDieR item whose text describes what the person
supplied and marks only part of it "[GAP]" counts as filled, with open parts
listed (task A2 Step 2: fill from the person's description first). The script counts and lists; it never judges
whether a mechanism works or a rule is acceptable. Row ids refer to
references/therapeutic-mechanism-and-translation-research.md.
"""
import argparse
import json
import re
import sys

TIDIER_ITEMS = {
    "1": "Brief name (TM22)",
    "2": "Why: rationale, theory or goal of essential elements (TM23)",
    "3": "What: materials (TM24)",
    "4": "What: procedures (TM25)",
    "5": "Who provided (TM26)",
    "6": "How: modes of delivery (TM27)",
    "7": "Where (TM28)",
    "8": "When and how much: sessions, schedule, duration, dose (TM29)",
    "9": "Tailoring: what, why, when, how (TM30)",
    "11": "How well, planned: how fidelity is assessed and maintained (TM32)",
}
# Items 10 and 12 cannot be completed before the intervention is delivered (TM34).
NOT_FOR_SPEC = {"10": "Modifications (TM31)", "12": "How well, actual (TM33)"}

THEORY_PARTS = {
    "components": "key components (TM6)",
    "mechanisms": "mechanisms: causal links from components to outcomes (TM6, TM8)",
    "context": "contextual features that influence the mechanisms (TM6, TM9)",
    "proximal_outcomes": "proximal outcomes (TM84)",
    "distal_outcome": "distal outcome (TM83)",
}

RULE_PARTS = {
    "decision_point": "decision point (TM78)",
    "options": "intervention options (TM79)",
    "tailoring_variables": "tailoring variables (TM80)",
    "rule": "decision rule (TM82)",
    "missing_data": "behavior when tailoring data are missing (TM89)",
}

PAPER_DOI = {
    "TM6": "10.1136/bmj.n2061", "TM8": "10.1136/bmj.n2061", "TM9": "10.1136/bmj.n2061",
    "TM22": "10.1136/bmj.g1687", "TM36": "10.1136/bmj.g1687",
    "TM77": "10.1007/s12160-016-9830-8",
}


def is_open(value):
    if value is None:
        return True
    if isinstance(value, str):
        v = value.strip()
        return v == "" or "[GAP]" in v
    if isinstance(value, (list, dict)):
        return len(value) == 0 or all(is_open(x) for x in (value if isinstance(value, list) else value.values()))
    return False


def has_content(value):
    """True when a string holds described content besides its [GAP] markers."""
    rest = re.sub(r"\[GAP\][^;,.()]*", " ", value)
    words = re.findall(r"[A-Za-z0-9]+", rest)
    return len(words) >= 2


def check(spec):
    out = {"product": spec.get("product", "[GAP]"), "version": spec.get("version", "[GAP]")}

    # TIDieR
    tid = spec.get("tidier", {}) or {}
    filled, partial, na, open_items = [], [], [], []
    for k, label in TIDIER_ITEMS.items():
        v = tid.get(k)
        if isinstance(v, str) and v.strip().upper() == "N/A":
            na.append(k)
        elif isinstance(v, str) and "[GAP]" in v and has_content(v):
            filled.append(k)
            partial.append(f"{k} {label}")
        elif is_open(v):
            open_items.append(f"{k} {label}")
        else:
            filled.append(k)
    out["tidier"] = {"filled": len(filled), "filled_with_open_parts": len(partial), "na": len(na),
                     "open": len(open_items), "total": len(TIDIER_ITEMS), "open_items": open_items,
                     "partial_items": partial,
                     "not_for_spec": [f"{k} {v}" for k, v in NOT_FOR_SPEC.items()]}

    # Program theory
    pt = spec.get("program_theory", {}) or {}
    out["program_theory_open"] = [label for key, label in THEORY_PARTS.items() if is_open(pt.get(key))]

    # Claims
    claims = {c.get("id"): c for c in spec.get("claims", [])}
    claim_rows = []
    for cid, c in claims.items():
        status = (c.get("status") or "gap").lower()
        src = c.get("source") or {}
        issues = []
        if status == "sourced":
            if is_open(src.get("ref")):
                issues.append("marked sourced but no source reference")
            if is_open(src.get("passage")):
                issues.append("no passage quoted: support not checked (N3)")
            if is_open(c.get("population")):
                issues.append("source population not stated")
        claim_rows.append({"id": cid, "status": status, "issues": issues})
    out["claims"] = claim_rows

    # Decision rules
    rule_rows = []
    for r in spec.get("decision_rules", []):
        missing = [label for key, label in RULE_PARTS.items() if is_open(r.get(key))]
        trace = []
        cids = r.get("claim_ids") or []
        if not cids:
            trace.append("traces to no claim")
        for cid in cids:
            c = claims.get(cid)
            if c is None:
                trace.append(f"claim {cid} not in the claim map")
            elif (c.get("status") or "gap").lower() != "sourced":
                trace.append(f"rests on claim {cid} with status {c.get('status') or 'gap'}: do not build (old DH-01.01.4.1.1 rule)")
        rule_rows.append({"id": r.get("id"), "missing": missing, "trace": trace})
    out["decision_rules"] = rule_rows

    # Limits
    lim_rows = []
    for l in spec.get("limits", []):
        miss = [k for k in ("not_covered", "behavior_off") if is_open(l.get(k))]
        owner = l.get("reopen_owner")
        lim_rows.append({"id": l.get("id"), "missing": miss,
                         "reopen_owner": owner if not is_open(owner) else "owner not named"})
    out["limits"] = lim_rows
    return out


def render(out):
    lines = []
    lines.append(f"Intervention specification check: {out['product']} {out['version']}")
    lines.append("A count, not a verdict. Nothing here says the mechanism works or a rule is acceptable.")
    t = out["tidier"]
    lines.append(f"TIDieR items for a specification: {t['filled']} filled ({t['filled_with_open_parts']} with open parts), "
                 f"{t['na']} N/A, {t['open']} open, of {t['total']} "
                 f"(TIDieR, DOI 10.1136/bmj.g1687; items 10 and 12 not completed before delivery, TM34, DOI 10.1136/bmj.g1687).")
    for i in t["partial_items"]:
        lines.append(f"  filled, open parts: {i}")
    for i in t["open_items"]:
        lines.append(f"  open: {i}")
    if out["program_theory_open"]:
        lines.append("Program theory open (TM6, DOI 10.1136/bmj.n2061):")
        for p in out["program_theory_open"]:
            lines.append(f"  open: {p}")
    else:
        lines.append("Program theory: all five parts present (TM6, DOI 10.1136/bmj.n2061). Still a hypothesis until tested.")
    lines.append("Claims:")
    for c in out["claims"]:
        tail = "; ".join(c["issues"]) if c["issues"] else "no structural issue"
        lines.append(f"  {c['id']} [{c['status']}]: {tail}")
    lines.append("Decision rules (JITAI components, TM77, DOI 10.1007/s12160-016-9830-8):")
    for r in out["decision_rules"]:
        parts = r["missing"] + r["trace"]
        lines.append(f"  {r['id']}: " + ("; ".join(parts) if parts else "all five parts present and traced to sourced claims"))
    lines.append("Limits:")
    for l in out["limits"]:
        miss = ("missing " + ", ".join(l["missing"]) + "; ") if l["missing"] else ""
        lines.append(f"  {l['id']}: {miss}reopened only by: {l['reopen_owner']}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    a = ap.parse_args()
    with open(a.spec, encoding="utf-8") as f:
        spec = json.load(f)
    out = check(spec)
    print(json.dumps(out, indent=2) if a.format == "json" else render(out))


if __name__ == "__main__":
    sys.exit(main())
