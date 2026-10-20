# Output format: review currency and change signals

## Short mode (default for a direct question; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** the date check for the named body (script lines), publication-status signals, the count of candidate new studies, and the one decision the person must make next.
2. **Search date:** date, locator in the paper, or `[GAP]`.
3. **Rule check:** Body · Rule (row) · Result (from `scripts/review_check.py`).
4. **Publication status:** Paper · Retraction, correction or concern (source, date).
5. **Candidate new studies:** Record · Date · Draft design label · "not screened".
6. **Superseded methods or guidance** the review used, if any.
7. **Calls made:** list.
8. **Record:** "AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft." This line appears in every answer, refusals included; never drop the verify.build_record clause.
9. One line offering the full version.

## Full mode

### Summary
### Search date and rule checks
| Body | Rule | Row | Last search | Target date | Result |
|---|---|---|---|---|---|

### Publication-status signals
| Paper | Tool | Status | Notice and date | Source checked | Read on |
|---|---|---|---|---|---|

### New-study signals
| Record | Date | Found by (cited_by or search) | Library design label (draft) | On topic? (person) |
|---|---|---|---|---|

### Method and guidance signals
| What the review used | What changed | Row |
|---|---|---|

### What it means (sourced consequences only)
### Calls made
### Record
AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. This line appears in every answer, refusals included.
