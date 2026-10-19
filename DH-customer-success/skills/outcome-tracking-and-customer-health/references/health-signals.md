# Health signals, the person's rules, and the register starter rules

Interpretive reference for tasks A1 and A2 and B1. Rows are CS rows in `customer-success-research.md`.

## What is sourced and what is the person's

No primary or peer-reviewed source in the research pass defines a customer health score, renewal rate, net or gross revenue retention, churn, expansion, time-to-value or NPS as a renewal predictor (research "Not sourced"). So:

- The signals that mean "healthy", their targets, their period, any weighting and the rule that turns signals into a health status are the person's, labeled owner-stated (O).
- The skill brings sourced definitions for the measures underneath (reach, adoption, penetration, effectiveness, maintenance: `outcome-measures.md`) and sourced practices for agreeing and reviewing them (below).
- No score, color or average across signals unless the person defines one. "Health" without a rule is a list of signals met and missed.

## Sourced practices for setting signals with a customer

| Practice | What the source says | Row |
|---|---|---|
| Define measures in advance | CFIR process construct Planning: "define goals and measures for implementation success in advance" | CS20 |
| Put measures in the plan | ERIC implementation blueprint has four parts, including "appropriate performance/progress measures"; use and update it over time | CS42 |
| Agree the usage profile with the customer | NICE ESF Standard 16: usage "in line with the expected usage profile (to be agreed at commissioning)" | CS61 |
| Get it in writing | ERIC: "Obtain written commitments from key partners that state what they will do" | CS49 |
| Review with data | ERIC audit and feedback: collect and summarize performance data "over a specified time period" and give it to clinicians and administrators | CS44 |
| Relay data close to real time | ERIC: provide "as close to real-time data as possible about key measures of process/outcomes" | CS49 |
| Make CFIR project-specific first | CFIR 2022 "must be fully operationalized prior to use in a project" | CS11 |
| Separate deployment from product | Implementation outcomes are preconditions for clinical or service outcomes | CS32 |

## Signal kinds the skill keeps apart

| Kind | Example (the person's words) | Can show | Cannot show |
|---|---|---|---|
| Uptake | Eligible members who activated | Reach, if the denominator is the eligible population (CS22, CS27) | Clinical effect |
| Use | Activated members active in the last 90 days | Individual-level implementation, "clients' use" (CS25) | Clinical effect |
| Setting adoption | Clinics live of clinics contracted | Adoption at setting level (CS24, CS28) | That staff deliver with fidelity |
| Outcome aggregate | Share of starters with a 5-point PHQ-9 drop | That measured scores moved in this population | That the product caused it; no comparator |
| Data completeness | Share of starters with a follow-up score | Whether an outcome share can be read at all (CS87 logic) | Outcome |
| Service | Usage reviews held with the sponsor | That the review practice runs (CS44) | Value |
| Economic | Customer-reported cost figure | What the customer reports | A saving; any cost claim stops for the owner |

## The register starter rules (offered, never imposed)

The VITAL register's earlier task sections for this competency carried these rules. They are a document's assertions (evidence class V), not sourced law or research. Offer them; apply one only if the person adopts it, and say "rule you adopted".

| Register rule | Plain meaning | Script option |
|---|---|---|
| "Drop a signal the product does not store" | Every signal must come from a field that exists | Check in A1 against the person's data dictionary (NICE ESF Std 19 asks the company for a data dictionary, CS64) |
| "Do not use a survey score as the only signal if the product has usage data" | Pair a survey with a usage signal | A1 check |
| "Do not mark an account healthy when a day-one workflow is still open" | An open go-live item blocks a healthy status | `adopted_rules: ["day_one_open_blocks"]` |
| "Do not send a result you cannot trace to a signal" | Every value-note number has a signal row | B1 and the monitoring skill's value evidence check |
| "Do not send a value story to an account below every threshold" | Below all targets, the note is a next-action note | B1 |

## Data the person supplies

Aggregates per account, period and measure: numerator, denominator and its basis, or the value. Never patient rows, names or identifiers; HIPAA minimum necessary applies to PHI that does flow (CS103), and outcome reporting under NICE Standard 16 is "anonymised, aggregate" (CS61). The script's columns are in its header (`scripts/account_health.py`).
