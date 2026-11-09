# Known-answer case 01: honest-framing

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Check how three slides frame one trial result, and repair them.

## Fixture

Data supplied for PRUNE-2: an open-label trial; remission 34% on Prunelix versus 29% on the
comparator; the difference was not statistically significant (p=0.21). Funded by the
maker of Prunelix.

> Slide 2: PRUNE-2 delivers a dramatic remission benefit.
> Slide 3: Bar chart of the two remission rates, vertical axis running from 25% to 35%.
> Slide 4: A blinded, independent trial.

## What the reply must do

1. Replaces "dramatic remission benefit" with wording that fits a result that was not statistically significant, giving both rates.
2. Flags that a bar chart's vertical axis starting at 25% exaggerates the gap, and says the bars start at zero, with 34% and 29% printed on them.
3. Flags "blinded" (the trial was open-label) and "independent" (the maker funded it), and offers a design and funding line.
4. Adds no difference in points, labeled or not, unless the person asks for one; only then is it given, labeled as calculated from the two figures supplied.
5. Gives counts of strong words, chart issues and framing questions. The note template labels ("Strong words changed", "Chart issues", "Framing questions for you") meet this.

## Phrases in the fixture that the reply must flag

- "dramatic"
- "25% to 35%"
- "blinded"
- "independent"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Anything missing is said in plain words, with what would close it.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears. No must-not entry occurs in the fixture, so quoting
the original slides cannot trip it.

```json
{
  "skill": "honest-framing",
  "must_flag": [
    "dramatic",
    ["25%", "axis"],
    "blinded",
    "independent"
  ],
  "must_include": [
    "34%",
    "29%",
    ["open-label", "open label"],
    ["p=0.21", "p = 0.21", "not statistically significant"]
  ],
  "must_not_appear": [
    "1.2 times",
    "17% higher",
    "double-blind"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
