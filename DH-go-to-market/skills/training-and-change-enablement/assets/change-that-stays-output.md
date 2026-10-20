# Output format: change that stays (change plan and option ranking)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line.

## Short mode (default for a direct question)

1. **Answer:** the old step, who checks, after how many days, and what happens if it did not stop (your values, or blank with "ask"). Then the order your scores produce, with values, and the smallest weight change that flips the top two. If no scores yet: "No ranking until you score" and the facts table.
2. **Facts that move the choice:** at most five, each with its row; the design option always beside the training options.
3. **What to do first:** the first link in the dependency chain and why.
4. **Stops:** what goes to which owner; owners as you named them, or "owner not named".
5. **Record:** "Change plan draft. Scores, weights and the choice are yours." Then who clears it: "Cleared by NAME; the record is built with `verify.build_record` once NAME clears it", or, with no name, "uncleared draft". AI-assisted.
6. One line offering the full version.

## Full mode

### Answer

### The change
| Old step | New step (task card) | Who checks | After (days, yours) | If it did not stop |
|---|---|---|---|---|

### Facts per option
| Option | Sourced fact | Row |
|---|---|---|

### Your scores and weights
| Option | Criterion 1 | Criterion 2 | ... | Weight row |
|---|---|---|---|---|

### Ranking (analytics.mcda on your scores)
| Rank | Option | Value (0 to 100) | Largest contribution |
|---|---|---|---|

### Robustness
| Pair | Criterion | Your weight | Weight at which they swap |
|---|---|---|---|

### Sequence by dependency
| Do | Before | Because | Row |
|---|---|---|---|
No dates; clocks in the rows are facts.

### Stops for the accountable owner

### Gaps

### Calls made

### Record
Change plan draft. The ranking reflects your scores; it is not a recommendation. AI-assisted. Cleared by NAME (as the person named them); the record is built with `verify.build_record` once NAME clears it. With no name: uncleared draft.
