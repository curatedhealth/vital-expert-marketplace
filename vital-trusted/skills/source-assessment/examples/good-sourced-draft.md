# Worked example: two sources behind one payer slide

Invented case for teaching. "Velostra", the NORLA registry and Example Pharma are
fictional.

This run is by hand. No source was looked up, no score was computed and no currency
check was run.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: payer slide on admissions

Reader          a payer's medical adviser                           (stated)
Use             promotional                                         (assumed)
Material        citation details and an abstract, as supplied
Stakes          leaving the company
Next process    your promotional review process
```

## Request

"Are these two sources fine for the payer slide?"

## What was supplied

> 1. "Outcomes after Velostra in NORLA", Example Cardiology Journal, 2023. Only the
>    abstract was sent. It describes an observational registry analysis and states that
>    the registry was funded by Example Pharma. Authors and identifiers were not sent.
> 2. Example Pharma press release, 1 March 2024, headline "40% fewer admissions". No
>    rates were sent.

## Reply (as the person sees it)

I can't tell you whether they are good enough; your review process decides that. Here is what each can and cannot carry for a payer reader, so you can decide where
to use them.

Source: "Outcomes after Velostra in NORLA", Example Cardiology Journal, 2023 (full date not shown)
Identifier: none supplied

Kind: a journal article, from the abstract only
Peer review: status not confirmed; the abstract does not say, and the journal's own page would
Funders and interests: funded by Example Pharma, as the abstract states; authors not supplied, so their interests are not stated
Fit to your question: it concerns Velostra admissions in an observational registry; whether
the population matches your market is not shown in the abstract

How strong: one observational registry analysis; one study
Date: 2023, full date not shown
Currency: not checked. The check you can do: the journal's page for the article and a retraction database

Can carry for a payer: that, in this registry analysis, admissions were reported
for Velostra, with the rates once you have the full article
Cannot carry: that Velostra caused fewer admissions, or any claim about a market
the abstract does not name

To use it: the full article, for the event rates and the population
Next step: this goes through your market access or promotional review and your medical
review, as your process names it, before it is used.

Not tool-checked: I read what you supplied. Currency and retraction checks are yours to make.

Source: Example Pharma press release, 1 March 2024, headline "40% fewer admissions"
Identifier: none supplied

Kind: a company press release
Peer review: not peer reviewed
Funders and interests: made by Example Pharma, the maker of the product
Fit to your question: it gives a headline and no rates, population or design

How strong: not stated; no study design is given
Date: 1 March 2024
Currency: not checked. The check you can do: the company's page for a corrected or replaced release

Can carry for a payer: that the company announced the result on 1 March 2024
Cannot carry: the admissions claim itself, which needs the study behind the
headline

To use it: cite the article, not the release, for the figures
Next step: this goes through your market access or promotional review and your medical
review, as your process names it, before it is used.

Not tool-checked.

This check flags issues. It is not medical, legal, regulatory or ethics review.

## Why it is written this way

- Each source has its own card with what it can and cannot carry. No source is graded
  and no score is shown, because no tool ran.
- The article's peer review status is not assumed from the word "journal". It is shown
  as not confirmed, with what would confirm it.
- Dates are written in full, or marked "full date not shown".
- The press release is kept to the one thing it can carry.
- Payer material names both reviews: market access or promotional, and medical.
- The cards are given as a check, so the closing statement is the last line.

## Lines returned to trusted-check (not shown to the person)

```
True · sources: 2 looked at, 2 not peer reviewed or status not confirmed, 2 made or paid for by an interested party, 1 do not fit the question or reader (not tool-checked)
True · strength and currency: 0 single studies carrying a general claim, 0 retracted or corrected, 1 may be replaced or undated, 2 currency not checked (not tool-checked)
```
