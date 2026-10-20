# Output format: fidelity repair (draft for the person and the owners they name)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** rules passed, failed and not measurable; the one decision the person needs to make.
2. **Failures:** table Rule (the person's words) · Evidence (quoted words or figure) · What changes (product text, decision rule, or claim map) · Owner (the person's, or owner not named) · Version that must not ship the failed text (the person's decision) · Routed to (pack and skill) · Rows (each [PAPER] row with its own paper's DOI in the same cell).
3. **Change facts that may apply:** one line each, only those triggered (PL95, PL96, PL59, PC-US-23); applicability is for the owner the person names for regulatory status, or owner not named.
4. **Re-check on the next version:** the rules touched.
5. **Record:** "Fidelity repair draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
6. **Calls made:** list. Follows the record line.

## Full mode

### Answer
### Pass rules (the person's words) and owners
### Results per rule
| Rule | Pass, fail or not measurable | Evidence | Source | Rows |
|---|---|---|---|---|
### Failures and repairs
| Failure | What changes | Routed to | Owner | Version that must not ship | Rows |
|---|---|---|---|---|---|

Routed to names the pack and the skill (for example `dh-regulatory-and-quality` document-and-change-control for the release record, `dh-regulatory-and-quality` audit-capa-and-complaints for complaints or CAPA).
### Change facts that may apply
### Re-check plan for the next version
### Gaps
### Decisions for the person and the owners they name
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made
