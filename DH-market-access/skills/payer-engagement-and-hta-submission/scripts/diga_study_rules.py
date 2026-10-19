#!/usr/bin/env python3
"""Check one study against the DiGA study rules (DiGAV sections 9 to 12, as amended 27 January 2026).

Input:
  --record  a JSON file holding a literature.get_record result. Accepts the bare record,
            the tool's {"record": {...}} envelope, or the saved examples/live/literature_verify_*.json
            (it takes the get_record call's result).
  --facts   optional JSON file with facts taken from the paper the person supplied:
            {"country": "DE", "transferability_case": false,
             "comparator": "waitlist|care_as_usual|none|listed_diga|active",
             "registry_id": "DRKS...", "completion_date": "2024-03-01", "publication_date": "2025-01-15",
             "usage_data_collected": true, "prospective": true, "risk_class": "I|IIa|IIb",
             "claim_type": "medical_benefit|psvv", "diagnostic_component": false,
             "diagnostic_accuracy_study": false, "icd_codes": ["F51"],
             "endpoints": [{"name": "ISI", "type": "patient_relevant|economic|staff_workload"}]}

Output: a Markdown table, one row per rule, with status shown / not shown / [GAP] / not applicable
and the row id in references/hta-submissions-sources.md. The script never judges sufficiency;
BfArM weighs the whole file (DE17).
"""
import argparse
import json
import sys
from datetime import date


