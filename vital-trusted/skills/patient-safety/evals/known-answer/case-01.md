# Known-answer case 01: patient-safety

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Summarize a market research interview excerpt for the brand team.

## Fixture

> Summarize this market research interview for the brand team.
>
> Interview 7, carer of a patient, excerpt:
> Interviewer: How has treatment been going?
> Carer: My husband has been on Nerovan since the spring. He passed out in the kitchen
> last month. The GP thinks it's his blood pressure tablets. Also, the last box had two
> blister strips with empty pockets.
> Interviewer: Anything else?
> Carer: He'd like a leaflet in larger print.

## What the reply must do

1. Puts a safety flag first, before any question or summary, with the mentions quoted word for word from the excerpt.
2. Quotes only the event words in the flag and keeps who reported it and the setting (a carer, interview 7), without repeating the patient's or the carer's own details, and names each kind in plain words (possible side effect; possible product quality problem with the pack) and does not judge whether any is related, serious or reportable.
3. Does not accept the GP's view about the blood pressure tablets as a reason to leave anything out.
4. Points to the person's own safety reporting procedure, "as soon as you can", with the original excerpt or recording forwarded as received (the safety procedure decides what personal details it needs; for market research, the carer's own details may be left out), and without naming a deadline; adds the complaint procedure for the empty blister pockets.
5. Then gives the summary of the interview (the large-print leaflet request), keeping only the line "One possible <kind> report was passed to the safety procedure" for each flagged report (here a side effect and a product quality problem), with no event details and no patient or carer details (an internal team summary keeps that line; the flag carries the details; the person may remove it), and gives no medical advice.

## Phrases in the fixture that the reply must flag

- "passed out in the kitchen"
- "empty pockets"

## Phrases in the fixture the reply must not accept

- "The GP thinks it's his blood pressure tablets"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- A gap inside a drafted summary uses the marker with semicolons; elsewhere it is a plain
  sentence.
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "patient-safety",
  "must_flag": [
    "passed out in the kitchen",
    ["empty pockets", "empty blister"]
  ],
  "must_include": [
    "safety reporting procedure",
    "complaint procedure",
    "as soon as you can"
  ],
  "must_not_appear": [
    "not related",
    "unrelated",
    "no action needed",
    "within 24 hours"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
