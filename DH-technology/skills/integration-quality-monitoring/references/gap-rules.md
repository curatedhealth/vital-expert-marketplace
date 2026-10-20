# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | An EN, DA, CP, UX, CS, SP or PL row states it | The fact, the source name and date in plain words, then the row id ("ONC certification requires US Core 6.1.0 (45 CFR 170.215, eCFR read 20 October 2026, EN-134)") | None |
| Version fact | A standard's version is involved | Two columns, always: "required for certification" (with the regulation) and "current HL7 or ONC publication" (with its date) (`monitoring-rules.md` sections 1 and 5) | Never merge the two |
| After the read date | A standard, rule or proposal may have moved after 20 October 2026 | "As read on 20 October 2026 (ROW); later changes not read `[GAP]`" | A research pass reads the source again |
| Proposal, not a rule | HTI-5 proposals, the HIPAA Security Rule NPRM, the CMS drug prior authorization proposal, any draft ballot (FHIR R6, Bulk Data 4.0.0) | "Proposed on DATE; not in force on 20 October 2026 (ROW)" | Plan on the rule in force; the owner watches the proposal |
| Summarized read | The row is [WF] (EN-173, EN-174 LOINC) | "(LOINC license page, read 20 October 2026, EN-173 [WF])" | Say the quote is close but not script-checked |
| Published method | The row is [PAPER] (DA-94 to DA-101) | Row id and its DOI at first use | State the paper's own scope |
| Specification documentation | The row is [SPEC] (DA-102 to DA-106, OHDSI) | "(OHDSI OMOP CDM documentation, read 20 October 2026, DA-103 [SPEC])" | None |
| Blog, not the standard | CP-UK-11 | "A blog on the NHS AI and Digital Regulations Service states ... (CP-UK-11); confirm against the DCB0129 specification" | The person reads the standard |
| Not in the sources | Any conformance, launch, latency, mapping, workaround or adoption benchmark or threshold; US Core element lists; EHR vendor app terms; code system release versions; ConceptMap equivalence codes; CHPL entries | "Not in this skill's sources `[GAP]`; the authority is AUTHORITY" | The person supplies it, or a research pass reads it |

## The person's facts

| Situation | How to word it |
|---|---|
| Exchange partners, purpose, EHR, sandbox, guide or version not given | "Not given"; ask once |
| Check sheet not given (must-support paths, cardinality, bindings) | "Check sheet not given: the model cannot say which elements the guide requires; supply the guide's StructureDefinitions or your sheet" |
| Pass rule, ceiling, threshold, sample definition, owner, release or recheck date not given | "Not given"; ask. Never fill, and never use today's date as a read date |
| A payload, matrix, sample or observation file not supplied | "Not run: no data supplied"; never "passed" |
| Script flags (S1 to S3, L1 to L7, R1 to R4, W1) | Quote the flag and the fact as the script prints it; a flag is a fact, never a verdict |
| A vendor or press claim ("Epic supports X", "certified to R5") | "From you (claim, not checked against a primary record)" |

## Never

- Never average away a profile that failed every sample (old task DH-04.01.1.2.2).
- Never treat a mocked token as an EHR launch, or retry a failed cell until it passes (old task DH-04.01.2.2.2).
- Never close a failure because a ticket exists, or reclassify a failed cell as a known limitation without naming who accepted it (old tasks DH-04.01.1.2.3, DH-04.01.2.2.3).
- Never report a mean time from a single observation (old task DH-04.01.4.2.2).
- Never supply a threshold or a ceiling; never turn "not checked" into "passed".
- Never carry facts from an earlier request; use only the inputs of the current request.

## How to cite a fact in an answer

A reader must be able to open the source. Every fact names its source and date in plain words, with the row id after it. Never a row id alone. [WF] rows add "[WF]"; [PAPER] rows add their DOI at first use (in a table, in the Rows cell beside the row id); "(inference)" rows add "(inference)" every time.

