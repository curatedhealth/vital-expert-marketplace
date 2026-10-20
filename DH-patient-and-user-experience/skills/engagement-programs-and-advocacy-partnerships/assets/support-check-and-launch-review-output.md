# Output format: support check and launch review

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line: who clears it, and that the record is built with `verify.build_record` once a named person clears it; otherwise "uncleared draft".

## Short mode (default for a direct question)

1. **Answer:** which support items stop for your compliance owner, and the elements in tension or not stated for each. Then the launch rules missed, if you set rules.
2. **Elements (compact):** Item · Element · As you state it (met, not stated, in tension) · Row. At most eight rows; the cap line always shown: "2026 cap $623 per patient per calendar year, OIG figure (CP-US-27); one element, not protection."
3. **Ranking of your scores (if scored):** order, values, the smallest weight change that swaps the top two.
4. **Stop:** "Support to patients or patient groups stops for [owner as named, or owner not named]. This draft does not say the arrangement is protected."
5. **Record:** "Support check draft. Values, rules, scores and the decision are yours. Clears: [person or role as you named them, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft."
6. One line offering the full version.

## Full mode

### Answer

### Support as you describe it
| Item | Recipient | Value per patient per calendar year (yours) | Cash or equivalent | Recommended by a licensed professional | Eligibility | Advertised | Duration |
|---|---|---|---|---|---|---|---|

### US elements
| Item | Element (hh-1 to hh-8, CMP exception, AKS) | As you state it | Row |
|---|---|---|---|

### Pattern OIG weighed (AO 19-02, binds only its requestor)

### Other markets
| Market | Rule | Your plan | Row |
|---|---|---|---|

### Your scores and the ranking (analytics.mcda on your scores)
| Rank | Option | Value (0 to 100) | Largest contribution |
|---|---|---|---|

### Robustness
| Pair | Criterion | Your weight | Weight at which they swap |
|---|---|---|---|

### Launch review against your rules
| Rule (yours) | Evidence (A1, A2) | Met or missed | Owner of a miss (yours) |
|---|---|---|---|

### Stops for the owner

### Gaps

### Calls made

### Record
Support check draft. Elements laid out for the compliance owner; no arrangement is called protected. The ranking reflects your scores; it is not a recommendation. AI-assisted. Clears: NAME (as you named them, or "owner not named"). The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
