# A1 Reporting and reference-case check

Framework task: DH-01.07.2.2, Part A, task A1. Replaces the reporting half of the old "Model validity check" section (CF-12.01.07.2.2.1), whose rule stays: check the inputs already shown; do not replace a buyer input.

## What this task delivers

A findings table for one economic model: which sourced CHEERS 2022 items its documentation addresses and where, which reference-case elements of the deciding body it states and whether they match the body's written rules, and which rules it cites that have since changed or conflict. Each finding carries the line of the document it rests on and the HE row it is checked against. No score.

Why it matters: an HTA reviewer's first pass is a completeness and conformance read. A model valued with a retired value set, quoting one NICE threshold as a verdict, or silent on funding is sent back before anyone reads the results. Finding these before submission costs a paragraph; finding them after costs a cycle.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.2.2 Part A, Reporting and reference-case check |
| Workflow | The steps below |
| Knowledge | `references/validity-rules.md` sections 1, 3 and 4; `references/reference-cases.md`; `references/health-economics-methods-research.md` |
| Tools | `scripts/cheers_check.py` (optional); `verify.qualify_source` and `verify.check_claim` for a published source the model cites; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/reporting-check-output.md` |
| Input | The request and its context; the person's model description, methods section, report or technical document; the decision-maker the model is for |
| Governance | `references/governance.md` |
| Catalogue job | none |

## Read the request

- **What document?** A methods summary supports a reporting check only; a full report supports more. Say what was read. "Not found" in a summary is never "absent from the model".
- **Which decision-maker?** The reference-case check needs one. If not named, run the CHEERS part and ask which body.
- **BIA or cost-effectiveness?** A budget impact analysis is outside CHEERS (HE-003, DOI 10.1177/23814683211061097): check it against BIA II and, for NICE ESF, standard 17 (`validity-rules.md` section 3).
- **Short or full?** "Is our model CHEERS-complete", "anything NICE will bounce" gets short mode. "Full review", "pre-submission check" gets full mode.
- **A score asked for?** Decline the CHEERS score (HE-005, DOI 10.1177/23814683211061097) and offer the item table; a score only with a rule the person supplies (task B1).

## Workflow

### Step 1. Note what was read

Document name, version or date as the person gives it, sections present. Everything after is "in this document".

### Step 2. CHEERS 2022 items

For each item in `validity-rules.md` section 1, find the passage that addresses it and quote its location (section or line). With code execution, `scripts/cheers_check.py description.md` does the first pass; read every hit, because a keyword is not compliance (for example "the perspective is the NHS" addresses item 8 but may not match the body). Mark each item: addressed (with location), partly addressed (say what is missing against the item's own wording), or not found in this document. List the unsourced items as `[GAP]` with the checklist DOI. No total.

### Step 3. Reference-case conformance

For the named body, take each element from `reference-cases.md` (perspective on costs and outcomes, form, outcome and value set, horizon, discount rate and exceptions, threshold as written, budget impact rule) and set the model's stated choice beside the rule with its row. Mark match, differs, or not stated. A difference is a finding, not an error: the body may accept a justified non-reference-case analysis kept separate (HE-035). With code execution, `scripts/cheers_check.py description.md --body NICE` (or HAS, IQWIG, ICER, ICER-PHTI) lists candidate lines.

### Step 4. Rule currency

Run the model against `validity-rules.md` section 4: 3L value sets in a new NICE topic (HE-058, HE-061), a single NICE threshold or verdict wording (HE-049, HE-050, HE-051, HE-074), a horizon justified only by trial follow-up (HE-040, HE-007, DOI 10.1177/23814683211061097), default plus or minus 20 percent ranges (`references/tools.md`), old manual titles (HE-033), EVA (HE-067), the old NICE budget impact figure (HE-055), CHEERS 2013 (HE-001), productivity costs in a NICE base case (HE-038), 1.5% discounting (HE-048), AMCP draft rows cited as final (HE-131). Each hit is a finding with the current position and row.

### Step 5. Claims the model cites

Where the document cites a published figure as an input and the person wants it checked, call `verify.qualify_source` with the DOI, then `verify.check_claim` with the figure, the verbatim passage and the full source object. Accept only a passage read in the same direction (register N3); "partial" on a method rule means the tool wanted a number, not that the rule is unsupported (`references/tools.md`). Clinical-effect inputs that need a review go to dh-clinical-validation (literature-and-real-world-evidence-review).

### Step 6. Wording a decision-maker reads as a verdict

Flag any sentence saying the technology "is cost-effective", "proves" value, or is "cost-saving" as fact, with HE-049 and the governance rule. Offer conditional, arithmetic wording labeled "proposed".

## Build the output

Follow `assets/reporting-check-output.md`. Short mode: the answer (the findings that would stop a reviewer, in words, not a score), the gaps, the record line.

## Before you hand it over

- No score, no percentage, no "compliant".
- Every finding has a document location and a row id; "not found" says which document was read.
- Inputs are checked, never replaced.
- Count the words in short mode.
- If the review leaves the conversation, it stops for the owner the person named; call `verify.build_record` with that named clearer, or label it an uncleared draft.

## Boundaries

- Whether a body will accept the model is the body's call.
- HTA submission mechanics belong to dh-market-access (payer-engagement-and-hta-submission); the literature review to dh-clinical-validation (literature-and-real-world-evidence-review).
- Drugs, biologics and wellness apps are out of scope.
