# Output format: program change decisions

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line: who clears it, and that the record is built with `verify.build_record` once a named person clears it; otherwise "uncleared draft".

## Short mode (default for a direct question)

1. **Answer:** the activities that missed your rules, the decision you recorded for each (or "decision not made"), and the first decision in the dependency chain.
2. **Misses (compact):** Activity · Your rule · Result · Decision (yours) · Owner (yours or "owner not named").
3. **Ranking (if you scored changes):** order and scores, labeled the result of your numbers.
4. **Stops:** support changes to your compliance owner; partner payments and agreement remedies to your compliance or legal owner; off-list claims to your review owner.
5. **Record:** "Change decision draft. Rules, decisions, scores and owners are yours. Clears: [person or role as you named them, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft."
6. One line offering the full version.

## Full mode

### Answer

### Rule against result
| Activity | Your rule | Result (A2, as of DATE) | Met, missed or unscored |
|---|---|---|---|

### Options per miss
| Activity | Option (stop, change audience, change content) | Facts that bear on it | Stop it triggers |
|---|---|---|---|

### Decisions
| Activity | Decision (yours) | Owner (yours) | Next date (yours, if set) |
|---|---|---|---|

### Ranking of your scored changes (analytics.rice or analytics.mcda)
| Rank | Change | Score | Inputs (yours) |
|---|---|---|---|

### Sequence by dependency
| Decide | Before | Because | Row |
|---|---|---|---|
No urgency; dates only where you set them.

### Stops for the owner

### Gaps

### Calls made

### Record
Change decision draft. The ranking reflects your numbers; it is not a recommendation. AI-assisted. Clears: NAME (as you named them, or "owner not named"). The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
