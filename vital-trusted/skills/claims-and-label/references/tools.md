# Tools and companion slot

## Companion slot

No companion exists for this skill at launch. The method runs fully on the label or
intended-purpose statement the person supplies. This skill never calls VERIFY directly
and never describes a label or review check that did not run (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Label and intended use | Fetch the current approved label for the named market and version, and compare each product statement with its indication, population and dose wording | No companion yet. Candidate: label source (`trusted-capability-map`, `references/tools.md`) | Method runs on the supplied label; whether that label is current and approved in the market is `[GAP: not checkable here — …]`; check line says "not tool-checked" |
| Promotional boundary | Prepare the piece for the company's promotional or medical review: route it, attach the label and references, record reviewer comments | No companion yet. Candidate: MLR preparation | Method runs; the note names the kind of process; "not tool-checked" |
| Comparative claims | Test the comparison against the passage of the head-to-head study it rests on | VERIFY `check_claim`, through `claim-assessment`, when VERIFY is connected | Method runs (five questions); whether the study says what the comparison claims is "not tool-checked" |

Hand-off rule: a comparison that has a supplied direct study goes to `claim-assessment`
for the support check, which owns the VERIFY contract. This skill did not read VERIFY's
argument or return contracts `[CHECK]` that the hand-off matches the final
`claim-assessment` scope.

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `find_claim_cues`

List wording that usually marks a label, promotion or comparison issue.

Data: `check-rules.json` → `checks.find_claim_cues.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.


