# Output format: evidence communication review

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** rules met and missed, as of DATE, in one or two sentences.
2. **Rule table:** Rule (the person's words) · Result · Number and date · Met, missed or [GAP].
3. **Main miss:** one-off or pattern, both readings with their facts; owner as named.
4. **Decision needed:** one line, for whom.
5. **Record:** "AI-assisted draft." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Pass rules (the person's, confirmed on DATE)
| # | Rule | Measured by | Owner (person's words) |
|---|---|---|---|

### Results
| Rule | Result | Number behind it | As of | Verdict |
|---|---|---|---|---|

### Misses: one-off or pattern
| Miss | Facts toward one-off | Facts toward pattern | Hypothesis and what would confirm it |
|---|---|---|---|

### Responses
| Miss | Responding work | Owner |
|---|---|---|

### Calls and record
Inputs used (A1, A2, the person's data). AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
