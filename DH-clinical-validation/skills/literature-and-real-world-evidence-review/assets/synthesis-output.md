# Output format: synthesis and evidence table

## Short mode (default for a direct question; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** per critical outcome, what the studies report in plain words with its limits; pooled or not and why (row); certainty "reviewers' rating" or "not yet rated"; the one decision the reviewers must make next. Never "proves".
2. **Flow:** the PRISMA 2020 counts and reconciliation result.
3. **Evidence table check:** the problems `scripts/check_evidence_table.py` printed.
4. **Summary of Findings (condensed):** Outcome · Studies (participants) · Effect as reported · Certainty (reviewers) · Note.
5. **Pass rule:** the person's rule in their words and each outcome against it, or "pass rule not given [GAP]".
6. **AI use** (mandatory for a JCA).
7. **Calls made:** list.
8. **Record:** "AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft." This line appears in every answer, refusals included; never drop the verify.build_record clause.
9. One line offering the full version.

## Full mode

### Summary
### PRISMA 2020 flow
Counts in ES-20 [PAPER] doi 10.1136/bmj.n160 order, excluded full texts with reasons, update counts if any.

### Pooling decision per outcome
| Outcome | Studies | Comparators | Measures and time points | Direction | Options and rules (rows) | Reviewers' choice |
|---|---|---|---|---|---|---|

### Certainty set-up per outcome (GRADE)
| Outcome | Start (design) | Risk of bias | Inconsistency | Indirectness | Imprecision | Publication bias | Upgrades | Rating (reviewers) | Explanation |
|---|---|---|---|---|---|---|---|---|---|

### Summary of Findings
| Outcome | Comparator burden | Relative effect | Absolute effect | Participants (studies) | Certainty | Comments |
|---|---|---|---|---|---|---|

### Evidence table and check
The table, then the script's missing fields, problems and notes.

### Findings checked
| Finding | Passage and locator | Verify status | Same direction read? |
|---|---|---|---|

### Pass rule and owners
| Item | Person's rule | Status | Owner (as named) |
|---|---|---|---|

### AI-use table
### References
Citations from `literature.build_citation`.

### Calls made
### Record
AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. This line appears in every answer, refusals included.
