# B1 Prioritization rule and ranking

Framework task: DH-01.03.3.1, Part B, task B1. Replaces the old "Prioritisation rule" task (CF-12.01.03.3.1.2) and keeps its method: state the rule, apply it to the choice list, show the item the rule placed last, and do not change the rule after seeing the rank you prefer.

## What this task delivers

The person's rule, written back and confirmed before any rank; a ranking of the items the person scored (MCDA or RICE), with each item's value and largest contribution; where the ranking would flip; any sensitivity run on the person's own inputs; and the item the rule places last. It answers "by our own rule, how do our items rank, and how firm is that rank?"

Why it matters: a rule written after the rank is a justification. Weights that sit one step from a flip mean the forum is choosing between near equals and should know it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.03.3.1 Part B, Prioritization rule and ranking (CF-12.01.03.3.1.2) |
| Workflow | The steps below |
| Knowledge | A1 output; `references/prioritization-methods.md` sections 1 to 5 (SP-074 to SP-087) |
| Tools | `analytics.mcda` or `analytics.rice` (ranks what the person scored); `analytics.scenario-modeler` and `analytics.risk-tornado` (sensitivity on the person's inputs); `scripts/portfolio_rank.py` (`mcda`, `swap`, `swap --scores`, `rice`, `capacity`, `words`) |
| Prompt | This guide |
| Template | `assets/rule-and-ranking-output.md` |
| Input | The request and its context; the A1 choice list; the person's criteria, anchors, weights, 0 to 4 scores (or RICE inputs), decision rule, capacity and any probability of success they hold |
| Governance | `references/governance.md`; people score, weight and decide; a ranking is not the decision |
| Catalogue job | none. The commercial job `partner-prioritization` uses the same tools but is scoped to partners (`references/tools.md`). |

## The rule that shapes this task: people score; the rule comes first

The person sets criteria, anchors, weights, scores and the decision rule, and confirms them before any calculator is called. `analytics.mcda` and `analytics.rice` rank only what the person scored. If asked to propose criteria or anchors, each is labeled "proposed" with the A1 fact behind it and is not used until confirmed. Proposed scores are never ranked. A rank is never presented as the choice (SP-080, [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016).

## Workflow

### Step 1. Start from the choice list

Use A1 from the conversation. If none exists, run A1 in short mode. Rank only items on the ready list. Items with a `[GAP]` stay in, with the gap visible in their row.

### Step 2. Write the rule

Ask for, or write back, the three parts of the rule (`prioritization-methods.md` section 2):
1. **Criteria and weights.** If the person has none, offer this set as "proposed"; they drop, add or rename. Keep four to six, each phrased so 4 is best (the tool treats every criterion as higher-is-better, register C17):

| Criterion (proposed) | Question | A1 facts that inform it |
|---|---|---|
| Unmet need fit | How well does the item address the need the person's strategy names? | The person's need statement |
| Evidence readiness | How far is the evidence the next gate asks for? | Readouts and stage gate record |
| Regulatory path clarity | How settled is the route? | Status as stated; library record |
| Strategic fit | How well does it fit the person's stated strategy? | Strategy from `strategic-vision-and-options` (this pack), if given |
| Capacity fit | How little of the named capacity does it use? (4 = least) | Capacity ask |

Check the set against the task force's tests and ask the person about any concern: complete (SP-076), no double counting (SP-077), preference-independent (SP-078), all [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016. When a scored criterion measures what the decision rule already constrains (for example a "capacity fit" score plus a cut at a named FTE capacity), name that pair first as the double-counting question (SP-077, [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016), and show what it does in the person's numbers (for example the item that scores 1 on capacity fit loses points for capacity and is then cut on capacity again). Check the person's own criteria before giving generic examples. Whether to keep both is the person's call.
2. **Anchors**: what 0, 2 and 4 mean for each criterion, in the person's words, before scoring.
3. **Decision rule and capacity**: how a rank becomes continue, stop or delay (for example "continue in rank order until the named capacity is used"), the capacity with unit and period, and any threshold. All the person's; "not given" otherwise.

Write the rule back, numbered, and ask the person to confirm it. Record the confirmation in the output. Ask which weighting method they used (SP-079); the method is theirs.

### Step 3. Facts, then scores

Build the items-by-criteria table with the A1 fact and its source in each cell and no score. Collect the person's weights (sum to 1) and 0 to 4 scores. Write them back for confirmation. A `[GAP]` cell stays visible even if scored. If the person's rule is RICE, collect reach, impact, confidence (a percent) and effort instead, and say RICE has no evidence, regulatory or capacity criterion unless they fold one in.

### Step 4. Rank

Call `analytics.mcda {alternatives: [{id, scores}], criteria_weights}` with the person's numbers only, or `analytics.rice {initiatives: [{id, reach, impact, confidence, effort}]}` with confidence as a percent. Drop an item with a missing score and list it as not ranked (a missing score returns HTTP 400, register C17). On 503, retry once; then compute by hand (value = 25 x sum of weight x score) and say the calculator was not used. With code execution, save the input and output and run `python3 scripts/portfolio_rank.py mcda FILE` (or `rice FILE`) to recompute and flag ties, weights that do not sum to 1, or a confidence sent on the wrong scale. Report each item's value and its largest contribution.

### Step 5. How firm is the rank

Run `python3 scripts/portfolio_rank.py swap FILE` (without code execution, work it by hand: move one weight, keep the others in proportion). State, for each adjacent pair, the weight at which they swap, and name the closest call. In the illustrative portfolio, Program C stayed above Program D unless "unmet need" rose from 0.30 to 0.36 (`examples/live/portfolio_rank_runs_output.md`). A swap point tests the person's weights; it never proposes new ones. For the pair at the capacity line (the last item inside the capacity and the first past it), also state the smallest one-point change in a recorded score that ties or reverses it: run `python3 scripts/portfolio_rank.py swap --scores FILE`, or show the arithmetic (one point on a criterion moves an item's value by 25 x that criterion's weight; compare with the gap between the two values). Label it a test, not a proposed score. In the illustrative portfolio, B (72.50) and C (65.00) differ by 7.50, and one point on unmet need (weight 0.30) is worth 7.50: B's need score falling from 4 to 3, or C's rising from 2 to 3, ties them (`examples/live/portfolio_rank_runs_output.md`). Never state what would change a ranking without this computation.

If the person wants more, offer sensitivity on their inputs only:
- `analytics.risk-tornado` on one item's weighted sum, `25 * (w1 * s1 + ...)`, with the person's own low and high for each score they are unsure of. Pass a range for every parameter; the default of plus or minus 20 percent is not theirs and moves weights off a sum of 1 (`tools.md`).
- `analytics.scenario-modeler` for a figure the person holds (for example their own probability of success times their own value measure) at the values they name, every parameter labeled theirs. Never enter a benchmark rate as the probability, and never a market size, price, valuation or return.
Both are **needs a live check** for portfolio formulas (`tools.md`).

### Step 6. Apply the decision rule and show the last item

Apply the person's decision rule to the rank as written, and show what it implies for each item as "implied by your rule", not as a decision. Name the item the rule places last. If capacity was given, run `python3 scripts/portfolio_rank.py capacity FILE` on the implied continue items and name the first item past the capacity. If every item would continue, say so: the old method's check is "do not continue every item".

### Step 7. Rule changes

If the person changes a weight, score or the rule after seeing the rank, record the new rule beside the first with the person's stated reason and show both ranks (old method: "Do not change the rule after you see the rank you prefer"). Do not judge the change.

## Build the output

Follow `assets/rule-and-ranking-output.md`. Answer first: the ranking as scored by the person, the closest call, the item the rule places last. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/portfolio_rank.py words ANSWER.md`.

## Before you hand it over

- The rule was written back and confirmed before the rank, and the output says so.
- Weights, scores, decision rule and capacity are the person's; any proposal is labeled "proposed" and was not ranked.
- Every [PAPER] row carries its DOI; every [WF] row says it was read through a summarizer.
- No benchmark used as a probability or a target; no market size, valuation, price or return.
- The rank is called arithmetic on the person's numbers, not the decision.
- Every statement of what would flip the rank was computed (script output or arithmetic shown), never estimated; any double counting between a scored criterion and the decision rule was put to the person.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model ranks what was scored and tests it; it does not choose, set weights or decide.
- Economic models behind a value criterion: `dh-access-and-value` economic-model-development.
- Recording the forum's decision: B2. Checking past decisions against the rule: `product-portfolio-review` (this pack).
