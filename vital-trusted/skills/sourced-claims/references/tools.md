# Tools and companion slot

## Companion slot

No companion is connected to this skill at launch. It hands finished work to the Prove
skills, which own the VERIFY tool calls and their interpretation. This skill never calls
VERIFY directly.

| Task | What a companion would do | Tool (through which skill) | Without it |
|---|---|---|---|
| Every claim sourced | Test each sourced claim against the quoted passage it rests on | VERIFY `check_claim`, `verify_text`, through `claim-assessment` | Method runs; check line says "not tool-checked" |
| Right type of source | Qualify a specific source (type, peer review, funding, fit for the question) and check whether it is current or superseded | VERIFY `qualify_source`, `check_currency`, `ingest_document`, through `source-assessment` | Method names the type and whether it fits; specific grading marked `[GAP: not checkable here — …]`; "not graded with a tool" |
| Specific citations | Build a formatted citation from a supplied or fetched source | VERIFY `build_citation`, through `citation-and-record` | Method lists fields from the supplied source; "citation not built or checked with a tool" |

Tool names are as the VERIFY connector lists them. This skill did not read their
argument or return contracts; those are recorded in the Prove skills. `[CHECK]` that the
three hand-offs above match the final Prove skill scopes.

A future companion that could fill a slot here: a company reference library (approved
references and data on file with their identifiers), which would let the specific
citations task match claims to approved references instead of asking. Candidate, not a
commitment. `[CHECK: not in the concept's candidate list; for the owner to decide]`

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `find_source_cues`

List wording that usually marks a claim needing a source, or a citation needing work.

Data: `check-rules.json` → `checks.find_source_cues.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.


