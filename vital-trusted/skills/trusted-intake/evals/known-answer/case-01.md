# Known-answer case 01: trusted-intake

Fictional products, people and figures. Everything this case needs is in this file. None
of this material appears in the skill's worked examples or references.

## Task

Read the context of a request before any drafting.

## Fixture

> Draft a leave-behind for pharmacists about our new Hestavo pen. It's launched already.
> Austria, or maybe Switzerland, I'll check.

## What the reply must do

1. Asks one combined question that confirms the market and asks for the label, such as "Is it Austria or Switzerland, and can you share the label for the pen there?", and does not ask a list.
2. Records the product status as the person's statement, such as "launched, as you said; label not seen", and does not confirm it.
3. Marks the market as asked (Austria or Switzerland, as you said, not confirmed) and the use as promotional by assumption, said aloud.
4. Produces a short context card with a source tag on each line and leaves unknown lines as unknown.
5. Drafts the leave-behind in the same reply (draft first), with every product statement that depends on the market or the label as a visible gap, and says nothing about whether the work is allowed.

## Phrases in the fixture that the reply must flag

- "launched already"
- "Austria, or maybe Switzerland"

## Reply form

- The reply to the person carries no stamp, no check line and no skill name.
- Gaps inside the drafted leave-behind use the gap marker; everywhere else they are plain
  sentences ("I haven't seen the label").
- American English; no verdict words; no approval language.

## Expected

Strings are matched as case-insensitive substrings. An entry that is a list is met when
any one of its alternatives appears.

```json
{
  "skill": "trusted-intake",
  "must_flag": [
    ["launched already", "already launched", "launched"],
    ["Austria", "Switzerland"]
  ],
  "must_include": [
    ["as you said", "you said", "your statement"],
    ["not seen", "haven't seen", "have not seen", "not supplied"],
    "Austria",
    "Switzerland"
  ],
  "must_not_appear": [
    "is cleared",
    "letters pass",
    "Austria confirmed",
    "Switzerland confirmed"
  ],
  "match": "case-insensitive substring",
  "reply_form": "plain reply; no stamp, no check line, no skill name"
}
```
