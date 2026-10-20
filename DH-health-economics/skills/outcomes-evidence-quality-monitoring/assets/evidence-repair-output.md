# Output format: evidence repair (repair draft)

## Short mode (default for a direct question)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Aim for at least 250. Any [PAPER] row id carries its DOI beside it, in prose and in tables (for example ES-75, DOI 10.1136/bmj.i4919).

1. **Answer:** whether the evidence meets your rule, the weakest point, whether it is repairable now or needs a new study, and the decision needed, in at most four sentences.
2. **One table, rules:** Rule in your words · Fact behind it · Met / Not met / Not measurable · Owner you named.
3. **Repair options:** at most three, each with its row, what it changes and what it does not.
4. **Record:** "Repair draft. Rules and owners are yours. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. AI-assisted draft." The record line appears in every answer, including refusals.

Offer the full version in one line.

## Full mode

### Summary
What the evidence is for, whether it meets your rule, the one decision needed.

### Evidence rule
| Rule in your words | Owner | Measured by |
|---|---|---|

### Results against the rule
| Result | Rule | Fact (A1 or A2, with date) | Verdict |
|---|---|---|---|

### Weakest point
Design weakness (new study needed) or disclosure or analysis weakness (repairable now), with rows.

### Repair options
| Weakness | Option | Row | Changes | Does not change |
|---|---|---|---|---|
Possible causes are labeled hypotheses.

### Routing
| Option | Responding work | Owner you named |
|---|---|---|

### Record
Dossier inclusion, submissions and external wording stop for the owner the person names, or owner not named. Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft. AI-assisted draft.
