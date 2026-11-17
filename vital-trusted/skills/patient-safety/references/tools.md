# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4). VERIFY does not fill
these slots: it checks sentences against supplied passages; it does not hold approved
labels or route safety reports.

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Clinical safety statements | A label-source companion would return the current approved label for a named product, market and formulation, with its revision date, section by section | None yet | Ask the person for the label; quote only what they supply; mark currency `[GAP: not checkable here — whether this is the current approved label — confirm with your regulatory function]` |
| Patient safety language | The same label-source companion, for the approved patient leaflet | None yet | Ask for the leaflet; method runs; "not tool-checked" |
| Side-effect flag | A safety-routing companion would open an intake in the company's safety system with the quoted text and source, and return a receipt reference. It would never assess the case | None yet | Write the flag for the person to pass on; never say it was sent |

When the person quotes their safety procedure, a contact route or a label in the
conversation, use their words as supplied, with their date, and do not extend them. That
is the person's input, not a companion result.

VERIFY may still check, through `claim-assessment`, that a quoted label sentence matches
the supplied label passage. That is a support check on wording, not a safety check.

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `label_match`

Compare safety sentences in a draft with the supplied label text.

Data: `check-rules.json` → `checks.label_match.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.



### `scan_safety_mentions`

Find words that may signal a possible safety report, or patient-wording problems.

Data: `check-rules.json` → `checks.scan_safety_mentions.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.


