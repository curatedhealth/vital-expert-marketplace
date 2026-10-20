# Output format: link-by-link check (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** cohort, version and data cut, each as the person gave it or "not given" (never today's date); "N of M measurable links met against your thresholds" (not a quality score); links not scored and why; the first link in reading order that missed.
2. **Links:** table Link · Measure · n (missing) · Value · Threshold · Met / missed / not scored · Source (file, passage locator, DOI or NCT id with read date).
3. **Reading note:** if a delivery or use link missed, later links cannot separate an ineffective mechanism from failed delivery (CS32, Proctor, DOI 10.1007/s10488-010-0319-7).
4. **Delivery events (named product only):** recall or report summaries in the cohort period the person gave, quoted as the record states, with date; no judgment of their bearing on the product.
5. **Misses for B1:** list.
6. **Record (last line of the answer body):** "Link check draft. AI-assisted. One cohort, one version; a met link is not proof the product works." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. **Calls made (after the record line):** list.

## Full mode

### Answer
### Cohort, version, data cut, context (as the person gave them; "not given" otherwise)
### Plan used (date set; prespecified or not)
### Links in reading order
| Link | Type | Measure | Prespecified | n | Missing | Value | Threshold | Result | Source | Rows |
|---|---|---|---|---|---|---|---|---|---|---|
### Not scored (no measure, measure set after data, no threshold)
### Published passages used (quoted, read in the same direction, N3)
### Delivery events
### Misses handed to B1
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
