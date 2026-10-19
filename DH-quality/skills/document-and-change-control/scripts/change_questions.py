#!/usr/bin/env python3
"""Change questions: walk a software change through the questions of each framework that
applies, record the person's answer and basis for each, and print a question sheet with the
source row behind every question.

The sheet never decides. For each answer it states what the source says that answer points
to, in the source's own hedged words ("likely required", "likely not required"), and it lists
open questions. The conclusion belongs to the person's regulatory owner.

Frameworks (keys)
  fda_sw     FDA, Deciding When to Submit a 510(k) for a Software Change (25 October 2017)
  pccp       FDA PCCP final guidance (reissued 18 August 2025) and section 515C
  mdcg       MDCG 2020-3 Rev.1, legacy devices under Article 120 MDR
  mdr_cert   MDR Annex IX 4.10 and 2.4, and MDCG 2025-6 on pre-determined AI changes
  field      Corrections and removals (21 CFR 806) and EU field safety corrective actions

Row ids refer to references/QUALITY_SYSTEMS.md (QS, EU, VG, CH), references/AI_ML_REGULATION.md
(AI US-, AI EU-) and references/supplementary-rows.md (QX).

Usage
  python3 change_questions.py --list fda_sw,pccp            print the questions only
  python3 change_questions.py answers.json [--json]         build the sheet from answers
  python3 change_questions.py --interactive fda_sw,mdcg     ask in the terminal, then print

answers.json
  {"change_id": "CR-0142", "device": "...", "description": "...",
   "frameworks": ["fda_sw", "pccp"],
   "answers": {"Q1": {"answer": "no", "basis": "risk file RMF-7 rev 4, item H-12"}, ...}}
  answer is "yes", "no" or "unknown". A missing question is "not answered [GAP]".
"""
import argparse
import json
import sys

