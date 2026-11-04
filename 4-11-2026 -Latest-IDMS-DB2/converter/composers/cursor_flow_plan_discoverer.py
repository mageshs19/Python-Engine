"""
Cursor flow plan discoverer.

Scans generated COBOL lines and correlates each cursor OPEN with its
matching FETCH paragraph and business processing loop, producing a list
of CursorFlowPlan objects. Discovery logic only.
"""

import re
from converter.composers.cursor_flow_line_formatter import (
    CursorFlowLineFormatter,
)
from converter.composers.cursor_flow_models import CursorFlowPlan
from patterns.cursor_flow_patterns import (
    PERFORM_BUSINESS_PATTERN,
    PERFORM_CURSOR_PATTERN,
    UNTIL_SQLCODE_100_PATTERN,
    UNTIL_CURSOR_EOC_PATTERN,
)
from rules.cursor_flow_rules import (
    LOOKAHEAD_LIMIT,
    UNTIL_LOOKAHEAD_LIMIT,
)


class CursorFlowPlanDiscoverer:
    def __init__(
        self,
        line_formatter: CursorFlowLineFormatter | None = None,
    ) -> None:
        self.line_formatter = line_formatter or CursorFlowLineFormatter()
        self.messages: list[str] = []

    def _logical(self, line: str) -> str:
        return self.line_formatter.logical(line)

    def discover(self, lines: list[str]) -> list[CursorFlowPlan]:
        self.messages = []
        plans: list[CursorFlowPlan] = []
        index = 0

        while index < len(lines):
            logical = self._logical(lines[index])
            open_match = PERFORM_CURSOR_PATTERN.match(logical)

            if not open_match:
                index += 1
                continue

            if open_match.group("operation").upper() != "OPEN":
                index += 1
                continue

            plan = self._build_plan(
                lines=lines,
                open_index=index,
                open_match=open_match,
            )

            if plan is None:
                index += 1
                continue

            plans.append(plan)
            # Do not skip to the end of this cursor's loop: another OPEN may
            # occur in a branch or in a nested/dependent path inside the span.
            # Each candidate is independently considered, then overlap is
            # rejected below rather than silently hiding the later cursor.
            index += 1

        # A line may belong to only one automatic rewrite. Overlapping plans
        # indicate nesting/shared business flow; leave those flows unchanged.
        accepted: list[CursorFlowPlan] = []
        claimed: set[int] = set()
        for plan in plans:
            span = set(range(plan.open_index, plan.until_index + 1))
            if claimed.intersection(span):
                self.messages.append(
                    f"Cursor flow for {plan.cursor_name} overlaps another cursor flow; "
                    "automatic rewrite withheld for ambiguous/nested control flow."
                )
                continue
            accepted.append(plan)
            claimed.update(span)
        return accepted

    def _build_plan(
        self,
        lines: list[str],
        open_index: int,
        open_match,
    ) -> CursorFlowPlan | None:
        cursor_name = open_match.group("cursor").upper()
        open_number = int(open_match.group("number"))
        fetch_call = self._find_cursor_call(
            lines, open_index + 1, cursor_name, "FETCH",
        )
        if fetch_call is None:
            self.messages.append(
                f"Cursor flow for {cursor_name}: no unambiguous FETCH call after OPEN; "
                "left unchanged."
            )
            return None
        fetch_index, fetch_number = fetch_call

        business_info = self._find_business_loop_after_fetch(
            lines=lines,
            start_index=fetch_index + 1,
        )
        if business_info is None:
            self.messages.append(
                f"Cursor flow for {cursor_name}: no provable simple business loop after FETCH; "
                "left unchanged."
            )
            return None

        business_index, until_index, business_paragraph = business_info
        close_call = self._find_cursor_call(
            lines, until_index + 1, cursor_name, "CLOSE",
        )
        if close_call is None:
            self.messages.append(
                f"Cursor flow for {cursor_name}: no CLOSE call after the loop; "
                "left unchanged."
            )
            return None
        close_index, close_number = close_call

        # Refuse transformations across control-flow boundaries or another
        # cursor's operation: a simple sequential template is not enough to
        # prove a conditional, nested, or interleaved cursor relationship.
        for pos in range(open_index + 1, close_index):
            logical = self._logical(lines[pos]).upper()
            if re.search(r"\b(IF|ELSE|EVALUATE|WHEN|GO\s+TO|GOTO|END-IF|END-EVALUATE)\b", logical):
                self.messages.append(
                    f"Cursor flow for {cursor_name}: branch/control transfer near line {pos + 1}; "
                    "automatic rewrite withheld for review."
                )
                return None
            other = PERFORM_CURSOR_PATTERN.match(logical)
            if other and other.group("cursor").upper() != cursor_name:
                self.messages.append(
                    f"Cursor flow for {cursor_name}: interleaved operation for "
                    f"{other.group('cursor').upper()} near line {pos + 1}; "
                    "automatic rewrite withheld for review."
                )
                return None

        return CursorFlowPlan(
            cursor_name=cursor_name,
            open_number=open_number,
            fetch_number=fetch_number,
            close_number=close_number,
            open_paragraph=f"{open_number}-OPEN-{cursor_name}",
            fetch_paragraph=f"{fetch_number}-FETCH-{cursor_name}",
            close_paragraph=f"{close_number}-CLOSE-{cursor_name}",
            eoc_condition=f"{cursor_name}-EOC",
            business_paragraph=business_paragraph,
            open_index=open_index,
            fetch_index=fetch_index,
            business_index=business_index,
            until_index=until_index,
            close_index=close_index,
        )

    def _find_cursor_call(
        self,
        lines: list[str],
        start_index: int,
        cursor_name: str,
        operation: str,
    ) -> tuple[int, int] | None:
        """Find the first matching operation call and use its actual number.

        No paragraph number arithmetic is used to infer cursor relationships.
        A candidate must be an explicit PERFORM of the requested cursor action.
        """
        end_index = min(len(lines), start_index + LOOKAHEAD_LIMIT)
        found: list[tuple[int, int]] = []
        for index in range(start_index, end_index):
            match = PERFORM_CURSOR_PATTERN.match(self._logical(lines[index]))
            if not match:
                continue
            if match.group("operation").upper() == operation.upper() and match.group("cursor").upper() == cursor_name.upper():
                found.append((index, int(match.group("number"))))
                break
            if match.group("cursor").upper() != cursor_name.upper() and match.group("operation").upper() in {"OPEN", "CLOSE"}:
                # A different cursor's lifecycle boundary makes a global
                # lookahead unsafe; the caller may be nested/interleaved.
                self.messages.append(
                    f"Cursor flow for {cursor_name}: interleaved operation for "
                    f"{match.group('cursor').upper()} near line {index + 1}; "
                    "automatic rewrite withheld for review."
                )
                return None
        return found[0] if found else None

    def _find_fetch_after_open(
        self,
        lines: list[str],
        start_index: int,
        cursor_name: str,
        fetch_number: int,
    ) -> int:
        end_index = min(len(lines), start_index + LOOKAHEAD_LIMIT)

        for index in range(start_index, end_index):
            logical = self._logical(lines[index])
            match = PERFORM_CURSOR_PATTERN.match(logical)

            if not match:
                continue
            if match.group("operation").upper() != "FETCH":
                continue
            if match.group("cursor").upper() != cursor_name:
                continue
            if int(match.group("number")) != fetch_number:
                continue

            return index

        return -1

    def _find_business_loop_after_fetch(
        self,
        lines: list[str],
        start_index: int,
    ) -> tuple[int, int, str] | None:
        end_index = min(len(lines), start_index + LOOKAHEAD_LIMIT)

        for index in range(start_index, end_index):
            logical = self._logical(lines[index])

            if not logical:
                continue
            if logical.startswith("*") or logical.startswith("/"):
                continue
            if PERFORM_CURSOR_PATTERN.match(logical):
                continue

            business_match = PERFORM_BUSINESS_PATTERN.match(logical)
            if not business_match:
                continue

            business_paragraph = business_match.group("paragraph").upper()
            until_index = self._find_until_sqlcode_100(
                lines=lines,
                start_index=index + 1,
            )
            if until_index < 0:
                continue

            return index, until_index, business_paragraph

        return None

    def _find_until_sqlcode_100(
        self,
        lines: list[str],
        start_index: int,
    ) -> int:
        end_index = min(len(lines), start_index + UNTIL_LOOKAHEAD_LIMIT)

        for index in range(start_index, end_index):
            logical = self._logical(lines[index])
            if (
                UNTIL_SQLCODE_100_PATTERN.match(logical)
                or UNTIL_CURSOR_EOC_PATTERN.match(logical)
            ):
                return index

        return -1
