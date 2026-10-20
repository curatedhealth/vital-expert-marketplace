# Output format: stage status read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (the answer without the calls list, piped to `wc -w`), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 1 and 2 from `scripts/gate_log_check.py` output; do not recount by hand.

1. **Answer:** as of the read date, the stages with missing or in-progress items, the longest-open stage and its days open, and the flags that bear on the person's measures. Two sentences.
2. **Stage table:** as the script prints it (stage, owed, accepted, missing, in progress, waived, days open, flags).
3. **Flags that matter:** at most five, item by item, each with one line of source context (F1 PL9; F2 PL5; F4 TM3, DOI 10.1136/bmj.n2061).
4. **Measures (if A1 exists):** met, not met or not measurable, with the count behind each.
5. **Post-market inputs (marketed product only):** date, type, severity, record summary as stated, reference and each record's own retrieval date; no judgment of its relevance to the person's product. Whether it reopens a stage is the person's call: the stage they name, or "stage not named; your call". "Whether it needs a submission: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control." MAUDE counts labeled "reports, not confirmed events".
6. **Gaps.**
7. **Record (last line of the answer body):** "Stage status read draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
8. **Calls made (after the record line):** list.

## Full mode

### Answer
### Stage table (script output)
### Flags by item
### Measures
### Post-market inputs
| Date | Event | Severity | Record summary | Source and retrieval date | Stage the person names (or "your call") | Context rows |
|---|---|---|---|---|---|---|
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
