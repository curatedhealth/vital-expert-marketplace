# Worked example: A1 co-design trace (with an A2 citation check)

Run on 19 October 2026. The person's files are illustrative (`sample-data/`; no real product, session or person). The citation check uses real library calls (`live/verify_gripp2.json`).

**Request:** "Our version 2.4 release notes say three changes were 'designed with patients': CH-12, CH-13 and CH-14. Can we stand behind that? Here are our changes, insight log and captures. CH-14 was in the backlog from 15 June 2026. Also, our write-up says 'GRIPP2-SF has five items and suits studies where patient and public involvement is a secondary focus'; is that cited correctly?"

**Calls and runs**

1. `scripts/insight_tracker.py check changes.csv insights.csv captures.csv`: no identifiers found.
2. `scripts/insight_tracker.py trace sample-data/changes.csv sample-data/insights.csv sample-data/captures.csv`
3. `scripts/insight_tracker.py tally sample-data/captures.csv --repeat 2` (the person's rule)
4. `verify.qualify_source {doi: "10.1136/bmj.j3453", question: "What items should a report of patient and public involvement include?"}`: tier gold, status current.
5. `verify.check_claim {claim: {text: "GRIPP2-SF has five items and suits studies where patient and public involvement is a secondary focus."}, passage: {text: "GRIPP2-SF includes five items on aims, methods, results, outcomes, and critical perspective and is suitable for studies where PPI is a secondary focus.", locator: "Abstract, Results; PMC5539518"}, source: {doi: "10.1136/bmj.j3453"}}`: supported.

## Answer (short mode)

**One of the three changes credited to co-design traces to what participants said: CH-12 (two-tap reading entry).** The other two do not support "designed with patients" as written.

| Change | Insight | Evidence | Trace status |
|---|---|---|---|
| CH-12 two-tap entry | I1 | 3 patients, 2 sessions; "I stopped logging after the first week because every entry took six taps" | Traced |
| CH-13 onboarding carousel | none | none | Credited, no capture link: not from this research (R-18) |
| CH-14 larger numerals | I3 | 2 patients, 2 sessions | Planned before capture: in backlog 15 June 2026, first linked capture 4 August 2026. The sessions support it; they are not its origin (R-14) |

Trace coverage: 1 of 3 credited changes. You set no coverage rule, so there is no verdict.

**Also in the log:** I3 is accepted without a product version in the insight log, although CH-14 shipped in 2.4 (R-12). Update the log so later traces hold.

**What it means for you:** a release note that says all three changes were designed with patients is not supported by these records for CH-13 and only as support, not origin, for CH-14. That wording, and any "co-designed" claim in marketing, stops for your accountable owner; owner not named. A draft for the owner could say: "Two-tap entry was changed after patients in our sessions told us logging took too long."

**Citation check:** your GRIPP2-SF sentence matches the paper's abstract (PE-91; Verify: supported, source tier gold). Note that Verify returned "partial", not "contradicted", for a deliberately wrong version of the sentence, so a "supported" result was accepted here only because the passage was read and says the same thing.

**Record:** Trace draft on your files. A trace shows provenance, not effect. AI-assisted. Uncleared draft; a named person clears it, then the record is built with verify.build_record.

The full version adds the per-change table with quotes, the accepted-without-version list and the session fit for the sessions behind each trace.

## What this example shows

- The backlog date turned a "co-designed" change into "supported by co-design".
- No verdict on coverage without the person's rule.
- The Verify result was accepted only with a passage read in the same direction (register N3).
