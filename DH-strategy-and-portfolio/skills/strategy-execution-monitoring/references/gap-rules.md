# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | An SP or DL row states it | The fact, the source name and date in plain words, then the row id ("A benefits register lists baseline, target and measurement method (UK Benefits Measurement Guidance Note, May 2021, SP-104)") | None |
| UK public-sector guidance used for a company | Green Book, benefits assurance, benefits measurement note | "UK public-sector guidance (SP-105), applied here as a checklist" | Never a rule the company must follow |
| Summarized read | The row is [WF] (SP-106, SP-148 to SP-162, DL-150 to DL-153) | "(UK Government Project Delivery benefits collection, 30 July 2026, SP-106 [WF])" | Say the quote is close but not script-checked |
| Published method | The row is [PAPER] (SP-107, SP-108) | The row id and its DOI at first use | State the review's own limits (high risk of bias, SP-108) |
| Researcher's reading | The row says "(inference)" (DL-018, DL-101, DL-137, DL-139, DL-142, DL-147, DL-149, DL-159, DL-163, DL-166, DL-168) | "Form 15 means SEC reporting stopped, not that the company ceased to exist (SEC Rule 12h-3, DL-149, inference)", every time it is cited | Never as the regulator's words |
| Not in the sources | Realization benchmarks, milestone hit rates, experiment success rates, OKR method, market sizes, optimism bias bounds for operating costs or benefits shortfall (SP-176), Virtual Therapeutics Corporation's corporate status | "Not in this skill's sources `[GAP]`" | The person supplies it or it stays a gap |

## Library facts

| Situation | How to word it |
|---|---|
| A period that starts before the change log (12 October 2026) | "The library change log began 12 October 2026, after the start of your period; it cannot show changes before then. Here are the company's dated authorization and filing records instead"; never "no change" |
| No change recorded inside the log window | "No change recorded in the library log from DATE to the last sweep DATE; a statement about the log, not the company" |
| Company status, company read in the research pass (Akili, Pear, Big Health, Aidoc) | Quote the status from `execution-frameworks.md` section 5 with filing name, date and row ("Akili 8-K, 2 July 2024, Items 2.01 and 5.01 (SP-151 [WF])") |
| Company status, any other company | "Company status [GAP]: not read" plus the filings to open (DL-135 to DL-168); Form 25 concerns the listing only (DL-144); Form 15 is not dissolution (DL-149, inference) |
| Product holder | The applicant at clearance and the current FDA listing holder, each with its source; never the listing holder as buyer or licensor |
| A field the saved record lacks | "not stored"; never 0 or none |
| Analytics default range | "plus or minus 20 percent default, not your range" |
| A tool with no saved output | "needs a live check" |

## The person's facts

| Situation | How to word it (script flag) |
|---|---|
| Benefit owner missing | "owner not named" (E1); ask |
| Baseline or target missing | "not given" (E2, E3); the share of planned change is not computed |
| No actual measured | "not measured" (E4) |
| Reread date earlier than the read date | Stated as a fact (E5), never as urgency |
| Pass rule missing | "pass rule not given" (E6, or "pass rule not given" in the milestone table); nothing is marked met or failed |
| Actual dated after the read date or before the baseline date | Stated as a fact (E7); the reading does not belong to the period |
| Milestone owner, evidence, timing | M1 to M6 as the script prints them; not-yet-due milestones are "not yet due" |
| Experiment elements | X1 to X6; a test without a rule written before the start "cannot be read against a rule" |
| Press or vendor claims | "From you (press claim, not checked against a primary record)" |
| A date, data cut, threshold or status not given (including the read date, a reread or recheck date, an owner or a pass rule) | "Not given"; ask. Never fill, and never use today's date as the read date |

## Never

- Never call the strategy on track or off track overall.
- Never set a target, a pass rule, a threshold, an owner or a recheck date.
- Never decide kill or continue.
- Never turn a press claim into a signal or a status.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words, with the row id after it: "Pear 8-K, 7 April 2023 (SP-156)", "HM Treasury Green Book, 5 February 2026 (SP-092)". Never a row id alone. A row marked [WF] adds "[WF]"; a row marked "(inference)" adds "(inference)" every time it is cited; a [PAPER] row adds its DOI at first use. Where the row gives no publication date, use the date it was read: "MHRA IDAP page, read 20 October 2026 (SP-124)".

