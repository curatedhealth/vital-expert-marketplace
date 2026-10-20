# B1 Adoption review and follow-up

Framework task: DH-02.02.4.2, Part B, task B1. Replaces register task CF-12.02.02.4.2.3 "Enablement follow-up" and the earlier one-line pass rule and owner sections.

## What this task delivers

A review of each site or role against the person's adoption rule; for each miss, the hypotheses (task wrong, training wrong, workflow wrong) with the signals in the data and what would confirm each; follow-up options laid out with sourced facts, the design or workflow option always beside any repeat of training; the person's scores ranked by the connector; owners and next steps as the person names them; and the stops. It answers "which sites missed our rule, what might be wrong, and what do we do next?"

Why it matters: repeating the same session is the default response and the weakest one: training depends on memory and decays (CS77, CS78), and the register rule says not to schedule the same session again without saying what changes (CF-12.02.02.4.2.3).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.4.2 Part B, Adoption review and follow-up |
| Workflow | The steps below |
| Knowledge | `references/follow-up-rules.md`; A1 rule; A2 results; sibling skill's session record if present |
| Tools | `analytics.mcda` (counted, when the person scored options); `verify.build_record` (counted, on release) |
| Prompt | This guide |
| Template | `assets/review-and-follow-up-output.md` |
| Input | The request and its context: the rule, the A2 results per site and role, what the person knows about each site, options they are weighing with criteria, weights and scores, owners and next dates as they set them |
| Governance | `references/governance.md`; people classify, score and own; the model offers hypotheses and ranks only what was scored |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## Read the request

- **Rule and results.** From A1 and A2. Without the rule, no site is a miss; report numbers only and ask for the rule.
- **Site knowledge.** What the person knows (for example "South uses the old log because pharmacy still asks for it"). Treat it as owner-stated (O), not as a finding.
- **Options, criteria, weights, scores.** The person's. Offer the options in `references/follow-up-rules.md` section 4 as a "starting list" if they have none.
- **Owners and dates.** The person's. If not named, "owner not named"; ask. Never pick a date.

## Workflow

### Step 1. Check each group against the rule

Met, missed, or no verdict (window not elapsed, no rule). Numerator and denominator on each line. Do not average sites.

### Step 2. Hypotheses per miss

For each miss, fill the table in `references/follow-up-rules.md` section 2: task wrong, training wrong, workflow wrong, each with the signal from A2 or the session record, and what would confirm or rule it out. Label every line "hypothesis". The person decides which holds.

### Step 3. Lay out follow-up options

For each option, the sourced facts with rows (section 4), always including a workflow or design option beside any training option (UX-US-33, CS77). Any repeat of training states what changes in it. For a device, cite UX-US-49 for routing a training change to the regulatory owner; cite CS79 only for "additional training" offered as a fix for critical-task errors. If the product is a device and the option changes training, add "goes to the regulatory owner" (UX-US-49). Any option that pays or gives something tied to usage: "stops for compliance" with the CP rows from `references/governance.md`.

### Step 4. Rank what they scored

If the person scored the options (0 to 4, weights summing to 1), call `analytics.mcda` and report values and largest contributions; work out the smallest weight change that flips the top two (`references/tools.md`). Without scores: no ranking; ask.

### Step 5. Owners and next steps

For each miss: the owner as named, the next step the person chose, and the date they set, or "owner not named" and blanks. Then say what A2 will measure to show the follow-up worked (the same rule, the next period).

## Build the output

Follow `assets/review-and-follow-up-output.md`. Answer first: which groups missed the rule, with numbers, then the hypotheses and the first follow-up in the dependency chain. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Verdicts only against the person's rule.
- Causes appear only as labeled hypotheses with what would confirm them.
- A workflow or design option sits beside any training option; a repeat session says what changes.
- Owners and dates are the person's or blank; no job title suggested.
- No clinical, payment or success claim from adoption numbers.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Follow-up on adoption of the trained task. Training redesign runs in the sibling skill (training-and-change-enablement); usability evidence in the UX pack; device and submission questions in dh-regulatory-and-quality.
- Customer health, renewal risk and expansion belong to DH-02.02.2.x and 3.x; outcome-based payment to Market Access.
