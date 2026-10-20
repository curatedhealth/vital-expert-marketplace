# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | An EN, CP, CS, DL or PL row states it | The fact, the source name and date in plain words, then the row id ("A cloud provider holding only encrypted ePHI without the key is still a business associate (HHS cloud computing guidance page, read 20 October 2026, EN-032 [WF])") | None |
| Summarized read | The row is [WF] (EN-032 to EN-035, EN-080, EN-081, EN-173, EN-174; CS69 to CS71) | Add "[WF]" every time it is applied | Say the quote is close but not script-checked |
| Researcher's reading | The row says "(inference)" (DL-087 second sentence, DL-092 last sentence, DL-097 last sentence, DL-101 second sentence) | Add "(inference)" every time it is cited | Never as the regulator's words |
| Proposal, not a rule | HIPAA Security Rule NPRM (EN-106, EN-107) | "Proposed on 6 January 2025; not final; the 2026 Unified Agenda shows final action 07/00/2027 (EN-106, EN-107)" | Never applied as a requirement; its specifics were not read `[GAP]` |
| Enforcement policy, not statute | FDA 30 and 60 days for uncontrolled risk (EN-066, EN-067) | "FDA's 2016 enforcement policy for 21 CFR 806, not a statutory deadline; 524B says 'reasonable time' and 'as soon as possible out of cycle'" | State both, without leaning |
| Moved or replaced | FDA premarket cybersecurity guidance (3 February 2026 supersedes 27 June 2025); CSA guidance (3 February 2026); Part 2 compliance date passed 16 February 2026 | "FDA premarket cybersecurity guidance, 3 February 2026, supersedes the 27 June 2025 final (EN-047)" | State the instrument and date |
| Scope depends on facts not read | NIS2 size thresholds and national transposition | "Annex II covers MDR and IVDR manufacturers (EN-094); size thresholds and national law decide scope and were not read `[GAP]`" | The legal owner checks national law |
| Not in the sources | IEC 62304 safety classes; NTIA SBOM minimum elements; CVSS, EPSS or any severity scale; HIPAA NPRM specifics; GDPR Articles 7 and 33(1); MHRA and Health Canada cybersecurity guidance; NHS DSPT; TIR57, TIR97 and IEC 81001-5-1 content beyond the recognition abstracts; any threat taxonomy beyond EN-050 and EN-051 | "Not in this skill's sources `[GAP]`" | The person, or the owner they name, supplies it; never fill it |
| A threshold the person did not set | Patch windows, severity cut-offs, risk acceptance criteria, support horizon | "Not given; ask. No source sets one" | Never supplied by the model |

## Library facts

| Situation | How to word it |
|---|---|
| A record holds an authorization | "K191716: Somryst, FDA 510(k), decision 23 March 2020 (library, retrieved 19 October 2026)" |
| A safety event | Title, date, class and manufacturer as the record states them, and what its summary says; never judge its relevance to the person's product |
| A safety event search with no security cause in the returned summaries | "None of the returned summaries names a security cause (keyword check of the saved output); a missing record is a coverage limit, not evidence that none exists" |
| A tool with no saved output | "needs a live check" |
| A field the saved record lacks | "not stored"; never 0 or none |

## The person's facts

| Situation | How to word it |
|---|---|
| No legal basis for a data class | "Basis not given `[GAP]`" |
| A control listed but not shown in force | "Not in force (intended only)" or "artifact not named" |
| A threat with no control and no acceptance | "Open" |
| An acceptance without a named person or reopen condition | "Acceptance has no named acceptor" or "no reopen condition" |
| A component without level of support or end-of-support date | "Not given (EN-054)" |
| A press or vendor claim | "From you (press or vendor claim, not checked against the primary record)" |
| A date, data cut, threshold or status not given | "Not given"; ask. Never fill |

## Never

- Never call a product compliant or secure, or a risk acceptable.
- Never supply a threshold, window, score or severity.
- Never describe a proposed rule as in force.
- Never write exploit or attack detail.
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. In answers, every fact names its source and date in plain words, with the row id after it: "FDA premarket cybersecurity guidance, 3 February 2026 (EN-057)", "45 CFR 164.312, eCFR read 20 October 2026 (EN-103)". Never a row id alone. A row marked [WF] adds "[WF]"; a row marked "(inference)" adds "(inference)" every time it is cited. No [PAPER] rows are used in this skill. Where the row gives no publication date, use the date it was read.

