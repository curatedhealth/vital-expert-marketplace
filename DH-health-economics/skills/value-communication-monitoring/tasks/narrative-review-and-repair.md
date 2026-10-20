# B1 Narrative review and repair

Framework task: DH-01.07.4.2, Part B, task B1. Replaces the old "Narrative repair" task and absorbs the old pass rule and owner steps.

## What this task delivers

A review against the person's own rules: for each line of the narrative or dossier, the reception result (A1), the currency result (A2), pass or miss by the person's rule, the cause class, the owner the person names, and a proposed repair drafted for that owner. Plus what the review does not show.

Why it matters: a line can fail because the evidence moved, because the line overstated it, because it answered a question the audience did not ask, or because a rule was crossed. Each cause has a different repair, and only some of them are a communication problem.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.4.2 Part B, Narrative review and repair |
| Workflow | The steps below |
| Knowledge | `references/reception-measures.md`; `references/currency-signals.md`; `references/certainty-and-wording.md`; A1 and A2 outputs |
| Tool | Through A2 only (`verify.*`, `literature.*`); `verify.build_record` when cleared; `analytics.mcda` or `analytics.rice` only if the person scores repair options |
| Prompt | This guide |
| Template | `assets/repair-review-output.md` |
| Input | The person's pass rules (in their words), the lines the person says failed, the owners, A1 and A2 results |
| Governance | `references/governance.md`; every repaired line stops for the owner the person names for regulatory or legal review, or owner not named |
| Catalogue job | None |

## Read the request

- **Pass rules.** The person's, in their words (for example "a line passes if fewer than half the payers who saw it questioned or rejected it, with at least three responses"). Example rules like this are illustrations, not sourced thresholds. If none, ask; without rules, report results only.
- **Failed lines.** Old rule: name the line the person said failed. If the person names lines, start with those; add lines A1 or A2 flagged, labeled as such.
- **Owners.** The person's. "Owner not named" otherwise.

## Workflow

### Step 1. Results against the rules

Lay out each line with its A1 result (on the person's measure, with base) and A2 status. Apply the person's rule: pass, miss, or "not assessable" (below base, no rule).

### Step 2. Cause class per missed line

Pick the class the facts support, and say which fact:

1. **Evidence moved:** A2 shows retraction, correction, a passage that no longer matches, or candidate new studies.
2. **Line overstated its source:** wider population, conclusion words, a held claim in use (`references/certainty-and-wording.md`).
3. **Audience expected something else:** the notes ask for something a source speaks to (budget impact on own population HE-021, [PAPER] DOI 10.1016/j.jval.2013.08.2291, PMPM HE-138, UK costs HE-089, cost-effectiveness for higher financial risk HE-090) and the dossier did not supply it.
4. **Rule crossed or guidance moved:** a PC row the line crosses, or a currency signal (PC-US-47, HE-131).
5. **Not a communication issue:** price, coverage or contract terms (dh-market-access or dh-commercial). Say so and route.

If the facts do not separate the classes, say "cause not established" and name what would settle it.

### Step 3. Propose the repair

Per missed line, a repair that stays inside the evidence: narrow the claim to its passage, add the limitation or the required context (PC-US-40), supply the element the audience asked for if the person has it, or drop the line. A repair never adds a claim without a passage; a new claim goes to value-narrative-and-dossier A1. Label every repair "proposed" and "draft for the owner". For an uncleared use already shared with payors, note the follow-up duty when materially outdated (PC-US-46).

### Step 4. Owners and decisions

Per line, the owner the person named or "owner not named". List decisions: accept or reject each repair, update the dossier version, follow up with stakeholders. If the person scores repair options and wants a rank, run `analytics.mcda` or `analytics.rice` on their scores only.

### Step 5. What the review does not show

Lines with too few responses, codes the person has not defined, objections whose cause is not established, and that reception is not evidence about the product.

## Build the output

Follow `assets/repair-review-output.md`. Answer first: lines passing, lines missing, the main cause, the proposed repairs.

## Before you hand it over

- Every pass or miss uses the person's rule; no model threshold.
- Every repair is narrower or better supported than the line it replaces, labeled proposed and draft for the owner.
- No judgment of people or stakeholders.
- Count the words in short mode; record line.

## Boundaries

- The skill never clears a repaired line or says it complies.
- Rewriting the whole narrative or dossier: value-narrative-and-dossier. Price, coverage and contracts: dh-market-access or dh-commercial.
