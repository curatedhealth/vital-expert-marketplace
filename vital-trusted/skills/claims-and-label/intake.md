# Intake: claims-and-label

Safety first (TR-H14): if any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person,
   medication error, lack of effect or product quality problem, patient-safety's flag
(`../patient-safety/templates/safety-flag.md`) comes before any question below. No
question here comes before it or holds it back.

Then read the context card from `trusted-intake` (`../trusted-intake/templates/context-card.md`).
If the conversation holds one for this work, take the reader, market, use and product status
from it and do not ask again for anything it holds. Product status stays "as you said" or
"per your label". It never comes from memory.
When the conversation holds no card (this skill used alone), take what the message says, ask at most the questions below, and do not run intake separately.

## What this skill needs

| Need | Comes from | If it is missing |
|---|---|---|
| The draft or the claims to check | The person | Ask for it |
| The label or intended purpose for the market | A document the person supplied | Ask for it (question 1), using `templates/label-request.md`. If the person goes on without it, mark every product statement as a gap and say so in one line |
| Use, as the person states it: promotional, scientific exchange, a reply to a question, disease information, internal | The card or the request | Ask (question 2) when the reader is a doctor, patient or the public |
| Market | The card or the label | Ask (question 3) only when the piece leaves the company |

## Questions

Ask them as one combined question, drawn from at most these three, and give the draft with gaps in the same reply unless a stop rule applies, and none for internal brainstorming. Plain words, one line each, with the
reason.

1. "Can you paste the label or intended-use text for this product in that country? I only
   check against what you give me, not what I recall about it." Ask only when the draft
   makes product statements and no label was supplied.
2. "Did the doctor ask this themselves, or is it going out without being asked?" Ask only
   when the piece could be read as scientific exchange or as promotion.
3. "Which country is it for?" Ask only when the piece leaves the company and the card and
   label do not show it.

## Never

- Say whether a use is approved. Say what the supplied label includes or does not include.
- Work from memory of what the product is for.
- Decide whether the piece is promotional. Record the use the person states.
