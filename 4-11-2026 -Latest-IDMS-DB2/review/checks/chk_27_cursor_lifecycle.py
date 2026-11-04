"""CHK-27 Cursor lifecycle - DECLARE, OPEN, FETCH, CLOSE, termination."""

from __future__ import annotations

import re

from review.engine import cursors, sql_blocks as sql
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std


class CursorLifecycleCheck(Check):
    CHECK_ID = "CHK-27"
    TITLE = "Cursor lifecycle validation"
    SEVERITY = CRITICAL
    APPLIES_TO = BOTH
    ORDER = 270

    def relevant(self, ctx, view) -> bool:
        return bool(cursors.declare_blocks(view))

    def not_relevant_reason(self) -> str:
        return "No cursor DECLARE blocks found."

    def review(self, ctx, view, record):
        declares = cursors.declare_blocks(view)
        declared = cursors.declared_cursors(view)
        opens = cursors.open_statements(view)
        closes = cursors.close_statements(view)
        fetches = sql.fetch_statements(view)

        # ---- 01 DECLARE - SELECT and FROM PRESENT ---------
        bad_declares = [
            d for d in declares 
            if not all(d.has(c) for c in ["SELECT", "FROM"])
        ]
        record.expect_none(
            "01", "Every cursor DECLARE has SELECT and FROM clauses",
            bad_declares,
        )

        # ---- 02 OPEN - Statement exists for each cursor ----
        open_names = {cursors.cursor_name(o) for o in opens}
        missing_opens = [d for d in declared if d not in open_names]
        record.expect_none(
            "02", "Every declared cursor has OPEN statement",
            missing_opens,
        )

        # ---- 03 FETCH - INTO clause with host variables ---
        bad_fetches = [f for f in fetches if not f.has("INTO")]
        record.expect_none(
            "03", "Every FETCH statement has INTO clause",
            bad_fetches,
        )

        # ---- 04 CLOSE - Statement exists for each open ----
        close_names = {cursors.cursor_name(c) for c in closes}
        missing_closes = [o for o in open_names if o not in close_names]
        record.expect_none(
            "04", "Every opened cursor has CLOSE statement",
            missing_closes,
        )

        # ---- 05 FETCH EOC and real SQL-error distinction -------------
        # A pass-all here used to mark every program green without examining
        # FETCH. SQLCODE +100 is the normal EOC result; WHEN OTHER must still
        # route genuine errors through the established SQLERROR path.
        missing_fetch_branches = []
        missing_error_branches = []
        missing_locations = []
        for para in cursors.cursor_paragraphs(view):
            body = "\n".join(cursors.paragraph_body(view, para)).upper()
            has_location = bool(re.search(
                rf"\bMOVE\s+['\"]?{para.number}['\"]?\s+TO\s+{re.escape(std.SQL_LOCATION_FIELD)}\b",
                body,
            ))
            if not has_location:
                missing_locations.append(para.name)
            if para.operation == "FETCH":
                if not re.search(r"\bWHEN\s+(?:\+?100|SQLCODE\s*=\s*\+?100)\b", body):
                    missing_fetch_branches.append(para.name)
            if not re.search(r"\bWHEN\s+OTHER\b", body) or not re.search(
                r"\b(?:PERFORM|GO\s+TO)\s+SQLERROR\b|\bSQLERROR\b",
                body,
            ):
                missing_error_branches.append(para.name)
        record.expect_all(
            "05", "FETCH handles SQLCODE +100 as EOC, not as a general SQL error",
            missing_fetch_branches,
        )
        record.expect_all(
            "06", "OPEN/FETCH/CLOSE route genuine SQL errors through SQLERROR",
            missing_error_branches,
        )
        record.expect_all(
            "07", f"Each cursor operation sets {std.SQL_LOCATION_FIELD} before SQL",
            missing_locations,
        )
