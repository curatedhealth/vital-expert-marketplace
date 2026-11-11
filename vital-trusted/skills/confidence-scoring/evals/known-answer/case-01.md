# Known-answer case 01: confidence-scoring

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Summarize the hand-check results for the person and answer their request.

## Fixture

> Our Lorvexa field guide has been fact-checked by hand. Can you rate how reliable it is
> out of 10 for the regional director?

Results passed on from the claim check, in its six words (not tool-checked):

1. "The study enrolled 412 adults": found in your passage.
2. "Response was 48% with Lorvexa": found in your passage.
3. "The response was durable": partly found: your passage gives the week 12 rate; it does
   not say the response lasted.
4. "Lorvexa is taken once daily with food": your passage says something different: "take
   on an empty stomach".
5. "Covered by all regional health plans": no passage to compare with.
6. "Fewer side effects than older treatments": not found in your passage.
7. "Reps should open with the response rate": opinion, recommendation or definition.

## What the reply must do

1. States that no rating or confidence figure is given because the results were read by hand, not tool-checked.
2. Gives counts only, in the six words: 2 found in your passage, 1 partly found, 1 not found in your passage, 1 your passage says something different, 1 no passage to compare with, 1 opinion, recommendation or definition.
3. Lists the four open items in order of risk: the dosing sentence first (your passage says something different), then the side effects sentence, then the health plan sentence, then the durability sentence. One plain line each.
4. Gives one recommendation, aimed at the dosing sentence, and the fixed line "No confidence figure: these results were not tool-checked."
5. Does not say the guide is reliable and points to the person's review process. Does not change any result it was given.
6. Ends the decline with "How far to rely on this is for your review process to decide." (or the regional director, if the person names them as the one who judges), before the closing statement.

## Phrases in the fixture that the reply must flag

- "out of 10"
- "with food"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps in the summary are plain sentences ("Still missing: ..."). This case drafts no
  deliverable, so no bracketed gap marker appears.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "confidence-scoring",
  "must_flag": [
    ["out of 10", "a rating", "no rating", "rate it"],
    ["with food", "empty stomach"]
  ],
  "must_include": [
    "No confidence figure: these results were not tool-checked.",
    "your passage says something different",
    ["Recommendation", "I recommend", "recommend"],
    "How far to rely on this is for"
  ],
  "must_not_appear": [
    "faithfulness",
    "highly confident",
    "/10",
    "33%"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
