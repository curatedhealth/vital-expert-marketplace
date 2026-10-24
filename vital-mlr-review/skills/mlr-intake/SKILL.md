---
name: mlr-intake
description: "This skill should be used when opening an MLR board-preparation packet: collecting markets (never default to the US), audience, channel, artefact version, and authorized-use text; calling intake and ruleset tools. Trigger on prepare for MLR or multi-country HCP materials. Do not use to approve copy or to run VERIFY alone."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-0.1"
  register_code: "MLR-0.1"
  framework_path: "MLR Review > Intake"
  family: "mlr-prep"
  worker: "MLR intake coordinator"
  pack: "vital-mlr-review"
  version: "0.3.1"
  route:
    - "Open an MLR intake for this artefact"
    - "Collect jurisdictions for the MLR packet"
    - "Never default MLR markets to the United States"
    - "Load rulesets after MLR intake context"
    - "Authorized use text per market for MLR"
    - "Prepare this material for MLR board intake"
    - "mlr_intake with Germany and Switzerland"
    - "Channel promo versus scientific exchange for MLR"
    - "Missing Fachinformation stays a gap at intake"
    - "List ruleset coverage after MLR intake"
---

# Intake

Open the file for human MLR review. Make markets, channel, and label basis explicit so chairs do not invent a country or a SmPC.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| collect context | Collect markets, channel, artefact, authorized use | `tasks/collect-context.md` |
| load rulesets | List and load rulesets for named markets | `tasks/load-rulesets.md` |

## Scripts

`scripts/check_jurisdictions.py`, `scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Tool path

1. Run `scripts/check_jurisdictions.py` on the context JSON when markets are proposed.
2. Call `vital-mlr-review:mlr_intake` then `vital-mlr-review:mlr_list_rulesets` / `vital-mlr-review:mlr_get_ruleset`.
3. Report coverage (`full` / `stub` / `missing`) per market.

## Boundaries

| Question | Where it goes |
|---|---|
| What can this pack do / which skill | `mlr-capability-map` |
| Markets and ruleset load | `mlr-intake` |
| Clinical / label accuracy | `mlr-medical-chair` |
| Misleadingness / comparative-ad / privacy | `mlr-legal-chair` |
| ISI / format / pre-approval process | `mlr-regulatory-chair` |
| Align + validate | `mlr-compile` |
| Passage / source proof | `mlr-verify-handoff` |
| Named-human prep record | `mlr-board-prep` |


## Hard rules (every MLR skill)

- **MLR-H1.** Only stored material counts — fields from the person or a tool result.
- **MLR-H2.** Teaching material is never input — examples/ and patterns.md are invented for shape.
- **MLR-H3.** Never approve — no approved-for-use, mlr_reviewed, or regulator-compliant stamp.
- **MLR-H4.** Never simulate the connector — without vmlr_/vvfy_ label not tool-checked.
- **MLR-H5.** A named human owns prep records — refuse ai/model/assistant/system as cleared_by.
- **MLR-H6.** Markets explicit — never default jurisdictions to the US.
- **MLR-H7.** Keep M / L / R MECE — do not blend chairs or substitute another market's rules.
- **MLR-H8.** Plain liability — every user-facing result ends with the closing line.

## What to return

Sections in `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Files

| File | Role |
|---|---|
| `tasks/` | Formula tasks for this skill |
| `references/tools.md` | Fully qualified MCP tool names |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Route and refuse cases |
| `scripts/check_jurisdictions.py` | Deterministic check — run, do not re-implement |
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/markets.md` | Preserved domain reference |
