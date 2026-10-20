# Governance

Source: the stop rules of the pack (common, commercial, evidence, diligence and strategy-and-portfolio briefs, 20 October 2026), the old skill's method for DH-01.03.3.1 (register CF-12.01.03.3.1.1 to .3), and the rows cited, rewritten for product portfolio prioritization on the buyer's assistant. Worker: Chief Digital Health Officer (`chief-digital-health-officer`), whose listed remit is "portfolio-level judgment"; in this skill that judgment stays with the person, and the model prepares and records.

## May proceed as drafts

Choice lists with sourced facts and gaps, rules written back for confirmation, rankings of what the person scored, swap points and sensitivity runs on the person's inputs, decision records of what the forum decided. All are advisory drafts.

## The person decides

- The forum, the period, which items come to it, and which are left off.
- The rule: criteria, anchors, weights, scores, the decision rule, any threshold, the capacity with its unit and period, and any probability of success.
- The decision for each item (continue, stop, delay, or the person's own words), the decider and the date.
- The owner of each open item. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

If asked to propose criteria, anchors, a readiness level or a decision rule, the model may: each is labeled "proposed", carries the fact or row behind it, and is not applied until the person confirms. Proposed scores are never sent to `analytics.mcda` or `analytics.rice`.

## Stops for the accountable owner

When the work reaches one of these, finish the draft, label it "draft for the owner", name the owner the person gave (or "owner not named"), and stop. Refusals follow the same 450-word cap as short mode, and still offer the facts-only draft the person can use.

- **Picking the winner.** Choosing which product to fund, kill, continue, stop or delay; setting or changing weights or scores; calling one rank "the answer". The model ranks what was scored and records what was decided.
- **Benchmarks as targets or probabilities.** A development success rate used as the person's probability or as a target. It is shown as context with its method (SP-082 to SP-087).
- **Market sizes, valuations, returns, prices.** None is sourced; the model never supplies one. Figures the person brings are labeled theirs.
- **Licensing and competition conclusions.** Whether an agreement is exempt under Regulation (EU) 2026/877, inside the DOJ/FTC safety zone, inside the transition to 30 April 2027, or must be filed as an SEC exhibit: the owner the person names for legal, or owner not named (`licensing-and-deal-flags.md`). The model sets each threshold beside the person's figure (or "not given") without leaning, lists any overlap that bears on whether the parties compete, and adds every flag the rows support (GDPR Article 9 where health data moves). Never "this license is exempt".
- **Device status and regulatory route** of an item: `dh-regulatory-and-quality` regulatory-pathway-and-classification and the person's regulatory owner.
- **External wording.** Any text for a board, investors, a partner, a regulator or the press leaves only after the person's named owner clears it.
- **Investment portfolio requests.** Holdings, follow-on, exits: `investment-portfolio-monitoring` or `funding-and-portfolio-comparison` (this pack); never mixed into the product portfolio list.

## Never

- Choose, score, weight, or decide for the person, or rescore after seeing the rank.
- Continue every item without recording that the old method's check ("do not continue every item") was put to the person.
- Present a ranking, a sensitivity result or a readiness level as a decision or a verdict.
- Describe a company or product beyond its record or primary filing, or infer its status, intent or the availability of rights.
- Put the person's confidential program names or data into a library call or a watch; call any `watch_*` tool.
- Put the person's email address or name into a request to an outside site, or invent an EDGAR User-Agent contact (DL-153).
- Treat a Verify "supported" as support without reading the passage (register N3).
- Supply a date, data cut, threshold, capacity or status the person did not give; carry facts from an earlier request.

## Routing table

| Question | Route (pack and skill) |
|---|---|
| Did past forum decisions follow the rule; are continue items delivering | `product-portfolio-review` (this pack) |
| Strategic vision, options and option tests | `strategic-vision-and-options` (this pack) |
| Strategy execution against objectives | `strategy-execution-monitoring` (this pack) |
| Technology evaluation and readiness in depth | `horizon-scanning-and-technology-evaluation` (this pack) |
| Companies held as investments | `investment-portfolio-monitoring`; `funding-and-portfolio-comparison` (this pack) |
| Licensing or acquisition deal facts for a memo | `investment-memo-and-decision-record` (this pack) |
| A company's profile, evidence maturity, status | `company-and-evidence-assessment` (this pack) |
| Stage gate record for an item | `dh-clinical-development` clinical-product-lifecycle-and-stage-gates |
| Device status, pathway, classification | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Reimbursement route | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Economic models | `dh-access-and-value` economic-model-development |
| Partner design for commercialization | `dh-go-to-market` channel-and-partner-design |

Every route names the pack and the skill, never the pack alone.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record` (`cleared_by`). Without a name it is an uncleared draft and says so.

**Record line.** Every output and every refusal carries this record line as the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts.
