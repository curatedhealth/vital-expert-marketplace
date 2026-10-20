# B1 Mechanism assumptions and stopping rules

Framework task: DH-01.01.2.1, Part B, task B1. Replaces the earlier "Mechanism assumption" section (DH-01.01.2.1.3, register CF-12.01.01.2.1.3).

## What this task delivers

An assumption register: for each link of the mechanism, the assumption that, if wrong, stops the intervention; the signal and measure that would show it is wrong; the milestone or threshold the person sets in advance; the gate it belongs to; and the person who stops the version. It answers "what would kill this, how would we know, and who decides?"

Why it matters: milestones written after the data arrive move the target (TM57). Writing the assumption, its signal and its stopper first makes the go or no-go repeatable at every version.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.1 Part B, Mechanism assumptions and stopping rules |
| Workflow | The steps below |
| Knowledge | A1, A2, A3 and A4 outputs; `references/assumption-rules.md`; `references/engagement-rules.md` section 3 and `references/safety-design-rules.md` section 4 for A3 and A4 items; `references/precedents.md`; rows TM2 to TM5, TM13 to TM17, TM54 to TM65, TM73, TM88, TM97, TM118, TM138, TM139, TM143, TM144 |
| Tools | `literature.search_literature`, `verify.qualify_source` and `verify.check_claim` only when an assumption rests on a published finding; `scripts/mechanism_map_check.py` |
| Prompt | This guide |
| Template | `assets/mechanism-assumptions-output.md` |
| Input | The request and its context; A1 chain, A2 components, A3 mechanics (effective engagement definition, open flags) and A4 hazards (mitigations, indicators, thresholds); the person's gate model, milestones and named owners |
| Governance | `references/governance.md`; people set milestones, thresholds and stoppers |
| Catalogue job | none |

## The rule that shapes this task: people decide

The person writes the milestones and thresholds and names who stops a version. The model lists the assumptions each link carries, lays out the signals the sources name, and checks that each assumption has a signal, a measure and a stopper. It never sets a threshold, never decides that a signal stops the product, and never names a stopper the person has not named. If asked to propose milestones, it may, each marked "proposed" with the row behind it, and applies none until the person confirms.

## Workflow

### Step 1. Gather the chain, components, mechanics and hazards

Use A1 and A2 from the conversation. If either is missing, run it first in short mode. An assumption register on A1 alone is possible and says components were not reviewed. Read A3 and A4 when they exist; if they do not, say mechanics and design hazards were not reviewed, and run them only if the person asks.

### Step 2. List the assumptions link by link

For each link, write the assumption in one sentence (assumption-rules section 1): delivered as specified (A2); user acts (engagement proximal outcome, TM87); action produces change (mediator, TM84); change moves outcome (TM83); the chain holds in this population (TM9); tailoring variables are reliable and valid (TM88). From A3, add: the person's definition of effective engagement holds (SE86, SE87, Michie 2017, DOI 10.2196/jmir.7126; or "usage, not adherence" if undefined, SE92, Sieverink 2017, DOI 10.2196/jmir.8578), and a mechanic does not crowd out the effective features (SE84, Perski 2017, DOI 10.1007/s13142-016-0453-1). From A4, add each mitigation that has not been tested as an assumption that it works, with the indicator and threshold the person set (SE63, MDCG 2025-10, not legally binding). Add the person's key uncertainties in their words (TM4, TM5). Mark the one or two the person considers fatal; that is their call.

### Step 3. Write the signal and its measure

For each assumption, name what would show it is wrong and the measure (TM14, TM97). Use the MRC/NIHR progression criteria list as prompts (recruitment, retention, adherence, acceptability, content, delivery, provider capacity, TM14). Where no measure exists, mark `[GAP]` and say it becomes a check in mechanism validation monitoring (A1 there).

### Step 4. Set the milestone with the person

Ask the person for the milestone or threshold for each signal, set now, on clinical significance (TM57). Offer the gate shapes in assumption-rules section 3 (ORBIT, MOST, MRC/NIHR) and let the person pick one or none (TM65). Write their words back for confirmation before anything else.

### Step 5. Name the stopper and the action

For each assumption, name who stops the version if the signal appears (old task rule), in the person's words, or "owner not named". Name the action the gate source states, only for the gate model the person picked; if none is picked, leave the column as "gate model not chosen" and list the options once (TM65). The actions the sources state are: return to an earlier phase, refine within agreed boundaries, narrow, abandon (TM3, TM13, TM62, TM73); name them without choosing one. ORBIT IIa (TM62) applies to clinically significant change on the target, not to engagement or adherence links; for those, the feasibility progression criteria apply (TM14).

### Step 6. Precedent signals (when useful)

Show how a precedent's record handled a link that did not hold: reSET's primary opioid users became a labeled limitation (TM138); EndeavorRx's control isolated the adaptive algorithm and the indication limits behavioral symptoms (TM143, TM144). These are context, not targets.

### Step 7. Evidence behind an assumption (only if asked)

If the person says an assumption is already supported by a study, take the sentence from the paper, call `verify.qualify_source {doi, question}` then `verify.check_claim` with the passage, and accept only a passage read in the same direction (N3). Say what population the paper studied.

### Step 8. Check completeness (optional, with code execution)

Add the register to the map JSON and run `python3 scripts/mechanism_map_check.py MAP.json`; it lists assumptions with no signal, no measure, no milestone or no stopper.

## Build the output

Follow `assets/mechanism-assumptions-output.md`. Short mode for a direct question: the fatal assumptions, each with signal, milestone (the person's or open) and stopper, and the one decision the person needs to make. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every milestone, threshold and stopper is the person's, or open; proposals are labeled.
- Every assumption has a signal and a measure, or a `[GAP]` routed to the monitoring skill.
- No verdict that the product will or will not work.
- Go or no-go and stopping a version stop for the named owner.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Checking assumptions against study or cohort data: mechanism validation monitoring (DH-01.01.2.2).
- Product-level stage gates and design reviews: `dh-clinical-development` clinical-product-lifecycle-and-stage-gates; risk files: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Feasibility or pivotal study design: `dh-clinical-development` study-protocol-and-endpoint-design.