Q = {
    "fda_sw": {
        "title": "FDA software-change questions (final guidance, 25 October 2017; predates the QMSR, CH10)",
        "scope": "510(k)-cleared device or De Novo baseline; not PMA or 510(k)-exempt devices (QX10, QX33)",
        "questions": [
            ("PRE0", "Is the change made with the intent to significantly affect safety or effectiveness (e.g. to significantly improve clinical outcomes or mitigate a known risk)?", "QX35", {"yes": "The guidance says a new 510(k) is likely required regardless of the questions (QX35)."}),
            ("PRE1", "Has a risk-based assessment of whether the change could significantly affect safety or effectiveness been done?", "CH11",
             {"no": "The guidance starts with this assessment (CH11). Do it before answering the questions."}),
            ("PRE2", "Have unintended consequences of the change been considered, not only the intended effect?", "QX21",
             {"no": "The guidance asks for this (QX21)."}),
            ("PRE3", "Is the comparison made against the most recently cleared device (give its K or DEN number)?", "QX18, QX33",
             {"no": "The comparison baseline is the most recently cleared device (QX18, QX33)."}),
            ("PRE4", "Has this change been assessed on its own and together with the other changes made since that clearance?", "QX12, QX13",
             {"no": "Assess each change separately and in aggregate; cumulative changes can cross the threshold (QX12, QX13)."}),
            ("Q1", "Is the change made solely to strengthen cybersecurity, with no other impact on the software or device?", "CH12",
             {"yes": "Source: in many cases a change made solely to strengthen cybersecurity is not likely to require a new 510(k) (CH12).",
              "no": "Go on to Q2."}),
            ("Q2", "Is the change made solely to return the system to the specification of the most recently cleared device?", "CH13",
             {"yes": "Source: a new 510(k) is likely not required; the impact must still be evaluated (CH13).",
              "no": "Go on to Q3a."}),
            ("Q3a1", "Does the change create a new, or modify an existing, hazard, hazardous situation or cause in the risk management file?", "CH14", {}),
            ("Q3a2", "Is the harm of that hazard, situation or cause serious or worse, judged on the pre-mitigation risk score?", "CH14, QX19", {}),
            ("Q3a3", "Is it not already effectively mitigated in the most recently cleared device?", "QX18", {}),
            ("Q3b", "Does the change create or need a new or modified risk control for a hazardous situation that could result in significant harm?", "CH15",
             {"yes": "Source: a new 510(k) is likely required (CH15).", "no": "Go on to Q4."}),
            ("Q4", "Could the change significantly affect clinical functionality or performance specifications directly associated with the intended use?", "CH16, QX17",
             {"yes": "Source: a new 510(k) is likely required (CH16).",
              "no": "No question in the guidance points to a new 510(k) on this answer set; the guidance asks to document the basis (QX14)."}),
            ("POST1", "Did verification or validation produce any unexpected result?", "QX15, QX16",
             {"yes": "Source: reconsider any no-submission conclusion and go through the questions again (QX15).",
              "no": "Passing V&V does not override a finding that the change could significantly affect safety or effectiveness (QX16)."}),
        ],
    },
    "pccp": {
        "title": "FDA PCCP (final guidance reissued 18 August 2025, AI US-01) and section 515C",
        "scope": "AI-enabled devices through 510(k), De Novo or PMA (AI US-02)",
        "questions": [
            ("P1", "Was a PCCP authorized with this device's marketing authorization?", "AI US-10",
             {"no": "No PCCP applies; walk the FDA software-change questions or the PMA route."}),
            ("P2", "Is this modification specified in the PCCP's Description of Modifications?", "AI US-04", {"no": "Outside the PCCP."}),
            ("P3", "Was it implemented and verified per the Modification Protocol, meeting its acceptance criteria?", "AI US-05, AI US-12", {"no": "Outside the PCCP."}),
            ("P4", "Does the device stay within its intended use?", "AI US-08", {"no": "Outside the PCCP: modifications in a PCCP must maintain the intended use (AI US-08)."}),
            ("P5", "Is there any deviation from the authorized PCCP?", "AI US-13",
             {"yes": "Source: deviations would generally cause the device to be adulterated and misbranded (AI US-13)."}),
        ],
    },
    "mdcg": {
        "title": "MDCG 2020-3 Rev.1 (May 2023), legacy devices, Article 120(3c)(b) MDR",
        "scope": "Legacy MDD or AIMDD devices only (CH1, CH3)",
        "questions": [
            ("M0", "Is the device a legacy device placed on the market under an MDD or AIMDD certificate or declaration (Article 120)?", "CH1, CH3",
             {"no": "MDCG 2020-3 does not apply; for MDR-certified devices see mdr_cert."}),
            ("M1", "Is the change related to a corrective action assessed and accepted by the competent authority?", "QX24", {}),
            ("MA", "Does the change alter the intended purpose?", "QX24",
             {"yes": "Chart A applies; its questions are not quoted in the references [GAP]. Read Chart A in MDCG 2020-3."}),
            ("MB", "Is it a major software change that alters the built-in control mechanism or operating principle?", "CH5",
             {"yes": "Source: such changes are evaluated per Chart B (CH5); its questions are not quoted in the references [GAP]."}),
            ("C1", "New or major change of operating system or any component?", "QX23, QX25, QX26",
             {"yes": "Body text: significant if the device software must be modified (QX26); third-party OS updates are listed as non-significant (QX25). Say which applies."}),
            ("C2", "New or modified architecture or database structure, or a change of an algorithm?", "QX23, CH8, QX38",
             {"yes": "Body text lists new architecture and an algorithm change that impacts operating principles or control and may alter diagnosis or therapy among significant examples (CH8); an algorithm change without alteration of diagnosis or treatment is listed as non-significant (QX38)."}),
            ("C3", "Required user input replaced by a closed loop algorithm?", "QX23, CH8",
             {"yes": "Body text lists this among significant examples (CH8)."}),
            ("C4", "New user interface, medical feature, channel of interoperability or presentation of data?", "QX23, CH8, QX27",
             {"yes": "Body text lists new medical features, new interoperability channels and changes in how data is read such that treatment may be altered among significant examples (CH8, QX27); UI appearance without new functions is non-significant (QX25)."}),
            ("C5", "Does the change negatively affect the benefit-risk ratio of the device?", "QX23, CH7",
             {"yes": "Source: the non-significant examples hold only if the benefit-risk ratio is not negatively affected (CH7)."}),
            ("M9", "Is the justification documented and available to a competent authority on request?", "QX22",
             {"no": "The guidance asks for this (QX22)."}),
        ],
    },
    "mdr_cert": {
        "title": "MDR certified devices: Annex IX 4.10 and 2.4; MDCG 2025-6 on pre-determined AI changes",
        "scope": "Devices under an MDR certificate issued by a notified body",
        "questions": [
            ("X1", "Is the device covered by an EU technical documentation assessment certificate?", "QX30", {"no": "Annex IX 4.10 does not apply; check Annex X 5.2 if under type examination (QX32)."}),
            ("X2", "Could the change affect the safety and performance of the device or the conditions prescribed for use?", "QX30, QX31",
             {"yes": "Source: changes of this kind require approval of the notified body that issued the certificate; the manufacturer informs it of the plan; the notified body decides between a new conformity assessment and a supplement (QX30, QX31)."}),
            ("X3", "Is it a substantial change to the QMS or to the device range covered?", "EU24",
             {"yes": "Source: plans go to the notified body that approved the QMS (EU24)."}),
            ("X4", "For an AI-enabled device: was this change pre-determined and assessed at the initial conformity assessment, and documented under AI Act Annex IV point 2(f)?", "AI EU-30, AI EU-05",
             {"yes": "Source: such changes are not a substantial modification and not a change under Annex IX 4.10 (AI EU-30)."}),
        ],
    },
    "field": {
        "title": "Changes applied to devices already in use: corrections, removals, FSCA",
        "scope": "US 21 CFR 806; EU MDR Article 2(68) and 87",
        "questions": [
            ("F1", "Will the change be applied to devices already in use (for example a pushed software update)?", "VG25",
             {"yes": "A correction includes modification or adjustment without physical removal (VG25)."}),
            ("F2", "US: is it made to reduce a risk to health, or to remedy a violation that may present a risk to health?", "VG22, VG23",
             {"yes": "Source: report within 10 working days of initiating the correction (VG22).",
              "no": "Source: improvements that do not reduce a risk to health are exempt from reporting (VG23); a record with a justification reviewed by a designated person is still kept (VG24)."}),
            ("F3", "EU: is it taken for technical or medical reasons to prevent or reduce the risk of a serious incident?", "VG3, VG8",
             {"yes": "Source: that is a field safety corrective action; except in urgency it is reported before it is undertaken (VG3, VG8)."}),
        ],
    },
}


