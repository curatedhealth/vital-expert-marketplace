# Output format: mechanism check plan (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** links with a measure and threshold (count), with a measure and no threshold, not measurable ([GAP], not scored); the plan date and whether data had been read; the one decision the person needs to make; who sets thresholds (named, or "owner not named").
2. **Plan:** table Link (reading order) · Measure (person's words) · Denominator · Time point and aggregation · Threshold (person's, or open) · Proxy named in advance · Rows (each [PAPER] row with its own DOI; abstract-only and [WF] rows labeled).
3. **Reading rule:** one line: delivery and use are read before change and outcome; use is not the outcome (CS32, Proctor, DOI 10.1007/s10488-010-0319-7).
4. **Record (last line of the answer body):** "Mechanism check plan draft. AI-assisted. Set on [the plan date the person gave, or "not given"], [before / after] the data were read." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
5. **Calls made (after the record line):** list (often none).

## Full mode

### Answer
### Cohort, version and data the plan covers
### Plan
| Link | Type (delivered, used, changed, outcome, population) | Measure | Instrument or log field | Denominator | Time point | Aggregation | Threshold | Proxy (named now) | Prespecified | Rows |
|---|---|---|---|---|---|---|---|---|---|---|
### Fidelity framework used (Moore, Carroll, Bellg abstract only, or the person's)
### Not measurable yet ([GAP], not scored)
### Proposed measures or thresholds (labeled "proposed", not applied until confirmed)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
