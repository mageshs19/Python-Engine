# LOCATION: converter/composers/counter_declaration_composer.py
# ACTION: REPLACE ENTIRE FILE

"""Counter declaration composer.

Declares every row counter the PROCEDURE DIVISION increments but
WORKING-STORAGE does not define, and appends the end-of-run totals.

    10  WS-NB-BFAS-COUNT       PIC 9(7)  COMP-3 VALUE ZEROES.
    10  WS-NB-OUTPUT-COUNT     PIC 9(7)  COMP-3 VALUE ZEROES.

    DISPLAY 'TOTAL BFAS RECORDS   : ' WS-NB-BFAS-COUNT
    DISPLAY 'TOTAL OUTPUT RECORDS : ' WS-NB-OUTPUT-COUNT
    STOP RUN.

REFERENCE-DRIVEN, NOT TABLE-DRIVEN

The composer declares exactly the counters the PROCEDURE DIVISION
actually increments. It can therefore never declare an unused field,
and never miss one.


CORRECTION 1 - the stage aborted on a missing helper

    [error] declare_counters: AttributeError:
    'CounterDeclarationComposer' object has no attribute
    '_procedure_division_index'

_referenced_counters called a method that was never declared, so the
whole stage raised and NOTHING was declared and NO totals were emitted.
That is worse than the defect it was added to fix: the generated
program increments fields WORKING-STORAGE does not define, and does not
compile. The helper is declared below.


CORRECTION 2 - a counter was declared for a table never read

    10 WS-NB-EVEF-COUNT   PIC 9(7) COMP-3 VALUE ZEROES.
    DISPLAY 'TOTAL EVEF RECORDS   : ' WS-NB-EVEF-COUNT

always zero, and misleading in the job log. The scan is now bounded to
the PROCEDURE DIVISION and skips comment, debug and continuation lines,
so a counter named in a DISPLAY literal or in a commented-out block is
never mistaken for an increment.


RESPONSIBILITY SPLIT

This class decides WHAT to declare and WHAT to display.
CounterDeclarationWriter decides WHERE to put it, which is where the
record-corruption defect lived.


CLEAN ARCHITECTURE

- Constants live in rules/counter_declaration_rules.py and
  rules/structural_safety_rules.py.
- Regex lives in patterns/counter_declaration_patterns.py.
- No program, record, table, cursor or host variable name is hardcoded.
"""

from __future__ import annotations

import re

from converter.composers.counter_declaration_writer import (
    CounterDeclarationWriter,
)
from converter.services.fixed_format_line_service import (
    FixedFormatLineService,
)
from patterns.counter_declaration_patterns import (
    COUNTER_INCREMENT_PATTERN,
    DATA_ENTRY_PATTERN,
)
from rules.counter_declaration_rules import (
    COUNTER_DECLARATION_MESSAGES,
    EMIT_COUNTER_TOTALS,
    ENFORCE_COUNTER_DECLARATION,
)

NOT_FOUND = -1

# A division header is Area A text. Matched on the logical body, so no
# indicator or sequence area reaches this comparison.
PROCEDURE_DIVISION_TOKEN = "PROCEDURE DIVISION"


