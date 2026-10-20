# B1 Partner action review

Framework task: DH-02.01.4.2, Part B, task B1. Replaces the register task "Partner action" (CF-12.02.01.4.2.3) and the one-line pass rule and owner sections.

## What this task delivers

One action per partner (hold, continue, or change terms) applied from the person's hold rules, with the number behind it, the owner the person names, the date the person sets for telling the partner, hypotheses for each miss labeled as hypotheses, and every stop: fraud-and-abuse triggers in any proposed change of terms, claim breaches, and anything sent to a partner. It answers "what do we do with each partner, by our own rules?"

Why it matters: a hold applied by rule is defensible; one applied by mood is not. A change of terms is also where compensation drifts toward per-referral or outcomes pay, which is a fraud-and-abuse stop (CP-US-01, CP-US-08, CP-US-13).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.01.4.2 Part B, Partner action review |
| Workflow | The steps below |
| Knowledge | A1 measure sheet and A2 scorecard; `references/partner-terms.md`; `references/fraud-and-abuse-stops.md`; `references/monitoring-signals.md` |
| Tools | `analytics.rice` (only if the person scores remediation initiatives); `scripts/partner_scorecard.py` through A2 |
| Prompt | This guide |
| Template | `assets/action-review-output.md` |
| Input | The request and its context: A2 results, the person's hold rules, owners, any change of terms under discussion |
| Governance | `references/governance.md`; the person decides every action, owner and date |
| Catalogue job | `partner-prioritization`, only when the person scores remediation initiatives (`analytics.rice`). The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## The rule that shapes this task: people decide

The person's hold rules decide the action. The model applies them, shows the number behind each, and lays out options. It never decides to terminate, never sets the date a partner is told, never names an owner the person has not named, and never writes to a partner. Two register rules are offered as defaults for the person to confirm: a partner whose claim-use term is absent is held, and a partner with an open claim breach is not continued.

## Workflow

### Step 1. Gather the evidence

Use A2 from the conversation. If it is missing and needed, run it first in short mode. A review without a scorecard gives no action, only the rules to apply.

### Step 2. Apply the hold rules

For each partner, apply the person's hold rules from the measure sheet, then the register defaults if confirmed. Write: action (hold, continue, change terms: as the rules give it, or "for your decision" where no rule decides), the measure and number behind it.

### Step 3. Hypotheses, not causes

For each miss, list possible reasons as hypotheses with what would confirm each, drawn from the data (for example: "partner reports leads without buyer ids: the handoff event may not be understood the same way by both sides; confirm by comparing the partner's list with the record"). Never state a cause the data does not show.

### Step 4. Changes of terms

If the person is considering a change of terms, list which term changes (from `references/partner-terms.md`) and check it against the triggers in `references/fraud-and-abuse-stops.md`. Any move to per-referral, per-patient, volume-based or outcomes-based pay, free items to patients or providers, or donated technology stops for the compliance or legal owner with the elements laid out (never "met", never "protected"). If the partner is or will be paid on outcomes, the monitoring duties of CP-US-14 apply and go on the measure sheet.

### Step 5. Owner and date

For each action: the owner as the person names them ("owner not named" otherwise, and ask), and the date the partner is told as the person sets it ("date not set" otherwise). No urgency framing; contractual notice periods are the person's facts.

If the person asks for a termination or notice to a partner, ask for the agreement's cause, notice and cure clauses (`[GAP]` if not given) and offer two neutral drafts for the owner: a notice of breach that asks for a cure, and a termination notice. Keep the performance ground (counts against the person's rules) and the claim-breach ground (the quoted wording, its date and source) in separate paragraphs. Use the counts and the quote from a scorecard already in the conversation rather than placeholders.

### Step 6. Rank remediation work (optional)

If the person lists remediation initiatives with reach, impact, confidence and effort, call `analytics.rice` with confidence as a percent (80, not 0.8; `references/tools.md`) and report the order as the result of their inputs.

## Build the output

Follow `assets/action-review-output.md`. Answer first: the action per partner by the person's rules, the stops, and the decision the owner faces. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, owner and date is the person's, and the output says so.
- Every action cites the number behind it.
- Causes are hypotheses, labeled.
- No message to a partner is sent or presented as final; any wording is "draft for the owner".
- Fraud-and-abuse triggers are laid out, never judged.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or partners beyond their counts.
- No forecast of a partner's recovery.
- Payer outcomes contracts are Market Access.
- Drugs, biologics and wellness apps are out of scope.
