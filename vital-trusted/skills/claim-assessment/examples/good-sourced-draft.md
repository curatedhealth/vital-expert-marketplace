# Worked example: one sentence taken apart against a registry passage

Invented case for teaching. "Velostra" and the NORLA registry are fictional; the figures
are made up.

This run is by hand. No tool result is shown, and no support word comes from a tool.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: payer deck sentence

Reader          a payer's medical adviser                           (stated)
Market          Germany                                             (stated)
Use             promotional                                         (assumed)
Material        one registry passage
Stakes          leaving the company
Next process    your promotional review process
```

## Request

"Fact-check this sentence against the registry passage."

> **Sentence:** In NORLA, Velostra cut heart failure admissions by 40% in 1,850 patients.
>
> **Passage supplied:** "NORLA is an observational registry of 1,850 adults with heart
> failure. Hospital admission for heart failure within 12 months occurred in 12.0% of
> patients on Velostra and 20.0% of patients on standard care (adjusted hazard ratio
> 0.60, 95% CI 0.48 to 0.75)."

## Parts of the sentence, one claim each

| # | Part | Against the passage |
|---|---|---|
| 1 | "1,850 patients" | found: "1,850 adults" |
| 2 | "heart failure admissions" | found: "admission for heart failure within 12 months" |
| 3 | "by 40%" | partly found: 40% not in your passage. The passage gives 12.0% and 20.0%; a figure worked out from them is not in the passage |
| 4 | "cut" | partly found: the passage describes an observational registry, so it shows a difference, not that Velostra caused it |

## Result (as the person sees it)

Fact-check against the passages you supplied (draft, for your review)

Not tool-checked: I compared each part of the sentence with your passage by hand.
Checked against: the NORLA registry passage (supplied).

What a match means: the passage you gave says the same thing as the sentence. It does
not mean the sentence is true, that the source is good, or that the work is ready.

4 factual claims: 2 found in your passage, 2 partly found, 0 not found in your passage,
0 your passage says something different, 0 no passage to compare with.
Listed separately, not in the total: 0 opinion, recommendation or definition.

Found in your passage: keep (2)
1. "1,850 patients" with "1,850 adults with heart failure" (registry passage)
2. "heart failure admissions" with "admission for heart failure within 12 months"
   (registry passage)

Partly found: rewrite to match (2)
1. "by 40%" → "12.0% of patients on Velostra and 20.0% on standard care". Partly found:
   40% not in your passage. Your passage gives the two rates; it does not give a 40%
   figure. Rewritten, not tool-checked.
2. "cut" → "were admitted". Partly found: cause not in your passage. Your passage
   describes an observational registry; it does not say Velostra caused the difference.
   Rewritten, not tool-checked.

Not found in your passage: removed or rewritten (0)

No passage to compare with: open, not removed (0)

Your passage says something different: ask you (0)

Opinion, recommendation or definition: for your judgment (0)

Revised text
> In the NORLA observational registry (1,850 adults), hospital admission for heart failure
> within 12 months occurred in 12.0% of patients on Velostra and 20.0% on standard care
> (adjusted hazard ratio 0.60, 95% CI 0.48 to 0.75).

Next: source quality, the open items and the record can be added, and this goes through
your market access or promotional review and your medical review, as your process names
it, before use.

This check flags issues. It is not medical, legal, regulatory or ethics review.

## Why it is written this way

- The 40% was not calculated for the person. Working it out from the two rates would put
  a figure in the text that the passage does not hold. A figure that could be worked out
  from the passage's numbers is "partly found", as `../references/statuses.md` says: the
  two rates are quoted, and the 40% is named as missing.
- Each part has one claim and one passage, so the result can say which part holds.
- Only the manual result words appear. No claim is marked as checked by a tool.
- No figure for confidence is given; none can be given from a by-hand comparison.

## Lines returned to trusted-check (not shown to the person)

```
True · claims compared by hand: 4 factual claims; 2 found in your passage, 2 partly found, 0 not found in your passage, 0 your passage says something different, 0 no passage to compare with; listed separately: 0 opinion, recommendation or definition (not tool-checked)
```