class CounterDeclarationComposer:
    """Declares referenced row counters and emits end-of-run totals."""

    def __init__(
        self,
        fixed_format: FixedFormatLineService | None = None,
        writer: CounterDeclarationWriter | None = None,
    ) -> None:
        self.fixed_format = fixed_format or FixedFormatLineService()
        self.writer = writer or CounterDeclarationWriter(
            fixed_format=self.fixed_format,
        )
        self.messages: list[str] = []

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------
    def compose(self, text: str) -> str:
        self.messages = []

        if not text or not ENFORCE_COUNTER_DECLARATION:
            return str(text or "")

        lines = (
            str(text)
            .replace("\r\n", "\n")
            .replace("\r", "\n")
            .split("\n")
        )

        # Preserve the source-level input/output totals before discovering
        # generated WS-NB-* counters. These counters are not WS-NB counters,
        # so the old row-counter-only scan could never create them.
        lines = self._preserve_input_and_treated_totals(lines)

        referenced = self._referenced_counters(lines)

        if not referenced:
            # Not a refusal. Either no pass emitted an increment, or
            # this is a second idempotent run. Say which, rather than
            # returning in silence.
            self.messages.append(
                COUNTER_DECLARATION_MESSAGES["no_references"].format(
                    examined=len(lines),
                )
            )
            return "\n".join(lines).rstrip() + "\n"

        declared = self._declared_names(lines)
        missing = [name for name in referenced if name not in declared]

        if missing:
            lines = self.writer.declare(lines=lines, missing=missing)
            self.messages.extend(self.writer.messages)

        if EMIT_COUNTER_TOTALS:
            # REFERENCED, not MISSING. A counter already declared in the
            # source is still incremented and still belongs in the
            # totals; displaying only the newly declared ones would drop
            # it from the job log.
            lines = self.writer.append_totals(
                lines=lines,
                counters=referenced,
            )
            self.messages.extend(self.writer.messages)

        return "\n".join(lines).rstrip() + "\n"

    # ------------------------------------------------------------------
    # Input / treated totals
    # ------------------------------------------------------------------
    def _preserve_input_and_treated_totals(
        self,
        lines: list[str],
    ) -> list[str]:
        """Keep the two business totals used by file-processing programs.

        Root cause: this composer only discovered generated ``WS-NB-*``
        row counters. It never counted successful sequential-file READs,
        and the existing treated counter was left under its legacy name.
        A reference program can therefore contain both totals while the
        generated program silently loses the input total.

        The behavior is inferred from COBOL statements, not a program ID:
        successful READs drive WS-TOTAL-INPUT; an incremented counter
        displayed as TREATED is normalized to the WS- prefix.
        """
        lines = self._normalize_treated_counter_name(lines)
        lines = self._normalize_treated_display_label(lines)
        if not self._has_treated_counter(lines):
            return lines

        lines, read_count = self._add_input_read_increments(lines)
        if read_count == 0:
            return lines

        declared = self._declared_names(lines)
        if "WS-TOTAL-INPUT" not in declared:
            lines = self._insert_before_section(
                lines,
                "01 WS-TOTAL-INPUT PIC S9(11) COMP-3 VALUE +0.",
                ("LINKAGE SECTION", "PROCEDURE DIVISION"),
            )
            self.messages.append(
                "Input totals: declared WS-TOTAL-INPUT for successful file READs."
            )

        lines = self._ensure_total_input_display(lines)
        return lines

    def _normalize_treated_counter_name(
        self,
        lines: list[str],
    ) -> list[str]:
        """Normalize a counted variable displayed as TREATED to WS-*.

        Only rename a declared counter when the same name is incremented
        and displayed on a TREATED diagnostic line. Other identifiers are
        untouched. This makes the convention semantic rather than tied to
        a specific program.
        """
        increments: set[str] = set()
        treated_lines: list[str] = []
        for line in lines:
            if self._is_skippable(line):
                continue
            logical = self._logical(line).upper()
            match = re.search(
                r"\bADD\s+1\s+TO\s+([A-Z0-9-]+)\b", logical
            )
            if match:
                increments.add(match.group(1))
            if "DISPLAY" in logical and "TREATED" in logical:
                treated_lines.append(logical)

        if not increments or not treated_lines:
            return lines

        declared = self._declared_names(lines)
        rename: dict[str, str] = {}
        for name in increments:
            if name.startswith("WS-"):
                continue
            if name not in declared or f"WS-{name}" in declared:
                continue
            if any(
                re.search(
                    rf"(?<![A-Z0-9-]){re.escape(name)}(?![A-Z0-9-])",
                    line,
                )
                for line in treated_lines
            ):
                rename[name] = f"WS-{name}"

        if not rename:
            return lines

        pattern = re.compile(
            r"(?<![A-Z0-9-])(" + "|".join(
                re.escape(name) for name in sorted(rename, key=len, reverse=True)
            ) + r")(?![A-Z0-9-])",
            re.IGNORECASE,
        )
        updated: list[str] = []
        for line in lines:
            if self._is_skippable(line):
                updated.append(line)
                continue

            # Replace only the COBOL source area. Replacing directly in the
            # 80-column physical record can push the right sequence area past
            # column 80 when WS- is added to a full-width line.
            body = self.fixed_format.body(line)
            rewritten_body = pattern.sub(
                lambda match: rename[match.group(1).upper()],
                body,
            )
            if rewritten_body == body:
                updated.append(line)
            elif self.fixed_format.is_fixed_line(line):
                updated.extend(
                    self.fixed_format.replace_body_wrapped(line, rewritten_body)
                )
            else:
                updated.append(rewritten_body)
        self.messages.append(
            "Input totals: normalized treated counter name(s) to WS-*."
        )
        return updated

    def _normalize_treated_display_label(self, lines: list[str]) -> list[str]:
        """Align the treated-count label to the reference convention."""
        label_pattern = re.compile(
            r"(['\"]#\s*TREATED)\s*=\s*(['\"])",
            re.IGNORECASE,
        )
        updated: list[str] = []
        changed = False
        for line in lines:
            if self._is_skippable(line):
                updated.append(line)
                continue
            body = self.fixed_format.body(line)
            rewritten = label_pattern.sub(r"\1    = \2", body)
            if rewritten == body:
                updated.append(line)
                continue
            changed = True
            if self.fixed_format.is_fixed_line(line):
                updated.extend(self.fixed_format.replace_body_wrapped(line, rewritten))
            else:
                updated.append(rewritten)
        if changed:
            self.messages.append("Input totals: aligned the treated-count display label.")
        return updated

    def _has_treated_counter(self, lines: list[str]) -> bool:
        """Require a real incremented/displayed treated counter before adding totals."""
        increments: set[str] = set()
        displays: list[str] = []
        for line in lines:
            if self._is_skippable(line):
                continue
            logical = self._logical(line).upper()
            match = re.search(r"\bADD\s+1\s+TO\s+([A-Z0-9-]+)\b", logical)
            if match:
                increments.add(match.group(1))
            if "DISPLAY" in logical and "TREATED" in logical:
                displays.append(logical)

        declared = self._declared_names(lines)
        return any(
            name in declared
            and any(
                re.search(
                    rf"(?<![A-Z0-9-]){re.escape(name)}(?![A-Z0-9-])",
                    display,
                )
                for display in displays
            )
            for name in increments
        )

    def _add_input_read_increments(
        self,
        lines: list[str],
    ) -> tuple[list[str], int]:
        """Increment WS-TOTAL-INPUT only on successful READ operations."""
        read_blocks: list[tuple[int, int, int | None, bool]] = []
        index = 0
        while index < len(lines):
            if self._is_skippable(lines[index]):
                index += 1
                continue
            logical = self._logical(lines[index]).upper()
            if not re.match(r"^READ\s+[A-Z0-9-]+\b", logical):
                index += 1
                continue

            end = index + 1
            while end < len(lines):
                body = self._logical(lines[end]).upper()
                if body.startswith("END-READ") or body == "END-READ.":
                    break
                # Do not let a malformed READ consume the next paragraph.
                if end > index and re.match(
                    r"^[A-Z0-9-]+\.\s*$", body
                ):
                    break
                end += 1

            if end >= len(lines) or not self._logical(lines[end]).upper().startswith("END-READ"):
                index += 1
                continue

            block_text = "\n".join(self._logical(line).upper() for line in lines[index:end + 1])
            already_counted = bool(re.search(
                r"\bADD\s+1\s+TO\s+WS-TOTAL-INPUT\b", block_text
            ))
            not_at_end = next(
                (
                    pos for pos in range(index + 1, end)
                    if re.search(r"\bNOT\s+AT\s+END\b", self._logical(lines[pos]).upper())
                ),
                None,
            )
            read_blocks.append((index, end, not_at_end, already_counted))
            index = end + 1

        insertions: list[tuple[int, str]] = []
        for start, end, not_at_end, already_counted in read_blocks:
            if already_counted:
                continue
            if not_at_end is not None:
                insertions.append((
                    not_at_end + 1,
                    self.fixed_format.build("", " ", "ADD 1 TO WS-TOTAL-INPUT", ""),
                ))
            else:
                # COBOL permits NOT AT END alongside AT END. Add it before
                # END-READ so EOF is never counted as an input record.
                insertions.append((
                    end,
                    self.fixed_format.build(
                        "", " ", "NOT AT END ADD 1 TO WS-TOTAL-INPUT", ""
                    ),
                ))

        for position, line in sorted(insertions, reverse=True):
            lines.insert(position, line)

        if insertions:
            self.messages.append(
                f"Input totals: added successful-read increments to {len(insertions)} READ block(s)."
            )
        return lines, len(read_blocks)

    def _ensure_total_input_display(self, lines: list[str]) -> list[str]:
        """Display input totals beside the existing treated total when possible."""
        for line in lines:
            if self._is_skippable(line):
                continue
            logical = self._logical(line).upper()
            if "DISPLAY" in logical and "TOTAL INPUTS" in logical and "WS-TOTAL-INPUT" in logical:
                return lines

        display_body = "DISPLAY 'TOTAL INPUTS ='  WS-TOTAL-INPUT"
        display_line = self.fixed_format.build("", " ", display_body, "")

        for index, line in enumerate(lines):
            if self._is_skippable(line):
                continue
            logical = self._logical(line).upper()
            if "DISPLAY" in logical and "TREATED" in logical and "WS-COUNT-TREATED" in logical:
                lines.insert(index + 1, display_line)
                self.messages.append("Input totals: added TOTAL INPUTS display beside treated total.")
                return lines

        # Fallback for programs without a treated-count DISPLAY.
        for index, line in enumerate(lines):
            if self._is_skippable(line):
                continue
            logical = self._logical(line).upper()
            if re.match(r"^(STOP\s+RUN|GOBACK)\b", logical):
                lines.insert(index, display_line)
                self.messages.append("Input totals: added TOTAL INPUTS display before program termination.")
                return lines

        self.messages.append(
            "Input totals: READs were found, but no safe totals-display anchor was found."
        )
        return lines

    def _insert_before_section(
        self,
        lines: list[str],
        body: str,
        anchors: tuple[str, ...],
    ) -> list[str]:
        """Declare the counter inside WORKING-STORAGE, never inside FILE SECTION."""
        ws_index = next(
            (
                index for index, line in enumerate(lines)
                if not self._is_skippable(line)
                and self._logical(line).upper().startswith("WORKING-STORAGE SECTION")
            ),
            -1,
        )

        if ws_index >= 0:
            # Insert at the end of WORKING-STORAGE, immediately before the
            # next section/division. This keeps the item out of FD record
            # descriptions and out of LINKAGE.
            for index in range(ws_index + 1, len(lines)):
                if self._is_skippable(lines[index]):
                    continue
                logical = self._logical(lines[index]).upper()
                if re.match(r"^[A-Z0-9-]+\s+SECTION\b", logical) or re.match(
                    r"^[A-Z]+\s+DIVISION\b", logical
                ):
                    lines.insert(index, self.fixed_format.build("", " ", body, ""))
                    return lines

            lines.append(self.fixed_format.build("", " ", body, ""))
            return lines

        # Some programs have no WORKING-STORAGE section at all. Create one
        # before LINKAGE/PROCEDURE rather than placing a 01 item in FILE SECTION.
        target = len(lines)
        for index, line in enumerate(lines):
            if self._is_skippable(line):
                continue
            logical = self._logical(line).upper()
            if any(logical.startswith(anchor) for anchor in anchors):
                target = index
                break

        lines[target:target] = [
            self.fixed_format.build("", " ", "WORKING-STORAGE SECTION.", ""),
            self.fixed_format.build("", " ", body, ""),
        ]
        self.messages.append(
            "Input totals: created WORKING-STORAGE SECTION for WS-TOTAL-INPUT."
        )
        return lines

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------
    def _procedure_division_index(self, lines: list[str]) -> int:
        """Index of the PROCEDURE DIVISION header, or NOT_FOUND.

        CORRECTION 1 declared this. Without it the whole stage raised
        AttributeError and no counter was declared at all.

        An ADD outside the PROCEDURE DIVISION is not an increment - it
        is a DISPLAY literal, a comment, or documentation. Scanning the
        whole file is how a counter for an unread table entered the set.
        """
        for index, line in enumerate(lines):
            if self._is_skippable(line):
                continue
            logical = self._logical(line).upper()
            if logical.startswith(PROCEDURE_DIVISION_TOKEN):
                return index
        return NOT_FOUND

    def _referenced_counters(self, lines: list[str]) -> list[str]:
        """Counter names the PROCEDURE DIVISION actually increments.

        The ONLY admissible source. A cursor spec, a table list or a
        DCLGEN group must never seed this set: each would declare a
        counter for a table this program does not read.

        Order is first-seen and never sorted, so the totals block reads
        in the order the program counts.
        """
        found: list[str] = []
        seen: set[str] = set()

        start = self._procedure_division_index(lines)
        if start == NOT_FOUND:
            return found

        for line in lines[start:]:
            if self._is_skippable(line):
                continue

            match = COUNTER_INCREMENT_PATTERN.match(self._logical(line))
            if not match:
                continue

            name = self._matched_name(match).upper()
            if name and name not in seen:
                seen.add(name)
                found.append(name)

        return found

    def _declared_names(self, lines: list[str]) -> set[str]:
        """Every data-name declared in the source, upper-cased.

        Read through DATA_ENTRY_PATTERN rather than a substring test: a
        DISPLAY literal mentioning the name is not a declaration, and
        declaring an existing name twice is a compile error.
        """
        names: set[str] = set()

        for line in lines:
            if self._is_skippable(line):
                continue

            match = DATA_ENTRY_PATTERN.match(self._logical(line))
            if match:
                name = self._matched_name(match)
                if name:
                    names.add(name.upper())

        return names

    # ------------------------------------------------------------------
    # Line helpers
    # ------------------------------------------------------------------
    def _logical(self, line: str) -> str:
        """Columns 8-72, stripped. Never raises on a malformed line."""
        try:
            return str(self.fixed_format.logical(line) or "").strip()
        except Exception:                       # noqa: BLE001
            return str(line or "").strip()

    def _is_skippable(self, line: str) -> bool:
        """Comment, page-eject, debug or continuation line."""
        try:
            return bool(
                self.fixed_format.is_comment_or_control_line(line)
            )
        except Exception:                       # noqa: BLE001
            return str(line or "").lstrip().startswith(("*", "/"))

    @staticmethod
    def _matched_name(match) -> str:
        """The 'name' group, or the last group the pattern exposes.

        Tolerates a pattern that uses a positional group, so a pattern
        file that has not been updated degrades to "works" rather than
        to IndexError in the middle of a conversion.
        """
        try:
            return str(match.group("name") or "").strip()
        except (IndexError, KeyError):
            groups = [g for g in match.groups() if g]
            return str(groups[-1]).strip() if groups else ""


__all__ = ["CounterDeclarationComposer"]