# Connector tools used by Close the Decision

Inputs read from the connector code at commit e23025f6e on the owner checkout (M). All need an open brief (`brief_id`). [CHECK on the live run]

## decide_attach_scores

- `{"brief_id", "stage", "scores": {...}}`. Several scorers as a `cells` list; values 1 to 10; an AI author is refused. Stored **unreleased**: a later stage read returns "[GAP] unreleased".

## decide_release_scores

- `{"brief_id", "stage", "released_by": "name"}`. A missing name, or "ai", "model", "assistant", releases nothing. Refuses a stage with no scores. Returns `released: true` and the name.

## decide_record_dissent

- `{"brief_id", "payload": {"person_name": "...", "text": "..."}}` or `{"person_name": "...", "none": true}`. Both text and none, neither, a missing name, or an AI author is refused. The record writes the line into the dissent section.

## decide_build_record

- `{"brief_id"}`. Returns the eight sections a person reads, plus compile keys in the draft (including a read-back). Status "Prepared for signature" or "blocked". It compiles only with a result of exactly Proceed, Investigate first or Handle it internally, owned by a named scorer.
- Pitfall: the draft's numbered compile keys differ from the canon sections (options appear as key 4); read the eight sections, never the compile keys, and never show either key names.

## decide_verify_record

- `{"brief_id"}`. Checks the built record; `cannot_choose: true`.

## decide_prepare_signoff

- `{"brief_id", "prepared_for": "name"}`. Builds the record, stores who it is prepared for and its status; `signed: false`, always. Call once per signer.

## Not available

- No tool records the act of signing; signing happens in the Navigator app (method.md D6).
- VITAL Verify `build_record` (separate connector) can produce a cleared record when a named human is given in `cleared_by`.
