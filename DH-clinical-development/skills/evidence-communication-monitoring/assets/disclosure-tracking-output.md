# Output format: disclosure tracking

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** as of DATE: clocks past due, due, met, not computed; the one that matters most, with its rule.
2. **Clock table:** Trial · Clock · Rule · Basis date (source field) · Due · Status.
3. **Not computed:** trials or regimes with the missing answer or date.
4. **Record:** "AI-assisted draft." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Regimes confirmed by the person
| Trial | Registry and id | ICMJE journal | US applicable clinical trial | EU CTR | WHO signatory | Confirmed by |
|---|---|---|---|---|---|---|

### Clocks
| Trial | Clock | Rule | Basis (date, source field) | Arithmetic | Due | Status as of DATE |
|---|---|---|---|---|---|---|

### Publication
| Trial | Paper (DOI) or [GAP] | Date | Registry posting (not prior publication, CV137) |
|---|---|---|---|

### Not computed and why
### Calls and record
Calls made; script run with its input file. "One calendar year added per 1-year rule; counting convention not sourced." AI-assisted draft. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
