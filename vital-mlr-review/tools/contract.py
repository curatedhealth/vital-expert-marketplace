"""Locked product constants (MLR Review v0.2, 24 October 2026)."""

from __future__ import annotations

PRODUCT = "mlr-review"
DISPLAY_NAME = "MLR Review"
KEY_PREFIX = "vmlr_"
PLUGIN = "vital-mlr-review"
SCOPE_READ = "mlr-review:read"
SCOPE_RECORD = "mlr-review:record"
MCP_PATH = "/api/mcp/mlr-review"
METHOD_VERSION = "2026-10-24.2"

LIABILITY_LINE = (
    "This prepares material for human MLR review. "
    "It is not medical, legal, or regulatory approval."
)

FORBIDDEN_PHRASES = (
    "approved for use",
    "mlr approved",
    "mlr_reviewed",
    "cleared for promotion",
    "regulator approved this copy",
    "fda approved this copy",
    "ema approved this copy",
    "mhra approved this copy",
    # TEH-RDY-013: clearance synonyms seen in approval-pressure prompts
    "cleared for use",
    "fda compliant",
    "regulator-cleared",
    "regulator cleared",
)

# TEH-RDY-019: regulator-cleared forms the literal list misses, incl. slash lists
# such as "FDA / EMA / Swissmedic cleared" (the last regulator in a list binds the verb).
# Matched case-insensitively. Same handling as FORBIDDEN_PHRASES everywhere they are used.
FORBIDDEN_PATTERNS = (
    r"\b(?:fda|ema|swissmedic|bfarm|mhra|pei|regulator|regulatory)\s*[-/ ]*\s*(?:cleared|approved for use|compliant)\b",
)

AUDIENCES = ("hcp", "patient", "payer", "internal", "mixed")
CHANNELS = ("promo", "scientific_exchange", "med_info", "digital", "congress", "other")


# TEH-RDY-057: two ideas share the word "channel". The rule-pack catalogue's `channel`
# (rulesets/REGISTRY.json) is the communication INTENT -- the ruleset key. The delivery MEDIUM
# people name (email, print, digital display, congress, social ...) is recorded for the record and
# NEVER binds a rule pack. Rule packs bind on market + audience + intent only.
INTENTS = ("promo", "scientific_exchange", "med_info", "other")
# Transparent intent-word mapping (reported back to the person, never silent).
INTENT_SYNONYMS = {
    "promo": "promo",
    "promotional": "promo",
    "promotion": "promo",
    "scientific exchange": "scientific_exchange",
    "sciex": "scientific_exchange",
    "sci ex": "scientific_exchange",
    "med info": "med_info",
    "medical information": "med_info",
    "mi": "med_info",
    "other": "other",
}
# Delivery media: recorded only. "digital" and "congress" stay valid packet-schema values but are
# media, not intents, so they never select a rule pack.
MEDIA = (
    "email", "e mail", "rep triggered email", "print", "printed", "digital", "digital display",
    "display", "banner", "web", "website", "webpage", "web page", "online", "social", "social media",
    "congress", "congress booth", "booth", "exhibition", "video", "webinar", "leave behind",
    "detail aid", "e detail", "edetail", "letter", "mailer", "direct mail", "sms", "text message",
    "app", "podcast", "newsletter", "poster", "slide deck", "slides", "deck", "brochure", "leaflet",
    "advertisement", "advert", "journal ad", "tv", "radio", "face to face", "meeting", "portal",
)
_FILLER = {"a", "an", "the", "and", "via", "by", "in", "on", "as", "of", "for", "piece", "material",
           "materials", "content", "communication", "communications", "campaign", "channel", "use",
           "delivered", "sent", "item", "asset"}


def _norm_term(value: object) -> str:
    import re as _re
    v = str(value or "").strip().lower().replace("_", " ").replace("-", " ").replace("/", " ")
    return _re.sub(r"\s+", " ", v).strip()


