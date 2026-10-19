# A Release scores and record dissent

Framework task: 6.1 Decision Facilitation.

## What this task delivers

Each scored stage released by a named person after every scorer submitted; dissent on the record, as text with each holder's name, or as "no dissent" attested by a named person.

Why it matters: private scoring only protects the room if scores stay hidden until everyone has scored and a person releases them. Dissent that silently goes missing is the averaging-away the Standard forbids (method.md D2, D3).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 6.1 |
| Knowledge | `references/method.md` (D2, D3) |
| Tools | `decide_release_scores`, `decide_record_dissent` |
| Template | Dissent section of `assets/decision-record.md` |
| Input | Scored stages; disagreement recorded in earlier reports |

## Workflow

1. **For each scored stage** (outcomes, options, capabilities, delivery risk), ask whether every scorer has submitted (question 2). If not, it stays unreleased; name who is missing.
2. **Release** (question 3): a named person, usually the facilitator or the owner. `decide_release_scores` with their name.
3. **Carry in dissent** from earlier reports (outcome priorities, options, readiness), each with its holder.
4. **Ask** (question 4) whether there is more. Each dissent is recorded in the holder's words with their name; if there is none, the owner attests "no dissent" (question 5). `decide_record_dissent`.

## Boundaries

- Never release, write dissent, or attest none yourself.
- Never summarize dissent into a consensus line. Keep the holder's words, or the wording given when relayed, with their name; add nothing (no comparison, no reason they did not give).

## When you are unsure

If a dissent holder is absent, record "relayed by [name]" and note that the holder should confirm before Gate 3.
