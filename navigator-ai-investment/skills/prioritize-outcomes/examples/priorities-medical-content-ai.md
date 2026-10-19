# Worked example: prioritizing outcomes for AI in medical content production

A constructed example continuing the *Decision Framing*, *Value-at-Stake Sizing* and *Outcome Discovery* examples. People, answers and scores are illustrative, not a real client. The connector was unavailable (its allowance was used up), so scores were computed with `scripts/outcome_priority_check.py`, which applies the Navigator's formula and bands (checked against the engine's own test case). [CHECK: replace with a live run]

## The session (turns condensed)

**Turn 1 (assistant).** Picking up your four outcomes and the frame: the CMO owns the decision; you said it is reversible (a pilot first) but spans Medical Information, Medical Writing and Field Medical. Three steps: score, read, attest. About three questions. Step 1 of 3. Who scores? I'd suggest the four heads who own these outcomes. Here is the private sheet; please return it to me only.

**Person.** [Four sheets returned: CMO, Head of Medical Information, Head of Medical Writing, Head of Field Medical.]

**Turn 2.** All four in, nothing missing. Step 2 of 3. Two outcomes split the room: writer time on label updates (importance 5 to 9) and approved content for field questions (importance 5 to 9). The Head of Field Medical scored the second much higher than anyone else: what is the view behind that, in a line?

**Person (Head of Field Medical).** My teams improvise answers every week; nobody else sees that.

**Turn 3.** Recorded as dissent. Step 3 of 3. The field-test rule applies, whatever the decision's size: the room split by 4 points on two top-five outcomes. Field-test the top three with the people they are for, or proceed without, with your reason?

**Person (CMO).** Test it, quickly. Five clinicians, five writers, five field medics. Two weeks.

**Turn 4.** Plan drafted. Last question: do you attest these priorities, with the dissent recorded and the field test pending, as the basis for choosing options?

**Person (CMO).** Yes, subject to the field test.

## The full report

**Summary.** The most underserved outcome is faster accurate answers for clinicians (opportunity 13, strong), then faster integration of new data into scientific materials (11.3, moderate). The room split on writer time and on approved field content, and the third place depends on one scorer, so the top outcomes go to a two-week field test. Gate 2 attested by the CMO, conditional on the test.

**1. The decision.** The Chief Medical Officer decides whether, and where, AI should change how medical content is produced across Medical Affairs.

**2. Outcome priorities**

| Rank | Outcome | For whom | Driver | Importance | Satisfaction today | Opportunity | Band | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Reduce the time from a clinician's question to an accurate medical answer | Clinicians | Faster, accurate responses | 8.5 | 4.0 | 13.0 | Strong | Scored in the room |
| 2 | Minimize the time to bring new clinical data into scientific materials | Scientific leads | Writer capacity | 7.5 | 3.8 | 11.3 | Moderate | Scored in the room |
| 3 | Reduce writer time on routine label-driven updates | Medical writers | Writer capacity | 6.8 | 4.0 | 9.5 | Low | Scored in the room |
| 4 | Increase the share of field questions answered with approved content | Field medical teams | Faster, accurate responses | 6.3 | 4.8 | 7.8 | Low | Scored in the room |

Scorers: CMO, Heads of Medical Information, Medical Writing and Field Medical (four, equal weight). Computed group averages. Outcomes 1 and 2 are underserved: important, and satisfaction below 4. Outcomes 3 and 4 rank lower on average but are each very important to one scorer.

**3. Does it hold?** The leader holds whoever is left out. The top three do not: without the Head of Medical Writing, approved field content replaces writer time in third place. Strong disagreement on writer time (importance 5 to 9, satisfaction 2 to 5) and on approved field content (importance 5 to 9, satisfaction 3 to 6). For outcome 2 the average (11.3) sits above the median of scorers' own scores (11.0); no single scorer pulls it.

**4. The owner's view** (shown after the group's). The CMO ranks the same top three in the same order (14, 13, 10). No difference on the top set.

**5. Field test.** Required: strong disagreement (4 points) on two top-five outcomes. Not triggered by size (the owner judged the decision reversible) or by a flip (the leader holds); the third-place change is reported only. Plan: the top three plus approved field content, given its split; five clinicians, five medical writers, five field medical leads; importance and satisfaction in their words; two weeks; run by the Medical Excellence lead. Until results return, every score is "scored in the room".

**6. Gate 2.** Priorities attested by the Chief Medical Officer, 19 October 2026, conditional on the field test. Evidence: four scorers, field test pending. Dissent entries: 2.

**7. Dissent**

| Outcome | View | Held by | Recorded |
|---|---|---|---|
| Approved content for field questions | Underrated: field teams improvise answers weekly, unseen by others | Head of Field Medical | 19 Oct 2026 |
| Writer time on label updates | Rated far more important than by the others (9 versus 5 to 7) | Head of Medical Writing | 19 Oct 2026 |

**8. Carried to the Intelligence Core.** Outcomes 1 and 2, and 3 pending the test. Options carried from discovery: the medical writing copilot. For each top outcome, the level of AI involvement (assist to redesign) is open, to be set by the process owner against the outcome.

**9. Gaps.** `[GAP]` Field test results not yet in; priorities are room views. `[GAP]` Outcome 4 has no baseline (from discovery). `[GAP]` Scores not stored on a Navigator brief (connector unavailable).

**10. Record.** Draft prepared with an AI assistant, 19 October 2026. Uncleared. Scores stored on a brief: no (computed locally with the same formula).

## Why this is good

The group's result came first and the owner's after. The split was turned into two named views, not averaged away. The field-test rule was read against the decision with the owner's thresholds, triggered by strong disagreement, not by size. The owner chose and attested; the assistant did neither.
