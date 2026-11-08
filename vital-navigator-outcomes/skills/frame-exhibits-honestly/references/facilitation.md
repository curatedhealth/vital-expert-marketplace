# Facilitation: frame-exhibits-honestly

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
See `method.md` and tasks under `frame-exhibits-honestly/tasks/`.

## C6 turn sequence (C6 Phase 1, 8 November 2026)

Progress marker: Step n of 9. Open with the first question in three sentences or fewer; do not show a table before the owner has answered.

| Step | Question to ask (one per turn) | Record in |
|---|---|---|
| 1 | Which supplied exhibit are we framing, and who is the named model owner? | worksheet row 1 or earlier answer |
| 2 | What kind of chart is it, and what are the axis minimum and maximum as drawn? | worksheet row 2 or earlier answer |
| 3 | If a bar chart does not start at zero, what is the reason in plain words? | worksheet row 3 or earlier answer |
| 4 | Will readers compare panels, and do those panels share one scale? | worksheet row 4 or earlier answer |
| 5 | Did the team supply an interval, and if so how was it computed? | worksheet row 5 or earlier answer |
| 6 | Is any relative change shown without the absolute change beside it? | worksheet row 6 or earlier answer |
| 7 | If something is compared with something else, what are the denominator and the period? | worksheet row 7 or earlier answer |
| 8 | Does the title say more than the data show? | worksheet row 8 or earlier answer |
| 9 | If this cannot be shown fairly, shall we withhold it and record why? | worksheet row 9 or earlier answer |

Refusals stay short: will not score, choose, sign or invent; say what you will do instead; ask one next question. When the owner says "just fill it in", leave `[GAP]`.

After the last step run `scripts/chart_scale.py` on the JSON built from the answers and read back its gaps unchanged.

## C7 facilitation absorb (8 November 2026)

Lane A practice inserts only. No new skills, CF codes, formulas, scoring, sibling gates, parallel seals, or WR-C6-032 thresholds. Decision Room timing is owner adaptation, not a validated optimum (`diligence/c7-exports-2026-11-08/facilitation/decision_room_agenda.md`). Source findings: WR-C7-006, WR-C7-010, WR-C7-021.

### Facilitation inserts
- Ask comparator/period/range meaning.
- Challenge framing without invented effects.
- Material discussion edits need current revision integrity review.

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
