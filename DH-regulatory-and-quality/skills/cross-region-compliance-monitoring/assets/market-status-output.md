# Output format: market status by region

## Short mode (default for a direct question)

Short mode: 450 words maximum. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose (keep them in the table), secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Do not send a short-mode answer over 450 words. Offer the full version in one line. Refusals follow the same 450-word cap.

1. **Next dates and changes:** the two or three obligations with the nearest dates (date, days from the as-of date, row) and any status change since the baseline.
2. **Status by region:** Region · Library result (gap class) · Record (regime, class as recorded, identifier) · Retrieved.
3. **Obligations:** only the lines not already given in item 1, at most five (Region · Duty · Date or window · Days from as-of · Row); offer the full table in one line.
4. **Confirm with the owner:** at most three items (passed dates, gaps, dates that depend on inputs not given).
5. **Record:** "Uncleared draft" or the clearer's name.

## Full mode

### Summary
Two or three sentences: where the product stands, what changed, which dates come next.

### Baseline
What this run compares against (an earlier run with its date, the person's statement, or "none: current snapshot").

### Status by region
| Region | Library result | Regime and class as recorded | Identifier | Decision date | Change since baseline | Source, retrieved |
|---|---|---|---|---|---|---|

### Change log
What `get_register_deltas` returned, worded per `gap-rules.md`, and any change found by comparing runs.

### Obligations table
Output of `scripts/obligations_table.py`: Market · Obligation · Date or window · Status as of · Legal status · Basis (row).

### What it means for you
Conditional consequences from sourced mechanics. No prediction.

### Gaps
Each with its class and where to check.

### Record
Advisory draft. Cleared by NAME, or uncleared. AI-assisted.
