# Verify claim packet

| Field | Value |
|---|---|
| Owner | |
| verify_status | verified / not tool-checked / claims_removed |
| circulation | internal_only / external_blocked / external_ok |
| self_blessed | must be N |

| Id | Claim text | tool_checked? |
|---|---|---|
| C1 | | Y/N |
| C2 | | Y/N |

Rules: external_ok only when verified and all claims tool_checked.  
Script: `python3 scripts/verify_handoff_check.py handoff.json --json`
