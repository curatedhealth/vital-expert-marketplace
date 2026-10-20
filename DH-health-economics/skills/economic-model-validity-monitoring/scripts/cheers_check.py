#!/usr/bin/env python3
"""CHEERS 2022 completeness check and reference-case check on the person's model description.

What it does
  Reads a model description, methods section or report the person supplies (plain text or
  markdown) and, for each CHEERS 2022 item the research file sources, shows the lines that
  appear to address it, or "not found". Optionally (--body) it looks for the reference-case
  elements that body has written (references/reference-cases.md) and flags rule-currency
  issues (for example a retired EQ-5D value set for a new NICE topic).

What it never does
  It gives no score and no total: CHEERS has no validated scoring system and using it as a
  scoring tool is strongly discouraged (HE-005, DOI 10.1177/23814683211061097). A line found is a candidate for the person
  to confirm, not a pass. "Not found" means the person checks the document, not that the
  item is missing. Items whose wording is not in the research file are listed as [GAP].

Usage: python3 cheers_check.py description.md [--body NICE|HAS|IQWIG|ICER|ICER-PHTI] [--json]
"""
import argparse
import json
import re
import sys

# CHEERS 2022 items sourced in references/health-economics-methods-research.md (HE rows).
ITEMS = [
    (4, "Health economic analysis plan", "HE-006 (DOI 10.1177/23814683211061097)", "State whether a plan was developed and where it is available",
     [r"analysis plan", r"\bHEAP\b"]),
    (8, "Perspective", "HE-007 (DOI 10.1177/23814683211061097)", "State the perspective(s) and why chosen", [r"perspective"]),
    (9, "Time horizon", "HE-007 (DOI 10.1177/23814683211061097)", "State the time horizon and why appropriate", [r"time horizon", r"\bhorizon\b"]),
    (10, "Discount rate", "HE-007 (DOI 10.1177/23814683211061097)", "Report the discount rate(s) and reason chosen", [r"discount"]),
    (15, "Currency, price date and conversion", "HE-008 (DOI 10.1177/23814683211061097)",
     "Report dates of resource quantities and unit costs, the currency and the year of conversion",
     [r"currency", r"price year", r"cost year", r"inflat", r"conver", r"\b(GBP|EUR|USD)\b"]),
    (16, "Rationale and description of model", "HE-009 (DOI 10.1177/23814683211061097)",
     "Describe the model and why used; report whether and where it is publicly available",
     [r"model structure", r"decision tree", r"markov", r"state.transition", r"cohort model", r"publicly available",
      r"available on request", r"discrete event"]),
    (17, "Analytics and assumptions", "HE-010 (DOI 10.1177/23814683211061097)",
     "Describe analytic and extrapolation methods and approaches for validating the model",
     [r"extrapolat", r"validat", r"verif"]),
    (19, "Characterizing distributional effects", "HE-011 (DOI 10.1177/23814683211061097)",
     "Describe how impacts are distributed across individuals or adjustments for priority populations",
     [r"distributional", r"subgroup", r"equity", r"priority population", r"inequalit"]),
    (20, "Characterizing uncertainty", "HE-011 (DOI 10.1177/23814683211061097)", "Describe methods used to characterize uncertainty",
     [r"sensitivity", r"probabilistic", r"uncertaint", r"scenario"]),
    (21, "Approach to engagement", "HE-012 (DOI 10.1177/23814683211061097)",
     "Describe any approaches to engage patients, the public, communities or stakeholders in the design",
     [r"(patient|public|stakeholder|carer|clinician|payer)s?\b.*\b(engag|involv|consult|advis)",
      r"(engag|involv|consult)\w*\b.*\b(patient|public|stakeholder|carer|clinician|payer)"]),
    (24, "Effect of uncertainty", "HE-013 (DOI 10.1177/23814683211061097)",
     "Report how uncertainty affects findings, including the effect of discount rate and time horizon",
     [r"(discount|horizon).*(scenario|sensitivity)", r"(scenario|sensitivity).*(discount|horizon)"]),
    (25, "Effect of engagement", "HE-012 (DOI 10.1177/23814683211061097)", "Report what difference engagement made",
     [r"engag\w*.*(changed|influenc|differen|led to|shaped)"]),
    (27, "Source of funding", "HE-014 (DOI 10.1177/23814683211061097)", "Describe how the study was funded and the funder's role", [r"fund"]),
    (28, "Conflicts of interest", "HE-014 (DOI 10.1177/23814683211061097)", "Report authors' conflicts of interest",
     [r"conflicts? of interest", r"competing interest", r"declar\w* of interest"]),
]
SOURCED = {i[0] for i in ITEMS}
UNSOURCED = [n for n in range(1, 29) if n not in SOURCED]  # 28 items in total (HE-002, DOI 10.1177/23814683211061097)

