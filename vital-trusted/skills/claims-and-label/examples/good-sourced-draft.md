# Worked example: a reply to a doctor's question about adolescents

Invented case for teaching. "Tavonis", "TAV-ADOL", the doctor and the figures are
fictional.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: reply to a doctor's own question

Reader          Dr. Meier, a dermatologist                          (stated)
Market          Switzerland                                         (stated)
Product status  approved in Switzerland per your label              (read)
Use             scientific exchange, a reply to a question          (stated)
Deliverable     email reply                                         (stated)
Material        Swiss label excerpt; study report; the doctor's email
Stakes          leaving the company
Next process    your medical information procedure
```

## Request

"Dr. Meier asked on 2 November 2026 whether Tavonis can be used in patients aged 14 to
17. Draft the reply from the label and the study report I attached."

## Material supplied

> **Label excerpt (Swiss product information, revision March 2026, as supplied):** Tavonis is indicated for
> the treatment of moderate to severe atopic dermatitis in adults who are candidates for
> systemic therapy. Safety and efficacy in patients under 18 years have not been
> established.
>
> **Study report (TAV-ADOL, as supplied):** open-label, single-arm study in 32 patients
> aged 12 to 17 with moderate to severe atopic dermatitis, 12 weeks. Clear or almost
> clear skin at week 12: 11 of 32 patients (34%). No comparator group.

## Reply (as the person sees it)

> Subject: Your question about adolescents
>
> Dear Dr. Meier,
>
> Thank you for your question of 2 November 2026 about the use of Tavonis in patients
> aged 14 to 17.
>
> This use is not included in the approved Swiss product information (revision March
> 2026). The approved use is the treatment of moderate to severe atopic
> dermatitis in adults who are candidates for systemic therapy, and safety and efficacy
> in patients under 18 years have not been established. The information below is
> provided in response to your question and is not a recommendation to use Tavonis in
> this way.
>
> **What the available data show.** The TAV-ADOL study was an open-label, single-arm
> study in 32 patients aged 12 to 17 with moderate to severe atopic dermatitis. At week
> 12, 11 of 32 patients (34%) had clear or almost clear skin. The study had no comparator
> group, was small and was open-label, so it cannot show how Tavonis compares with
> other treatment or with no treatment.
>
> **References**
> TAV-ADOL study report, as supplied.
>
> Kind regards,
> [GAP: not supplied; sender name and role; from your medical information team]

## Note to the person (not part of the reply)

Label, promotion and comparisons: what I changed (Uncleared draft)

Working from: the Swiss product information excerpt you supplied (revision March 2026);
for Dr. Meier, as a reply to a question.

"Not included in the approved Swiss product information" is per the label you supplied.

Kept out
1. The efficacy data in the approved adult use. The doctor did not ask about it.
2. Any statement about dose or patient selection for adolescents. Neither the label nor
   the study report gives one, and the reply makes no recommendation.

Left as gaps for you to fill
1. The sender's name and role.

Next step: this goes through your medical information procedure before it is sent.
Whether it can be used is decided there.

I compared the draft with the label you gave me. I did not check that the label is the
current approved version, and none of this was tool-checked.

## Why it is written this way

- The first paragraph of substance says plainly that the use is outside the label,
  using the label's words and its revision date, not TRUSTED's own ruling. "Per the label
  you supplied" goes in the note to the person, who supplied it, not in the reply to the
  doctor, who did not.
- The only data are what the person supplied. The percentage is the study report's own,
  with the count behind it, and the limits are the ones the design shows.
- The reply has no taglines, no adjectives about the product and no call to prescribe.
- The doctor's email mentions no side effect, so no safety flag is needed here.

## Lines returned to trusted-check (not shown to the person)

```
Rule-compliant · label and intended use: 1 statement beyond the label or intended use, label supplied (not tool-checked)
  - the study data on patients aged 12 to 17 are outside the approved adult use; the reply says so before giving them
Rule-compliant · promotion: 0 promotional statements in material meant as scientific exchange (not tool-checked)
```
