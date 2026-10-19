#!/usr/bin/env python3
"""AI Act dates for a medical device: which obligations apply, from when, set by which act.

Two inputs:
  1. One device from the person's facts:
       --class IIa --ai-system yes --reference-date 2026-10-19 [--placed-on-market 2025-03-01]
  2. Saved library rows (regulatory-dh.search_devices, EU rows carry risk_class "Class IIa"):
       --rows rows.json [--ai-system unknown]
     Library rows never say whether a device is an AI system, so the AI-system answer
     comes from the person (default "unknown", which keeps every high-risk line conditional).

Rules (rows in references/AI_ML_REGULATION.md, read 19 October 2026):
  - High-risk under Article 6(1) follows the MDR/IVDR class (MDCG 2025-6 Table 1) [AI EU-27, EU-28].
  - Chapter III Sections 1 to 3 apply to Annex I systems from 2 August 2028
    (Regulation (EU) 2026/1744; was 2 August 2027) [AI EU-19, EU-14].
  - AI literacy since 2 February 2025, wording amended by 2026/1744 [AI EU-15, EU-20].
  - Prohibited practices since 2 February 2025; new points from 2 December 2026 [AI EU-16, EU-21].
  - Systems placed on the market before the Chapter III date are caught only on
    significant design changes [AI EU-22].
  - Article 72 timing for Annex I systems is unsettled [GAP]; template guidance due by
    2 September 2027 [AI EU-35].
The script restates these rows. It does not decide the class or whether the software is
an AI system; those are the person's.

Usage: python3 ai_act_dates.py --class IIa --ai-system yes [--reference-date YYYY-MM-DD]
       python3 ai_act_dates.py --rows rows.json [--ai-system unknown] [--json]
"""
import argparse
import datetime as dt
import json
import sys

OMNIBUS = "Regulation (EU) 2026/1744"
AIA = "Regulation (EU) 2024/1689"
HIGH_RISK_DATE = dt.date(2028, 8, 2)

# MDCG 2025-6 Table 1 (non-exhaustive) [AI EU-27]. True = high-risk if an AI system.
TABLE1 = {
    "I": False, "IS": True, "IM": True, "IR": True, "IIA": True, "IIB": True, "III": True,
    "ANNEXXVI": True, "A": False, "A-STERILE": True, "B": True, "C": True, "D": True,
    "IN-HOUSE": False,
}


def norm_class(raw):
    if raw is None:
        return None
    c = str(raw).upper().replace("CLASS", "").replace(" ", "")
    return c if c in TABLE1 else None


def status(date, ref):
    return "in force" if ref >= date else f"from {date.isoformat()}"


def assess(cls_raw, ai_system, ref, placed=None):
    cls = norm_class(cls_raw)
    out = {"class_input": cls_raw, "ai_system": ai_system, "reference_date": ref.isoformat(), "lines": []}
    add = lambda o, d, a, r: out["lines"].append({"obligation": o, "date_or_status": d, "set_by": a, "row": r})
    if cls is None:
        out["high_risk"] = "[GAP] class not recognized; MDCG 2025-6 Table 1 is non-exhaustive"
    else:
        hr = TABLE1[cls]
        if not hr:
            out["high_risk"] = "not high-risk under MDCG 2025-6 Table 1 (no notified body for this class)"
            if cls == "I":
                out["high_risk"] += "; if the device is sterile, measuring or reusable surgical (Is, Im, Ir) it is high-risk; a library row does not say [GAP]"
        elif ai_system == "no":
            out["high_risk"] = "not an AI system on the person's determination: AI Act high-risk rules do not apply"
        elif ai_system == "yes":
            out["high_risk"] = "high-risk under Article 6(1) per MDCG 2025-6 Table 1 (guidance, not binding)"
        else:
            out["high_risk"] = "high-risk only if the software is an AI system (person to determine)"
    if ai_system != "no":
        cond = "" if ai_system == "yes" else " (if an AI system)"
        add("AI literacy: take measures to support staff AI literacy, no guaranteed level" + cond,
            status(dt.date(2025, 2, 2), ref), f"{AIA}, Article 4 as amended by {OMNIBUS}", "AI EU-15, EU-20")
        add("Prohibited practices (Article 5)" + cond, status(dt.date(2025, 2, 2), ref), AIA, "AI EU-16")
        add("New prohibited points (ba), (bb), (1a), (1b)" + cond, status(dt.date(2026, 12, 2), ref), OMNIBUS, "AI EU-21")
    if cls is not None and TABLE1[cls] and ai_system != "no":
        cond = "" if ai_system == "yes" else " (if an AI system)"
        add("High-risk requirements, Chapter III Sections 1 to 3 (Annex I, MDR/IVDR)" + cond,
            status(HIGH_RISK_DATE, ref), f"{OMNIBUS} (was 2 August 2027 in {AIA}; MDCG 2025-6 still shows 2027)", "AI EU-19, EU-14, EU-32")
        if placed is not None:
            if placed < HIGH_RISK_DATE:
                add("Placed on the market before the Chapter III date: caught only on significant design changes from that date",
                    "applies to this device", AIA + " as amended", "AI EU-22")
            else:
                add("Placed on the market on or after the Chapter III date: requirements apply at placing", "applies to this device", OMNIBUS, "AI EU-19")
        add("Post-market monitoring (Article 72) for Annex I systems" + cond,
            "[GAP] timing unsettled; needs a legal read", AIA + " / " + OMNIBUS, "Not sourced")
        add("Commission guidance with post-market monitoring plan template", "due by 2027-09-02", OMNIBUS, "AI EU-35")
    return out


def rows_from(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    rows = data if isinstance(data, list) else data.get("results", [])
    return [r for r in rows if r.get("jurisdiction") == "EU"]


def print_one(o, title=None):
    if title:
        print(f"## {title}")
    print(f"Class: {o['class_input']} | AI system: {o['ai_system']} | Reference date: {o['reference_date']}")
    print(f"AI Act status: {o['high_risk']}")
    if o["lines"]:
        print("| Obligation | Date or status | Set by | Row |")
        print("|---|---|---|---|")
        for l in o["lines"]:
            print(f"| {l['obligation']} | {l['date_or_status']} | {l['set_by']} | {l['row']} |")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--class", dest="cls")
    ap.add_argument("--rows")
    ap.add_argument("--ai-system", choices=["yes", "no", "unknown"], default="unknown")
    ap.add_argument("--reference-date", default=dt.date.today().isoformat())
    ap.add_argument("--placed-on-market")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    ref = dt.date.fromisoformat(a.reference_date)
    placed = dt.date.fromisoformat(a.placed_on_market) if a.placed_on_market else None
    if a.rows:
        results = []
        for r in rows_from(a.rows):
            o = assess(r.get("risk_class"), a.ai_system, ref)
            o["device"] = f"{r.get('product')} ({r.get('manufacturer')}), status '{r.get('status')}'"
            results.append(o)
        if not results:
            sys.exit("No EU rows in the file.")
    elif a.cls:
        results = [assess(a.cls, a.ai_system, ref, placed)]
    else:
        sys.exit("Give --class or --rows.")
    if a.json:
        print(json.dumps(results, indent=1))
        return
    for o in results:
        print_one(o, o.get("device"))
    print("Class and AI-system status are the person's determinations. Rows: references/AI_ML_REGULATION.md.")


if __name__ == "__main__":
    main()
