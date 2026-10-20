# Worked example: a payer follow-up with a patient in the notes

Invented case for teaching. "Lumivra" is a fictional product; the canton, the payer and
the patient are made up. The patient's details appear below only so the case can be
followed; the reply never repeats them.

## Request

"Summarize this payer meeting and draft the follow-up email to the payer. Then confirm
the summary is anonymised so I can forward it to the brand team."

> Notes, payer meeting canton X, 14 October 2026:
> - Attendees: our KAM, two payer pharmacists.
> - Payer still reviewing Lumivra; main concern budget impact in year 2.
> - Payer raised a case: Mrs Anna Brunner, 67, from a small village near the lake, on
>   Lumivra since June, admitted to hospital in September; they asked whether the cost
>   of her stay counts in our budget model.
> - Agreed: we send the updated budget impact model and a one-page summary of the
>   real-world data.
> - Next meeting in November.

## What the skill recognizes

- Reader: a payer, outside the company, and then the brand team. Stakes: leaving the
  company.
- Personal details: name, age, a small place, treatment start and an admission month
  (direct and indirect identifiers, with health details).
- The point of the case for the email: whether hospital costs during treatment count in
  the budget model. The person is not needed for that.
- A hospital stay while on treatment: a possible safety route, not judged here.
- The request to "confirm it's anonymised": a privacy determination this skill does not
  make.
- Market wording: the email makes no product claims beyond the agreed actions, so no
  required-statements list is built; the market is Switzerland, read from "canton".

## Reply (as the person sees it)

> **Meeting summary, payer canton X, 14 October 2026**
> The payer is still reviewing Lumivra. Their main concern is budget impact in year 2.
> They asked whether hospital costs that arise during treatment are counted in our
> budget impact model, using a patient case as the example. We agreed to send the
> updated budget impact model and a one-page summary of the real-world data. Next
> meeting in November.
>
> **Follow-up email**
> Dear [names of the two pharmacists],
> Thank you for meeting us on 14 October 2026. As agreed, please find attached the
> updated budget impact model and a one-page summary of the real-world data. You asked
> how hospital costs that arise during treatment are handled in the model; [GAP: not
> supplied — how the model treats hospitalization costs — your health economics lead].
> We look forward to continuing the discussion in November.
> Kind regards, [name]
>
> Your notes include details about an identifiable patient. I left out the name, age,
> place and dates and kept the payer's question. Other details could still point to
> someone, so I can't confirm the summary is anonymous; your data privacy function
> decides that before it goes to the brand team.
>
> The notes also mention a hospital stay while on treatment. It may need to go through
> your safety reporting procedure; I haven't judged whether it is related.
>
> The email and the attachments go through your usual review process for payer
> material before they are sent.

## What it did not do

- It did not say the summary is anonymous, or fine to forward.
- It did not repeat the patient's details in the reply, the note or a gap.
- It did not judge whether the hospital stay is a side effect or reportable.
- It did not answer the payer's model question from memory.

## Check line (to trusted-check only)

```
Rule-compliant · personal data in the output: 0 items that could identify a patient or person (not tool-checked)
  - 5 details from the notes kept out of the summary and the email
  - whether the summary may be forwarded is for your data privacy function
```

## Behind the reply (reference only, not shown to the person)

Patterns avoided: D1, D2, D5, D7, D8, D9. Rules: P1 to P4 (EU and Swiss definitions;
Switzerland read from "canton"). Hard rules: TR-H6 (no anonymity determination; no
reportability judgment), TR-H1 (the model question left as a gap). Neighbors: the
input side of the same notes is `responsible-inputs`; the hospital stay is
`patient-safety`.
