# Outcome measures: what official sets exist, and how to judge a candidate

Interpretive reference for task A1. Every fact cites its row: `OC` rows are in `outcomes-contracting-sources.md` (named by table and topic, because that file has no row ids), `DE-` rows are in `access-monitoring-sources.md`. Read on 19 October 2026. Not owner-reviewed.

## Germany: what DiGA outcome measurement (AbEM) collects

AbEM is the statutory outcome measurement for DiGA. It is the only official German measure set a DiGA outcome-linked price component can point to today, and the framework agreement does not yet say how it should be used (see `risk-share-models.md`).

| Field | What it is | Stage and start | Row |
|---|---|---|---|
| Usage duration and frequency | Data on how long and how often the DiGA is used | Stage I, collected from 1 July 2026 | DE-18; OC Germany "AbEM content (payer description)" |
| Recommended use | Recommended weekly minutes, weekly frequency, minimum and maximum duration of use | Reported each quarter | OC Germany "AbEM: denominators for monitoring" (DiGAV § 23b) |
| Redeemed prescriptions and direct repeat prescriptions | Denominators; repeat prescriptions are excluded from reported results; quarter follows the code activation date | Every report | DE-18; OC Germany "AbEM: denominators for monitoring" |
| Patient satisfaction | Satisfaction with quality | Stage II, 2027 | DE-18 |
| Single-item PROM | Patient-reported health status on a one-item score | Stage II, 2027 | DE-18 |
| Indication-specific PROMs | Health status on indication-specific instruments | Stage III, 2028 | DE-18 |

Limits that matter for a contract measure:

- **Scope.** Only DiGA with a permanent-listing decision report AbEM. Trial-listed DiGA do not. PROM data is not required where benefit was shown only through structure and process improvements. The BfArM guide narrows scope further and excludes self-payer data. The two sources may not describe the same set (DE-17; OC "Changes and conflicts", scope limit).
- **Participation is voluntary.** Patients choose whether to answer satisfaction and PROM items; questionnaires must be uniform and not steer answers; one reminder is allowed (OC Germany "AbEM: voluntary patient participation"). Expect missing PROM data; it is not a defect of the product.
- **Cadence.** Collected per calendar quarter, reported twice a year (Q1 and Q2 by 15 October; Q3 and Q4 by 15 April), first report by 15 April 2027 (OC Germany "AbEM reporting cadence"; DE-18).
- **Publication.** BfArM publishes results once a manufacturer has first sent usage data from at least 200 users for a quarter (DE-16).
- **Which instruments.** The single-item PROM and the indication-specific PROMs are not named in the sourced rows `[GAP]`. Do not name an instrument as "the AbEM PROM" for an indication.

## United States: ACCESS model outcome measures

ACCESS is the first CMS model that pays technology-supported chronic care on outcomes. It pays Part B enrolled care organizations, not device or software makers (OC United States "ACCESS: who is paid").

| Measure (examples sourced) | Target | Row |
|---|---|---|
| Systolic blood pressure | Final systolic BP below 130 mm Hg, or a 15 mm Hg reduction | OC United States "ACCESS: outcome measures" |
| PHQ-9 (depression) | If baseline PHQ-9 is 10 or more: 5-point reduction; if under 10: final PHQ-9 under 10 (control target) | same; OC "ACCESS: BH targets by baseline, Table 5" |
| GAD-7 (anxiety) | If baseline GAD-7 is 10 or more: 4-point reduction; if under 10: final GAD-7 under 10 (control target) | same; OC "ACCESS: BH targets by baseline, Table 5" |
| PGIC (BH) | No target; success is submission of the end-of-period measure. Not marked optional, so a missing PGIC fails the patient | OC "ACCESS: PGIC, submission-only measure, Table 5" |
| Weight | 5 percent weight loss | same |

A patient under 10 on both PHQ-9 and GAD-7 at baseline is not eligible for the BH initial period (OC "ACCESS: BH initial-period eligibility, Table 5 notes"). Patients who relocate out of the participant's licensed service area or become ineligible leave the attainment numerator and denominator (OC "ACCESS: denominator exclusions"). The full measure list for the eCKM, CKM and MSK tracks is not in the sourced rows `[GAP]`; read the CMS payment amounts and performance targets PDF before using a track's full set.

Rules that shape every ACCESS measure (OC United States "ACCESS: all-or-nothing per patient" and "ACCESS: verification data"):

- A patient counts as a success only if every required measure is reported on time and met. Missing a measure is a failure. Patients lost to follow-up stay in the denominator.
- Baseline is due within 60 days of alignment via the CMS API, or the patient is unaligned. End-of-period values are due no later than day 425.
- Self-reported values are not allowed except weight and PROMs. BP, weight and PROMs are valid only within 15 days of collection.
- Quarterly values are for monitoring only, not payment.

## England and France

No outcome-linked payment for digital devices was found in England: the MedTech Funding Mandate pays on cost and volume and asks only that outcomes be recorded (OC England, both MedTech rows, [WF]). In France, the historical ETAPES telemonitoring scheme paid the supplier a performance bonus in year N+1 (OC France "ETAPES telemonitoring"); the measure behind that bonus is not in the sourced rows `[GAP]`, and no current French outcome-linked payment for digital devices was confirmed (OC "Not sourced").

## How to judge a candidate measure

Five properties, each written for the person with the facts. None is scored by the model.

| Property | The question | Why it matters (source) |
|---|---|---|
| Measurable | Is there a defined instrument, unit and time window? | OECD lists difficulty getting informative outcome data and validated surrogate endpoints as a known weakness (OC Method guidance "OECD: known problems") |
| Attributable | Could the change come from something other than the product (other care, regression to the mean, selection)? | ISPOR: study design must match the uncertainty addressed (OC Method guidance "ISPOR: cost of evidence and design fit") |
| Named data source and owner | Who collects it, in which system, and who hands it over? | OECD design question: are data sources available for the outcome in the population of interest? (OC Method guidance "OECD: design questions") |
| Collection burden | What does collection cost the patient, the provider and the payer? | OECD names administrative burden and data collection cost first among known problems (OC Method guidance "OECD: known problems") |
| Baseline need | Does the measure need a baseline value, and how soon after start? | ACCESS requires baseline within 60 days or the patient is unaligned (OC United States "ACCESS: verification data") |

Attribution risk and burden are judgments. Lay out the facts that bear on them; the person rates them.
