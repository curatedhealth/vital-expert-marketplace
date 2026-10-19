# B1 Unactioned stop review

Framework task: DH-02.04.3.2, Part B, task B1. Replaces the earlier "Unactioned stop" section (CF-12.02.04.3.2.3) and the one-line rules "name the owner" and "name the date the action or refusal will be written".

## What this task delivers

A review draft: the person's rules for research actionability, each checked against A1 and A2; every repeated stop with no action or refusal, with its count and the participants' words; hypotheses for why it is open, labeled, with what would confirm each; response options labeled "proposed"; a ranking only if the person scored them; and for each stop the owner the person names, the forum that will see it and the date they set for the action or refusal to be written. It answers "which stops are still open, and who will decide them by when?"

Why it matters: a repeated stop with no owner stays only in a recording, which the register names as the failure to avoid. A rule written before the numbers stops every review from reopening what "acted on" means.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.04.3.2 Part B, Unactioned stop review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/actionability-indicators.md`; `references/study-quality-criteria.md`; rows UX-US-32, UX-US-33, UX-US-42, UXR-03 |
| Tool | `analytics.rice` or `analytics.mcda` (counted, optional, on the person's scores); A2's script if no indicator run exists; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/unactioned-stop-review-output.md` |
| Input | The request and its context; the person's rules, named owners, forums and dates, any scores; A1 findings and A2 indicators |
| Governance | `references/governance.md`; people set rules, name owners and choose dates |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## Workflow

### Step 1. Gather the evidence

Use A2 (open insights, ages, owners) and A1 (sample and method findings) from the conversation. If A2 is missing and the logs exist, run it in short mode. A review without A1 says the study's soundness was not checked.

### Step 2. Write the rules with the person

Offer this shape, filled with their words and numbers:

| Rule type | Example shape (their words) | Checked against |
|---|---|---|
| Decision | "Every repeated stop has an action or a refusal by the next release planning" | A2 status, open ages |
| Reason | "Every refusal records its reason" | A2 refusals without a reason |
| Owner | "Every open insight has a named owner" | A2 no owner |
| Trace | "No change is credited to research without an insight id" | A2 not traced |
| Critical | "Every stop on a critical task goes to the HF lead before release" | A2 critical-task insights |

Write the rules back for confirmation. Without rules: a factual summary and no verdict.

### Step 3. Check each rule

Met, missed or not measurable `[GAP]`, with the number. Never average across studies or teams.

### Step 4. Unactioned stops

For each repeated stop with no action or refusal: stop id, participants hit by group, the participants' words (from the session log if available), age, owner. Stops on critical tasks first, whatever their count (UX-US-32). If A1 found the stop rests on wrong-role sessions, say so.

### Step 5. Hypotheses and response options

For each, list hypotheses, labeled, with what would confirm them (for example: no owner was ever named, confirm from the log; the fix needs a design decision outside the team, confirm with the person; the stop rests on one group only, confirm from A1). Never state a cause.

Response options, labeled "proposed": write the action or the refusal with its reason; retest a wording-only fix on a critical task (UX-US-42); prefer a design fix over information (UX-US-33); run a further formative round where the sample did not fit (UXR-03). If the person wants a ranking, ask for their scores and call `analytics.rice` (confidence as a percent) or `analytics.mcda` (0 to 4 scores, weights summing to 1, criteria phrased so higher is better). Never score for them.

### Step 6. Owner, forum and date

For each open stop: the owner the person names, the forum that will see it, and the date by which the action or refusal will be written (register method). Missing: "owner not named" or "not set", and ask. No dates or job titles from the model, no urgency.

### Step 7. Stops

State what goes to the accountable owner: critical-task stops and any decision to accept them without a fix; any claim that research is complete or the product usable; board or regulator wording. Draft only what the facts support, labeled "draft for the owner".

## Build the output

Follow `assets/unactioned-stop-review-output.md`. Answer first: which rules miss, the open stops with the most participants or on critical tasks, and the owner decision needed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, owner, forum, date and score is the person's, and the output says so.
- Every verdict cites its number.
- Causes are hypotheses, labeled.
- Critical-task stops are listed first and not ranked away.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Writing the action itself: `patient-and-clinician-user-research` (B1).
- Residual-risk acceptance: the regulatory or human factors owner.
- No judgment of people or teams; no forecast of release outcomes.
