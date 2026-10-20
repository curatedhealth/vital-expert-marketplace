# Output format: estimand and SAP decisions (decision draft for the owner the person names for statistics)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the primary estimand as far as it can be written, and the number of decisions open for the owner the person names for statistics (named, or "owner not named").
2. **Estimand:** five lines: treatment and comparator, population, variable (four elements), intercurrent events with strategy (or "open: options CV35 to CV39"), population-level summary. Rows CV33, CV34.
3. **Decisions open:** table Decision · Options · Facts and rows · Decides.
4. **Cautions that apply:** one line each with rows (for example non-inferiority with DHT measures, CV58, CV72).
5. **Calls made:** list.
6. **Record:** "Decision draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Estimand
| Attribute | Content | Source (person, A1, owner named for statistics) | Rows |
|---|---|---|---|
### Intercurrent events and strategies
| Event (person's words) | Treatment policy | Hypothetical | Composite | While on treatment | Principal stratum | Chosen by |
|---|---|---|---|---|---|---|
### SAP decisions
| Decision | Options | Facts and rows | Status (open, decided by NAME) |
|---|---|---|---|
### Assumptions and their sources
| Assumption | Value | Source (passage, Verify result) or "named owner's" |
|---|---|---|
### Bias planning view (not a risk-of-bias judgment)
### Decision log
### Gaps
### Calls made
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
