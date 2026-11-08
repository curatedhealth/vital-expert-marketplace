# Method: route-the-entry

Owner-facing method for Outcome Navigator (`CF-01.06.01`). Written 7 November 2026.

## Purpose
Open a session by classifying **family** (outcome / launch / due_diligence / ready / other) and **entry shape** (top_down / middle_out / bottom_up). Hand off siblings; never absorb their work.

## Rules
1. Family test before facilitation depth. Launch Pass/Hold/Escalate, READY chairs, DD valuation grades → stop and name sibling.
2. Middle-out and bottom-up always route through `frame-the-decision` then `size-value-at-stake` before options.
3. Tool-named asks ("deploy GPT agents") are reframed as investment decisions; the tool is an option.
4. One question per turn; human confirms classification when ambiguous.
5. Offline script `routing_check.py` validates the routing JSON; never invents a route.

## Outputs
Routing map (family, shape, next_skill or sibling_plugin + handoff_reason). Gaps named, not filled.

## Lane A absorb — job vs solution at entry (7 November 2026)

Solution-first and middle-out entry must record a **job statement** and **job executor** separate from the proposed solution (Bettencourt & Ulwick 2008 — LA-HBR-JOBMAP / WR-011). Prefer understanding the **execution** step first, then expand (WR-013). Offline: `routing_check.py` fields `job_statement`, `proposed_solution`, refuse `treat_solution_as_job`.

## Deepening note (8 November 2026)

- Middle-out and bottom-up entries always route frame-the-decision then size-value-at-stake before compare-options, run-weight-sensitivity or place-the-portfolio. `route_path`, when supplied, is checked against that order and against the real skill ids.
- A solution-first ask (named tool or a deploy/buy/implement verb, with or without `proposed_solution`) needs `job_executor`, an independent `job_statement`, an execution-step interview start (WR-013) and a first route to frame-the-decision.
- Gate vocabulary in the ask text (Pass/Hold, launch readiness, READY chair, asset valuation) with family=outcome is a gap even when `forbidden_vocab_present` is unset.
