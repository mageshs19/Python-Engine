"""Access-pattern-aware DB2 SQL result and error policy.

This module is deliberately independent of COBOL rendering.  The analyzer and
validators use it to distinguish cursor FETCH end-of-cursor from singleton
not-found and from unexpected SQL failures.  LR OBTAIN FIRST/NEXT are retained
as source semantics until the LR mapper proves a concrete DB2 access pattern.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re


class AccessPattern(str, Enum):
    CURSOR_OPEN = "cursor_open"
    CURSOR_FETCH = "cursor_fetch"
    CURSOR_CLOSE = "cursor_close"
    SINGLETON_SELECT = "singleton_select"
    LR_OBTAIN_FIRST = "lr_obtain_first"
    LR_OBTAIN_NEXT = "lr_obtain_next"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class AccessErrorPolicy:
    pattern: AccessPattern
    sqlcode_zero: str
    sqlcode_100: str
    unexpected_sqlcode: str = "route_to_shared_sqlerror"


POLICIES: dict[AccessPattern, AccessErrorPolicy] = {
    AccessPattern.CURSOR_OPEN: AccessErrorPolicy(AccessPattern.CURSOR_OPEN, "opened", "unexpected_result"),
    AccessPattern.CURSOR_FETCH: AccessErrorPolicy(AccessPattern.CURSOR_FETCH, "row_available", "set_this_cursor_eoc_only"),
    AccessPattern.CURSOR_CLOSE: AccessErrorPolicy(AccessPattern.CURSOR_CLOSE, "closed", "unexpected_result"),
    AccessPattern.SINGLETON_SELECT: AccessErrorPolicy(AccessPattern.SINGLETON_SELECT, "row_available", "apply_original_not_found_behavior"),
    AccessPattern.LR_OBTAIN_FIRST: AccessErrorPolicy(AccessPattern.LR_OBTAIN_FIRST, "first_record_available", "apply_original_lr_not_found_or_end_of_set_status"),
    AccessPattern.LR_OBTAIN_NEXT: AccessErrorPolicy(AccessPattern.LR_OBTAIN_NEXT, "next_record_available", "apply_original_lr_end_of_set_status"),
    AccessPattern.UNKNOWN: AccessErrorPolicy(AccessPattern.UNKNOWN, "preserve_existing_behavior", "do_not_infer", "human_review_required"),
}


def classify_access(*, sql: str = "", source_statement: str = "", cursor_operation: str = "") -> AccessPattern:
    """Classify one access using explicit operation metadata first, then text.

    `source_statement` is used for LR semantics before SQL conversion.  A
    singleton SELECT is recognized only when SELECT has an INTO host list;
    cursor declaration SELECTs are not misclassified as singleton access.
    """
    operation = (cursor_operation or "").strip().lower()
    if operation in {"open", "fetch", "close"}:
        return {"open": AccessPattern.CURSOR_OPEN, "fetch": AccessPattern.CURSOR_FETCH, "close": AccessPattern.CURSOR_CLOSE}[operation]

    source = _mask_literals(source_statement).upper()
    if re.search(r"\bOBTAIN\s+FIRST\b", source):
        return AccessPattern.LR_OBTAIN_FIRST
    if re.search(r"\bOBTAIN\s+NEXT\b", source):
        return AccessPattern.LR_OBTAIN_NEXT

    statement = _mask_literals(sql).upper()
    if re.search(r"\bSELECT\b", statement) and re.search(r"\bINTO\b", statement) and re.search(r"\bFROM\b", statement):
        return AccessPattern.SINGLETON_SELECT
    return AccessPattern.UNKNOWN


def policy_for(pattern: AccessPattern) -> AccessErrorPolicy:
    return POLICIES.get(pattern, POLICIES[AccessPattern.UNKNOWN])


def _mask_literals(text: str) -> str:
    """Mask SQL/COBOL literals so keywords inside strings do not classify code."""
    chars = list(str(text or ""))
    quote: str | None = None
    i = 0
    while i < len(chars):
        ch = chars[i]
        if quote:
            chars[i] = " "
            if ch == quote:
                if i + 1 < len(chars) and chars[i + 1] == quote:
                    chars[i + 1] = " "
                    i += 2
                    continue
                quote = None
        elif ch in ("'", '"'):
            quote = ch
            chars[i] = " "
        i += 1
    return "".join(chars)


__all__ = ["AccessPattern", "AccessErrorPolicy", "classify_access", "policy_for", "POLICIES"]
