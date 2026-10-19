# B1 Operating model decision

Framework task: DH-03.02.3.1, Part B, task B1. Replaces the earlier one-line pass rule and owner sections.

## What this task delivers

A decision paper for the QMS operating model: the options (for example one global QMS or regional systems; MDSAP now, later or not), the sourced facts that bear on each, the person's scores and weights ranked by the connector, where a weight change would flip the order, the sequence of decisions by dependency, and the points that stop for the accountable owner. It answers "which QMS model fits our markets, and what has to be decided first?"

Why it matters: the model fixes the audit load for years. MDSAP runs a three-year cycle (QS42); Canada ties MDSAP certification to Class II to IV licenses (MR-05); FDA uses MDSAP reports only in place of surveillance inspections (QS40). Choosing without these facts on the table locks in cost or blocks a market.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Quality & Software Lifecycle Director (`quality-systems-director-software`) |
| Skill | DH-03.02.3.1 Part B, Operating model decision |
| Workflow | The steps below |
| Knowledge | `references/operating-model-options.md`; A1 scope (markets and classes); A2 governance design if present |
| Tools | `analytics.mcda` (counted); `scripts/mcda_swap.py` (optional) |
| Prompt | This guide |
| Template | `assets/operating-model-decision-output.md` |
| Input | The request and its context: markets and classes (A1), the options the person is weighing, the criteria and weights they set, their scores, the accountable owner for the decision |
| Governance | `references/governance.md`; people score, the connector ranks, the owner decides |

## The rule that shapes this task: people score

The person chooses the criteria, sets the weights and scores each option. The model lays out the sourced facts per option and criterion so the scoring is informed, runs the ranking, and shows where the order is fragile. It never scores, never fills a missing score, and never calls an option "recommended". If asked for a proposal, it may write one labeled "proposed", with the facts behind it, and does not treat it as decided.

## Read the request

- **Markets and classes.** From A1. Without them the MDSAP question cannot be framed; ask.
- **Options.** Take the person's. If they have none, offer the decisions D1 to D5 in `references/operating-model-options.md` as a starting list, labeled "starting list".
- **Criteria and weights.** Ask. Offer criteria names only as examples phrased so that higher is better (the connector treats every criterion that way, `references/tools.md`), for example "markets served", "audit burden avoided", "build effort avoided", "speed to first market".
- **Accountable owner.** Who decides. If not named, "owner not named"; ask.
- **Mode.** Short for a direct question; full for a decision paper.

## Workflow

### Step 1. Frame the decisions

Write each decision (D1 structure, D2 MDSAP, and any others the person names) with its options. Keep decisions separate: a combined option ("single QMS with MDSAP") is fine if the person frames it that way.

### Step 2. Lay out the facts per option

For each option and criterion, list the sourced facts from `references/operating-model-options.md` with row ids. Facts only, no scores. Point out where the facts depend on the market list, for example: "MDSAP changes the license route only in Canada among the rows (MR-05); in the US it replaces surveillance inspections only (QS40, MR-39); for the EU no row shows a substitution (QS38, EU25) `[GAP]`."

State the consequence for the person in one or two lines per option, conditional on their markets ("if Canada is in scope...").

### Step 3. Collect the person's scores

Ask for scores on a 0 to 4 scale (the connector's scale) and weights that sum to 1. Write them back for confirmation. A missing score stops the ranking for that option; say which.

### Step 4. Rank what they scored

Call `analytics.mcda` with `alternatives` (id and scores) and `criteria_weights`. Report each option's value and the contributions by criterion. With code execution, save the call and response as JSON and run `scripts/mcda_swap.py FILE` to check the values and get the swap points. Report the smallest weight change that flips the top two, in plain words ("if build effort avoided were weighted 0.36 instead of 0.20, the order of the top two would reverse").

### Step 5. Sequence by dependency

From the "Sequencing by dependency" list in `references/operating-model-options.md`, write which decision blocks which, with the reason and row. No dates and no urgency. Clocks in the rows are facts.

### Step 6. Stops and the owner

List what stops for the accountable owner: the decision itself; any notified body notification of a substantial QMS change (EU24); certification claims; conformity route or class (regulatory owner). Name the owner the person gave, or "owner not named". If the person asks for wording to a board or a notified body, draft only what the facts support and label it "draft for the owner".

## Build the output

Follow `assets/operating-model-decision-output.md`. Answer first: the ranked result of the person's scores and how robust it is, then the first decision in the dependency chain. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections, then table rows that the person's facts do not touch (list them by P number in one line); count every table cell except the Rows column; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every score and weight is the person's, and the output says so.
- Every fact has a row id; every unknown is `[GAP]`.
- The ranking is described as the result of their scores, never as a recommendation.
- No dates or urgency in the sequence.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The operating model of the QMS only. Regulatory pathway and classification belong to the Regulatory pack and the person's regulatory owner.
- No cost estimates: the rows hold no cost data. A cost criterion is scored by the person from their own figures.
- Drugs, biologics and wellness apps are out of scope.
