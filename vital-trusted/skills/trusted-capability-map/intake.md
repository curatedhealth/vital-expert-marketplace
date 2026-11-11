# Intake: trusted-capability-map

Read the request first. If the conversation already holds a context card from
`trusted-intake` (`../trusted-intake/templates/context-card.md`), take the reader,
market, use and stakes from it and do not ask again for anything it holds.
When the conversation holds no card (this skill used alone), take what the message says, ask at most the questions below, and do not run intake separately.

## What this skill needs

| Need | Comes from | If it is missing |
|---|---|---|
| What the person wants: to understand TRUSTED, to set letters, or help with a piece of work | The request | Ask question 1 |
| Which letters are on or off | The person's last choice in the conversation, or all seven by default | Ask question 2 only when a change is requested and unclear |
| For routing a piece of work: the work itself | The request or attachment | Route to `trusted-intake`; do not collect it here |

## Questions

At most one combined question here, drawn from the two below, and none when the request
is clear. Plain words, one line, with the reason.

1. "Do you want to know what TRUSTED does, change which checks run, or get help with a
   piece of work?" Ask only when the request does not say.
2. "Which of the seven checks should be off: Tangible, Rule-compliant, Unbiased, Safe,
   True, Ethical, Defensible?" Ask only when the person says "turn some off" or "just the
   basics" without naming them.

Reader, market, product status and use are not asked here. When the request is a draft,
a fix or a check, hand over to `trusted-intake` so the questions are asked once, in one
place.

## Never

- Ask for a draft before answering a plain "what does TRUSTED do" request.
- Ask the person to name a skill. Describe the next step in everyday words.
- Turn a letter back on after the person turned it off.
