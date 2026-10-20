# B1 Outcome result

Framework task: DH-01.07.3.1, Part B, task B1. Replaces the earlier "Outcome result" section (CF-12.01.07.3.1.3), and carries the usable-result rule and the gap owner as steps.

## What this task delivers

A result draft that reports a finished real-world study's result against the plan fixed beforehand: what was prespecified and what was not, what the result says in the paper's own direction and hedge, what it can and cannot carry for the decision makers named, whether it meets the usable-result rule the person sets, and who the person says owns each gap. It answers "what does our result support, and what do we do next?"

Why it matters: a real-world result is read through its plan. The same number means different things as a prespecified primary analysis, a post hoc subgroup, or an analysis changed after the data were seen (CV75, ES-87, HE-028).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Clinical Trials Director |
| Skill | DH-01.07.3.1 Part B, Outcome result |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/execution-and-reporting.md` sections 5 and 6; `references/study-question-and-design.md` section 5 |
| Tool | `verify.qualify_source` then `verify.check_claim` (wording check against the study report); `literature.get_record` if the result is published; `verify.build_record` for sign-off |
| Catalogue job | none |
| Prompt | This guide |
| Template | `assets/outcome-result-output.md` |
| Input | The request; the study report or paper; the A1 question and A2 record; the person's usable-result rule and named owners |
| Governance | `references/governance.md`; people set the rule and name owners; claims stop for the owner |

## Read the request

- **Which result.** Primary or secondary, which outcome, which population. Only results already in the conversation (a report, a table, a paper) are reported.
- **What it is for.** Internal decision, publication, payer or HTA use. External use stops for the owner.
- **The person's rule.** Whether they have one for "usable". If not, Step 4 writes it with them.

## The rule that shapes this task: the plan and the person decide

The plan fixed before outcome access decides what is prespecified. The person decides what result is usable and who owns each gap. The model reports and checks; it never upgrades a result's certainty, never calls a product effective or cost-effective, and never names an owner the person has not named. Any suggested rule is marked "proposed" and not applied until confirmed.

## Workflow

### Step 1. Gather the plan and the record

Use A1 (question, type, estimand) and A2 (order check, deviations). If A2 is missing, run it in short mode first; a result without A2 says "prespecification not checked".

### Step 2. Sort each result by its status

For each result the person wants to use: prespecified primary, prespecified secondary or sensitivity, changed after outcome access (deviation, HE-028), or not prespecified (exploratory or post hoc, ES-87). This column comes from A2, not from the report's own labels.

### Step 3. State the result in the report's own words

Quote the result passage with a locator. Keep its direction and its hedge: "associated with" stays "associated with". If the person wants a sentence for use elsewhere, check it: `verify.qualify_source {doi or document}`, then `verify.check_claim {claim: {text}, passage: {text, locator}, source: <full qualify_source object>}`. Accept it only if you read the passage and it says the same thing in the same direction with the same hedge (register N3: the tool returned "supported" for a reversed claim). A causal sentence from an observational result is declined and redrafted as an association, labeled "draft for the owner".

### Step 4. Write the usable-result rule with the person

Offer this shape, filled in their words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Prespecification | "Primary result prespecified with no change after outcome access" | A2 |
| Direction | "Point estimate favors the product on the primary outcome" | The report |
| Precision | "Confidence interval excludes no difference" | The report |
| Completeness | "Complete-case share above a level we set" | The report |
| Robustness | "Prespecified sensitivity analysis agrees in direction" | The report |

Write rules and owners back for confirmation before checking.

### Step 5. Check each rule

Met, not met, or not measurable `[GAP]`, each with the number behind it. Context to give beside the verdict, never instead of it: non-randomized evidence starts at low GRADE certainty and sound non-randomized studies are generally graded low (ES-90, ES-100); low risk of bias due to confounding is exceptional (ES-79); certainty is per outcome and a judgment, not a score (ES-96, ES-94). The certainty rating is the person's or the HTA body's.

### Step 6. Name the gaps and their owners

For each rule not met or not measurable, name the gap, the work that would close it, and the owner the person gave; if none, "owner not named" and ask. Typical routes: a rigor check of the study (DH-01.07.3.2 `outcomes-evidence-quality-monitoring`); replication in a different data source (HE-029); a deviation report and sensitivity analysis (HE-028, ES-40 by analogy); an economic model (dh-access-and-value 2.x); an HTA or payer submission (dh-access-and-value `payer-engagement-and-hta-submission`). One customer's outcome tracking is dh-go-to-market; outcome-linked payment is dh-access-and-value `outcomes-contract-monitoring`.

### Step 7. What the result can carry

For each decision maker the person named, one line from the rows: for example NICE early-use guidance evidence generation within 3 years (HE-072), ICER-PHTI emphasis on budget impact (HE-121), EU JCA clinical only (HE-094). No "cost-effective", no threshold comparison as a conclusion (HE-049).

## Build the output

Follow `assets/outcome-result-output.md`. Short mode: the answer (the result in its own words with its status, and whether it meets the person's rule), one table of rules with number, verdict and owner, at most three open items, the record line. Full mode adds the status table for every result, the wording check, the context per decision maker, and the draft conformance statement from A2.

## Before you hand it over

- Every result keeps the report's direction and hedge.
- Every rule and owner is the person's, and the output says so.
- Post hoc and changed analyses are labeled as such.
- No efficacy, superiority or cost-effectiveness claim; external wording stops for the owner.
- The record line ends the answer: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft." Call `verify.build_record` with that person in `cleared_by` only once they clear it.
- Every [PAPER] row id carries its DOI beside it (HE-025 to HE-030: DOI 10.1002/pds.4297).

## Boundaries

- The model reports and checks; it does not grade certainty, judge the study's acceptability for an HTA body, or forecast what a payer will accept.
- Rigor assessment in depth (risk of bias by domain) is the sibling skill, DH-01.07.3.2.
- Drugs, biologics and wellness apps are out of scope.
