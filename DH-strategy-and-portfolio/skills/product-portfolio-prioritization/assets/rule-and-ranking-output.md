# Output format: prioritization rule and ranking

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/portfolio_rank.py words ANSWER.md`.

## Short mode (default for a direct question)

1. **Your rule (confirmed before ranking):** criteria and weights; anchors in one line each; decision rule; capacity. Any part not given: "not given". Any proposal: "proposed, not used until you confirm".
2. **Ranking as scored by you:** Item · Value (0 to 100) · Largest contribution. Method as returned by the tool (EVIDEM weighted sum) or RICE; "arithmetic on your numbers, not a decision". Not ranked: item and missing score.
3. **Closest call:** the pair and the weight at which they would swap; for the pair at the capacity line, the smallest one-point score change that ties or reverses it (computed with `swap --scores` or with the arithmetic shown, labeled a test). Any scored criterion that double counts the decision rule (for example capacity fit beside a capacity cut), put to you.
4. **Implied by your rule:** what your decision rule gives each item, labeled "implied by your rule"; the item your rule places last; capacity check if given.
5. **Stops:** benchmark asked as a probability, licensing conclusions, external wording, with the owner you named or owner not named.
6. One line offering the full version.
7. **Record:** "Ranking draft. Rule, weights, scores and the decision are yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made (after the record line): calls with arguments, or "computed by hand (calculator not used)" with the reason.

## Full mode

### The rule as you confirmed it
| Criterion | 0 means | 2 means | 4 means | Weight | Weighting method (yours) |
|---|---|---|---|---|---|
Decision rule. Capacity. Checks put to you: completeness (SP-076), double counting (SP-077), preference independence (SP-078); all [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016.

### Facts behind the scores
| Item | Criterion 1 | Criterion 2 | ... |
|---|---|---|---|
Each cell: fact with source, then your score in brackets. A `[GAP]` cell says so.

### Ranking
| Rank | Item | Value | Contributions |
|---|---|---|---|

### How firm
| Pair | Criterion | Current weight | Swap at |
|---|---|---|---|

| Pair | Values | Gap | One-point change that ties or reverses | Effect of one point (25 x weight) |
|---|---|---|---|---|
Computed with `scripts/portfolio_rank.py swap --scores` or by the arithmetic shown; a test of your scores, not a proposed score.

### Sensitivity on your inputs (only if asked)
Tool, formula, your ranges per parameter (or "default plus or minus 20 percent applied, not yours"), result. Every parameter labeled yours.

### Implied by your rule
| Item | Rank | Implied (continue, stop, delay) | Capacity use (yours) | Running total |
|---|---|---|---|---|
Item placed last. If every item would continue: "do not continue every item" put to you.

### Rule changes after the rank
Old rule, new rule, your stated reason, both ranks.

### Record
Ranking draft for the owner. No benchmark used as a probability; no market size, valuation, price or return. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
