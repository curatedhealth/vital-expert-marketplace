# Output format: public launch signals

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** two or three sentences: what changed since the launch date (or that the library cannot show change, and the baseline date), the clock that matters most, and what touches the field.
2. **Events:** table Date · Product (identifier) · Event · Source, retrieved. Peers labeled comparables.
3. **Clocks and moved rules:** at most four lines, each with row and instrument.
4. **Gaps:** at most three lines, one per class.
5. **Record:** "Library copy, retrieved DATE; confirm on the authority's page." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

End with one offer: the full version, or the next task (A2 launch measures).

## Full mode

### Answer

### What the library can see

### Change feed
Feed by feed as returned by `get_deltas`, including `[GAP]` lines.

### Sequence now, and differences from the earlier run
| Product (identifier) | Event | Date now | Date in earlier run | Difference | Source, retrieved |
|---|---|---|---|---|---|

### Cohort
| Product | Status (source wording) | Listed | Trial end | Source, retrieved |
|---|---|---|---|---|

### Clocks and moved rules
| Clock or rule | Date and instrument | Touches | Rows |
|---|---|---|---|

### Gaps

### Calls made

### Record
Draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
