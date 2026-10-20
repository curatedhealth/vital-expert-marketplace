> Shared origin: copied from payer-engagement-and-hta-submission/references/readiness-checklists.md (19 October 2026), where it serves submission readiness. Here it is the checklist a draft dossier is checked against.

# Submission readiness: checklists, fees, clocks and failure patterns

Checklist reference for A1 and B1 in this skill (in the preparation skill it serves A2, submission readiness). Every line cites a row in `hta-submissions-sources.md` or a topic row in `requirements/<file>.md`. Read on 19 October 2026; not owner-reviewed. A checklist item is a fact about what the body asks for. Whether the person's material is good enough is the person's judgment.

## Germany: DiGA application to BfArM

**Formal completeness items** (the file is incomplete without them)

| # | Item | Row |
|---|---|---|
| D1 | Application through the electronic BfArM portal only | `DE29` |
| D2 | gematik TI confirmation (ePA writing and GesundheitsID) for new applications: a condition of formal completeness | `DE29`; `requirements/germany-diga.md` "Interoperability: gematik confirmation" |
| D3 | BSI data-security certificate: since 1 July 2025 a condition of formal completeness | `requirements/germany-diga.md` "Data security: TR-03161 and completeness" |
| D4 | Free access to the DiGA for BfArM; directory-bound statements in German | `DE4` |
| D5 | Choice of permanent or provisional (trial) listing stated | `DE4` |
| D6 | The 24 content items of DiGAV § 2 Abs. 1. Check each: manufacturer and product identifiers; intended purpose; notified body; instructions for use; EU AI Act compliance where applicable (D8); plain-language description; functions; medical content sources; PICO summary; patient groups as ICD-10-GM codes; positive care effects by type; studies or data analyses; diagnostic-accuracy studies; independent evaluating institution; compliance with DiGAV §§ 3 to 6; user roles; required physician services; minimum use duration; data-processing locations; interoperability standards; liability insurance cover; actual prices | `DE3`, `DE9` |
| D7 | For trial listing: systematic data analysis of use, and an evaluation concept by a manufacturer-independent institution with the study protocol and analysis plan | `DE18`, `DE19`, `DE20` |
| D8 | EU AI Act compliance statement where applicable | `requirements/germany-diga.md` "Eligibility: AI Act" |
| D9 | Data protection proof (statute: certificate; BfArM practice: self-declaration until BfArM sets a deadline) | `requirements/germany-diga.md` "Data protection: certificate (statute)", "(BfArM practice)" |

**Fees** (DiGAV § 25 to § 30)

| Decision | Fee range | Row |
|---|---|---|
| Permanent or trial listing | EUR 3,000 to 9,900 | `DE25` |
| Final listing after trial | EUR 1,500 to 6,600 | `DE25` |
| Trial extension | EUR 1,500 to 4,900 | `DE25` |
| Refused application | Up to the full fee | `DE26` |
| Withdrawal before completion | Up to 75 percent of the fee | `DE26` |
| Reduction | To one quarter possible for small target groups or low expected economic benefit | `DE26` |

**Clocks**

| Clock | Length | Row |
|---|---|---|
| Receipt of a complete file confirmed | 21 days in the ordinance; 14 days in BfArM's guide (practice) | conflict note 4 |
| Decision | Three months from a complete file, extendable by up to three more in justified cases | `DE21` |
| Completing an incomplete file | Up to three months, else refusal by formal decision | `DE22` |
| Objection (Widerspruch) | Within one month of notification | `DE24` |
| Re-application after refusal or withdrawal | Not before 12 months from the refusing decision or the withdrawal, only with new evidence; no second trial listing. Do not present it as the consequence of not objecting. | `DE23` |

Actual BfArM days to decision are not published: `[GAP]` (research file, "Not sourced").

**Official outcome statistics** (snapshot; BfArM updates the chart monthly)

As of 9 September 2026: 254 applications since 27 May 2020 (196 for trial listing, 58 for permanent listing) (`DE33`). Outcomes: 62 listed, 29 refused, 131 withdrawn, 14 in review, 18 delisted, 7 of them at the manufacturer's request (`DE34`). Withdrawals far exceed refusals, so a refusal-only rate understates failed applications (conflict note 9). These counts overlap (a delisted DiGA was first listed), so do not add them up to 254. BfArM does not say which manufacturers applied or which products were refused (`DE32`).

## France: CNEDiMTS

