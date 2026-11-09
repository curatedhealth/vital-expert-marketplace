# Intake: responsible-inputs

Safety first (TR-H14): if any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person,
   medication error, lack of effect or product quality problem, patient-safety's flag
(`../patient-safety/templates/safety-flag.md`) comes before any question below. No
question here comes before it or holds it back.

Then read the context card from `trusted-intake` (`../trusted-intake/templates/context-card.md`).
If the conversation holds one for this work, take the input kinds, the AI use policy line,
the reader and the stakes from it and do not ask again for anything it holds. A card line
that says the person states their policy allows this use stands as stated. It is not
decided here.
When the conversation holds no card (this skill used alone), take what the message says, ask at most the questions below, and do not run intake separately.

## What this skill needs

| Need | Comes from | If it is missing |
|---|---|---|
| What the material is | Reading what was pasted or described | Read it before asking |
| What the company's AI use policy says about it, as the person states it | The card, or the person | Ask (question 1) when the material is sensitive and the card has no policy line |
| Where the result will go | The card or the request | Ask (question 2) only when it changes the advice |
| Whose work it is, for an article, report or guideline | The material or the person | Ask (question 3) only when the request is to reproduce or rework it |

## Questions

Ask them as one combined question, drawn from at most these three, and give the draft with gaps in the same reply unless a stop rule applies. None for public material or the person's own non-sensitive work, where this
skill says nothing about inputs. Plain words, one line each, with the reason.

1. "What does your company's AI use policy say about this kind of material in this
   assistant? Allows it, does not, not sure, or no policy?"
2. "Where will the result go: only you, your team, or outside the company?" Ask only when
   it is unclear and the answer changes the safer route.
3. "Is this your company's own work, or someone else's article or report?" Ask only when
   the request is to copy or rework a full document.

## Never

- Decide whether a tool is approved. The person and their AI policy owner decide.
- Ask for patient or personal identifiers.
- Warn about public material or a person's own non-sensitive work.
