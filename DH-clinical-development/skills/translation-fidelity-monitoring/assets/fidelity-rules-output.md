# Output format: fidelity rules (draft for the person and the owners they name)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** the framework used (named with its DOI; frameworks disagree, research file conflicts item 3; when citing the disagreement, cite TM94 with DOI 10.1136/bmj.h1258 (Moore); Bellg TM99 is abstract only), the number of core and adaptable components, the fail conditions, the delivery measures, and the decisions waiting for the person.
2. **Core and adaptable (proposed):** table Component · Core or adaptable · Permitted variation · Prohibited variation · Rows (TM11 and TM19, DOI 10.1136/bmj.n2061; TM117, DOI 10.1136/bmj.i6795; CS4, DOI 10.1186/1748-5908-4-50; TM105, DOI 10.1186/1748-5908-2-40).
3. **Fail conditions (proposed):** table Type (wider population, stronger verb, missing caveat, other outcome, other dose, no source, rule misfire, missing-data behavior) · How it is detected · Rows (each [PAPER] row with its own paper's DOI in the same cell).
4. **Delivery measures:** table Measure · Data source · Regimen measured against · Threshold (the person's, blank until set) · Rows (TM102, DOI 10.1186/1748-5908-2-40).
5. **Record:** "Fidelity rules draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
6. **Calls made:** list (usually none). Follows the record line.

## Full mode

### Answer
### Source of truth (claim map, specification, label) and version
### Framework chosen and why (the person's choice)
### Core components and permitted variation
| Component | Core or adaptable | Function it serves | Permitted variation | Prohibited variation | Owner | Rows |
|---|---|---|---|---|---|---|
### Claim fail conditions
| Type | Definition in the person's words | Example from the sources | Rows |
|---|---|---|---|
### Decision rule fail conditions
| Rule | What is checked | Evidence needed | Rows |
|---|---|---|---|
### Delivery measures
| Measure | Definition (including what one session is) | Data source | Threshold (the person's) | Rows |
|---|---|---|---|---|
### Gaps
### Decisions for the person and the owners they name
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