| Rows | Cite as |
|---|---|
| EN-023 to EN-027 | FDA Off-The-Shelf Software Use in Medical Devices guidance, 11 August 2023 |
| EN-032 to EN-035 | HHS guidance on HIPAA and cloud computing, page read 20 October 2026 [WF] |
| EN-036 to EN-040 | NIST SP 800-218 (SSDF) version 1.1, February 2022 |
| EN-041 to EN-046 | FD&C Act section 524B (21 USC 360n-2), US Code read 20 October 2026 |
| EN-047 to EN-061 | FDA premarket cybersecurity guidance, 3 February 2026 |
| EN-062 to EN-068 | FDA postmarket cybersecurity guidance, 28 December 2016 |
| EN-069, EN-070 | MDR, Regulation (EU) 2017/745, Annex I 17.4 and 18.8 (consolidated text read 20 October 2026) |
| EN-071 to EN-074 | MDCG 2019-16 rev.1, July 2020 |
| EN-075 to EN-077 | NIST Cybersecurity Framework 2.0, 26 February 2024 |
| EN-078, EN-079 | NIST SP 800-30 Rev. 1, September 2012 |
| EN-080, EN-081 | CISA Known Exploited Vulnerabilities catalog page, read 20 October 2026 [WF] |
| EN-082 to EN-085 | FDA recognized consensus standards database entries, read 20 October 2026 |
| EN-086 to EN-092 | Cyber Resilience Act, Regulation (EU) 2024/2847 |
| EN-093 to EN-096 | NIS2 Directive (EU) 2022/2555 |
| EN-097 to EN-105 | HIPAA Security Rule, 45 CFR Part 164 Subpart C (eCFR read 20 October 2026) |
| EN-106 | HIPAA Security Rule NPRM, Federal Register, 6 January 2025 (proposed) |
| EN-107 | Unified Agenda entry RIN 0945-AA22, read 20 October 2026 |
| EN-108 to EN-113 | GDPR, Regulation (EU) 2016/679, Articles 25, 32, 35 and 36 |
| EN-114, EN-115, EN-120 | 42 CFR Part 2 final rule, Federal Register, 16 February 2024 |
| EN-116 to EN-119 | 42 CFR Part 2 (eCFR read 20 October 2026) |
| EN-121 to EN-128 | Washington My Health My Data Act, RCW 19.373 (read 20 October 2026) |
| CP-US-44 | 45 CFR 160.103 (eCFR read 19 October 2026) |
| CP-US-54 to CP-US-56 | FTC Health Breach Notification Rule, 16 CFR Part 318 (eCFR read 19 October 2026) |
| CP-EU-01 to CP-EU-08 | GDPR, Regulation (EU) 2016/679, Articles 28 and 33(2) |
| CP-UK-01 to CP-UK-04 | NHS AI and Digital Regulations Service, DTAC guidance, read 19 October 2026 |
| CP-UK-05 | Health and Social Care Act 2012, section 250 |
| CP-UK-06 to CP-UK-10 | NHS AI and Digital Regulations Service, DCB0129 and DCB0160 guidance, read 19 October 2026 |
| CP-UK-11 | NHS AI and Digital Regulations Service blog (a blog, not the standard) |
| CS68 | NICE Evidence Standards Framework |
| CS69 to CS71 | NHS England and NHS Digital pages on DTAC and DCB0160, read 19 October 2026 [WF] |
| CS96 to CS105 | HIPAA, 45 CFR 164.314, 164.410, 164.502, 164.504 and 164.514 (eCFR read 19 October 2026) |
| CS106 to CS110 | GDPR, Regulation (EU) 2016/679, Articles 28 and 33(2) |
| DL-024, DL-027 | SEC Form 8-K and Form 10-K instructions, read 20 October 2026 |
| DL-086 to DL-094 | HIPAA Breach Notification Rule, 45 CFR 164.402 to 164.414 (eCFR read 20 October 2026) |
| DL-099 to DL-106 | GDPR, Regulation (EU) 2016/679, Articles 4, 9 and 35(3)(b) |
| PL87 | DiGAV (gesetze-im-internet.de), read 20 October 2026 |
| Library facts | "library, retrieved 19 October 2026" plus the record number |
