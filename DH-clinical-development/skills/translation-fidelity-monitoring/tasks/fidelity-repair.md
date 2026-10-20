# B1 Fidelity repair

Framework task: DH-01.01.4.2, Part B, task B1. Replaces the earlier "Fidelity repair" section (DH-01.01.4.2.3).

## What this task delivers

A repair draft that says, rule by rule, whether the version meets the fidelity rules the person set: pass, fail, or not measurable. For each failure: whether the product text, the decision rule or the claim map changes; the owner the person names; and the version that must not ship the failed text, as the person decides. It answers "what fails, who fixes it, and what must not ship?"

Why it matters: the old rule is plain: do not ship the failed text while the repair is open (DH-01.01.4.2.3). Writing the owner and the blocked version next to each failure makes that rule usable at release.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.4.2 Part B, Fidelity repair |
| Workflow | The steps below |
| Knowledge | A1 rules and A2 sample; `references/claim-and-rule-fidelity.md`; rows TM13, TM93, TM98, TM105, PL95, PL96, PL59, PL75, PC-US-23, PC-US-31 |
| Tools | A2's tools if no sample exists; `scripts/fidelity_sample.py` |
| Prompt | This guide |
| Template | `assets/fidelity-repair-output.md` |
| Input | The request and its context; the person's pass rules and named owners; the A2 sample; the release plan |
| Governance | `references/governance.md`; people set rules, name owners and decide what ships |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the pass rules, in their own words, and names the owner of each. The model checks the A2 evidence against those rules, lists failures and routes the work. It never sets a rule, never decides on its own that a difference is a failure, never names an owner the person has not named, and never decides that a version may ship. If asked to propose rules, it may, each marked "proposed" with the row behind it, and applies none until the person confirms.

## Workflow

### Step 1. Gather the evidence

Use A1 (rules) and A2 (sample) from the conversation. If either is missing, run it first in short mode. A review on part of the sample says what was not reviewed.

### Step 2. Confirm the pass rules and owners

Write the person's rules back in this shape, filled in their words, and confirm before checking:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Claim population | "No shipped claim names a population wider than its source" | A2 claims comparison |
| Claim verb | "No shipped claim drops a hedge the source has" | A2 claims comparison |
| Caveat | "Every caveat in the indication appears in the onboarding text" | A2 claims comparison |
| No source | "Every shipped claim has a source passage" | A2 count with no source |
| Decision rule | "Each rule fires as specified in release testing, including missing-data behavior" | A2 rule check |
| Dose | The person's threshold for sessions delivered and coverage | A2 adherence output |

### Step 3. Check each rule

Mark pass, fail, or not measurable `[GAP]`, with the quoted words or the figure behind it and its source (claim id and version, rule id and evidence, script output).

### Step 4. Name what changes

For each failure, state which of three changes responds, without choosing for the person (old method step 1):
- **Product text changes** to match the source (the claim map stands).
- **Decision rule changes** to match the specification (a software fix; release records go to `dh-regulatory-and-quality` document-and-change-control, verification records to `dh-regulatory-and-quality` design-controls-and-risk-management).
- **Claim map changes** because the source was read wrongly or new evidence exists: route to evidence-to-intervention translation (DH-01.01.4.1); a new claim is a translation limit question there, not a repair.
A low-dose finding may point to the product (engagement design), to the regimen, or to context; Moore separates adaptation from infidelity by reference to the intervention theory (TM93). Name the options; the person decides.

### Step 5. Name the owner and the version that must not ship

For each failure, the owner the person gave, or "owner not named" and ask. Ask which version must not carry the failed text, and record their answer. Facts that bear on it: for a DiGA, changes affecting the care-effect evidence or the patient group are significant changes, and BfArM provides a checklist to decide (PL95, PL96); a change that alters the SaMD definition statement re-opens categorization (PL59); for US products, communications that change indication, population, limitations or regimen are inconsistent with labeling (PC-US-23, nonbinding guidance). Whether any applies is a question for the owner the person names for regulatory status, or owner not named.

### Step 6. Re-run on the next version

Say which rules to re-check when the next version arrives (all rules touching changed text, rules or regimen), and that a feasibility-stage check does not replace one in the full rollout (TM98).

## Build the output

Follow `assets/fidelity-repair-output.md`. Short mode for a direct question: rules passed and failed, each failure with the change, the owner and the version that must not ship it, and the one decision the person needs to make. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule and owner is the person's; proposals are labeled.
- Every verdict cites the quoted words or figure behind it.
- No general verdict ("faithful", "compliant", "safe to ship"); only per-rule pass or fail.
- The version that must not ship is the person's decision, recorded in their words.
- Each [PAPER] paper cited has its DOI once in prose, and every table cell that cites a [PAPER] row carries that row's own DOI; abstract-only and [WF] rows carry their label each time.
- No date, data cut, version, threshold or status appears that the person did not give ("not given" and ask); no fact comes from an earlier, separate request.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Release approval, change records and CAPA: `dh-regulatory-and-quality` document-and-change-control and audit-capa-and-complaints.
- Change notices and submissions: `dh-regulatory-and-quality` regulatory-submission-and-dossier; PCCP: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Promotional claim corrections already in market: `dh-go-to-market` pricing-and-value-message-monitoring, with the owner the person names for claims, or owner not named.
- No judgment of people or teams; the model checks text, rules and figures.
