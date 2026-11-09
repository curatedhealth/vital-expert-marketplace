#!/usr/bin/env python3
"""Structural channel-intent gate (offline). Never approves. Never invents facts."""

from __future__ import annotations

import argparse
import json
import sys

import re

# Field-based, whole-word logic (TEH-RDY-018). Free text never sets the channel or the
# reactive posture; it can only *add* promotional signals that force a human gate.
# TEH-RDY-057: "channel" here is the communication intent (the rule-pack catalogue key). A delivery
# medium (email, print, digital display, congress, social ...) is recorded in `medium` and never
# classifies, never counts as an unrecognized channel, and never binds a rule pack. The split and
# the intent-word mapping come from contract.split_channel so every tool reads words the same way.
try:
    from contract import split_channel
except ImportError:  # pragma: no cover - monorepo import path
    from mlr_review.contract import split_channel  # type: ignore

_REACTIVE = {"reactive", "unsolicited"}
_PROACTIVE = {"proactive", "push", "solicited"}
_NEGATORS = {"no", "not", "non", "without", "never", "none", "lacks", "lacking", "absent"}

# Whole-word / whole-phrase promotional markers in the body.
PROMO_SIGNALS = (
    "prescribe",
    "buy",
    "order now",
    "superior",
    "best in class",
    "only therapy",
    "branded",
    "important safety information",
    "isi",
    "brief summary",
)
SCIEX_OK = ("unsolicited", "reactive", "response to enquiry", "scientific exchange")  # kept for importers; not used to set posture

# TEH-RDY-061: whole-word / whole-phrase medical-information (MI letter) markers in the body. Used only to
# detect a piece that mixes promotional and medical-information content (more than one channel/intent
# reading -> human gate) and, when no intent was declared, to give a provisional content-based reading
# (TEH-RDY-062). They never set the declared channel or the posture. A product's "medical information"
# contact line is deliberately not a marker (promotional pieces routinely carry one).
MI_SIGNALS = (
    "mi letter",
    "medical information letter",
    "medical information response",
    "standard response letter",
    "response to enquiry",
    "response to your enquiry",
    "response to your inquiry",
    "in response to your request",
    "in response to your question",
    "unsolicited request",
)

# TEH-RDY-062: who will use / present the piece (e.g. reps vs MSLs). Not an intent and never classifies;
# when the person says it is not decided, it is a pending item and the answer asks for it.
_USERS_UNKNOWN = {"unknown", "undecided", "not decided", "not yet decided", "tbd", "tbc", "open", "?",
                  "not known", "unclear", "either", "both"}

# TEH-RDY-064: non-promotional (disease awareness / corporate) content markers. Like MI_SIGNALS they never
# set the declared channel; they only allow a provisional reading when no intent was declared.
NON_PROMO_SIGNALS = ("disease awareness", "unbranded", "non branded", "non promotional",
                     "corporate communication", "corporate information", "corporate")


def _plain_hits(text: str, phrases: tuple[str, ...]) -> list[str]:
    """Whole-word phrase matches without the negation window (non-promotional markers are themselves
    often written with 'non' / 'no', e.g. 'non-branded disease awareness')."""
    toks = _tokens(text)
    return [p for p in phrases
            if any(toks[i : i + len(_tokens(p))] == _tokens(p) for i in range(len(toks) - len(_tokens(p)) + 1))]
NON_PROMO_LABEL = "provisional: non-promotional (disease awareness / corporate)"
# Intent words read from the person's description (whole-word, negation-aware). Signals only.
_DESC_READINGS = (
    ("promo", ("promotional", "promo", "advert", "advertisement", "leave behind", "sales aid", "detail aid",
               "branded")),
    ("med_info", ("med info", "medical information", "mi letter", "mi response", "response letter",
                  "standard response")),
    ("scientific_exchange", ("scientific exchange",)),
)

