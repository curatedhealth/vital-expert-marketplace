# Output format: value proposition and messages (draft for the owner)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the record line, the guidance-status line for US payor material (PC-US-47), or the base EU device rule for any EU or German message (MDR Article 7, PC-EU-01, PC-EU-02). Refusals follow the same 450-word cap.

1. **Answer:** the value proposition in one sentence per audience asked about.
2. **Message draft:** per audience: the message; the outcomes used (case-study results included), each with its source or `[GAP]`; the required disclosures.
3. **Binding rules:** per audience, the rows (labels for [INDUSTRY] and [WF]).
4. **Not drafted:** wording the person wanted that crosses a rule, with the row and a safer draft for the owner.
5. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Value proposition
| Audience | What they get | Outcome used | Source and passage checked | Status |
|---|---|---|---|---|

### Message map
| Audience | Market | Message (draft) | Required disclosures | Binding rows |
|---|---|---|---|---|

### Wording not drafted and safer alternatives
| Wanted wording | Rule it crosses | Row | Safer draft for the owner |
|---|---|---|---|

### Evidence checks
| Outcome | Source (tier) | Passage locator | Verify status | Read in the same direction? |
|---|---|---|---|---|

### Decisions for the owner
Numbered list: each message, disclosure, [INDUSTRY] code applied, [WF] row relied on, gap.

### Sources and record
Calls made. "Draft for the owner. The skill does not clear messages." AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
