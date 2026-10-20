# Software sold with or for a drug: what changes in the go-to-market

Use this when the product is software sold with a drug, for a drug, or by or with a drug maker (a companion app, an adherence app paired with a medicine, a DTx a pharma partner co-promotes). It lists only what the sourced rows say changes for segments, routes and motions. Everything else is `[GAP]`. The regulatory status of the combination (device, drug labeling, combination product) is not decided here: route it to `dh-regulatory-and-quality`.

## What the sourced rows say

| Area | What changes | Row |
|---|---|---|
| Germany: DiGA route | A DiGA "meant for use with a specific aid or drug" is excluded from the statutory DiGA claim. An app tied to one drug cannot use the DiGA prescription or fund-approval route. | CP-DE-04 (also Market Access `germany-diga.md`, "Eligibility: exclusions") |
| Germany: partner terms | DiGA manufacturers may not make agreements with drug makers that could restrict patients' choice or physicians' therapeutic freedom in choosing drugs. Any co-promotion or bundle with a drug maker stops for the legal owner. | CP-DE-07 |
| Germany: advertising | The HWG covers advertising for both drugs (Arzneimittel) and medical devices, so joint material falls under it for both parts. | PC-DE-01 |
| US: free items to patients | OIG approved one drug maker loaning limited-function smartphones to needy patients so they could use an app paired with a sensor-embedded drug; even the restricted phone was remuneration, and the safeguards (not advertised, need-based, two 12-week periods) carried the outcome. | CP-US-39, CP-US-40, CP-US-41 |
| US: who the CMP reaches | OIG does not treat drug makers as "providers, practitioners, or suppliers" for the beneficiary CMP unless they own billing entities; the anti-kickback statute still applies to anything of value that induces a purchase payable by a Federal program. | CP-US-42, CP-US-01 |
| US: reliance | An advisory opinion protects only its requestor and only the facts certified. AO 19-02 is an example, not a safe harbor for anyone else. | CP-US-43 |
| US: intended use | Intended use is shown by labeling, advertising, statements and distribution circumstances. Copy that ties the software to a drug can change what the software is. | PC-US-17, PC-US-20 |
| EU: intended purpose | Software used "alone or in combination" for a medical purpose is a device, and intended purpose includes promotional and sales material. | PC-EU-04, PC-EU-03 |
| US: DMHT payment | DMHT payment is limited to use in line with the device's FDA classification. A drug-companion use outside that classification does not use the code. | CP-US-64 |

## Not sourced: say `[GAP]` and route

- Whether the product is a combination product, and which FDA center or EU procedure applies: not in the research files. Route to `dh-regulatory-and-quality`. (The shared regulatory research, `REG_PATHWAYS_SUBMISSIONS.md` row US-28, notes only that FDA generally recommends Enhanced Documentation for device constituents of combination products; that is the regulatory skill's to apply.)
- FDA rules on software referenced in or distributed with drug labeling, and drug-promotion rules for the drug part: not sourced `[GAP]`.
- EU rules for a drug that integrates a device, and England NHS buying for drug-companion software: not sourced `[GAP]`.
- US commercial payer or pharmacy-benefit coverage for drug-companion software: not sourced `[GAP]`; payer questions go to the Market Access pack.
- Pricing a bundle with a drug: Market Access and the pricing skill; not sourced here.

## How the person uses it (method, not a sourced rule)

In A1, add a "with or for a drug" flag to each segment row and fill the route and channel cells from the table above. A segment whose route depends on a fact listed as `[GAP]` keeps the gap in its route cell. In B1, any motion that involves a drug maker as partner, co-promoter or payer of free items carries the stop from `governance.md` for the legal or compliance owner.
