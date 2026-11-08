# Task: Number consistency

Input: draft with quantitative claims; source tables
Atom: compose-draft
Tool: scripts/grounding_check.py (owner key); arithmetic by hand from supplied figures only
Template: templates/repair-note.md
Output: draft with consistent bases and labeled units
Check: percent vs pp called out; absolute beside relative when relative appears
Human: owner confirms corrected figures match their table

## Checks
- Same denominator when comparing rates.
- Relative uplift always paired with absolute change from the same base.
- Ranges state low/mid/high and the metric date the team entered — never invent midpoints.
- Do not convert currencies or units without a team-supplied factor.
