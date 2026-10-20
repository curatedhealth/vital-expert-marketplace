# B1 Company and evidence assessment record

Framework task: DH-DIL.2.1, Part B, task B1. Replaces the judgment the old company-dossier job left undefined: the old skills ran tools and stopped, with no step that read the facts against the person's own criteria.

## What this task delivers

An assessment record draft: each of the person's diligence criteria read against the A1 profile and the A2 evidence read, marked met, not met or not measurable, with the fact and record behind each; the data and privacy facts to request from the target, flagged for the owner the person names for compliance (or owner not named); the decision the person states (for example "move to full diligence", "hold", "drop"), its date and the person who decided; open items with the owner the person names. It answers "against our criteria, what do the records show, what is missing, and what did we decide?"

Why it matters: a screen decided on a score or a deck leaves nothing a reader can check later. Writing each criterion beside the record it rests on, and the decision in the person's words, keeps the judgment the person's and the facts traceable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old skill "Worker: not bound"); see `references/governance.md` |
| Skill | DH-DIL.2.1 Part B, Company and evidence assessment record |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/public-record-rules.md`; `references/company-status.md` (DL-135 to DL-168); `references/evidence-frameworks.md`; rows DL-086 to DL-106 (health data), DL-126 to DL-128, DL-107 to DL-113 (DOI 10.1038/s41746-023-00836-5) |
| Tools | A1 and A2 tools if no profile or read exists in this request; `scripts/profile_table.py` |
| Prompt | This guide |
| Template | `assets/assessment-record-output.md` |
| Input | The request and its context: the person's criteria in their words, A1 and A2 outputs, the person's material (kept separate), the decision, date and decider as stated, owners named |
| Governance | `references/governance.md`; the person sets the criteria and makes the decision; no investment advice |
| Catalogue job | `company-dossier` (the record step has no tool; `investment-memo` is never started) |

## The rule that shapes this task: people decide

The person writes the criteria and makes the decision. The model reads the facts against the criteria and writes down what the person decided. It never recommends investing or passing, never sets a criterion, never states a valuation, price, multiple or return, and never names a decider or owner the person has not named. If asked to propose criteria, it may, each marked "proposed" with the row behind it (for example "an FDA marketing authorization, not a registration", DL-126, DL-128), and applies none until the person confirms.

## Workflow

### Step 1. Confirm the criteria

Write the person's criteria back, numbered, verbatim. If none were given, say "Diligence criteria not stated `[GAP]`", offer source-named elements as "proposed", and stop before marking anything.

### Step 2. Gather the facts

Use the A1 and A2 outputs the person brings into this request. If there are none, run A1 and A2 in short mode for the company in this request. Say what was not read (for example Companies House, not loaded). Always carry two facts into the record: the saved safety events and recall flags (`references/tools.md`, `compare_portfolio`), or "not read `[GAP]`"; and the company's status from the status step (`references/company-status.md`), or "Status: [GAP]: not read" with the filings to open. Never print 0, "none" or "US company" for a field the record lacks.

### Step 3. Read each criterion

Mark met, not met, or not measurable `[GAP]`, with the record and retrieval date behind it, or "your material" with the document name. A criterion that depends on a record the library does not hold is not measurable until the person reads it. Never read a record's silence as "not met" (no breach on the portal is not "no breach", DL-092 and DL-096; no registered study is not "no evidence"). For a recall or safety criterion, cite the saved `compare_portfolio` result for the company (`examples/live/compare_portfolio_dtx_2026-10-19.json`): `safety_events` and `risk_flags`. `none_found` means the store was searched and holds no row: write "none found in the loaded enforcement source, retrieved 19 October 2026; not proof of none", mark the criterion not measurable, and name the direct FDA recall read. A recall flag is quoted as stored (for example Pear Therapeutics, Inc.: "fda_recall: Class II on 2021-06-07" for reSET and reSET-O Mobile App), with no judgment of its relevance to the person's question. For a criterion on whether the company still exists, is listed or was acquired, use the status step (`references/company-status.md`); never mark it from press or memory.

### Step 4. Data and privacy facts to request

Where the target handles health data, list as requests for the owner the person names for compliance (or owner not named), each with its row: the four-factor breach risk assessments and the burden-of-proof file (DL-087, DL-094); the HHS portal read, main list and archive (DL-095, DL-096); the Article 9(2) ground per processing purpose and any DPIA for EU data (DL-101 (inference), DL-106); national conditions where they apply (DL-105). Whether the target complies is that owner's call. Transaction rules (HSR, CFIUS, DOJ bulk data, EU and Swiss screening, DL-044 to DL-085) belong to `investment-memo-and-decision-record` (this pack); name them there only.

### Step 5. Record the decision as stated

Write the decision, date and decider exactly as the person gives them. If the decision is "move forward" while a criterion is not met, write both facts side by side and the person's stated reason; do not judge it. If no decision was given, write "decision not given".

### Step 6. Open items and owners

For each criterion not met or not measurable: what would settle it (a record to read, a document to request), the owner the person named or "owner not named", and the date the person set to read it again or "not given".

## Build the output

Follow `assets/assessment-record-output.md`. Answer first: criteria met, not met and not measurable (counts of the person's criteria), the decision as stated, and the open item that blocks most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every criterion, the decision, the decider and owners are the person's, and the record says so.
- Every "met" carries a record reference and date, or "your material".
- No recommendation to invest or pass, no valuation, price, multiple, return or market size.
- No statement that a target complies or a deal is clear.
- Safety events and recall flags are cited from the saved `compare_portfolio` result ("none found in the loaded enforcement source ... not proof of none" where `none_found`), or marked not read; status is from a filing or register, or "[GAP]: not read".
- Word count: run `python3 scripts/profile_table.py --count ANSWER.md` on the short answer; at or under 450 words, counted without the calls list and source columns.
- The record is labeled "assessment record draft for OWNER".
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The investment memo and decision record across the deal: `investment-memo-and-decision-record` (this pack).
- Regulatory status analysis: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Reimbursement status: `dh-access-and-value` coverage-pathway-and-access-strategy.
