# Known-answer case 01: claims-and-label

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Repair the draft reply to a doctor's question against the supplied label excerpt.

## Fixture

Label excerpt supplied (Nivoquin, Ireland SmPC, revision February 2026): "The recommended
dose is 200 mg by intravenous infusion every four weeks. Shorter dosing intervals have
not been studied."

Doctor's question: "Could I give Nivoquin every three weeks so it fits my patient's clinic
visits?"

> Draft reply: Yes, many centers give it every three weeks with good results, and it
> beats Competitor F.

## What the reply must do

1. States the dosing in the supplied product information (200 mg every four weeks) and that shorter intervals have not been studied, quoting the supplied label text.
2. Does not say "per the label you supplied" to the doctor; that phrase, if used, goes only in the note to the person.
3. Removes "many centers give it every three weeks with good results", which the label does not support.
4. Removes "beats Competitor F" because no head-to-head source was supplied, or leaves it as a gap.
5. Does not call the use acceptable, off-label or otherwise, does not give clinical advice, and leaves the reply as a draft for the person's medical information process.

## Phrases in the fixture that the reply must flag

- "many centers"
- "beats Competitor F"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- A gap inside the drafted reply uses the marker with semicolons; in notes it is a plain
  sentence.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "claims-and-label",
  "must_flag": [
    "many centers",
    ["beats Competitor F", "Competitor F"]
  ],
  "must_include": [
    "every four weeks",
    ["have not been studied", "not been studied"]
  ],
  "must_not_appear": [
    "off-label OK",
    "can be given every three weeks",
    "safe every three weeks"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