# Reference-case elements per body: (element, rule as written, row, patterns, kind)
# kind "expect": the element should be stated; "flag": text that needs a check against the row.
BODIES = {
    "NICE": [
        ("Discount rate", "3.5% a year for costs and effects", "HE-047", [r"3\.5\s?%"], "expect"),
        ("Perspective on costs", "NHS and PSS", "HE-037", [r"\bNHS\b.*(PSS|personal social services)"], "expect"),
        ("Outcome measure", "QALYs; EQ-5D preferred in adults", "HE-043", [r"\bQALY", r"EQ-5D"], "expect"),
        ("UK 5L value set (new topics)", "UK 5L value set for all adult reference-case utilities (PMG51)", "HE-058",
         [r"Rowen", r"UK (EQ-5D-)?5L value set", r"UK value set"], "expect"),
        ("3L value set used", "New topics: map 3L to the UK 5L set; no 3L utilities in sensitivity or scenario analyses",
         "HE-060, HE-061", [r"\b3L\b", r"EQ-5D-3L", r"Dolan", r"van Hout", r"crosswalk"], "flag"),
        ("1.5% discount rate", "Non-reference-case 1.5% only if all three criteria are met", "HE-048",
         [r"1\.5\s?%"], "flag"),
        ("Time horizon", "Long enough to reflect all important differences in costs or outcomes", "HE-040", [r"\bhorizon\b"], "flag"),
        ("Default ranges", "Plus or minus 20 percent defaults are not the modeler's ranges; justify each range and run one-way analysis on net benefit", "tools.md (tornado pitfall)", [r"(plus or minus|\u00b1)\s?20\s?(%|percent)"], "flag"),
        ("Productivity costs", "Excluded from the reference case; may be shown separately", "HE-038",
         [r"productivity"], "flag"),
        ("Threshold stated", "PMG48 states GBP 20,000 and 20,000 to 30,000 (HE-074); PMG36 states 25,000 to 35,000 "
         "(HE-050, HE-051): open conflict; NICE uses no precise maximum (HE-049)", "HE-049, HE-050, HE-051, HE-074",
         [r"20,?000", r"25,?000", r"30,?000", r"35,?000", r"threshold"], "flag"),
        ("Verdict wording", "No precise maximum; acceptability is the committee's judgment", "HE-049",
         [r"\bis cost.effective\b", r"\bproves?\b", r"\bwill be cost.effective\b"], "flag"),
        ("Old manual title", "PMG36 is now 'NICE technology appraisal and highly specialised technologies guidance: the manual'",
         "HE-033", [r"health technology evaluations: the manual"], "flag"),
        ("Early value assessment name", "EVA is now early-use HealthTech guidance (PMG48 section 3)", "HE-067",
         [r"early value assessment", r"\bEVA\b"], "flag"),
    ],
    "HAS": [
        ("Perspective", "Collective; healthcare-system perspective must be justified", "HE-103", [r"collective"], "expect"),
        ("Discount rate", "2.5% for horizons under 30 years, falling to a 1.5% floor; discount when horizon exceeds 12 months",
         "HE-105", [r"2\.5\s?%"], "expect"),
        ("Value set", "EQ-5D-5L with the French value set in force", "HE-106", [r"French", r"Andrade"], "expect"),
    ],
    "IQWIG": [
        ("Perspective", "SHI-insured community", "HE-110", [r"\bSHI\b", r"statutory health insurance", r"GKV"], "expect"),
        ("Discount rate", "3% after year 1; sensitivity 0% and 5%, optionally 3% costs and 1.5% benefits", "HE-111",
         [r"\b3\s?%"], "expect"),
        ("Budget impact", "Mandatory, at least 3 years, without and with the product", "HE-112",
         [r"budget impact"], "expect"),
    ],
    "ICER": [
        ("Perspective", "Health care system base case; modified societal analysis", "HE-116",
         [r"health care system", r"healthcare system"], "expect"),
        ("Discount rate", "3% for costs and outcomes", "HE-117", [r"\b3\s?%"], "expect"),
        ("Utilities", "EQ-5D-5L preferred if available; lifetime horizon default", "HE-120", [r"5L", r"lifetime"], "expect"),
    ],
    "ICER-PHTI": [
        ("Primary measure", "Budget impact is the primary measure of comparative value", "HE-115, HE-121",
         [r"budget impact"], "expect"),
        ("Horizon", "1 year, with 2 to 5 year scenarios where offsets accrue later", "HE-122",
         [r"\b(one|1)[- ]year", r"12 months"], "expect"),
        ("Perspectives", "DHT user and payer or plan sponsor", "HE-123", [r"payer", r"plan sponsor", r"\buser"], "expect"),
    ],
}


