# Known-answer case 01: fit-for-reader

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Rewrite a clinician-language text for patients.

## Fixture

> Rewrite this for patients to read.
>
> Ilvantra is a monoclonal antibody indicated for severe eosinophilic asthma. It is
> contraindicated in patients with hypersensitivity to the active substance. Helminth
> infections should be treated before initiation.

## What the reply must do

1. Gives a plain-language version that keeps the three facts: what it is for, who should not take it, and treating worm infections before starting.
2. Replaces "monoclonal antibody", "contraindicated" and "Helminth infections" with everyday words or explains them.
3. Adds no symptoms, side effects or emergency advice that the text does not hold.
4. Shows a gap in the patient version for anything a patient needs that the text lacks, such as how it is given or what to do if unwell.
5. Gives a repair note with counts of passages and terms changed. The note template labels ("Passages changed", "Terms replaced or explained") meet this.

## Phrases in the fixture that the reply must flag

- "monoclonal antibody"
- "contraindicated"
- "Helminth infections"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps in the patient version use the marker with semicolons:
  `[GAP: <class>; <what is missing>; <what would close it>]`. Gaps in the note are plain
  sentences.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "fit-for-reader",
  "must_flag": [
    "monoclonal antibody",
    "contraindicated",
    ["Helminth", "worm"]
  ],
  "gap_marker_expected_in": "drafted deliverable",
  "must_include": [
    "[GAP:",
    ["worm", "parasite"]
  ],
  "must_not_appear": [
    "call 911",
    "go to the emergency room",
    "emergency department"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
