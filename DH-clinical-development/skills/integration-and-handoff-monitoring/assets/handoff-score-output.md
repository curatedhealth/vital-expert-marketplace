# Output format: handoff score for a period

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** period, rule applied (person's, dated), counts received, late, open, not measurable; critical-to-quality handoffs late or open; on-time over measurable with its denominator.
2. **Late and open:** table Work product · Category · CTQ (person's mark) · Status · Fact (dates, names) · Source (log row).
3. **Not measurable:** one line each with what is missing, `[GAP]`, and the question to the person (for example "who receives H9?"). Never rule on it.
4. **By category:** one line per category and CTQ mark, never merged.
5. **Record:** "Handoff score, [period], draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
6. **Calls made** (after the record line): list (script run included).

## Full mode

### Answer
### Rule applied (person's words, version date)
### Every handoff scored
| id | Work product | Category | CTQ | Status | Fact | Carried in | Source |
|---|---|---|---|---|---|---|---|
### Counts by status, category and CTQ mark
### Public records the person asked about (quoted, with date, severity, source; no cause inferred)
### Feedback: who receives this score (the person's choice; CS44 pattern)
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
