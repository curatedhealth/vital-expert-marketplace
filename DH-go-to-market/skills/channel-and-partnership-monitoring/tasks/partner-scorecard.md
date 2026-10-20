# A2 Partner scorecard

Framework task: DH-02.01.4.2, Part A, task A2. Replaces the register task "Partner score" (CF-12.02.01.4.2.2).

## What this task delivers

A score per partner for the period: each of the person's measures counted from the person's handoff record, marked met or missed against the person's threshold, partner reports that could not be tied to a buyer listed separately and not counted, claim breaches quoted with their evidence, and duty checks from the measure sheet marked "evidence given" or "not shown". It answers "how did each partner do this period, on our record?"

Why it matters: a partner's own report counts what the partner wants counted. Scoring from the record, and only on buyers that can be tied to it, keeps the review fair to every partner and makes a claim breach visible before it spreads.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.01.4.2 Part A, Partner scorecard |
| Workflow | The steps below |
| Knowledge | A1 measure sheet; `references/monitoring-signals.md`; the approved claim list (the person's) |
| Tools | `scripts/partner_scorecard.py` (optional); `commercial-dh.audit_claims` (optional, with the caution in `references/tools.md`) |
| Prompt | This guide |
| Template | `assets/scorecard-output.md` |
| Input | The request and its context: the measure sheet, the handoff record for the period (a table, CSV or numbers), partner reports, claim evidence |
| Governance | `references/governance.md`; the person's data stays in the conversation |
| Catalogue job | `claim-labels`, only for the optional claim check (`commercial-dh.audit_claims`). The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## Read the request

- **Measure sheet.** From A1, or the person states the rules now. Without rules, the scorecard gives counts and no verdict.
- **Handoff record.** One row per event with partner, buyer id, event, date and source (record or partner report). Ask for buyer ids, not patient data.
- **Claim evidence.** The material, link or note showing the wording used, and the approved claim list.
- **Mode.** Short for a direct question; full for a review pack.

## Workflow

### Step 1. Put the data in one table

Partner, partner type, buyer id, event, date, source. Check periods and units; ask about rows without a buyer id or a later stage larger than an earlier one.

### Step 2. Count from the record

For each partner and measure, count distinct buyers from the handoff record. A partner report counts only where the same buyer and event are in the record (then the record row is what counts). An implementation counts only for a buyer this partner handed off. With code execution, save the table as CSV in the columns the script names and run `python3 scripts/partner_scorecard.py LOG.csv MEASURES.json`.

### Step 3. List what is not counted

Partner reports with no buyer id or a buyer not in the record: list them with date and what the partner claimed, "not counted". Implementations for buyers another partner handed off: list them. Do not argue with the partner's number; show the gap between it and the record.

### Step 4. Mark each measure

Met or missed against the person's threshold, with the number. A measure without a record is "not measurable `[GAP]`" and names who would hold the data.

### Step 5. Claim breaches

Quote each breach exactly as the evidence shows it, with date and source. Compare it with the approved claim list the person gave. Where a rule applies, cite it (for example implying FDA approval from registration is misbranding, CP-US-74). The breach goes to the person's regulatory or legal owner; the model does not decide whether the wording is lawful. `commercial-dh.audit_claims {reference: "<FDA number>", claims: [...]}` can be run as a screen, but it labeled every claim "exceeds_record" when the record held no intended purpose (`references/tools.md`); never cite its label as a finding.

### Step 6. Duty checks

For each duty on the measure sheet (breach notices, sub-processor changes, patient engagement cap, disclosure), mark "evidence given" or "not shown" from what the person supplies. Never infer a breach of a duty from missing evidence; say "not shown".

## Build the output

Follow `assets/scorecard-output.md`. Answer first: which partners missed which of the person's rules, which hit a hold rule, and any open claim breach. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every count comes from the person's record; partner-only numbers are listed and not counted.
- Every rule is the person's; no benchmark is used.
- Claim breaches are quoted, not judged; they go to the owner.
- No cause is stated for a miss; causes are B1 hypotheses.
- Confidential partner data is not put into any tool call or shared record without the person's say.

## Boundaries

- Scoring only. The action (hold, continue, change terms) is B1.
- No judgment of people or teams.
- Drugs, biologics and wellness apps are out of scope.
