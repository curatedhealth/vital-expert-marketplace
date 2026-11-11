# Intake: trusted-intake

This skill makes the context card, so there is no earlier card to read unless one exists
for this piece of work. Look for one in the conversation first. If it is there, start from
it, update only the field the person changed, and ask nothing it already answers.
When another skill is used alone and the conversation holds no card, that skill takes what the message says, asks at most its own questions, and intake does not run separately.

## What this skill needs

| Need | Comes from | If it is missing |
|---|---|---|
| The request and anything attached or pasted | The conversation | Read it fully before any question |
| Reader | The request ("for the board", "a doctor wrote in") | Ask, unless the work cannot leave the company |
| Market | The request or an attached label | Ask when the work is about a product and leaves the company |
| Use (scientific exchange or promotion) | The request, as the person states it | Ask when the reader is a doctor or other prescriber and it could be read either way. For other work leaving the company, assume promotional and say so in one line |
| Product status | A label the person supplied, or what they said, in their own words ("launched" stays "launched") | Ask only when the work makes product statements and it cannot be read |
| What AI use policy says about a sensitive input | The person | Ask first, before anything else, when something sensitive is pasted or mentioned |

## Questions

If any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem, patient-safety's flag goes out first, in its template
wording (`../patient-safety/templates/safety-flag.md`), before any question and before
any draft, whatever letters are active (TR-H14). No stop rule or intake step holds it
back.

At most one combined question in one turn, asked alongside the draft (draft first,
TR-H7). None at internal and quick, unless the data question applies. Pick the field
highest in this order:

- First, the AI use policy question, when a sensitive input came up.
- Then reader, if unknown.
- Then market.
- Then use.
- Then product status.
- Then material, when the work needs facts and none were given.

Two related fields can share the question. The cap is for the whole reply, including any
question from the skill that drafts in the same reply: one combined question in all. Everything else becomes a gap in the draft or
one stated assumption, with the careful option chosen. The card always says what was not
seen ("label: not seen"). The full method is in `tasks/work-context.md` and
`tasks/data-and-policy-context.md`.

## Never

- Hand over a list of fields to fill in.
- Ask about tone, format or voice unless the work cannot be drafted without it.
- Ask for patient names, ages or histories.
- Ask the assistant to decide whether a tool is approved. Record what the person says.
