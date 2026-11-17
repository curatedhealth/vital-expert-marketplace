# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Input confidentiality | An AI-policy companion would read the company's AI use policy and approved-tool list and return, for this kind of material and this tool, the covering section, the approved alternative if any, and the policy owner | None yet | Ask the person the policy question; check line says "asked, not checked" |
| Intellectual property | The same companion, extended with the company's license register, could say whether a subscription or license covers this use and this tool | None yet | Ask the person or point to the licensing process; "asked, not checked" |

When a person quotes their policy or approved-tool list in the conversation, use their
words as supplied, with their date, and do not extend them. That is the person's input,
not a companion result.

VERIFY does not fill these slots. It checks sentences against supplied passages; it does
not read policies or licenses.

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `scan_inputs`

Pattern scan of a text before it is used with an AI assistant.

Data: `check-rules.json` → `checks.scan_inputs.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.


