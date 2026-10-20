# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A DA or CV row states it | The fact, the source name and date in plain words, then the row id ("Completeness concerns whether attributes are present, not their values (Kahn et al. 2016, DA-97, DOI 10.13063/2327-9214.1244)") | None |
| Draft | FDA AI-enabled device software functions draft (DA-35, DA-37, DA-44) | "the draft proposes", plus "(draft)" | Never "FDA requires" |
| Future application date | EU AI Act Article 10 (DA-47 to DA-50) | State 2 December 2027 (Annex III) or 2 August 2028 (Annex I) as amended (DA-67) | Never "applies now" |
| Other market or setting used as context | FDA drug guidance for a device or analytics model; EMA for a device; CMS measure rules outside quality measures; DCT guidance outside a trial | "(FDA, drugs and biologics; context for your data)" | Say whose rule it is |
| Published method | [PAPER] row | Row id and the DOI of that row's own paper | None |
| Community standard | [SPEC] rows DA-102 to DA-106 | "OHDSI community standard" | Never "regulation" |
| Old method step | Rules taken from the old tasks (rule, score, repair) | "(old task DH-01.04.4.2.3, method)" | Never a regulator's rule |
| Not in the sources | Any limit, acceptable error share, drift threshold, re-run cadence, benchmark data quality score, ISO data quality standard text, OHDSI data quality dashboard checks | "Not in this skill's sources `[GAP]`" | The person supplies it or it stays a gap |

## Library facts

| Situation | How to word it |
|---|---|
| A library design label | "library label, checked against the paper: ..." (register N8) |
| A check_claim status | The tool status beside your own reading of the passage (register N3) |
| A tool with no saved output for this use | "needs a live check" |

## The person's facts

| Situation | How to word it (script flag) |
|---|---|
| Rules without a version | "dataset version not given" (Q1); a run cannot be tied to a version (V2) |
| Check in an unknown category | "category not recognized" (Q2) |
| Check without a limit | "limit not given" (Q3); counts reported, never pass or fail |
| Completeness the only check | Stated (Q4), with the old rule that one completeness percentage is not enough |
| No leak check | Stated (Q5) |
| Date the rules were written not given | Stated (Q6); the run cannot show the rules came first |
| Rules written for another version than the data read | Stated (V1); results reported against the rules as written |
| Failed check without owner, action, new version or recheck date | "owner not named" (R1), "not given" (R2, R3, R5); ask |
| Repair names the failed version itself | Stated (R4) |
| Repair log row for a check that did not fail in this run | Stated (R6) |
| Field not in the data, reference file not supplied | "not run", with the reason |
| A date, data cut, limit or status not given | "Not given"; ask. Never fill, and never use today's date as the read date |

## Never

- Never supply a limit or call a share acceptable.
- Never call a dataset fit for use, reliable or compliant.
- Never close a failed check or name an owner the person has not named.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. Every fact names its source and date in plain words, with the row id after it; never a row id alone. A [WF] row adds "[WF]"; a [PAPER] row adds its own DOI at first use; a draft row adds "draft".

| Rows | Cite as |
|---|---|
| DA-12 to DA-14 | NIST AI 100-1, AI Risk Management Framework 1.0, January 2023 (voluntary) |
| DA-35, DA-37, DA-44 | FDA AI-enabled device software functions draft guidance, January 2025 (draft, not for implementation) |
| DA-47 to DA-50 | EU AI Act, Regulation (EU) 2024/1689, Article 10 |
| DA-67 | Digital Omnibus, Regulation (EU) 2026/1744 |
| DA-68, DA-71, DA-73, DA-74 | EMA reflection paper on AI in the medicinal product lifecycle, adopted 9 September 2024 |
| DA-87, DA-88 | Sahiner et al., Br J Radiol 2023, DOI 10.1259/bjr.20220878 |
| DA-94 to DA-98 | Kahn et al., eGEMs 2016, DOI 10.13063/2327-9214.1244 |
| DA-99 to DA-101 | FAIR principles, Wilkinson et al., Sci Data 2016, DOI 10.1038/sdata.2016.18 |
| DA-102 to DA-106 | OHDSI OMOP CDM documentation, read 20 October 2026 (community standard) |
| DA-139, DA-140 | CMS Measures Management System Hub, read 20 October 2026 |
| CV65, CV71 | FDA guidance "Conducting Clinical Trials With Decentralized Elements", September 2024 (trial context) |
| CV78 to CV83 | FDA RWD guidance on EHR and medical claims data (drugs and biologics), July 2024 |
| CV86, CV87 | FDA RWD data standards guidance, December 2023 |
| Library facts | "library, retrieved 19 October 2026" plus the record identifier |
