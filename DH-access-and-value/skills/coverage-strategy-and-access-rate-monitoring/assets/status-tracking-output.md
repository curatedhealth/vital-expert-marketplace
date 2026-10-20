# Output format: coverage status tracking

## Short mode (default for a direct question; aim for 250 to 450 words)

1. **What changed or is about to:** one to three sentences, each with a date and source.
2. **Status by market:** Market · Status in plain words · Listed · Clock and flag · Source (retrieval date).
3. **Comparables:** one line per scheme (for example "In this indication on DE_DIGA: 3 on trial, 2 permanent, 1 deleted after 16 months").
4. **What it means for you:** one to three conditional lines from sourced mechanics.
5. **Check at the authority:** at most three items (gaps, disagreements, expired clocks).
6. **Record:** "Uncleared draft" or the clearer's name.

## Full mode

### Summary
Two or three sentences: what changed since the baseline, what is about to, and what the person should check.

### Baseline
What this run compares against (an earlier run with its date, the person's statement, or "none: current snapshot").

### Status by market
| Market and scheme | Status in plain words | Listed | Price where stated | Change since baseline | Source and retrieval date |
|---|---|---|---|---|---|

### Running clocks
| Market | Clock (from `lapse-signals.md`) | Counted from | Elapsed | Signal to check |
|---|---|---|---|---|

### How comparable products fared
| Scheme | Comparable products (indication) | On trial | Permanent | Deleted (time to deletion) | National context |
|---|---|---|---|---|---|
Comparables are what happened to other products, not a forecast for this one.

### What it means for you
Conditional consequences from sourced mechanics (price clock, wind-down, same-manufacturer listings). No prediction.

### Gaps and disagreements
Each with its class from `gap-rules.md` and where to check.

### Watch
Only if requested: scheme, product, snapshot hash, time registered, and the note that changes appear after the next library refresh.

### Record
Advisory draft. Cleared by NAME, or uncleared.
