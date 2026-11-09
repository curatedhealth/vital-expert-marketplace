# Known-answer case 01: sourced-claims

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Add the sources to four lines for a formulary committee leaflet.

## Fixture

Sources supplied: a congress abstract, Fictional Headache Congress, 12 June 2026, PRAVE-1:
monthly migraine days fell by 4.1 on Pravella and by 2.6 on placebo at week 12 (no
authors or abstract number sent); a slide from an agency survey, August 2026, online, 60
neurologists: "38% rate Pravella as their preferred new preventive". Nothing on any other
preventive.

> - Headache specialists agree Pravella is the new benchmark.
> - Preferred by most neurologists.
> - Fewer migraine days than any other preventive.
> - Monthly migraine days fell by 4.1 versus 2.6 on placebo.

## What the reply must do

1. Names the PRAVE-1 congress abstract as the source for the migraine-days line, with its figures and week 12 as supplied, and labels it a conference abstract.
2. Shows "Headache specialists agree" and "Fewer migraine days than any other preventive" as needing a source, not as sourced.
3. Says the survey (38% of 60 neurologists, August 2026) cannot carry "preferred by most neurologists".
4. Builds the reference lines from the supplied details only, and says in plain words which details (authors, abstract number, title) are still missing.
5. Invents no author, journal, volume, page or access date, and adds no difference between the two figures.

## Phrases in the fixture that the reply must flag

- "Headache specialists agree"
- "Preferred by most neurologists"
- "than any other preventive"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- A claim without a source in the revised leaflet text may carry the gap marker with
  semicolons; in the note it is a plain sentence.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "sourced-claims",
  "must_flag": [
    ["specialists agree", "Headache specialists"],
    ["Preferred by most", "most neurologists"],
    ["than any other", "any other preventive"]
  ],
  "must_include": [
    "PRAVE-1",
    ["abstract"],
    ["38%", "survey"]
  ],
  "must_not_appear": [
    "et al.",
    "Accessed",
    "N Engl J Med",
    "verified",
    "1.5 days"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
