# Output format: evidence requirement map

Two modes, same order. Short mode is the default for a direct question.

## Short mode (250 to 450 words)

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

Hard cap: count the words before sending. Over 450, cut in this order: comparables to one line, the consultation line, rows already marked "[GAP]" merged into one row ("Not in the record: ..."), the closing offer. Never cut the answer, row ids, the claim status or the record line.

1. **Answer:** per body, one line: what the evidence shows, what is open, as read on the rule date.
2. **Requirements against evidence:** one table: Body · Rule (row id) · Status (shown, not shown, `[GAP]`, not applicable) · Shown by (study, section).
3. **Claims:** one line per claim: claim · status as read (checked or not checked) · passage locator.
4. **Open items:** at most three lines, each with what would close it.
5. **Record:** "Rules read 19 October 2026 from primary sources; library calls of DATE. Uncleared draft. Effect type, comparator and claims are decisions for the accountable owner (as named, or owner not named)."

End with one offer: the full map, or the next task (submission readiness).

## Full mode

### Answer
Two or three sentences per body.

### Product facts used
Device class, intended purpose, ICD-10-GM codes or indication, each with its source or `[GAP]`.

### Rules per body
| Body and route | Rule | Row | Read on |
|---|---|---|---|

### The person's studies
| Study (DOI, PMID) | Design (decided by) | CEBM level from design only | Retraction | Registry id | Country | Comparator | Source |
|---|---|---|---|---|---|---|---|

### Requirements against evidence
| Body | Rule (row) | Status | Shown by | What would close it |
|---|---|---|---|---|

### Claims checked
| Claim | Body and requirement | Study, locator | Passage (verbatim) | Verify status | Read as |
|---|---|---|---|---|---|

### What it means
Facts only: which requirements are open, which route the current evidence fits on the rules alone. Advisory; the route is the person's decision.

### Sources and record
Row ids with URLs from `references/hta-submissions-sources.md`; library calls with date; "Record: cleared by NAME" or "uncleared draft". AI-assisted draft.
