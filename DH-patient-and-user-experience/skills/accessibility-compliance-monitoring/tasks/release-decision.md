# B1 Release decision

Framework task: DH-02.04.1.2, Part B, task B1. Replaces the earlier "Access release decision" section and the one-line pass rule and owner sections.

## What this task delivers

A release decision record for one build, drafted for the person: their release rule (or the register starter rule, if they adopt it), the facts from A1 and A2 that the rule reads (open issues on day-one tasks, open issues on later screens, untested criteria), each exclusion with its basis, what the rule's outcome is on those facts, a ranked repair list from the person's own scores if asked, and the decision line left for the person. It answers "under our rule, can this build ship, with what exclusions, and what is repaired first?"

Why it matters: a release shipped with an open break on sign-in shuts people out of everything behind it. A rule written down before the decision, and applied the same way each time, keeps the call honest.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.04.1.2 Part B, Release decision |
| Workflow | The steps below |
| Knowledge | `references/release-rules.md`; A1 and A2 outputs; `references/obligation-map.md` |
| Tools | `analytics.rice` (counted, optional, to rank repairs the person scored); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/release-decision-output.md` |
| Input | The request and its context: the build, the access requirement, A1 sample and A2 log summary, the person's release rule and day-one definition, exclusions and their basis, scores if ranking is wanted, the accountable owner |
| Governance | `references/governance.md`; the rule and the decision are the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: the person's rule decides, the person decides

The model applies the person's rule to the facts and states what the rule says. It does not ship or block a build, does not invent a rule, and does not treat a national deadline as a release threshold. Without a rule, it reports the facts and offers the register starter rule (`references/release-rules.md`) for the person to adopt in their own words.

## Read the request

- **Build.** Which build or version.
- **Rule.** The person's release rule, verbatim. If none, offer the starter rule; apply it only if adopted.
- **Day-one tasks.** The person's definition. Without it, the starter rule cannot be applied.
- **Facts.** A1 and A2 outputs, or the log and records to run them.
- **Exclusions.** What the person will exclude and the basis.
- **Ranking.** Only if asked, with their RICE inputs.
- **Owner.** Who decides. If not named, "owner not named"; ask.
- **Issues without a criterion.** If an issue is described without a criterion, give the candidate criterion number and level from references/data/wcag_criteria.csv, labeled "candidate; your tester confirms" (for example, a button with no name read by a screen reader: 4.1.2 Name, Role, Value, Level A). Severity stays the person's.
- **Mode.** Short for a direct question; full for the decision record.

## Workflow

### Step 1. Write back rule and facts

The rule (theirs or the adopted starter rule), the day-one definition, the build, and the facts it reads: open in-target issues on day-one tasks and on later screens (A2), processes with a fail and criteria not tested (A1).

### Step 2. Apply the rule, clause by clause

For each clause, the facts it reads and what it says on them: for example "Clause 1 (block if a day-one task has an open break): 4 open in-target issues on day-one tasks (A11Y-04, A11Y-01, A11Y-03, A11Y-11); the rule says block." Where the rule does not decide a case (an untested criterion on a day-one task; an issue outside the target), say "your rule does not decide this; your call".

### Step 3. Exclusions

For each exclusion: the screen or content, the basis the person gives, and the row (`references/release-rules.md`), or "no sourced basis: your choice for this release". A burden determination is the owner's, in writing where the row says so (UX-US-14). The starter rule allows a later screen only with a named exclusion; a day-one task cannot be excluded under it.

### Step 4. Optional: rank repairs the person scored

Ask for reach, impact (0.25, 0.5, 1, 2 or 3), confidence as a percent (0 to 100) and effort per repair. Write them back. Call `analytics.rice {initiatives: [{id, reach, impact, confidence, effort}]}` with confidence as a percent (a fraction is silently divided by 100, `references/tools.md`). Show the order and scores as the result of their inputs, with day-one status beside each. If the order puts a later-screen repair ahead of a day-one one, state it; the person decides.

### Step 5. The record

Draft the decision record: build, date, rule, facts, clause outcomes, exclusions, ranked repairs, and the decision line "Decision: ______ (by the owner)". Owner as named, or "owner not named".

## Build the output

Follow `assets/release-decision-output.md`. Answer first: what the person's rule says on these facts, and the facts that drive it. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The rule is the person's or the starter rule they adopted, quoted.
- Each clause outcome cites the issues or records it read.
- Exclusions carry a basis and row, or say they have none.
- The decision line is left for the person; no "ship" or "block" written as decided.
- No statement that the release conforms.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Applies the person's rule; it does not set the access requirement (sibling skill B1) or test screens (A1 reads records).
- No legal conclusion on exceptions or burden; those are the owner's.
- Usability acceptance and human factors validation are UX 4.x and dh-regulatory-and-quality.
