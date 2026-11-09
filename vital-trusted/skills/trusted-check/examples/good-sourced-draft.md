# Worked example: a follow-up email to a payer's medical adviser

Invented case for teaching. "Velunor" is a fictional product; the registry, figures and
people are made up.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: follow-up email to a payer's medical adviser

Reader          a payer's medical adviser, Dr. Brandt                (stated)
Market          Germany                                              (stated)
Product status  approved in Germany, as you said; label not supplied (stated)
Use             promotional                                          (assumed)
Deliverable     short email                                          (stated)
Material        registry summary
Stakes          leaving the company
Next process    the review process your company uses for material sent to payers
```

## Request

"Is this OK to send to Dr. Brandt? Please check it."

## Material supplied

> (Registry summary) Observational registry, 1,850 patients. Hospital admission within
> 12 months: 12.0% on Velunor versus 20.0% on standard care. Adjusted hazard ratio 0.60
> (95% CI 0.48 to 0.75). No cost analysis done.

## Draft supplied

> Dear Dr. Brandt, thank you for your time. In a registry of 1,850 patients, Velunor
> cuts hospital admissions by 40% and is the leading therapy for this group. These
> savings will free budget for your other plans. We would welcome a listing decision
> this quarter. Kind regards.

## Summary (as the person sees it)

TRUSTED check: follow-up email, for a payer's medical adviser. Uncleared draft.

Before it goes, fix these 4 things and supply 1 missing item. Your review process for
material sent to payers decides whether it can be used.

Tangible        nothing flagged in what was checked
Rule-compliant  1 to fix. 1 missing
                - "the leading therapy" ranks Velunor above other treatments, and your registry summary compares nothing with another named product
                - no approved label was supplied, so statements about use could not be compared with it
Unbiased        1 to fix
                - only the percentage drop is given; your summary also has the admission rates, 12.0% and 20.0%
Safe            nothing flagged in what was checked
True            2 to fix
                - "cuts" says the medicine caused the drop; the summary describes an observational registry
                - "these savings" refers to cost savings, and no cost analysis was done
                Compared by hand with your sources (not tool-checked): 4 factual claims: 1 found in your passage, 1 partly found, 2 not found in your passage, 0 your passage says something different, 0 no passage to compare with.
                Listed separately, not in the total: 1 opinion, recommendation or definition.
                No confidence figure: these results were not tool-checked. Found in your passage means the passage says it, not that the statement is true.
Ethical         nothing flagged in what was checked
Defensible      record: 2 materials, 1 assumption, 4 open items (4 without an owner); Uncleared draft
                Formal record written by hand: 1 source, 4 open items, 1 handed on to a review process; Uncleared draft (not tool-checked)

Open for a person
1. Whether any statement about Velunor's standing against other treatments can be kept.
   Your review process for material sent to payers decides. (Not found in your passage.)
2. Whether a cost statement can be made at all, since no cost analysis exists yet. (Not
   found in your passage.)
3. "Cuts hospital admissions by 40%": partly found. Your summary gives 12.0% and 20.0%;
   the 40% figure is not in it. You decide whether to state the two rates instead.

Could not be checked
- Statements about use: no approved label was supplied.

Next step: this goes through your review process for material sent to payers before it
is used.

This check flags issues. It is not medical, legal, regulatory or ethics review.

## Why it is written this way

- Full depth, because the reader is outside the company (TR-H12).
- "Is it OK to send" got what to fix and who decides, not yes or no (TR-H5, TR-H11).
- Each finding is counted once, in one row, and the header equals the sums of the rows:
  4 to fix ("the leading therapy" under Rule-compliant, the percentage drop with no rates
  under Unbiased, "cuts" and "these savings" under True) and 1 missing (the label, under
  Rule-compliant). The second sentence of the draft carries three of the four findings;
  each is its own thing to fix. Recounted before sending.
- Letters read in plain words. There are no verdict words, no figure for how well the
  claims held up, no skill names and no raw gap syntax.
- A source was supplied, so the claims were compared by hand at full depth. The five
  sentences that make a statement are counted once each: the registry size is found;
  the 40% is partly found (a worked-out figure is not in the passage); "the leading
  therapy" and "these savings" are not found; the listing request is a recommendation.
  The fixed line follows the counts, and there is no figure for how well the claims
  held up.
- The open items are counted as the 3 items for a person plus the 1 check that could
  not run, so the Defensible row says 4. The record says "Uncleared draft" because no
  reviewer was named.
- Nothing was added to the draft and no new figure was introduced; the two admission
  rates come from the person's own summary.

## Lines received by trusted-check (not shown to the person)

```
Tangible · substance: 0 statements too vague to act on, 0 passages of filler or repetition, 0 sections with no "so what" (not tool-checked)
Rule-compliant · label and intended use: not checked, label not supplied (2 product statements affected)
Rule-compliant · comparisons: 1 comparative or superiority claim, 1 without a head-to-head source (not tool-checked)
Unbiased · framing: 1 relative figure with no absolute rates beside it (not tool-checked)
Safe · safety statements: 0 statements on dosing, warnings, interactions or special populations, 0 not as the label states them, label not supplied (not tool-checked)
True · invented details: 1 cost claim not in your material, 1 causal word the material does not support (not tool-checked)
True · sources: 1 looked at, 1 not peer reviewed or status not confirmed, 0 made or paid for by an interested party, 0 do not fit the question or reader (not tool-checked)
True · claims compared by hand: 4 factual claims; 1 found in your passage, 1 partly found, 2 not found in your passage, 0 your passage says something different, 0 no passage to compare with; listed separately, not in the total: 1 opinion, recommendation or definition (not tool-checked)
True · open items: 4 factual claims; 1 found in your passage, 1 partly found, 2 not found in your passage, 0 your passage says something different, 0 no passage to compare with; listed separately: 1 opinion, recommendation or definition; 3 open items (not tool-checked)
True · No confidence figure: these results were not tool-checked.
Ethical · human review: stakes leaving the company, reviewer not named, 0 requests to send without review (not tool-checked)
Defensible · record: 2 materials, 1 assumption, 4 open items (4 without an owner); Uncleared draft (not tool-checked)
Defensible · formal record: 1 source, 4 open items, 1 handed on to a review process; Uncleared draft (not tool-checked)
```
