# A1 Outcome and signal plan

Framework task: DH-02.02.3.1, Part A, task A1. Replaces the earlier "Health signal list" section.

## What this task delivers

A measurement plan for one customer (or a standard plan for a segment the person names): the outcomes the customer agreed to see, the usage and outcome signals that will show them, each with a sourced definition, its denominator, the product field or report that holds it, the period, and the person's target. It answers "what will we measure to know this customer is getting what they bought, and how?"

Why it matters: CFIR asks that "goals and measures for implementation success" be defined in advance (CS20), and NICE asks for usage reporting against an "expected usage profile (to be agreed at commissioning)" (CS61). A health number defined after the results are in can be bent to fit them.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.3.1 Part A, Outcome and signal plan |
| Workflow | The steps below |
| Knowledge | `references/outcome-measures.md`; `references/health-signals.md`; `references/customer-success-research.md` |
| Tools | Optional: `literature.search_literature` or `literature.get_record` (counted) for an instrument paper the person names; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/outcome-and-signal-plan-output.md` |
| Input | The request and its context: the customer and its population, the outcomes it agreed to see (contract, success plan, commissioning note), the product's data dictionary or list of stored fields, any targets the person has |
| Governance | `references/governance.md`; signals and targets are the person's; uptake is not clinical evidence |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **Customer and setting.** Who the customer is (health system, employer, payer, clinic group) and its eligible population, in the person's words. The eligible population is the reach denominator (CS27).
- **Agreed outcomes.** What the customer was told it would see. If nothing was agreed, say so: the plan then proposes, labeled "proposed", and the person confirms with the customer.
- **Stored fields.** What the product actually records. A signal the product cannot produce is dropped (register starter rule, `health-signals.md`).
- **Payment link.** If any outcome is tied to payment, the payment part goes to Market Access `outcomes-contract-monitoring`; this plan keeps only the customer success view.
- **Mode.** Short for a direct question; full for a success-plan appendix.

## Workflow

### Step 1. Fix the frame

Write back: customer, setting (inner and outer setting in CFIR terms, CS12), eligible population, agreed outcomes, period, and whether any outcome is payment-linked. Confirm before building.

### Step 2. Map each agreed outcome to measure families

For each outcome the customer wants to see, pick the measure family from `references/outcome-measures.md` and name the definition used: reach (CS22), setting or staff adoption (CS24, CS28), penetration (CS39), use or fidelity (CS25, CS37), effectiveness (CS23), maintenance (CS26, CS30). One definition per measure. If the customer wants to see an effect on health, add the effectiveness measure and its limits: without a comparator, a moved score is not evidence the product moved it (CS32).

RE-AIM effectiveness includes "potential negative effects, quality of life, and economic outcomes" (CS23). Ask whether the customer wants a negative-effect signal (for example, scores that worsened); record the answer.

### Step 3. Choose instruments only from the sourced set

For patient-reported outcomes use instruments the person or customer names. State what is sourced: PHQ-9 bands 5, 10, 15, 20 (CS92); GAD-7 items and accuracy but no cut point (CS93, `[GAP]`); PAM stages but no level cut points, scoring licensed (CS94, CS95, `[GAP]`). A change threshold (for example "5-point drop") is the person's, or an ACCESS rule the person chooses to borrow (CS89, CS90), labeled with its origin and period (CS84).

If the person names an instrument paper not in the rows, call `literature.search_literature {query: "<instrument> validation", limit: 5}` or `literature.get_record {doi}` to identify it. Do not take a cut point from a search result; mark it `[GAP]` until a full text is read.

### Step 4. Write each signal

For each signal record: name in the person's words, kind (uptake, use, setting adoption, outcome aggregate, data completeness, service, economic: `health-signals.md`), definition and row, numerator, denominator and its basis, product field or report that holds it, period, source type (product log, customer report, PROM aggregate, survey), and the person's target with direction. Apply the register starter rules only if the person adopts them: drop a signal the product does not store; do not use a survey as the only signal where usage data exist.

Add a data completeness signal beside every outcome share (for example "starters with a follow-up score"): an outcome share without it cannot be read (`outcome-measures.md`, denominators).

### Step 5. Targets and the health rule

Ask for a target per signal and a health rule (all listed signals met, at least N met, or none). Do not propose numbers. If the person asks for a starting point, offer only what the sources give as context, labeled: the ACCESS 50 percent attainment threshold applies to a payment model (CS85); RE-AIM's 6-month maintenance window (CS26, CS30). Record the version and date of the targets: the monitoring sibling compares versions.

Write the plan into the target-file shape the script reads (`scripts/account_health.py` header) so A2 can run on it.

### Step 6. Agreement and review

Note how the plan is agreed and reviewed, from the sourced practices: written commitment from the customer (CS49), the blueprint's performance measures kept updated (CS42), audit and feedback over a specified period (CS44). The forum, cadence and owner are the person's.

## Build the output

Follow `assets/outcome-and-signal-plan-output.md`. Answer first: the signals that will show each agreed outcome, and the gaps (signals not stored, targets not set, instruments without sourced cut points). Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every definition carries a CS row; every target, rule and owner is the person's and says so.
- Every outcome share has its denominator basis and a completeness signal.
- No GAD-7 band, PAM level or PHQ-9 change threshold from memory.
- The label "uptake, use and customer-reported outcomes are not clinical evidence" appears once.
- Payment-linked outcomes are routed to `outcomes-contract-monitoring`.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Measurement design for customer success only. Study design and endpoints for clinical evidence are dh-clinical-development; payment-linked outcomes are dh-access-and-value.
- Reading accounts against the plan is A2; whether thresholds still fit over time is the monitoring sibling.
- No patient-level data.
