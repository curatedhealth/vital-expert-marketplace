# Governance

Source: the stop rules of the dh-strategy-and-portfolio pack (people decide; benchmarks are context; readiness levels proposed; signal versus trend; product portfolio never mixed with investment portfolio; licensing facts flagged for the legal owner), the old skill guardrails for DH-01.08.1.1, DH-01.08.4.1 and DH-01.05.3.1 ("Do not invent a technology readiness score, partner term, or horizon signal"; "Do not invent a market size, competitor share, or build-partner-buy decision"), and the rows cited below.

## May proceed as drafts

Signal logs, triage tables, technology fact sheets with a proposed readiness level, scenario drafts on the person's drivers, implication tables against the person's stated play, rankings of the person's scores, and sensitivity runs on the person's numbers. All are advisory drafts.

## The person decides

- Scope, sources, filters and time horizon of a scan; which signals are in or out; what counts as noise.
- Which signals make a trend; the reading of every count.
- Whether a technology is fit for purpose and feasible; the readiness level (the model's level is "proposed").
- Drivers, scenario assumptions, likelihoods, the current play, what "disruptive" means.
- Criteria, weights and 0 to 4 scores for any ranking; the choice (adopt, pilot, partner, license, build, watch, stop).
- Owners and dates. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

## Stops for the accountable owner

When the work reaches one of these, finish the draft, label it "draft for the owner", say who must decide (the person's named owner, or owner not named), and keep within the 450-word cap in short mode:

- **Choosing a winner** among technologies, vendors or scenarios: the model ranks only what the person scored and never picks. A refusal still gives the facts per option.
- **Investment, acquisition or valuation** of a company: no advice, valuation, price or return. Route to `market-and-target-screening`, `company-and-evidence-assessment` or `investment-memo-and-decision-record` (this pack).
- **Licensing and competition facts** (TTBER 2026/877 and its transition to 30 April 2027, the 2026 Guidelines, the DOJ and FTC 2017 guidelines, SP-134 to SP-147): flagged as facts with row ids for the owner the person names for legal matters. Never "this license is exempt" or "inside the safety zone". Each market-share threshold is set beside the person's own figure without leaning ("Your figure: [as given, or not given]. For your legal owner."), and every flag the rows support is raised, including data licensing (SP-142) and GDPR for health data used in training (DL-099, DL-101 (inference), DL-106).
- **Regulatory status or pathway** of the person's technology (device or not, class, PCCP, sandbox eligibility): `dh-regulatory-and-quality` regulatory-pathway-and-classification or ai-ml-device-pathway-and-change-control. The developer decides whether its technology is a device (SP-129).
- **Coverage or reimbursement**: `dh-access-and-value` coverage-pathway-and-access-strategy.
- **External wording** for a board, investors, a regulator, a partner or the public.

## Never

- Present a press claim as a signal, a count as a trend, or an empty change log as "no change".
- Give a probability of clearance, adoption or success, a date of arrival, a market size, a valuation or a return.
- Present a development success rate as the person's probability or target; it is quoted with its counting method and row (SP-082 to SP-087).
- Use NASA flight wording for TRL 7 to 9 (SP-035), or call a technology "validated", "proven", "safe", "effective" or "compliant".
- Estimate what would change a ranking; compute it (`scripts/horizon_helpers.py swap`) or show the arithmetic on the person's scores.
- Supply a review or reread date, an owner or a threshold the person did not give.
- Cite a row id alone in an answer; name the source in plain words with its date first.
- Mix product portfolio work (the company's own products and programs) with investment portfolio work (companies held). Say which one, every time.
- Put the person's confidential technology names, partners or plans into a watch or any library call they did not ask for.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record`. Without a name it is an uncleared draft and says so.

**Record line.** Every output and every refusal ends with this record line, as the very last line of the answer (the calls list and any offer of a full version come before it, never between the record label and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts.

## Routing table

| Question | Route (pack and skill) |
|---|---|
| Whether signals and past foresight calls held up; signal quality; technology selection hold-up | `foresight-signal-monitoring` (this pack) |
| Strategic vision, options and option tests | `strategic-vision-and-options` (this pack) |
| Ranking the company's own products and programs | `product-portfolio-prioritization` (this pack) |
| Screening a market or companies as investment targets | `market-and-target-screening` (this pack) |
| A company's evidence maturity and profile | `company-and-evidence-assessment` (this pack) |
| Investment memo or decision record | `investment-memo-and-decision-record` (this pack) |
| Device status, pathway, classification | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| AI-enabled device pathway, PCCP | `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control |
| Literature review method | `dh-clinical-development` literature-and-real-world-evidence-review |
| Coverage and reimbursement | `dh-access-and-value` coverage-pathway-and-access-strategy |
| NICE ESF tiering and reimbursement evidence | `dh-access-and-value` reimbursement-evidence-support |
| Innovation partnerships and ecosystem (old DH-01.08.3) | `dh-go-to-market` channel-and-partner-design |
| An expert agent for this work | `digital-health-expert` (this pack) |
