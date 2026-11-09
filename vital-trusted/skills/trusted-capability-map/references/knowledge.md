# Knowledge: trusted-capability-map

This file is the single home for this skill's routing knowledge, gap wording and
failure modes. Where the same rule appeared in more than one earlier file, one copy
is kept.

## Contents

- Part 1: What this skill owns, routes and honesty rules
- Part 2: Gap rules (shared by every TRUSTED skill)
- Part 3: Failure modes

## Part 1: What this skill owns

### What this skill owns

Routing and explanation of the TRUSTED kit: which Core/Build/Prove skills apply, which
letters are on, and where shared cards live. It does **not** run letter repairs or Prove
checks itself.

### Default routes (everyday)

| Ask shape | First stop | Then |
|---|---|---|
| Missing market/use/reader | `trusted-intake` | `trusted-check` at the right depth |
| Colleague light note | `trusted-check` (light) | Build letters only if something would mislead |
| External / promotional / payer | `trusted-intake` → `trusted-check` (full) | Prove skills by hand when True needs passage checks |
| Any input with a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem | `patient-safety` first: its flag before any question (TR-H14) | `trusted-intake`, then the skill the work needs; safety reporting procedure (named, not replaced) |
| Doctor dosing question, no safety mention | `trusted-intake` → `patient-safety` → `claims-and-label` | Company MI process (named, not replaced) |
| "Just mark supported/approved" | Refuse unchecked labels | Offer check now or label not checked |

### Shared cards

The plugin root `templates/` folder holds claim-card, source-card, confidence-card,
evidence-table, gap-list, prove-brief and check-line-stamp. Where a skill has its own
template for the same output, the skill's template wins; the shared cards are reference
only. See `../../../templates/README.md`.

### Honesty rules

- Prefer supplied material over model memory.
- Mark missing inputs as gaps (the `[GAP: …]` marker only inside a drafted deliverable, plain words elsewhere); untraced norms `[CHECK]`.
- No invented skill results; no send-ready verdicts from the map alone.

## Part 2: Gap rules

Every TRUSTED skill words gaps the same way, so a reviewer can scan them across a
document.

### Where the marker belongs

The `[GAP: …]` marker goes only inside a drafted deliverable, where the missing content
would sit, so the person can find and fill it. Everywhere else (notes, open-item lists,
change notes, explanations) say the same thing in plain words: "Still missing: the 95%
confidence interval for the primary endpoint, from the results table." Testing on 20
October 2026 showed raw markers in notes lists read as internal plumbing (TR-H13).

### Format

`[GAP: <class>; <what is missing>; <what would close it>]`

Keep it to one line. Put it where the missing content would have gone.

### Classes

| Class | Use it when | Example |
|---|---|---|
| `not supplied` | The material the person gave does not contain it | `[GAP: not supplied; 95% CI for the primary endpoint; supply the results table]` |
| `not checkable here` | Only something not supplied could establish it | `[GAP: not checkable here; whether the claim matches the cited passage; supply the passage so it can be compared by hand]` |
| `conflicting` | Two supplied sources disagree and nothing says which governs | `[GAP: conflicting; abstract says 412 patients, full text says 408; confirm which is final]` |
| `needs a decision` | A person with authority has to decide (policy, scope, sign-off) | `[GAP: needs a decision; whether this tool is approved for unpublished data; ask your AI policy owner]` |
| `out of date or unclear date` | A "current" or "latest" statement has no date, or the source may be superseded | `[GAP: out of date or unclear date; "latest guidance" has no title or date; name the document]` |

### Wording rules

- Name what is missing, not that "information is unavailable".
- Never use a gap to hint at an answer ("probably around 400").
- Never turn an absence into a claim. "The paper does not report harms" is a finding only
  if the full paper was supplied and read. Otherwise it is `[GAP: not supplied; the full paper's harms results; supply the full paper]`.
- A gap is not a failure of the person. Do not apologize for it or blame anyone.

### The [CHECK] marker

`[CHECK]` is for the skill's own content, not the person's draft: a rule or reference the
skill could not trace to a dated primary document. A `[CHECK]` rule is described, never
enforced as fact.

## Part 3: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-CM-01 | Skip intake routing | Was a doctor question routed straight to draft-and-send? | Routing | TRUSTED capability-map | VERIFIED practice |
| FM-CM-02 | Invented skill results | Did the map declare Safe/Rule-compliant fine without those skills? | Honesty | TR-H4 | VERIFIED practice |
| FM-CM-03 | Replaced company SOP | Did routing guess a company's SOP name, or present itself as replacing the process? | Process | TR-H11 | VERIFIED practice |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
