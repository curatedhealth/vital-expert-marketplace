# Output format: review and data quality appraisal

## Short mode (default for a direct question; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** for a review, which critical domains have a passage and which do not, and the overall confidence only if the appraisers have rated; for RWD or a digital measure, the framework named and the checks with gaps. Then the one decision next.
2. **Critical domains (AMSTAR 2):** Item · Passage and locator, or "not reported (looked in ...)" · Rating (appraisers).
3. **Overall (if rated):** script lines from `review_check.py amstar2`; critical-item list used; never a score.
4. **RWD or digital measure (if that branch):** Check · Row · Evidence or `[GAP]` · Answer (appraisers).
5. **Calls made:** list.
6. **Record:** "AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft." This line appears in every answer, refusals included; never drop the verify.build_record clause.
7. One line offering the full version.

## Full mode

### Summary
### AMSTAR 2 layout
| Item | Critical (list used) | Where to look (PRISMA item) | Passage and locator | Rating (appraisers) |
|---|---|---|---|---|

### Overall confidence by the AMSTAR 2 rule (ES-107)
Script output; "Partial yes" items left to the appraisers.

### RWD fitness (framework named)
| Dimension | Check | Row | Evidence | Answer (appraisers) |
|---|---|---|---|---|

### Digital signal validity (framework named)
| Step | Check | Row | Evidence | Answer (appraisers) |
|---|---|---|---|---|

### Calls made
### Record
AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. This line appears in every answer, refusals included.
