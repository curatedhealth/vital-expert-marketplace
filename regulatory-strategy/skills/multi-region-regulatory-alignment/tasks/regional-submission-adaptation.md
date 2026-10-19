# B1 Regional submission adaptation

Framework task: DH-03.03.2.1, Part B, task B1. Replaces the earlier "Regional Submission Adaptation" section.

## What this task delivers

A decision draft for the order in which to file and what to adapt in each region: the candidate sequences built on dependency and reliance, the facts for each against the person's criteria, the person's scores ranked, and the per-region adaptation list. Every decision stops for the regulatory owner. It answers "in what order do we go, and what changes for each region?"

Why it matters: the order decides what can be reused. A decision in one region can open evidence routes in three others; the wrong first region can mean filing the same evidence three times.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.2.1 Part B, Regional submission adaptation |
| Workflow | The steps below |
| Knowledge | A1 map and A2 plan; `references/jurisdiction-requirements.md`; `references/evidence-reuse.md` |
| Tools | `analytics.mcda` (ranks options the person has scored); A1's tools if no map exists |
| Prompt | This guide |
| Template | `assets/submission-adaptation-output.md` |
| Input | The request and its context; A1 and A2; the person's criteria, weights and scores; their constraints (certificates held, evidence timing, team) |
| Governance | `references/governance.md`; people score; the regulatory owner decides |

## The rule that shapes this task: people decide

The model lays out the dependency facts for each option. The person sets the criteria, weights and scores. `analytics.mcda` ranks only what the person scored. The model never scores, never chooses the sequence, and never declares a class or pathway. If asked to propose scores, it may, each marked "proposed" with the fact behind it, and it does not rank them until the person confirms.

## Workflow

### Step 1. Start from A1 and A2

Use the map and the evidence plan in the conversation. If either is missing, run it first in short mode.

### Step 2. Build the dependency graph

From `jurisdiction-requirements.md` sections 3 and 4, list what each authorization or certificate unlocks, with legal status:

| If the person holds | It is accepted evidence or a basis in | Status | Rows |
|---|---|---|---|
| FDA 510(k), De Novo or PMA | Australia (same device; audit possible); Brazil (Class III and IV optimized review; software scope `[GAP]`) | in force | MR-09, MR-10, MR-11, MR-30 |
| FDA authorization | Great Britain reliance; Switzerland FDA route | draft; draft policy | MR-26, MR-27, MR-21 |
| EU MDR certificate and CE marking | Great Britain until 30 June 2030; Switzerland (EU notified body certificate deemed equivalent if credibly demonstrated); Australia (EU notified bodies) | in force | MR-23, MR-20, MR-07 |
| MDSAP certificate | Canada (required for Class II to IV per the MDSAP site); Australia (if Australian requirements audited); Brazil (GMP certificate, Class III and IV); Japan (inspection relief); US (routine inspections) | in force | MR-05, MR-36, MR-37, MR-38, MR-39 |
| Health Canada license | Australia; Brazil (Class III and IV) | in force | MR-09, MR-12, MR-30 |

Only routes that are in force can carry a sequence. Draft routes go in a separate line: "would shorten the plan if adopted; not available today".

### Step 3. Lay out two or three candidate sequences

Each sequence starts from what unlocks the most in-force routes for this product's classes, then follows the graph. Example shape: "EU MDR first, then Switzerland, Great Britain under CE acceptance, Australia on the EU certificate" or "FDA first, then Australia and Brazil on the FDA decision; MDSAP to serve Canada". State the shared prerequisite each relies on (a notified body certificate, an MDSAP audit covering Australian requirements). Where order does not matter, say so.

### Step 4. Criteria, facts, scores

Offer criteria and let the person change them: reliance reach (in-force routes opened), evidence reuse (from A2), readiness (certificates and evidence already held), route certainty (law versus draft). Define each 0 to 4 anchor in the person's words. Fill the options-by-criteria table with facts and rows, no scores. Ask for weights (sum to 1) and scores, and write them back for confirmation.

### Step 5. Rank and show what would flip it

Call `analytics.mcda` with `alternatives` (each sequence's id and scores) and `criteria_weights`. Report the value estimate and contributions. The tool gives no robustness view: for the top two, list each criterion on which their scores differ and say which option gains if that criterion's weight rises (others kept in proportion); give the swap point for the heaviest such criterion. If the tie is exact, say so and name every criterion that would break it in each direction.

When an option starts with an MDSAP audit, say in one line that MDSAP itself grants no marketing authorization and each regulator remains the authority for its own (MR-35), then what each member uses it for: Canada, required for a Class II, III or IV license (MR-05); Australia, evidence only if Australian requirements were audited (MR-36); Brazil, GMP certificate for Class III and IV (MR-37); Japan, exemption from on-site inspection (MR-38); United States, substitute for routine inspections only (MR-39).

### Step 6. Adaptation per region

For the person's chosen or leading sequence, list per region what must be adapted, from A1 and A2: classification argument under local rules (GB MDD-derived rules, Australian rules 4.5 to 4.7); dossier format (eSTAR, Annex II and III, IMDRF ToC for Canada); clinical evidence conditions (812.28 statements, TGA GCP basis, Health Canada disaggregation, EU equivalence data access); certificates (notified body, UK approved body above class I under UKCA, MDSAP covering Australian requirements); registration after authorization. Each item cites its row; unread items are `[GAP]`.

### Step 7. Stops and owners

Every region's submission, any pre-submission question, any reliance or equivalence claim, and the final class and pathway stop for the regulatory owner. Use the owner or role the person names for each region, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Build the output

Follow `assets/submission-adaptation-output.md`. Short mode for a direct question: the ranking with its close call, the sequence with what each step unlocks, the top adaptations, and the decisions waiting on the owner. Full mode adds the fact table, anchors and the full adaptation list.

## Before you hand it over

- Scores and weights are the person's, and the output says so.
- Only in-force routes carry the sequence; drafts are labeled.
- No class, pathway or submission content is presented as decided.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model structures, ranks what was scored, and lists adaptations. It does not choose and does not write submissions (DH-03.03.4).
- No approval timing promised. Review clocks are cited only from sourced rows (for example US-11, US-14, US-46).
- Drugs, biologics and wellness apps are out of scope.
