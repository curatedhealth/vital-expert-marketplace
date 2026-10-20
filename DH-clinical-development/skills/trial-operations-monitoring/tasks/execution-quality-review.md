# B1 Execution quality review

Framework task: DH-01.02.3.2, Part B, task B1. Replaces the old "trial operations pass rule" (DH-01.02.3.2.2) and "trial operations miss owner" (DH-01.02.3.2.3) sections.

## What this task delivers

A review draft that says, site by site, whether execution meets the rules the person set: pass, miss or not measurable; where execution first stalls; whether the pattern looks site-specific or systemic, as hypotheses; who the person says owns each miss; and which work should respond. It answers "which sites miss our limits, why might that be, and what do we do?"

Why it matters: ICH E6(R3) expects acceptable ranges set in advance, an evaluation when one is exceeded, and the issue and remedial action documented in the clinical trial report (CVB3, CVB4). A review without pre-set rules turns into an argument about what "good" means.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.3.2 Part B, Execution quality review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/review-and-response.md`; `references/execution-metrics.md`; rows CV7, CV41, CV48, CV51, CV58, CV60, CV67, CV69, CV70, CV102, CV149, CVB1 to CVB6 |
| Tool | `scripts/trial_ops_metrics.py sites --rules` (with code execution); A2's tools if no clock run exists |
| Catalogue job | None |
| Prompt | This guide |
| Template | `assets/execution-quality-review-output.md` |
| Input | The request and its context; the person's rules or acceptable ranges and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the pass rules (or acceptable ranges, CVB3), in their own words and numbers, and names the owner of each. The model checks results against those rules, finds where execution stalls, and lays out hypotheses and options. The model never sets a threshold, never decides what counts as a miss or an important deviation (CVB2), and never names an owner the person has not named. If asked to propose rules, it may, each labeled "proposed" with the fact behind it, and does not apply them until the person confirms.

## Workflow

### Step 1. Gather the evidence

Use A1 (metrics by site and arm) and A2 (clocks) from the conversation. If A1 is missing, run it first in short mode. A review on metrics alone is possible and says that disclosure clocks were not reviewed.

### Step 2. Write the rules with the person

Ask for two to four rules, each with a number, a scope (each site or the trial) and an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Retention | "At least 85% of enrolled participants retained at each site" | A1 retention |
| Completeness | "Primary endpoint data at least 90% complete per site" | A1 completeness |
| Deviations | "No more than 1 important deviation per 10 participants" | A1 important deviations per participant |
| Arm balance | "Arms within 5 points on completeness" | A1 completeness by arm |
| Disclosure | "Results posted by the 42 CFR 11.44 date" | A2 clock |

Write the rules back for confirmation before checking anything. A site without rules gets a factual summary and no verdict.

### Step 3. Check each rule

With code execution: `python3 scripts/trial_ops_metrics.py sites <export.csv> --targets <targets.csv> --as-of <date> --rules <rules.json>`. Mark each rule pass, miss or not measurable `[GAP]`, with the number. Where a rule is scoped to the whole trial, also show the site values beneath it: a trial-level pass can hide a site (for example, an arm gap at one site).

### Step 4. Find the stall point

For each site with a miss, name the first metric in the order of `review-and-response.md` (enrollment, retention, deviations, completeness, disclosure) that missed. That is where the response goes.

### Step 5. Site-specific or systemic, as hypotheses

For each stall point, list the hypotheses from `review-and-response.md` that fit the pattern, each with what would confirm it. A miss at one site points to a site-specific hypothesis; the same miss at every site points to a systemic one (CVB3, CVB5). Never state a cause the data do not show.

### Step 6. Route the response and name the owner

Map each stall point to the responding work in `review-and-response.md` without choosing for the person. Name the owner the person gave. If no owner was named, write "owner not named" and ask. Note that exceeded ranges and remedial actions belong in the clinical trial report (CVB4), and that important deviations need an explanation and a recurrence measure from the investigator (CVB1).

## Build the output

Follow `assets/execution-quality-review-output.md`. Short mode for a direct question: the verdict per site against the rules, the stall point, the owner, the first hypothesis to test, the one decision needed. Full mode adds the rule table, evidence, all hypotheses and routing.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the number behind it.
- Causes are hypotheses, labeled.
- No site staff are named or ranked; sites only.
- Site communications, protocol changes and steering-committee reporting stop for the owner.
- Record line present.

## Boundaries

- The model checks and structures; it does not judge people.
- No forecast of when a site will recover or when enrollment will complete.
- Operational metrics are not the trial's result.
