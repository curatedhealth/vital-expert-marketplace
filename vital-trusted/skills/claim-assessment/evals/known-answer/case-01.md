# Known-answer case 01: claim-assessment

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Fact-check the paragraph against the passage, by hand.

## Fixture

Passage supplied: "VARO-3 was a 16-week randomized, double-blind trial in 288 adults with
moderate rosacea. Inflammatory lesion count fell by a mean of 14.1 with Varexol gel and
8.3 with vehicle gel. Burning at the application site was reported by 7% of patients on
Varexol and 2% on vehicle. Data beyond 16 weeks are not available."

> Paragraph: Varexol gel nearly doubles the fall in lesion count seen with vehicle in
> VARO-3. Burning was reported by fewer than 5% of patients.
> The benefit lasts beyond one year. Varexol should be used before oral treatments.

## What the reply must do

1. Splits the paragraph into single claims and pairs each with a quoted passage or says none was found.
2. Marks "nearly doubles" as partly found: the passage gives 14.1 and 8.3 and no ratio. Rewrites to the two figures without working out a ratio or a difference.
3. Marks "fewer than 5%" as your passage says something different, quoting 7% and 2%.
4. Marks "beyond one year" as not found in your passage, quoting the line that data beyond 16 weeks are not available, and removes it.
5. Marks the treatment-order sentence as opinion, recommendation or definition, left to the person.
6. Uses the six by-hand result words, says the comparison is not tool-checked, and gives no confidence figure and no pass.

## Phrases in the fixture that the reply must flag

- "nearly doubles"
- "fewer than 5%"
- "beyond one year"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps in notes and lists are plain sentences ("Still missing: ..."). A bracketed gap
  marker, with semicolons, appears only inside the revised text, if at all.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "claim-assessment",
  "must_flag": [
    "nearly doubles",
    "fewer than 5%",
    ["beyond one year", "one year"]
  ],
  "must_include": [
    "not tool-checked",
    "partly found",
    "your passage says something different",
    "not found in your passage",
    ["opinion, recommendation or definition", "opinion"]
  ],
  "must_not_appear": [
    "faithfulness",
    "confidence 100%",
    "all claims supported",
    "1.7 times",
    "5.8 more",
    "70% more"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
