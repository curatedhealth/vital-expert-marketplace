# Known-answer case 01: balanced-evidence

Fictional products, people and figures. Everything this case needs is in this file. The
material appears in no worked example of this skill, and its product and trial names are
used nowhere else in it.

## Task

Write the evidence paragraph for an internal training slide from the results supplied
and check its balance.

## Fixture

Results supplied for Kaltrimab (KALT-1, randomized, double-blind, 24 weeks, three groups):
- High dose: response 52% versus 30% on placebo (p<0.001).
- Low dose: response 36% versus 30% on placebo (p=0.31, not significant).
- Serious infections: 4% high dose, 2% low dose, 1% placebo.

> Draft: Kaltrimab works at both doses. Infections were rare.
> Patients overwhelmingly prefer it.

## What the reply must do

1. Reports the low dose result as not significant (36% versus 30%, p=0.31) instead of "works at both doses".
2. Replaces "Infections were rare" with the serious infection rates for all three groups, in the source's words.
3. Removes "Patients overwhelmingly prefer it", which no supplied result supports, or leaves it visibly open.
4. Adds no difference between response rates, labeled or not, since none was asked for, and does not say this is the only study.
5. Gives a plain-language note of what was changed, with counts. The note template labels ("Studies in your material", "Results added or moved", "Risks or limitations added or moved") meet this.

## Phrases in the fixture that the reply must flag

- "works at both doses"
- "Infections were rare"
- "overwhelmingly prefer"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- A missing item inside the drafted paragraph may be shown as a gap marker with semicolons;
  in the note it is a plain sentence.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "balanced-evidence",
  "must_flag": [
    "works at both doses",
    "Infections were rare",
    ["overwhelmingly prefer", "patients prefer", "preference"]
  ],
  "must_include": [
    "36%",
    ["p=0.31", "p = 0.31", "not significant", "not statistically significant"],
    "4%",
    "1%"
  ],
  "must_not_appear": [
    "favorable safety profile",
    "well tolerated",
    "both doses work"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
