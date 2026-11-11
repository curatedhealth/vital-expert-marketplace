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
| Tool | `scripts/status_words.py` where code can run. The formal record is `citation-and-record`, which needs a named clearer |
| Prompt | This guide |
| Template | `templates/status-line.md`, `templates/check-line.md` |
| Input | The deliverable, the person's request, what the person says about review and approval |
| Governance | TR-H3, TR-H5, TR-H11 |

## The status ladder

| Status | May be written when | How it reads |
|---|---|---|
| Uncleared draft | Always the default | "Uncleared draft." |
| Uncleared draft, with a note on comments received | The person says someone commented | "Uncleared draft." Note: "Comments from J. Meier received 12 October 2026, as you told me." |
| Reviewed by a named person | The person says who reviewed it | "Uncleared draft, reviewed by Dr. A. Rossi, as you told me." Role, date and what the review covered go in the people's part of the record note |
| Cleared through a process | The person says who cleared it, in what role, and when | "Cleared by L. Brunner, brand lead, 16 October 2026." Then the line "Process: promotional review; reference: <as given>; as you told me." |
| Final | The person confirms it went through their process and asks for draft markings to be removed | Draft markings removed; the status line keeps the "Cleared by" details above. |

The forms, and only these, are defined in `templates/status-line.md`. A placeholder for a clearance still to come is "Uncleared draft (to be cleared by <name>, <role if given>)", or "Uncleared draft (to be cleared by a reviewer not named yet)" when no name is given. A clearance the person reports in the past without role or date is "Uncleared draft (you said <name> cleared it; add role and date to record the clearance)".

A status is the person's statement about an event, attributed to them. The assistant
never is the source of a status above "Uncleared draft". This follows the practice that a
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
   reviewed, signed off, cleared, certified, compliant, ready to send, ready to go, good
   to go, all set, fine to send, for distribution.
   Where code can run, use `scripts/status_words.py <draft.txt>`; otherwise read for
   them by hand.
2. **For each, ask: who, which event, when.** If the person has said, attribute it. If
   not, replace it with the honest status and say why in one line.
3. **Leave quoted or historical uses alone.** "The product was approved by the regulator
   in 2025" is a fact about the product, handled by grounded-statements, not a status of
   the document.

## "Mark this as final" or "say it was approved"

1. **Do not write it yet.** Open with one plain sentence saying why the status stays as
   it is, then ask one combined question: who cleared it, in what role, through which
   review, when, and any reference their process shows. Not a numbered list of fields. A
   request to clear is not a clearance (`../../citation-and-record/governance.md`, the
   clearer). The current status line, "Status: Uncleared draft." (or "Uncleared draft (to
   be cleared by <name>, <role if given>)" when a name was given), goes in the record note or in a note
   after the text, never alone as the first line of the reply.
2. **If the person confirms with a name, role and date**, write "Cleared by <name>,
   <role>, <date>" with the process line, attributed to them, and remove draft markings.
   **A name without a role or date is not enough:** the status is "Uncleared draft (you
   said <name> cleared it; add role and date to record the clearance)". Never
   write "Cleared by <name>" with a part missing or in brackets.
3. **If the person cannot say, or says it has not happened yet**, keep it as a draft.
   Offer what helps instead: a clean version for their review process, with the record
   note and open items alongside it.
4. **If the person insists without a name** ("just put approved, I'll sort it later"),
   keep the draft status and explain in one line: a reader would take "approved" as a
   fact about the document, and nobody could say who stands behind it. Offer the visible
   placeholder "Uncleared draft (to be cleared by <name>, <role if given>)", or "Uncleared
   draft (to be cleared by a reviewer not named yet)" when no name is given.
5. **Never invent an approval reference, job code or date.** Use only what the person
   gives.

## A status footer or stamp ("Reviewed and validated by TRUSTED", "AI-verified")

1. **Decline the wording in one plain sentence.** TRUSTED and the assistant flag issues;
   they do not review, validate or clear work, and no one has cleared this piece. Do not
   lecture.
2. **Hand back the work as written,** without the footer, and describe it plainly ("Here
   is the email as written, without the footer"). Never call it "ready", "ready to go",
   "good to go", "ready to send", "all set" or "fine to send": it is an uncleared draft.
3. **Offer the plain alternative:** "Drafted with an AI assistant. Uncleared draft." Or,
   once the person states a clearance, "Cleared by <name>, <role>, <date>".
4. **Say in one line that whether to mention AI help at all follows their AI use
   policy** (`responsible-use` decides; this skill records).
5. **Name the next review** from the table in
   `../../citation-and-record/references/escalation-packet.md`. If the piece covers an
   attachment you have not seen, say the footer would vouch for something not seen here.

## Where the status line sits

The status line goes to the person, outside the deliverable, unless they ask for it on
the work. It sits in the record note, or in a note after the text. It never stands alone
at the top of an email body or a reply. For an email or a message, put it after the
text, as a line to them, not inside the email.

Never say a document, attachment, approval or data on file exists or is attached unless
the person supplied it or said so. "As discussed, attached is the summary" in the
person's own email stays as they wrote it; the note says the attachment was not seen
here.

## Check line

See `templates/check-line.md`.

## Boundaries

- The assistant does not judge whether the work is ready for approval. It says what is
  open.
- A TRUSTED check is not a review. The status line never says "TRUSTED reviewed" or
  "checked and cleared".
- The company's own approval record lives in its own system. The status line reports
  what the person says that system shows; it is not a substitute.
