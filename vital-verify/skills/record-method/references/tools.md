# Tool calls

## Companion slot

`build_record` and `build_citation` need a VERIFY key and a human name for clearance (VR-H5).

# Tool calls

## build_citation

Arguments: one admitted source, and a style only when the person names chicago or harvard. Otherwise omit style so the key preference applies.

Returns: one formatted line. Paste it. Add no caption.

## build_record

Arguments: clearances, each with a decision, a human name, a role, a time, and a note.

Returns: the record. Refuses when the name is missing.

## build_evidence_table

Call only when the person asks for the table. It does not change a status.

Schema source: Verify connector, 19 October 2026.
