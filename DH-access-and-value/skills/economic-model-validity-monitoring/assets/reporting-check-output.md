# Output format: reporting and reference-case check

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** two or three sentences: what document was read, for which decision-maker, and the findings a reviewer would stop on. No score, no "compliant".
2. **Findings that matter:** Finding · Where in the document · Rule as written (row). Five rows at most, rule-currency and verdict-wording findings first.
3. **CHEERS items not found:** one line listing item numbers, "in this document"; one line for the unsourced items `[GAP]`.
4. **Gaps:** at most three lines.
5. **Record:** "AI-assisted draft. No CHEERS score is given (HE-005, DOI 10.1177/23814683211061097)." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode (pre-submission review)

### Answer

### What was read

### CHEERS 2022 items (sourced items only)
| Item | Topic | Row | Addressed, partly, or not found | Where | What is missing |
|---|---|---|---|---|---|
Unsourced items: `[GAP]`, check the checklist (DOI 10.1177/23814683211061097).

### Reference-case conformance: [body, text, version]
| Element | Rule as written | Row | Model's choice | Where | Match, differs, not stated |
|---|---|---|---|---|---|

### Rule currency
| What the model says | Current position | Row |
|---|---|---|

### Cited sources checked (if run)
| Input | DOI | Verify tier | Passage read, same direction? |
|---|---|---|---|

### Verdict wording
Sentence, row, proposed conditional wording.

### Gaps

### Sources and record
Calls made. Row ids. AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
