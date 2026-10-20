# Output format: results and sensitivity

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** two or three sentences: the base case, its quadrant, net benefit at the person's thresholds, and the one input that most decides it. End with "Whether this is acceptable is [decision-maker]'s call."
2. **Drivers:** Input · Range (person's) · Net benefit low to high · Switching value. Top three only.
3. **Scenarios:** one line each for the scenarios run.
4. **Not shown:** probabilistic analysis and anything else not run.
5. **Gaps and stop:** at most three gap lines; "Results for [body or payer] stop for [the owner the person names, or owner not named], draft for the owner."
6. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode (results chapter or HTA annex)

### Answer

### Base case
| Comparison | dCost | dQALY | Quadrant | ICER | Net health benefit and net monetary benefit at each threshold the person gave |
|---|---|---|---|---|---|

### Thresholds as written
| Body | Text and version | Range as written | Row | Result's position (arithmetic) |
|---|---|---|---|---|

### One-way sensitivity
| Input | Base | Low | High | Reason for range | NMB low | NMB high | Swing | Switching value | Quadrant change |
|---|---|---|---|---|---|---|---|---|---|
Inputs with no range listed as "no range given". Tool or script named.

### Scenarios
| Scenario | Change | dCost | dQALY | Quadrant | ICER | NMB |
|---|---|---|---|---|---|---|

### What the analysis cannot show

### Evidence that would narrow the decision (advisory)

### Reporting items covered (CHEERS 2022, sourced items only, no score)

### Gaps

### Sources and record
Calls made. Row ids. AI-assisted draft. Stops for the owner. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
