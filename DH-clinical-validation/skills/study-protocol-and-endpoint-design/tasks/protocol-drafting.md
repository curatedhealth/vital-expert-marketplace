# A2 Protocol drafting

Framework task: DH-01.02.1.1, Part A, task A2. Replaces the earlier "Study Protocol Drafting" section.

## What this task delivers

A protocol draft organized by the 34 SPIRIT 2025 items, filled only from the person's facts and earlier task outputs, with every item marked filled, stated not relevant, or open, and the digital health additions (DHT, decentralized elements, AI, registration, data flow) placed under the item they belong to. The open items become the work list before ethics submission.

Why it matters: SPIRIT 2025 expects every item addressed before ethics submission, and a non-applicable item stated as such (CV117). Digital trials add data-flow, device and remote-visit duties that general templates miss (CV67, CV68, CV102).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.1.1 Part A, Protocol drafting |
| Workflow | The steps below |
| Knowledge | `references/spirit-2025-checklist.md` (SP- rows); `references/protocol-rules.md`; A1 output for endpoints |
| Tools | `scripts/spirit_tally.py` for the item counts. A1's tools if no endpoint work exists yet |
| Prompt | This guide |
| Template | `assets/protocol-draft-output.md` |
| Input | The request and its context: product and version, intended use, population, comparator, design, setting and markets, visit plan (site or remote), data systems and DHTs, sponsor and roles, registry plans, existing protocol text |
| Governance | `references/governance.md`; the person's protocol owner signs |
| Catalogue job | none |

## Read the request

- **Scope.** Full protocol draft, an outline, or one section ("draft our data management section")? Draft only what was asked; list the rest as open.
- **Facts the person holds.** Take them verbatim. Every filled item names where its content came from (the person, A1, B1).
- **Elements that change the rules.** Decentralized visits, participant-owned devices, an AI component, real-world data or linkage, US or EU sites, an intervention that is a device. Each pulls in rows from `references/protocol-rules.md`.
- **Owner.** Who owns the protocol, in the person's words, or "owner not named".

## Workflow

### Step 1. Build the item skeleton

List the 34 items with their sub-items in SPIRIT order (SP-1a to SP-34). For each, mark: filled (from the person or an earlier task), not relevant (the person said so, with the reason, CV117), or open `[GAP]`.

### Step 2. Place the digital health additions

For each item, add the rule from `references/protocol-rules.md` that applies to this trial and its row, for example item 13 with remote visits (CV67), item 17 with DHT safety data (CV62), item 26 with data flow (CV68, CV102), source data location (CV60) and audit trails (CV14), item 32a with remote consent (CV16, and CV100 for EU sites). Add only rules triggered by the person's facts; list them once.

### Step 3. Draft the filled items

Write the text for items the person's facts cover, in protocol register, plainly. Never invent numbers, dates, sites, roles or instruments. Where a sentence needs a number the person has not given, write the sentence with `[GAP: who supplies it]`.

### Step 4. Outcomes and statistics

Take the endpoint from A1 (item 16, four elements) and the estimand and SAP decisions from B1 (items 19, 27a to 27d, 28b). If they do not exist, mark the items open and say A1 or B1 is the next step; do not draft statistical content.

### Step 5. Registration and dissemination

State the registration duties that apply on the person's facts: ICMJE before first consent (CV132); 21 days after first enrollment for a US applicable clinical trial (CV141); data sharing plan in the registration (CV135); results clocks for the markets involved (CV145, CV152). Whether the trial is an applicable clinical trial is the call of the owner the person names for regulatory status, or owner not named (CV142).

### Step 6. Open-items list

Collect every open item into one list ordered by dependency: what blocks what (for example, the endpoint blocks sample size, which blocks recruitment strategy). Name the owner the person gave for each, or "owner not named".

## Build the output

Follow `assets/protocol-draft-output.md`. Answer first: how many items are filled, not relevant and open (run `scripts/spirit_tally.py`; the three counts sum to 53 and every open id is listed once), and the open item that blocks the most. Short mode lists the open items and the triggered digital additions; full mode adds the drafted text per item. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every filled item says where its content came from; nothing is invented.
- Every digital addition carries its row; guidance is labeled nonbinding where it is.
- The draft is labeled "protocol draft for OWNER"; it is never called complete, compliant or ready for submission.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line ends the answer: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Checking an existing protocol for completeness: study design quality monitoring, A1.
- Statistical content: B1, and the owner the person names for statistics, or owner not named decides.
- Ethics, IDE, CTA or notified body submissions: the owner the person names for regulatory status, or owner not named, and `dh-regulatory-strategy` regulatory-submission-and-dossier.
- Trial operations (site contracts, platform selection): `dh-clinical-validation` decentralized-trial-operations (DH-01.02.3).
