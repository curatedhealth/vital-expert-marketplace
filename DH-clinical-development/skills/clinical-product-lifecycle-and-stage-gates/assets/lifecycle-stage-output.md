# Output format: lifecycle stage map

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (the answer without the calls list, piped to `wc -w`), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the stage (person's name, and the sourced vocabulary it maps to), the owed item that blocks the next stage, and what it blocks. Two sentences.
2. **What the stage owes:** table Work product · Named by (row) · Present, missing or [GAP] (with the person's reference). In the Named by cell, every TM row carries the DOI beside it ("TM14, DOI 10.1136/bmj.n2061"), and every PL110 to PL120 row carries DOI 10.1097/SLA.0000000000004907, even if the DOI also appears in prose. At most eight rows; the rest stay in full mode.
3. **Blocks, by dependency:** one line per blocked step.
4. **Comparable product (only if named):** the dated timeline from `scripts/lifecycle_timeline.py`, at most five rows, with reference numbers and retrieval dates; MAUDE counts labeled "reports, not confirmed events". One line: "Records only; reasons, market status and outcome are not stated by the record."
5. **Decisions for the person:** at most three, each with the fact behind it.
6. **Gaps and stops:** device status `[GAP]` if not stated, pointing to `dh-regulatory-and-quality` regulatory-pathway-and-classification.
7. **Record (last line of the answer body):** "Lifecycle stage map draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
8. **Calls made (after the record line):** list (often none).

## Full mode

### Answer
### Stage placement
Person's stage name · Vocabulary and rows (DOI beside [PAPER] rows) · Facts that place it
### What the stage owes
| Work product | Named by | Rows | Status | Person's reference |
|---|---|---|---|---|
### Blocks, by dependency
### Comparable product timeline
### MRC/NIHR core element questions (proposed, complex interventions only)
### Decisions for the person
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
