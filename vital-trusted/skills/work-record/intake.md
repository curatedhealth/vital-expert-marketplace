# Intake: work-record

Read the context card from `trusted-intake` first (`../trusted-intake/templates/context-card.md`).
If the conversation holds one for this work, take the reader, stakes, material and next
process from it. Take the assistant, the connectors and what the AI did from the
conversation itself, as it shows them. Do not ask again for anything these hold.
When the conversation holds no card (this skill used alone), take what the message says, ask at most the questions below, and do not run intake separately.

## What this skill needs

| Need | Comes from | If it is missing |
|---|---|---|
| The work the record is for | The conversation | Ask for it |
| Who will read the record, which sets its size | The card or the request | Ask once (question 1) |
| The materials the work was built from | The conversation and the card | Ask (question 2) only when the conversation does not show them |
| Whether anyone has reviewed it, and who | The person | Ask (question 3) only when a status is wanted. Without a named person the status is draft |

## Questions

Ask them as one combined question, drawn from at most these three, and give the record, with gaps where details are missing, in the same reply unless a stop rule applies. None for a quick internal note, where no record is added. Plain words, one
line each, with the reason.

1. "Who will read this record?" Ask only when the card and request do not show it.
2. "Which materials did you use for this: notes, papers, data?" Ask only when the
   conversation does not show them.
3. "Has someone reviewed this? If so, who, and on what date?" Ask only when a status such
   as reviewed or approved is requested.

Owners of open decisions are never guessed. Write "owner to be named" unless the person
said who.

## Never

- Mark work as approved or final on request. A named person's own statement is recorded as
  "as you told me".
- Add a draft banner or an open-items list to a quick internal note that did not ask for one.
