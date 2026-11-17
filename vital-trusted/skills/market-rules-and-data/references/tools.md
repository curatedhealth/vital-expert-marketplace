# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Jurisdiction | An MLR preparation companion would hold the company's market templates and the approved label per market, and return which market's wording, approval and channels apply | None yet | Ask the market; work from the label the person supplies; check line says "not tool-checked" |
| Required statements | The same companion would return the company's element list for this material and market, and draw the job code, date and current PI link from the approval system | None yet | Placeholders for the person to fill; `[GAP: not checkable here — current approved version — your approval system]` |
| Privacy in the output | A privacy companion could apply the company's minimum-count rule and its consent records | None yet | Ask the privacy function; never set a threshold |

VERIFY does not fill these slots. It checks sentences against supplied passages; it does
not hold market rules, templates, codes or consent records.

When the person supplies a template, element list or minimum count from their company,
use it as given, with its date, and do not extend it. That is the person's input, not a
companion result.

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `scan_output`

Cue scan of a draft for market statements and personal details in the output.

Data: `check-rules.json` → `checks.scan_output.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.


