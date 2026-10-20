# B1 Stage repair review

Framework task: DH-01.01.1.2, Part B, task B1. Replaces the earlier "Stage repair" section (DH-01.01.1.2.3).

## What this task delivers

A review draft that says, rule by rule, whether each stage meets the lifecycle rules the person set: met, missed, or not measurable; for each miss, the missing item, the owner the person names, whether the next stage stays blocked (the person's call), the date the gate will be read again (the person's date), and the work that responds. It answers "which stages miss our standard, and who repairs what?"

Why it matters: the old rule holds, do not unblock the next stage while the item is missing. Writing the owner, the block and the reread date down makes the repair traceable and the next read repeatable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Product Manager (`digital-health-product-manager`) |
| Skill | DH-01.01.1.2 Part B, Stage repair review |
| Workflow | The steps below |
| Knowledge | A1 measures and A2 read; `references/lifecycle-measures.md`; `references/gate-evidence-rules.md`; rows TM3, TM13, TM14, PL5, PL9, CH9, PL95 (DOI 10.1136/bmj.n2061) |
| Tools | A2's tools if no stage read exists; `scripts/gate_log_check.py` |
| Prompt | This guide |
| Template | `assets/stage-repair-output.md` |
| Input | The request and its context; the person's rules and named owners; A1 and A2 results; reread dates |
| Governance | `references/governance.md`; people set rules, owners, blocks and dates |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the rules, names the owner of each, decides whether a stage stays blocked and sets the reread date. The model checks the A2 read against those rules, finds where a stage misses, and routes the work. It never sets a rule, decides a block, sets a date, names an owner the person has not named, or scores a team. If asked to propose rules, it may, each marked "proposed" with the row behind it, and applies none until the person confirms.

## Workflow

### Step 1. Gather the read

Use the A2 read the person brings into this request. If there is none, run A2 first in short mode on the log in this request. Say what was not read (for example post-market inputs for an unmarketed product).

### Step 2. Confirm the rules and owners

Write the person's rules back, numbered, with the owner of each. A rule without an owner is checked; its miss is listed as "owner not named".

### Step 3. Check each rule

Mark met, missed or not measurable `[GAP]`, with the count, flag or register fact behind it and its source (log row, script output, register reference and retrieval date).

### Step 4. For each miss: item, owner, block, reread date

Name the missing item, the owner given, and what it blocks by dependency. State the block as the person decided it ("next stage stays blocked, per your rule 2") or "block not decided; your call". Write the reread date the person set or "reread date not given" and ask; never supply one. Where the log shows the next stage already started (F4), write the fact and leave the decision to the person.

### Step 5. Route the response

| Miss | Responding work |
|---|---|
| Owed work product missing or accepted with no evidence | `clinical-product-lifecycle-and-stage-gates` (this pack) A2 evidence plan and B1 gate record |
| Design control or risk record gap | `dh-regulatory-and-quality` design-controls-and-risk-management |
| Post-market change not assessed | `dh-regulatory-and-quality` document-and-change-control for the record; `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control for whether a submission or notification is needed (CH9 to CH16, PL95) |
| Recall or complaint follow-up | `dh-regulatory-and-quality` audit-capa-and-complaints |
| Evidence behind a feasibility or evaluation stage | `dh-clinical-development` study-protocol-and-endpoint-design |
| Usability item missing or late | `dh-patient-and-user-experience` usability-monitoring |
| Handoff between functions | `integration-and-handoff-monitoring` (this pack) |

### Step 6. Re-run

Say which rules to re-check at the reread date (all rules touching the open items), using the same script and log.

## Build the output

Follow `assets/stage-repair-output.md`. Short mode for a direct question: rules met and missed, each miss with owner, block and reread date, and the one decision the person needs to make. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, owner, block and date is the person's, and the output says so; proposals are labeled.
- Every verdict cites the fact and source behind it.
- No overall rating of the lifecycle, a team or a person.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model checks and routes; it does not judge people or teams.
- No forecast of when a stage will close.