def _find_terms(tokens: list, vocab) -> tuple:
    """Longest-first whole-token phrase matches; returns (matched phrases, remaining tokens)."""
    phrases = sorted({_norm_term(p) for p in vocab}, key=lambda p: -len(p.split()))
    rest = list(tokens)
    found = []
    for phrase in phrases:
        pt = phrase.split()
        n = len(pt)
        i = 0
        while i <= len(rest) - n:
            if rest[i:i + n] == pt:
                found.append(phrase)
                del rest[i:i + n]
            else:
                i += 1
    return found, rest


def split_channel(channel: object = None, intent: object = None, medium: object = None) -> dict:
    """Separate the ruleset intent from the delivery medium (TEH-RDY-057).

    Returns {"intent": <INTENTS key or "">, "medium": <str or "">, "mapping": [..], "unmatched": <str>,
    "conflict": bool}. Every mapping from a supplied word to a key is listed in "mapping" so the
    answer can report it. A medium never becomes an intent. Unknown values are returned in
    "unmatched" (never mapped, never substituted)."""
    intents = {_norm_term(k): v for k, v in INTENT_SYNONYMS.items()}
    intents.update({_norm_term(k): k for k in INTENTS})
    media = {_norm_term(m) for m in MEDIA}
    found_intents = []
    found_media = []
    mapping = []
    unmatched = []
    explicit_medium = str(medium or "").strip()
    for field, raw in (("intent", intent), ("channel", channel)):
        supplied = str(raw or "").strip()
        if not supplied:
            continue
        t = _norm_term(supplied)
        if t in intents:
            key = intents[t]
            found_intents.append(key)
            mapping.append({"field": field, "supplied": supplied, "read_as": "intent", "value": key})
            continue
        if t in media:
            found_media.append(supplied)
            mapping.append({"field": field, "supplied": supplied, "read_as": "medium", "value": supplied,
                            "binds_rule_pack": False})
            continue
        toks = t.split()
        ints, rest = _find_terms(toks, list(intents))
        meds, rest = _find_terms(rest, media)
        if (ints or meds) and all(tok in _FILLER for tok in rest) and len({intents[i] for i in ints}) <= 1:
            for i in ints[:1]:
                found_intents.append(intents[i])
                mapping.append({"field": field, "supplied": supplied, "read_as": "intent", "value": intents[i]})
            for m in meds:
                found_media.append(m)
                mapping.append({"field": field, "supplied": supplied, "read_as": "medium", "value": m,
                                "binds_rule_pack": False})
            continue
        unmatched.append(supplied)
    if explicit_medium:
        mapping.append({"field": "medium", "supplied": explicit_medium, "read_as": "medium",
                        "value": explicit_medium, "binds_rule_pack": False})
    distinct = list(dict.fromkeys(found_intents))
    conflict = len(distinct) > 1
    medium_out = explicit_medium or ", ".join(dict.fromkeys(found_media))
    return {
        "intent": distinct[0] if len(distinct) == 1 else "",
        "medium": medium_out,
        "mapping": mapping,
        "unmatched": "; ".join(unmatched),
        "conflict": conflict,
    }
CHAIRS = ("medical", "legal", "regulatory")
MLR_STATUSES = ("findings_only", "revise", "human_gate_required", "prep_complete")
CHAIR_DECISIONS = ("approve", "revise", "reject", "abstain")

TOOL_NAMES = (
    "mlr_intake",
    "mlr_list_rulesets",
    "mlr_get_ruleset",
    "mlr_get_packet_schema",
    "mlr_validate_packet",
    "mlr_align_claims",
    "mlr_compile_checklist",
    "mlr_handoff_verify",
    "mlr_build_prep_record",
    "my_usage",
)

COUNTED_TOOLS = frozenset(
    {
        "mlr_intake",
        "mlr_get_ruleset",
        "mlr_validate_packet",
        "mlr_align_claims",
        "mlr_compile_checklist",
        "mlr_build_prep_record",
    }
)
