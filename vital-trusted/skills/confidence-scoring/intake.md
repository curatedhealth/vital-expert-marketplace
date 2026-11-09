# Intake: confidence-scoring

Read the context card from `trusted-intake` first (`../trusted-intake/templates/context-card.md`).
If the conversation holds one for this work, take the reader and stakes from it and do not
ask again for anything it holds. Then read what `claim-assessment` and `source-assessment`
already produced in the conversation. This skill works from those results and adds no
new checking of its own.
When the conversation holds no card (this skill used alone), take what the message says, ask at most the questions below, and do not run intake separately.

## What this skill needs

| Need | Comes from | If it is missing |
|---|---|---|
| The results of the hand check, one per claim | `claim-assessment` in this conversation | Do not ask for a number. If the material and its passages are pasted, run the claim check by hand first, then give one combined summary (`templates/open-items.md`). If they are not pasted, ask for them. If the person reports a check done elsewhere, see the stop rule in `governance.md` |
| The source notes | `source-assessment` in this conversation | Carry on without them and say so in one line |
| Reader | The card or the request | Ask once (question 1) |

## Questions

At most one. Plain words, with the reason.

1. "Who will read this?" Ask only when neither the card nor the request shows it and the
   level of detail would differ.

A request for a percent or a score is answered, not asked about: results are counts only,
with no confidence figure, and the open items are listed for a person to
decide.

## Never

- Estimate a percent, or print one. Every result is by hand and there is no figure.
- Say that a count means the work is fine to send.
- Ask whether a tool is connected.
