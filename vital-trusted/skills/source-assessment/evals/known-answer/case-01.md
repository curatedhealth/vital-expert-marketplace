# Known-answer case 01: source-assessment

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Say what each source can and cannot carry for the use the person names.

## Fixture

> Can I use these two for the nurse training module?
> 1. "Ilvantra in community practice", a registry report by Fictional Health Analytics
>    GmbH, commissioned by the maker of Ilvantra, dated March 2026. 820 patients; no
>    comparison group. The report does not say whether it was peer reviewed.
> 2. A patient forum thread, "Ilvantra stories", 14 posts, last post 30 September 2026.
>    One post says "most of us stopped needing steroid tablets".

## What the reply must do

1. Gives one card per source with what it can carry and what it cannot.
2. Says the registry report was commissioned by the maker, has no comparison group and that its peer review status is not confirmed.
3. Says the forum thread holds individual accounts that cannot be checked, and that it cannot carry "most patients stop steroid tablets" or any treatment effect.
4. Gives no score, tier or grade, says retraction and currency were not checked, and writes dates in full ("30 September 2026"; the report shows only a month, so "day not shown").
5. Points to the review process for training material.

## Phrases in the fixture that the reply must flag

- "commissioned by the maker of Ilvantra"
- "most of us stopped needing steroid tablets"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps in notes and cards are plain sentences ("Still missing: ..."). This case drafts no
  deliverable, so no bracketed gap marker appears.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings, so "Cannot carry:" in a card meets
"cannot carry". An entry that is a list is met when any one of its alternatives appears.

```json
{
  "skill": "source-assessment",
  "must_flag": [
    ["commissioned", "maker of Ilvantra", "paid for by the maker"],
    ["most of us", "steroid tablets"]
  ],
  "must_include": [
    "not tool-checked",
    ["cannot carry", "can't carry"],
    "not checked",
    ["comparison group", "no comparator"]
  ],
  "must_not_appear": [
    "out of 100",
    "gold tier",
    "silver tier",
    "high-quality source"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
