# B1 Launch review and miss owners

Framework task: DH-02.01.1.2, Part B, task B1. Replaces the earlier one-line pass rule and "Launch miss owner" sections.

## What this task delivers

A launch review: each measure checked against the person's pass rule, every miss with the owner the person names and a next step of one of three kinds (a briefing, a claim fix, a stopped claim), hypotheses for each miss labeled as hypotheses with what would confirm them, the stops for the regulatory, legal or compliance owner, and repairs ranked only if the person scored them. It answers "did launch run as planned, and who does what about each miss?"

Why it matters: a miss without an owner closes itself when the week ends. A claim in the field that was never approved is not a sales miss but a regulatory one (PC-US-17). The review keeps those apart and keeps the decisions with the people who own them.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.01.1.2 Part B, Launch review and miss owners |
| Workflow | The steps below |
| Knowledge | A2 results; A1 signals if relevant; `references/launch-measures.md`; `references/launch-clocks.md`; `references/governance.md` |
| Tools | `analytics.rice` or `analytics.mcda` only on the person's scores; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/launch-review-output.md` |
| Input | The request and its context: A2 results, the person's pass rules, the owners they name, the forum that will see the review, any scores |
| Governance | `references/governance.md`; people own the misses and decide the repairs |
| Catalogue job | `partner-prioritization`, for the ranking step only (`analytics.rice` or `analytics.mcda` on the person's scores). The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## Read the request

- **Results.** From A2, or the person's own numbers with their basis. If numbers come without a period or denominator, ask.
- **Pass rules.** The person's, per measure. "Did we hit it" without a rule gets the numbers and a request for the rule, not a verdict.
- **Owners.** In the person's words. Missing ones are "owner not named", and you ask.
- **Forum.** Which meeting or person sees the review. Never pick a date.

## Workflow

### Step 1. Check each measure against its rule

Met, missed, not measured, or no rule given, with the value and the rule. Do not average measures into one result.

### Step 2. Classify each miss and set the next-step kind

For each miss, record the kind of next step (old task rules):
- **Briefing**: a person sold or met customers without a delivered briefing, or the roster share missed.
- **Claim fix**: an approved claim was used to the wrong audience, or the leave-behind lacked a required section.
- **Stopped claim**: a claim id not on the approved list was used in the field. This stops for the regulatory or legal owner (PC-US-17, PC-EU-03), who decides on correction or withdrawal. For a comparative or efficacy claim, the evidence point is PC-US-28; do not cite PC-US-26, which lists comparisons that can be consistent with labeling. When the market is not stated, cite both PC-US-17 and PC-EU-03.
- Customer-side misses (cancelled meetings, accounts not reached) get their own line, separate from briefing misses.

### Step 3. Name the owner

Use the owner the person names for each miss. Leave an owner blank only when the role does not exist, and say so (old task rule). Otherwise "owner not named", and ask. Never suggest a job title.

### Step 4. Hypotheses, labeled

For each miss, offer at most two hypotheses, each labeled "hypothesis" with the record that would confirm or rule it out (for example "rep met customers before the briefing date; confirm from the briefing log"). Never state a cause.

### Step 5. Stops

List what goes to which owner: stopped claims (regulatory or legal owner); any free item, code, device or payment found in the records (compliance or legal owner, with the elements from CP-US-01, CP-US-09, CP-US-25 to CP-US-28, CP-US-34); any rule moved since the material was approved (A1, `references/launch-clocks.md`), which sends the material back to its owner.

### Step 6. Rank repairs only if scored

If the person wants an order, ask for criteria and scores and call `analytics.rice` (confidence as a percent; `references/tools.md`) or `analytics.mcda` with their numbers. Report their ranking and check one score by hand. Without scores, list the repairs labeled "proposed" in dependency order: a stopped claim before a reprint, a briefing before the next customer meeting for that person.

### Step 7. Keep misses open

A miss stays open until its owner closes it with evidence. Never close one because the period ended (old task rule).

## Build the output

Follow `assets/launch-review-output.md`. Answer first: how many measures met and missed against the person's rules, the stops, and the misses without an owner. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, owner, score and date is the person's.
- Every miss has a next-step kind and an owner or "owner not named".
- Hypotheses are labeled; no cause is asserted.
- No statement that the launch succeeded or failed overall.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Rewriting claims: the sibling skill's A2, then the regulatory or legal owner.
- Payer and coverage misses: Market Access.
- Personnel decisions about individual reps are the person's; the review reports activity facts only.
