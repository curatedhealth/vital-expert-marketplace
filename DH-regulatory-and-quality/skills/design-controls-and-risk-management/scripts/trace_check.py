#!/usr/bin/env python3
"""Trace check: find orphans, gaps and broken links in a design-control trace file.

Input
  trace.csv   one row per item, exported from the person's requirements or ALM tool.
              Required columns:
                id      unique item id, for example UN-01, DI-07, RC-03
                type    one of: user_need, design_input, design_output, verification,
                        validation, hazard, risk_control
                links   the ids this item traces UP to, separated by ";" (blank for roots)
              Optional columns:
                text    short wording of the item
                result  for verification and validation rows: pass, fail, or blank
                note    anything the person wants carried into the report
              Expected upward links (the structure in references/trace-structure.md):
                design_input  -> user_need and/or risk_control
                design_output -> design_input
                verification  -> design_input, design_output or risk_control
                validation    -> user_need
                risk_control  -> hazard
                user_need, hazard -> nothing (roots)

Output
  A findings table: item, finding code, what is missing or broken, and the check that
  found it. Findings, not a score. The script never decides whether a finding matters
  or whether a release can go ahead; that is the owner's decision.

Finding codes
  G1 user need with no design input tracing to it
  G2 user need with no validation tracing to it
  G3 design input with no verification (directly or through one of its design outputs)
  G4 hazard with no risk control
  G5 risk control with no verification
  G6 risk control not carried into any design input (check: a control given only as
     information for safety may legitimately sit in labeling; the person decides)
  G7 design input with no design output (working convention: no specification, code
     module or label is recorded as implementing the requirement; QS24 requires the
     design and development file to contain or reference the records)
  O1 non-root item with no upward link (orphan)
  O2 link to an id that is not in the file (dangling)
  O3 link to an item of a type the structure does not expect
  R1 verification or validation with result "fail"
  R2 verification or validation with no result recorded
  D1 duplicate id
  T1 unknown type

Usage: python3 trace_check.py trace.csv [--json] [--only CODE[,CODE]]
"""
import argparse
import csv
import json
import sys
from collections import defaultdict

TYPES = ["user_need", "design_input", "design_output", "verification", "validation", "hazard", "risk_control"]
ROOTS = {"user_need", "hazard"}
EXPECTED_UP = {
    "design_input": {"user_need", "risk_control"},
    "design_output": {"design_input"},
    "verification": {"design_input", "design_output", "risk_control"},
    "validation": {"user_need"},
    "risk_control": {"hazard"},
}
DESCRIPTIONS = {
    "G1": "user need with no design input tracing to it",
    "G2": "user need with no validation tracing to it",
    "G3": "design input with no verification (directly or through a design output)",
    "G4": "hazard with no risk control",
    "G5": "risk control with no verification",
    "G6": "risk control not carried into any design input (check; may sit in labeling)",
    "G7": "design input with no design output (working convention; QS24)",
    "O1": "item with no upward link (orphan)",
    "O2": "link to an id not in the file",
    "O3": "link to an unexpected item type",
    "R1": "verification or validation recorded as fail",
    "R2": "verification or validation with no result recorded",
    "D1": "duplicate id",
    "T1": "unknown type",
}


def norm_type(value):
    return (value or "").strip().lower().replace(" ", "_").replace("-", "_")


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        cols = {c.strip().lower(): c for c in (reader.fieldnames or [])}
        for need in ("id", "type", "links"):
            if need not in cols:
                sys.exit(f"trace.csv needs an '{need}' column; found {reader.fieldnames}")
        rows = []
        for r in reader:
            get = lambda k: (r.get(cols[k]) or "").strip() if k in cols else ""
            rows.append({
                "id": get("id"),
                "type": norm_type(get("type")),
                "links": [x.strip() for x in get("links").replace(",", ";").split(";") if x.strip()],
                "text": get("text"),
                "result": get("result").lower(),
                "note": get("note"),
            })
    return rows


