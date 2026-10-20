# Output format: value narrative and use (draft for the owner)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** the narrative in one or two sentences per audience.
2. **Rests on:** the claims used, each with source and certainty (person's rating or `[GAP]`).
3. **Not said:** held claims and outcomes that did not move, one line each.
4. **Uses and rules:** per use the person named: the rows that bind it and the stop.
5. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Narrative per audience
| Audience | Narrative (draft) | Claims used | Certainty (rating, who) |
|---|---|---|---|

### Not said, and why
| Claim or outcome | Reason held | Row or passage |
|---|---|---|

### Uses
| Use (person's words) | Market | Rows that bind it | Required statements | Stop, owner |
|---|---|---|---|---|

### Wording not drafted and safer alternatives
| Wanted wording | Rule it crosses | Row | Safer draft for the owner |
|---|---|---|---|

### Decisions for the owner
Numbered list.

### Sources and record
Calls made. "Draft for the owner. The skill does not clear narratives. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
