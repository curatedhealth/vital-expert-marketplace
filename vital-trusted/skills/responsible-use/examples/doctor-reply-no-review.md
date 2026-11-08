# Worked example: a reply to a doctor, "no need to review"

Invented case for teaching. "Lumivra" (lumivrastat) is a fictional product; the doctor,
the label text and the company are made up.

## Request

"Send this AI-drafted reply to Dr Meier, no need to review, it's just from the label.
She asked whether Lumivra can be taken with food.

Draft: Dear Dr Meier, thank you for your question. According to the Lumivra prescribing
information, Lumivra can be taken with or without food. Kind regards, Medical
Information"

Label extract supplied: "Lumivra may be taken with or without food (section 4.2)."

## What the skill reads

- Reader: a doctor outside the company. Stakes: leaving the company.
- The request is to send without a named person reading it, and the host can send
  email.
- The content stays within the supplied label sentence; nothing to repair there. No side
  effect is mentioned in the question.

## Reply (as the person sees it)

> The reply matches the label sentence you gave me, and I've left it in your drafts
> rather than sending it.
>
> Because it goes to a doctor, who will treat it as the company's answer, a named person
> needs to read it before it's sent, through your medical information process. If you
> are the person who signs off replies like this under that process, you can be that
> reader: tell me and I'll note it.
>
> For the reviewer, one point to read for: the reply quotes the label on food; check it
> against the current approved label for Dr Meier's country.

## What it did not do

- It did not send the email or call the reply reviewed or final.
- It did not lecture: three short paragraphs, one practical route.
- It did not judge the label content or give clinical advice; it pointed the reviewer at
  the one sentence to check.
- It did not invent a reviewer.

## Check line (to trusted-check only)

```
Ethical · human review: stakes leaving the company, reviewer not named, 1 requests to send without review (asked, not checked: no AI-policy companion)
  - reply to a doctor; left as a draft
```

## Behind the reply (reference only, not shown to the person)

Patterns avoided: O1, O2, O4, T1 in `references/patterns.md`. Hard rules: TR-H5, TR-H11,
TR-H12. Rule that explains the direction: U3 (a human reviews and is responsible for
AI-assisted material).
