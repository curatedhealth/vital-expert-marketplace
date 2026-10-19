# Connector tools used by Close the Decision

Inputs read from the connector code at commit e23025f6e on the owner checkout (M). All need an open brief (`brief_id`). Checked live on 19 October 2026 (M, `eval-runs/LIVE_CONNECTOR_CHECK_2026-10-19.md`).

## decide_attach_scores

- Earlier skills attach the scores; see their tools reference ("Storing scores on a brief"). Each cell needs `rater_id`, `rater_role`, `source`, `scale` and `submitted_at`. The connector refuses an AI name (build 5b1220dc1); never attach a cell a named person did not give.

## decide_release_scores

- `{"brief_id", "stage", "released_by": "name"}`. A missing name, or "ai", "model", "assistant", releases nothing. Refuses a stage with no scores. Returns `released: true` and the name.

## decide_record_dissent

- `{"brief_id", "payload": {"person_name": "...", "text": "..."}}` or `{"person_name": "...", "none": true}`. Both text and none, neither, a missing name, or an AI author is refused. The record writes the line into the dissent section.

## decide_build_record

- `{"brief_id"}`. Since build 5b1220dc1 (checked live): the draft carries the trial, delivery order, delegation (with any exception), value realized, review, scaling plan, steward, readiness and who released each stage's scores. It still holds nine numbered keys, not the eight canon sections (register C3).
- So assemble the eight sections from the earlier reports yourself (task B), check them with `scripts/record_check.py`, and use the connector draft as a cross-check. Never show its key names.
- It reports "passed: false" until a result of exactly Proceed, Investigate first or Handle it internally is owned by a named scorer.

## decide_verify_record

- `{"brief_id"}`. Checks the built record; `cannot_choose: true`.

## decide_prepare_signoff

- `{"brief_id", "prepared_for": "audience label", "signers": ["owner's name", "second signer's name"]}` (build 5b1220dc1). Returns `signed: false`, always, and the reasons whenever the status is blocked.
- Refuses a missing or AI name and two identical names; a title without a name is a gap. Without `signers` it returns blocked with "two named signers needed".
- Keep `scripts/record_check.py` as the check you report from; the connector's reasons are a cross-check.

## Not available

- No tool records the act of signing; signing happens in the Navigator app (method.md D6).
- VITAL Verify `build_record` (separate connector) can produce a cleared record when a named human is given in `cleared_by`.
