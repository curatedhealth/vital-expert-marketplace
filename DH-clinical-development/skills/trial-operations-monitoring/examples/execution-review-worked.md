# Worked run: B1 execution quality review (short mode)

Run on 19 October 2026. The export, targets and rules are illustrative files in `evals/files/` (invented, labeled illustrative). The script output is in `examples/script-runs.md`. The registry lookup is a live library call on a real, completed trial, shown only to demonstrate A2's lookup; it is not the illustrative trial.

## Request

"Here is our export as of today plus our quality tolerance limits (rules_illustrative.json). Which sites miss, why, and who owns it? Also, what does the registry show for NCT04885530?"

## Calls and runs

| Call or run | Arguments | Result |
|---|---|---|
| `scripts/trial_ops_metrics.py sites` | export, targets, `--as-of 2026-10-19`, `--rules rules_illustrative.json` | 4 sites, 65 enrolled of 84 targeted; 13 rule checks |
| `literature.find_trial` | `{nct_id: "NCT04885530"}` | COMPLETED, PHASE3, sponsor named; 5 linked publications (3 preprints); no dates returned |

## Answer (short mode)

**Against your rules (as of 19 October 2026):**

| Site | Retention (your 85%) | Completeness (your 90%) | Important deviations per participant (your 0.1) |
|---|---|---|---|
| Berlin | 90.9 pass | 95.0 pass | 0.0 pass |
| Boston | 100.0 pass | 77.0 miss | 0.0 pass |
| Denver | 88.9 pass | 89.2 miss | 0.33 miss |
| Munich | 76.9 miss | 93.5 pass | 0.08 pass |

Arm balance (your 5 points, trial-wide): 2.8 points, pass. Beneath it, Boston's arms differ by 10.1 points (A 81.4, B 71.3 percent): the trial total hides one site.

**Stall points.** Boston: completeness. Denver: deviations (3 important among 9 enrolled), then completeness. Munich: retention (2 withdrawn, 1 lost of 13).

**Hypotheses to test (not causes).**

- Boston: the collection method differs between arms in practice (CV58). Confirm with device or app version and visit type by arm (CV69).
- Denver: a site-specific process issue, since no other site has important deviations above 0.08 per participant (CVB5, CVB6). Confirm with deviation categories from the monitoring report. Under E6(R3) the investigator explains important deviations and acts to prevent recurrence (CVB1).
- Munich: participants choosing remote visits may differ from those attending (CV67). Confirm with retention by visit type.

**Owners (yours).** Completeness: Data Management. Deviations: QA. Retention: Clinical Operations lead. Arm balance: owner not named; who owns it?

**For the clinical trial report.** Exceeded ranges and the remedial actions taken are documented there (CVB4).

**Registry check.** NCT04885530 shows COMPLETED, phase 3, with five linked publications, three of them preprints. The library returns no registration, completion or results dates `[GAP]`; for clocks, give the dates and A2 computes them.

**Decision needed.** Whether Boston's arm gap is reviewed before further enrollment there, by Data Management.

**Record.** Uncleared draft. Rules and owners are yours.

(Word count of the answer, without the calls table and the rules table: about 330.)
