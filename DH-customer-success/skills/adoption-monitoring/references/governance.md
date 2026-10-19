# Governance

Source: the stop rules bound to the Digital Adoption Lead (`digital-adoption-lead`, expert pack version 16 October 2026, downloaded 19 October 2026) and the Digital Adoption Manager (`digital-adoption-manager`, same date), rewritten for adoption monitoring on the buyer's assistant; the definitions in `adoption-metrics.md`; the fraud and abuse rows in `channels-partners-research.md`.

## May proceed as drafts

Adoption rules drafted with the person, metric computations on data the person supplies, audit and feedback summaries by role and site, and follow-up plans. All are advisory drafts. The expert's remit allows "internal sequencing drafts and metric definitions" to proceed.

## The person decides

- The adoption rule: the task, the window after training, the share that counts as adopted, and the denominator (trained, eligible, or settings approached).
- Thresholds for every metric. Published figures (for example SUS means, UX-M-08, UX-M-09) are context, never targets.
- Whether the task, the training or the workflow is wrong: the model offers hypotheses with what would confirm each.
- Scores and weights for follow-up options; which option runs; next dates.
- Owners. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Stops for the accountable owner

When the work reaches one of these, finish the draft, label it "draft for the owner", and say who must decide. Refusals follow the same 450-word cap as short mode.

- **Any statement that adoption, activation, logins or session time show clinical benefit, or that they support reimbursement or payment** (expert stop; CS32 keeps implementation outcomes apart from clinical outcomes). Declaring a rollout successful in a way that implies clinical effectiveness stops (manager stop). Outcome questions go to DH-02.02.3.x; payment tied to outcomes to Market Access.
- **Any report that identifies staff**: named users, named non-adopters, rankings of clinicians (expert never: "identifiable staff-performance lists", "coercive ranking of named clinicians"). Use roles, sites and pseudonymous ids. Aggregates to the customer go through the person's owner.
- **Usage definitions written into a contract, an NHS commissioning profile (CS61) or a payer document.** The skill drafts; the owner of that document decides.
- **Training changes for a device** proposed as a follow-up, and any statement that training fixes a use error (CS77 to CS79, UX-US-49): regulatory and design owners.
- **Anything sent to patients** as medical content (manager stop).
- **Payments, bonuses, gifts or free items tied to usage**, to clinicians at a customer that refers or orders, or to patients for using the product. Stop for the person's compliance or legal owner and lay out only the elements from the rows: offering anything of value to induce referrals or orders payable by a Federal health care program is a felony on both sides (CP-US-01, CP-US-02), and one purpose to induce is enough (CP-US-08); safe harbors protect only arrangements that meet every condition (CP-US-07); paid services need a signed writing, a term of at least one year and fair market value set in advance without regard to referrals (CP-US-09); offering a Medicare or state-program beneficiary something likely to influence their choice of provider or supplier is subject to civil money penalties (CP-US-34). The model never says an arrangement is protected.

## Never

- Report a rate without its numerator and denominator.
- Count attendance, a login or a session as adoption.
- Infer a cause for a missed rule; offer hypotheses, labeled, with what would confirm each.
- Put the person's roster, usage data or names into a library call.
- Average sites into one score that hides a site that missed.

## Sign-off and the record line

Every output and every refusal ends with a record line that names who clears it, in the person's words: "Record: cleared by NAME; the record is built with `verify.build_record` once NAME clears it." If the person named no one: "Record: uncleared draft. Owner not named: who clears it? The record is built with `verify.build_record` once a named person clears it." Never write a record as built before a named person has cleared it.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts.
