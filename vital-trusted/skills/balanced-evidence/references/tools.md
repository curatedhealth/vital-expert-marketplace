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

## Script

### `scripts/balance_cues.py`

Lists wording that usually marks a benefit, a risk or limitation, reassurance about
safety, or a selected result, and compares study names and time points in the draft with
those in the supplied material. It finds wording, not meaning: read the whole draft as
well, and do not report its counts as the check line without reading.

```
python scripts/balance_cues.py draft.txt
python scripts/balance_cues.py draft.txt --source material.txt
python scripts/balance_cues.py draft.txt --window 2 --json
cat draft.txt | python scripts/balance_cues.py -
```

| Output | What it means |
|---|---|
| Cue lines | Each line with benefit, risk or limitation, reassurance or selection wording, and the words matched |
| Counts | Lines with each kind of wording |
| Benefit lines with no risk or limitation nearby | Benefit lines with no risk or limitation wording within `--window` lines (default 3). A pointer to where balance may be missing, not a finding |
| In the material, not in the draft | Study names in capital-letter-and-number form (for example ZELORA-3) and time points (week 52, 12 months) present in the material but absent from the draft |

Pitfalls:

- Benefit words also appear in risk statements ("reduced dose because of nausea"); risk
  words also appear in benefit statements ("reduced the risk of events"). Read the line.
- Study names not in capital-letter-and-number form are not found.
- A time point missing from the draft may be legitimately out of scope. State the scope
  rather than restoring everything.

Tested on 20 October 2026 with `python3 scripts/test_balance_cues.py` against
`scripts/test_draft.txt` and `scripts/test_material.txt` (expected cue groups per line,
counts, unpaired benefit lines at window 3 and 1, and the missing study and time points
asserted). Result: OK.
