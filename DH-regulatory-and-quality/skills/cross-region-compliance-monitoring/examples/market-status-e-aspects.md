# Worked example: market status by region (A1)

Request: "Where is Brainomix 360 e-ASPECTS authorized according to the registers, what changed this year, and which registration dates are coming up for a product like it in the US, EU, UK, Canada, Switzerland and Australia?"

Real library data, retrieved on 19 October 2026. The obligations run uses example inputs a person would give (dates, GB basis, Canadian certificate); they are not facts about Brainomix. Shown for the shape of a good answer, not to be reused as current fact.

## Calls made

| Call | Arguments | Saved output |
|---|---|---|
| `regulatory-dh.list_jurisdictions` (free) | none | `live/list_jurisdictions_2026-10-19.json` |
| `regulatory-dh.get_market_status` | `name` "Brainomix 360 e-ASPECTS" | `live/get_market_status_brainomix_e-aspects_2026-10-19.json` |
| `regulatory-dh.search_devices` | `query` "Brainomix", `software_only` "false", `limit` 25 | `live/search_devices_brainomix_2026-10-19.json` |
| `regulatory-dh.get_register_deltas` | `manufacturer` "Brainomix", `since` "2026-01-01" (plus two `get_deltas` scopes) | `live/register_deltas_2026-10-19.json` |
| `regulatory-dh.retrieve_guidance` | single keywords and two questions | `live/retrieve_guidance_2026-10-19.json` |
| `scripts/obligations_table.py` | `markets_example.json` | `obligations_table_2026-10-19.md` |

## What the tools returned (abridged)

- `get_market_status`: three rows that disagree (two US true / EU false, one US false / EU true). Merged: records in both.
- `search_devices`: US 510(k) records for e-ASPECTS, class 2, K243294 (14 February 2025) and K221564 (23 February 2023); EU_MDR Class IIb record ++B720EASPECTSCEGK and three EU_MDD Class IIa records, all "On the EU market", no decision dates.
- `get_register_deltas`: no rows; "no watch is registered for this scope; the change log has not started". The same search shows a Brainomix US decision on 12 June 2026 (K260406, Brainomix 360 Hyperdensity), inside the window.

## The answer the skill should give (short mode)

**Next dates and changes.** For a product placed in the markets below, as of 19 October 2026: the FDA annual registration window is open until 31 December 2026 (JX-29), 73 days away; the Health Canada license statement is due before 1 November 2026 (JX-33), 13 days away; EUDAMED UDI/device registration for a device first placed before 28 May 2026 is due by 28 November 2026 (JX-39), 40 days away. In 2026 the registers show one new Brainomix US decision (K260406, 12 June 2026), for a different product; nothing new is stored for e-ASPECTS. The library's change log has not started for this scope, so this comes from comparing decision dates, not from the log.

| Region | Library result | Record | Retrieved |
|---|---|---|---|
| US | Found | 510(k), class 2, K243294 | 13 October 2026 |
| EU | Found, two regimes | MDR Class IIb ++B720EASPECTSCEGK; three MDD Class IIa records | 14 October 2026 |
| GB | Register not loaded | | |
| CH | Register not loaded | | |
| CA | Loaded, not searchable | check MDALL | |
| AU | Register not loaded | | |

| Region | Duty | Date | Row |
|---|---|---|---|
| GB | CE (MDR) accepted until | 30 June 2030 | UK-03 |
| GB | Indefinite recognition | proposal, not law | UK-05 |
| CH | Swissmedic registration (devices placed from 1 July 2026) | by 31 December 2026 | JX-43 |
| AU | Registration duties | [GAP] | |

**Confirm with the owner.** The Canadian QMS certificate copy in the example inputs was due 1 April 2026 (JX-35); that date has passed, so confirm it was sent. The EU vigilance module date is not published (JX-38). MHRA registration renewal is not sourced (UK-01).

**Record.** Uncleared draft. AI-assisted. Want the full version with the complete obligations table?

## Why this is a good answer

Dates come with their basis and the days from the as-of date, without pressure language. The empty change log is not read as "no change", and change is found another way. The two EU regimes are reported by identifier without explanation. Passed dates are things to confirm, not misses. The GB proposal is kept apart from the law.
