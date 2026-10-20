# Output format: launch review and miss owners

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** N of M measures met your rules; the stops; misses without an owner.
2. **Misses:** table Measure · Value vs your rule · Next-step kind (briefing, claim fix, stopped claim, customer side) · Owner (yours, or "owner not named").
3. **Stops:** one line per owner, with rows.
4. **Hypotheses:** at most one per miss, labeled, with the record that would confirm it.
5. **Record:** "Launch review draft. Rules, owners and decisions are yours. Misses stay open until their owner closes them." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### Results against your rules
| Measure | Value | Your rule | Result |
|---|---|---|---|

### Misses, owners and next steps
| Miss | Kind | Owner (yours) | Next step (proposed) | Forum (yours) | Open |
|---|---|---|---|---|---|

### Hypotheses (labeled)
| Miss | Hypothesis | Record that would confirm or rule it out |
|---|---|---|

### Stops for the accountable owner
| Item | Owner | Rows |
|---|---|---|

### Repairs
Ranked only on your scores (tool, your numbers, result), otherwise listed as proposed in dependency order.

### Gaps

### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
