# Task: Sensitivity exhibit

Input: scored options matrix with team-set weights; named scorers
Atom: compare-against-criteria
Tool: scripts/options_check.py (if present); feeds run-weight-sensitivity
Template: templates/worksheet.md
Output: one-way weight swing table showing any rank swap; source ids on every series
Check: no invented weights; human confirms swings worth showing
Human: named decision owner confirms which swings enter the board pack

## Steps
1. Take the locked weights and scores from score-the-options (human-entered only).
2. Swing one weight at a time within the band the team set; recompute ranks offline.
3. List options whose rank changes; mark stable options.
4. Hand the exhibit draft to design-decision-exhibits / run-weight-sensitivity.
