# Output format: economic case gap check

## Short mode (default; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** per body, one or two sentences: what is shown, the departures, what is open; "the body concludes on cost-effectiveness, not this check".
2. **Items table (asked body):** Item · Status (shown, not shown, departure, `[GAP]`, not applicable) · Where in the material · Row.
3. **Studies:** one line each: DOI · design label and CEBM level from design only · retraction and currency.
4. **Claims:** one line each: claim · checked or not checked · passage locator · why (for example "interval includes zero").
5. **Arithmetic (hypotheses):** at most three lines: ratio (and the source's own), net monetary benefit at the person's thresholds, budget impact on the person's numbers, with inputs; any calculator `[GAP]`.
6. **Calls and record:** calls made with dates. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

End with one offer: the full check, or B1 (gap plan and economic section).

## Full mode

### Answer

### Material checked
What it is (paper, report, parameter list), date, sections used.

### Items by body
| Body | Item | Status | Where in the material | Row | What would close it |
|---|---|---|---|---|---|

### CHEERS 2022 reporting (not a score)
| Item | Reported or not | Where | Row |
|---|---|---|---|

### Studies the model rests on
| Study (DOI, PMID) | Design (decided by) | CEBM level from design only | Retraction and currency | Registry id (from the paper) | Source |
|---|---|---|---|---|---|

### Claims checked
| Claim | Passage (verbatim) | Locator | Verify status | Read as | Why |
|---|---|---|---|---|---|

### Arithmetic on your numbers (hypotheses)
| Computation | Inputs | Result | Tool or script | Note |
|---|---|---|---|---|
Beside any ratio: the body's written ranges with rows (both NICE ranges), "the body decides".

### What it means
Facts per body; departures for the owner to decide.

### Sources and record
Rows, DOIs, calls with dates. AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
