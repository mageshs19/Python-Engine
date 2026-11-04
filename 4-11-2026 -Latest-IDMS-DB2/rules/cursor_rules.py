"""
Cursor generation rules.

This file contains cursor authority rules and paragraph numbering rules.

Rules belong in rules/, not patterns/.

No regex patterns should be defined here.
No parser, service, transformer, or generator logic should be placed here.
"""

CURSOR_AUTHORITY_RULES = [
    "Cursor names are derived from Sheet Mapping DB2 record/table names.",
    "Cursor names are not derived from IDMS set names.",
    "Generated cursor OPEN, FETCH, and CLOSE paragraphs are placed near the end.",
    "SQL-ERROR paragraph is required when cursor code performs SQL error handling.",
]

# COBOL team convention: one 1000-number block per cursor.
# Cursor 1: OPEN/FETCH/CLOSE = 2100/2200/2300
# Cursor 2: OPEN/FETCH/CLOSE = 3100/3200/3300
# Cursor 3: OPEN/FETCH/CLOSE = 4100/4200/4300
# Cursor order comes from discovered cursor specs, never a program allowlist.
CURSOR_PARAGRAPH_BASE = 2100
CURSOR_PARAGRAPH_ORDER_STRIDE = 1000
CURSOR_OPERATION_OFFSETS = {
    "open": 0,
    "fetch": 100,
    "close": 200,
}


def cursor_paragraph_number(
    cursor_order: int,
    operation: str,
) -> int:
    """Return the stable four-digit paragraph number for a cursor operation.

    Cursor order is discovered from the generated cursor plan, not a
    program-specific lookup table. Examples: cursor 1 -> 2100/2200/2300;
    cursor 2 -> 3100/3200/3300; cursor 3 -> 4100/4200/4300.
    """
    try:
        order = int(cursor_order)
    except (TypeError, ValueError) as error:
        raise ValueError(f"Invalid cursor order: {cursor_order}") from error
    if order < 1:
        raise ValueError(f"Unsupported cursor order: {cursor_order}")

    operation_key = str(operation or "").strip().lower()
    if operation_key not in CURSOR_OPERATION_OFFSETS:
        raise ValueError(f"Unsupported cursor operation: {operation}")

    return (
        CURSOR_PARAGRAPH_BASE
        + ((order - 1) * CURSOR_PARAGRAPH_ORDER_STRIDE)
        + CURSOR_OPERATION_OFFSETS[operation_key]
    )
