# Output format: insight actionability indicators

Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Use only these sections, in this order. One line per item; no context paragraphs and no explanatory bullets. Tables at most five rows; quotes at most ten words; each row id once. The format fits under 450 words when followed.

1. **Answer** (at most 60 words): decided vs open with denominators and the as-of date; the oldest open insights; changes not traced to research.
2. **Status:** one line: Action · Refusal · Open (each "n of N").
3. **Open insights:** Insight · Age (days) · Owner · Participants hit · Critical (your flag). Oldest first.
4. **Trace:** one line each for traced, not traced to this research, broken links, and actions not yet shipped.
5. **Against your rules:** one line per rule (met or missed), or "no rule set: numbers only".
6. **Record:** "Indicator draft, AI-assisted. Clearer: [name you give, or not named]. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft."
7. One line offering the full version.

## Full mode

### Answer

### Source
Files, as-of date, column mapping if a tracker export was used.

### Decision status
| Status | Count | Of |
|---|---|---|

### Open insights
| Insight | Stop | Raised | Age (days) | Owner | Participants hit | Critical (your flag) |
|---|---|---|---|---|---|---|

### Time to decision
n, median, longest (days).

### Quality of the log
Refusals without a reason; insights without an owner; broken links.

### Trace to shipped changes
| Change | Release | Shipped | Insight cited | Status (traced / not traced to this research / link broken) |
|---|---|---|---|---|

### SUS across rounds (if given)
| Round | n | Mean | Difference from previous |
|---|---|---|---|
Context only (UX-M-08, UX-M-09, [PAPER], DOI 10.2196/37290); no significance claim.

### Against your rules
| Rule (your words) | Number | Met / missed / not measurable |
|---|---|---|

### Gaps

### Record
Indicator draft. No verdict without your rule. AI-assisted. Clearer: NAME, or not named. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft.
