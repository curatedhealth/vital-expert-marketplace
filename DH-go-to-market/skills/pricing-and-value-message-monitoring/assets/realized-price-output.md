# Output format: realized price tracking

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** deals counted, how many below, inside and above the corridor, realized price range per currency, period.
2. **Rules used:** one line: "Deal set, realized-price rule and corridor are yours: ..."
3. **Deals outside the corridor:** Contract id · Realized unit price · Position · Discount from list.
4. **Stops:** deals with referral- or volume-linked terms, free units or self-pay prices, with rows and owner.
5. **Gaps and record:** missing fields; "AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### Rules (yours)
| Rule | Your wording | Confirmed on |
|---|---|---|

### Deal table
| Contract id | Type | Date | Units | Value | Realized unit price | Currency | List | Discount | Position |
|---|---|---|---|---|---|---|---|---|---|

### Excluded deals
| Contract id | Why excluded (other unit, currency, payer-set) |
|---|---|

### Summary
Counts and shares per position; median and range per currency; arithmetic shown. National context with period (for example DE-9), labeled context.

### Stops
| Deal | Feature | Rows | Owner you named |
|---|---|---|---|

### Gaps and record
Missing fields. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
