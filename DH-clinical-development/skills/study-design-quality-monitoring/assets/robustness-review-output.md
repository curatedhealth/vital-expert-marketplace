# Output format: robustness review against the person's rules

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** rules passed, missed and not measurable (the person's rules, counted); the decision the person needs to make.
2. **Misses:** table Rule (person's words) · Fact and source · Owner (named, or "owner not named") · Responding work.
3. **Not measurable:** one line each with what is missing.
4. **Re-check at next amendment:** the rules touching changed items.
5. **Calls made:** list.
6. **Record:** "Robustness review draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Rules as confirmed by the person
| # | Rule (person's words) | Owner | Measured by |
|---|---|---|---|
### Check
| # | Result (pass, miss, not measurable) | Fact | Source | Rows |
|---|---|---|---|---|
### Misses, owners and responding work
### Proposed rules (only if asked; not applied)
### Gaps
### Calls made
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
