#!/usr/bin/env python3
"""Comparable-trial endpoint table from ClinicalTrials.gov records.

Input: one or more study records saved from the ClinicalTrials.gov API v2
(https://clinicaltrials.gov/api/v2/studies/<NCT id>), as JSON files.
Output: a markdown table per trial (design, enrollment, registration dates,
primary and secondary outcomes) and, per primary outcome, which of the four
outcome elements of SPIRIT 2025 item 16 (SP-16) the registered wording shows.

The element check looks for words only. A "not seen" means the words were not
found in the registry text, not that the trial lacks the element. Read the
registry record and the protocol before relying on it.

Usage: python3 registry_endpoints.py FILE.json [FILE.json ...]
"""
import json, re, sys

METRIC = [r"\bchange\b", r"\btime to\b", r"\bfinal\b", r"\bfrom baseline\b", r"\bonset\b", r"\bremission\b", r"\bresponse\b"]
AGGREG = [r"\bnumber of\b", r"\bpercentage\b", r"\bproportion\b", r"\bmean\b", r"\bmedian\b", r"\brate\b", r"\bhazard\b"]

def found(pats, text):
    hits = [p.strip(r"\b").replace("\\b", "") for p in pats if re.search(p, text, re.I)]
    return ", ".join(hits) if hits else "not seen"

def load(path):
    d = json.load(open(path))
    p = d.get("protocolSection", {})
    return d, p

def row(path):
    d, p = load(path)
    ident = p.get("identificationModule", {})
    st = p.get("statusModule", {})
    des = p.get("designModule", {})
    info = des.get("designInfo", {})
    mask = info.get("maskingInfo", {})
    enr = des.get("enrollmentInfo", {})
    out = p.get("outcomesModule", {})
    lines = []
    nct = ident.get("nctId", "[GAP]")
    lines.append(f"### {nct}: {ident.get('briefTitle', '[GAP]')}")
    lines.append("")
    lines.append("| Field | Registry value |")
    lines.append("|---|---|")
    lines.append(f"| Design | {info.get('allocation','[GAP]')}, {info.get('interventionModel','[GAP]')}, purpose {info.get('primaryPurpose','[GAP]')} |")
    who = ", ".join(mask.get("whoMasked", [])) or "none stated"
    lines.append(f"| Masking | {mask.get('masking','[GAP]')} ({who}) |")
    lines.append(f"| Enrollment | {enr.get('count','[GAP]')} ({enr.get('type','[GAP]')}) |")
    lines.append(f"| First submitted to registry | {st.get('studyFirstSubmitDate','[GAP]')} |")
    lines.append(f"| Start date | {st.get('startDateStruct',{}).get('date','[GAP]')} ({st.get('startDateStruct',{}).get('type','')}) |")
    lines.append(f"| Status | {st.get('overallStatus','[GAP]')}; results posted: {'yes' if d.get('hasResults') else 'no'} |")
    lines.append("")
    prim = out.get("primaryOutcomes", [])
    lines.append("| Primary outcome (registry wording) | Time frame | Metric words | Aggregation words |")
    lines.append("|---|---|---|---|")
    for o in prim:
        txt = (o.get("measure","") + " " + o.get("description","")).replace("|", "/")
        lines.append(f"| {o.get('measure','[GAP]')} | {o.get('timeFrame','not seen')} | {found(METRIC, txt)} | {found(AGGREG, txt)} |")
    if not prim:
        lines.append("| [GAP] no primary outcome in the record | | | |")
    sec = out.get("secondaryOutcomes", [])
    lines.append("")
    lines.append(f"Secondary outcomes registered: {len(sec)}" + ("" if not sec else ": " + "; ".join(o.get("measure","") for o in sec)))
    lines.append("")
    return "\n".join(lines)

def main(paths):
    if not paths:
        print(__doc__); sys.exit(1)
    print("Source: ClinicalTrials.gov API v2 records as saved. Element words are a reading aid for SP-16 ([PAPER] SPIRIT 2025 DOI 10.1136/bmj-2024-081477), not a judgment.\n")
    for p in paths:
        print(row(p))

if __name__ == "__main__":
    main(sys.argv[1:])
