# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A DA, US, EU, UK, IM or TM row states it | The fact, the source name and date in plain words, then the row id ("Recalibration would be indicated in the case of calibration drift with event rate shift and stable discrimination (Davis et al. 2017, DOI 10.1093/jamia/ocx030, DA-92)") | None |
| Draft or proposal | FDA AI-enabled device software functions draft (January 2025); FDA request for comment FDA-2025-N-4203; IMDRF N93 | "The January 2025 draft recommends a postmarket performance monitoring plan (draft, DA-44)" | Never "required" |
| Voluntary framework | NIST AI RMF, GMLP | "NIST AI RMF 1.0, voluntary (DA-14)" | A checklist, never a duty |
| Law with a moved date | EU AI Act Articles 12, 15, 72 | "Applies from 2 August 2028 for AI in Annex I devices, as amended by Regulation (EU) 2026/1744 (DA-67)"; Article 72(3) template "by 2 September 2027 (DA-66)" | State the act that set the date |
| Summarized read | [WF] rows (DA-93, IM-04) | "Finlayson et al. 2021 [WF], DOI 10.1056/NEJMc2104626 (DA-93)" | Say the quote is close but not script-checked |
| Published method | [PAPER] rows | The row id and its DOI at first use; in a table, the DOI in the Rows cell | State the paper's own setting |
| Not in the sources | A drift, calibration, AUROC, missing-data, fairness or engagement threshold; a review cadence; an SMD or PSI cut-off; a "stable discrimination" margin | "Not in this skill's sources `[GAP]`" | The person, or the owner they name, supplies it; never fill it |

## Library facts

| Situation | How to word it |
|---|---|
| A recall record | "FUJIFILM Synapse PACS software v7.4.310, Class II recall, 22 July 2026 (library, retrieved 19 October 2026)"; no judgment of relevance |
| MAUDE counts | "10 MAUDE reports for product code QIH (2 in 2024, 5 in 2025, 3 in 2026); reports, not confirmed events; not attributable to one manufacturer" |
| No recall found | "No recall in the loaded sources for this search `[GAP]`; not evidence of safety; a recall filed under another entity name will not match" |
| Change log not started | "No change log for this scope (no watch registered); compared by dated rerun instead" |
| A tool with no saved output | "needs a live check" |

## The person's facts

| Situation | How to word it |
|---|---|
| No pass rule for records or for a personalization rule | "Pass rule not given `[GAP]`"; flags reported, nothing marked pass or fail |
| No thresholds file | "Thresholds not given"; values and changes reported, no flag raised |
| Thresholds or rules labeled proposed | "Not applied: proposed thresholds are never used to raise a flag" |
| Outcomes not yet known for some predictions | "N predictions without an outcome; the period's performance is read on outcomes known only" |
| No owner, action or recheck date for a miss | "Owner not named", "action not given", "recheck date not given"; ask |
| A date, data cut, threshold or status not given | "Not given"; ask. Never fill |
| A vendor or press claim about performance | "From you (vendor or press claim, not checked against a primary record)" |

## Never

- Never supply a threshold, tolerance, cut-off or cadence.
- Never call a model drifting, stable, safe, fair or fit for use; report the values against the person's thresholds.
- Never decide retrain, roll back or stop; never close a fired watch or failed element.
- Never decide whether an event is reportable.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words, with the row id after it: "Regulation (EU) 2024/1689, Article 72(2) (DA-65)". Never a row id alone. A [WF] row adds "[WF]"; a [PAPER] row adds its DOI at first use.

| Rows | Cite as |
|---|---|
| DA-01 to DA-16 | NIST AI 100-1, AI Risk Management Framework 1.0, January 2023 (voluntary) |
| DA-24 to DA-29 | WHO, Ethics and governance of AI for health, 28 June 2021 (publication page and news release) |
| DA-30 to DA-34 | WHO, Guidance on large multi-modal models (news release 18 January 2024; page dated 25 March 2025) |
| DA-35 to DA-46 | FDA, AI-Enabled Device Software Functions draft guidance, January 2025 (draft) |
| DA-47 to DA-50, DA-54 to DA-63, DA-65 | Regulation (EU) 2024/1689 (AI Act) |
| DA-51 to DA-53, DA-64, DA-66, DA-67 | Regulation (EU) 2026/1744 (Digital Omnibus on AI), 8 July 2026 |
| DA-87 to DA-90 | Sahiner et al. 2023, DOI 10.1259/bjr.20220878 |
| DA-91, DA-92 | Davis et al. 2017, DOI 10.1093/jamia/ocx030 |
| DA-93 | Finlayson et al. 2021, DOI 10.1056/NEJMc2104626 [WF] |
| DA-113 to DA-115 | Rajkomar et al. 2018, DOI 10.7326/M18-1990 |
| DA-116 to DA-120 | Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9 |
| US-01 to US-14, US-36 | FDA PCCP final guidance, 18 August 2025 |
| US-19 to US-22, US-37, US-38 | FDA AI lifecycle draft guidance, 7 January 2025 (draft); CDRH FY 2027 A-list |
| US-39 | FDA request for comment FDA-2025-N-4203 (not guidance) |
| UK-10 | GMLP guiding principle 10 (FDA, Health Canada, MHRA, 27 October 2021) |
| EU-05 | Regulation (EU) 2024/1689, Article 43(4) |
| EU-19 | Regulation (EU) 2026/1744 |
| EU-25, EU-32, EU-36 | MDCG 2025-6 FAQ, June 2025 (not legally binding) |
| EU-33 to EU-35 | Regulation (EU) 2024/1689 Article 72, as amended |
| TM79 to TM90 | Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8 |
| TM92, TM93 | Moore et al. 2015, DOI 10.1136/bmj.h1258 |
| Library facts | "library, retrieved 19 October 2026" plus the record title or number |
