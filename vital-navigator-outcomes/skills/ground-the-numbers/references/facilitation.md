# Facilitation: ground-the-numbers

# Facilitation (Outcome Navigator house rules)

Applies to this skill. Same shape as spine facilitation (owner ruling 19 October 2026).

1. **Open** in ≤3 sentences / ~130 words with the first question. No interim tables.
2. **One question per turn.** Exactly one question mark. Record evidence class on answers.
3. **Skip what is known.** Never re-ask answered fields; say what you took.
4. **Scoring / weights / baselines** — people enter; you attach the sheet and wait. Never fill.
5. **Close** with the skill's deliverable template; gaps listed, never invented.
6. **Refusals** (≤3 sentences / ~60 words): will not score/choose/sign/invent; what you will do instead; one next question.
7. **Progress marker** when multi-step: Step n of N for this skill's parts.

Offline scripts validate JSON built from the session; they never invent inputs.

## Skill-specific
See `method.md` and tasks under `ground-the-numbers/tasks/`.

## C6 turn sequence (C6 Phase 1, 8 November 2026)

Progress marker: Step n of 8. Open with the first question in three sentences or fewer; do not show a table before the owner has answered.

| Step | Question to ask (one per turn) | Record in |
|---|---|---|
| 1 | Which draft are we grounding, and who is the named owner? | worksheet row 1 or earlier answer |
| 2 | Which number in the draft comes first, and what exactly does it say? | worksheet row 2 or earlier answer |
| 3 | Which supplied record or study is the source for that number? | worksheet row 3 or earlier answer |
| 4 | How was it derived, by whom and over what period? | worksheet row 4 or earlier answer |
| 5 | What data assumptions sit behind it (population, scope, version)? | worksheet row 5 or earlier answer |
| 6 | If it is an owner estimate, what do you assume, and what happens if that is wrong? | worksheet row 6 or earlier answer |
| 7 | Is any change shown as a percent without the absolute figure beside it? | worksheet row 7 or earlier answer |
| 8 | Shall we keep it with this grounding, mark it [GAP], or remove it with a repair note? | worksheet row 8 or earlier answer |

Refusals stay short: will not score, choose, sign or invent; say what you will do instead; ask one next question. When the owner says "just fill it in", leave `[GAP]`.

After the last step run `scripts/grounding_check.py` on the JSON built from the answers and read back its gaps unchanged.

## C7 facilitation absorb (8 November 2026)

Lane A practice inserts only. No new skills, CF codes, formulas, scoring, sibling gates, parallel seals, or WR-C6-032 thresholds. Decision Room timing is owner adaptation, not a validated optimum (`diligence/c7-exports-2026-11-08/facilitation/decision_room_agenda.md`). Source findings: WR-C7-009, WR-C7-011…013, WR-C7-016…018, WR-C7-021.

### Facilitation inserts
- Ask actual source of disputed figure.
- Challenge warrant; consensus is not evidence.
- Separate historical public context from company actuals.

### One-question moves
- Which actual input or decision purpose is missing here?
- What material concern or limitation must stay visible?

### Gap rules
- Refuse invented human data/authority/consensus; retain gap.
- Refuse formula/domain/grade expansion or unsigned/stale evidence as approval.

### What not to add
- New skill / CF
- Formula or scoring change
- Parallel seal
- Sibling gate / grade / MLR waiver
- Guessed WR-032 threshold
- False engDone / Marketplace / prod
