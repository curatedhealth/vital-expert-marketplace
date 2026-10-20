# Output format: model inputs and runs

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** two or three sentences with the headline result, its quadrant or year-by-year net impact, and "hypothesis on your inputs".
2. **Key inputs:** Input · Value · Source kind · Checked? Only the inputs that move the result; blanks shown as `[GAP]`.
3. **Results:** a table with the tool or script that computed each figure. ICER only with its quadrant. Net benefit only at thresholds the person gave.
4. **Reference-case mismatches:** one line each, if any.
5. **Gaps:** at most three lines, including any tool failure and the fallback used.
6. **Record:** "Calls: [list]." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode (model report or technical appendix)

### Answer

### Input register
| Input | Value | Unit | Year | Currency | Source kind | Source | Checked (Verify status, passage read) |
|---|---|---|---|---|---|---|---|

### Reference-case check
| Element | Body's rule (row) | Model's choice | Match |
|---|---|---|---|

### Budget impact (if run)
| Year | Population | Uptake | Patients | Current mix cost | New cost | Condition cost change | Net impact | Cumulative |
|---|---|---|---|---|---|---|---|---|
Tool or script, perspective, horizon, displacement assumption, discounting.

### Cost-utility or cost-comparison (if run)
| Arm | Cost | QALYs | Cost discounted | QALYs discounted |
|---|---|---|---|---|
| Comparison | dCost | dQALY | Quadrant | ICER | Net benefit at the person's thresholds |
|---|---|---|---|---|---|

### Value-based ceiling (only if asked)
| Threshold (person's) | Ceiling | Defaults the tool applied |
|---|---|---|
"A ceiling is not a price. Price positions stop for the owner the person names for pricing, or owner not named."

### Calculation check
Tool versus script, match or difference.

### Gaps

### Sources and record
Calls made with arguments. Published inputs with DOI and Verify status. AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
