# Output format: coding pathway map

## Short mode (default for a direct question; 250 to 450 words)

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.


1. **Answer:** the route or routes that fit, and the one condition that decides each (for example "G0552 to G0554 fit only if the device is FDA cleared at 21 CFR 882.5801 and the billing practitioner buys it").
2. **Routes by market:** Market · Route and codes · What is paid (service, product, contract) · Who bills · Fits / Does not fit / Unclear · Row or library source.
3. **Conflicts:** one line per pair of routes that cannot be combined.
4. **Pending changes:** at most three, each "proposed DATE; final rule not published".
5. **Gaps:** at most three, each with where to check.
5a. **Next steps:** at most three, each naming the owner the person named; if none is named, write "owner not named" and ask. Never suggest a job title. No price.
6. **Record:** "Uncleared draft" or the clearer's name.

## Full mode

### Summary
Two or three sentences: which routes fit, the decisive conditions, the largest pending risk.

### Library coverage
| Scheme | Listings | Last load | What it holds for this map |
|---|---|---|---|

### Map by market
| Market | Route | Codes or identifier | What is paid | Who bills | Entry conditions | Product meets it? | Source (row or library, date) |
|---|---|---|---|---|---|---|---|

### Stored code rows
| Code | Description | Amount as stored (setting) | Conversion factor | Source, retrieved |
|---|---|---|---|---|
National amounts, before geographic adjustment. Not a payment the product will receive.

### Conflicts between routes
| Route A | Route B | Rule | Row |
|---|---|---|---|

### Pending changes (dated risk, not law)
| Proposal | Proposed on | Status | Effect on this map | Row |
|---|---|---|---|---|

### Gaps
Each with its class from `gap-rules.md` and the authority to check.

### Record
Advisory draft. Coding decisions stop for the accountable owner. Cleared by NAME, or uncleared.
