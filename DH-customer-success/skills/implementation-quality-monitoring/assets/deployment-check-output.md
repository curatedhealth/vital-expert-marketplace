# Output format: deployment check

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** per site, bar items with evidence seen out of all items, the items without evidence seen, and go-live slippage from the agreed date, as of the date used.
2. **Bar check (compact):** Item · Evidence (seen with id / described / status field only / none) · Met under your rule. Without a rule, the evidence column only.
3. **Field events (if asked):** each event as its record states, with the openFDA API caveat.
4. **What it means for you:** two lines from the rows.
5. **Stops:** no statement to the customer that the site is live; the site approver agrees.
6. **Record:** "Deployment check draft on your evidence. Cleared by NAME; record built with verify.build_record." Until a named person clears it: "Deployment check draft on your evidence. Uncleared draft." AI-assisted. Refusals carry the same line.
7. **Papers:** one line, each [PAPER] paper used once with its DOI (not counted toward the 450 words); omit if none was used.
8. One line offering the full version.

## Full mode

### Answer

### Site: NAME (agreed go-live DATE, actual DATE or not met)
| # | Bar item (yours) | Evidence type needed | Evidence status | Evidence id (yours) | Met under your rule | Row |
|---|---|---|---|---|---|---|

Rule applied: yours, or the register starter rule you adopted ("missing evidence counts as not met"), or none.

### Slippage
| Item | Agreed date | Met on | Days from agreed date | Re-baselined to |
|---|---|---|---|---|

### Field events for the product since go-live (if asked)
| Event as its record states | Date | Class or alert | Source |
|---|---|---|---|

### Gaps

### Calls made

### Record
Deployment check draft. Evidence and rules are yours; the site approver agrees the bar is met. AI-assisted. Cleared by NAME; record built with verify.build_record. Until a named person clears it: uncleared draft.

### Papers
Each [PAPER] paper used, once, with its DOI.
