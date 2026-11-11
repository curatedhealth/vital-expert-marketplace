# Known-answer case 01: trusted-check

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Run the TRUSTED check on a leaflet for a hospital pharmacy committee.

## Fixture

Context given by the person: the reader is a hospital pharmacy committee in Belgium; the
leaflet leaves the company; no label and no sources were supplied.

> Fendralix: the only kidney therapy proven to delay dialysis by five years. Recommended
> by leading nephrologists. Order through your usual wholesaler.

## What the reply must do

1. Gives the summary with a row for each letter, counts in plain words, and what to fix and what is missing.
2. Treats the label check as not possible because no label was supplied, and says what would close it.
3. Flags the "only" claim, the five-year figure and the unnamed recommendation as having no source supplied.
4. Says the hand comparison of claims with sources could not be made because no sources were supplied, and names what it would compare. It shows no hand-check counts and no confidence figure.
5. Gives no pass, no overall verdict and no clearance; the status is "Uncleared draft"; ends with the closing statement.

## Phrases in the fixture that the reply must flag

- "the only kidney therapy"
- "delay dialysis by five years"
- "Recommended by leading nephrologists"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps appear in plain sentences ("no sources were supplied; a hand check would compare
  the five-year figure with them"), never as gap markers.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears. Must-not entries avoid bare words such as "pass",
which would also match "passage" or "pass it to".

```json
{
  "skill": "trusted-check",
  "must_flag": [
    ["the only kidney therapy", "only kidney therapy", "\"only\""],
    ["delay dialysis by five years", "five years"],
    ["leading nephrologists", "Recommended by"]
  ],
  "must_include": [
    ["Could not be checked", "could not check"],
    ["no sources were supplied", "no sources supplied", "no source was supplied"],
    "Uncleared draft"
  ],
  "must_not_appear": [
    "Result: pass",
    "all letters pass",
    "cleared for external use",
    "is ready to send",
    "[GAP:",
    "found in your passage",
    "No confidence figure"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
