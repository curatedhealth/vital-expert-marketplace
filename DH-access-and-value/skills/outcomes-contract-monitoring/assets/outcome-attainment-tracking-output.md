# Output format: outcome attainment tracking

## Short mode (default for a direct question)

**Short mode: 450 words maximum, counted without tables' source column; aim for at least 250. Four parts only: the answer with its number, one table, open items (at most three), the record line. No rules list and no context paragraph in short mode: they belong to the full mode; offer the full version in one line.** The calls list is not counted.

1. **Answer:** attainment rate against the threshold (interim or final), the payment factor the rules give, the dollars on the right basis (for ACCESS BH initial, the $144 Medicare portion, never the $180 allowed amount), and the distance to the threshold in patients.
2. **One table, by measure:** Measure · Met · Not met · Missing · Not applicable.
3. **Open items (at most three):** rules the contract leaves open (`[GAP]`), data handed to the completeness check, verdicts handed to the review.
4. **Record:** "Computation on your data and rules. Attainment is not clinical evidence. Uncleared." or the clearer's name.

## Full mode

### Rules applied
| Measure | Target | Applies if | Window | Self-report allowed | Missing treated as | Source (yours / public rule, row) |
|---|---|---|---|---|---|---|
Plus: rule family (patient all-or-nothing or population average), dropouts in denominator, threshold, payment link.

### Results by measure
| Measure | Met | Not met | Missing | Not applicable | Mean change (population rule) |
|---|---|---|---|---|---|

### Results by patient (patient-level rules)
| Patient | Status | Each measure | Outcome |
|---|---|---|---|
De-identified ids only.

### Attainment and payment
Rate, threshold, payment factor, per-patient and total amount on the person's figures. Distance to threshold. Second adjustments not computed, named.

### Gaps
Each `[GAP]` with its reason.

### Record
Computation on the person's data and rules; interim or final. Contract changes and payer wording stop for the accountable owner. Cleared by NAME, or uncleared. AI-assisted draft.