| Rows | Cite as |
|---|---|
| SP-029 to SP-031 | European Commission, Horizon Europe Work Programme 2026-2027, Annex XV |
| SP-032 to SP-035 | NASA technology readiness levels page, read 20 October 2026 |
| SP-036 to SP-043 | OECD/Eurostat Oslo Manual, 2018 |
| SP-044 to SP-047 | ISO abstract pages, read 20 October 2026 [WF] |
| SP-048 to SP-053 | WHO guideline on digital interventions, 2019 |
| SP-054 to SP-057 | WHO Classification of digital interventions, second edition, 2023 |
| SP-059 to SP-065 | WHO Global strategy on digital health 2020-2025 (published 2021) |
| SP-066 | World Health Assembly WHA78 decision, 27 May 2025 |
| SP-068 to SP-073 | Regulation (EU) 2025/327 (European Health Data Space), 11 February 2025 |
| SP-074 to SP-081 | ISPOR MCDA Report 2, Marsh et al. 2016 [WF], DOI 10.1016/j.jval.2015.12.016 |
| SP-082 to SP-085 | Wong, Siah and Lo 2019, DOI 10.1093/biostatistics/kxx069 |
| SP-086, SP-087 | Büssgen and Büssgen 2023, DOI 10.1186/s40545-023-00612-6 |
| SP-088 to SP-098 | HM Treasury Green Book, 5 February 2026 (UK public-sector guidance) |
| SP-099 to SP-103 | Assurance of Benefits Realisation in Major Projects v2.1, August 2026 (UK public-sector guidance) |
| SP-104, SP-105 | UK Benefits Measurement Guidance Note, May 2021 (UK public-sector guidance, written for commercial benefits) |
| SP-106 | UK Government Project Delivery benefits management collection, 30 July 2026 [WF] |
| SP-107 | Balanced scorecard systematic review, Int J Environ Res Public Health 2022, DOI 10.3390/ijerph191610291 |
| SP-108 | Amer et al. 2022, BMC Health Serv Res, DOI 10.1186/s12913-021-07452-7 |
| SP-109 to SP-118 | FDA early feasibility study guidance, October 2013 |
| SP-119, SP-120 | FDA Early Feasibility Studies Program page, read 20 October 2026 |
| SP-121, SP-122 | FDA TAP pages, read 20 October 2026 (enrollment count as of 7 October 2026) |
| SP-124 to SP-126 | MHRA IDAP pages, read 20 October 2026 |
| SP-127 to SP-129 | NHS AI and Digital Regulations Service, read 20 October 2026 |
| SP-130 to SP-133 | SEC Regulation S-K Item 601(b)(10) (eCFR, read 20 October 2026) |
| SP-134 | Regulation (EU) 316/2014, expired 30 April 2026 |
| SP-135 to SP-140 | Regulation (EU) 2026/877 of 16 April 2026 |
| SP-141, SP-142 | European Commission Technology Transfer Guidelines, OJ 21 April 2026 |
| SP-143 to SP-147 | DOJ/FTC Antitrust Guidelines for the Licensing of Intellectual Property, 12 January 2017 |
| SP-148 | Akili, Inc. EDGAR submissions record, read 20 October 2026 [WF] |
| SP-149 | Akili 8-K, 30 April 2024 [WF] |
| SP-150 | Akili 8-K, 29 May 2024 [WF] |
| SP-151, SP-152 | Akili 8-K, 2 July 2024 [WF] |
| SP-153 | Akili Form 25-NSE, 2 July 2024 [WF] |
| SP-154 | Akili Form 15-12G, 12 July 2024 [WF] |
| SP-155 | Pear EDGAR submissions record, read 20 October 2026 [WF] |
| SP-156 to SP-159 | Pear 8-K, 7 April 2023 [WF] |
| SP-160 | Pear 8-K, 10 April 2023 [WF] |
| SP-161 | Pear EDGAR submissions record, read 20 October 2026 [WF] |
| SP-162 | EDGAR company lookup and full-text search, 20 October 2026 [WF] |
| SP-163, SP-164, SP-167 to SP-169 | FDA registration and listing database (openFDA), read 20 October 2026 |
| SP-165 | FDA 510(k) record K191716, decision 23 March 2020 |
| SP-166 | FDA De Novo record DEN200026, read 20 October 2026 |
| SP-170 | HM Treasury optimism bias supplementary guidance page (gov.uk, first published 21 April 2013) |
| SP-171 | HM Treasury Green Book, 5 February 2026 |
| SP-172 to SP-176 | HM Treasury Green Book supplementary guidance: optimism bias (2003 PDF, Mott MacDonald review of 2002), Table 1 and method |
| DL-016, DL-018 | SEC Form D instructions (DL-018 is an inference) |
| DL-019 to DL-021, DL-135 to DL-141 | SEC Form 8-K instructions (DL-137 and DL-139 are inferences) |
| DL-142 to DL-145 | SEC Rule 12d2-2, Form 25 (eCFR, read 20 October 2026; DL-142 is an inference) |
| DL-146 to DL-149 | SEC Rules 12g-4 and 12h-3, Form 15 (eCFR, read 20 October 2026; DL-147 and DL-149 are inferences) |
| DL-150 to DL-153 | SEC EDGAR API and fair access pages [WF] |
| DL-154 to DL-156 | PACER (US federal courts) pages |
| DL-157 to DL-164 | Companies House register guidance (DL-159 and DL-163 are inferences) |
| DL-165 to DL-168 | German insolvency and register portals (DL-166 and DL-168 are inferences) |
| DL-101, DL-106 | GDPR, Regulation (EU) 2016/679, Articles 9(1) and 35(3)(b) (DL-101's second sentence is an inference) |
| UK-06 to UK-08 | MHRA AI Airlock pages, read 20 October 2026 |
| PL110 to PL112 | IDEAL-D, Marcus et al. 2022, DOI 10.1097/SLA.0000000000004907 |
| CS56, CS57, CS67 | NICE Evidence Standards Framework |
| Library facts | "library, retrieved 19 October 2026" plus the record number (for example "FDA 510(k) K231337, library, retrieved 19 October 2026") |
