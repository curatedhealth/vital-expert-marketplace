# Tools and companion slot

## Companion slot

No companion exists for this skill at launch. Both tasks run fully as method from the
supplied material. This skill never calls VERIFY or any other connector.

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Fair balance | Read the approved label or the full safety tables for the product and market, and list the risks, warnings and discontinuation figures a piece about that benefit would normally carry, for the medical reviewer to choose from | None yet. Candidates in the product concept: an MLR preparation companion and a label source companion. Neither exists. | Method runs from what was supplied; missing risk data marked `[GAP: not supplied — …]`; check line says "not tool-checked" |
| Selective reporting | List every registered study of the product for the use, and every registered primary and secondary outcome and time point, so the draft can be compared with the whole set and not only with what was supplied | None yet. `[CHECK]`: a trial registry or literature companion is not in the concept's candidate list; for the owner to decide. | Method compares the draft with the supplied material only; whether other studies exist is asked, never assumed, and marked `[GAP: not checkable here — …]` |

What VERIFY does not do here: VERIFY tests whether a sentence is supported by a supplied
passage (through `claim-assessment`). It does not test whether a passage that should be
in the draft was left out. A draft can score well on support and still omit every
side effect. Do not present a VERIFY result as evidence of balance (TR-H4).

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `balance_cues`

List balance cues in a draft, and what the source material holds that the draft does not.

Data: `check-rules.json` → `checks.balance_cues.data`.

## Procedure: balance cues

1. Split the draft into lines (1-based). For each line, test every regex in each group in `cue_groups` (case-insensitive unless the pattern is the AE/SAE abbreviation forms).
2. Record line, groups matched, and the matched substrings.
3. Count benefit lines vs risk-or-limitation lines.
4. Unpaired benefits: each benefit line with no risk/limitation cue on the **same** line and none within ±`unpaired_window_lines` (default 3) of a risk/limitation line.
5. If source material is supplied: list study-name and time-point tokens in material that do not appear in the draft (`study_name_pattern`, `timepoint_pattern`).
6. Report cues and gaps only — no judgment that the draft is balanced or unbalanced.


