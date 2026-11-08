# Task: Run swings

Input: sensitivity-input.json
Atom: rank-by-consequence
Tool: scripts/sensitivity_exhibit.py
Template: templates/sensitivity-input.md
Output: base_rank + per-swing swaps
Check: exit 0; no invented totals
Human: owner picks swings for board
