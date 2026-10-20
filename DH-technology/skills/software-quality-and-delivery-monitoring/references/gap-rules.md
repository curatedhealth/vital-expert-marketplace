# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | An EN, QS, EU, ST, CH, PL or AI US row states it | The fact, the source name and date in plain words, then the row id ("Any change, even a small one, re-opens validation (FDA General Principles of Software Validation, 11 January 2002, EN-008)") | None |
| Summarized read | The row is [WF] (EN-032 to EN-035, EN-080, EN-081, PL97 to PL102) | "(HHS OCR cloud computing guidance, read 20 October 2026, EN-032 [WF])" | Say the quote is close but not script-checked |
| Abstract only | Standards known only by an FDA recognition entry or an IEC or ISO catalog page (IEC 62304, IEC 82304-1, IEC 81001-5-1, AAMI TIR45, TIR57, TIR97) | "IEC 62304 edition 1.1, 2015, FDA recognition 13-79 (ST7, ST9); clause content not in this skill's sources" | The person reads their licensed copy |
| Proposal, not a rule | HIPAA Security Rule NPRM of 6 January 2025 (EN-106, EN-107) | "Proposed on 6 January 2025, not final; the Unified Agenda lists it under Long-Term Actions (EN-107); the current Security Rule remains in force" | Never present a proposed specific as a requirement; its specifics were not read |
| Enforcement policy, not statute | The 30 and 60 day clocks of the 2016 postmarket cybersecurity guidance (EN-066, EN-067) | "FDA enforcement policy for 806 reporting, not a statutory deadline; 524B says reasonable time and as soon as possible out of cycle (EN-043, EN-044)" | State both |
| Not in the sources | Any threshold for trace coverage, deploy frequency, change failure, rollback, recovery time, capacity margin, uptime or end of support; DevOps benchmark tiers; IEC 62304 class definitions and class-by-class plans; NTIA SBOM minimum elements; CI/CD-specific regulator text; GDPR international transfers; release criteria | "Not in this skill's sources `[GAP]`" | The person supplies it from their own standard, procedure or regulator contact, or it stays a gap |

## Library facts

| Situation | How to word it |
|---|---|
| A recall of comparable software | Title, date and class as the record states them, "FDA recall record, library, retrieved 19 October 2026"; never a judgment of relevance to the person's product |
| A row matched only on title words | "Matched the word 'software' in its title; not a software defect as the record states it" |
| MAUDE counts | "Reports by product code and year; reports, not confirmed events; no manufacturer attached" |
| EU safety search | "The library holds no EU safety events (list_jurisdictions, 19 October 2026); an empty EU result says nothing about the market" |
| A field the saved record lacks | "not stored"; never 0 or none |
| A tool with no saved output | "needs a live check" |

## The person's facts

| Situation | How to word it (script flag) |
|---|---|
| Hazard with no case; hazard covered only by unit-level cases | "No case points to HZ-nn" (T1); "only unit-level cases; whether they exercise the hazard is yours" (T2) |
| Case run on a build other than the candidate, no waiver | "Run on 3.2.0, candidate 3.2.1-rc2; repeat or waive is yours" (T3) |
| Case failed or not run; expected output "works correctly" or blank | T4; T5, quoted as written |
| Class not given, or an item the person says influences a clinical action carries the class the person names as lowest | T6; T7 listed for the person, never reclassified |
| Plan missing, draft, template not filled, or naming another product | L1 to L4 |
| Required stage skipped; skip with no exception recorded at the time; failure caught in production; caught-at not given | R1 to R4; an unrecorded skip is not a hotfix |
| SBOM support fields missing or outside the FDA values; not maintained; past end of support; CVE in the KEV list the person supplied | S1 to S5; dates are facts, not urgency |
| Quota offered as a load test; no measurement; saturation on a component the design did not name | K1 to K3 |
| Live, replica or backup region differs from the placement table | Y1 to Y3; whether it is permitted is the owner's |
| Pass rule missing; failed element without owner, recheck date or blocks-release statement; closed without evidence; recheck date passed; build not given | G1 to G7; an element without a rule is not marked pass or fail |
| A period, read date, threshold, owner, recheck date or status not given | "Not given"; ask. Never fill, and never use today's date as the read date |
| A benchmark or press claim ("elite teams fail under 15%") | "From you (claim, not in this skill's sources); not a rule unless you adopt it as yours" |