def check(rows):
    findings = []
    by_id = {}
    for r in rows:
        if not r["id"]:
            continue
        if r["id"] in by_id:
            findings.append((r["id"], "D1", "appears more than once"))
        by_id[r["id"]] = r
    children = defaultdict(list)  # parent id -> list of child rows
    for r in rows:
        if r["type"] not in TYPES:
            findings.append((r["id"], "T1", f"type '{r['type']}' is not one of {', '.join(TYPES)}"))
            continue
        if r["type"] not in ROOTS and not r["links"]:
            findings.append((r["id"], "O1", f"{r['type']} traces to nothing"))
        for target in r["links"]:
            parent = by_id.get(target)
            if parent is None:
                findings.append((r["id"], "O2", f"links to {target}, which is not in the file"))
                continue
            expected = EXPECTED_UP.get(r["type"], set())
            if parent["type"] not in expected:
                findings.append((r["id"], "O3", f"{r['type']} links to {target} ({parent['type']}); expected {', '.join(sorted(expected)) or 'no upward link'}"))
            children[target].append(r)

    def kinds(item_id):
        return {c["type"] for c in children.get(item_id, [])}

    for r in rows:
        t, i = r["type"], r["id"]
        if t == "user_need":
            if "design_input" not in kinds(i):
                findings.append((i, "G1", "no design input traces to this need"))
            if "validation" not in kinds(i):
                findings.append((i, "G2", "no validation traces to this need"))
        elif t == "design_input":
            verified = "verification" in kinds(i)
            if not verified:
                for out in (c for c in children.get(i, []) if c["type"] == "design_output"):
                    if "verification" in kinds(out["id"]):
                        verified = True
                        break
            if not verified:
                findings.append((i, "G3", "no verification traces to this input or its outputs"))
            if "design_output" not in kinds(i):
                findings.append((i, "G7", "no design output traces to this input (working convention)"))
        elif t == "hazard":
            if "risk_control" not in kinds(i):
                findings.append((i, "G4", "no risk control traces to this hazard"))
        elif t == "risk_control":
            if "verification" not in kinds(i):
                findings.append((i, "G5", "no verification traces to this control"))
            if "design_input" not in kinds(i):
                findings.append((i, "G6", "no design input carries this control"))
        if t in ("verification", "validation"):
            if r["result"] in ("fail", "failed"):
                findings.append((i, "R1", "result recorded as fail"))
            elif r["result"] in ("", "tbd", "open", "pending"):
                findings.append((i, "R2", "no result recorded"))
    return findings


def summary(rows, findings):
    count_types = defaultdict(int)
    for r in rows:
        count_types[r["type"]] += 1
    count_codes = defaultdict(int)
    for _, code, _ in findings:
        count_codes[code] += 1
    return dict(count_types), dict(count_codes)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("trace_csv")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--only", help="comma-separated finding codes to keep")
    a = ap.parse_args()
    rows = load(a.trace_csv)
    findings = check(rows)
    if a.only:
        keep = {c.strip().upper() for c in a.only.split(",")}
        findings = [f for f in findings if f[1] in keep]
    order = list(DESCRIPTIONS)
    findings.sort(key=lambda f: (order.index(f[1]), f[0]))
    types, codes = summary(rows, findings)
    if a.json:
        print(json.dumps({"items_by_type": types, "findings_by_code": codes,
                          "findings": [{"item": i, "code": c, "detail": d, "check": DESCRIPTIONS[c]} for i, c, d in findings]}, indent=1))
        return
    print(f"Items read: {len(rows)} ({', '.join(f'{k} {v}' for k, v in sorted(types.items()))})")
    print(f"Findings: {len(findings)}" + (f" ({', '.join(f'{k} {v}' for k, v in sorted(codes.items()))})" if codes else ""))
    print("Findings, not a score. Whether any finding blocks a release is the owner's decision.\n")
    if findings:
        print("| Item | Code | Detail | Check |")
        print("|---|---|---|---|")
        for i, c, d in findings:
            print(f"| {i} | {c} | {d} | {DESCRIPTIONS[c]} |")


if __name__ == "__main__":
    main()
