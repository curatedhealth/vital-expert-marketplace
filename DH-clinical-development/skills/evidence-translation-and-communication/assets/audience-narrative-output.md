# Output format: audience evidence narrative (draft for the owner)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** one sentence per audience: what the evidence supports for them, with certainty and rater.
2. **Narrative draft:** per audience: the text; the required statements (limitations, not-cleared statement, material differences, study citation details).
3. **Binding rules:** per audience and market, the rows ([INDUSTRY] and [WF] labeled).
4. **Not drafted:** wording the person wanted that crosses a rule or a passage, with the row and a safer draft for the owner.
5. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Evidence used (from A1)
| Outcome | Statement | Certainty (rater) | Passage |
|---|---|---|---|

### Narratives
| Audience | Market | Narrative (draft) | Required statements | Binding rows |
|---|---|---|---|---|

### Wording not drafted and safer alternatives
| Wanted wording | What it crosses (row or A1 gap) | Safer draft for the owner |
|---|---|---|

### Decisions for the owner
Numbered: each narrative, each required statement, each [INDUSTRY] or [WF] row relied on, each gap.

### Calls and record
Calls made. "Draft for the owner. The skill does not clear narratives." AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
