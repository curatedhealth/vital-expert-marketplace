# Output format: evidence statement

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** one sentence per outcome: effect as reported, population, comparator, time point, number of studies, certainty with its rater or "certainty not rated [GAP]".
2. **Table:** Outcome · Statement · Passage (locator) · Same direction? · Certainty (rater, date) · Source.
3. **Checks:** design and registry id checked against the paper; retraction status and the source checked.
4. **Gaps:** at most three lines, by class (`references/gap-rules.md`).
5. **Record:** "AI-assisted draft." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode (dossier input, evidence summary, Summary of Findings)

### Answer
### Studies in the statement
| Study | Design (checked against) | Registry id (from) | N | Retraction check (source) | Citation |
|---|---|---|---|---|---|

### Statements by outcome
| Outcome (measure, time point) | Population | Comparator | Effect as reported | Passage locator | Verify status and own reading | Certainty, rater, date, reason if below high |
|---|---|---|---|---|---|---|

### Summary of Findings (only if the person rated certainty)
Population and setting, comparison, up to seven outcomes, comparator burden, absolute and relative effects, participants and studies, certainty, comments (ES-97, ES-98, ES-99).

### What this statement does not say
Outcomes with no passage, populations not studied, comparators not tested.

### Calls and record
Calls made with arguments. Library fields not used and why (starting-level grade, empty table fields). Searches cover the loaded sources only. AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
