# Output format: screening, extraction and appraisal

## Short mode (default for a direct question; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** studies and reports included so far, the problems found (from the scripts, verbatim), and the one decision the reviewers must make next.
2. **Flow counts:** from `scripts/prisma_flow.py`, with the reconciliation result.
3. **Design check:** Report · Library label (basis) · Design from the paper (basis) · Note.
4. **Risk-of-bias set-up:** Result · Tool (row) · Domains with "passage found" or "No information" · Judgment: reviewers.
5. **Retractions and registrations:** Report · Retraction (Crossref, date) · Registry id.
6. **AI use:** steps and responsible human.
7. **Calls made:** list.
8. **Record:** "AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft." This line appears in every answer, refusals included; never drop the verify.build_record clause.
9. One line offering the full version.

## Full mode

### Summary
### Deduplication and study grouping
| Study | Reports (DOI, PMID, registry) | Merge rule | Grouped by |
|---|---|---|---|

### Screening against the body's rule
Script output (counts, reconciliation, problems) and the rule applied with its row.

### Design check (register N8)
| Report | Library label | decided_by | Design from the paper | Basis | Publication type |
|---|---|---|---|---|---|

### Extraction sheet
| Study | Outcome | Time point | n | Effect | Measure | Interval | Locator |
|---|---|---|---|---|---|---|---|

### Risk of bias layout
| Result | Tool | Domain | Passage and locator | Signalling answer (reviewers) | Judgment (reviewers) |
|---|---|---|---|---|---|

### RWD fitness or digital endpoint validation (if in scope)
| Study | Framework named | Question | Passage and locator or [GAP] | Answer (appraisers) |
|---|---|---|---|---|

### Retractions and registrations
### AI-use table
| Step | AI or automation used | Human responsible | How checked |
|---|---|---|---|

### Calls made
### Record
AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. This line appears in every answer, refusals included.