def norm(a):
    a = (a or "").strip().lower()
    return a if a in ("yes", "no", "unknown") else ""


def indicators(fw, ans):
    """Return the sentences the source associates with the answer set, without deciding."""
    out = []
    if fw == "fda_sw":
        a3 = [norm(ans.get(k, {}).get("answer")) for k in ("Q3a1", "Q3a2", "Q3a3")]
        if a3 == ["yes", "yes", "yes"]:
            out.append("Q3a: all three criteria answered yes. Source: a new 510(k) is likely required (CH14).")
        elif "" in a3 or "unknown" in a3:
            out.append("Q3a: not all three criteria answered; Q3a cannot be read.")
    if fw == "pccp":
        p = {k: norm(ans.get(k, {}).get("answer")) for k in ("P1", "P2", "P3", "P4", "P5")}
        if p["P1"] == p["P2"] == p["P3"] == p["P4"] == "yes" and p["P5"] == "no":
            out.append("P1 to P5: source says no new marketing submission is necessary; document the modification and analysis in the quality system (AI US-12).")
    return out


GATES = {"pccp": ("P1", "no"), "mdcg": ("M0", "no"), "mdr_cert": ("X1", "no")}


def build(data):
    ans = data.get("answers", {})
    sheet = {"change_id": data.get("change_id", "[GAP]"), "device": data.get("device", "[GAP]"),
             "description": data.get("description", "[GAP]"), "frameworks": [], "open": []}
    for fw in data.get("frameworks", []):
        if fw not in Q:
            sheet["frameworks"].append({"key": fw, "error": "unknown framework"})
            continue
        rows = []
        gate = GATES.get(fw)
        gated = bool(gate) and norm(ans.get(gate[0], {}).get("answer")) == gate[1]
        for qid, text, src, points in Q[fw]["questions"]:
            a = ans.get(qid, {})
            av = norm(a.get("answer"))
            basis = (a.get("basis") or "").strip()
            if gated and qid != gate[0] and not av:
                rows.append({"id": qid, "question": text, "source": src,
                             "answer": f"not applicable ({gate[0]} answered {gate[1]})",
                             "basis": "", "source_says": ""})
                continue
            if not av:
                av_txt = "not answered [GAP]"
                sheet["open"].append(f"{fw}:{qid}")
            elif av == "unknown":
                av_txt = "unknown"
                sheet["open"].append(f"{fw}:{qid}")
            else:
                av_txt = av
            rows.append({"id": qid, "question": text, "source": src, "answer": av_txt,
                         "basis": basis or ("basis not given" if av in ("yes", "no") else ""),
                         "source_says": points.get(av, "")})
        sheet["frameworks"].append({"key": fw, "title": Q[fw]["title"], "scope": Q[fw]["scope"],
                                    "rows": rows, "indicators": indicators(fw, ans)})
    return sheet


