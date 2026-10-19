# Worked run: B1 Inclusive change (with A1 in short form)

Run of 19 October 2026. The product, the counts and the scores are illustrative: the counts are in `examples/sample-data/rpm_equity_illustrative.csv` (written for this example, not real data) and the scores were typed for the live measurement call (`examples/live/mcda_inclusive_change.json`). They are presented here as an example person's inputs. The connector output is real.

## The request

"We run a remote blood pressure monitoring program for a US health system customer. Enrollment is lower for Spanish speakers. Our options: Spanish onboarding with human-reviewed translation, a phone-assisted enrollment line, or a low-bandwidth mode. Here are our scores and weights. Rank them. Our small-cell rule is 11; compare against English speakers. Owner is Ana Ruiz's enrollment team; target release is 4.3."

## Calls made

1. `python scripts/equity_compare.py examples/sample-data/rpm_equity_illustrative.csv --min-cell 11 --reference "preferred language=English" --reference "age band=45-64" --reference "SVI band (US database)=0 to 0.25"` (local, no connector)
2. `analytics.mcda` with the person's scores and weights (counted; saved in `examples/live/mcda_inclusive_change.json`)

## Output (short mode)

**Answer.** On your scores, Spanish onboarding with human-reviewed translation ranks first (77.5), the phone-assisted line second (70), the low-bandwidth mode third (58.75). Your enrollment team (Ana Ruiz) owns it; release 4.3 carries it. Open decision: whether release 4.3 also carries the evidence record monitoring needs (below).

**Group, step, barrier.** Spanish-preferring patients, enrollment step, onboarding offered in English only (your description).

**What your counts show (your rule: counts below 11 suppressed).** Reach (enrolled and transmitting, your definition) for Spanish 51.8 percent (95 percent interval 47.6 to 55.9; 290 of 560) against English 68.0 percent (65.6 to 70.3; 1,020 of 1,500): a difference of 16.2 percentage points, ratio 0.762. "Other" languages are suppressed (8 reached) and Vietnamese is suppressed as a complement so "Other" cannot be derived from the total. 174 of 2,400 eligible (7.2 percent) have no language recorded. No verdict: whether this gap misses a rule is yours (monitoring skill B1).

**Options.**

| Option | Basis | Value (your scores) |
|---|---|---|
| Spanish onboarding, human-reviewed translation | 92.201 meaningful access (PE-107); human review of machine-translated critical text (PE-108) | 77.5 |
| Phone-assisted enrollment line | 92.201 language help free, timely (PE-107); alternate path: your evidence | 70 |
| Low-bandwidth mode | No row; your evidence on connectivity `[GAP]` for a rule | 58.75 |

**Ranking note.** "Barrier addressed at the step" separates the top two (30 against 22.5 points); the phone line leads on "group reach expected" (35 against 26.25). Moving weight from "barrier addressed" to "group reach expected" changes the order at a shift of 0.15 (reach 0.50, barrier 0.15): Spanish onboarding loses 25 points per unit of weight moved ((3 minus 4) divided by 4, times 100) and the phone line gains 25, closing the 7.5-point gap at 0.15. Your weights decide.

**Evidence definition for monitoring.** Change: Spanish onboarding flow in 4.3. Group: patients with Spanish recorded as preferred language. Record of use: enrollment completed in the Spanish flow. Denominator: eligible Spanish-preferring patients. First period: the first full quarter after 4.3 ships (yours to set). Not recorded: which flow a patient used `[GAP]` until 4.3 logs it.

**Stops.** Whether 92.201 binds your customer, and any statement that the program meets it, is your customer's and your legal owner's call. No public claim that the program is "accessible" or "equitable". Accessibility conformance of the new flow: dh-user-experience accessibility skills.

**Record.** Inclusive change draft on your scores and illustrative counts. Uncleared.

Full version available on request.

(Short mode word count, excluding the calls list and the table's basis column: about 410.)
