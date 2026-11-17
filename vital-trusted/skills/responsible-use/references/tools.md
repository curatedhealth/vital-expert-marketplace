# Tools and companion slot

## Companion slot

No companion exists for this skill yet. Do not imitate one (TR-H4).

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Human oversight | An AI-policy or MLR-preparation companion would read the company's review procedures and say which process this work goes through and who the reviewer role is | None yet | Ask who will read it before use; name the kind of process in plain words; check line says "asked, not checked" |
| AI use disclosure | An AI-policy companion would read the company's AI use policy and return whether and how it expects disclosure for this kind of work and audience, with the section | None yet | Ask what the policy says; offer wording for the person to approve; "asked, not checked" |
| Authorship integrity | A publications companion would read the company's publication policy and the target journal's instructions and list the authorship and acknowledgment steps | None yet | Ask for the venue and point to the publications process; "asked, not checked" |
| Equity and inclusion | A language companion would check wording against the community guides the company has adopted | None yet | `scripts/scan_language.py` where code can run, plus reading by hand; "not tool-checked" |

When the person quotes their policy, the venue's instructions or a community guide in
the conversation, use their words as supplied, with their date, and do not extend them.
That is the person's input, not a companion result.

VERIFY does not fill these slots. It checks sentences against supplied passages; it
does not read policies, venue rules or language guides. When a disclosure statement or
evidence-gap sentence states a fact from a source ("the trial included 9% of people over
75"), that sentence can go to `claim-assessment` like any other claim.

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `scan_language`

List phrases in a text that may stigmatize, blame or define people by a condition.

Data: `check-rules.json` → `checks.scan_language.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.


