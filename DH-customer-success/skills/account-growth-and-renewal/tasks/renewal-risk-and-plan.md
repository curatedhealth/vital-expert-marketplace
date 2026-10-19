# B1 Renewal risk note and plan

Framework task: DH-02.02.2.1, Part B, task B1. Replaces the earlier "Renewal risk note" section (CF-12.02.02.2.1.3) and the old one-line pass rule and owner sections.

## What this task delivers

For each account the person's rule marks as at risk: the reason as the account record shows it, hypotheses labeled with what would confirm them, the actions that respond (labeled proposed), the owner the person names for each, the actions ranked only if the person scored them, the points that stop for an owner, and the steps the contract requires if the account does not renew. It answers "which accounts may not renew, why, and what do we do before the renewal date?"

Why it matters: reasons differ in what responds to them. A loss on an open implementation needs the implementation finished; a loss on price needs the pricing owner; a "value unseen" may be an implementation not yet complete (CS32 [PAPER], DOI 10.1007/s10488-010-0319-7). A concession offered to save a renewal is itself an offer element with its own rules (`offer-rules.md`).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.02.2.1 Part B, Renewal risk note and plan |
| Workflow | The steps below |
| Knowledge | A1 output; `references/renewal-facts.md`; `references/offer-rules.md`; `references/starter-rules.md` (SR9 to SR11) |
| Tools | `analytics.mcda` or `analytics.rice` (counted, only on the person's scores); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/renewal-risk-and-plan-output.md` |
| Input | The request and its context: the accounts in the window (A1), the person's risk rule, the account record (implementation status, agreed outcomes and what was seen, sponsor and champion changes, price feedback, usage), actions the person is weighing, their criteria, weights and scores, owners |
| Governance | `references/governance.md`; people score, the connector ranks, the owner decides |
| Catalogue job | none for renewal actions. `partner-prioritization` runs the same mcda and rice tools but is framed for partners and indications; the direct `analytics.mcda` or `analytics.rice` call on the person's scores remains the method. |

## The rule that shapes this task: risk is the person's rule, applied to the record

No source defines renewal risk or customer health. The person states the rule (for example "at risk if go-live missed or sponsor left"). If they have none, offer SR9 (reasons: value unseen, champion gone, price, implementation open) and SR11 (an unexpired contract is not evidence of health), labeled "register starter rule, yours to adopt". Without a rule, list the facts per account and give no verdict. Never score an account, never fill a missing score for an action, and never call an action "recommended".

## Read the request

- **Accounts.** From A1, or the person's list.
- **Risk rule.** Ask once; offer SR9 and SR11 as above.
- **Reasons and evidence.** What the record shows per account: implementation status, outcomes agreed and seen, sponsor or champion change, price objection in writing, usage against an agreed profile (CS61).
- **Actions and scores.** The actions the person is weighing; criteria phrased so higher is better; weights summing to 1; scores 0 to 4.
- **Owners.** One per action, as the person names them.
- **Mode.** Short for "which accounts are at risk"; full for a renewal plan.

## Workflow

### Step 1. Apply the person's rule

For each account, apply the rule to the record and write the verdict with the fact that triggered it ("at risk on your rule: go-live not recorded, renewal 15 December 2026"). Accounts the rule does not catch are listed as "not caught by your rule", never as "healthy" (SR11).

### Step 2. State the reason from the record

One reason per line, in the record's words, with its source in the account file. Keep the reasons apart: never merge price with open implementation (SR17 in the sibling's terms), never merge "value unseen" with "implementation open" (CS32). Where the record does not say, write "reason not recorded `[GAP]`".

### Step 3. Hypotheses, labeled

Where the person asks why, offer at most three hypotheses per account, each labeled "hypothesis" with what would confirm it. Examples: "Hypothesis: users were not trained to the workflow validated; confirm with the training records against the validated training (CS80)." "Hypothesis: the expected usage profile was never agreed; confirm with the commissioning file (CS61)."

### Step 4. Actions, labeled proposed

For each reason, list the actions the person named, and add others only as "proposed". For each action, state which reason it responds to and any stop it triggers:

- A price concession, credit, free module or service, extended trial or anything for patients: an offer element; run it through `references/offer-rules.md` and stop for the compliance owner. The price itself is the pricing owner's.
- A bridge term, early renewal or changed terms: the legal owner.
- A results guarantee or price tied to outcomes: CP-US-11 to CP-US-14 and CP-US-13; Market Access (`outcomes-based-contracting`).
- A non-renewal: the PHI return or destroy step (CS100) and the EU delete-or-return choice (CS109), with the owner the person names.

### Step 5. Rank only what the person scored

If the person gives scores and weights, call `analytics.mcda` with `alternatives` (id and scores) and `criteria_weights`. Report each action's value and its contributions, and say plainly when two values tie (the connector does not). With two or three criteria, also state, from the person's own scores, the weight on the first criterion at which the top-ranked action changes, labeled 'arithmetic on your scores, not a recommendation'. If the person scores by reach, impact, confidence and effort, `analytics.rice` is the alternative. Without scores, no ranking: lay out the facts per action and ask.

### Step 6. Owners and sequence

Name the owner the person gave for each action, or "owner not named" and ask. Sequence by dependency (for example "the implementation items close before a growth offer, if your rule SR3 holds"), never by urgency. The renewal date is a fact.

## Build the output

Follow `assets/renewal-risk-and-plan-output.md`. Answer first: which accounts are at risk on the person's rule, the recorded reason for each, and the first action in the dependency chain. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every verdict comes from the person's rule; no account is called healthy.
- Reasons come from the record; causes are hypotheses, labeled.
- Every action not named by the person is labeled "proposed"; every score and weight is the person's.
- Concessions are routed through `offer-rules.md` and stop for the compliance owner.
- No urgency language.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Risk notes and plans for named accounts. Renewal and retention rates across a cohort are the sibling skill (`expansion-and-renewal-monitoring`).
- Customer health scoring and value realization are the Customer Health skills (`outcome-tracking-and-customer-health`, `value-realization-monitoring`).
- No price, no contract wording, no legal opinion.
