# Data completeness: what goes missing, and what that does to attainment

Interpretive reference for task A2. Rows cited as in `attainment-rules.md`. Read on 19 October 2026. Not owner-reviewed.

## The checks

| Check | What to count | Sourced rule that makes it matter |
|---|---|---|
| Baseline present and on time | Patients with a baseline value; days from start to baseline | ACCESS: baseline due within 60 days of alignment via the CMS API, or the patient is unaligned (OC United States "ACCESS: verification data") |
| Final value present and in window | Patients with an end-of-period value; values taken after the window; patients already on target who could submit early | ACCESS: end-of-period values no later than day 425 from alignment; BH and MSK may submit up to 180 days before day 365 (OC "ACCESS: quarterly timeliness and early success reporting") |
| Value still valid | Days between collection and submission for BP, weight and PROMs | ACCESS: valid only within 15 days of collection (same row) |
| Self-reported values | Final values reported by the patient, per measure | ACCESS: self-report not allowed except weight and PROMs (same row) |
| Lost to follow-up and unaligned | Patients who stopped, vanished or unaligned, and the reason for each unalignment | ACCESS: they stay in the denominator (OC "ACCESS: all-or-nothing per patient"); patients who relocate outside the licensed service area or become ineligible leave the numerator and denominator (OC "ACCESS: denominator exclusions") |
| Required measures with no data column | Measures the track requires that the data does not carry | ACCESS BH: PGIC success is submission of the end-of-period measure (OC "ACCESS: PGIC, submission-only measure, Table 5") |
| Voluntary questionnaires | Share of patients who answered PROM and satisfaction items | DiGA AbEM: participation voluntary; questionnaires uniform and not steering; one reminder allowed (OC Germany "AbEM: voluntary patient participation") |
| Denominators | Redeemed prescriptions and direct repeat prescriptions per quarter; quarter by code activation date; repeat prescriptions excluded from reported results | DiGAV § 23b and BfArM guide (OC Germany "AbEM: denominators for monitoring"; DE-18) |
| Scope | Whether the product is in AbEM scope at all (permanent DiGA; PROMs not required for structure-and-process-only benefit; self-payer data excluded) | DE-17 |

## What missing data does under each rule family

| Rule family | Missing value treated as | Effect on attainment |
|---|---|---|
| Patient level, all-or-nothing (ACCESS pattern) | Failure; lost patients stay in the denominator | Every missing value lowers the rate. Completeness and outcome are inseparable. |
| Patient level, missing excluded | Patient leaves the denominator | The rate describes completers only and can look better than the cohort |
| Population average | Value drops out of the average | Selective dropout (patients doing badly leave) can raise the average |

The A2 output always shows the rate both ways: under the contract's rule, and under the other treatment of missing data. The gap between them is what completeness is worth under this contract. `scripts/attainment.py` prints both.

## Self-report limits

Self-reported values are cheaper to collect and are allowed for PROMs and weight in ACCESS; clinical measures such as blood pressure need non-self-reported values there (OC "ACCESS: verification data"). A contract that pays on a self-reported measure carries a verification question; record who checks it (`contract-structuring` term section 6 in the sibling skill).

## Known problem behind all of this

The OECD lists the difficulty of getting informative outcome data, and the administrative burden of collecting it, among the main weaknesses of performance-based agreements (OC Method guidance "OECD: known problems"). A completeness problem found in monitoring is evidence for that design question, and routes back to the contract design (DH-03.01.1.1).
