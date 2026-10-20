# Gap rules applied to claim assessment

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/gap-rules.md`.

Same format and classes as every TRUSTED skill:
`[GAP: <class> — <what is missing> — <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A claim with no passage in the supplied material; a removed sentence the person may want back |
| `not checkable here` | Whether a sentence matches its passage, when VERIFY is not connected; a source not yet admitted |
| `conflicting` | Two supplied passages disagree on the claim, or the passage says something different from the draft |
| `needs a decision` | Which of two passages governs; whether to keep a recommendation that no passage can settle |
| `out of date or unclear date` | The passage supports the claim but is undated, or says "current" without a date |

How VERIFY results map to gaps:

| VERIFY status | Gap, if the sentence is removed or held |
|---|---|
| `supported` | None |
| `partial` | `not supplied` for the dropped part, if the person needs it |
| `unsupported` | `not supplied` |
| `contradicted` | `conflicting` |
| `unverifiable` | `not supplied` (no passage) or `not checkable here` (source not admitted) |
| `out_of_scope` | `needs a decision`, only when the person must decide whether to keep it |

Wording rules:

- Name the exact item: "approval date in Switzerland", not "regulatory details".
- Never hint at a value inside a gap.
- "The passage does not state X" is a finding only for the passage that was quoted. It
  says nothing about the full source unless the full source was supplied and read.
- A gap replaces a removed sentence only when the person needs to see that something is
  missing. Otherwise the sentence simply comes out, and the result lists it.