def find(lines, patterns):
    hits = []
    for n, line in enumerate(lines, 1):
        for sentence in re.split(r"(?<=[.!?])\s+", line.strip()):
            if any(re.search(p, sentence, flags=re.IGNORECASE) for p in patterns):
                hits.append((n, sentence[:160]))
    return hits


def run(text, body=None):
    lines = text.splitlines()
    items = []
    for num, name, row, req, pats in ITEMS:
        hits = find(lines, pats)
        items.append({"item": num, "name": name, "row": row, "requirement": req,
                      "status": "text found: person confirms" if hits else "not found: person checks",
                      "lines": hits[:3]})
    out = {"cheers_items": items,
           "not_sourced": [{"item": n, "status": "[GAP] item wording not in the research file; check the CHEERS 2022 "
                            "checklist, DOI 10.1177/23814683211061097"} for n in UNSOURCED],
           "note": "No score or total is given (HE-005, DOI 10.1177/23814683211061097)."}
    if body:
        key = body.upper()
        if key not in BODIES:
            raise ValueError(f"unknown body {body}; use one of {', '.join(BODIES)}")
        rc = []
        for el, rule, row, pats, kind in BODIES[key]:
            hits = find(lines, pats)
            if kind == "expect":
                status = "stated: person confirms it matches" if hits else "not found: person checks"
            else:
                status = "check against the row" if hits else "no text found"
            rc.append({"element": el, "rule_as_written": rule, "row": row, "kind": kind, "status": status,
                       "lines": hits[:3]})
        out["reference_case"] = {"body": key, "checks": rc}
    return out


def to_markdown(r):
    L = ["# CHEERS 2022 completeness check (sourced items only, no score)", "",
         "| Item | Topic | Row | Status | Where (line: text) |", "|---|---|---|---|---|"]
    for i in r["cheers_items"]:
        where = "<br>".join(f"{n}: {t}" for n, t in i["lines"]) or ""
        L.append(f"| {i['item']} | {i['name']} | {i['row']} | {i['status']} | {where.replace('|', '/')} |")
    L.append("")
    L.append("Items " + ", ".join(str(x["item"]) for x in r["not_sourced"]) +
             ": [GAP] item wording not in the research file; check them against the CHEERS 2022 checklist "
             "(DOI 10.1177/23814683211061097).")
    if "reference_case" in r:
        L += ["", f"# Reference-case check: {r['reference_case']['body']}", "",
              "| Element | Rule as written | Row | Status | Where (line: text) |", "|---|---|---|---|---|"]
        for c in r["reference_case"]["checks"]:
            where = "<br>".join(f"{n}: {t}" for n, t in c["lines"]) or ""
            L.append(f"| {c['element']} | {c['rule_as_written']} | {c['row']} | {c['status']} | {where.replace('|', '/')} |")
    L += ["", "A line found is a candidate for the person to confirm; 'not found' means check the document. "
          "No score or total is given (HE-005, DOI 10.1177/23814683211061097)."]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("description")
    ap.add_argument("--body")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    with open(a.description, encoding="utf-8") as f:
        text = f.read()
    try:
        r = run(text, a.body)
    except ValueError as e:
        sys.exit(str(e))
    print(json.dumps(r, indent=1) if a.json else to_markdown(r))


if __name__ == "__main__":
    main()
