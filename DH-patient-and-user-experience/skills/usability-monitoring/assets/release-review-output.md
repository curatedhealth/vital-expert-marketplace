# Output format: release review and repair plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** rules the build misses, the decision or block and whose it is, and the first repair with its owner.
2. **Your rules and the check (compact):** Rule (your words) · Result (count or evidence) · Met / missed / not measurable.
3. **Repairs:** Repair (proposed) · Control type · Answers which miss · Owner (yours, or "owner not named") · Ranking if you scored.
4. **For the regulatory owner:** UI or training changes as Decision Point B facts; no conclusion.
5. **Stops:** shipping (release owner), risk acceptance (risk owner), regulatory questions.
6. **Record:** "Release review draft on build NAME. Decision: as you state it, or not taken. Uncleared until a named person clears it through verify.build_record. AI-assisted."
7. One line offering the full version.

## Full mode

### Answer

### Build and evidence reviewed
A1 run (date), A2 run (date), what was not reviewed.

### Rules and results
| Rule (person's words) | Applies to | Result | Evidence | Status |
|---|---|---|---|---|

### Hypotheses for each miss
| Miss | Hypothesis (labeled) | What would confirm it | Row |
|---|---|---|---|

### Repair options (proposed)
| Repair | Type (UX-US-33) | Needs data (UX-US-42) | Score and rank (person's scores) | Owner | Forum |
|---|---|---|---|---|---|

Calls made: analytics.mcda or analytics.rice with arguments.

### Regulatory handoff facts
| Change | Decision Point B item (UX-US-49) | Owner |
|---|---|---|

### Decision record
| Build | Decision (person's) | Conditions | Decided by | Cleared by |
|---|---|---|---|---|

### Gaps

### Record
Release review draft. The model did not decide shipping. AI-assisted. Cleared by NAME through verify.build_record, or "uncleared draft" until a named person clears it.
