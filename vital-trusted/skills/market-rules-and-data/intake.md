# Intake: market-rules-and-data

Safety first (TR-H14): if any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person,
   medication error, lack of effect or product quality problem, patient-safety's flag
(`../patient-safety/templates/safety-flag.md`) comes before any question below. No
question here comes before it or holds it back.

Then read the context card from `trusted-intake` (`../trusted-intake/templates/context-card.md`).
If the conversation holds one for this work, take the market, reader, use and stakes from
it and do not ask again for anything it holds.
When the conversation holds no card (this skill used alone), take what the message says, ask at most the questions below, and do not run intake separately.

## What this skill needs

| Need | Comes from | If it is missing |
|---|---|---|
| The draft, or the material to draft from | The person | Ask for it |
| Market the piece is for | The card or the request | Ask (question 1) when the piece leaves the company or names a market |
| Who could read it, including whether it could reach the public | The card or the request | Ask (question 2) when a doctor piece could be seen by patients |
| The prescribing-information link and the company name for required statements | The person | Leave a visible gap and say who supplies it. Ask (question 3) only when the person wants the statements filled in now |
| Whether the material holds details about real people | Reading the material | Do not ask. Keep identifiable details out of the output in every case |

Language: stay in the language the person asked for (`SKILL.md`, "Stay in the language
asked"). It is a note for drafting, not a question: never ask which language to use when
the request shows it, and never add a question for it.

## Questions

Ask them as one combined question, drawn from at most these three, and give the draft with gaps in the same reply unless a stop rule applies. None for a quick internal note, where privacy still runs quietly. Plain
words, one line each, with the reason.

1. "Which country will this be read in? What can be said and what must be added differs by
   market." Ask only when the card does not show it.
2. "Could this be seen by patients or the public, for example on a website or social
   channel?" Ask only when the reader is a doctor and the channel is open.
3. "What link and company name should the required statements use?" Ask only when the
   piece needs them and none were supplied.

## Never

- Write a link, a clause number or a company name the person did not give.
- Ask for patient names, ages or histories. The point is to keep them out.
- Say that data is anonymous. That is for the company's data privacy process.
