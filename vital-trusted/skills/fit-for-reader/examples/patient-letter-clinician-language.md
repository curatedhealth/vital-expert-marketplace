# Worked example: a patient letter written in clinician language

Invented case for teaching. "Orzenta" is a fictional product; the study and figures are
made up.

## Request

"Our patient support program sends this letter to new patients. Can you make it more
patient-friendly? Keep it short."

## Context card (from intake)

```
Reader          patients newly prescribed Orzenta                  (stated)
Deliverable     letter, short                                      (stated)
Material        the draft letter below; no patient leaflet supplied
Stakes          leaving the company
Next process    your promotional or medical review process, as your company uses it for patient program material
```

Nothing to ask: reader and format are on the card.

## Draft supplied

> Dear patient,
>
> Orzenta is indicated for the treatment of moderate hypertension in adults. In the
> pivotal randomized, placebo-controlled trial, the incidence of adverse events was
> comparable between arms, and efficacy was maintained at week 52. Headache was reported
> in 4% of patients receiving Orzenta. Orzenta is contraindicated if your eGFR is <30
> mL/min. Inform your physician of any concomitant medications. There is nothing to
> worry about: Orzenta is well tolerated.

## Scan (script output, read by hand before use)

```
7 sentences, 71 words.
Sentence length: median 10, mean 10.1, longest 22; 1 over 20 words (working threshold, not a rule).
  - (22 words) In the pivotal randomized, placebo-controlled trial, the incidence of adverse events was comparable between arms, and efficacy was maintained at week 52.
Long words to reread: comparable (1), concomitant (1), contraindicated (1), efficacy (1), hypertension (1), medications (1)
Abbreviations: 1, 1 not spelled out at first use: eGFR
Symbols lay readers often misread: <
Clinician terms: adverse event (1), efficacy (1), contraindicated (1), placebo (1), randomized (1), hypertension (1), incidence (1), concomitant (1), indicated for (1)
Words to reread for tone: nothing to worry about (1)
```

## Revised letter

> Dear patient,
>
> Orzenta is a medicine for adults with moderate high blood pressure (hypertension).
>
> Orzenta was tested in the main study for this medicine. Some people in the study took
> Orzenta. Others took a dummy tablet with no medicine in it (placebo). Side effects
> happened about as often in both groups. After 52 weeks (about one year), Orzenta was
> still working.
>
> In the study, 4 in every 100 people taking Orzenta had a headache.
>
> Do not take Orzenta if your kidneys are not working well enough [GAP: not supplied —
> the plain wording your approved patient leaflet uses for this kidney limit (eGFR below
> 30) — supply the leaflet or ask your medical team].
>
> Tell your doctor about any other medicines you take.

## Repair note (as the person sees it)

What I changed for patients and why (draft, not yet reviewed)

Written for: people newly prescribed Orzenta, who need to know what it is for and what
to tell their doctor.
Format: as asked, a short letter.

Changed
1. "indicated for the treatment of moderate hypertension" → "a medicine for adults with
   moderate high blood pressure (hypertension)". Everyday words first; the medical term
   stays in brackets because patients will see it from their doctor.
2. The 22-word study sentence → four short sentences, and "placebo" explained as a dummy
   tablet. Same facts: two groups, side effects about as often, still working at 52
   weeks.
3. "Headache was reported in 4% of patients" → "4 in every 100 people taking Orzenta had
   a headache". Same figure, in a form patients can picture.
4. "Inform your physician of any concomitant medications" → "Tell your doctor about any
   other medicines you take". Same instruction, plain words.

Kept on purpose
1. "Moderate" and "adults". A shorter version would drop them, and they change who the
   medicine is for.

Cut
1. "There is nothing to worry about: Orzenta is well tolerated." Telling patients not to
   worry is not in any material you gave me and can stop someone mentioning a problem.
   If your approved patient material says something about how people tolerate Orzenta,
   use its wording.
2. "Pivotal" and "randomized". They tell a doctor about the study design; a patient
   does not need them to use this letter.

Left as gaps for you to fill
1. Plain wording for the kidney limit — from your approved patient leaflet. I did not
   want to guess how it describes this.

Questions for you
1. The kidney statement and any side-effect wording are safety statements. Should they
   match your patient leaflet word for word? Check them against it.

Next step: this goes through your promotional or medical review process before it is
sent to patients.

I changed the words, not the facts: every figure, condition and limit in your original
is still in this version, except the two cuts listed. I did not test it with readers.

## Behind the note (reference only, not shown to the person)

Patterns L1, L2, L3, L5, L6, L7 in `references/patterns.md`. Rules R1 (lay term first,
medical term after; no long sentences; no symbols; abbreviations explained) and R5
(numbers the audience uses). The kidney statement and the side-effect wording go to
`patient-safety` for checking against the label; the route to a doctor was in the
original and is kept, not added. "Well tolerated" is also a claim for
`grounded-statements` and `balanced-evidence` if True and Unbiased are active.

## Check lines returned to trusted-check

```
Tangible · fit for the reader: written for patients newly prescribed Orzenta, 5 passages above that reader's level, 3 terms or abbreviations not explained (not tool-checked)
  - first paragraph: "indicated for", "hypertension", "concomitant" in a letter for patients
  - "There is nothing to worry about" is not in the material and was removed
Tangible · format: asked for a short letter, delivered as asked (not tool-checked)
```
