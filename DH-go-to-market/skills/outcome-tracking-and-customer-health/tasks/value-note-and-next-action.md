# B1 Value note and next action

Framework task: DH-02.02.3.1, Part B, task B1. Replaces the earlier "Value note to the account" section and carries the one-line pass rule and miss owner rule as steps.

## What this task delivers

For each account in scope, one of two drafts: a value note that states only results traceable to signal rows, in plain wording that makes no effect, cost or comparison claim; or a next-action note naming the missed signal, the actions the person chose, their owners and the forum that will see them. It answers "what can we show each account, and what do we do where it misses?"

Why it matters: a value note is wording that leaves the company. The register's rules are blunt: "Do not send a result you cannot trace to a signal" and "Do not send a value story to an account below every threshold". A note that turns a usage share into an outcome claim crosses into promotion.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.3.1 Part B, Value note and next action |
| Workflow | The steps below |
| Knowledge | A2 output; `references/health-signals.md`; `references/outcome-measures.md`; `references/governance.md` |
| Tools | `verify.extract_claims` (counted) on any draft wording; `verify.qualify_source` then `verify.check_claim` (counted) only for a literature claim in the note; `analytics.rice` or `analytics.mcda` (counted) only for actions the person scored; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/value-note-and-next-action-output.md` |
| Input | The request and its context: the A2 read, the person's pass rule for a value note, named owners, the audience at the account, scores if ranking is wanted |
| Governance | `references/governance.md`; every note is a draft for the owner; nothing is sent by the model |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: trace or do not say

Every result in a note points to a signal row (account, measure, period, value). Every outcome result carries its denominator and the label that it is not clinical evidence. Words that state or imply effect ("improves", "reduces", "clinically proven", "saves"), a forecast, or a comparison with another product are not drafted; they stop for the person's owner.

## Workflow

### Step 1. Take the read

Use A2 from the conversation. If it is missing, run A2 in short mode first. If the account file is in the conversation, take each figure's numerator and denominator from it. Only when no file is in the conversation, say "described, not seen" and ask for the counts.

### Step 2. The pass rule for a value note

Ask the person when an account gets a value note rather than a next-action note (for example "meets my health rule" or "at least one outcome signal met with follow-up at or above my completeness target"). Write it back. Offer the register rule as an option the person may adopt: no value note to an account below every threshold. Without a pass rule, draft both views and let the person choose.

### Step 3. Draft the value note (accounts that pass)

For each result to show: the signal in the person's words, the value with numerator and denominator, the period, the row it comes from. Plain verbs: "activated", "were active", "had a follow-up score", "had a drop of 5 points or more on PHQ-9". Add one sentence on what the figure cannot show. Run `verify.extract_claims {text}` on the draft and check each claim against a signal row; split any sentence that joins a number with a forecast (observed in `references/tools.md`). If the person wants a published finding in the note, use `verify.qualify_source {doi}` then `verify.check_claim` with a passage you have read, and accept only a passage that states the finding in the same direction (register N3); otherwise leave it out.

### Step 4. Draft the next action (accounts that miss)

For each missed signal: the number against the target, the implementation signals beside it (CS32), and hypotheses for the miss, labeled, each with what would confirm it (for example "low active use may follow from onboarding reaching only part of the clinics; confirm from setting adoption, CS24"). Then actions from sourced practices, labeled "proposed": audit and feedback with the customer over a specified period (CS44), relay data close to real time (CS49), identify and prepare champions (CS46), ongoing or train-the-trainer training (CS45), staged scale-up (CS47). Training is the weakest control for use-related risk (CS77 to CS79): never propose training alone where a use error is suspected; route that to the owner the person names for product changes; if none is named, write "owner not named" and ask.

### Step 5. Rank only what the person scored

If the person wants an order, ask for Reach, Impact (0.25, 0.5, 1, 2 or 3), Confidence and Effort per action, then call `analytics.rice {initiatives}`. Pass confidence as a percent (80, not 0.8): the tool divides a fraction by 100 again (`references/tools.md`). Check the order by hand (Reach x Impact x Confidence / Effort). Report the person's own arithmetic. Never fill a score.

### Step 6. Owner and the forum that will see it

For each action, record the owner the person names and the forum and date they choose. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. No dates proposed by the model.

### Step 7. Stops

State what stops for the accountable owner: sending any note; any effect, cost or comparison wording (flag to the person's regulatory or legal owner; the Commercial pack's claims check can help but never clears); any outcome tied to payment (Market Access `outcomes-contract-monitoring`); any renewal or price position. When asked for such wording, draft only what the facts support and label it "draft for the owner".

## Build the output

Follow `assets/value-note-and-next-action-output.md`. Answer first: which accounts get a value note, which get a next action, and the one decision the person must take. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every result in a note points to a signal row; no number appears that is not in the account file.
- No effect, cost, forecast or comparison wording; the "not clinical evidence" label is in every note that shows an outcome figure.
- Hypotheses labeled; actions labeled "proposed"; owners and forums the person's.
- Every note is marked "draft for the owner"; nothing is sent.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Drafts for the person's owner; the model does not send, negotiate or promise.
- Whether notes already sent were backed is the monitoring sibling's value evidence check.
- Claims clearance, pricing and renewal terms, and payment-linked outcomes belong to other packs and owners.
