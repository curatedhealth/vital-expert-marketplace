# Output format: lifecycle measures

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (the answer without the calls list, piped to `wc -w`), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** how many measures, for which stage pairs, and which one the current log cannot yet measure. Two sentences.
2. **Measures:** table # · Stage pair · Counts when (person's words, or "proposed") · Evidence required · Source rows or "your own" (every TM row carries DOI 10.1136/bmj.n2061 in the same cell, and every PL110 to PL120 row carries DOI 10.1097/SLA.0000000000004907) · Read by (script count or flag, or B1 judgment).
3. **Moves that do not count:** at most four lines, each with its row or "proposed".
4. **Not measurable yet:** the log field each needs.
5. **Gaps:** thresholds not set (yours to set; no benchmark in the sources `[GAP]`).
6. **Record (last line of the answer body):** "Lifecycle measures draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. **Calls made (after the record line):** list (usually none).

## Full mode

### Answer
### Measures as confirmed by the person
| # | Stage pair | Counts when | Evidence required | Rows | Read by |
|---|---|---|---|---|---|
### Moves that do not count
### Proposed measures (only if asked; not applied)
### Log fields needed
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
