# B1 Model review and repair

Framework task: DH-01.07.2.2, Part B, task B1. Replaces the old "Model score" (CF-12.01.07.2.2.2) and "Model repair" (CF-12.01.07.2.2.3) sections and the old one-line pass rule and miss owner. Their rules stay as steps: score only with the rule the buyer supplied; name the input the buyer said is wrong.

## What this task delivers

A review draft that says, against the acceptance rules the person set, which findings from A1 and A2 pass, miss or cannot be judged; who the person says owns each miss; and a repair list that names each input or section to change, the change proposed, and what the change does to the result. The person decides what is accepted and what is repaired.

Why it matters: without written acceptance rules, every model review reopens what "good enough" means, and the reviewer's taste wins. Rules set before the review make it fair and repeatable, and a repair list tied to named inputs stops a model being rebuilt when it only needed three changes.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.2.2 Part B, Model review and repair |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/validity-rules.md`; `references/reference-cases.md` |
| Tools | A1's and A2's tools if their outputs are missing; `scripts/he_model.py` and `scripts/sensitivity_summary.py` to show the effect of a repair; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/review-and-repair-output.md` |
| Input | The request and its context; A1 and A2 results; the person's acceptance rules and named owners; the inputs the person says are wrong |
| Governance | `references/governance.md`; people set rules, name owners and choose repairs |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the acceptance rules, in their own words, and names the owner of each. The model checks findings against those rules, shows the effect of each repair, and lays out options. It never scores on CHEERS (HE-005, DOI 10.1177/23814683211061097), never sets a rule, never decides what counts as a miss, never names an owner the person has not named, and never changes an input the person has not named as wrong. If asked to propose rules, it may, each marked "proposed" with the row behind it, and it does not apply them until the person confirms.

## Workflow

### Step 1. Gather the findings

Use A1 (reporting, reference case, rule currency) and A2 (validity evidence, recomputation, observed values) from the conversation. If either is missing and needed, run it first in short mode. A review on reporting alone is possible and says that validity was not reviewed.

### Step 2. Write the acceptance rules with the person

Ask for the rules, each with an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Checked by |
|---|---|---|
| Reporting | "Every sourced CHEERS item addressed in the full report" | A1 Step 2 |
| Reference case | "Base case follows the NICE reference case; anything else is a separate scenario" | A1 Step 3, HE-035 |
| Rule currency | "No retired value set or old threshold wording" | A1 Step 4 |
| Verification | "Every reported number recomputes" | A2 Step 2 |
| Monitoring | "Re-review if an observed value crosses a switching value" | A2 Step 6 |

If the person asks for a score, use only their scoring rule, applied as written, and show the arithmetic; never a CHEERS score. Write the rules back for confirmation before checking anything. A model with no rules gets the factual findings and no verdict.

### Step 3. Check each rule

Mark each rule pass, miss, or not judgeable `[GAP]`, with the findings behind it. Group misses by kind: reporting gap, reference-case difference, rule currency, calculation difference, validity evidence missing, assumption overtaken by observed data.

### Step 4. Name the owners

For each miss, the owner the person named for that rule. If none, "owner not named", and ask.

### Step 5. The repair list

For each input or section the person names as wrong, write the repair: what changes, from what to what, the source of the new value, and the effect on the result. With code execution, run the model before and after with `scripts/he_model.py`, or the change as a scenario in `scripts/sensitivity_summary.py`; otherwise one `analytics.scenario-modeler` call. Findings the person has not named as wrong are listed as "for the person to decide", with proposed repairs labeled "proposed" and not applied. Typical repairs drawn from the rows: re-derive utilities with the UK 5L value set and drop 3L sensitivity analyses for a new NICE topic (HE-058, HE-061), with any new utility evidence from dh-clinical-validation (literature-and-real-world-evidence-review); move productivity costs out of the NICE base case (HE-038); state both NICE threshold ranges and remove verdict wording (HE-049, HE-050, HE-051, HE-074); add the funding and conflicts statements (HE-014, DOI 10.1177/23814683211061097); replace default plus or minus 20 percent ranges with ranges the modeler can justify, and run sensitivity on net benefit rather than the ICER (`references/tools.md`).

### Step 6. Route the response

| Miss | Responding work |
|---|---|
| Model structure, inputs, runs | economic-model-development (A2, B1) |
| Clinical or utility evidence | dh-clinical-validation (literature-and-real-world-evidence-review) |
| Real-world outcomes data | dh-health-economics DH-01.07.3 |
| Submission text and HTA engagement | dh-market-access (payer-engagement-and-hta-submission) |
| Value messages built on results | dh-health-economics DH-01.07.4 (value-narrative-and-dossier), dh-commercial (pricing-and-value-message-monitoring) |

## Build the output

Follow `assets/review-and-repair-output.md`. Short mode: the verdict per rule (the person's rules only), the misses with owners, the top repairs with their effect, the one decision needed, the record line.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- No CHEERS score; any score uses only the person's rule.
- Only inputs the person named are repaired; other repairs are "proposed".
- The repaired result is a hypothesis; no sentence says the model is now valid or the product cost-effective.
- Count the words in short mode.
- A repaired model or review for an HTA body or payer stops for the owner the person named; call `verify.build_record` with that named clearer, or label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- Acceptability to a decision-maker is never the model's call.
- Drugs, biologics and wellness apps are out of scope.
