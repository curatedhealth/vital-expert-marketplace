# Tools and companion slot

## Companion slot

No companion exists for this skill and none is planned (product concept §10.2:
"Tangible: no candidate, stays method only"). Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Audience and literacy | None planned. A hypothetical companion could hold a company's approved lay glossary and patient wording, so plain terms are looked up rather than chosen | None | Method runs in full; plain-language scan where code can run; check line says "not tool-checked" |
| Deliverable fit | None planned. Nothing here needs a tool beyond counting | None | Method runs in full; "not tool-checked" |
| Translation fidelity | None planned. A hypothetical companion could look up approved product information and approved local terms by product, language and date, so flagged terms become lookups | None | Approved wording comes only from the person; terms without it are flagged for a qualified translator; "not tool-checked" |

VERIFY does not fill these slots. It checks sentences against supplied passages; it does
not judge reader fit, format or translation.

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `compare_numbers`

Compare the numbers and units in an original text and its translation.

Data: `check-rules.json` → `checks.compare_numbers.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.



### `plain_language_scan`

Plain-language scan for patient-facing or lay text.

Data: `check-rules.json` → `checks.plain_language_scan.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.


