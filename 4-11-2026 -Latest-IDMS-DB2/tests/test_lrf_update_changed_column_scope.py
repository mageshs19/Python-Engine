from __future__ import annotations

import re
from types import SimpleNamespace

from converter.composers.update_sql_cleanup.modify_update_rewriter import (
    ModifyUpdateRewriter,
)


def _rewriter():
    owner = SimpleNamespace(
        _logical=lambda line: (
            line[7:72].strip()
            if len(line) >= 8 and line[:6].strip().isdigit()
            else str(line or "").strip()
        ),
        EXEC_SQL_END_PATTERN=re.compile(r"^END-EXEC\.?$", re.IGNORECASE),
    )
    return ModifyUpdateRewriter(owner=owner, scanner=object())


def test_lrf_modify_marker_is_detected_without_program_name_hardcoding():
    rewriter = _rewriter()
    lines = [
        "UPDATE-PARAGRAPH.",
        "*DB2: Expanded LRF MODIFY CUSTOMER-LR WHERE MO-CUSTOMER -> MODIFY CUSTOMER.",
        "*DB2: Converted MODIFY for CUSTOMER.",
    ]

    assert rewriter._is_lrf_expanded_modify(lines, 2) is True


def test_lrf_update_scan_uses_full_paragraph_instead_of_last_20_lines():
    rewriter = _rewriter()
    lines = ["UPDATE-PARAGRAPH."]
    lines.extend(f"MOVE VALUE-{index} TO CUSTOMER-FIELD-{index}." for index in range(30))
    lines.append("*DB2: Expanded LRF MODIFY CUSTOMER-LR WHERE MO-CUSTOMER -> MODIFY CUSTOMER.")
    lines.append("*DB2: Converted MODIFY for CUSTOMER.")
    modify_index = len(lines) - 1

    # The LRF marker activates the wider, paragraph-scoped scan.
    assert rewriter._is_lrf_expanded_modify(lines, modify_index) is True
    assert rewriter._post_select_scan_start(
        lines, modify_index, lrf_update=True
    ) == 1

    # Ordinary MODIFY retains the established conservative 20-line window.
    assert rewriter._post_select_scan_start(
        lines, modify_index, lrf_update=False
    ) == max(0, modify_index - 20)


def test_lrf_update_scan_stops_at_latest_sql_boundary_in_paragraph():
    rewriter = _rewriter()
    lines = [
        "UPDATE-PARAGRAPH.",
        "MOVE OLD-VALUE TO CUSTOMER-NAME.",
        "EXEC SQL",
        "SELECT CUSTOMER_NAME",
        "END-EXEC",
        "MOVE NEW-VALUE TO CUSTOMER-NAME.",
        "*DB2: Expanded LRF MODIFY CUSTOMER-LR WHERE MO-CUSTOMER -> MODIFY CUSTOMER.",
        "*DB2: Converted MODIFY for CUSTOMER.",
    ]

    assert rewriter._post_select_scan_start(
        lines, len(lines) - 1, lrf_update=True
    ) == 5


def test_lrf_provenance_detection_supports_fixed_format_comment_indicators():
    rewriter = _rewriter()
    lines = [
        "000100 UPDATE-PARAGRAPH.                                            00010000",
        "000110*DB2: Expanded LRF MODIFY CUSTOMER-LR WHERE MO-CUSTOMER ->     00011000",
        "000120*MODIFY CUSTOMER.                                              00012000",
        "000130*DB2: Converted MODIFY for CUSTOMER.                           00013000",
    ]

    assert rewriter._is_lrf_expanded_modify(lines, 3) is True
