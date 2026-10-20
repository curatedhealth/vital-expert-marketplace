# Worked example: B1 design decision and evaluation plan

Run on 19 October 2026. The product, options, scores and weights are illustrative, written for this example and labeled so. The ranking call is a real library call (`live/mcda_alert_placement.json`). The swap points come from `scripts/mcda_swap.py` on the saved call (`live/mcda_swap_output.txt`).

**Request (illustrative):** "Our sepsis-risk score goes into the hospital EHR for ward nurses (US, certified health IT module). We are choosing between an interruptive alert, a worklist banner and an inline panel in the order screen. Our scores and weights are below. Rank them and tell us what to test first. Priya decides; regulatory is Tom."

**Calls and runs**

1. `analytics.mcda` with the person's scores (0 to 4) on critical-task protection, workflow interruption avoided, basis reviewable, build effort avoided; weights 0.40, 0.25, 0.20, 0.15.
2. `python3 scripts/mcda_swap.py examples/live/mcda_alert_placement.json`: values match the connector; swap points below.

## Answer (short mode)

**Your scores put the inline order panel first (72.5), the worklist banner a close second (71.25), and the interruptive alert third (67.5).** The top two are 1.25 points apart: if critical-task protection were weighted 0.37 instead of 0.40, or workflow interruption avoided 0.29 instead of 0.25, the banner would move ahead. Scores and weights are yours; this is not a recommendation.

| Option | Value | Largest contributions |
|---|---|---|
| Order panel inline | 72.5 | critical-task protection 30, basis reviewable 20 |
| Worklist banner | 71.25 | workflow interruption avoided 25, critical-task protection 20 |
| Interruptive alert | 67.5 | critical-task protection 40 |

**Facts behind "basis reviewable":** Criterion 4 asks that the HCP can review inputs, a plain-language algorithm basis, and knowns and unknowns such as missing inputs, with decision-relevant information first (UX-US-67 to UX-US-70). As certified health IT, the intervention must appear while the nurse is interacting with the system and capture feedback (UX-US-54, UX-US-55). Source-attribute access (UX-US-56) is in force but proposed for removal under HTI-5, not final (UX-US-60). Whether sepsis-risk triage is time critical in the sense of UX-US-66 is a question for Tom, not for this paper.

**First formative test:** the inline panel and the banner side by side on the critical task you marked in A2 ("act on a high score before the next round"), with ward nurses as one population. Purpose, scenarios, participants, data and analysis per UX-US-44; the number is yours, with the rationale written down (UX-UK-17). Employees may join formative work (UX-US-45), not validation (UX-US-38).

**For Tom (regulatory owner), no category chosen:** the UI is new, users and environment are unchanged, one critical task is new (A2); FDA recommends keeping these records whether or not submitted (UX-US-53).

**Stops:** the option choice is Priya's; device status, Criterion 4 and HF category are Tom's.

**Record:** Design decision draft. Uncleared. AI-assisted.

The full version adds the facts table per criterion, the full swap table and the formative plan table.

## What this example shows

- The connector ranked only what the person scored; the swap points show the order is fragile.
- Regulatory questions were handed to the named owner with the decision-point facts, not answered.
- HTI-5 items were labeled proposed.
