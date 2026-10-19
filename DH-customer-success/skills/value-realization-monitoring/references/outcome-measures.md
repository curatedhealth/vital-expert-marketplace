Copied from the sibling skill outcome-tracking-and-customer-health (DH-02.02.3.1), 19 October 2026. Task names in this file refer to that skill; in this skill the same content serves A1, A2 and B1.

# Outcome measures and what each can show

Interpretive reference. Every rule cites a CS row in `customer-success-research.md` (research pass of 19 October 2026). Where a fact is not in a row, it is marked `[GAP]`. Targets are never taken from this file: they are the person's.

## The one rule that shapes everything here

A customer account shows use and outcomes in a customer's own population, without a comparator. Those figures can show that the product is reached, used and that measured scores moved. They cannot show that the product caused the change. Uptake, use and customer-reported outcome aggregates are not clinical evidence. The worker's own stop rule says the same: never treat "activation, login, or session time as a clinical endpoint or reimbursement proof" (expert download, `examples/live/agent_pack.json`).

Proctor et al. separate implementation outcomes from clinical and service outcomes, and treat implementation outcomes as preconditions: "implementation outcomes serve as necessary preconditions for attaining subsequent desired changes in clinical or service outcomes" (CS32). Read a poor outcome figure next to the implementation figures first: a failed deployment and an ineffective product look the same in an outcome number.

## Measure families and their sourced definitions

Pick one definition per measure and name it (research "Changes and conflicts": Proctor and RE-AIM overlap).

| Family | Definition to use | Denominator rule | Row |
|---|---|---|---|
| Reach | "absolute number, proportion, and representativeness of individuals who are willing to participate" | Valid denominator of eligible people, "not of volunteers who indicate interest" | CS22, CS27 |
| Adoption (setting or staff) | Number, proportion and representativeness of settings and delivery staff willing to start | Settings approached; staff invited | CS24, CS28 |
| Adoption (Proctor) | "intention, initial decision, or action to try or employ"; "also may be referred to as uptake" | Not set by the source | CS34 |
| Penetration | Eligible users who use the service divided by all eligible; or providers delivering divided by providers trained or expected to deliver | Stated in the source | CS39 |
| Implementation (fidelity, use) | Setting level: fidelity, consistency, time and cost; individual level: "clients' use of the intervention strategies" | Not set by the source | CS25, CS29, CS37 |
| Effectiveness | "impact of an intervention on important outcomes, including potential negative effects, quality of life, and economic outcomes" | Not set by the source | CS23 |
| Maintenance (setting) | Institutionalized in routine practice; checked as "still ongoing at ≥ 6 month post study funding" | 6 months is the source's window | CS26, CS30 |
| Maintenance (individual) | Long-term effects "after 6 or more months after the most recent intervention contact" | 6 months is the source's window | CS26 |
| Sustainability | Maintained or institutionalized in ongoing, stable operations (maps to maintenance) | Not set by the source | CS40 |

How this skill reads them for a customer: reach and penetration need the eligible population as the customer defines it; a share computed on enrolled or interested people is not reach (CS27). Effectiveness in RE-AIM includes negative effects and quality of life, so an outcome plan that lists only the hoped-for score is incomplete by the framework's own definition (CS23). The setting-level maintenance check is written for study funding; applying it to "implementation support ended" is this skill's analogy, labeled as such.

## Usage reporting agreed at commissioning (NICE ESF)

NICE Evidence Standards Framework (ECD7, published 10 December 2018, last updated 9 August 2022, CS56). Standard 16 asks company and evaluator to agree reporting on "ongoing usage of the DHT in the target population in line with the expected usage profile (to be agreed at commissioning)" and on "anonymised, aggregate data to show service user outcomes" where appropriate (CS61). For products that change over time, agree "how and when changes in performance should be reported and to whom" (CS62). Deployment standards apply to all three tiers (CS57).

What this gives the skill: the expected usage profile is agreed with the customer, not set by the vendor alone, and outcome reporting is anonymized and aggregate. It does not give any usage number or threshold `[GAP]`.

## Patient-reported outcome instruments

| Instrument | What is sourced | What is not sourced | Row |
|---|---|---|---|
| PHQ-9 | 9 items scored 0 to 3; cut points 5, 10, 15, 20 = mild, moderate, moderately severe, severe; a score of 10 or more gave 88 percent sensitivity and 88 percent specificity for major depression (Kroenke, Spitzer, Williams 2001, abstract) | A minimal clinically important difference; any change threshold from the 2001 paper `[GAP]` | CS92 |
| GAD-7 | 7 items; a cut point gave 89 percent sensitivity and 82 percent specificity (Spitzer et al. 2006, abstract) | The cut point value and severity bands: not in the abstract; full text returned 403 `[GAP]`. The library record (`literature.get_record`, PMID 16717171) returns the abstract opening only, without the results | CS93 |
| PAM | Four stages of activation (Hibbard et al. 2004); 13-item short form keeps the 22-item properties (2005) | Level cut points; scoring is licensed `[GAP]` | CS94, CS95 |

Rules that follow:

- Report PHQ-9 bands only with the 2001 cut points and the row. Never write a GAD-7 or PAM band or level from memory.
- A change threshold (for example "5-point drop") is the person's choice or the contract's. The only change thresholds in the sources are the CMS ACCESS ones below, which belong to that payment model.
- Rows CS92 to CS95 are [PAPER, abstract]: say so when a rule rests on them.

## CMS ACCESS: context only

ACCESS links payment to "measurable clinical and patient-reported outcomes" over an Effective Period of 5 July 2026 to 31 December 2027 (CS84). Its rules: full payment if at least 50 percent of aligned beneficiaries meet all required targets (CS85); each measure met by control or minimum improvement (CS86); partial attainment fails and lost-to-follow-up patients stay in the denominator (CS87); PHQ-9 baseline of 10 or more needs a 5-point reduction (CS89); GAD-7 baseline of 10 or more needs a 4-point reduction (CS90); scores 0 to 9 at baseline are not eligible for the Initial Period (CS91). CMS says it may update measures and targets (research "Changes and conflicts").

Use in this skill: a customer may choose to borrow an ACCESS-style rule for its own success plan; then say where the rule comes from and that it was written for a payment model. ACCESS's treatment of missing data (lost to follow-up stays in the denominator, CS87) is a useful honesty check on any outcome share. Where payment depends on outcomes (ACCESS participation, a risk-share or outcomes-based contract), stop and point to the Market Access skill `outcomes-contract-monitoring` (dh-market-access). Never compute a payment, withhold or reconciliation here.

## Outcome share denominators

The same data give different shares by denominator. In the illustrative Northfield cohort (`examples/sample-data/`, built from the illustrative 20-patient cohort of the outcomes-contract build), 11 of 20 who started with a baseline PHQ-9 of 10 or more had a 5-point or larger drop: 55 percent of starters, but 73 percent of the 15 with a follow-up score. Always state the denominator; prefer the starters, the way ACCESS keeps lost patients in (CS87); report follow-up completeness beside it.
