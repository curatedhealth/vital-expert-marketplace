# Output format: partner and initiative prioritization (B1)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question; 250 to 450 words)

1. **Answer:** the order your scores produce, with values, and how robust it is (the smallest weight change that flips the top two). If no scores yet: "No ranking until you score" and the facts per option.
2. **Facts that bear on the choice:** at most five, each with its row, or with its source (dossier or peer screen) for options from research.
3. **What to settle first:** the first link in the dependency chain and why (row).
4. **Stops:** fraud-and-abuse triggers on any option; owner as you named them, or "owner not named".
5. **Record:** "Prioritization draft. Scores, weights and the choice are yours; the ranking is not a recommendation. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. One line offering the full version.

## Full mode

### Answer

### Facts per option
| Option | Criterion | Sourced fact | Row |
|---|---|---|---|

### Your scores and weights (MCDA) or your RICE inputs
| Option | Criterion 1 | Criterion 2 | ... |
|---|---|---|---|
| Weight | | | |

| Initiative | Reach (your unit) | Impact | Confidence (percent) | Effort (your unit) |
|---|---|---|---|---|

### Ranking (connector on your numbers)
| Rank | Option or initiative | Value or score | Largest contribution |
|---|---|---|---|

### Robustness
| Pair | Criterion | Your weight | Weight at which they swap |
|---|---|---|---|

### Sequence by dependency
| Settle | Before | Because | Row |
|---|---|---|---|
No dates; legal clocks are facts.

### Stops for the accountable owner

### Gaps

### Calls made

### Record
Prioritization draft. The ranking reflects your scores; it is not a recommendation. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
