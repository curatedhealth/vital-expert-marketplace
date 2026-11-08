# Gap rules applied to citation and record

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/gap-rules.md`.

Same format and classes as every TRUSTED skill:
`[GAP: <class> — <what is missing> — <what would close it>]`

In what the person reads, a gap in a reference list or record is usually better as a
plain sentence after the list ("The second source has no year in what you gave me").
The bracketed form is for the record itself and for `trusted-check`.

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A reference detail (year, pages, identifier, author) the person did not give; the clearer's role or the decision date |
| `not checkable here` | VERIFY is not connected, so citations and the record are not tool-built, and claims are not tool-checked |
| `conflicting` | Two supplied sources disagree; a claim's passage contradicts it; two versions of the same source give different details |
| `needs a decision` | No named clearer; an open item without a decision; a policy question for the AI use policy owner |
| `out of date or unclear date` | A cited source flagged as retracted, corrected or superseded, or with no date |

## Mapping from the earlier vital-verify classes

The vital-verify record and escalation methods used four other class names (found,
field missing, covered but absent, not covered; restated there on 19 October 2026). For
migration they map as follows. [CHECK: mapping to be confirmed by the owner when the
VERIFY plugin is migrated.]

| vital-verify | TRUSTED |
|---|---|
| found | Not a gap: quote what the tool returned |
| field missing | `not supplied` |
| covered but absent | `conflicting` when the passage says otherwise; otherwise `not supplied` |
| not covered | `not checkable here` |

## Wording rules

- Name the exact item: "year of the Okafor and Lind abstract", not "missing metadata".
- Never hint at a value inside a gap ("probably 2024").
- A missing clearer is `needs a decision`, never a placeholder name.
