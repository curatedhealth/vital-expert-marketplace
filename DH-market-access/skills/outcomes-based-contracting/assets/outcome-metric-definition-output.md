# Output format: outcome metric definition

## Short mode (default for a direct question)

**Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.** The calls list is not counted; aim for at least 250 words.

1. **Answer:** the two or three measures that are proposed on the facts (write "proposed"), and the one decision the person must make. The person chooses.
2. **Candidates:** Measure · Source (yours or official set, row) · Data source and owner · Burden (one fact) · Attribution risk (one fact) · Baseline needed.
3. **Limits of the official set:** at most three lines (for example "AbEM PROMs from 2027; permanent DiGA only; participation voluntary").
4. **Open inputs:** owners or data sources not named.
5. **Record:** "Draft for the owner. Measures are not chosen until NAME decides. Uncleared." or the clearer's name.

## Full mode

### What this lists
One paragraph: product, indication, market, payer; which measures came from the person and which from an official set.

### Candidate measures
| # | Measure | Definition (instrument, unit, window) | Origin (yours / official set, row) | Data source and owner | Collection burden (facts) | Attribution risk (facts) | Baseline need |
|---|---|---|---|---|---|---|---|

Ratings, if the person gave them, in brackets; proposed ratings marked "proposed".

### Measures that need a decision
Data not available in time, no owner, use standing in for health, baseline not taken today.

### Comparables (if run)
Product · Status · Recorded price · Retrieved. One line: the library holds no comparator's outcome terms.

### Instruments checked (if asked)
Claim · Source · Status from `check_claim` · Passage.

### Gaps
Each `[GAP]` with its reason.

### Record
Draft for the owner. Choosing contract measures and any clinical claim stop for the accountable owner. Cleared by NAME, or uncleared. AI-assisted draft.
