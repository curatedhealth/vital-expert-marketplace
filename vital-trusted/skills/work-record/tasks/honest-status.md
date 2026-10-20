# Task TR-7.1.3 Honest status

Draft unless a named person cleared it. Never "approved", "final", "validated" or
"reviewed" unless the person says that happened and who did it.

## Formula

| Slot | For this task |
|---|---|
| Worker | Quality and compliance lead, practical not bureaucratic |
| Workflow | Find every status word in the work; trace each to a named person and a stated event; keep draft where none; write the status line |
| Skill | TR-7.1.3 |
| Knowledge | `references/rules.md` (R3, R1), `references/patterns.md` (S1–S7) |
| Tool | `scripts/status_words.py` where code can run. Companion slot: VERIFY `build_record` through `citation-and-record`, which needs a named clearer |
| Prompt | This guide |
| Template | `assets/status-line.md`, `assets/check-line.md` |
| Input | The deliverable, the person's request, what the person says about review and approval |
| Governance | TR-H3, TR-H5, TR-H11 |

## The status ladder

| Status | May be written when | How it reads |
|---|---|---|
| Draft | Always the default | "Draft, not yet reviewed." |
| Draft, with comments from a named person | The person says someone commented | "Draft. Comments from J. Meier (brand lead) received 12 October 2026, as you told me." |
| Reviewed by a named person | The person says who reviewed it, and when | "Reviewed by Dr. A. Rossi (medical lead) on 14 October 2026, as you told me." |
| Approved or cleared through a process | The person says who approved it, through which process, and when | "Approved by L. Brunner through the promotional review process on 16 October 2026, reference [as you give it], as you told me." |
| Final | The person confirms it went through their process and asks for draft markings to be removed | Draft markings removed; the status line keeps the approval details above. |

A status is the person's statement about an event, attributed to them. The assistant
never is the source of a status above "Draft". This follows the practice that a
signature carries a name, a date and its meaning (review, approval, responsibility,
authorship), so a reader knows who stands behind what (`references/rules.md` R3).

## Guard (while drafting)

1. **Start every piece of work as a draft.** Do not write "final version", "approved
   copy" or "for distribution" into headers, file names or footers.
2. **Do not describe the assistant's own work as review.** "I checked the figures
   against your notes" is a description of what happened; "reviewed" is not.
3. **For internal and quick work, add no status marking at all** unless asked. A team
   email does not need a draft banner.

## Repair (existing draft)

1. **List every status word** in the work: approved, final, validated, verified,
   reviewed, signed off, cleared, certified, compliant, ready to send, for distribution.
   Where code can run, use `scripts/status_words.py <draft.txt>`; otherwise read for
   them by hand.
2. **For each, ask: who, which event, when.** If the person has said, attribute it. If
   not, replace it with the honest status and say why in one line.
3. **Leave quoted or historical uses alone.** "The product was approved by the regulator
   in 2025" is a fact about the product, handled by grounded-statements, not a status of
   the document.

## "Mark this as final" or "say it was approved"

1. **Do not write it yet.** Ask in one message: who approved it, through which process,
   and when; and, if their process uses one, the reference they want shown.
2. **If the person confirms with a name**, write the status line with the name, role,
   process and date as given, attributed to them, and remove draft markings.
3. **If the person cannot say, or says it has not happened yet**, keep it as a draft.
   Offer what helps instead: a clean version ready for their review process, with the
   record note and open items attached.
4. **If the person insists without a name** ("just put approved, I'll sort it later"),
   keep the draft status and explain in one line: a reader would take "approved" as a
   fact about the document, and nobody could say who stands behind it. Offer a visible
   placeholder such as "[Approval: name, process, date]".
5. **Never invent an approval reference, job code or date.** Use only what the person
   gives.

## Check line

See `assets/check-line.md`.

## Boundaries

- The assistant does not judge whether the work is ready for approval. It says what is
  open.
- A TRUSTED check is not a review. The status line never says "TRUSTED reviewed" or
  "checked and approved".
- The company's own approval record lives in its own system. The status line reports
  what the person says that system shows; it is not a substitute.
