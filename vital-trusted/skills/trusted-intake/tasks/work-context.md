# Task TR-0.2.1 Work context

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague |
| Workflow | Read the request, fill the card from what is there, find the fields that are missing and matter, ask at most three, state the rest as assumptions, set stakes and the internal process |
| Skill | TR-0.2.1 |
| Knowledge | `references/rules.md` (I1 to I6), `references/patterns.md` (C1 to C13) |
| Tool | None. Companion slot: none yet (`references/tools.md`) |
| Prompt | This guide |
| Template | `assets/context-card.md`, `assets/intake-questions.md`, `assets/check-line.md` |
| Input | The request, any attached or pasted material, earlier turns, any card already in the conversation |
| Governance | TR-H1, TR-H7, TR-H11, TR-H12, TR-H13, `references/governance.md` |

## The fields

| Field | What it holds | Why it can change the answer |
|---|---|---|
| Reader | Who will read it: colleague, leadership, board, headquarters, doctor or other prescriber, pharmacist, payer, patient or public, agency, partner, regulator | Sets the stakes, the language level and whether advertising rules can apply (I1, I3) |
| Market | Country or region where it will be read | Promotion rules, required statements and approved uses differ by market (I1 to I3, I6) |
| Product status | Approved in this market; approved elsewhere only; investigational; device and its class if known; not about a product | What may be said about uses and claims (I3, I4, I5) |
| Use | Internal only; scientific exchange (for example a reply to an unsolicited question); promotional; not about a product | Promotion and scientific exchange are handled by different rules and different review processes (I1, I2, I5) |
| Deliverable | What is being made, its format and rough length | Shapes the draft; usually readable from the request |
| Material supplied | What the person gave: notes, label, papers, data, a draft | Facts may come only from here (TR-H1) |
| Stakes | Internal and quick; leadership; leaving the company | Sets depth for every skill (TR-H12) |
| Internal process | The kind of process the work goes through next, if any | TRUSTED points to it and never replaces it (TR-H11) |

Each field carries where it came from: **stated** (the person said it), **read** (clear
from the request or material), **assumed** (said out loud in one line), **asked** (waiting
for an answer) or **unknown** (does not change this answer, left open).

## Steps

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
   leaving the company until the person says otherwise.
4. **Find the fields that matter.** A missing field is a candidate question only when its
   answer would change what is written or which checks run. Use this test for each one:
   "Would I write a different sentence, or check something different, depending on the
   answer?" If not, leave it unknown or assume it and say so.
5. **Rank and cap.** Ask in this order, stopping at three:
   1. The data question, if `tasks/data-and-policy-context.md` raised one.
   2. Reader, if unknown.
   3. Market, if the work is about a product and will leave the company.
   4. Use, if it is for doctors or other prescribers and could be read either as
      scientific exchange or as promotion.
   5. Product status, if the work makes product statements and the status in that market
      cannot be read.
   6. Material, if the work needs facts and nothing was supplied.
   Two related fields may share one question ("Which country is the doctor in, and did
   they ask this themselves?"). That counts as one question.
6. **Match the cap to the stakes.** Internal and quick: none, unless the data question
   applies. Leadership: at most one. Leaving the company: up to three.
7. **Write the questions** with `assets/intake-questions.md`. Each question is one line,
   with a short reason in plain words, and offers likely answers where that saves typing.
8. **State the assumptions** for every other gap in one line each, choosing the careful
   option (`references/governance.md`, careful defaults).
9. **Name the internal process** when the stakes are leaving the company, or when the
   work is promotional or answers a doctor at any stakes. Use the kind of process only:
   "your promotional review process", "your medical information procedure", "your safety
   reporting procedure". Never a company-specific name.
10. **Decide whether to wait or proceed.**
    - Leaving the company, and market or use is missing: wait for the answer before
      drafting. A draft written for the wrong market or use has to be thrown away.
    - Leadership or internal: proceed on stated assumptions; the person can correct them.
    - The person says "just draft it": proceed, keep the assumptions visible, and keep
      unknown product statements as gaps.
11. **Write the card** (`assets/context-card.md`) and keep it in the conversation for
    other skills.

## If the request already carries enough

Ask nothing. Write one line saying what you took as given, then do the work:

> Working from: board of the Swiss affiliate, internal, from your notes only.

## Check line

See `assets/check-line.md`.

## Boundaries

- Intake does not draft, check or fix the work. It hands the card to the skills that do.
- Intake does not decide whether something is promotional. It records the use the person
  states, or the careful assumption, and the review process decides.
- Intake does not confirm a product's approval status. It records what the person or the
  supplied label says.
- No style questions (TR-H9). Tone, length and format are asked only when the request is
  silent and the deliverable cannot be drafted without them.
