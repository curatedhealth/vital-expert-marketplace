# Output format: launch claim list (proposed, for approval)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** N claims proposed, N flagged, the most important flag and who approves (owner as named, or "owner not named").
2. **Claims:** table ID · Claim (verbatim) · Market and audience · Source · Flag · Rows. Flagged claims only if over the word cap, with the count of unflagged ones in one line.
3. **Safer wording:** for each flagged claim, one line labeled "draft for the owner".
4. **Not on the list:** claims with no source, in one line each with `[GAP]`.
5. **Stops:** one line per owner.
6. **Record:** "Proposed claim list for approval by OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### Authorization the list must stay within
The labeling or intended-use text the person supplied, quoted, with its source. If none: `[GAP]`.

### Proposed claim list
| ID | Claim (verbatim) | Market | Audience | Evidence (source, passage) | Verify result | Connector label | Flag | Rows |
|---|---|---|---|---|---|---|---|---|

### Safer wording (draft for the owner)
| ID | Original | Draft | Why (rows) |
|---|---|---|---|

### Not on the list
| Claim | Reason | Next step |
|---|---|---|

### Rules applied
Market and audience rules used, with rows; [INDUSTRY] and [WF] labeled.

### Stops for the accountable owner

### Gaps

### Calls made

### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
