# Output format: money flow and value unit

Two modes. Pick by the request (see the task guide). Both keep the same order; the short mode compresses.

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the record line, the guidance-status line for US payor material (PC-US-47), or the base EU device rule for any EU or German message (MDR Article 7, PC-EU-01, PC-EU-02). Refusals follow the same 450-word cap.

1. **Answer:** per market, one sentence: who uses, who buys, who pays, for which unit.
2. **Roles table:** Market · User · Buyer · Payer · Route (rows) · Listing status (source, retrieved). Germany route: for a DiGA, one line: the DiGA must be ad-free and may not use opaque offers such as auto-renewing subscriptions (PC-DE-15, PC-DE-17); this limits the offer models the unit can carry.
3. **Value unit:** the unit, what it includes, what it excludes, or `[GAP]` with the question to the person.
4. **Stops:** one line per stop, with rows and the owner the person named (or "owner not named").
5. **Gaps:** at most three lines.
6. **Calls and record:** calls made; "Library records retrieved DATE; confirm on the authority's page." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

End with one offer: the full version, or the next task (A2 price corridor evidence).

## Full mode (pricing paper, board, document to share)

### Answer
Two or three sentences.

### Roles by market
| Market | User | Buyer | Payer | Route the money takes | Rows | Listing status | Source, retrieved |
|---|---|---|---|---|---|---|---|

### Value unit
| Unit | What the buyer receives | Excluded | Matches a route's unit? | Rows |
|---|---|---|---|---|

### Rules the flow touches
| Point in the flow | Rule | Row | Kind (law, guidance, [INDUSTRY]) |
|---|---|---|---|

### Stops for the owner
| Arrangement | Why it stops | Rows | Owner you named |
|---|---|---|---|

### Gaps
Grouped by class from `references/gap-rules.md`.

### Sources and record
Numbered sources with URL and retrieval or read date. Calls made. AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
