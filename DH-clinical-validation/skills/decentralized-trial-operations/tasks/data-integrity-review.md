# B1 Data integrity review

Framework task: DH-01.02.3.1, Part B, task B1 (old DH-01.02.3.1.3 Trial Data Integrity Management).

## What this task delivers

A readiness review of the trial's data controls, from first capture through lock: each control checked against the sourced requirement and against the critical-to-quality factors and acceptance rules the person sets; met, open or not assessable; who the person says owns each open item; and which item closes first because others depend on it. It answers "are our data controls ready for first participant, and what do we close first?"

Why it matters: ICH E6(R3) asks the sponsor to name critical-to-quality factors in advance and to set acceptable ranges for them (CV5, CVB3). Without them, every review argues about what "good enough" means after the data arrive.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.3.1 Part B, Data integrity review |
| Workflow | The steps below |
| Knowledge | `references/data-integrity-rules.md`; A1 and A2 outputs; rows CV5 to CV14, CV23, CV24, CV28, CV29, CV58, CV60, CV71, CV79, CV91, CV92, CV99, CV102, CV103, CVB2, CVB3, CVB5, CVB6 |
| Tool | None from the library. `scripts/capture_inventory_check.py` if A2 was run with an inventory |
| Catalogue job | None |
| Prompt | This guide |
| Template | `assets/data-integrity-review-output.md` |
| Input | The request and its context; the person's critical-to-quality factors, acceptance rules and named owners; evidence documents per control |
| Governance | `references/governance.md`; the person sets every rule and names every owner |

## The rule that shapes this task: people judge

The person names the critical-to-quality factors, the acceptable ranges and the readiness rule ("all controls for primary-endpoint streams met before first participant"), in their own words, and names an owner for each. The model checks evidence against those rules and the sourced requirements, finds what is open and what depends on what, and lays out options. It never sets a range, never decides readiness, never names an owner the person has not named. If asked to propose rules, it may, each labeled "proposed" with the row behind it, and does not apply them until confirmed.

## Workflow

### Step 1. Gather the evidence

Use A1 (elements, monitoring, contingency) and A2 (streams, source, flow) from the conversation. If A2 is missing and the review concerns DHT data, run A2 in short mode first. Ask for the documents behind each control.

### Step 2. Write the rules with the person

Ask for the critical-to-quality factors (CV29: attributes whose integrity is fundamental to participant protection and reliable results) and, per factor, the acceptance rule and owner. Offer this shape, filled with the person's words:

| Factor (person's words) | Control that protects it | Acceptance rule (person's) | Owner (person's) |
|---|---|---|---|
| "Primary endpoint step count" | System validation, audit trail, same method in both arms | "Validation summary signed before first participant" | "Data management lead" |

Write the rules back for confirmation before checking anything. A control without a rule gets a factual status and no verdict.

### Step 3. Check each control

Walk the 14-line checklist in `data-integrity-rules.md`. For each control tied to a factor: met (evidence seen, with the document named), open (evidence missing or incomplete, with what is missing), or not assessable `[GAP]`. Name the reliability vocabulary you apply (CV23, CV79 or CV91 and CV92) for the person's product and jurisdiction.

### Step 4. Deviation criteria and acceptable ranges

Check that the person has trial-specific criteria for important protocol deviations (CVB2) and, where relevant, acceptable ranges for the critical factors with an evaluation step when exceeded (CVB3). If they are missing, say so as an open item; do not write the criteria. These feed the sibling monitoring skill's review.

### Step 5. Find the dependency order

Order open items by what blocks what: for example, the data flow overview (CV102) comes before validation of interfaces (CV13), which comes before the audit-trail check on the transferred data (CV14). State the order as dependency, not as a schedule.

### Step 6. Route each open item

Name the owner the person gave. If no owner was named, write "owner not named" and ask. Route work outside this competency: device status or human factors to dh-regulatory-strategy; endpoint redefinition to the study design skill; running-trial monitoring to the trial operations monitoring skill.

## Build the output

Follow `assets/data-integrity-review-output.md`. Short mode: readiness against the person's rule, the open items that block it, their owners, and the first item to close. Full mode adds the rule table, the control checklist with evidence, and the dependency order.

## Before you hand it over

- Every rule, range and owner is the person's, and the output says so.
- Every "met" names its evidence document.
- The output never says the trial or a system is compliant, validated or inspection-ready.
- Record line present.

## Boundaries

- The model checks and structures; it does not certify, audit or sign.
- Computer system validation execution and QMS procedures: the quality packs (dh-quality).
- No forecast of inspection outcomes.
