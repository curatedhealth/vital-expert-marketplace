# Gap rules

Every TRUSTED skill words gaps the same way, so a reviewer can scan them across a
document.

## Where the marker belongs

The `[GAP: …]` marker goes only inside a drafted deliverable, where the missing content
would sit, so the person can find and fill it. Everywhere else (notes, open-item lists,
change notes, explanations) say the same thing in plain words: "Still missing: the 95%
confidence interval for the primary endpoint, from the results table." Testing on 20
October 2026 showed raw markers in notes lists read as internal plumbing (TR-H13).

## Format

`[GAP: <class> — <what is missing> — <what would close it>]`

Keep it to one line. Put it where the missing content would have gone.

## Classes

| Class | Use it when | Example |
|---|---|---|
| `not supplied` | The material the person gave does not contain it | `[GAP: not supplied — 95% CI for the primary endpoint — supply the results table]` |
| `not checkable here` | Only a companion tool could establish it, and none is connected | `[GAP: not checkable here — whether the claim matches the cited passage — connect VERIFY or check manually]` |
| `conflicting` | Two supplied sources disagree and nothing says which governs | `[GAP: conflicting — abstract says 412 patients, full text says 408 — confirm which is final]` |
| `needs a decision` | A person with authority has to decide (policy, scope, sign-off) | `[GAP: needs a decision — whether this tool is approved for unpublished data — ask your AI policy owner]` |
| `out of date or unclear date` | A "current" or "latest" statement has no date, or the source may be superseded | `[GAP: out of date or unclear date — "latest guidance" has no title or date — name the document]` |

## Wording rules

- Name what is missing, not that "information is unavailable".
- Never use a gap to hint at an answer ("probably around 400").
- Never turn an absence into a claim. "The paper does not report harms" is a finding only
  if the full paper was supplied and read. Otherwise it is `[GAP: not supplied]`.
- A gap is not a failure of the person. Do not apologize for it or blame anyone.

## The [CHECK] marker

`[CHECK]` is for the skill's own content, not the person's draft: a rule or reference the
skill could not trace to a dated primary document. A `[CHECK]` rule is described, never
enforced as fact.
