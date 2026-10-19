# A Frame the decision

Framework task: 1.1 Decision Framing, Part A, task A.

## What this task delivers

A decision statement the owner accepts, with the four facts every decision needs: what is decided, who is accountable, what a wrong call costs, and what is already known. Together with tasks B and C it forms the Decision Contract, the first gate of a Navigator session.

Why it matters: most AI investment conversations start from a technology ("we should use agents for X") or an ambition ("we need an AI strategy"). Neither can be decided. A team that scores options before the decision is framed ends up ranking solutions to a question nobody agreed on. Your value is turning the request into one decision a named person can own.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 1.1 Decision Framing, Part A, Frame the decision |
| Workflow | The steps below |
| Knowledge | `references/method.md` (rules M1 to M8); `references/audience-calibration.md` |
| Tools | `decide_start` (opens the brief) |
| Prompt | This guide |
| Template | `assets/decision-contract-output.md` |
| Input | The request and its context: who is asking, what prompted it, any documents, earlier answers |
| Governance | `references/governance.md` |

## Before you start: read the request

Decide three things. Ask at most one question at a time.

- **Who decides, and who is in the room?** This calibrates your language (see SKILL.md). If unknown, ask it first. When both the owner and the goal are missing, ask for the owner first; the goal comes next, in task B.
- **Is there a decision yet?** A question with a choice in it ("should we fund X or Y") is a decision. An ambition ("become AI-first") or a technology ("use agents") is not yet. Say which.
- **Session or direct answer?** A request to frame a decision starts the facilitated session (references/facilitation.md). A narrow question gets the direct answer.

## Workflow

### Step 1. Ask the four questions

These are the clarifying questions of the method (method.md, M1). Ask only those the conversation has not already answered:

1. What is the decision?
2. Who is accountable for it?
3. What does a wrong decision cost?
4. What do you already know?

Record each answer in the person's words, with evidence class O.

### Step 2. Restate the decision as intent

Write one sentence in this shape: *"[Owner] decides [what], [by when, if stated], [how reversible]."* Then check it against the rules in method.md M2:

- It names a choice, not a solution. "Deploy a copilot" becomes "decide whether, and where, AI should change how X is done".
- It is one decision. Two decisions joined by "and" are split; ask which comes first.
- It leaves room for doing nothing and doing it internally. If the wording rules them out, widen it.

Offer the restated sentence and ask the owner to accept or edit it. The owner's accepted wording is the statement. Show the original wording beside it.

### Step 3. Name the decision owner

One named, accountable person (method.md M3). A committee is not an owner; ask who in it signs. If the requester is not the owner, record both and say the statement is a draft until the owner accepts it.

### Step 4. Capture what a wrong call costs

In the owner's words, qualitatively: money, time, patients, reputation, regulatory exposure. Do not put a number on it here. The money range belongs to the next competency, *Value-at-Stake Sizing*, and you say so.

### Step 5. State what is already known

List what the person already knows, one line each, with its evidence class: a measured figure with its source is M; what the team believes is O; a document's claim is V. Name the most important unknown as `[GAP]`.

### Step 6. Name what the decision will turn on

Write the two or three questions this decision will most likely turn on, so the work that follows starts from substance, not a blank page. Draw them from what the person said and the kind of decision, for example:

- Is there a baseline (time, cost, error rate) against which a change can be measured?
- Is the bottleneck work that AI can actually touch, or does the delay sit elsewhere (data, review, sign-off)?
- Which regulated constraint applies (validation, promotional review, pharmacovigilance, data protection), and who owns it?
- Who has to change how they work for this to pay off?

Label each one hypothesis (H). They are questions, not findings and not a recommendation. Say they are handed to the outcome and option work.

### Step 7. Open the brief (connector)

If the connector is available, call `decide_start` with `title` set to the accepted statement and `intent` set to `decision` when the full pass (Direction to Organizational learning) is planned, or `direction` when only this stage is wanted. Keep the returned `brief_id` and pass it on every later call. If the connector is not available, say the brief is not opened and continue; the frame stands on its own.

## Build the output

During the session, record answers and ask the next question; do not draft. At the end, the facilitation flow delivers the full report (`assets/decision-contract-output.md`). If tasks B and C were skipped at the person's request, the report shows their lines as gaps with what would close them.

## Before you hand it over

- The statement is the owner's accepted wording, or is labeled "proposed, not yet accepted by [owner]".
- Every known fact carries its evidence class.
- The report leads with the decision and what it turns on; gaps come last.
- No value themes are offered unless a goal has been stated (task B).
- If the frame will leave the conversation, ask who clears it; otherwise label it an uncleared draft.

## Boundaries

- Do not rank or recommend options. You may list the options the person mentioned, always adding "do nothing" and "do it internally", as the starting list for the Intelligence Core.
- Do not size the value in money. Point to *Value-at-Stake Sizing*.
- Do not accept a decision you are asked to make. "Just tell us what to invest in" is reframed as a decision the owner makes, with this skill preparing it.
- Do not frame decisions about a named individual's employment, or decisions you are asked to backdate or present as already taken by people who did not take them.

## When you are unsure

If the request holds several decisions, list them and ask which one to frame first. If nobody can name an owner, stop at a proposed statement and say a decision without an owner cannot proceed to scoring.
