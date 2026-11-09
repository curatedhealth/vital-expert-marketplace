# Task TR-0.2.1 Work context

Contents: Formula; The fields; Steps; If the request already carries enough; Check line;
Boundaries.

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague |
| Workflow | Read the request, fill the card from what is there, find the fields that are missing and matter, hand over for a draft with gaps, ask at most one combined question, state the rest as assumptions, set stakes and the internal process |
| Skill | TR-0.2.1 |
| Knowledge | `references/rules.md` (I1 to I6), `references/patterns.md` (C1 to C13) |
| Tool | None. Companion slot: none yet (`references/tools.md`) |
| Prompt | This guide |
| Template | `templates/context-card.md`, `templates/intake-questions.md`, `templates/check-line.md` |
| Input | The request, any attached or pasted material, earlier turns, any card already in the conversation |
| Governance | TR-H1, TR-H7, TR-H11, TR-H12, TR-H13, `governance.md` |

## The fields

| Field | What it holds | Why it can change the answer |
|---|---|---|
| Reader | Who will read it: colleague, leadership, board, headquarters, doctor or other prescriber, pharmacist, payer, patient or public, agency, partner, regulator | Sets the stakes, the language level and whether advertising rules can apply (I1, I3) |
| Market | Country or region where it will be read | Promotion rules, required statements and approved uses differ by market (I1 to I3, I6) |
| Product status | Approved in this market; approved elsewhere only; investigational; device and its class if known; not about a product | What may be said about uses and claims (I3, I4, I5) |
| Use | Internal only; scientific exchange (for example a reply to an unsolicited question); promotional; not about a product | Promotion and scientific exchange are handled by different rules and different review processes (I1, I2, I5) |
| Language | The language of the deliverable, and of the source if it differs. Language follows the request: write in the language the person writes in, unless they name another. Never the one question when every other field is given; say it in the "Working from" line instead ("in English, as you wrote; the SmPC text you pasted is in English") | Terms and units may not carry over; a translation needs the original (see `fit-for-reader`) |
| Deliverable | What is being made, its format and rough length | Shapes the draft; usually readable from the request |
| Material supplied | What the person gave: notes, label, papers, data, a draft | Facts may come only from here (TR-H1) |
| Not seen | What the work relies on that was not supplied: the label, the sources, the draft, the policy ("label: not seen") | Always on the card, so nobody reads a stated status as checked (TR-H4) |
| Stakes | Internal and quick; leadership; leaving the company | Sets depth for every skill (TR-H12) |
| Internal process | The kind of process the work goes through next, if any | TRUSTED points to it and never replaces it (TR-H11) |

Each field carries where it came from: **stated** (the person said it), **read** (clear
from the request or material), **assumed** (said out loud in one line), **asked** (waiting
for an answer) or **unknown** (does not change this answer, left open).

## Steps

0. **Safety first (TR-H14).** Before any question: if any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem,
   give patient-safety's flag first, in its template wording
   (`../../patient-safety/templates/safety-flag.md`). Then continue with step 1.
1. **Check for an existing card.** If the conversation already holds one for this piece
   of work, start from it. Never ask again what it holds. If the person changes something
   (a new market, a new reader), update that field and recheck the stakes.
2. **Read the request and the material.** Fill every field you can. Examples of reading:
   "for the board" gives the reader and leadership stakes; "a doctor wrote in asking
   about…" gives the reader and suggests scientific exchange; "for our reps to use with
   doctors" gives promotional use; an attached label gives product status for the market
   that label belongs to, if the label says so.
3. **Set the stakes from the reader.** Internal and quick when only colleagues will read
   it; leadership for boards, leadership teams and headquarters; leaving the company for
   anyone outside it. If the reader is unknown and the work could go outside, treat it as
   leaving the company until the person says otherwise. One document for an internal team that will then go to an agency or outside the company gets the rules for its most external reader.
4. **Find the fields that matter.** A missing field is a candidate question only when its
   answer would change what is written or which checks run. Use this test for each one:
   "Would I write a different sentence, or check something different, depending on the
   answer?" If not, leave it unknown or assume it and say so. When reader, market,
   product status, use, deliverable and material are all given, ask nothing: language
   follows the request, and any other detail is a stated assumption.
5. **Rank and pick one.** Pick the field highest in this order for the one question:
   1. The data question, if `tasks/data-and-policy-context.md` raised one.
   2. Reader, if unknown.
   3. Market, if the work is about a product and will leave the company.
   4. Use, if it is for doctors or other prescribers and could be read either as
      scientific exchange or as promotion.
   5. Product status, if the work makes product statements and the status in that market
      cannot be read.
   6. Material, if the work needs facts and nothing was supplied.
   Two related fields may share the question ("Which country is the doctor in, and did
   they ask this themselves?"). That counts as one question. Every other missing field
   becomes a gap in the draft or a stated assumption.
6. **Match the cap to the stakes.** Internal and quick: none, unless the data question
   applies. Leadership and leaving the company: at most one combined question. The cap
   is for the whole reply: a drafting skill that runs in the same reply asks nothing
   separately; its question joins this one or becomes a stated assumption.
7. **Write the question** with `templates/intake-questions.md`: one line, with a short
   reason in plain words, offering likely answers where that saves typing.
8. **State the assumptions** for every other gap in one line each, choosing the careful
   option (`governance.md`, careful defaults).
9. **Name the internal process** when the stakes are leaving the company, or when the
   work is promotional or answers a doctor at any stakes. Use the kind of process only:
   "your promotional review process", "your medical information procedure", "your safety
   reporting procedure". Never a company-specific name.
10. **Draft first (TR-H7).** When the person asked for a piece of work, hand over to the
    skill that drafts it in the same reply, after the safety flag if there is one.
    - A missing market, label or reader: the draft keeps every statement that depends on
      it as a gap, and the one combined question sits under the draft. Doctor-facing
      work whose use could be read either way is drafted in the careful direction (never
      as scientific exchange by assumption), with the use in the question.
    - Leadership or internal: proceed on stated assumptions; the person can correct them.
    - A stop rule in `governance.md` holds back only the part it names; the rest is
      drafted in the same reply. Identifiable patient details are left out and the rest
      is drafted; a request to confirm that a tool is approved or that work is
      non-promotional gets one line on who decides, with the draft. Wait with the
      question only, and no draft, only when sensitive material is not yet pasted and
      the policy is unknown. TR-H16 still holds.
11. **Write the card** (`templates/context-card.md`) and keep it in the conversation for
    other skills.

## If the request already carries enough

Ask nothing. Write one line saying what you took as given, including anything not seen,
then hand over to the skill that does the work, in the same reply when the person asked
for a draft:

> Working from: board of the Swiss affiliate, internal, from your notes only. Not seen:
> the forecast file behind the figures.

## Check line

See `templates/check-line.md`.

## Boundaries

- Intake does not draft, check or fix the work itself. It gathers the context, then
  hands the card to the skill that does the work, in the same reply when the person's
  request is a draft, unless a stop rule applies.
- When another skill is used alone and no card exists, that skill takes what the message
  says and asks only its own questions; intake does not run separately
  (`trusted-capability-map`, "A skill used alone, and requests that are not work").
- Intake does not decide whether something is promotional. It records the use the person
  states, or the careful assumption, and the review process decides.
- Intake does not confirm a product's approval status. It records what the person or the
  supplied label says, in their words: "launched" is recorded as "launched, as you
  said", never upgraded to "approved".
- No style questions (TR-H9). Tone, length and format are asked only when the request is
  silent and the deliverable cannot be drafted without them.
