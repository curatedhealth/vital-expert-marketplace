# Connector tools used by the Outcomes skills

Connector: VITAL Ontology Navigator (listed as `Ontology_Navigator` or `vital-ontology-navigator`, depending on the install; tool names are the same). Your assistant may prefix the names. Counted calls draw on the key's monthly allowance; check `my_usage` (free) first. Behavior below was established by read-only lanes on the connector's code on 19 October 2026 (M), not by live calls. [CHECK on the first live test run]

## catalogue_search (counted)

- Outcomes: pillar `JT`, `level` 1 (strategic), 2 (category) or 3 (mission), `query` with words from the decision and goal, optional `limit` 1 to 25.
- Measures: pillar `VP`, same levels (headline metrics, category measures, measures).
- Returns rows with a spoken label and code. Speak the label; code in brackets only if needed.
- Pitfalls: library opportunity values on outcome rows are stored decimals from earlier work; they are not this room's scores and are never shown as such. Measure rows almost never carry a baseline and never an owner.

## catalogue_list_children (counted)

- Arguments: the parent row's `id` and the pillar.
- Pitfalls: links between levels are incomplete (49 category outcomes have no strategic parent; 8 mission outcomes have no category parent). Drilling by parent misses them; search the finer level with the parent's words as well.

## catalogue_pack (counted)

- Returns a function's mission outcomes as one set. Only Medical Affairs has a pack today (15 rows); other functions return a gap. Say "no ready-made set for this function yet" only if it matters.

## bridge_for_driver, bridge_for_outcome, chain_trace (counted)

- Read links at level 3 only (driver to outcome, outcome to measure and to use cases). For level 1 or 2 nothing useful returns.
- The result labels links with internal edge names. Say "contributes to" (outcome to driver), "measured by" (outcome to measure). An empty result means "the library links nothing here yet", never "no link exists".

## methods_nav_compute (counted): outcome scoring, several scorers

- Payload: `{"template_id": "nav.outcomes", "items": [{"item_id": "o1"}, ...], "scores": [{"scorer_id": "...", "item_id": "o1", "criterion_key": "importance" | "satisfaction", "value": 1-10}, ...], "owner_scorer_id": "..."}`; optional `missing_scorer_ids`.
- Returns per outcome: group importance and satisfaction (mean, median, spread, disagreement at a spread of 3 or more), opportunity, band, median of scorers' own opportunity; the owner's view computed separately; sensitivity (drop one scorer; "stable" or "close call" for the leader only (the local script also compares the top set, its order and the full order)); "indicative" under three scorers.
- Refuses: a value that is not a whole number 1 to 10; a missing cell (nothing is imputed); an owner with no scores.
- Use item ids that are short and neutral (o1, o2). Map them back to statements yourself; never show the ids.
- Pitfall (live, 19 October 2026): the hosted engine call returned an error three times. When it fails, compute with the skill's local script and say once, in a clause, that the connector could not compute; the result is the same formula.

## methods_odi_score (counted): one score set only

- Takes one importance and satisfaction per outcome (decimals allowed). Use only when a single person scores, labeled indicative. Its band words differ from the engine's; use the engine's words (method.md O11).

## Storing scores on a brief (decide_attach_scores, then decide_release_scores)

Checked live on 19 October 2026 (M). Only when a brief is open and named people gave the scores.

- `decide_attach_scores`: `{"brief_id", "stage", "scores": {"cells": [ ... ]}}`. Each cell needs `item_id`, `criterion`, `value` (whole number 1 to 10), `rater_id` (the person's name), `rater_role` (`decision_owner`, `participant` or `facilitator`), `source` (`owner` or `participant`), `scale` (`"1-10"`) and `submitted_at` (time stamp). The connector names a missing field one at a time; fill them all at once.
- Never attach a cell a named person did not give. Since build 5b1220dc1 the connector also refuses an AI name and the old rows shape (M, recheck 19 October 2026). `simulated` is stored only on a brief marked as a test.
- Each person's cells are added as they come in. The same person scoring the same stage twice is refused unless the call carries `replace` (top-level, with `by`, a person's name, and `reason`); the earlier cells are kept in the brief's history.
- Then `decide_release_scores` with `released_by` (a named person), once every scorer has submitted. Without a name nothing is released, and the record shows the stage as unreleased.
- Never show the field names to the person.
## Not available

- No Gate 2 function: the attestation is taken in conversation (method.md O15).
- No field-test check: use `scripts/outcome_priority_check.py` (prioritize-outcomes) to read the conditions.
- No offline fallback is needed for scoring: the local script computes the same formula.

## my_usage (free)

Calls used, monthly cap and plan.
