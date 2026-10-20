# Output format: message fidelity audit (flags for the owner, not a clearance)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** N statements; Stop, Review, Note counts; the drift that matters most, in one sentence. "This audit flags; it does not clear."
2. **Flag table:** Statement · Drift type · Rows · Level · Faithful draft for the owner.
3. **Evidence:** one line per source: passage read, currency checked (source), certainty rating used (rater) or [GAP].
4. **Record:** "Communication not cleared. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Basis
Communication audited, audience, market, intended use (source), studies and passages, ratings and raters.

### Statements
| # | Statement (as written) | Passage (locator) | Direction, population, comparator, outcome, time point, effect | Certainty claimed vs rated | Drift type | Rows | Level |
|---|---|---|---|---|---|---|---|

### Faithful drafts for the owner
| # | Statement | Faithful draft | What it keeps | What it drops |
|---|---|---|---|---|

### Decisions for the owner
Numbered: each Stop and Review, each [INDUSTRY] or [WF] row relied on, each gap.

### Calls and record
Calls made with arguments. Verify statuses shown beside the own reading. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The record covers the audit, not the communication.
