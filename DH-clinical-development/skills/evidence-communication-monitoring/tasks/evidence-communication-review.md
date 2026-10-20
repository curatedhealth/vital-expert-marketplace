# B1 Evidence communication review

Framework task: DH-01.02.2.2, Part B, task B1. Replaces the old "evidence communication pass rule" and "evidence communication miss owner" sections and the "did the message land" half of "Message Impact Monitoring".

## What this task delivers

A review draft that says, against rules the person set before looking at the results: whether disclosure clocks are being met (from A1), whether live communications stay faithful (from A2), and, where the person tracks it, whether the communications reached the audiences meant; for each miss, the owner the person named, whether it is a one-off or a pattern, and the work that responds.

Why it matters: without written rules, every review reopens what "good" means. A late posting can be one forgotten trial or a process with no owner; a drifted statement can be one slide or a template copied into every deck. The review separates them and names who decides.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Bound: `cybersecurity-architect-digital-health` (binding under owner review; see SKILL.md) |
| Skill | DH-01.02.2.2 Part B, Evidence communication review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/fidelity-checks.md`; `references/disclosure-rules.md` |
| Tools | A1's and A2's tools if either is missing; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/communication-review-output.md` |
| Input | The request and its context; the person's pass rules, thresholds and named owners; A1 and A2 results; any reach or response data the person tracks |
| Governance | `references/governance.md`; people set rules and name owners |
| Catalogue job | none. Rules, thresholds and owners are the person's. |

## The rule that shapes this task: people judge

The person writes the pass rules, in their words and numbers, and names the owner of each. The model checks results against those rules, separates one-offs from patterns, and lays out options. It never sets a threshold, never decides what counts as a miss, never names an owner the person has not named, and never judges a person or a team. If asked to propose rules, it may, each marked "proposed" with the fact behind it, and does not apply them until the person confirms. Reach and response measures are not sourced; they are the person's, and never evidence of clinical effect.

## Workflow

### Step 1. Gather the evidence

Use A1 (disclosure table) and A2 (fidelity audit). If either is missing and needed, run it first in short mode. A review on one half says the other was not reviewed.

### Step 2. Write the pass rules with the person

Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Disclosure on time | "No results clock past due for a trial we confirmed is covered" | A1 statuses |
| Registration | "Every trial registered before first consent" | A1 ICMJE test |
| Fidelity | "No Stop flag live in any communication" | A2 flags |
| Certainty | "Every certainty word matches the team's rating" | A2 drift 5 |
| Reach or response | The person's measure and data source | The person's data |

Write the rules back for confirmation before checking anything. A rule without a number or a clear test is a summary, not a verdict.

### Step 3. Check each rule

Mark each rule met, missed or not measurable `[GAP]`, with the number behind it and its as-of date.

### Step 4. One-off or pattern?

For each miss, lay out both readings with the facts that favor each, without choosing: the same drift in several communications, or several late postings with no owner named for the registry, points toward a process or template; a single instance points toward the item. Reach results the person tracks are reported against their rule; any cause is a hypothesis, with what would confirm it.

### Step 5. Route the response

| Miss | Responding work |
|---|---|
| Results clock past due or registration late | The person responsible for the registry; the disclosure plan (evidence-translation-and-communication, task A2) |
| Statement drifted from its passage or rating | The owner the person names for regulatory or legal review, or owner not named; the evidence statement (sibling skill, task A1) and audience narrative (task B1) |
| Retracted or corrected source in use | The owner the person names for regulatory or legal review and for the source, or owner not named; the evidence statement rebuilt |
| Marketing claim or ad | dh-go-to-market (pricing-and-value-message-monitoring), marketing claims |
| Payer submission or HTA dossier wording | dh-access-and-value (payer-engagement-and-hta-submission), payer routes, submissions, prices |

Name the owner the person gave. If none, write "owner not named" and ask.

## Build the output

Follow `assets/communication-review-output.md`. Short mode: verdict per rule, the one-off-or-pattern reading for the main miss, owners, the one decision needed.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the number behind it and its date.
- Causes are hypotheses, labeled; no verdict on people or teams.
- Count the words in short mode.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No forecast of disclosure or reach results.
- No clearance of any communication.
- No reach or response figure presented as clinical evidence.
