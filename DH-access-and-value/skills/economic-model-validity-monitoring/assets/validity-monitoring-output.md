# Output format: validity and input monitoring

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** two or three sentences: the evidence for validity by type, whether the reported numbers recompute, and how the result moves on the observed values. Never "valid" or "invalid".
2. **Validation evidence:** Type · Evidence shown, claimed, or none (HE-017, [PAPER] Eddy et al. 2012, DOI 10.1016/j.jval.2012.04.012, abstract only).
3. **Observed versus assumed:** Assumption · Model value · Observed value · Source and period · Result on observed values (quadrant, ICER where meaningful, net benefit at the person's threshold).
4. **Triggers:** which of the person's triggers were crossed, or "none set".
5. **Gaps and stop:** at most three gap lines; who decides.
6. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode (monitoring review)

### Answer

### Validation evidence by type
| Type | What it compares | Evidence in hand | Status |
|---|---|---|---|

### Recomputation
| Reported figure | Reported value | Recomputed | Tool or script | Match | Likely reason if not |
|---|---|---|---|---|---|

### Transparency and replicability

### Assumptions versus observed values
| Assumption | Model value | Observed | Source, period, population | Checked (Verify or study design) |
|---|---|---|---|---|

### Re-runs on observed values
| Scenario | dCost | dQALY | Quadrant | ICER | Net benefit at the person's threshold |
|---|---|---|---|---|---|

### Triggers and switching values

### Gaps

### Sources and record
Calls made. Row ids. AI-assisted draft. Stops for the owner. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
