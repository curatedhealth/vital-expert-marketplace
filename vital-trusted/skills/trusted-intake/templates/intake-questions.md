# Output format: intake questions

What the person sees when something is missing. Plain words, no field names, no rule
ids, no skill names (TR-H13). At most one combined question, asked under the draft, not
instead of it (draft first, TR-H7). Never a numbered form of fields.

If any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem, patient-safety's flag comes first, above the questions,
in its template wording (`../../patient-safety/templates/safety-flag.md`) (TR-H14).

```
Working from: <one short line per field that matters, each with its source tag, as in the person view of `context-card.md`>
<If assumed:> I've assumed <assumption>; tell me if that's wrong.

<The draft, by the skill that owns it, with each statement that depends on a missing detail as a gap.>

One question: <question, covering at most two related fields>? <Short reason in plain words.> (<likely answers, if that saves typing>) I'll fill the gaps when you reply.
<If an internal process applies:> It goes through your <kind of process> before it's used.
```

Only when sensitive material is not yet pasted and the policy is unknown
(`governance.md`) does the question come alone, with no draft, saying why it has to
wait. Every other stop holds back only the part it names; the rest is drafted.

## Good questions

- "Which country will the doctors be in, and can you share the label there? What can go
  in a doctor email differs by market."
- "Did the doctor ask this themselves, or is this something we're sending out? It changes
  what the reply can cover."
- "Is it Austria or Switzerland, and can you share the label for the pen there?"
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
