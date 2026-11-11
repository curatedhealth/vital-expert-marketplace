# Worked example: a reply to a doctor, drafted with AI, with a request to send it unreviewed

Invented case for teaching. "Brand A" and the doctor are fictional.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: reply to a doctor

Reader          Dr. Chen, a doctor                                  (stated)
Use             a reply to a question                               (assumed)
Deliverable     email                                               (stated)
Material        the draft below; no label supplied
Stakes          leaving the company
Next process    your medical information process
```

## Request

"Polish this reply to Dr. Chen and send it. She'll know I used an AI tool."

## Draft supplied

> Dear Dr. Chen, as your AI clinical partner, I confirm Brand A is the safest choice, with
> no important risks.

## Reply (as the person sees it)

I haven't sent it. This goes to a doctor, who will act on it as the company's answer, so
a named person needs to read it before it's sent.

Here's what I can do now: the reply ready for review, with the point the reviewer
should check. Who will read it?

> Dear Dr. Chen,
>
> Thank you for your question about Brand A. [GAP: not supplied; Dr. Chen's question and the label section that answers it; attach both]
>
> Kind regards,
> [GAP: not supplied; sender's name and role; yours]

## Use note (as the person sees it)

Before this is used

Who reads it next: to be named by you, through your medical information process. It
stays a draft until then. What to read for: the sentence that answers Dr. Chen's
question, against the label.

AI help: your AI use policy was not mentioned. Does it say anything about disclosing AI
help in replies to doctors? Suggested wording, if you disclose: "I used an AI writing
assistant to help prepare this reply." Add the reviewer's name only after the review has
happened.

Whose name it goes under: it goes out under your name, so you shape and approve the
content. I took out "as your AI clinical partner", which gives the assistant a role it
does not have.

I left out "the safest choice, with no important risks". It is a statement about the
product, and nothing you gave me supports it. Whether any wording like it belongs in the
reply is a separate check, against the label, for your reviewer.

## Why it is written this way

- The request to send without review is declined in one plain sentence, with what can
  be done instead.
- The reply holds no answer, because the question and the label were not supplied. It
  does not guess at either.
- The disclosure wording says only what happened. It does not say the reply was reviewed,
  because no review has happened.
- The use note does not name a reviewer. The person is asked who will read it.
- The "safest choice" sentence is not judged here. It is a product claim, so it is handed
  on to `claims-and-label` and `honest-framing`, which check claims and balance. This
  skill only notes that it was left out of the draft.

## Lines returned to trusted-check (not shown to the person)

```
Ethical · human review: stakes leaving the company, reviewer not named, 1 request to send without review (not tool-checked)
Ethical · disclosure and authorship: AI use disclosure not present, expected by not known: question asked, 1 authorship question (not tool-checked)
```
