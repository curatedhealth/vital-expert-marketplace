# Worked example: payer slide claims with a report and a press release

Invented case for teaching. "Brand A", "ORION-4" and "Competitor B" are fictional.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: payer slide on a registry result

Reader          a payer's medical adviser                           (stated)
Market          not stated                                          (asked)
Use             promotional                                         (assumed)
Deliverable     three bullets for a slide                           (stated)
Material        ORION-4 registry report; company press release
Stakes          leaving the company
Next process    your review process for material sent to payers
```

## Request

"Add the sources to these claims before it goes to the payer."

## Material supplied

> **ORION-4 registry report (internal), data cut-off 30 June 2026:** 1,850 adults.
> Hospital admission: 12.0% on Brand A versus 20.0% on standard care (adjusted hazard
> ratio 0.60, 95% CI 0.48 to 0.75). The excerpt does not give the length of follow-up or
> page numbers.
> **Press release, 14 March 2026:** announces topline ORION-4 results. It gives no rates.
> No study comparing Brand A with Competitor B was supplied.

## Draft supplied

> - Studies show fewer admissions with Brand A (press release, 14 March 2026).
> - Leading treatment in its class.
> - Better outcomes than Competitor B.

## Revised bullets

> - In the ORION-4 registry (1,850 adults; data cut-off 30 June 2026), 12.0% of patients
>   on Brand A were admitted to hospital, versus 20.0% on standard care (adjusted hazard
>   ratio 0.60, 95% CI 0.48 to 0.75). [GAP: not supplied; length of follow-up for the admission figures; from the registry report]
> - The company announced topline ORION-4 results on 14 March 2026.
> - Comparison with Competitor B: [GAP: not supplied; a study that compares Brand A with Competitor B; supply it or remove the comparison]

## Note to the person

Sources: what I changed and what is still needed (Uncleared draft)

Sources you gave me: ORION-4 registry report (internal), data cut-off 30 June 2026;
company press release, 14 March 2026.

Changed
1. "Studies show fewer admissions (press release)" → the registry named, with its two
   admission rates. "Studies show" needs the study named, and the press release gives no
   rates.
2. "Leading treatment in its class" → removed. No source was supplied for a ranking.

Claims that still need a source
1. "Better outcomes than Competitor B" needs a study that compares the two, for a payer
   reader. Your medical information team may hold one.

Sources that cannot carry their claim for this reader
1. The press release announces the results and gives no rates, so it can support the
   date of the announcement and nothing more.

Question for you
Which market is this for, and can the internal ORION-4 registry report be provided to
the payer on request? Your review process decides the second part; until then the rates
rest on a report the payer cannot see.

Next step: this goes through your review process for material sent to payers before it
is used.

I did not write any reference from memory. No source was tool-checked.

References (built from the sources you supplied; not tool-checked)

1. ORION-4 registry report. Internal report. Data cut-off 30 June 2026. Used for: the
   admission rates and the hazard ratio.
2. Company press release announcing topline ORION-4 results, 14 March 2026. Used for:
   the date of the announcement.

Missing details
- Reference 1: the authors, the report title and the table or page for the figures are
  not in what you sent; please add them from the full report.

Claims with no reference yet
- "Better outcomes than Competitor B" needs a study that compares the two.

## Why it is written this way

- Every detail in the bullets comes from the excerpt. No time window, page number or
  market was added; each is a gap or a question.
- The press release is used for the one thing it can carry. Why the rates come from the
  registry report is said in the note, not on the slide.
- The registry report is internal, so whether it can be provided to the payer is asked,
  not assumed.
- The references list only what the person supplied.

## Lines returned to trusted-check (not shown to the person)

```
True · sources: 3 claims that need a source, 1 with a source you supplied, 0 with a source named but not supplied, 2 with no source (not tool-checked)
True · kind of source: 1 claim resting on a source that cannot carry it for this reader (not tool-checked)
  - the admissions statement cited only a press release, which gives no rates
True · citations: 1 reference looked at, 1 missing details a reviewer needs, 0 guidance or "current" statements with no title or date (not tool-checked)
  - the press release citation in the draft has no title or issuing company
```
