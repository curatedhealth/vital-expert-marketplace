# B1 Research action

Framework task: DH-02.04.3.1, Part B, task B1. Replaces the earlier "Research action" section (CF-12.02.04.3.1.3) and the one-line rules "take stops hit by more than one participant" and "name the release".

## What this task delivers

A research action log: for each stop that meets the person's rule for "repeated", and for every stop on a flagged critical task, a proposed design or content change or a refusal with a reason; the fix type in the sourced order (design, protective measure, information); a retest where the fix is wording or training; the owner and release the person names; a ranking only if the person scored the actions; and an insight log the monitoring sibling can trace. It answers "what do we change because of this research, and who owns it?"

Why it matters: research filed as insight with no action is the failure the register names. A log written in the same ids as the session record lets anyone check later that a shipped change came from a real stop, and that no stop sits only in a recording.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.04.3.1 Part B, Research action |
| Workflow | The steps below |
| Knowledge | A2 output; `references/session-evidence-and-sus.md` (From stops to actions); `references/formative-and-validation.md`; rows UX-US-32, UX-US-33, UX-US-42, UXR-03 |
| Tool | `analytics.rice` (counted, optional, only on the person's scores); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/research-action-output.md` |
| Input | The request and its context; A2 stops with counts; the person's rule for "repeated", critical-task flags, decisions, owners, releases and any scores |
| Governance | `references/governance.md`; actions, refusals, owners, releases and scores are the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## Read the request

- **Stops.** From A2 in the conversation, or the person's list with counts by group. If neither exists, run A2 first in short mode.
- **Rule for "repeated".** The person's. If none, offer the register starter rule ("more than one participant") as theirs to adopt, and until they adopt one list all stops with counts and no "repeated" label.
- **Decisions already taken.** Changes or refusals the team has agreed, with owners.
- **Scores.** Only if the person wants a ranking: reach, impact (0.25, 0.5, 1, 2 or 3), confidence (percent), effort, per action.
- **Mode.** Short for "what should we do"; full for an action log document.

## Workflow

### Step 1. Select the stops

Apply the person's rule. Add every stop on a task the owner flagged critical, whatever its count, because severity of harm weighs more than probability (UX-US-32). List the stops below the rule in one line so none disappears.

### Step 2. Action or refusal per stop

For each selected stop, write either a change (design or content) or a refusal with its reason, in the person's words where they gave them. Where the model suggests a change, label it "proposed" and tie it to the participants' words. Never write an action for a stop the record does not show.

### Step 3. Fix type and retest

Name the fix type in the sourced order: inherent safety by design, protective measure, information for safety (UX-US-33). If a proposed fix for a critical-task stop is wording or training only, say a retest is needed: FDA does not accept labeling or training as a mitigation without data showing it works (UX-US-42). Formative results do not carry to the final design (UXR-03), so a fix tested only in formative work is not validated.

### Step 4. Owner, release and date

Record the owner the person names, the release that will show an accepted change, and any date they set. Missing: "owner not named" or "not set", and ask. Never propose a date or a job title.

### Step 5. Ranking (only if scored)

If the person gave reach, impact, confidence and effort for each action, call `analytics.rice` with `initiatives: [{id, reach, impact, confidence, effort}]`. Pass confidence as a percent (80, not 0.8); the tool divides by 100 (`references/tools.md`). Check one score by hand (reach x impact x confidence/100 / effort) and report the order and scores. Critical-task stops are not ranked away: list them for the owner whatever their score. No scores: no ranking.

### Step 6. Write the insight log

Produce the log in the columns `scripts/research_log.py trace` reads: `insight_id, study_id, stop_id, participants_hit, raised_on, decision (action, refusal or open), decided_on, decision_ref, owner, release`. Open items stay "open". This is what the monitoring sibling checks.

### Step 7. Stops

State what goes to the accountable owner: critical-task stops and their fixes (human factors or regulatory owner); any claim that a fix made the product usable or safe; patient-facing wording that states or implies benefit. When asked for such wording, draft only what the facts support, labeled "draft for the owner".

## Build the output

Follow `assets/research-action-output.md`. Answer first: the stops that need a decision, the proposed change or refusal for each, and what goes to the owner. Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every selected stop has an action or a refusal, or is marked open; none is left only in a recording.
- Model suggestions are labeled "proposed"; decisions, owners, releases and scores are the person's.
- Critical-task stops are listed for the owner, not ranked away.
- Wording or training fixes for critical tasks carry a retest.
- The insight log uses the session ids.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checking later whether actions shipped and traced: `user-research-quality-monitoring`.
- Residual-risk acceptance and validation of a fix: the regulatory or human factors owner.
- Roadmap prioritization beyond research findings is the person's product process; this task ranks only research actions they scored.
