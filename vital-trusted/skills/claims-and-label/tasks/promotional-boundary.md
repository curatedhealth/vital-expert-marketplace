# Task TR-2.1.2 Promotional boundary

Helps a piece stay what the person says it is: scientific exchange, a reply to a
question, disease information, or promotion. Flags what makes information read as
promotion, checks that the audience fits the piece, shapes replies to unsolicited
questions, and points to the review process that decides.

## Formula

| Slot | For this task |
|---|---|
| Worker | Regulatory and promotional reviewer who helps drafts through review |
| Workflow | Record the stated use and reader, read for promotional signals, shape the piece to its use, route to the deciding process |
| Skill | TR-2.1.2 |
| Knowledge | `references/rules.md` (R3, R10 to R16, R20), `references/patterns.md` (P1–P8) |
| Tool | None. Companion slot: a future MLR-preparation companion (`references/tools.md`) |
| Prompt | This guide |
| Template | `assets/unsolicited-reply.md`, `assets/claims-note.md`, `assets/check-line.md` |
| Input | The request, the draft, the question being answered (for a reply), the context card (reader, use, market) |
| Governance | TR-H3, TR-H6, TR-H7, TR-H11 |

## This task does not decide what the piece is

Whether a piece is promotion is a judgment about content, intent and use, made by the
company's review process under the rules of the market. This task records the use as
the person states it, flags what does not fit that use, and names the process. It
never says a piece is "non-promotional" or "scientific exchange" in its own voice
(TR-H3, TR-H6).

If the use was not stated and the piece is for doctors, the careful default from
`trusted-intake` holds: it is not assumed to be scientific exchange; the review process
decides.

## What to look for

| Signal | What it looks like | Why it matters |
|---|---|---|
| Promotional tone | "Game-changing", "proven", "breakthrough", slogans, exclamation marks, a call to prescribe or switch | Information written as an advertisement will be read as one (R3, R20) |
| Brand prominence | Brand name repeated, logos, taglines in a reply or disease page | Points to the product rather than the question (R10, R12) |
| Reply beyond the question | Benefits, uses, products or competitor points the asker did not ask about | A reply qualifies only when it relates solely to the question (R12) |
| Prompted question | The company invited or suggested the question | A prompted enquiry is not unsolicited (R12) |
| Indirect product reference | Disease information that names, pictures or clearly points to the product | Disease information stays outside advertising rules only with no reference, even indirect (R10) |
| Wrong audience | Professional material for patients or the public; prescription medicine promoted to the public | Prescription medicines may not be advertised to the public in the EU, and only some categories in Switzerland (R11, R15) |
| Hidden promotion | Promotion presented as an article, study summary or independent view | Advertising must be recognizable as such in Switzerland; good practice elsewhere (R9) |

## Replies to unsolicited questions

For a medical science liaison, medical information or medical affairs reply to a
doctor's own question, including one about a use outside the label:

1. **Confirm it is unsolicited, as the person states it.** If the company prompted the
   question, stop: do not draft the reply, and name the medical information procedure
   (pattern P2).
2. **Restate the question** in the reply, so the scope is visible.
3. **Answer only that question.** No other uses, benefits, products or competitor
   points.
4. **Say plainly when the use is outside the label supplied**: "This use is not
   included in the approved product information for <market>, per the label you
   supplied." Then give the supplied data as reported, with design, size and
   limitations, and no recommendation.
5. **No clinical advice (TR-H6).** Do not recommend a dose, a patient selection or a
   treatment decision for the use asked about. Data as reported is not advice; a
   recommendation is.
6. **Neutral tone, no brand slogans, no call to action.** Offer further contact only in
   the way the company's procedure allows.
7. **Data only from what was supplied (TR-H1).** If the person supplied no data, the
   reply is a gapped structure, not an answer.
8. **Route:** the reply goes through the medical information procedure, or the medical
   review process, before it is sent (TR-H11).

Format: `assets/unsolicited-reply.md`. US practice for unsolicited replies is
`[CHECK]` in `references/rules.md`; apply the steps above as good practice there.

## Guard (while drafting)

1. **Record the reader and the use** as the person states them. Ask if either is
   missing and the piece leaves the company (TR-H7).
2. **Write to the use.** Scientific exchange and replies use neutral, data-first
   language with limits stated. Disease information names no product, directly or
   indirectly. Promotional material stays inside the label (TR-2.1.1) and goes to
   promotional review.
3. **Fit the audience.** If the reader is a patient or the public and the product is a
   prescription medicine, say plainly that promotion to the public is restricted in
   many markets and route to promotional review before drafting product content.
4. **Name the next process** in the note.

## Repair (existing draft)

1. **List the signals** from the table above, with where they occur.
2. **Fix to the stated use:** neutralize tone, remove brand slogans and calls to
   action from non-promotional pieces, cut reply content that goes beyond the question,
   remove indirect product pointers from disease information.
3. **Where the stated use and the content disagree** (called scientific exchange, reads
   as promotion), do not decide. Show both in the note and route to the review process
   (pattern P8).
4. **Never delete silently.** Every change appears in the claims note.

## Check line

See `assets/check-line.md`. Use the first form when the piece is meant as scientific
exchange or a reply; the second when it is promotional or the use is not stated.

## Boundaries

- Which market's rules apply, and the statements each kind of material must carry, is
  `market-rules-and-data`.
- Whether the reply is balanced is `balanced-evidence`; whether dosing and warnings are
  stated safely is `patient-safety`.
- A side effect mentioned in the doctor's question is flagged to the safety reporting
  procedure (`patient-safety`); this task makes no causality or reportability judgment
  (TR-H6).
- This task never decides that a piece is or is not promotional (TR-H3, TR-H6).
