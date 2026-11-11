# Worked example: references and a record for a payer slide, built by hand

Invented case for teaching. "Velostra", the NORLA registry and Example Pharma are
fictional.

This run is by hand. Nothing was looked up, and no reference was built by a tool.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: payer slide on admissions

Reader          a payer's medical adviser                           (stated)
Use             promotional                                         (assumed)
Material        two sources, as supplied below
Stakes          leaving the company
Next process    your promotional review process
```

## Request

"Build the references and a record for the Velostra admissions slide."

## What was supplied

> 1. "Outcomes after Velostra in NORLA", Example Cardiology Journal, 2023. Authors,
>    volume, pages and identifier were not sent.
> 2. Example Pharma press release, 1 March 2024, headline "40% fewer admissions". No
>    link or document number was sent.
>
> **Slide text as received:** "Velostra cut admissions by 40%." The journal abstract gives
> 12.0% on Velostra and 20.0% on standard care, with an adjusted hazard ratio of 0.60.

## Reply (as the person sees it)

Uncleared draft (to be cleared by a reviewer not named yet)

What this covers: the Velostra admissions slide for a payer meeting
Sources: 2, in the reference list
Factual claims compared with their passages by hand: 1 (not tool-checked; counts only)
  0 found in your passage
  1 partly found
  0 not found in your passage
  0 your passage says something different
  0 no passage to compare with
Listed separately, not in the total: 0 opinion, recommendation or definition
Found in your passage means the passage says it. It does not mean the claim is true in the
world.

Decisions
None yet. You have not made a decision on any item below.

Still open (no decision yet)
1. "Velostra cut admissions by 40%": partly found, 40% not in your passage. The abstract
   gives 12.0% on Velostra and 20.0% on standard care, with an adjusted hazard ratio of
   0.60. Do you want the sentence to give those figures instead, or to remove it?
2. "40% fewer admissions" (press release): a company headline with no rates; goes to your
   promotional review process.
3. Whether a newer version of the 2023 article exists: not checked; goes to the document's
   owner.

Next step: this record goes with the work into your promotional review process. It does
not replace it.

Record note written by hand; not tool-checked.

References

1. Outcomes after Velostra in NORLA. Example Cardiology Journal. 2023.
2. 40% fewer admissions. Press release. Example Pharma. 1 March 2024.

Source 1 has no authors, volume, pages or identifier in what you gave me; I left them out.
Add them from the full article if you have it.
Source 2 has no link or document number in what you gave me; I left it out. Add it from
the company's own file if you have it.

Reference lines built from the details you gave; not tool-checked.

## Why it is written this way

- The status is "Uncleared draft", with the placeholder saying no reviewer is named yet. No
  clearer was invented, and no word such as approved appears.
- The record lists no decision, because the person made none. The rewrite of the 40%
  sentence is offered as a question under "Still open", not recorded as done.
- The 40% is partly found: the abstract gives the two rates, and a figure worked out from
  them is not in the passage. No figure was calculated for the person.
- The reference lines hold only what the person gave, in the order
  `scripts/plain_reference.py` prints. No author, volume, page, access date or "used for"
  text was added, and each missing detail is a plain sentence after the list.
- The counts describe the text as it arrived, and they are in plain words with "not
  tool-checked".

## Lines returned to trusted-check (not shown to the person)

```
True · references: 2 sources, 2 reference lines, 2 with a missing detail (not tool-checked)
Defensible · formal record: 2 sources, 3 open items, 1 handed on to a review process; Uncleared draft (not tool-checked)
```
