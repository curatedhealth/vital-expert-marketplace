# Attainment rules: how a contract turns outcomes into a payment

Interpretive reference for tasks A1 and B1. Rows: `OC` = `outcomes-contracting-sources.md` by table and topic; `DE-` = `access-monitoring-sources.md`; `US` = the coding and pricing research pass (cited, quotes below). Read on 19 October 2026. Not owner-reviewed.

The contract's own rules always decide. This file describes the two families of rules found in the sources, so the tracking method can match whichever one the person's contract uses.

## Family 1: patient-level, all-or-nothing (the ACCESS pattern)

| Rule | ACCESS value | Row |
|---|---|---|
| Unit of success | A patient succeeds only if every required measure is reported on time and met; partial attainment is not success | OC United States "ACCESS: all-or-nothing per patient" |
| Missing data | Failure to submit a valid required measure in the end-of-period window is non-attainment | same |
| Dropouts | Patients who unalign or are lost to follow-up stay in the denominator | same |
| Exclusions | Beneficiaries who relocate outside the participant's licensed service area or become ineligible during the care period leave the numerator and denominator; those who initiate unalignment stay in | OC "ACCESS: denominator exclusions" |
| Submission-only measures | BH: PGIC, where success is submission of the end-of-period measure; a missing PGIC fails the patient (PGIC is not marked optional, and only optional measures leave attainment untouched) | OC "ACCESS: PGIC, submission-only measure, Table 5" |
| Example targets | PHQ-9 5-point reduction if baseline 10 or more, else final under 10; GAD-7 4-point reduction if baseline 10 or more, else final under 10; systolic BP below 130 mm Hg or 15 mm Hg reduction; 5 percent weight loss | OC "ACCESS: outcome measures"; OC "ACCESS: BH targets by baseline, Table 5" |
| Below the baseline cut-off | Control target: final PHQ-9 under 10, final GAD-7 under 10; a patient under 10 on both is not eligible for the BH initial period. A contract that drops the measure instead differs from ACCESS: say so and compute both ways | OC "ACCESS: outcome measures"; OC "ACCESS: BH initial-period eligibility, Table 5 notes" |
| Threshold | Full payment if at least 50 percent of aligned patients succeed | OC "ACCESS: attainment threshold"; US33 |
| Below threshold | (attainment rate / 50 percent) x full payment; reduction capped at 50 percent | same |
| Second adjustment | Substitute spend: cut if fewer than 90 percent avoid listed substitute services, capped at 25 percent; only the larger of the two adjustments applies per semi-annual reconciliation | OC "ACCESS: substitute spend adjustment"; US33 |
| Timing and dollar basis | 50 percent of the Medicare portion withheld and reconciled after the 12-month care period. The Medicare portion is 80 percent of the allowed amount (BH initial: $144 of $180; withhold $72). The factor applies to the Medicare paid amount, never to the allowed amount | OC "ACCESS: withhold"; OC "ACCESS: Medicare portion and payment basis"; US32 |
| Payment-relevant data | End-of-period values decide each measure; quarterly values are not used for payment, but timely submission of all required quarterly measures is considered in calculating the attainment rate: ask for quarterly timeliness per patient | OC "ACCESS: verification data"; OC "ACCESS: quarterly timeliness and early success reporting" |

What follows for monitoring: under this family, every missing value is a lost success, including a missing PGIC submission on BH. Ask for the reason behind every unalignment: relocation and ineligibility leave the denominator, self-initiated unalignment stays in. Data completeness is part of attainment, not a separate quality topic. Near the threshold, one lost patient can change the payment.

## Family 2: population-level (average change or share meeting a target)

The sources give no published digital contract with a population-average rule; the OECD names population-level coverage with evidence development as one of the two most common performance designs for medicines (OC Method guidance "OECD MEA taxonomy"). A population rule compares an average (mean change, share improved) with a target. Missing values usually drop out of the average rather than count as failures, so selective dropout can raise the average. Say this whenever a population rule is tracked.

## Germany: the outcome-linked DiGA price component

- At least 20 percent of the negotiated DiGA amount must be outcome-dependent since 1 January 2026 (OC Germany "DiGA outcome-linked price share"; DE-19).
- No framework method sets how attainment is measured or paid: the latest listed framework agreement says "can" and leaves successes to the parties; how AbEM feeds the component is still to be set (OC Germany framework rows; DE-19). Track against the rules in the person's own agreement, and say the method is the parties', not a national one.
- AbEM data arrives twice a year: Q1 and Q2 by 15 October, Q3 and Q4 by 15 April; first report 15 April 2027 (OC Germany "AbEM reporting cadence"; DE-18). A contract that pays on AbEM cannot be reconciled before then.

## Attainment is not clinical evidence

ACCESS publishes risk-adjusted outcomes (OC "ACCESS: public reporting"), and the OECD notes that payment-by-result data are often not aggregated into evidence (OC "OECD: known problems"). Contract attainment uses the contract's population, windows and rules, without a comparator. Report it as attainment under the contract, never as proof that the product works.

## Rows cited from the coding and pricing research pass

| Row | Source URL | Verbatim quote | Read on |
|---|---|---|---|
| US32 | https://www.cms.gov/priorities/innovation/files/access-payments-amts-perf-targets.pdf | "The sum of monthly payments may not exceed 50 percent of the Medicare portion of the annual OAP allowed amount. The remaining 50 percent will be withheld and reconciled after the 12-month care period concludes" | 19 October 2026 |
| US33 | same | "During the Effective Period, the OAT will be 50 percent for all ACCESS Participants." / "During the Effective Period, the SST will be 90 percent for all ACCESS Participants." | 19 October 2026 |
