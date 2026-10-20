# B1 Review and follow-up

Framework task: DH-02.04.2.2, Part B, task B1. Replaces the register task "System follow-up" (CF-12.02.04.2.2.3) and the one-line pass rule and miss owner of the register.

## What this task delivers

A review draft that checks the A1 counts and A2 breaches against the rules the person sets, lays out for each miss whether the person fixes it in the contract or in the surface, records the owner they name and the version that should contain the fix, and ranks the follow-ups only on the person's scores. It answers "which results miss our rules, does the contract or the surface change, who owns the fix and in which version?"

Why it matters: without rules written before the numbers, every review reopens what "good" means. The register rules: name the owner, state whether the contract or the surface changes, name the version that should contain the fix, and never update the contract silently to match a breach.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | UX/UI Designer, Digital Health (`ux-ui-designer-digital-health`) |
| Skill | DH-02.04.2.2 Part B, Review and follow-up |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/indicators.md`; `references/governance-models.md`; `references/component-requirements.md` section 5 for device surfaces |
| Tools | `analytics.rice` or `analytics.mcda` (counted, only on the person's scores); `regulatory-dh.search_safety_events` (counted, optional, device surfaces only); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/review-and-follow-up-output.md` |
| Input | The request and its context; the person's rules, scores and named owners; A1 counts and A2 breaches |
| Governance | `references/governance.md`; people set rules, choose contract or surface, score, and name owners and versions |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. The post-market-watch job also reads safety events but sets a watch; it is not called. |

## The rule that shapes this task: people decide, the contract is not rewritten to fit a breach

The person writes the rules, decides for each miss whether the contract or the surface changes, scores the follow-ups and names the owner and the target version. The model checks results against the rules, lays out the facts for each choice, ranks only what was scored, and labels any suggestion "proposed". Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

## Workflow

### Step 1. Gather the evidence

Use A1 and A2 from the conversation. If either is missing and needed, run it first in short mode. A review on one of them says what was not reviewed.

### Step 2. Write the rules with the person

For each indicator in scope, ask for a rule with a number or a condition. Offer this shape, filled with the person's words:

| Rule type | Example shape (their words and numbers) | Checked against |
|---|---|---|
| Drift on clinical surfaces | "No clinical or device surface behind the current version of a component" | A1 by owner |
| Forks | "No fork of a component used on a device surface without a named owner of the port" | A1 modification |
| Lifecycle | "No component marked use with caution on a clinical surface" | A1 lifecycle |
| Accessibility status | "Every component version on a clinical surface tested against our target since its last change" | A1 status |
| Contract | "No open breach of a contract on a clinical surface" | A2 |
| Concerns | "Time to resolution of an evidenced concern" as GOV.UK measures it (DSX-48), with their own number | Issue log |

Write the rules back for confirmation. An indicator without a rule gets a factual summary and no verdict. Public practice is labeled as such: GOV.UK's 3-month rule is for community resources (DSX-16); its 6-month measurement cadence is its own (DSX-49).

### Step 3. Check each rule

Mark each rule met, missed, or not measurable `[GAP]`, with the number or the evidence behind it. Never average components or products into one score.

### Step 4. Hypotheses, not causes

For each miss, list possible reasons as hypotheses, each with what would confirm it. Draw them from mechanisms the rows state: a product behind on a forked component may never have received the fix (DSX-33; confirm from the modification record); an override may have broken on update (DSX-31; confirm from the product's change history); a component still in use after the system marked it for caution (DSX-28; confirm whether the team knew of the status change). Never state a cause the data does not show; never judge a team.

### Step 5. Contract or surface, owner and version

For each miss or breach, lay out the facts for each side: what changing the surface involves (products affected, from A1) and what changing the contract would change for every other product using it. The person chooses. If the person wants to change the contract, the change is a new contract version made in the development skill with its own change note (A2 there), and the output says the contract is not being changed silently. Record the owner and the version that should contain the fix, as the person names them; if missing, "owner not named" or "version not set", and ask. No dates proposed by the model.

### Step 6. Rank follow-ups (only on the person's scores)

If the person wants a ranking, ask for RICE inputs (reach, impact 0.25, 0.5, 1, 2 or 3, confidence as a whole percent, effort) and call `analytics.rice` (confidence as 80, not 0.8; check each score, `references/tools.md`), or criteria, weights and 0 to 4 scores for `analytics.mcda`. Report the order and scores. Never fill a score.

### Step 7. Device surfaces

For misses on a device user interface: any fix that changes the component is a design change with the questions in `component-requirements.md` section 5 for the person's quality and regulatory owners (QS34, CH9, UX-US-49). Optional field context with `regulatory-dh.search_safety_events` on the person's own or a named partner's manufacturer, reported only as the records state.

### Step 8. Stops

State what stops for the accountable owner: release of a fix into a regulated interface; any statement that a product or the system is accessible or compliant; clinical content; device significance or submission questions. When asked for such wording, draft only what the facts support and label it "draft for the owner".

## Build the output

Follow `assets/review-and-follow-up-output.md`. Answer first: which rules are missed (clinical and device first), the follow-up with its owner and target version, and the one decision needed from the person. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, score, owner, version and the contract-or-surface choice is the person's, and the output says so.
- Every verdict cites the number or evidence behind it.
- Causes are hypotheses, labeled, with what would confirm them.
- No silent contract change; no averaging; no judgment of teams.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not decide fixes, release versions or assess clinical content.
- Writing the new contract version is the development skill; product conformance is DH-02.04.1.x; usability evidence is DH-02.04.4.x; device decisions are dh-regulatory-and-quality.
