# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A CS, DA, UX, PE or EN row states it | The fact, the source name and date in plain words, then the row id ("Reach is computed on a valid denominator, not volunteers (RE-AIM, re-aim.org, read 19 October 2026, CS27)") | None |
| Guidance used as context | NICE ESF usage profile outside the NHS; FDA human factors guidance on training for internal analytics; CMS measure rows for internal metrics | "NHS evidence standard, used here as context (CS61)" | Never presented as a rule the organization must follow |
| Draft or proposal | FDA AI-enabled device software functions draft (DA-35, DA-44); ONC HTI-5 proposal (UX-US-60); HIPAA Security Rule NPRM (EN-106, EN-107) | "A January 2025 draft, not for implementation (DA-35)" | Never as a requirement |
| Dated application | AI Act Articles 10 to 15 and 72 as amended (DA-66, DA-67) | "applies from 2 December 2027 (Annex III) or 2 August 2028 (Annex I) as amended by Regulation (EU) 2026/1744 (DA-67)" | State the instrument that moved the date |
| Published method | The row is [PAPER] | The row id and its DOI at first use | State the paper's own setting |
| Abstract only | CS21 (RE-AIM 1999) | "Glasgow 1999, abstract only (CS21)" | Definitions come from re-aim.org (CS22 to CS30) |
| Summarized read | The row is [WF] (DA-93) | "Finlayson 2021 (DA-93) [WF]" | Say the quote is close but not script-checked |
| Not in the sources | Adoption, penetration, literacy, agreement, override, cadence or outcome targets; a review interval; a stale rule; a validated data-literacy instrument | "Not in this skill's sources `[GAP]`" | The person, or the owner they name, supplies it; never fill it |

## The person's facts

| Situation | How to word it |
|---|---|
| No one marked in scope | "Valid denominator not given (flag A1)"; nothing is reported as a rate of adoption |
| Window or read date not given | "Not given"; ask; the funnel is not run |
| Trained with no practice proof | "Attended, practice task not done or not recorded (A2)"; never counted as enabled |
| A metric never instrumented | "Not instrumented `[GAP]`"; never zero, never a product failure |
| No comparison for the bet metric | "No comparison (O1)"; the change is not reported |
| A champion with no record | "Unmeasured (no record)"; never inactive |
| No pass rule for a unit | "Pass rule not given `[GAP]`"; values reported, nothing marked met or missed |
| No owner or recheck date for a miss | "owner not named"; "recheck date not given"; ask |
| A date, data cut, threshold or status not given | "Not given"; ask. Never fill |
| A field the person's file lacks | "not in your file"; never 0 or none |
| A vendor dashboard figure the person brings | "From you (vendor figure, not recomputed from your file)" |

## Library facts

| Situation | How to word it |
|---|---|
| A tool with no saved output | "needs a live check" |
| `check_claim` "supported" | Accepted only when the passage reads in the same direction as the claim (register N3) |

## Never

- Never supply an adoption target, penetration benchmark, agreement or override limit, cadence tolerance, review interval or stale rule.
- Never call a product a success or a failure, or decide keep, change or stop.
- Never rank or judge named individuals; report by role and site unless the person asks for named follow-up lists for their own use.
- Never present a draft guidance or a proposed rule as a requirement.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words, with the row id after it: "Proctor 2011, DOI 10.1007/s10488-010-0319-7 (CS39)", "45 CFR 92.210, eCFR read 19 October 2026 (PE-113)". Never a row id alone. A row marked [WF] adds "[WF]"; a [PAPER] row adds its DOI at first use. Where the row gives no publication date, use the date it was read.

| Rows | Cite as |
|---|---|
| CS8 | CFIR 2009, Damschroder et al., DOI 10.1186/1748-5908-4-50 |
| CS21 | RE-AIM, Glasgow, Vogt and Boles 1999, DOI 10.2105/ajph.89.9.1322 (abstract only) |
| CS22 to CS30 | RE-AIM official site, re-aim.org, read 19 October 2026 |
| CS31 to CS40 | Proctor et al. 2011, DOI 10.1007/s10488-010-0319-7 (the library record gives 2010) |
| CS41 to CS49 | ERIC, Powell et al. 2015, DOI 10.1186/s13012-015-0209-1 |
| CS60 to CS62 | NICE Evidence Standards Framework, last updated 9 August 2022 |
| CS77, CS78 | FDA Applying Human Factors and Usability Engineering to Medical Devices, reissued 3 August 2026 |
| CS104 | HIPAA Privacy Rule, 45 CFR 164.514, eCFR read 19 October 2026 |
| DA-14 | NIST AI Risk Management Framework 1.0, January 2023 |
| DA-29 | WHO Ethics and governance of AI for health, 28 June 2021 |
| DA-35, DA-44 | FDA AI-enabled device software functions draft guidance, January 2025 (draft, not for implementation) |
| DA-54, DA-55, DA-65 to DA-67 | Regulation (EU) 2024/1689 (AI Act), as amended by Regulation (EU) 2026/1744 where the row says so |
| DA-80 to DA-84 | DECIDE-AI, Vasey et al. 2022, DOI 10.1136/bmj-2022-070904 |
| DA-91, DA-92 | Davis et al. 2017, DOI 10.1093/jamia/ocx030 |
| DA-93 | Finlayson et al. 2021, DOI 10.1056/NEJMc2104626 [WF] |
| DA-119 | Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9 |
| DA-136, DA-139, DA-140 | CMS Measures Management System Hub, read 20 October 2026 (CMS quality-measure guidance) |
| UX-US-55 | 45 CFR 170.315(b)(11), from HTI-1, eCFR read 19 October 2026 |
| UX-US-60 | ONC HTI-5 proposed rule, 29 December 2025 (90 FR 60970), proposed only |
| PE-113 to PE-115 | 45 CFR 92.210, eCFR read 19 October 2026 |
| EN-101, EN-103 | HIPAA Security Rule, 45 CFR Part 164 Subpart C, eCFR read 20 October 2026 |
| EN-106, EN-107 | HIPAA Security Rule NPRM, Federal Register 6 January 2025; 2026 Unified Agenda (proposal, not final) |
| Library facts | "library, retrieved 19 October 2026" plus the saved file name |
| The person's files | "your file NAME, window and read date as you gave them" |
