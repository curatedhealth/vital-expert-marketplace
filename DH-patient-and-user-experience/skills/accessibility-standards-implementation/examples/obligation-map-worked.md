# Worked example: A1 obligation map

Live connector calls on 19 October 2026. The person and their facts are written for this example; the rows and the connector responses are real (`examples/live/`).

**Request:** "We're a 60-person US company. Our medication app (native, some screens are web views) is licensed to US health systems, most of which take Medicare and Medicaid money, and to two NHS trusts in England. In Germany we sell a consumer subscription inside the app. Which accessibility rules apply, which WCAG version, and by when?"

**Calls made**

1. `regulatory-dh.retrieve_guidance {query: "WCAG", limit: 5}`: five passages, all `source_url` "[GAP]"; none usable.
2. `regulatory-dh.retrieve_guidance {query: "web content and mobile apps accessibility Section 504 compliance date", limit: 5}`: no passage.
3. `verify.qualify_source {url: "https://www.govinfo.gov/content/pkg/FR-2026-05-11/pdf/2026-09266.pdf"}`: tier bronze, publisher Federal Register.
4. `verify.check_claim` with that source object and the rule's own sentence as passage: "11 May 2027" returned "partial"; the superseded "11 May 2026" also returned "partial". The date below rests on reading the passage, not on the status.
5. `verify.qualify_source {url: "https://www.w3.org/TR/WCAG22/"}`: "inadmissible, no provenance". W3C facts are cited to the rows.

## Answer (short mode)

**On your facts, three sets of rules may reach your app, and they cite three WCAG versions.** Your US health-system customers, if they receive HHS federal financial assistance, must make apps they provide "through contractual, licensing, or other arrangements" meet WCAG 2.1 A and AA, from 11 May 2027 for recipients with 15 or more employees (UX-US-15, UX-US-16), a date moved from 11 May 2026 by the HHS interim final rule effective 7 May 2026 (UX-US-18). Interim: a later final rule could change it. The NHS requires WCAG 2.2, including the six new A and AA criteria (UX-UK-22, UX-UK-23). Whether the EAA reaches your German subscription is an inference, not a stated rule.

| Instrument | Applies if | Cites | Rows |
|---|---|---|---|
| HHS Section 504 | your customer is an HHS recipient and provides your app (your contract terms decide how this passes to you) | WCAG 2.1 A and AA; 11 May 2027 (15 or more employees), 10 May 2028 (fewer) | UX-US-15 to UX-US-18 |
| Section 1557, 92.204 | same customers | Section 504 "as interpreted consistent with title II of the ADA"; no WCAG version of its own | UX-US-21 |
| NHS service manual | you supply NHS trusts' services | WCAG 2.2; six new A and AA criteria required | UX-UK-22, UX-UK-23 |
| UK PSBAR | the trusts as public sector bodies `[GAP]` on how it reaches a supplier | four principles, no version | UX-UK-02, UX-UK-03 |
| European Accessibility Act | the subscription is an "e-commerce service" (inference from the definition; the Directive has no health category) | EN 301 549 V4.1.1 is one voluntary means; OJ citation not checked `[GAP]` | UX-EU-03, UX-EU-04, UX-STD-29 |

Not mapped: Section 508 and ADA Title II (you named no federal or state-government customer).

**Where versions differ:** 2.1 AA to 2.2 AA adds six criteria (2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8) and drops 4.1.1 Parsing, which a 2.1 policy may still require you to test and report (UX-STD-07, UX-STD-08). Your web views are tested under EN 301 549 clause 11 (UX-STD-32).

**Open questions:** do your contracts pass the customers' 504 duty to you; which EU entity sells the subscription (the EAA microenterprise exemption needs fewer than 10 staff, UX-EU-07, so it does not fit 60 staff); which German law transposes the EAA for you `[GAP]`.

**Stops:** whether each instrument binds you is your legal owner's call. Nothing here says the app conforms.

**Record:** Obligation map draft on facts you supplied. Not a legal opinion. Uncleared. AI-assisted.

The full version adds exceptions, burden routes and the instruments left out.

## What this example shows

- The guidance store could not answer; the sourced rows did, with the moved date and its instrument.
- Verify could not tell the current date from the superseded one; the skill relies on the passage.
- The EAA line is labeled an inference, and the role questions stay open rather than being answered for the person.
