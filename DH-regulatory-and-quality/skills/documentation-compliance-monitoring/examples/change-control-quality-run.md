# Worked example: "Audit our change log before the FDA inspection"

Tasks A2 then B1. The change log is illustrative (`change-log-illustrative.csv`, eight changes to a fictional insulin dose app); the recall context is real library data from 19 October 2026 (`examples/live/safety_events_QRX_2026-10-19.json`). Shown so the model sees the shape of a good answer, not to be reused as fact.

## Calls and commands

| Step | Call or command | What came back |
|---|---|---|
| A2 checks | `python3 scripts/change_log_check.py change-log-illustrative.csv --rules rules-illustrative.json` | 8 changes, 16 findings; full output in `change-log-check-output.md` |
| Context | `regulatory-dh.search_safety_events {jurisdiction: "US", product_code: "QRX", limit: 10}` | 10 recall rows; CGM app version recalls (Class I, 24 July 2025 and 28 August 2025; Class II, 14 April 2026); one row a sensor-theft recall, not a software defect; rows carry no product code |

The person set two rules: no change without an assessment, and no change implemented before approval; no owners named.

## The answer the skill should give for A2 (short mode)

**Answer.** Your log holds 8 changes (2 March to 15 July 2026). Two of your rules are not met: 2 of 8 changes have no impact assessment (CR-0204, CR-0208), and 3 of 8 were implemented before approval (CR-0202, CR-0203, CR-0208). Owner for both rules: not named. Who owns them?

**Hazard-touching changes first.**
- CR-0202, background alert processing: implemented 15 April 2026, assessed 20 April, approved 22 April; the "no submission" decision has no rationale; no risk file review reference. Rows QS34, QX14, QS22.
- CR-0203, dose rounding: implemented 6 May 2026, approved 7 May (one day later). Rationale and risk review recorded.
- CR-0206, unit conversion table: no risk file review reference (QS22).

**Other findings.** CR-0205 has an approval date and no approver name. Five changes sit on two items (app-ios: CR-0201, CR-0202, CR-0205; cloud-api: CR-0207, CR-0208) with no aggregate assessment reference (QX12, QX13).

**Context, not evidence.** Released CGM app versions have been recalled for a background-processing defect (Class II, 14 April 2026, versions 2.9.0 through 2.11.2), which is the kind of change CR-0202 made.

**Not measurable.** None: the log has every column the checks use.

AI-assisted draft, uncleared. Want the repair plan (B1)?

## B1, after the person's team scored

The person's two reviewers scored each finding with MDSAP's inputs (QS45), by their choice. The model ranks only those scores:

| Rank | Finding | Scores (who) | Proposed repair | Owner | Date |
|---|---|---|---|---|---|
| 1 | CR-0202 implemented before assessment and approval, no rationale, no risk review | 4 (both reviewers) | New dated assessment stating it is late, walking the sibling skill's question sheet; risk file review; owner decides whether a CAPA is warranted (QS18) | owner not named | not set |
| 2 | CR-0208 no assessment, implemented with no approval | 4 (both reviewers) | Same pattern | owner not named | not set |
| 3 | CR-0204 no assessment (labeling) | 3 | Late assessment, dated today | owner not named | not set |

Ties are shown as ties (ranks 1 and 2 share a score; listed in log order). Unscored, so unranked: CR-0203 (approved one day after implementation), CR-0205 (no approver name), CR-0206 (no risk review), and the two aggregate findings. **Decision needed:** whether the release-before-approval pattern (3 of 8) goes to CAPA. That is the owner's call. No past entry is edited.

## Why this is a good answer

It states counts with their base and the log's period. It puts hazard-touching changes first by fact, not by its own severity score. It names no owner and asks. It treats a public recall as context. In B1 it ranks only what people scored, shows the tie, and never proposes editing a past entry.
