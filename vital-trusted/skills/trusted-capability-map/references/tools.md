# Companions

A companion is an MCP connector that gives TRUSTED skills real tools. The plugin is free
and complete without one. A companion turns a method flag into a checked result.

## The slot rule

Every task in every TRUSTED skill has a companion slot:

1. What the companion would do for this task, in one line.
2. The tool call when it is connected.
3. Without it: the method runs fully, and tool-only checks are marked
   `[GAP: not checkable here — …]`.
4. Never simulate a companion (TR-H4).

## Detecting a companion

A companion is connected when its tools appear in the assistant's tool list (on Cowork
and Claude, as connector tools; on other hosts, as the host shows MCP tools). Do not
assume a connector exists because the person mentions it. If unsure, say which tool
would be used and ask whether it is connected.

## VERIFY (live)

VERIFY checks sentences against passages the person or the tools supplied, qualifies
sources, checks currency, builds citations and builds a record cleared by a named human.
A support status is overlap with a supplied passage, not a verdict on truth in the world.

Tool names as listed by the VERIFY connector. [CHECK: argument and return contracts to
be confirmed against the connector schema before the Prove skills are finalized.]

| Tool | Used by |
|---|---|
| `extract_claims` | `claim-assessment` |
| `check_claim` | `claim-assessment` |
| `verify_text` | `claim-assessment` |
| `ingest_document` | `source-assessment` |
| `qualify_source` | `source-assessment` |
| `check_currency` | `source-assessment` |
| `build_citation` | `citation-and-record` |
| `build_record` | `citation-and-record` |
| `build_evidence_table` | `citation-and-record`, only when the person asks for a table |

How to connect VERIFY: this pack already declares the connector at
`https://mcp.vital.expert/api/mcp/verify` (server id `vital-verify`). In Cowork, paste the
`vvfy_` key from the VITAL purchase when the pack asks for it. Tools appear in the
assistant tool list when the key is accepted. Do not add a second MCP entry for the same
URL. The standalone `vital-verify` pack uses the same connector; installing both does not
create a second product host.

## Future companions

Candidates, not commitments. Until one exists, its slots run as method only.

| Candidate | Would fill slots in |
|---|---|
| MLR preparation | `claims-and-label`, `market-rules-and-data`, `balanced-evidence`, `patient-safety`, `work-record` |
| Label source | `claims-and-label`, `patient-safety` |
| Evidence grading | `source-assessment` |
| Safety routing | `patient-safety` |
| AI policy | `responsible-inputs`, `responsible-use` |
