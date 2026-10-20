# Worked example: A2 and B1 on illustrative sandbox files

All inputs are ILLUSTRATIVE (`sample-data/README.md`): a synthetic sandbox bundle, the person's own check sheet, a scope list, a screen list, a saved token response and a code map. The connector was disconnected during this build (20 October 2026), so no library call was made; the record step is described from the saved refusal in `live/verify_build_record_refusal_2026-10-19.json`.

**Request (illustrative):** "We're a diabetes app vendor connecting to a hospital's EHR sandbox ('Sandbox A'). We built to US Core 6.1.0 and wrote our own check sheet. Here are a sample bundle, our scopes, the screen list, the token we got back, and our lab and diagnosis map. Are we ready for go-live? Our integration lead is Dana."

**Runs**

1. `python3 scripts/fhir_check.py scopes --scopes "launch openid fhirUser patient/Observation.rs patient/Condition.read system/*.read patient/Encounter.sr" --screens sample-data/screens_illustrative.csv`
2. `python3 scripts/fhir_check.py token sample-data/token_response_illustrative.json --need patient,encounter,fhirUser`
3. `python3 scripts/fhir_check.py capability sample-data/capability_illustrative.json`
4. `python3 scripts/fhir_check.py resources --sheet sample-data/check_sheet_illustrative.json sample-data/bundle_illustrative.json`
5. `python3 scripts/fhir_check.py map sample-data/terminology_map_illustrative.csv`

## Answer (short mode)

**Answer.** Go-live is your call and Dana's; this is the record against your own sheet. Against US Core 6.1.0, which is the version ONC certification requires (45 CFR 170.215, eCFR read 20 October 2026, EN-134), the sample has 3 misses on one Observation, one of which you flagged as blocking; MedicationRequest was not checked because your sheet has no entry for it. The sandbox token carried patient and fhirUser but no encounter context, and two scope lines need attention.

**Scopes**

| Scope | Finding | Rows |
|---|---|---|
| system/*.read | SMART v1 syntax; system/ scopes are for backend services with no user, and your app launches as a user | HL7 SMART App Launch 2.2.0 pages, read 20 October 2026 (EN-138, EN-139) |
| patient/Encounter.sr | Suffix is not an ordered subset of c r u d s; no screen uses Encounter | EN-138 |
| patient/Condition.read | v1 syntax; v2 equivalent .rs | EN-138 |

Screen "Risk score card" claims write-back on a read interaction; "Settings" is local-only and not integrated.

**Sandbox launch (Sandbox A):** patient present, fhirUser present (id_token, signature not verified), encounter MISSING; no refresh token issued.

**Gap record (your sheet, US Core 6.1.0)**

| Payload | Resource | Element path | Result | Blocks go-live |
|---|---|---|---|---|
| bundle | Observation/obs-glucose-002 | code.coding.system | local code, sheet binds LOINC | yes |
| bundle | Observation/obs-glucose-002 | category.coding.code | missing | not given |
| bundle | Observation/obs-glucose-002 | effectiveDateTime | missing | not given |

**Map flags:** LIPID-PNL is unmatched but sits in production (K1); DM2 has no terminology version (K2); a free-text source was mapped to a code with no stated method and a label outside your list (K3, K4). One code is correctly on hold; steward not named.

**For you to decide:** blocking flag for the two "not given" misses; whether MedicationRequest is in go-live scope; the encounter context fix (app or EHR configuration); the steward for held codes; your adoption definition (not given).

**Gaps.** Element-level must-support beyond your sheet is not checked `[GAP]`; Sandbox A's app-registration terms are not in the sources `[GAP]`.

**Calls made:** scripts only (five runs above); library disconnected, no counted call. Full version (registration note, screen map, licensing lines) on request.

**Record:** Gap record draft for the owner. AI-assisted. Clears it: Dana. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## What this example shows

- No "ready" verdict: the answer counts misses against the person's sheet and leaves go-live to the named owner.
- The version that certification requires is named with its source; nothing claims R5 or US Core 9.0.0 is needed.
- Unchecked resource types and "not given" blocking flags stay visible.
- The token check reads fields only; it does not test or replay the token.
- `python3 scripts/fhir_check.py words` on the answer above: within the short-mode cap.
