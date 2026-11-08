# Task: Seal check

Input: pack.json fields for board_pack_check
Atom: none
Tool: scripts/board_pack_check.py
Template: templates/worksheet.md
Output: ok or [GAP] list; status prepared or blocked
Check: signed must not be true; verify_status required
Human: two signers named (human only)
