# Output format: evidence claim map (draft for the person and the owner they name)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** number of claims; how many sourced, narrower than claimed, [GAP] and refused; the claim the product will not make (proposed); who decides (named, or "owner not named").
2. **Claim map:** table Claim (verbatim) · Status · Passage (quoted, locator) · Source (DOI, NCT or DEN) · Population and dose in the source · Certainty (as rated by the person or a review, or [GAP]) · Rows (each [PAPER] row with its DOI in the same cell; ES-199 to ES-201 and BCTTv1 rows marked "abstract only"; cite a TM row only when the quoted passage is that row's quote, otherwise the Source column alone).
3. **Narrower and refused:** one line each quoting the words that differ (population, verb, outcome, caveat).
4. **Rules that apply:** one line each, only those triggered (CFL factors PC-US-23, PC-US-24, nonbinding; DiGAV § 9(2) TM148; MDCG 2020-1 PL70 to PL72; IMDRF N41 PL63 to PL65).
5. **Not checked:** any claim whose source Verify could not admit (for example FDA decision summaries, register C1), any Verify "supported" read and found to differ (N3).
6. **Record:** "Evidence claim map draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
7. **Calls made:** list. Follows the record line.

## Full mode

### Answer
### Product, intended use and population (as the person stated them)
### Claim map
| # | Claim (verbatim) | Kind (effect, population, dose, caveat, mechanism) | Status | Passage (quoted) | Locator | Source | Population in source | Dose in source | Outcome in source | Certainty (rated by) | Verify status, read in the same direction (yes or no) | Rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
### Claims the product will not make (proposed)
### Consistency rules that apply
### Library labels (design and level, not certainty)
### Gaps
### Decisions for the person and the owners they name
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made
