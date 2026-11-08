# Intake

Ask for every missing item in one message. Do not start on assumptions.

| # | Input | If missing |
|---|---|---|
| 1 | Buyer mode (bd or investor), unit (asset, or company with the list of pipeline assets; one run per asset, then a roll-up), and the countries in scope from US, DE, FR, IT, ES, UK. Another market, or "EU" as one price, is a [GAP]. | ask in the one message; do not start on an assumption; record a [GAP] if it cannot be supplied |
| 2 | The signed market register (skill evaluate-market-opportunity-and-competitive-position): addressable patients per country with source, year and geography equal to the country's own. The market register carries a `country_patients` block for US, DE, FR, IT, ES and UK (each with source, year and geography; a country without a sourced figure is a GAP there): read the low / central / high figures as low / mid / high. Only where the block is absent may the team supply a country figure, with the same source, year and geography rules. | route to the market skill; a country without patients is a [GAP] and is not computed |
| 3 | The development risk and timeline ranges (skill estimate-development-risk-and-timeline): launch year per country as early, mid and late, and the probability of success low, mid and high (displayed only). | route to the timeline skill; a country without a launch year is a [GAP] |
| 4 | The exclusivity register (skill assess-ip-portfolio-and-freedom-to-operate): the effective exclusivity end date per country, and which patents count (the team decides). | route to the IP skill; without an end date no erosion is placed and the consequence is stated |
| 5 | List prices per country from dated public sources (references/source-register.md), per patient-year, low, mid and high, with reference and date. A team assumption is allowed only if marked public false. | a country without a list price is a [GAP] and is not computed |
| 6 | Net price assumption ranges per country (net-to-list ratio, low, mid, high), set by a named deal-team member. | net revenue is a [GAP]; no default ratio is used |
| 7 | The uptake path per country from analogs: share of the addressable patients by year from launch, low, mid and high, with the analogs and their dated sources. Adherence or persistence where sourced. | the country is a [GAP]; no default curve is used |
| 8 | Loss-of-exclusivity erosion parameters per country: price decline and volume decline (low, mid, high), years to the floor, and a source reference. | revenue after the exclusivity end year is shown unadjusted with a [CHECK]; no default curve is used |
| 9 | Market Access pack outputs, if any, with the pack state (Released or not). | the cross-check columns are empty; the ranges stand without them |
| 10 | The name of the deal-team member who sets the net price assumptions and the name of the person who will adopt a forecast. | ask; the register stays UNSIGNED and the adoption stays HUMAN ONLY |

Rules: if 2 to 4 are missing, ask. A figure you were not given is a [GAP] with the consequence stated, never an estimate. A single currency per country; a total across currencies needs a dated, sourced rate from the team. The company unit runs one register per asset; the roll-up lists assets side by side and never merges ranges across assets.
