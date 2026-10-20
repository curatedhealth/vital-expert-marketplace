# Output format: evidence and audience map

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** which claims can be carried, for which audience, and the main gap, in two or three sentences.
2. **Claim register:** Claim · Source · Passage (locator) · Verify status · Same direction? · Certainty (who rated) · May enter?
3. **Audience fit:** one line per audience: framework, what it expects (row ids), which claims meet it, the gap.
4. **Gaps:** at most four lines, by class (`references/gap-rules.md`).
5. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
Two or three sentences.

### Studies resolved
| Study | Identifiers | Design (checked against the paper) | Registration | Retraction check (source) |
|---|---|---|---|---|

### Claim register
| # | Claim | Source | Passage and locator | Verify status and overlap | Read in the same direction? | Population, comparator, outcome, time point match | Certainty (rating, who) | May enter / held, why |
|---|---|---|---|---|---|---|---|---|

### Audience map
| Audience (person's words) | Framework | What it expects | Rows | Claims that meet it | Gap |
|---|---|---|---|---|---|

### Decisions for the person
Certainty ratings, claims to carry, audiences, ESF tier or AMCP dossier type to confirm.

### Sources and record
Calls made, with dates. AMCP rows labeled "AMCP 6.0 draft". "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