## Never

- Never supply a threshold, coverage figure, failure rate, capacity margin or end-of-support allowance.
- Never give an overall quality verdict, a go or no-go, or close a failed element.
- Never reclassify an item or say a class is wrong; list the facts for the person.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words, with the row id after it. Never a row id alone. A row marked [WF] adds "[WF]". Where the row gives no publication date, use the date it was read.

| Rows | Cite as |
|---|---|
| EN-001 to EN-011 | FDA General Principles of Software Validation, 11 January 2002 |
| EN-012 to EN-022 | FDA Computer Software Assurance guidance, reissued 3 February 2026 |
| EN-023 to EN-027 | FDA Off-The-Shelf Software Use in Medical Devices, 11 August 2023 |
| EN-028 to EN-030 | FDA recognized standards entry for AAMI TIR45:2023, read 20 October 2026 |
| EN-031, EN-069, EN-070 | MDR (Regulation (EU) 2017/745) Annex I, consolidated 19 July 2026 |
| EN-032 to EN-035 | HHS OCR guidance on HIPAA and cloud computing, read 20 October 2026 [WF] |
| EN-036 to EN-040 | NIST SP 800-218 (SSDF) version 1.1, February 2022 |
| EN-041 to EN-046 | FD&C Act section 524B (21 USC 360n-2) |
| EN-047 to EN-061 | FDA premarket cybersecurity guidance, 3 February 2026 |
| EN-062 to EN-068 | FDA postmarket cybersecurity guidance, 28 December 2016 |
| EN-082 to EN-085 | FDA recognized standards entries (TIR57, IEC 81001-5-1, TIR97), read 20 October 2026 |
| EN-080, EN-081 | CISA Known Exploited Vulnerabilities Catalog page, read 20 October 2026 [WF] |
| EN-086 to EN-092 | Cyber Resilience Act, Regulation (EU) 2024/2847 |
| EN-097 to EN-105 | HIPAA Security Rule, 45 CFR 164 Subpart C (eCFR, read 20 October 2026) |
| EN-106, EN-107 | HIPAA Security Rule proposed rule, 6 January 2025 (90 FR 898), and Unified Agenda entry RIN 0945-AA22 |
| EN-108 to EN-110 | GDPR, Regulation (EU) 2016/679, Articles 25 and 32 |
| QS6, QS9, QS22 | QMSR final rule, 89 FR 7496, 2 February 2024, and 21 CFR 820 (eCFR, as of 14 October 2026) |
| QS31, QS33, QS34 | FDA Compliance Program 7382.850, 2 February 2026 |
| ST6 to ST8 | IEC webstore pages for IEC 62304, read 19 October 2026 |
| ST9 to ST11 | FDA recognized standards entries for IEC 62304 and IEC 82304-1, read 19 October 2026 |
| EU19, EU20 | MDR Annex I sections 17.1 and 17.2 (consolidated 10 January 2025) |
| EU30 | European Commission harmonized standards page and decisions to 11 June 2026, measured 19 October 2026 |
| CH1 to CH4 | MDR Article 120 (consolidated 10 January 2025) |
| CH3 to CH8 | MDCG 2020-3 Rev.1, May 2023 |
| CH9 to CH16 | FDA "Deciding When to Submit a 510(k) for a Software Change to an Existing Device", 25 October 2017 |
| PL7, PL11 | QMSR final rule, 89 FR 7496, 2 February 2024 |
| PL12, PL24 to PL29 | FDA Multiple Function Device Products guidance, 29 July 2020 |
| PL15 to PL22 | FDA guidance on premarket submissions for device software functions (fda.gov/media/153781), read 20 October 2026 |
| PL45 to PL49 | FDA device software functions policy, 28 September 2022 (PL45), and General Wellness guidance, 6 January 2026 (PL46 to PL49) |
| PL97 to PL102 | NHS DTAC and DCB0129 pages, read 20 October 2026 [WF] |
| PL103 to PL105 | IEC webstore pages for IEC 82304-1 and IEC 62304, read 20 October 2026 |
| AI US-01 to AI US-14, AI US-36 | FDA PCCP final guidance for AI-enabled device software functions, 18 August 2025 |
| AI US-30, AI US-31 | FDA, Health Canada and MHRA PCCP guiding principles, October 2023 |
| Library facts | "library, retrieved 19 October 2026" plus the record number or recall title and date |
