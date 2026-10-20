# Output format: adoption review and follow-up

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap and end with the same record line.

## Short mode (default for a direct question)

1. **Answer:** which sites or roles missed your rule, with numerator and denominator; which met; which have no verdict yet.
2. **Hypotheses per miss:** task, training or workflow, each labeled "hypothesis" with the signal in the data and what would confirm it.
3. **Follow-up options:** the design or workflow option beside any training option; a repeat session says what changes; ranking only if you scored (values and the smallest weight change that flips the top two).
4. **Owners and next steps:** as you named them, or "owner not named"; dates yours or blank.
5. **Stops:** clinical or payment claims from adoption, staff-identifying reports, training changes for a device, payments tied to usage.
6. **Record:** "Adoption review draft. Rule, scores, owners and dates are yours." Then who clears it: "Cleared by NAME; the record is built with `verify.build_record` once NAME clears it", or, with no name, "uncleared draft". AI-assisted.
7. One line offering the full version.

## Full mode

### Answer

### Against your rule
| Site / role | Result | Numbers | Verdict |
|---|---|---|---|

### Hypotheses (not findings)
| Miss | Hypothesis | Signal in the data | What would confirm it | Row |
|---|---|---|---|---|

### Follow-up options
| Option | What changes | Sourced fact | Row |
|---|---|---|---|

### Ranking (analytics.mcda on your scores)
| Rank | Option | Value (0 to 100) | Largest contribution |
|---|---|---|---|

### Owners and next steps
| Miss | Owner (yours) | Next step (yours) | Date (yours) | What A2 will measure next |
|---|---|---|---|---|

### Stops for the accountable owner

### Gaps

### Calls made

### Record
Adoption review draft. The ranking reflects your scores; it is not a recommendation. AI-assisted. Cleared by NAME (as the person named them); the record is built with `verify.build_record` once NAME clears it. With no name: uncleared draft.
