# Worked example: placing the medical content AI options

A constructed example continuing the earlier examples. People, answers and scores are illustrative. Placement computed with `scripts/placement_check.py`; given capacity as the burden split, the buckets match the Navigator engine's grid (checked 19 October 2026). [CHECK: replace with a live run]

## The session (turns condensed)

**Turn 1 (assistant).** Picking up the comparison: the medical writing copilot (outcome fit 7.0, burden 6.0) and the AI medical information assistant (8.0, 7.8); doing nothing and doing it internally stay as reference lines, not placed. We'll score how much oversight you can carry, place the two options, then look at them through the lenses. How much oversight can the organization carry today? Here is the private sheet.

**Person.** [Four scores: 5, 6, 5, 6.]

**Turn 2.** Recorded: capacity 5.5 (5 to 6). Step 1 of 3: Score capacity and consequence. For which options would an error be too costly to hand to AI at all?

**Person (CMO).** The medical information assistant: wrong answers reach clinicians.

**Turn 3.** Recorded. Step 2 of 3: Place the options. With two options a median split puts one low by definition: what outcome fit counts as high value?

**Person (CMO).** Six or more.

**Turn 4.** Step 3 of 3: Read through the lenses. How would you tag each option: augmentation or automation, productivity or differentiation, internal or external?

**Person.** Copilot: augmentation, productivity, external. Assistant: automation, differentiation, external.

## The full report

**Summary.** Both options are high value and both need more oversight than the organization can carry today (5.5). The copilot goes to "Build the basis first"; the medical information assistant to "Support, do not automate", because the CMO judges its errors too costly to delegate. The CMO's result, Investigate first on the copilot, fits its bucket: build review into a pilot before scaling.

**1. The decision and the options.** The CMO decides whether and where AI should change medical content production. Placed: medical writing copilot; AI medical information assistant. Reference lines, not placed: doing nothing, doing it internally.

**2. Capacity and consequence.** Oversight the organization can carry today: 5.5 (range 5 to 6; CMO and Heads of Medical Information, Medical Writing and Field Medical). Too costly to delegate: the medical information assistant ("wrong answers reach clinicians", CMO).

**3. Placement**

| Option | Value (outcome fit) | Oversight needed | Fit | Bucket |
|---|---|---|---|---|
| Medical writing copilot | 7.0 | 6.0 | −0.5 (close to the line) | Build the basis first |
| AI medical information assistant | 8.0 | 7.8 | −2.3 | Support, do not automate (would be: Build the basis first) |

| | Oversight fits capacity | Oversight above capacity |
|---|---|---|
| **High value** (outcome fit 6 or more, owner's split) | — | Medical writing copilot |
| **Low value** | — | — |

Support, do not automate: AI medical information assistant (underlying: Build the basis first).

Build the basis first: put the method, review gates and capacity in place, then scale; the copilot is half a point above capacity. Support, do not automate: AI may help a person answer; a person decides what reaches clinicians.

**4. Lenses.** Capability against capacity: copilot is augmentation (capability play); assistant is automation (capacity play). Productivity against differentiation: copilot productivity; assistant differentiation. Internal against external: both external. Cost against benefit: copilot cost 5.8 for fit 7.0; assistant cost 6.8 for fit 8.0. Pattern: both options are external; nothing builds internal capability.

**5. Views recorded.** None.

**6. Gaps and record.** `[GAP]` No context-of-use statement yet for the assistant; the consequence answer is the CMO's judgment. `[GAP]` Play tags given in the session, not read from the organization's records. A decision aid, not a measurement. Draft prepared with an AI assistant, 19 October 2026; uncleared; placement not stored on a brief (connector unavailable).

## Why this is good

Capacity was scored by the people who would carry the oversight, not assumed. Neither baseline was placed. The consequence override kept the underlying bucket visible. The owner set the value split because a median of two would have been arbitrary. The lenses showed a pattern without changing anything.
