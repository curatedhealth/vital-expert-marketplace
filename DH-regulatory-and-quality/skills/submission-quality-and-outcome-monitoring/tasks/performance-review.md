# B1 Performance review

Framework task: DH-03.03.4.2, Part B, task B1. Replaces the earlier "submission quality pass rule" and "submission quality miss owner" sections.

## What this task delivers

A review draft that says, submission by submission, whether submission quality and the review are going as the person's rules say they should: on track, at risk, or missed; where it stalled; who the person says owns each miss; labeled hypotheses for why; and which work in the sibling skill responds. It answers "are our submissions going well, and what do we do where they are not?"

Why it matters: without rules set in advance, every review reopens what "good" means. Rules on measures the agency itself reports (first-cycle acceptance, hold letters, review cycles, sponsor days, minutes on time) make the review fair and repeatable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.4.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/outcome-signals.md` (quality signals and agency figures) |
| Tools | A2's tools if no tracking run exists; `scripts/review_clock.py` (optional) |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the rules, in their words and numbers, and names the owner of each. The model checks results against those rules, finds where the submission stalled, and lays out options. It never sets a threshold, never decides what counts as a miss, and never names an owner the person has not named. If asked to propose rules, it may, each marked "proposed" with the measure and row behind it, and it does not apply them until the person confirms. Agency averages are context, never targets.

## Workflow

### Step 1. Gather the evidence

Use A1 (completeness) and A2 (clocks, hold letters, comparables) from the conversation. If either is missing and needed, run it in short mode first. A review on one of them alone is possible and says what was not reviewed.

### Step 2. Write the rules with the person

For each submission, ask for two to four rules, each with a number and an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Completeness | "Nothing missing against the map at filing" | A1 counts |
| First cycle | "Pass technical screening first time" | A2 events (S-15, S-38) |
| Hold letters | "No more than one Additional Information letter" | A2 events (S-25, S-41) |
| Sponsor time | "Answer each hold letter within 60 days, so a SIR stays in the 21-day window" | A2 events (S-34) |
| Interaction hygiene | "Pre-Sub minutes sent within 15 days every time" | Team records (S-30) |

Write the rules back for confirmation before checking anything. A submission without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule pass, miss, or not measurable `[GAP]`, with the number behind it. A submission is "on track" if every rule passes, "missed" if any rule misses, "at risk" if every rule passes so far but a sourced trigger is close (for example near the 100 FDA-day point for a 510(k), S-27, or a response deadline, RP US-13, S-16). With code execution, `scripts/review_clock.py events` gives the day counts.

### Step 4. Find the stall point

Name the first stage where a rule missed: content (A1), screening or acceptance, first substantive interaction, response to hold letters, or decision. An early stall (incomplete file) is a different problem from a late one (repeated hold letters on one section).

### Step 5. Hypotheses, not causes

For each stall point, list possible reasons as hypotheses to test, each with what would confirm it, drawn only from the sources and the person's records. For example: repeated hold letters on software could reflect a documentation level the reviewer read differently (test: compare the level rationale, S-01, with the letter's questions); an EU refusal could reflect an application outside the notified body's designation scope, one of the two main refusal reasons in the contractor study (S-72; test: check the body's designation in the official list, RP EU-45). Never state a cause the data does not show.

### Step 6. Route the response

| Stall point | Responding work |
|---|---|
| Missing or thin sections | Dossier assembly (sibling skill DH-03.03.4.1, task B1) |
| Clinical evidence questions | Clinical evaluation support (DH-03.03.4.1, task A2) |
| Content map unclear for the route | Submission content map (DH-03.03.4.1, task A1) |
| Route, class or predicate challenged | Pathway and classification work (DH-03.03.3) |
| Agency interaction (SIR, Pre-Sub, minutes) | Agency plan (DH-03.03.4.1, task B1); wording stops for the regulatory owner |

Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Build the output

Follow `assets/performance-review-output.md`. Short mode: verdict per submission, stall point, owner, the one decision needed. Full mode adds the rule table, evidence and hypotheses.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the number behind it and its basis.
- Causes are hypotheses, labeled.
- Responses to the agency, refile or withdrawal decisions, and board or investor reporting stop for the regulatory owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- No forecast of a decision or a date.
- Drugs, biologics and wellness apps are out of scope.
