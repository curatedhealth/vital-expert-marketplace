# Output format: price corridor evidence

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the record line, the guidance-status line for US payor material (PC-US-47), or the base EU device rule for any EU or German message (MDR Article 7, PC-EU-01, PC-EU-02). Refusals follow the same 450-word cap.

1. **Answer:** two or three sentences: what the registered evidence shows for each end, and that the corridor is the person's.
2. **Comparators:** Product · Status · Listed on · Price as stored · Source, retrieved. Low, high, count. The unit caveat in one line.
3. **Binding payer rule:** one or two rows with ids and validity window; "payer pricing: see dh-market-access".
4. **Models (only if run):** inputs (the person's, or adopted with their tool and source), result, "hypothesis"; a rejected or unexposed calculator is `[GAP]`.
5. **Reasons per end:** Floor: evidence. Ceiling: evidence. Ends not set: `[GAP]`.
6. **Gaps and record:** at most three gap lines; "Price positions stop for OWNER." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### The product's registered price
| Product | Scheme | Price as stored | Unit | Source | Retrieved |
|---|---|---|---|---|---|
One line on the corridor tool's set-aside rows (count), if it was called.

### Comparators
| Product | Manufacturer | Scheme | Status | Listed on | Price as stored | Unit stated? | Source | Retrieved |
|---|---|---|---|---|---|---|---|---|

### Payer rules (context; owned by dh-market-access)
| Market | Rule | Value | Valid | Row |
|---|---|---|---|---|

### Models on your numbers (hypotheses)
| Model | Your inputs | Defaults the tool applied | Result |
|---|---|---|---|

### Reasons for each end
| End | Evidence | Kind (rule, registered price, hypothesis) | Source |
|---|---|---|---|

### Gaps

### Sources and record
Calls made. Price positions stop for the owner. AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
