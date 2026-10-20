# Output format: endpoint and COA selection (draft for the person and the owner they name for statistics)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** comparables found (count, NCT ids), the endpoint options in one line each, the biggest open item, and who chooses (named, or "owner not named").
2. **Comparables:** table NCT or DOI · Design and masking · Primary outcome (registry wording) · Paper's primary outcome sentence, where it differs (quoted, locator) · Time frame · Source.
3. **Endpoint options:** table Option · COA type or digital measure · Four elements (variable, metric, aggregation, time point) · Used by · Open items · Rows.
4. **Digital measure:** one line per DHT endpoint: verification, validation in the study population, usability (shown, stated not shown, or [GAP], with rows); replicated existing measure or novel endpoint (CV57, CV56); if V3 terms are used, V3 is [PAPER] DOI 10.1038/s41746-020-0260-4, not FDA policy.
5. **Decisions for the person:** the choices still open, none made by the model; any proposal labeled "proposed".
6. **Calls made:** list.
7. **Record:** "Endpoint options draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Study question (PICO)
### Comparable trials
| NCT | Paper (DOI) | Design | Masking | Enrollment | Primary outcome (verbatim) | Time frame | Secondary outcomes | Registry vs paper |
|---|---|---|---|---|---|---|---|---|
### Endpoint options
| Option | Meaningful aspect of health and concept of interest | COA type | Variable | Metric | Aggregation | Time point | Used by | Meaningful change anchor | Measurement properties | Rows |
|---|---|---|---|---|---|---|---|---|---|---|
### Digital measure fitness
| Question | Status (shown, stated, [GAP]) | Source held | Rows |
|---|---|---|---|
### Decisions for the person and the owners they name
### Gaps
### Calls made
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
