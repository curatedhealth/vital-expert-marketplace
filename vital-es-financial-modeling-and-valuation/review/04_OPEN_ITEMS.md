# Open items

Written 7 November 2026. Tags: M measured, V asserted by a file, H hypothesis.

## A. Untraced items ([CHECK]); never scored, never filled

- V1 · rule FV-TERMINAL-SHARE: disabled rule: no registered threshold for a terminal-value share; the script prints [CHECK] and does not compute it
- V1 · FV-04: detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md
- V2 · rule FV-RATE-CHOICE: disabled rule: no registered default or range for a biotech discount rate (the one rate-magnitude source opened concerns capitalizing R&D outlays, VP-V-060, and is out of scope); the script prints [CH
- V2 · FV-04: detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md
- V3 · rule FV-TERMINAL-SHARE: disabled rule: no registered threshold for a terminal-value share; the script prints [CHECK] and does not compute it
- V3 · FV-04: detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md

## B. Validation state
- Capability tier: Standard (owner ruling of 8 November 2026). The Full-tier back-test was retired before any run [V: evals/backtest/AMENDMENTS.md]; a filing-fidelity known-answer set (four cases, one held-out) tests method fidelity and has not been run.
- Standard-tier known-answer sets for all nine skills: built and frozen with held-out cases written by blind sub-agents; **no executor or grader has been run** [V: each FREEZE.md]. Two held-out cases of V3 and both of V4 disagree with the script for stated reasons recorded in their FREEZE.md.
- Release state of every skill: Draft. Practitioner review: pending, this pack is its input.

## C. Decisions for the owner
- Tier is Standard; no SEC download is pending for the valuation plugin.
- Prompt suite rows (PS03 to PS05) are not in the binding migration; they need steward review of prompt text.
- The agent row npv_analyst is recommended and not written (shared row).

## D. Binding state
- Migration 20261107140000 is a local file in supabase/migrations_pending; **nothing is applied to any database**. The local dry run passed and its re-runs changed 0 rows; the live pre-check (SELECT only) matched every valuation target row and failed only on the Market Access atoms the migration depends on.
