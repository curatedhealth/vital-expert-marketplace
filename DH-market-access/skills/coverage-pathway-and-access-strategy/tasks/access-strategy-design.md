# B1 Access strategy design

Framework task: DH-03.01.4.1, Part B, task B1.

## What this task delivers

A decision draft that helps the person choose which coverage routes to pursue and in what order: the options from the pathway map, the criteria that matter to this person with their own weights and scores, a transparent ranking, a sequence built on what unlocks what, and the gates where the plan should be reviewed. The person decides; this task makes the decision explicit, sourced and repeatable.

Why it matters: market order is often set by habit or by the loudest stakeholder, and the reasons are lost. A weighted, documented choice can be challenged, rerun when facts change, and defended to a board.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.4.1 Part B, Access strategy design |
| Workflow | The steps below |
| Knowledge | The A2 pathway map; `references/requirements/`; `references/scheme-kinds.md`; the MCDA method cited by the tool (EVIDEM; ISPOR MCDA good practice) |
| Tools | `analytics.mcda` (ranks options the person has scored); A2's tools if no map exists yet |
| Prompt | This guide |
| Template | `assets/access-strategy-output.md` |
| Input | The request and its context; the A2 map; the person's criteria, weights and scores; their constraints (budget, evidence already held, team, preferred markets) |
| Governance | `references/governance.md`; people score, the model does not |

## The rule that shapes this task: people score

The model lays out the facts for every option against every criterion. The person sets the weights and gives the scores. `analytics.mcda` only ranks what the person scored. The model never invents a score, and never presents its own reading as the person's choice. Why: a ranking is only as good as the judgment in its scores, and that judgment belongs to the people accountable for the outcome. If the person asks you to propose scores, you may, but each proposed score carries the fact that supports it, is marked "proposed", and is not run through the ranking until the person confirms it.

## Workflow

### Step 1. Start from the map

If the conversation holds an A2 pathway map, use it. If not, run A2 first (short mode is enough) for the person's target countries. The options are the routes marked "fits" or "unclear" on the map; routes that do not fit stay out, named in one line.

### Step 2. Agree the criteria

Propose this default set and let the person drop, add or rename criteria. Keep it to four to seven; more criteria dilute the weights and make the result harder to defend.

| Criterion | The question it answers | Facts that inform it (from the map and requirements files) |
|---|---|---|
| Evidence fit | Does the evidence we hold or will hold meet this route's bar? | Evidence bar per route; the person's studies |
| Prerequisite readiness | How much is left to do before we can file? | Device class, certificates (for example BSI TR-03161, ANS conformity, HDS hosting, DTAC), registrations |
| Time to first payment | How soon could payment start? | Review timelines; whether a trial or early-funding phase pays |
| Durability | Is the coverage lasting or does a clock run? | Temporary versus permanent; renewal rules |
| Payment potential | What does this route pay, and for what? | How the scheme pays (product, flat fee, code, guidance only); comparators' recorded prices as facts |
| Competitive position | Is the route proven, and how crowded is it? | Precedents and their dates |
| Evidence reuse | Does work for this route also serve others? | Overlap in comparators, settings and study design across routes |

Define each score on the tool's 0 to 4 scale with the person before scoring, in their words (for example, for durability: 0 guidance only, no funding; 2 temporary funding with a clock; 4 permanent listing). Anchors written down make scores comparable and the result repeatable.

### Step 3. Lay out the facts, then collect weights and scores

Build the options-by-criteria table with the supporting fact and its source in each cell, and no score. Ask the person for weights (they must sum to 1) and a 0 to 4 score per cell. Accept them in any form (a table, a list, "Germany 4 on evidence") and write them back for confirmation. If a fact needed to score a cell is `[GAP]`, say so in that cell: the person may score it anyway, but the gap stays visible.

### Step 4. Rank

Call `analytics.mcda` with `alternatives` (each route's id and its scores) and `criteria_weights`. Report the value estimate per route and each criterion's contribution, so the person sees why a route ranks where it does. Then test whether the order is robust. Better than a fixed nudge: for the top two routes, and for the second and third, state how far a weight would have to move before they swap ("DiGA stays first unless competition counts for more than about 52%"). Work it out from the scores and weights already given (with the other weights kept in proportion); no extra tool call is needed. Say plainly which call is close, because that is where the person's judgment matters most.

### Step 5. Sequence by dependency

Ranking says which routes are worth most; sequence says what has to happen first. Order the chosen routes by what unlocks what, using the requirements files: shared prerequisites done once (for example EU or EEA hosting serving two countries), evidence that serves several routes generated first, and clocks that should start only when the next step is ready (for example, a route whose permanent-listing dossier is due within months of starting should begin only when that study is well under way). Where order does not matter, say so.

### Step 6. Set the gates

For each step in the sequence, name the gate: what must be true to proceed (a certificate obtained, a study reading out, a decision received), and what would change the plan. Gates are what the person reviews; they are stated as conditions, never as dates.

## Build the output

Follow `assets/access-strategy-output.md`. A direct question ("which order should we go in?") gets **short mode**: the ranking, how robust it is, the sequence with gates, and at most three facts that could change a score. Full mode (the fact table for every cell, risks, anchors) is for a document to share or when asked. Never turn comparators' prices into an expected price for the person's product, even as a range: that is a pricing position and stops for its owner.

## Before you hand it over

- Every fact in the table carries its source from the map or the requirements files.
- Scores and weights are the person's, and the output says so.
- The final choice of routes, any pricing position, and any wording for a payer, HTA body or BfArM stop for the accountable owner (`references/governance.md`). Label the output as a decision draft.
- If it will leave the conversation, ask who clears it and call `verify.build_record` with that person in `cleared_by`; otherwise label it an uncleared draft.

## Boundaries

- The model does not score and does not choose. It structures, ranks what was scored, and sequences.
- No price for the person's product, no forecast of revenue, no promise that any route will succeed.
- No dates or durations invented for the plan. Timelines come only from the sourced requirements (review periods, clocks).
- Drugs, biologics and wellness apps are out of scope.