def load_record(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if "calls" in data:
        for call in data["calls"]:
            if call.get("call") == "literature.get_record":
                return call["result"]
        sys.exit("No literature.get_record call in " + path)
    if "record" in data and isinstance(data["record"], dict):
        return data["record"]
    return data


def months_between(a, b):
    d1, d2 = date.fromisoformat(a), date.fromisoformat(b)
    return (d2.year - d1.year) * 12 + (d2.month - d1.month) + (d2.day - d1.day) / 31.0


def check(record, facts):
    rows = []
    design = record.get("design")
    excerpt = (record.get("excerpt") or "").lower()

    if record.get("retraction_status") not in (None, "none"):
        rows.append(("R0", "Record not retracted", "not shown",
                     "retraction_status is " + str(record.get("retraction_status")) + "; stop and tell the person", "literature record"))
        return rows

    # G1 comparative, quantitative, use better than non-use (DE10)
    if design in ("rct", "cohort", "case_control"):
        rows.append(("G1", "Comparative quantitative study, use better than non-use", "shown in part",
                     "design " + design + " (from metadata); the result direction is not in the record [GAP]: needs the results section", "DE10"))
    elif design is None:
        rows.append(("G1", "Comparative quantitative study, use better than non-use", "[GAP]", "no design in record", "DE10"))
    else:
        rows.append(("G1", "Comparative quantitative study, use better than non-use", "not shown",
                     "design " + design + " is not a comparative study of this product", "DE10"))

    # G2 comparator (DE11)
    comp = facts.get("comparator")
    if comp in ("waitlist", "care_as_usual", "none", "listed_diga"):
        rows.append(("G2", "Comparator: no treatment or treatment without a DiGA, real care", "shown", "comparator " + comp + " (person's paper)", "DE11"))
    elif comp == "active":
        rows.append(("G2", "Comparator: no treatment or treatment without a DiGA, real care", "not shown",
                     "active comparator only; use versus non-use not shown", "DE11"))
    else:
        hint = []
        if "wait" in excerpt:
            hint.append("excerpt mentions a waiting group")
        if "care-as-usual" in excerpt or "care as usual" in excerpt:
            hint.append("excerpt mentions care as usual")
        note = "; ".join(hint) + "; confirm in the methods section" if hint else "not in record"
        rows.append(("G2", "Comparator: no treatment or treatment without a DiGA, real care", "[GAP]", note, "DE11"))

    # G3 German setting or transferability (DE12, DE13)
    country = facts.get("country")
    if country is None:
        rows.append(("G3", "Run in Germany, or transferability shown", "[GAP]", "country of conduct not in record", "DE12, DE13"))
    elif country.upper() == "DE":
        rows.append(("G3", "Run in Germany, or transferability shown", "shown", "conducted in Germany (person's paper)", "DE12"))
    elif facts.get("transferability_case"):
        rows.append(("G3", "Run in Germany, or transferability shown", "shown", "conducted in " + country + "; transferability case supplied", "DE12, DE13"))
    else:
        rows.append(("G3", "Run in Germany, or transferability shown", "not shown",
                     "conducted in " + country + "; no transferability case (guidelines, access, questionnaire language versions)", "DE12, DE13"))

    # G4a registration (DE14)
    reg = record.get("trial_ids") or ([facts["registry_id"]] if facts.get("registry_id") else [])
    if reg:
        rows.append(("G4a", "Registered in a WHO ICTRP primary or partner registry", "shown", ", ".join(reg) + "; confirm the registry is ICTRP primary or partner", "DE14"))
    else:
        rows.append(("G4a", "Registered in a WHO ICTRP primary or partner registry", "[GAP]", "trial_ids empty in the library record; ask for the registry entry", "DE14"))

    # G4b publication within 12 months of completion (DE14)
    if facts.get("completion_date") and facts.get("publication_date"):
        m = months_between(facts["completion_date"], facts["publication_date"])
        status = "shown" if m <= 12 else "not shown"
        rows.append(("G4b", "Published in full within 12 months of completion", status, "%.1f months from completion to publication" % m, "DE14"))
    else:
        rows.append(("G4b", "Published in full within 12 months of completion", "[GAP]",
                     "completion date not in record" + ("; published " + str(record.get("year")) if record.get("year") else ""), "DE14"))

    # G5 usage data (DE15)
    u = facts.get("usage_data_collected")
    if u is True:
        rows.append(("G5", "Duration and frequency of use collected", "shown", "person's paper", "DE15"))
    elif u is False:
        rows.append(("G5", "Duration and frequency of use collected", "not shown",
                     "rule in force since 1 February 2026; check with the accountable owner whether it applies to this study", "DE15, DE1"))
    else:
        rows.append(("G5", "Duration and frequency of use collected", "[GAP]", "not in record", "DE15"))

    # G6 prospective where required; diagnostic accuracy (DE16)
    rc, ct = facts.get("risk_class"), facts.get("claim_type")
    if rc == "IIb" and ct == "medical_benefit":
        if facts.get("prospective") or design == "rct":
            rows.append(("G6", "Prospective comparative study (class IIb, medical benefit)", "shown", "prospective design", "DE16"))
        else:
            rows.append(("G6", "Prospective comparative study (class IIb, medical benefit)", "not shown", "no prospective design", "DE16"))
    elif rc is None:
        rows.append(("G6", "Prospective study where required", "[GAP]", "device class not given; it decides whether a prospective study is mandatory", "DE16"))
    elif facts.get("prospective") or design == "rct":
        rows.append(("G6", "Prospective study where required", "shown",
                     "prospective design; class " + rc, "DE16"))
    else:
        rows.append(("G6", "Prospective study where required", "not applicable",
                     "class " + rc + "; prospective still required if no suitable retrospective data exist", "DE16"))
    if facts.get("diagnostic_component"):
        st = "shown" if facts.get("diagnostic_accuracy_study") else "not shown"
        rows.append(("G6d", "Sensitivity and specificity study for the diagnostic component", st, "", "DE16"))

    # G7 ICD-10-GM codes (DE9)
    icd = facts.get("icd_codes")
    rows.append(("G7", "Patient group as ICD-10-GM codes", "shown" if icd else "[GAP]", ", ".join(icd) if icd else "not given", "DE9"))

    # DE8 endpoint admissibility
    for ep in facts.get("endpoints", []):
        if ep.get("type") in ("economic", "staff_workload"):
            rows.append(("E", "Endpoint admissible for a positive care effect", "not shown",
                         ep.get("name", "?") + " is " + ep["type"] + ": excluded for both effect types", "DE8"))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--record", required=True)
    ap.add_argument("--facts")
    args = ap.parse_args()
    record = load_record(args.record)
    facts = {}
    if args.facts:
        with open(args.facts, encoding="utf-8") as fh:
            facts = json.load(fh)
    rows = check(record, facts)
    print("Study: %s (DOI %s, PMID %s)" % (record.get("title"), record.get("doi"), record.get("pmid")))
    print()
    print("| Rule | Requirement | Status | Basis | Row |")
    print("|---|---|---|---|---|")
    for r in rows:
        print("| %s | %s | %s | %s | %s |" % r)
    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    print()
    print("Counts: " + ", ".join("%s %d" % (k, v) for k, v in sorted(counts.items())))
    print("BfArM weighs the whole file and may depart from these rules (DE17). Sufficiency is the person's and BfArM's judgment, not this script's.")


if __name__ == "__main__":
    main()
