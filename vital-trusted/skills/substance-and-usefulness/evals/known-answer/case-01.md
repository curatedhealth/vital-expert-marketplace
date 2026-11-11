# Known-answer case 01: substance-and-usefulness

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Make a steering committee update useful, from what was supplied.

## Fixture

> Make this steering committee update more useful.
>
> The registry is progressing nicely. Sites are engaged and data quality is good. We need
> to keep the momentum going and think about next steps.

No enrollment, site, data quality or timeline figures were supplied.

## What the reply must do

1. Replaces each vague phrase with a visible gap instead of a figure.
2. Lists what the person needs to send to close each gap (enrollment, active sites, data quality measure, timeline).
3. Adds no figure of any kind, and no percentage.
4. Names the missing decision and owner for "next steps" as a gap, and offers a "so what" only as a suggestion for the person to confirm.
5. Counts vague statements, filler and sections with no "so what" in plain words. The note template labels ("Vague statements", "Filler passages", "Sections with no "so what"") meet this.

## Phrases in the fixture that the reply must flag

- "progressing nicely"
- "Sites are engaged"
- "data quality is good"
- "keep the momentum going"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps in the revised update use the marker with semicolons:
  `[GAP: <class>; <what is missing>; <what would close it>]`. Gaps in the note are plain
  sentences.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "substance-and-usefulness",
  "must_flag": [
    "progressing nicely",
    ["Sites are engaged", "engaged"],
    ["data quality is good", "data quality"],
    ["keep the momentum", "momentum"]
  ],
  "gap_marker_expected_in": "drafted deliverable",
  "must_include": [
    "[GAP:",
    ["owner", "who decides", "who will"]
  ],
  "must_not_appear": [
    "%",
    "grew",
    "increased by"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