_DECISION_WORDS = {
    "treat_as_promo": "treat as promotional",
    "treat_as_scientific_exchange": "treat as scientific exchange",
    "treat_as_med_info": "treat as medical information",
}
_PENDING_WORDS = {
    "channel": "the intent (promotional, scientific exchange or medical information)",
    "proactive_or_reactive": "proactive or reactive (unsolicited request)",
    "offlabel_or_unlicensed": "whether off-label or unlicensed content is present",
    "users": "who will use it",
    "unrecognised_channel_or_intent": "the intent (the value supplied was not recognized)",
}
_QUESTIONS = {
    "channel": "Which intent applies: promotional, scientific exchange or medical information?",
    "proactive_or_reactive": "Is the piece sent proactively, or in reply to a documented unsolicited request?",
    "offlabel_or_unlicensed": "Does it contain off-label or unlicensed content?",
    "users": "Who will use or present it (for example sales reps or MSLs)?",
    "unrecognised_channel_or_intent": "Which intent applies: promotional, scientific exchange or medical information?",
}


def _norm(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _phrase_hits(text: str, phrases: tuple[str, ...]) -> list[str]:
    """Whole-word phrase matches that are not directly negated (e.g. 'non-branded', 'no ISI')."""
    toks = _tokens(text)
    hits: list[str] = []
    for phrase in phrases:
        ptoks = _tokens(phrase)
        n = len(ptoks)
        for i in range(len(toks) - n + 1):
            if toks[i : i + n] == ptoks:
                prev = toks[max(0, i - 2) : i]
                if any(t in _NEGATORS for t in prev):
                    continue
                hits.append(phrase)
                break
    return hits


def _quotes(text: str, phrases: list[str]) -> list[str]:
    """Verbatim sentences from the supplied text that carry each phrase (for quoting conflicting elements)."""
    sentences = [s.strip() for s in re.split(r"(?<=[.!?;])\s+|\n+", text) if s.strip()]
    out: list[str] = []
    for phrase in phrases:
        ptoks = _tokens(phrase)
        for sent in sentences:
            stoks = _tokens(sent)
            if any(stoks[i : i + len(ptoks)] == ptoks for i in range(len(stoks) - len(ptoks) + 1)):
                q = sent if len(sent) <= 200 else sent[:197] + "..."
                if q not in out:
                    out.append(q)
                break
    return out


def _users_unknown(value: object) -> bool | None:
    """True when the person said who will use the piece is not decided; None when not supplied."""
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        vals = [_norm(v) for v in value if _norm(v)]
        if not vals:
            return True
        return len(vals) > 1 or vals[0] in _USERS_UNKNOWN
    v = _norm(value)
    if not v or v in _USERS_UNKNOWN:
        return True
    toks = set(_tokens(v))
    if toks & {"unknown", "undecided", "tbd", "tbc", "unclear"} or "not decided" in v or " or " in f" {v} ":
        return True
    return False


def _truthy(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    v = _norm(value)
    if v in {"yes", "true", "y", "1"}:
        return True
    if v in {"no", "false", "n", "0"}:
        return False
    return None


def gate(args: dict) -> dict:
    proactive = _norm(args.get("proactive_or_reactive"))
    offlabel = _truthy(args.get("offlabel_or_unlicensed"))
    request_documented = _truthy(args.get("unsolicited_request_documented"))
    body = str(args.get("body") or "")
    # Optional derived fields (TEH-RDY-040): set by the skill only from person-supplied evidence
    # (for example the pasted text names no product -> branded "no"). Never guessed.
    branded = _truthy(args.get("branded"))
    claims_present = _truthy(args.get("product_claims_present"))
    # TEH-RDY-061: a person-stated mix (from the person's description, no text supplied). The skill passes
    # `mixed_content: true` and the conflicting elements quoted from the description in `mixed_elements`.
    mixed_described = _truthy(args.get("mixed_content")) is True
    raw_elements = args.get("mixed_elements") or []
    if isinstance(raw_elements, str):
        raw_elements = [raw_elements]
    mixed_elements = [str(e).strip() for e in raw_elements if str(e).strip()]
    # TEH-RDY-064: the person's own words for what the piece is ("a med-info letter", "unbranded disease
    # awareness slides"). A signal for a provisional reading only -- never the declared intent.
    described_as = str(args.get("described_as") or "")
    users_raw = args.get("users", args.get("intended_users"))
    users_unknown = _users_unknown(users_raw)
    gaps: list[str] = []
    rationale: list[str] = []

    # Channel (intent) comes from the declared channel / intent fields, split from any medium
    # (TEH-RDY-057). Free-text intent counts only when it reads as an intent word, never by substring.
    split = split_channel(args.get("channel"), args.get("intent"), args.get("medium"))
    channel = split["intent"] if split["intent"] in {"promo", "scientific_exchange", "med_info"} else ""
    unmatched = split["unmatched"] or (split["intent"] if split["intent"] and not channel else "")
    # Judgment flags (TEH-RDY-058): only a genuine call on supplied facts gates; missing inputs never do.
    judgment = False
    if not channel:
        gaps.append("channel")
    if proactive in _REACTIVE:
        posture = "reactive"
    elif proactive in _PROACTIVE:
        posture = "proactive"
    else:
        posture = ""
        gaps.append("proactive_or_reactive")
    if posture == "reactive" and request_documented is False:
        rationale.append("Reactive posture declared but no documented unsolicited request; treated as not established.")
        posture = ""
        judgment = True  # supplied facts conflict: a human must settle the posture

    promo_hits = _phrase_hits(body, PROMO_SIGNALS)
    mi_hits = _phrase_hits(body, MI_SIGNALS)
    promo_content = bool(promo_hits) or branded is True or claims_present is True
    if users_unknown:
        gaps.append("users")
    desc_readings = [r for r, phrases in _DESC_READINGS if described_as and _phrase_hits(described_as, phrases)]
    desc_non_promo = _plain_hits(described_as, NON_PROMO_SIGNALS) if described_as else []
    desc_conflict = len(desc_readings) > 1 or ("promo" in desc_readings and bool(desc_non_promo))
    desc_intent = desc_readings[0] if len(desc_readings) == 1 else ""
    body_non_promo = _plain_hits(body, NON_PROMO_SIGNALS)
    non_promo_reading = None

    decision = "human_gate_required"
    if channel == "promo":
        if posture == "reactive":
            rationale.append(
                "channel_content_mismatch: unsolicited / reactive request answered with promotional material; human gate."
            )
            judgment = True
        else:
            decision = "treat_as_promo"
            rationale.append("Declared promotional channel.")
    elif channel in {"scientific_exchange", "med_info"}:
        if offlabel is True and posture == "proactive":
            rationale.append(
                "Proactive off-label / unlicensed content often fails scientific-exchange tests; human gate."
            )
            judgment = True
        elif posture == "reactive":
            decision = "treat_as_med_info" if channel == "med_info" else "treat_as_scientific_exchange"
            rationale.append("Reactive / unsolicited posture declared in the posture field; still not approval.")
        elif posture == "proactive":
            rationale.append("Scientific exchange / med_info declared with a proactive posture; human gate.")
            judgment = True
        else:
            rationale.append("Scientific exchange / med_info without a declared reactive posture.")
    else:
        if unmatched or split["conflict"]:
            # A value that is neither an intent nor a known medium (or two conflicting intents) is an
            # unmatched input -- reported, never mapped. A medium alone is NOT unrecognized (TEH-RDY-057).
            gaps.append("unrecognised_channel_or_intent")
        elif posture == "reactive" and request_documented is True and branded is False \
                and claims_present is not True and offlabel is not True:
            # TEH-RDY-040: no declared channel, but the gate fields derived from supplied evidence
            # allow a classification. It stays provisional: the channel is still for a human to declare.
            decision = "treat_as_med_info"
            rationale.append(
                "Derived from supplied fields: reactive posture with a documented unsolicited request, "
                "non-branded, no product claims -> not promotional; medical information response "
                "(scientific exchange also plausible). Provisional until a human declares the channel."
            )
            if offlabel is None:
                gaps.append("offlabel_or_unlicensed")
        elif posture == "proactive" and (branded is True or claims_present is True) and offlabel is not True:
            decision = "treat_as_promo"
            rationale.append(
                "Derived from supplied fields: proactive posture with branding or product claims -> "
                "promotional rules apply. Provisional until a human declares the channel."
            )
        # TEH-RDY-062: no declared intent, but the supplied content carries a reading -> a provisional
        # content-based decision (findings_only), never "not classified". Content with no signal for any
        # reading stays a missing input (rule 4). Conflicting supplied facts stay a judgment call.
        elif promo_content and posture == "reactive":
            rationale.append(
                "channel_content_mismatch: reactive / unsolicited posture with promotional content "
                "(branding, product claims or promotional markers); human gate."
            )
            judgment = True
        elif promo_content and offlabel is True:
            rationale.append(
                "Promotional content with off-label or unlicensed content and no declared intent; human gate."
            )
            judgment = True
        elif promo_content:
            decision = "treat_as_promo"
            rationale.append(
                "Provisional, from the supplied content: branding, product claims or promotional markers -> "
                "promotional rules apply until a human declares the intent."
            )
        elif mi_hits and posture == "proactive":
            rationale.append(
                "Medical-information letter content with a proactive posture; human gate."
            )
            judgment = True
        elif mi_hits and offlabel is not True:
            decision = "treat_as_med_info"
            rationale.append(
                "Provisional, from the supplied content: medical-information letter markers ("
                + ", ".join(mi_hits) + ") and no promotional markers -> medical information response "
                "until a human declares the intent and confirms the request record."
            )
        # TEH-RDY-064: the person's description names what the piece is -> a provisional reading from it.
        elif desc_conflict:
            mixed_described = True
            if not mixed_elements:
                mixed_elements = [described_as.strip()]
        elif desc_intent == "promo" and posture == "reactive":
            rationale.append("channel_content_mismatch: described as promotional with a reactive posture; human gate.")
            judgment = True
        elif desc_intent in {"med_info", "scientific_exchange"} and posture == "proactive":
            rationale.append(f"Described as {desc_intent} with a proactive posture; human gate.")
            judgment = True
        elif desc_intent in {"promo", "med_info", "scientific_exchange"} and offlabel is not True:
            decision = {"promo": "treat_as_promo", "med_info": "treat_as_med_info",
                        "scientific_exchange": "treat_as_scientific_exchange"}[desc_intent]
            rationale.append(
                f"Provisional, from the person's description ({described_as.strip()!r}): read as {desc_intent} "
                "until a human declares the intent."
            )
        elif (desc_non_promo or body_non_promo or (branded is False and claims_present is False)) \
                and offlabel is not True:
            non_promo_reading = (
                "person's description" if desc_non_promo else
                ("supplied content" if body_non_promo else "supplied fields: unbranded, no product claims")
            )
            rationale.append(
                f"Provisional, from the {non_promo_reading}: non-promotional (disease awareness / corporate) "
                "until a human declares the intent; no rule pack binds on a provisional reading."
            )

    if promo_hits and decision != "treat_as_promo":
        rationale.append(
            "channel_content_mismatch: promotional markers in body (" + ", ".join(promo_hits) + ") — reconsider channel."
        )
        decision = "human_gate_required"
        judgment = True

    # TEH-RDY-061: a piece that mixes promotional and medical-information content supports more than one
    # channel/intent reading -> human gate (map rule 2, row (e)), whatever intent was declared. The
    # conflicting elements are quoted from the supplied text, or from the person's description.
    mixed = None
    if promo_hits and mi_hits:
        mixed = {
            "source": "supplied_text",
            "promotional": _quotes(body, promo_hits),
            "medical_information": _quotes(body, mi_hits),
        }
    elif mixed_described:
        mixed = {"source": "person_description", "elements": mixed_elements}
    if mixed is not None:
        if mixed["source"] == "supplied_text":
            detail = ("promotional: " + " | ".join(f'"{q}"' for q in mixed["promotional"])
                      + "; medical information: " + " | ".join(f'"{q}"' for q in mixed["medical_information"]))
        else:
            detail = ("person's description: " + " | ".join(f'"{q}"' for q in mixed_elements)
                      if mixed_elements else "person's description (quote the conflicting elements)")
        rationale.append(
            "mixed_content: promotional and medical-information content in one piece — supports more than "
            "one channel/intent reading; a human decides (" + detail + ")."
        )
        decision = "human_gate_required"
        judgment = True

    # TEH-RDY-058: the gate's status follows the shared finding-status map (tool status is an input).
    # A judgment call on supplied facts -> human_gate_required. A decision held only because inputs
    # are missing -> findings_only with the questions; a treat_as_* decision -> findings_only
    # (provisional while gaps remain). Precedence rule 1 (approval / bypass requests) is applied by
    # the skill on top -- the tool never sees the person's request.
    if judgment:
        status, basis = "human_gate_required", "judgment"
        non_promo_reading = None
    elif non_promo_reading:
        status, basis = "findings_only", "provisional"
    elif decision.startswith("treat_as_"):
        status, basis = "findings_only", ("provisional" if gaps else "final")
    else:
        status, basis = "findings_only", "missing_inputs"
    pending = [g for g in gaps]
    provisional_label = None
    if decision.startswith("treat_as_") and not judgment and gaps:
        provisional_label = (
            f"provisional: {_DECISION_WORDS[decision]} — pending: "
            + "; ".join(_PENDING_WORDS.get(g, g) for g in gaps)
        )
    if non_promo_reading:
        provisional_label = NON_PROMO_LABEL + " — pending: " + "; ".join(_PENDING_WORDS.get(g, g) for g in gaps)
    # TEH-RDY-064: the provisional reading, whatever its kind (a treat_as_* decision with open items, or a
    # non-promotional reading that has no decision value of its own). None when no reading is provisional.
    provisional_reading = provisional_label
    if split["medium"]:
        rationale.append(
            f"Medium recorded: {split['medium']} (delivery medium; never classifies and never binds a rule pack)."
        )
    for m in split["mapping"]:
        if m.get("read_as") == "intent" and _norm(m.get("supplied")).replace("-", "_") != m.get("value"):
            rationale.append(f"Intent word {m['supplied']!r} read as {m['value']}.")

    return {
        "tool": "channel_intent_gate",
        "ok": not gaps,
        "decision": decision,
        "rationale": rationale,
        "gaps": gaps,
        "status": status,
        "status_basis": basis,
        "pending": pending,
        "medium": split["medium"] or None,
        "channel_mapping": split["mapping"],
        "provisional_label": provisional_label,
        "provisional_reading": provisional_reading,
        "questions": [_QUESTIONS[g] for g in gaps if g in _QUESTIONS],
        "users": (None if users_raw is None else ("unknown" if users_unknown else users_raw)),
        "mixed_content": mixed,
        "mode": "READY-local",
        "tool_checked": False,
        "metered": False,
        "note": "Structural gate only. Humans still classify and approve nothing here.",
        "liability_line": (
            "This prepares material for human MLR review. "
            "It is not medical, legal, or regulatory approval."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--args-json", default="-")
    p.add_argument("--file")
    ns = p.parse_args()
    raw = open(ns.file, encoding="utf-8").read() if ns.file else (sys.stdin.read() if ns.args_json == "-" else ns.args_json)
    args = json.loads(raw or "{}")
    out = gate(args if isinstance(args, dict) else {})
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
