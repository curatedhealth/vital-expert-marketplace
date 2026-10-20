# Output format: decision record check

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/forum_check.py words ANSWER.md`.

## Short mode (default for a direct question)

1. **Answer:** Forum and sitting · pass rule (yours, confirmed; or "proposed, not yet confirmed": no pass or fail given) · pass n of N · the fail that matters most for the forum score.
2. **Per decision:** Item · Decision · Rule · Rank · Decider · Date · Where recorded · Pass or fail · Reason in the rule's words.
3. **Not scorable in A2:** item and why (no rule, no scores in the record).
4. **Rank order and decision:** where a lower-ranked item continued while a higher-ranked item was delayed or stopped: "rank order and decision differ; reason not in the record", beside both, as a question for the forum score.
5. One line offering the full version.
6. **Record:** "Record check draft. The pass rule is yours; each decision reported on its own." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made (after the record line), or "no library call".

## Full mode

### Forum
Forum and sitting as you gave them; product portfolio only.

### Pass rule
The default from the old method (CF-12.01.03.3.2.1), with your changes, as confirmed.

### Decisions
| Item | Decision | Rule | Rank | Decider | Date | Record | Result | Reason |
|---|---|---|---|---|---|---|---|---|

### What the forum score can read
| Item | Scorable | Why not |
|---|---|---|

### Record
Record check draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
