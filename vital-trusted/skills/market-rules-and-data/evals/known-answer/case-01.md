# Known-answer case 01: market-rules-and-data

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Adapt a US letter for a pharmacist in Ireland.

## Fixture

> Adapt this to send to a pharmacist in Ireland.
>
> Dear Ms Halloran, regarding your customer Liam Dorsey (date of birth 4 July 1961):
> Rostavel is FDA-approved for postmenopausal women with osteoporosis. Prescribing
> information is attached. To report side effects call 1-877-310-0142.

## What the reply must do

1. Replaces "FDA-approved" with a gap for the status in Ireland, and does not state approval in Ireland.
2. Leaves placeholders for the elements the person's review process requires (product information for Ireland and its date, side effect reporting route, company contact, reference code), each as a gap.
3. Does not supply a reporting web address or a telephone number from memory, and does not keep the US number as the reporting route.
4. Flags the customer's personal details, does not repeat the name or date of birth, and says in one line that personal details were left out and why it matters.
5. Does not say the letter meets any code; that decision is the person's review process.

## Phrases in the fixture that the reply must flag

- "FDA-approved"
- the customer's name and date of birth (flagged without repeating them)
- "1-877-310-0142"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps inside the drafted letter use the marker with semicolons:
  `[GAP: <class>; <what is missing>; <what would close it>]`. Gaps in the note are plain
  sentences.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears. The identifier entry tests that the details were
flagged, in whatever words, without repeating them.

```json
{
  "skill": "market-rules-and-data",
  "must_flag": [
    "FDA-approved",
    ["date of birth", "personal details", "personal data", "customer's name", "identif"],
    ["1-877-310-0142", "US phone", "US number", "US telephone", "phone number"]
  ],
  "gap_marker_expected_in": "drafted deliverable",
  "must_include": [
    "[GAP:"
  ],
  "must_not_appear": [
    "Liam Dorsey",
    "1961",
    "meets the code",
    "hpra.ie"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
