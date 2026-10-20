# Worked example: B1 program change decisions (live connector call, 19 October 2026)

The program data are the illustrative files in `sample-data/` (they describe no real program). The RICE inputs, rules and owners are the example person's; the RICE numbers were typed for the measurement call and are presented here as theirs.

Request (illustrative person): "Quarter results are in for our insomnia education program (1 July to 30 September 2026). Our targets were 60 for the webinar series and 60 for peer-mentor calls. We think we should change the webinar content, stop the newsletter, and widen the peer-mentor calls to caregivers. We scored those three with RICE. Jo owns the webinars; the newsletter owner is not decided. What should we do first?"

## Calls made

1. `scripts/engagement_monitor.py activities sample-data/activities.csv` (local; output in `script-output.md`).
2. `scripts/engagement_monitor.py partners sample-data/partners.csv` (local).
3. `analytics.rice` with confidence as a percent (saved: `live/rice_percent.json`). A first call with confidence as a fraction is saved as `live/rice_fraction.json` to show the pitfall.

## Answer (short mode)

**Answer.** One activity missed your rule: the webinar series, 37 bookings against your target of 60 (9 percent of 412 reached). Peer-mentor calls met it (71 completions against 60). The newsletter and the partner forum posts are unscored: there is no record of the action, so they are neither met nor missed. Your recorded decision for the webinar is "change content", owned by Jo. The newsletter decision (stop) has no owner yet: owner not named. Decide the webinar and the newsletter before widening the peer-mentor calls, which is a change to an activity that met its rule, not a decision on a miss.

**Your changes ranked by your RICE numbers** (confidence passed as a percent):

| Rank | Change | Score | Your inputs (reach, impact, confidence, effort) |
|---|---|---|---|
| 1 | newsletter: stop | 360 | 900, 0.25, 80, 0.5 |
| 2 | webinar-series: change content | 100 | 400, 1, 50, 2 |
| 3 | peer-mentor calls: change audience | 64 | 120, 2, 80, 3 |

This order is the result of your numbers, not a recommendation.

**Sequence by dependency.**
1. Name an owner for the newsletter decision; then decide whether to stop it or create a record of sign-up page visits first, since it is unscored.
2. The newsletter used "clinically proven to improve sleep", which is not on its allowed list: that goes to your review owner before any further issue.
3. Two partners have flags: the regional support group received in-kind support 38 days before its agreement, with no stated purpose and no disclosure; the forum network has no signed agreement for a contracted survey service (PE-71, PE-75, PE-80, PE-82 [INDUSTRY], if your company is bound by those codes). The remedy is your compliance or legal owner's, before further support to either.
4. Then the peer-mentor change. Widening to caregivers adds no support item; if it would, it stops for your compliance owner.

**Stops.** Off-list claim: review owner (owner not named). Partner flags: compliance or legal owner (owner not named).

**Record.** Change decision draft. Rules, decisions, scores and owners are yours. Uncleared.

Full version available on request (options table per miss, attrition context).

## What the run showed about the connector

- `analytics.rice` reads confidence as a percent. With 0.8 it returned confidence 0.008 and a score of 3.6 for the newsletter; with 80 it returned 0.8 and 360. The order did not change in this case, but mixed inputs would distort it. Proposed for the register (see build notes).
- The RICE response note ("Public registers and published literature ... Price figures on finder tools are hypotheses") does not describe a RICE run.
