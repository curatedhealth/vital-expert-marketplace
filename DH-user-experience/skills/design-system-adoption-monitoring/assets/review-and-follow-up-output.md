# Output format: review and follow-up

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** which of your rules are missed (clinical and device first), the follow-up with its owner and target version, and the one decision needed from you.
2. **Rules checked (compact):** Rule (your words) · Number or evidence · Met / missed / not measurable.
3. **Follow-ups:** Miss · Contract or surface (your choice, or "your call") · Owner (yours, or "owner not named") · Version to carry the fix (yours, or "not set").
4. **Hypotheses:** labeled, each with what would confirm it.
5. **Ranking:** only on your scores, with tool and inputs; or "not ranked: scores needed".
6. **Stops:** what goes to the accountable owner.
7. **Record:** "Review draft. Rules, choices, owners and versions are yours. The contract is not changed to fit a breach. Clears: the person you name. Record built with verify.build_record once they clear it; until then, uncleared draft. AI-assisted."
8. One line offering the full version.

## Full mode

### Answer

### Rules and results
| Indicator | Rule (your words) | Number or evidence | Result |
|---|---|---|---|

### Hypotheses for each miss
| Miss | Hypothesis (labeled) | Mechanism row | What would confirm it |
|---|---|---|---|

### Contract or surface
| Miss or breach | If the surface changes (products affected) | If the contract changes (every product using it) | Your choice |
|---|---|---|---|

### Follow-ups
| Follow-up | Owner (your words) | Version to carry the fix | Device UI: questions for your owners (rows) |
|---|---|---|---|

### Ranking (your scores only)
| Rank | Follow-up | Inputs (yours) | Score (tool) | Checked by hand |
|---|---|---|---|---|

### Field events (optional, device surfaces)
| Title (as recorded) | Event date | Summary (quoted) | Source |
|---|---|---|---|

### Stops

### Gaps

### Calls made

### Record
Review draft. AI-assisted. Clears: NAME (the person you name). The record is built with `verify.build_record` once NAME clears it; until then it reads "uncleared draft".
