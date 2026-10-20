# B1 Pathway strategy

Framework task: DH-03.03.3.1, Part B, task B1. Replaces the earlier "Regulatory Pathway Selection" section.

## What this task delivers

A decision draft for the person's regulatory owner: the route options per jurisdiction with sourced facts (route, evidence bar, review clock, fee, notified body capacity), the criteria that matter to this person with their own weights and scores, a ranking of what they scored, a sequence built on what unlocks what, and the gates where the plan should be reviewed. The owner decides; this task makes the decision explicit, sourced and repeatable.

Why it matters: the first market and route set the evidence plan, the spend and the team for years. A choice made on habit ("FDA first, everyone does") is hard to defend when a fact moves, for example a notified body timeline or a predicate that turns out not to fit.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.3.1 Part B, Pathway strategy |
| Workflow | The steps below |
| Knowledge | A1 classification arguments; A2 precedents; `references/pathway-facts.md`; `references/classification-rules.md`; MCDA method as the tool cites it (EVIDEM; ISPOR MCDA good practice) |
| Tools | `analytics.mcda` (ranks options the person scored); A2's tools if no precedents exist yet; `scripts/mcda_swap_points.py` (optional) |
| Prompt | This guide |
| Template | `assets/pathway-strategy-output.md` |
| Input | The request and its context; A1 and A2; the person's target markets, evidence held or planned, constraints (budget, team, investor or partner commitments); their criteria, weights, scores and named owner |
| Governance | `references/governance.md`; people score; the pathway decision stops for the regulatory owner |

## The rule that shapes this task: people score

The model lays out the facts for every option against every criterion. The person sets the weights and gives the scores. `analytics.mcda` only ranks what the person scored. If the person asks the model to propose scores, each proposed score carries the fact behind it, is labeled "proposed", and is not ranked until the person confirms it.

## Workflow

### Step 1. Start from A1 and A2

Use the A1 classification arguments and the A2 precedents in the conversation. If either is missing, run it first in short mode. An option exists only where A1 and A2 support it: for example a 510(k) option needs at least one predicate candidate from A2; an EU class I self-declaration option needs an A1 argument that Rule 11 leaves the product in class I. Options without support are named in one line and left out.

### Step 2. Lay out the options with sourced facts

For each option (route per jurisdiction), fill five facts from `pathway-facts.md`, each with its row:

| Fact | Example content |
|---|---|
| Route | 510(k) to predicate K233577; De Novo; EU class IIa under Annex IX; GB via CE acceptance; CH via EU declaration |
| Evidence bar | Substantial equivalence test (RP US-06); De Novo risks and mitigations (RP US-12); MDR Article 61 clinical evaluation and MDCG 2020-1 (RP EU-17, RP EU-32) |
| Review clock | Regulation clock, MDUFA goal in FDA days, observed average total days, each named for what it is (RP US-11, RP US-46, RP US-58) |
| Fee | FY 2027 FDA fees with the small-business amount (RP US-55); notified body fees `[GAP]` |
| Capacity | Notified body survey figures, dated and labeled as a Commission-commissioned contractor survey (RP EU-40 to EU-44); `[GAP]` for software-specific capacity |

Add the dependencies that tie options together: Switzerland recognizes EU declarations (MR-19) and deems EU notified body certificates equivalent if equivalence of procedure and qualification is credibly demonstrated (MR-20) but not FDA authorizations yet (MR-21); GB accepts CE marked MDR devices to 30 June 2030 (RP UK-03); FDA accepts foreign clinical data under GCP conditions (JX-15); a PCCP can only be established in certain original submissions (AI US-09). These are facts, not recommendations.

### Step 3. Agree the criteria

Propose a default set and let the person drop, add or rename (four to seven):

| Criterion | The question it answers | Facts that inform it |
|---|---|---|
| Evidence fit | Does the evidence we hold or plan meet this route's bar? | Evidence bar per route; the person's studies |
| Readiness | How much is left before we can file? | QMS, technical documentation, notified body agreement, eSTAR |
| Review clock | How long from filing to decision? | The three clocks, kept separate |
| Cost | What does the route cost to file? | Fees; `[GAP]` cells shown as gaps |
| Market value to us | How much does this authorization matter to our plan? | The person's own plan; reimbursement routes it unlocks (Market Access pack) |
| Reuse | Does work for this route serve others? | Recognition and reliance facts in Step 2 |

Define the 0 to 4 anchors for each criterion with the person, in their words, before scoring.

### Step 4. Collect weights and scores, then rank

Show the options-by-criteria table with the facts and no scores. Ask for weights (summing to 1) and a 0 to 4 score per cell. Write them back for confirmation. Then call `analytics.mcda`:

```
{"alternatives": [{"id": "US 510(k) to K233577", "scores": {"evidence_fit": <person>, ...}}, ...],
 "criteria_weights": {"evidence_fit": <person>, ...}}
```

Report the value estimate and each criterion's contribution. The tool returns no tie flag and no robustness view: state ties yourself, and for each adjacent pair give the weight at which they would swap (other weights kept in proportion). With code execution, `scripts/mcda_swap_points.py` recomputes the values (a check on the tool) and the swap weights. Name the close call: that is where the owner's judgment matters most.

### Step 5. Sequence by dependency

Order the chosen routes by what unlocks what, never by date. Examples of sourced dependencies: an EU notified body certificate is deemed equivalent in Switzerland if equivalence of procedure and qualification is credibly demonstrated (MR-20), and serves GB until 30 June 2030 (RP UK-03); EUDAMED registration must precede placing the first unit (JX-40); a De Novo grant creates a code that later 510(k)s can cite (RP US-05); a PCCP has to be in the original submission (AI US-09). Where order does not matter, say so.

### Step 6. Set the gates and stop for the owner

For each step, the gate: what must be true to proceed (A1 class argument accepted by the owner, a Pre-Submission answer received, a notified body agreement signed, a study read out), and what would change the plan. Gates are conditions, never dates. Close with the decision the owner has to take, by name, or "owner not named".

## Build the output

Follow `assets/pathway-strategy-output.md`. Short mode: the ranking with the close call, the sequence with gates, at most three facts that could change a score, the owner's decision. 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line.

## Before you hand it over

- Every fact carries its row; every `[GAP]` cell is visible.
- Scores, weights and the owner are the person's, and the output says so.
- Clocks are labeled (regulation, MDUFA FDA days, observed total days); fees are FY 2027.
- The pathway choice and any wording for a regulator or notified body stop for the owner; label the output a decision draft.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model does not score and does not choose.
- No predicted decision date, approval probability or budget beyond the sourced fees.
- No submission content; dossier assembly is DH-03.03.4, PCCP content is DH-03.03.1.
- Drugs, biologics and wellness apps are out of scope.
