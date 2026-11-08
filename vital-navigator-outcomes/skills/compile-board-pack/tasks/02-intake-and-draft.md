# Task: Intake and draft

Input: team-entered facts for this step; upstream skill outputs listed at intake; connector availability.
Atom: compose-draft
Tool: scripts/board_pack_check.py
Template: templates/worksheet.md
Output: draft worksheet
Check: no invented numbers; [GAP] listed; autonomy respected
Human: named decision owner

## Steps
1. Restate what is known and what is [GAP].
2. Run the offline tool if listed; otherwise draft from templates only.
3. Present options or draft to the named human; stop for human-only gates.
