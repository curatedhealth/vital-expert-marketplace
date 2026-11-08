# Facilitation: cut-the-slop

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
See `method.md` and tasks under `cut-the-slop/tasks/`.

## C6 turn sequence (C6 Phase 1, 8 November 2026)

Progress marker: Step n of 7. Open with the first question in three sentences or fewer; do not show a table before the owner has answered.

| Step | Question to ask (one per turn) | Record in |
|---|---|---|
| 1 | Who will read this text, and what do they need from it? | worksheet row 1 or earlier answer |
| 2 | Can you paste the original passage exactly as it stands? | worksheet row 2 or earlier answer |
| 3 | Which sentences do you think the reader can do without? | worksheet row 3 or earlier answer |
| 4 | Who acts in each sentence, and where does the name come from? | worksheet row 4 or earlier answer |
| 5 | Which qualifiers, limits or dissent in the original must stay? | worksheet row 5 or earlier answer |
| 6 | Does any figure remain, and what should the reader do about it? | worksheet row 6 or earlier answer |
| 7 | Does the owner accept the cuts, with the repair log attached? | worksheet row 7 or earlier answer |

Refusals stay short: will not score, choose, sign or invent; say what you will do instead; ask one next question. When the owner says "just fill it in", leave `[GAP]`.

After the last step run `scripts/substance_check.py` on the JSON built from the answers and read back its gaps unchanged.

## C7 facilitation absorb (8 November 2026)

Lane A practice inserts only. No new skills, CF codes, formulas, scoring, sibling gates, parallel seals, or WR-C6-032 thresholds. Decision Room timing is owner adaptation, not a validated optimum (`diligence/c7-exports-2026-11-08/facilitation/decision_room_agenda.md`). Source findings: WR-C7-006, WR-C7-010, WR-C7-021.

### Facilitation inserts
- Ask each sentence’s decision purpose.
- Compare before/after caveats, sources, and dissent.
- No new actor/fact or meaning loss for brevity.

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
