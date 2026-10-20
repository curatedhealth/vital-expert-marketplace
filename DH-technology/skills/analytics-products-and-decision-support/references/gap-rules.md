# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A DA, UX, PE, CS or EN row states it | The fact, the source name and date in plain words, then the row id ("Software for a critical, time-sensitive task does not meet Criterion 4 (FDA CDS guidance, 29 January 2026, UX-US-66)") | None |
| Guidance used as a checklist | CMS measure specification rows applied to an internal metric; ONC predictive DSI attributes outside certification; NICE ESF outside the NHS | "CMS quality-measure guidance, used here as a checklist (DA-134)" | Never presented as a rule the organization must follow |
| Draft or proposal | FDA AI-enabled device software functions draft (DA-35); ONC HTI-5 proposal (UX-US-60, UX-US-63); HIPAA Security Rule NPRM (EN-106, EN-107) | "A January 2025 draft, not for implementation (DA-35)"; "proposed 29 December 2025, not final (UX-US-60)" | Never as a requirement |
| Dated version | USCDI published versus required for certification; AI Act dates as amended; CDS guidance superseded issue | "USCDI v7 published 23 July 2026 (DA-108); certification adopts v1 (expired 1 January 2026) and v3 (DA-111)" | State both |
| Published method | The row is [PAPER] | The row id and its DOI at first use | State the paper's own population and method |
| Specification | The row is [SPEC] (OMOP) | "OHDSI documentation, read 20 October 2026 (DA-103 [SPEC])" | None |
| Summarized read | The row is [WF] (DA-22, DA-23, DA-93) | "ISO/IEC 42001 public page (DA-22) [WF]" | Say the quote is close but not script-checked |
| Not in the sources | Targets, thresholds or tolerances for metrics, dashboards, adoption or value; value benchmarks or typical savings; official dashboard or KPI governance; ISO/IEC 42001 clause text | "Not in this skill's sources `[GAP]`" | The person, or the owner they name, supplies it; never fill it |

## The person's facts

| Situation | How to word it |
|---|---|
| No decision maker or choice | "Decision not given"; ask; the frame stops here (old DH-05.01.3.1.3) |
| No current cost or no source for it | "Current cost not given `[GAP]`"; the value case is not written as complete |
| No priority rule, or scores labeled proposed | "Not ranked: rule not given" or "Not ranked: proposed scores are never sent to analytics.rice or analytics.mcda" |
| No owner for a metric or a stop rule | "owner not named"; ask |
| A dashboard figure without its data timestamp | "Data timestamp not given"; the figure is not compared |
| No rule for when a segment accounts for a move | "Your rule not given: no driver named" |
| A date, data cut, threshold or status not given | "Not given"; ask. Never fill |
| A vendor or press claim the person brings | "From you (vendor or press claim, not checked against a primary record)" |
| A field the person's file lacks | "not in your file"; never 0 or none |

## Library facts

| Situation | How to word it |
|---|---|
| A tool with no saved output | "needs a live check" |
| `check_claim` "supported" | Accepted only when the passage reads in the same direction as the claim (register N3) |
| RICE confidence as a fraction | "Confidence must be a whole percent; recompute with 80, not 0.8" |

## Never

- Never supply a target, threshold, tolerance, adoption level or value benchmark.
- Never say a decision support function is or is not a device, or that a tool complies with 45 CFR 92.210 or a certification criterion.
- Never name a driver without the person's rule; never add a second claim to commentary.
- Never present a draft guidance or a proposed rule as a requirement.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words, with the row id after it: "FDA CDS guidance, 29 January 2026 (UX-US-65)", "Kahn 2016, DOI 10.13063/2327-9214.1244 (DA-94)". Never a row id alone. A row marked [WF] adds "[WF]"; a [PAPER] row adds its DOI at first use; a [SPEC] row adds "[SPEC]". Where the row gives no publication date, use the date it was read: "CMS MMS Hub, read 20 October 2026 (DA-134)".

| Rows | Cite as |
|---|---|
| DA-01 to DA-16 | NIST AI Risk Management Framework 1.0 (NIST AI 100-1), January 2023 |
| DA-17 to DA-21 | NIST AI 600-1 Generative AI Profile, July 2024 |
| DA-22, DA-23 | ISO/IEC 42001 and 23894 public pages, read 20 October 2026 [WF] |
| DA-24 to DA-29 | WHO Ethics and governance of AI for health, 28 June 2021 (publication page and news release) |
| DA-30 to DA-34 | WHO guidance on large multi-modal models (news release 18 January 2024; publication page dated 25 March 2025) |
| DA-35 to DA-46 | FDA AI-enabled device software functions draft guidance, January 2025 (draft, not for implementation) |
| DA-47 to DA-67 | Regulation (EU) 2024/1689 (AI Act), as amended by Regulation (EU) 2026/1744 where the row says so |
| DA-80 to DA-84 | DECIDE-AI, Vasey et al. 2022, DOI 10.1136/bmj-2022-070904 |
| DA-94 to DA-98 | Kahn et al. 2016, DOI 10.13063/2327-9214.1244 |
| DA-99 to DA-101 | FAIR principles, Wilkinson et al. 2016, DOI 10.1038/sdata.2016.18 |
| DA-102 to DA-106 | OHDSI OMOP CDM documentation, read 20 October 2026 [SPEC] |
| DA-107 to DA-112 | ONC USCDI page and 45 CFR 170.213, read 20 October 2026 |
| DA-113 to DA-115 | Rajkomar et al. 2018, DOI 10.7326/M18-1990 |
| DA-116 to DA-120 | Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9 |
| DA-132 to DA-140 | CMS Measures Management System Hub, read 20 October 2026 (CMS quality-measure guidance) |
| UX-US-54 to UX-US-59, UX-US-62 | 45 CFR 170.315(b)(11) and (g)(3), from HTI-1, eCFR read 19 October 2026 |
| UX-US-60, UX-US-61, UX-US-63 | ONC HTI-5 proposed rule, 29 December 2025 (90 FR 60970), proposed only |
| UX-US-64 to UX-US-74 | FDA Clinical Decision Support Software guidance, 29 January 2026 |
| PE-113 to PE-115 | 45 CFR 92.210, eCFR read 19 October 2026 |
| CS13 | CFIR 2022, Damschroder et al., DOI 10.1186/s13012-022-01245-0 |
| CS38 | Proctor et al. 2011, DOI 10.1007/s10488-010-0319-7 (the library record gives 2010) |
| CS60, CS63, CS65 | NICE Evidence Standards Framework, last updated 9 August 2022 |
| CS103 to CS105 | HIPAA Privacy Rule, 45 CFR 164.502 and 164.514, eCFR read 19 October 2026 |
| EN-097 to EN-105 | HIPAA Security Rule, 45 CFR Part 164 Subpart C, eCFR read 20 October 2026 |
| EN-106, EN-107 | HIPAA Security Rule NPRM, Federal Register 6 January 2025; 2026 Unified Agenda (proposal, not final) |
| Library facts | "library, retrieved 19 October 2026" plus the saved file name |
| The person's files | "your file NAME, as of the date you gave" |
