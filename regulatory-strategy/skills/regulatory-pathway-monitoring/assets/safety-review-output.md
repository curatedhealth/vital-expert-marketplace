# Output format: safety signal review

Short mode is 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line. A refusal or stop answer follows the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** one or two sentences: what the public records show and the main limit of what can be seen.
2. **Records:** Date · Source type · Product as named · Firm · Label as given · Stated reason (quoted) · In scope? · Source (retrieved DATE).
3. **Report counts:** product code · reports by year · "reports, not confirmed events"; not attributable to one product.
4. **Questions for the owner:** at most three, phrased as questions about the person's own risk file or pathway.
5. **Not visible:** one line (Swiss actions, EU vigilance, recalls without software terms).
6. **Record:** "Safety record summary as of DATE. No causal claims. Uncleared." or the clearer's name.

## Full mode

### Scope and what the library can see

Searches run (manufacturer, product, code, period) and the loaded sources per jurisdiction.

### Recalls

| Date | Product as titled | Firm | Classification label | Stated reason (quoted) | Scope check | Source, retrieved |
|---|---|---|---|---|---|---|

### MAUDE report counts

| Product code | Year | Reports | Basis |
|---|---|---|---|

### MHRA alerts

| Date | Title | Link |
|---|---|---|

### Off-scope rows

Rows returned for other products, one line each.

### Questions for the owner

Phrased as questions; reporting clocks given as context only.

### Gaps

Classified per `references/gap-rules.md`.

### Record

Public records described as stated. Reportability and any external wording stop for the vigilance owner (NAME, or owner not named). AI-assisted. Cleared by NAME, or uncleared.
