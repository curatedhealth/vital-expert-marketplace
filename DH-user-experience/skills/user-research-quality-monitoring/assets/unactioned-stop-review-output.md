# Output format: unactioned stop review

Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Use only these sections, in this order. One line per item; no context paragraphs and no explanatory bullets. Tables at most five rows; quotes at most ten words; each row id once. The format fits under 450 words when followed.

1. **Verdict by rule:** one line per rule: Rule (your words) · Met or missed · The number behind it.
2. **Open stops and responses** (critical first): Stop · Participants by group · Age · One quote · Response (proposed unless yours) · Owner you named · Forum and date you set.
3. **Hypotheses:** at most two, one line each, with what would confirm it.
4. **Decision needed:** one line. If a ranking was asked for and no scores were given, name the scores it needs.
5. **For the owner:** one line.
6. **Record:** "Review draft, AI-assisted. Clearer: [name you give, or not named]. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft."
7. One line offering the full version.

## Full mode

### Summary

### Your rules
| Rule type | Rule in your words | Checked against |
|---|---|---|

### Results
| Rule | Number or evidence | Met / missed / not measurable | Source (A1 or A2) |
|---|---|---|---|

### Open stops
| Stop | Participants by group | Their words | Age | Critical (your flag) | Sample note (A1) |
|---|---|---|---|---|---|

### Hypotheses
| Stop | Hypothesis | What would confirm it |
|---|---|---|

### Response options
| Stop | Response (proposed or yours) | Basis (row) | Your score, if ranked |
|---|---|---|---|

### Ranking (only if you scored)

### Owners, forums and dates
| Stop | Owner you named | Forum that will see it | Date for the action or refusal |
|---|---|---|---|
"Owner not named" or "not set" where missing.

### Stops for the accountable owner

### Gaps

### Record
Review draft. Rules, owners and dates are yours. AI-assisted. Clearer: NAME, or not named. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft.
