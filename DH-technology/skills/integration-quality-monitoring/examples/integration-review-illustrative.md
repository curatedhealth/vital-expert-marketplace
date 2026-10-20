# Worked example: A1, A2 and B1 on illustrative files

All inputs are ILLUSTRATIVE (`sample-data/README.md`): two synthetic sandbox exchanges, a six-cell launch matrix, a ten-row map review sample and five workflow observations. The connector was disconnected during this build (20 October 2026), so no library call was made; the record step is described from the saved refusal in `live/verify_build_record_refusal_2026-10-19.json`.

**Request (illustrative):** "Review our integration after the pilot. Two sandbox exchanges (6 and 13 October), the launch matrix we ran on 14 October, the map review and the clinic observations are attached. Our token ceiling is 800 ms. Priya owns the app side; the hospital's interface team owns EHR configuration. Is our map accurate enough?"

**Runs**

1. `python3 scripts/integration_check.py score --sheet sample-data/check_sheet_illustrative.json sample-data/exchange_2026-10-06_illustrative.json sample-data/exchange_2026-10-13_illustrative.json`
2. `python3 scripts/integration_check.py launch sample-data/launch_matrix_illustrative.csv --token-ms 800`
3. `python3 scripts/integration_check.py mapsample sample-data/map_review_sample_illustrative.csv --exact-labels equal`
4. `python3 scripts/integration_check.py workflow sample-data/workflow_observations_illustrative.csv`

## Answer (short mode)

**Answer.** Against your sheet, Observation had a miss in 3 of 4 samples and Patient in 1 of 2; MedicationRequest was not checked (no sheet entry). Of six launch cells, four carry a flag, one of them a mocked token and one not run. "Accurate enough" is your threshold, and none was given: the exact-match rate is 5 of 8 reviewed rows (62.5%) and the unmatched rate 2 of 10 sampled rows (20.0%), by the old task's definitions.

**Failures**

| Unit | Failure | System to change | Owner | Release or accepted by |
|---|---|---|---|---|
| Observation | local glucose code where your sheet binds LOINC; category and effectiveDateTime missing | not given | not given | not given |
| Patient pt-101 | identifier.value missing | not given | not given | not given |
| Cell C3 (nurse, inpatient) | encounter context missing; write-back not visible; token 910 ms over your 800 ms | not assigned | Priya or the interface team (your call) | not given |
| Cell C4 (nurse, discharged) | HTTP 403; no context | not assigned | not given | not given |
| Cell C5 | mocked token: not an EHR launch | app | Priya (app side, as you named) | not given |
| Cell C6 | not run | not given | not given | not given |

**Map.** Two disagreements (M05 "equivalence too strong", M09 "stale code"). Row M06 was reviewed by its own mapper, unblinded, and drawn from rows hand-checked the day before (R1, R2, R4). In Kahn et al. 2016 terms (DOI 10.13063/2327-9214.1244, DA-94 to DA-96), the reviewer's acceptance is a validation judgment; the target code against allowed values is value conformance.

**Workflow.** Result review: 2 of 4 observations done as designed, 1 skipped, 1 replaced; workarounds quoted: "Printed the lab flowsheet and wrote values on paper" (O3), "Asked the patient to read values from their phone" (O4); 48 to 151 seconds over 4 observations. Care plan note: replaced once ("Copied the note text into a free-text chart note", O5); one observation, so no mean or range.

**For you to decide:** your map threshold; the system and owner for each failure; whether C3 belongs to the app or EHR configuration; the blocking map class and the blocking step; recheck dates (not given).

**Calls made:** scripts only (four runs above); library disconnected, no counted call. Full version (all cells, error classes, standards read) on request.

**Record:** Integration review draft for the owner. AI-assisted. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## What this example shows

- "Accurate enough" is answered with computed rates and "threshold not given", never with a model's number.
- A profile with misses in most samples is named, not averaged into an overall score.
- Owners appear only where the person named them, in their words; everything else is "not given".
- The mocked-token cell is visible as not an EHR launch.
- `python3 scripts/integration_check.py words` on the answer above: within the short-mode cap.