def to_md(s):
    L = [f"# Change question sheet: {s['change_id']}", "",
         f"Device: {s['device']}", f"Change: {s['description']}", ""]
    for f in s["frameworks"]:
        if "error" in f:
            L += [f"## {f['key']}: {f['error']}", ""]
            continue
        L += [f"## {f['title']}", f"Scope: {f['scope']}", "",
              "| # | Question | Answer | Basis given | What the source says about this answer | Row |",
              "|---|---|---|---|---|---|"]
        for r in f["rows"]:
            L.append(f"| {r['id']} | {r['question']} | {r['answer']} | {r['basis']} | {r['source_says']} | {r['source']} |")
        if f["indicators"]:
            L += [""] + [f"- {i}" for i in f["indicators"]]
        L.append("")
    L.append("Open questions: " + (", ".join(s["open"]) if s["open"] else "none"))
    L += ["", "Decision: for the owner. This sheet records answers and what the sources say; it does not decide whether a submission, notification or approval is needed."]
    return "\n".join(L)


def interactive(fws):
    data = {"change_id": input("Change id: "), "device": input("Device and authorization: "),
            "description": input("Change, in one or two sentences: "), "frameworks": fws, "answers": {}}
    for fw in fws:
        print(f"\n{Q[fw]['title']}\nScope: {Q[fw]['scope']}")
        for qid, text, src, _ in Q[fw]["questions"]:
            a = input(f"{qid} {text} [{src}] (yes/no/unknown/blank): ")
            b = input("   basis (document, version, test report): ") if a.strip() else ""
            data["answers"][qid] = {"answer": a, "basis": b}
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("answers", nargs="?")
    ap.add_argument("--list")
    ap.add_argument("--interactive")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.list:
        for fw in a.list.split(","):
            print(f"\n{Q[fw]['title']}\nScope: {Q[fw]['scope']}")
            for qid, text, src, _ in Q[fw]["questions"]:
                print(f"  {qid}  {text}  [{src}]")
        return
    if a.interactive:
        data = interactive(a.interactive.split(","))
    elif a.answers:
        data = json.load(open(a.answers))
    else:
        ap.error("give answers.json, --list or --interactive")
    s = build(data)
    print(json.dumps(s, indent=1) if a.json else to_md(s))


if __name__ == "__main__":
    sys.exit(main())
