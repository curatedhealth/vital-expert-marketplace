# A1 Equity evidence

Framework task: DH-02.03.4.2, Part A, task A1. Replaces the earlier "Equity evidence" section (CF-12.02.03.4.2.1).

## What this task delivers

An evidence definition the person can count against: the change, the group, the record that shows the group used it, the denominator, the period, and (optionally) the outcome among those reached, with every field that the person's systems do not record marked `[GAP]`. It answers "what would show that the change reached the group?"

Why it matters: without a record of use and a denominator there is no rate, and without a fixed definition every review measures something different. The register's rules: name the change and the group, name the record, set the period, and never use a policy statement as evidence.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.03.4.2 Part A, Equity evidence |
| Workflow | The steps below |
| Knowledge | `references/equity-measures.md`; `references/equity-frames.md`; PE rows |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/equity-evidence-output.md` |
| Input | The request and its context: the change and version (from the design skill's B1 if present), the group and the field that records it, the systems that log use, the outcome the person cares about, their small-cell rule |
| Governance | `references/governance.md`; every definition is the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: a record and a denominator, defined before the numbers

The model proposes the shape; the person fixes each field. Anything not logged is `[GAP]` with the change to logging that would fill it. A policy, a release note, a translated listing or app availability is not evidence of reach.

## Read the request

- **Change and version.** What shipped and when. If the design skill's B1 wrote an evidence definition, start from it.
- **Group.** The subgroup and the field that records it (for example preferred language at registration). Ask how "not recorded" is coded.
- **Record of use.** The event that counts as reached.
- **Denominator.** Who was eligible in the period.
- **Period.** Start and end dates.
- **Outcome.** Optional; the person's outcome and how it is measured.
- **Other dimensions.** Age, area band (SVI), others the person wants to compare at the same time.

## Workflow

### Step 1. Write the five fields

Fill change, group, record of use, denominator and period in the person's words. Use `references/equity-measures.md` for the shape. Offer the register examples for the record (completed task, supported site, language used) if the person has none.

### Step 2. Separate reach from outcome and from attrition

If the person wants more than reach, add the outcome among those reached (effective engagement, PE-104 [PAPER], abstract only, doi:10.1016/j.amepre.2016.06.015) and say which attrition the record captures: dropout or nonusage (PE-102). One record per measure.

### Step 3. Check each field is recorded

For each field, mark: recorded (where), recorded only in part (where not), not recorded `[GAP]`. For not recorded, name the logging change that would fill it and route the change to the product owner; do not estimate. Where the change is a language flow, add a mismatch check, labeled proposed: the count in the group who completed the step in a different language flow. A high count points to measurement or routing, not to the change.

### Step 4. Counting rules

Write: how people entering mid-period are counted, how "not recorded" is reported (as its own row, never redistributed), the small-cell rule (the person's; `[GAP]` until given), and the reference group for comparison (the person's).

### Step 5. Rows that touch the definition

Only where they apply: DAP disaggregation by age group, sex, racial and ethnic characteristics, optionally geography and socioeconomic status, if the measure will feed a clinical study (PE-37; status in `equity-frames.md`); SVI U.S. versus state database (PE-123) if area bands are used; Section 1557 language-access duty if the change is language help (PE-107), with applicability left to the legal owner.

## Build the output

Follow `assets/equity-evidence-output.md`. Answer first: the definition in one sentence ("Reached = X among eligible Y in period Z") and the fields not yet recorded. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every field is the person's, or marked as offered and not yet chosen.
- Denominator and period are present, or `[GAP]` with the consequence (no rate).
- No policy, listing or release note used as evidence.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Defines the measure; computing it is A2; judging it is B1.
- Accessibility conformance measures belong to the dh-user-experience accessibility skills.
- KPI frameworks and dashboards in general are DH-02.03.3.x.
