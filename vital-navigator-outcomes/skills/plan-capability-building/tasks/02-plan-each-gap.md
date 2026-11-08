# Task: 02-plan-each-gap

Input: team-entered facts for this step; upstream skill outputs listed at intake; connector availability.
Atom: compose-draft
Tool: offline script if present
Template: templates/worksheet.md
Output: step output
Check: no invented numbers; [GAP] listed; autonomy respected
Human: named decision owner

## Steps
1. Restate what is known and what is [GAP].
2. Run the offline tool if listed; otherwise draft from templates only.
3. Present options or draft to the named human; stop for human-only gates.

## Body

# A Plan each top gap

Framework task: 4.2 Capability Build Planning, Part A.

## What this task delivers

For each top gap in the register: the action that closes it, in the person's words; the owning role; the level it aims for (the register's Required score unless the person says otherwise, with a reason); and a check date.

Why it matters: a gap register with no owners is a list of worries. Each top gap needs someone accountable and a date on which closing it is checked (method.md X11).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Outcome Decision Lead |
| Skill | 4.2, Part A |
| Workflow | The steps below |
| Knowledge | `references/method.md` (X2, X11) |
| Tools | `scripts/build_plan_check.py` |
| Template | "Build plan" section of the report |
| Input | The strategic gap register |
| Governance | `references/governance.md` |

## Workflow

1. **Show the top gaps** (three by default, or as the owner sets) with the outcomes they hold back.
2. **For each, ask what will close it** (question 2), in turn. If the person asks for options, list kinds of action in one line (develop people, hire, partner, buy a service, change a process) without recommending one.
3. **Owner and check date** (questions 3, 4): a role and a month.
4. **Aim**: the register's Required score, recorded as "default" when the person states none (not a gap). If the person aims lower or higher, record why.
5. **Check** with `scripts/build_plan_check.py`. C4: it refuses plans with an unknown gap, a maturity percentage, attendance-only acceptance, an unevidenced overseer, a prerequisite cycle, or scale dated before acceptance.

## Boundaries

- No maturity levels, no vendor names from you, no individuals.
- A "buy a service" action names a service type, not a vendor, unless the person names one (theirs, O).

## When you are unsure

If a gap seems to need two different actions (for example hire and change a process), record both under one gap with one owner.
