# Output format: fidelity sample (draft for the person and the owners they name)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** version and read date; sample coverage (n of N shipped); claims with differences by type; claims with no source; rules with differences; dose summary; what was not sampled.
2. **Claims:** table Claim id · Product text (quoted) · Source passage (quoted, locator) · Words that differ · Type under the person's rule (or "for the person to mark") · Verify status and overlap, read by hand · Rows (each [PAPER] row with its own paper's DOI in the same cell).
3. **Decision rules:** one line each: specified behavior, observed behavior, evidence, difference.
4. **Dose:** regimen and session definition; percent of expected sessions (mean, median, range); coverage; threshold (the person's).
5. **Not shown by this sample:** one line.
6. **Record:** "Fidelity sample draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
7. **Calls made and script runs:** list. Follows the record line.

## Full mode

### Answer
### Version, read date and coverage
### Claims compared
| Claim id | Product text | Source passage | Locator | Source | In source, not in product | In product, not in source | Numbers | Person's mark | Verify (status, overlap) | Rows |
|---|---|---|---|---|---|---|---|---|---|---|
### Claims with no source
### Decision rules compared
| Rule | Specified (decision point, variable, option, missing data) | Observed | Evidence | Difference | Rows |
|---|---|---|---|---|---|
### Safety events read (named products only, from their records)
### Delivered dose
| User or group | Sessions delivered of expected | Weeks with use | Mean minutes | Coverage | Rows |
|---|---|---|---|---|---|
### What the sample does not show
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made and script output