| Rows | Cite as |
|---|---|
| EN-097 to EN-105 | HIPAA Security Rule, 45 CFR part 164 subpart C (eCFR, read 20 October 2026) |
| EN-106, EN-107 | HIPAA Security Rule NPRM, Federal Register 6 January 2025, and Unified Agenda RIN 0945-AA22 (proposal) |
| EN-108 to EN-113 | GDPR, Regulation (EU) 2016/679 |
| EN-114, EN-115, EN-120 | 42 CFR Part 2 final rule, Federal Register 16 February 2024 |
| EN-116 to EN-119 | 42 CFR Part 2 (eCFR, read 20 October 2026) |
| EN-121 to EN-128 | Washington My Health My Data Act, RCW 19.373 |
| EN-129, EN-130 | HL7 FHIR R5 and R4 home pages, read 20 October 2026 |
| EN-131 | HL7 FHIR package list, read 20 October 2026 |
| EN-132, EN-135 | HL7 US Core package list, read 20 October 2026 |
| EN-133, EN-134, EN-137, EN-141 | 45 CFR 170.215 (eCFR, read 20 October 2026) |
| EN-136, EN-138 to EN-140 | HL7 SMART App Launch 2.2.0 pages, read 20 October 2026 |
| EN-142 to EN-146 | 45 CFR 170.315 (eCFR, read 20 October 2026) |
| EN-147, EN-149 | HTI-1 final rule, Federal Register 9 January 2024 |
| EN-148 | 45 CFR 170.213 (eCFR, read 20 October 2026) |
| EN-150 | HTI-2 withdrawal, Federal Register 29 December 2025 |
| EN-151 | Unified Agenda RIN 0955-AA09 (HTI-5 proposal), read 20 October 2026 |
| EN-152 to EN-158 | CMS-0057-F final rule, Federal Register 8 February 2024 |
| EN-159 | CMS drug prior authorization proposed rule, Federal Register 14 April 2026 (proposal) |
| EN-160 | TEFCA final rule, Federal Register 16 December 2024 |
| EN-161 to EN-163 | 45 CFR part 172 (eCFR, read 20 October 2026) |
| EN-164 to EN-170, SP-068 to SP-073 | Regulation (EU) 2025/327 (European Health Data Space) |
| EN-171, EN-172 | SNOMED International "Get SNOMED CT" page, read 20 October 2026 |
| EN-173, EN-174 | LOINC license page, read 20 October 2026 [WF] |
| EN-175, EN-176 | WHO ICD-11 license |
| EN-177 | 45 CFR 162.1002 (eCFR, read 20 October 2026) |
| EN-050, EN-051 | FDA premarket cybersecurity guidance, 3 February 2026 |
| DA-94 to DA-98 | Kahn et al., eGEMs 2016, DOI 10.13063/2327-9214.1244 |
| DA-99 to DA-101 | Wilkinson et al., Sci Data 2016 (FAIR), DOI 10.1038/sdata.2016.18 |
| DA-102 to DA-106 | OHDSI OMOP CDM documentation, read 20 October 2026 [SPEC] |
| DA-107 to DA-110, DA-112 | ONC USCDI page (healthit.gov), read 20 October 2026 |
| DA-111 | 45 CFR 170.213 (eCFR, read 20 October 2026) |
| CP-US-44 to CP-US-49 | HIPAA, 45 CFR 160.103, 164.504, 164.314 and 164.410 (eCFR, read 19 October 2026) |
| CP-US-50 to CP-US-53 | Information blocking, 45 CFR part 171 (eCFR, read 19 October 2026) |
| CP-US-54 | FTC Health Breach Notification Rule, 16 CFR part 318 |
| CP-UK-01 to CP-UK-04 | NHS England DTAC guidance pages, read 19 October 2026 |
| CP-UK-05 | Health and Social Care Act 2012, section 250 |
| CP-UK-06 to CP-UK-10 | NHS AI and Digital Regulations Service, DCB0129 and DCB0160 pages, read 19 October 2026 |
| CP-UK-11 | NHS AI and Digital Regulations Service blog (not the standard) |
| UX-US-54 to UX-US-59 | 45 CFR 170.315(b)(11) (eCFR, read 19 October 2026) |
| UX-US-60 to UX-US-63 | HTI-5 proposed rule, Federal Register 29 December 2025 (proposal) |
| CS72, CS73 | ONC SAFER Guides page, read 19 October 2026 |
| CS74 | 42 CFR 495.24 (eCFR, read 19 October 2026) |
| PL89 | DiGAV (gesetze-im-internet.de), read 20 October 2026 |
| Saved library output | "library, saved DATE" plus the file in `examples/live/` |
