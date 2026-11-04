"""Apply validated LRF key bindings and status ownership to generated COBOL.

Runs after DB2 infrastructure generation and before final line layout, so the
cursor's DCLGEN group is initialized before parent key values are copied.
"""
from __future__ import annotations

import re

from converter.generators.initialization.line_geometry import LineGeometry
from rules.lrf_conversion_rules import LRF_PARENT_NOT_FOUND_TOKEN


class LrfKeyBindingComposer:
    def __init__(self) -> None:
        self.geometry = LineGeometry()
        self.messages: list[str] = []

    def compose(self, text: str, child_moves_by_group: dict[str, list[str]] | None = None) -> str:
        self.messages = []
        lines = self.geometry.split(text)
        moves = {
            str(group or "").strip().upper(): list(statements or [])
            for group, statements in (child_moves_by_group or {}).items()
            if str(group or "").strip() and statements
        }
        output: list[str] = []
        skipped_parent_status = 0
        inserted_groups: set[str] = set()
        cursor_after_close = ""

        index = 0
        while index < len(lines):
            line = lines[index]
            body = self.geometry.body(line)
            upper = body.upper().strip()

            # Parent SELECT handles the parent not-found result at the point
            # it executes. Remove the original source IF block, which would
            # otherwise test the child's later SQLCODE/FETCH result.
            if re.search(rf"\bIF\s+{re.escape(LRF_PARENT_NOT_FOUND_TOKEN)}\b", upper):
                depth = 1
                index += 1
                while index < len(lines) and depth:
                    nested = self.geometry.body(lines[index]).upper().strip()
                    if re.match(r"^IF\b", nested):
                        depth += 1
                    if re.match(r"^END-IF\b", nested):
                        depth -= 1
                    index += 1
                output.append("*DB2: Parent not-found is handled by the keyed SELECT SQLCODE check.")
                skipped_parent_status += 1
                continue

            # A cursor loop must test its retained EOC flag, not SQLCODE, so
            # its termination remains correct even if another SQL statement
            # runs inside the loop body. Resolve the cursor from the FETCH in
            # this same PERFORM block; if no FETCH can be proved, leave it and
            # report the unsupported shape rather than guessing.
            if re.match(r"^PERFORM\s+UNTIL\s+SQLCODE\s*=\s*100\b", upper):
                cursor = self._fetch_cursor_before_end(lines, index)
                if cursor:
                    updated = re.sub(
                        r"SQLCODE\s*=\s*100\b",
                        f"{cursor}-EOC",
                        body,
                        count=1,
                        flags=re.I,
                    )
                    line = self._replace_body(line, updated)
                    body = updated
                    upper = updated.upper().strip()
                    self.messages.append(
                        f"LRF loop status: changed SQLCODE end-of-cursor test to {cursor}-EOC."
                    )

            # The child DCLGEN group is cleared by the initializer. Copy the
            # parent key into its FK host variables AFTER that INITIALIZE and
            # BEFORE the cursor OPEN that consumes them, when such a plan exists.
            init_match = re.match(r"^INITIALIZE\s+(DCL[A-Z0-9-]+)\b", upper)
            output.append(line)
            if init_match:
                group = init_match.group(1)
                if group in moves:
                    output.extend(moves[group])
                    inserted_groups.add(group)

            close_match = re.search(r"\bPERFORM\s+\d{3,6}-CLOSE-([A-Z0-9-]+)", upper)
            if close_match:
                cursor_after_close = close_match.group(1)
            elif cursor_after_close and re.match(r"^IF\s+SQLCODE\s*=\s*100\b", upper):
                # CLOSE overwrites SQLCODE. EOC is retained in the cursor flag.
                output[-1] = self._replace_body(
                    line, f"IF {cursor_after_close}-EOC"
                )
                cursor_after_close = ""
            elif cursor_after_close and self._is_paragraph_header(upper):
                cursor_after_close = ""

            index += 1

        missing = set(moves) - inserted_groups
        for group in sorted(missing):
            self.messages.append(
                f"LRF key propagation: no INITIALIZE {group} site was found; "
                "the child cursor key binding was not inserted."
            )
        if skipped_parent_status:
            self.messages.append(
                f"LRF status ownership: removed {skipped_parent_status} parent-not-found "
                "IF block(s); the keyed SELECT now owns that status."
            )
        if inserted_groups:
            self.messages.append(
                "LRF key propagation: copied parent key values after child DCLGEN "
                f"initialization for {', '.join(sorted(inserted_groups))}."
            )
        return self.geometry.join(output)

    def _fetch_cursor_before_end(self, lines: list[str], start: int) -> str:
        depth = 0
        for index in range(start, len(lines)):
            body = self.geometry.body(lines[index]).upper().strip()
            if index > start and self._is_paragraph_header(body):
                return ""
            if re.match(r"^PERFORM\s+UNTIL\b", body):
                depth += 1
            fetch = re.search(r"\bPERFORM\s+\d{3,6}-FETCH-([A-Z0-9-]+)\b", body)
            if fetch:
                return fetch.group(1)
            if re.match(r"^END-PERFORM\b", body):
                depth -= 1
                if depth <= 0:
                    return ""
        return ""

    def _replace_body(self, line: str, body: str) -> str:
        # Keep fixed-format geometry when possible; otherwise retain the
        # existing free-format style. Layout pipeline re-sequences later.
        from converter.services.fixed_format_line_service import FixedFormatLineService
        fixed = FixedFormatLineService()
        if fixed.is_fixed_line(line):
            try:
                return fixed.replace_body(line, body)
            except Exception:  # noqa: BLE001
                return body
        indent = line[: len(line) - len(line.lstrip())]
        return f"{indent}{body}"

    @staticmethod
    def _is_paragraph_header(body: str) -> bool:
        if not body or body.startswith(("*", "/")):
            return False
        return bool(re.match(r"^[A-Z0-9][A-Z0-9-]*\.$", body))


__all__ = ["LrfKeyBindingComposer"]