| # | Item | Route | Row |
|---|---|---|---|
| F1 | Medico-technical file to CNEDiMTS on the HAS template, and jointly medico-technical and economic files to CEPS | LPPR | `FR2` |
| F2 | "Complete" dossier: product description, clinical data selection, SA, prescribing conditions, ASA, target population. A "light" dossier only in listed situations | LPPR | `FR5` |
| F3 | Two templates (HAS part, ministers part) on the Sésame platform, plus a parallel ANS Convergence filing; class I devices first need an ANSM qualification opinion | PECAN | `FR15` |
| F4 | CE marking and an ANS interoperability and security conformity certificate for the device and any collection accessories | LATM | `FR16` |
| F5 | Two dossiers where the device is both therapeutic and telemonitoring | LPPR + LATM | `FR8` |
| F6 | Current guides: LPPR March 2026; PECAN guide 15 September 2026; PECAN and LATM pages updated 22 September 2026 | all | `FR2`, `FR13`, `FR18`; conflict notes 6, 7 |

**Fees.** HAS fee per LPPR or intra-GHS request: EUR 3,220 for listing, EUR 644 for renewal or modification. PECAN, PECT and LATM fees await a decree (`FR10`).

**Clocks.**

| Clock | Length | Row |
|---|---|---|
| LPPR regulatory timeline | 180 days from CEPS admissibility, suspended while requested information is awaited | `FR6` |
| PECAN opinion | 60 days from a complete file | `FR14` |
| PECAN missing information | 30 days, or the request is deemed abandoned | `FR14` |
| After a PECAN decision | 6 months to file for LPPR, 9 months for LATM | `FR14` |
| LATM opinion | 90 days maximum from a complete file; 70 days where the activity is under PECAN | `FR17`; `requirements/france-pecan-lppr-latm.md` "LATM evaluation: CNEDiMTS timeline" |
| Contradictory phase | 10 days to comment on the draft opinion or ask for a hearing | `FR19` |

**Official failure patterns.**

- 2025: 69 percent of LPP and intra-GHS requests (204 of 297) had at least one incompleteness suspension; 51 percent (153 of 297) for administrative reasons only; mean time to administrative completeness 49 days (`FR24`).
- January to April 2023 dossiers: 55 percent suspended, 86 percent of those for at least two causes, mainly device description, clinical data and missing vigilance data (`FR7`).
- Organizational impact claimed but not evaluated (`FR25`).
- 2025 outcomes, as context: CNEDiMTS recommended reimbursement for 214 products (91 percent of requests), with progress recognized for 41 (19 percent); LATM 8 favorable and 2 unfavorable opinions; PECAN 5 requests, 1 favorable and 4 unfavorable (`FR21`, `FR22`, `FR23`).

## England: NICE HealthTech

There is no dossier to complete. Readiness means being able to answer NICE's requests for information and evidence requests (`UK2`).

| # | Item | Row |
|---|---|---|
| N1 | Regulator-approved intended purpose (UKCA or CE); guidance covers only that purpose | `requirements/uk-nice-nhs.md` "HealthTech: regulatory approval" |
| N2 | Registered on the NHS Innovation Service; topic routed through NICE-wide prioritization | `UK9` |
| N3 | Evidence mapped to the ESF tier and its standards | `UK12`, `UK13` |
| N4 | Any economic model fully executable in standard software with full code access | `UK3` |
| N5 | Confidential-information checklist ready for every response | `UK3` |
| N6 | For early use: a credible plan to resolve key uncertainties within 3 years | `UK7` |
| N7 | MHRA registration before placing on the GB market | `requirements/uk-nice-nhs.md` "MHRA: registration" |

**Fees.** None for healthtech evaluations; NICE Advice is separate and fee-based (`UK9`).
**Clocks.** Scoping about 10 weeks; assessment typically 12 to 30 weeks; then committee, draft and final draft guidance (`UK5`).
**Failure pattern.** Missing information may affect the recommendation (`UK4`); early-use recommendations can be withdrawn, for example if the company is not engaging in evidence generation (`UK8`).

## United States: Medicare

| Item | Row |
|---|---|
| NCD request completeness: the formal letter and its listed contents (see `evidence-requirements.md`) | `US1` |
| NCD clock: proposed decision normally within six months of opening, 30-day comment, final within 60 days after comment close | `US2` |
| TCET capacity: up to five candidates a year; self-nomination about 12 months before expected FDA authorization | `US5` |

No fee is sourced for an NCD request: `[GAP]`.
