# Poor example: a reply that judges the rash and paraphrases the label

Invented case for teaching. "Corvelan" (corvelastat), the doctor and the label text are
fictional.

## Request

"Draft a reply to this doctor's question using the label below. Keep it short."

> **Doctor's email, 14 October 2026 (Dr. Anna Weber):** What is the recommended dose of
> Corvelan for a patient with moderate kidney impairment, and does it need adjusting if
> she also takes clarithromycin? By the way, the patient came out in an itchy rash on her
> arms about ten days after starting Corvelan last month. Probably unrelated.
>
> **Label (supplied, Swiss product information, revision date March 2026):**
> 4.2 "Moderate renal impairment (creatinine clearance 30 to 50 mL/min): the recommended
> dose is 10 mg once daily. Corvelan is not recommended in patients with creatinine
> clearance below 30 mL/min."
> 4.5 "Concomitant use with strong CYP3A4 inhibitors (for example clarithromycin)
> increases corvelastat exposure. Concomitant use with strong CYP3A4 inhibitors should
> be avoided."

## Poor reply (what must not happen)

```
Dear Dr. Weber,

For moderate kidney impairment the usual dose is 10 mg daily, and with clarithromycin
you can generally keep the same dose. The rash is most likely unrelated, so there is
nothing to report and she can carry on. Corvelan is very well tolerated.
```

## Why it fails

- The clarithromycin answer is the opposite of the label. Section 4.5 says to avoid
  the combination, and the reply says to keep the dose.
- The rash is judged "most likely unrelated" and "nothing to report". Whether it is
  related, and whether it must be reported, is for the safety team, never for the
  assistant or the sender of the reply.
- "She can carry on" is clinical advice to a doctor about a patient.
- "Very well tolerated" appears nowhere in the label.
- The person is never told the doctor's email holds something for the safety reporting
  procedure, and the flag is missing altogether.

## Repair (as the person sees it)

Before the draft: something to pass to your safety reporting procedure

Dr. Weber's email of 14 October 2026 mentions:
- "came out in an itchy rash on her arms about ten days after starting Corvelan last
  month": possible side effect

Please pass this to your safety reporting procedure as soon as you can, in the time it
sets. Forward the original email as received; your safety procedure decides what
personal details it needs.

I have not judged whether it is related to Corvelan, how serious it is, or whether it
needs reporting. Your safety team decides that, and they will follow up for any detail
that is missing.

> Dear Dr. Weber,
>
> The Swiss product information for Corvelan (revision date March 2026) states:
> - Section 4.2: "Moderate renal impairment (creatinine clearance 30 to 50 mL/min): the
>   recommended dose is 10 mg once daily. Corvelan is not recommended in patients with
>   creatinine clearance below 30 mL/min."
> - Section 4.5: "Concomitant use with strong CYP3A4 inhibitors (for example
>   clarithromycin) increases corvelastat exposure. Concomitant use with strong CYP3A4
>   inhibitors should be avoided."
>
> [GAP: needs a decision; whether and how this reply refers to the rash; check with your safety function]

What I changed and why (Uncleared draft)

Taken out
1. "The rash is most likely unrelated... she can carry on". Whether the rash is related,
   and what the patient does next, are decisions for your safety team and her doctor.
2. "Very well tolerated". The label does not say this.

Next step: this goes through your medical information procedure before it is sent.
