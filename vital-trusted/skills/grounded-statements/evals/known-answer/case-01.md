# Known-answer case 01: grounded-statements

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Check the figures in a steering committee update against the report supplied, and repair
the draft.

## Fixture

Trial operations report, 31 October 2026: 214 patients enrolled against a target of 300;
38 sites active. The report holds no screen-failure figures and no date for the last
patient enrolled.

> Draft: Enrollment is on track with 255 patients across 40 sites. Screen failures are
> below 10%. The last patient will be enrolled in March.

## What the reply must do

1. Replaces the enrollment sentence with the figures from the report (214 of a target of 300; 38 sites).
2. Leaves the screen-failure figure and the last-patient date visibly missing, with where each would come from.
3. Adds no estimate and no "about" figure, and does not call enrollment on track.
4. Does not calculate a percentage of target, labeled or not, unless the person asks; only then is it given, labeled as calculated from the two figures supplied.
5. Gives counts of figures not in the material and figures changed, in plain words. The note template labels ("Figures not in your material", "Figures changed") meet this.

## Phrases in the fixture that the reply must flag

- "255 patients"
- "40 sites"
- "below 10%"
- "March"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- A missing figure inside the repaired draft uses the gap marker with semicolons; in the
  note it is a plain sentence.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "grounded-statements",
  "must_flag": [
    "255",
    "40 sites",
    ["below 10%", "screen failure", "screen-failure"],
    "March"
  ],
  "must_include": [
    "214",
    "300",
    "38"
  ],
  "must_not_appear": [
    "71%",
    "approximately",
    "all figures are accurate"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
