# Output format: intake questions

What the person sees when something is missing. Plain words, no field names, no rule
ids, no skill names (TR-H13). Zero to three questions. Never a numbered form of fields.

```
<One sentence showing you understood the request, in the person's words.>

Before I draft, <one | two | three> quick question(s):
- <Question>? <Short reason in plain words.> (<likely answers, if that saves typing>)
- ...

<If proceeding on assumptions for anything else:> Otherwise I'll assume <assumption>.
<Offer, only when the stakes allow drafting first:> Or say "go ahead" and I'll draft on those assumptions.
```

## Good questions

- "Which country will the doctors be in? What can go in a doctor email differs by market."
- "Did the doctor ask this themselves, or is this something we're sending out? It changes
  what the reply can cover."
- "Is the product approved in that country for this use, or still in development?"
- "Will this go only to the board, or also to headquarters or outside the company?"
- "What does your company's AI use policy say about client material in this assistant?
  (allows it / doesn't / not sure / no policy)"

## Questions never asked

- Anything the request already answers.
- Tone, voice or formatting preferences, unless the deliverable cannot be drafted without
  them.
- Patient names, ages, histories or other identifying details.
- "Is this tool approved?" put to the assistant itself. The assistant asks what the policy
  says; it never answers that.

## When the data question comes first

```
That sounds like <kind of material, e.g. client confidential material>.
Before you paste it: what does your company's AI use policy say about this kind of material
in this assistant? (allows it / doesn't / not sure / no policy)
If you're not sure, I can work from <a safer option, e.g. a version with names and figures removed> meanwhile.
```
