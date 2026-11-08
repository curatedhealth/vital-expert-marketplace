# Regulatory precedent for the endpoint (how to fill regulatory_precedent)

US: look the endpoint up in the FDA Table of Surrogate Endpoints (method-standards M5), in the table that
matches adult / pediatric and non-cancer / cancer. Record `surrogate_table_listed` true or false, the
table row's "Type of Approval Appropriate for" value, and the page date. A clinical (non-surrogate)
endpoint is recorded `false` with the note "clinical endpoint". If you cannot check the table, record GAP.

EU: the register states "no EU surrogate table exists" ([CHECK] until re-opened). If an EMA qualification
opinion for the endpoint is found, cite its reference in `qualification_opinion_ref`. Otherwise precedent is
by individual assessment report, which the register cites if used.

Neither market: a regulator's acceptance of an endpoint for one indication is not acceptance for another.
The precedent row names indication and population.
