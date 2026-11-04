"""
Child fetch early-stop cleanup.

Discovers business-control flags from assignments and cursor control flow,
then preserves the discovered flag in nested child cursor loops.
"""

import re

from converter.composers.cleanup.business_control_flag_analyzer import (
    BusinessControlFlagAnalyzer,
)
from converter.composers.cleanup.cleanup_message_collector import (
    CleanupMessageCollector,
)
from converter.composers.cleanup.cobol_cleanup_line_utils import (
    CobolCleanupLineUtils,
)
from converter.composers.cleanup.cursor_nesting_analyser import (
    CursorNestingAnalyser,
)
from patterns.cobol_cleanup_patterns import (
    FETCH_PARAGRAPH_NUMBER_PATTERN,
    FETCH_UNTIL_EOC_FULL_SW_PATTERN,
    FETCH_UNTIL_EOC_OR_SW_PATTERN,
    FETCH_UNTIL_EOC_PATTERN,
    PARAGRAPH_HEADER_PATTERN,
    SW_STATUS_Y_CONTINUATION_PATTERN,
)

SW_STATUS_Y_CONTINUATION_INDENT = "                             "


class ChildFetchEarlyStopCleanup:
    def __init__(
        self,
        messages: CleanupMessageCollector,
        line_utils: CobolCleanupLineUtils | None = None,
    ) -> None:
        self.messages = messages
        self.line_utils = line_utils or CobolCleanupLineUtils()
        self.cursor_nesting = CursorNestingAnalyser(self.line_utils)
        self.business_flags = BusinessControlFlagAnalyzer(self.line_utils)

    def _logical(self, line: str) -> str:
        return self.line_utils.logical(line)

    def _leading_spaces(self, line: str) -> str:
        return self.line_utils.leading_spaces(line)

    def _normalize_sw_status_child_loop(self, text: str) -> str:
        """Normalize a legacy child business-loop into FETCH-driven processing.

        Apply only when structural evidence proves all of the following:
        - a nested cursor is opened and primed in a parent paragraph;
        - the parent loops over a business paragraph until that cursor's EOC;
        - that business paragraph assigns a business-control flag and fetches the same cursor;
        - the successful FETCH branch does not already call that business paragraph.

        This is the IDMS end-of-set -> business-control-flag conversion shape. It avoids
        mixing a priming FETCH, a business-driven loop, and a second FETCH loop.
        """
        lines = text.splitlines()
        spans = self.cursor_nesting.paragraph_spans(lines)
        if not spans:
            return text

        def render_like(reference: str, body: str) -> str:
            """Render an intermediate line without cloning sequence numbers.

            This pass can insert several physical records where one existed.
            Copying columns 1-7 and 73-80 from a reference line duplicated both
            sequence areas. Emit free-form intermediate records instead; the
            shared fixed-format composer reflows and resequences the complete
            member after the structural edit has finished.
            """
            raw = str(reference or "")
            if len(raw) >= 72 and raw[:6].isdigit():
                indicator = raw[6:7]
                return f"{indicator}{body.rstrip()}" if indicator.strip() else body.rstrip()
            indent = self._leading_spaces(raw)
            return f"{indent}{body.lstrip()}"

        def finalize_fixed_format(value: str) -> str:
            """Return semantic intermediate text; layout belongs to the owner.

            Cleanup passes must not resequence/reflow the entire member. The
            enclosing CobolCleanupComposer owns the single physical-rendering
            boundary after all semantic cleanup passes have completed.
            """
            return value

        def logical_at(index: int) -> str:
            return self._logical(lines[index]).strip()

        def find_span(name: str):
            return spans.get(str(name or "").strip().upper())

        # Find the owner/business/cursor relationship by references, not by
        # program names or hard-coded paragraph numbers.
        candidate = None
        for owner, (owner_start, owner_end) in spans.items():
            body = [logical_at(i) for i in range(owner_start + 1, owner_end + 1)]
            opens = []
            for item in body:
                m = re.match(r"^PERFORM\s+([0-9]+-OPEN-([A-Z0-9-]+))\b", item, re.I)
                if m:
                    opens.append((m.group(1).upper(), m.group(2).upper()))
            for open_name, cursor in opens:
                fetch_name = close_name = ""
                for name in spans:
                    upper = name.upper()
                    if upper.endswith(f"-FETCH-{cursor}"):
                        fetch_name = upper
                    elif upper.endswith(f"-CLOSE-{cursor}"):
                        close_name = upper
                if not fetch_name or not close_name:
                    continue

                fetch_ref = re.compile(rf"^PERFORM\s+{re.escape(fetch_name)}\b", re.I)
                business_loop = None
                for idx in range(owner_start + 1, owner_end + 1):
                    item = logical_at(idx)
                    m = re.match(
                        r"^PERFORM\s+(?P<business>[A-Z][A-Z0-9-]*)\s+UNTIL\s+"
                        rf"{re.escape(cursor)}-EOC(?:\s+OR\s+[A-Z][A-Z0-9-]*(?:\s*=\s*['\"]Y['\"])?|\s+OR)?\.?$",
                        item,
                        re.I,
                    )
                    # Also support split fixed-format PERFORM / UNTIL.
                    if not m and re.match(r"^PERFORM\s+[A-Z][A-Z0-9-]*\s*$", item, re.I) and idx + 1 <= owner_end:
                        target = re.match(r"^PERFORM\s+([A-Z][A-Z0-9-]*)", item, re.I).group(1)
                        nxt = logical_at(idx + 1)
                        if re.match(rf"^UNTIL\s+{re.escape(cursor)}-EOC\.?$", nxt, re.I):
                            m = type("Match", (), {"group": lambda self, key: target if key == "business" else None})()
                    if m:
                        business = m.group("business").upper()
                        if find_span(business):
                            business_start, business_end = find_span(business)
                            business_body = [
                                logical_at(i)
                                for i in range(business_start + 1, business_end + 1)
                            ]
                            flag_evidence = self.business_flags.analyze(lines)
                            assigned_flags = {
                                name
                                for name, evidence in flag_evidence.items()
                                if any(
                                    str(assignment.get("paragraph", "")).upper() == business
                                    and str(assignment.get("value", "")).upper() == "Y"
                                    for assignment in evidence.assignments
                                )
                            }
                            repeats_fetch = any(fetch_ref.match(x) for x in business_body)
                            if len(assigned_flags) == 1 and repeats_fetch:
                                candidate = {
                                    "owner": owner,
                                    "owner_span": (owner_start, owner_end),
                                    "cursor": cursor,
                                    "fetch": fetch_name,
                                    "close": close_name,
                                    "business": business,
                                    "business_span": (business_start, business_end),
                                    "flag": next(iter(assigned_flags)),
                                }
                                break
                if candidate:
                    break
            if candidate:
                break

        if not candidate:
            return text

        owner_start, owner_end = candidate["owner_span"]
        business_start, business_end = candidate["business_span"]
        fetch_name = candidate["fetch"]
        close_name = candidate["close"]
        cursor = candidate["cursor"]
        business = candidate["business"]
        stop_flag = candidate["flag"]

        # The fetch success branch must not already be bound to business.
        fetch_start, fetch_end = spans[fetch_name]
        when_zero = -1
        bound = False
        continue_index = -1
        for idx in range(fetch_start + 1, fetch_end + 1):
            item = logical_at(idx).upper().rstrip(".")
            if re.match(r"^WHEN\s+ZERO\b", item):
                when_zero = idx
                continue
            if when_zero >= 0 and re.match(r"^WHEN\b|^END-EVALUATE\b", item):
                break
            if when_zero >= 0:
                if re.match(rf"^PERFORM\s+{re.escape(business)}\b", item, re.I):
                    bound = True
                if re.match(r"^CONTINUE\.?$", item, re.I):
                    continue_index = idx
        if bound or continue_index < 0:
            return text

        # Locate the parent-loop driver and the initial (priming) FETCH.
        owner_perform = -1
        owner_until_end = -1
        priming_fetch = -1
        for idx in range(owner_start + 1, owner_end + 1):
            item = logical_at(idx)
            if re.match(rf"^PERFORM\s+{re.escape(fetch_name)}\b", item, re.I):
                priming_fetch = idx
            if re.match(rf"^PERFORM\s+{re.escape(business)}\s+UNTIL\b", item, re.I):
                owner_perform = idx
                owner_until_end = idx
                if stop_flag in item.upper():
                    pass
                elif idx + 1 <= owner_end and re.match(rf"^{re.escape(stop_flag)}\s*=", logical_at(idx + 1), re.I):
                    owner_until_end = idx + 1
            elif re.match(rf"^PERFORM\s+{re.escape(business)}\s*$", item, re.I) and idx + 1 <= owner_end and re.match(rf"^UNTIL\s+{re.escape(cursor)}-EOC", logical_at(idx + 1), re.I):
                owner_perform = idx
                owner_until_end = idx + 1

        if priming_fetch < 0 or owner_perform < 0:
            return text

        # The old business paragraph tail advances the child cursor and writes
        # on SQLCODE=100. Move that output decision to after CLOSE, where the
        # business flag can guard it once per parent record.
        tail_start = -1
        for idx in range(business_start + 1, business_end + 1):
            if re.match(r"^IF\s+NOT\s+SQLCODE\s*=\s*100\b", logical_at(idx), re.I):
                tail_start = idx
                break
        if tail_start < 0:
            return text

        # Find the matching END-IF for the legacy fetch/output tail.
        def matching_end_if(start: int, limit: int) -> int:
            depth = 0
            for pos in range(start, limit + 1):
                item = logical_at(pos)
                if re.match(r"^IF\b", item, re.I):
                    depth += 1
                if re.match(r"^END-IF\b", item, re.I):
                    depth -= 1
                    if depth == 0:
                        return pos
            return -1

        tail_end = matching_end_if(tail_start, business_end)
        if tail_end < 0:
            return text

        # Find the legacy SQLCODE=100 branch that contains the final output
        # decision. Lift its body verbatim (minus only the SQLCODE wrapper),
        # because output fields, status conditions, counters and WRITE targets
        # are business-specific and must never be synthesized by this cleanup.
        sqlcode_end_start = -1
        sqlcode_end = -1
        for idx in range(tail_start + 1, tail_end):
            if re.match(r"^IF\s+SQLCODE\s*=\s*100\b", logical_at(idx), re.I):
                sqlcode_end_start = idx
                sqlcode_end = matching_end_if(idx, tail_end)
                break
        if sqlcode_end_start < 0 or sqlcode_end <= sqlcode_end_start:
            return text

        output_body_source = list(range(sqlcode_end_start + 1, sqlcode_end))
        if not output_body_source:
            return text

        # Prove this is the target shape: the lifted branch must contain a
        # direct WRITE/REWRITE or PERFORM of a paragraph that writes output.
        spans_for_output = self.cursor_nesting.paragraph_spans(lines)
        has_output_action = False
        for pos in output_body_source:
            item = logical_at(pos)
            if re.search(r"\b(?:WRITE|REWRITE)\b", item, re.I):
                has_output_action = True
                break
            performed = re.match(r"^PERFORM\s+([A-Z][A-Z0-9-]*)\b", item, re.I)
            if performed:
                target_span = spans_for_output.get(performed.group(1).upper())
                if target_span and any(
                    re.search(r"\b(?:WRITE|REWRITE)\b", logical_at(target_pos), re.I)
                    for target_pos in range(target_span[0] + 1, target_span[1] + 1)
                ):
                    has_output_action = True
                    break
        if not has_output_action:
            return text

        # Build replacements against the original line list. The lifted body
        # keeps its original statements and relative indentation, but moves
        # after CLOSE and is guarded by the discovered business flag.
        ref = lines[priming_fetch]

        def source_area(line: str) -> str:
            raw = str(line or "").rstrip("\n")
            if len(raw) >= 72:
                return raw[7:72].rstrip()
            return raw.rstrip()

        body_areas = [source_area(lines[pos]) for pos in output_body_source]
        meaningful_indents = [
            len(area) - len(area.lstrip())
            for area in body_areas if area.strip()
        ]
        base_indent = min(meaningful_indents) if meaningful_indents else 0
        lifted_lines = []
        for area in body_areas:
            if not area.strip():
                lifted_lines.append(render_like(ref, ""))
                continue
            indent = len(area) - len(area.lstrip())
            relative = max(0, indent - base_indent)
            lifted_lines.append(render_like(ref, "       " + (" " * relative) + area.lstrip()))

        loop_lines = [
            render_like(ref, f"    MOVE 'N' TO {stop_flag}"),
            render_like(ref, f"    PERFORM {fetch_name} UNTIL {cursor}-EOC OR"),
            render_like(ref, f"                                  {stop_flag} = 'Y'"),
            render_like(ref, f"    PERFORM {close_name}."),
            render_like(ref, f"    IF NOT {stop_flag} = 'Y'"),
            *lifted_lines,
            render_like(ref, "    END-IF."),
        ]

        # Replace the old priming FETCH + business loop with the single
        # FETCH-driven loop. If a MOVE N already sits immediately before the
        # old business loop, replace from that reset so it isn't duplicated.
        replace_start = priming_fetch
        # Include the old CLOSE after the business-driven loop so only one
        # CLOSE remains after the new FETCH-driven loop.
        for idx in range(owner_until_end + 1, owner_end + 1):
            if re.match(rf"^PERFORM\s+{re.escape(close_name)}\b", logical_at(idx), re.I):
                owner_until_end = idx
                break

        replace_end = owner_until_end
        lines[replace_start : replace_end + 1] = loop_lines

        # Indices have shifted. Rebuild spans and locate business/fetch
        # paragraphs by label to remove the old next-FETCH/output tail.
        spans2 = self.cursor_nesting.paragraph_spans(lines)
        business_span2 = spans2.get(business)
        fetch_span2 = spans2.get(fetch_name)
        if not business_span2 or not fetch_span2:
            return finalize_fixed_format("\n".join(lines).rstrip() + "\n")

        bstart, bend = business_span2
        current_tail = -1
        for idx in range(bstart + 1, bend + 1):
            if re.match(r"^IF\s+NOT\s+SQLCODE\s*=\s*100\b", self._logical(lines[idx]).strip(), re.I):
                current_tail = idx
                break
        if current_tail >= 0:
            depth = 0
            current_end = -1
            for idx in range(current_tail, bend + 1):
                item = self._logical(lines[idx]).strip()
                if re.match(r"^IF\b", item, re.I):
                    depth += 1
                if re.match(r"^END-IF\b", item, re.I):
                    depth -= 1
                    if depth == 0:
                        current_end = idx
                        break
            if current_end >= 0:
                del lines[current_tail : current_end + 1]

        spans3 = self.cursor_nesting.paragraph_spans(lines)
        fstart, fend = spans3[fetch_name]
        when_zero = -1
        continue_index = -1
        for idx in range(fstart + 1, fend + 1):
            item = self._logical(lines[idx]).strip().upper().rstrip(".")
            if re.match(r"^WHEN\s+ZERO\b", item):
                when_zero = idx
                continue
            if when_zero >= 0 and re.match(r"^WHEN\b|^END-EVALUATE\b", item):
                break
            if when_zero >= 0 and re.match(r"^CONTINUE\.?$", item):
                continue_index = idx
        if continue_index >= 0:
            lines[continue_index] = render_like(lines[continue_index], f"    PERFORM {business}")

        return finalize_fixed_format("\n".join(lines).rstrip() + "\n")

    def ensure_child_fetch_early_stop(self, text: str) -> str:
        if not text:
            return text

        lines = text.splitlines()
        output: list[str] = []
        changed = False
        index = 0

        while index < len(lines):
            line = lines[index]
            logical = self._logical(line)

            # Some generated fixed-format outputs split a business PERFORM
            # and its UNTIL clause across adjacent source lines.
            business_head = re.match(
                r"^\s*PERFORM\s+(?P<target>[A-Z0-9][A-Z0-9-]*)\s*$",
                logical,
                re.I,
            )
            if business_head and index + 1 < len(lines):
                until_match = re.match(
                    r"^UNTIL\s+(?P<eoc>[A-Z0-9-]+-EOC)\.?$",
                    self._logical(lines[index + 1]).strip(),
                    re.I,
                )
                target = business_head.group("target")
                if (
                    until_match
                    and not FETCH_PARAGRAPH_NUMBER_PATTERN.match(target.upper())
                    and self._business_loop_stop_flag(
                        lines, target, until_match.group("eoc")
                    )
                ):
                    stop_flag = self._business_loop_stop_flag(
                        lines, target, until_match.group("eoc")
                    )
                    self._append_business_loop_early_stop(
                        output, line, target, until_match.group("eoc"), stop_flag
                    )
                    changed = True
                    index += 2
                    continue

            # Some valid conversions keep the business paragraph as the
            # loop body and perform the next FETCH inside that paragraph:
            #   PERFORM VERWERK-CHILD UNTIL CHILD-CURSOR-EOC.
            # If that business paragraph sets a control flag and fetches the
            # matching nested cursor, its loop must also stop on that flag.
            # Looking only for PERFORM <n>-FETCH UNTIL ... misses this shape.
            business_match = re.match(
                r"^(?P<prefix>\s*PERFORM\s+)"
                r"(?P<target>[A-Z0-9][A-Z0-9-]*)"
                r"\s+UNTIL\s+(?P<eoc>[A-Z0-9-]+-EOC)\.?$",
                logical,
                re.I,
            )
            if (
                business_match
                and not FETCH_PARAGRAPH_NUMBER_PATTERN.match(
                    business_match.group("target").upper()
                )
                and self._business_loop_stop_flag(
                    lines,
                    business_match.group("target"),
                    business_match.group("eoc"),
                )
            ):
                stop_flag = self._business_loop_stop_flag(
                    lines, business_match.group("target"), business_match.group("eoc")
                )
                self._append_early_stop(output, line, business_match, stop_flag)
                changed = True
                index += 1
                continue

            full_match = FETCH_UNTIL_EOC_FULL_SW_PATTERN.match(logical)
            if full_match and self._is_child_or_nested_fetch(
                lines, full_match.group("fetch")
            ):
                stop_flag = full_match.groupdict().get("flag") or self._flag_from_loop_condition(logical) or self._fetch_business_flow_stop_flag(lines, full_match.group("fetch"))
                if stop_flag:
                    self._append_early_stop(output, line, full_match, stop_flag)
                else:
                    output.append(line)
                changed = True
                index += 1
                continue

            or_match = FETCH_UNTIL_EOC_OR_SW_PATTERN.match(logical)
            if or_match and self._is_child_or_nested_fetch(
                lines, or_match.group("fetch")
            ):
                stop_flag = or_match.groupdict().get("flag") or self._flag_from_loop_condition(logical) or self._fetch_business_flow_stop_flag(lines, or_match.group("fetch"))
                if stop_flag:
                    self._append_early_stop(output, line, or_match, stop_flag)
                else:
                    output.append(line)
                changed = True

                if self._next_line_is_sw_status_y_continuation(lines, index):
                    index += 2
                else:
                    index += 1
                continue

            match = FETCH_UNTIL_EOC_PATTERN.match(logical)
            if (
                match
                and self._is_child_or_nested_fetch(lines, match.group("fetch"))
                and self._fetch_business_flow_stop_flag(lines, match.group("fetch"))
            ):
                # A nested cursor is not sufficient evidence by itself.
                # Infer the business flag from assignments and control-flow reads.
                stop_flag = self._fetch_business_flow_stop_flag(lines, match.group("fetch"))
                self._append_early_stop(output, line, match, stop_flag)
                changed = True
                index += 1
                continue

            output.append(line)
            index += 1

        if changed:
            self.messages.add("child_fetch_early_stop")

        result = "\n".join(output).rstrip() + "\n"
        return self._normalize_sw_status_child_loop(result)

    @staticmethod
    def _flag_from_loop_condition(logical: str) -> str | None:
        """Read the actual flag from an existing EOC OR flag='Y' condition."""
        match = re.search(
            r"\bOR\s+(?P<flag>[A-Z][A-Z0-9-]*)\s*=\s*['\"]Y['\"]",
            logical,
            re.I,
        )
        return match.group("flag").upper() if match else None

    def _append_early_stop(
        self,
        output: list[str],
        line: str,
        match,
        stop_flag: str,
    ) -> None:
        leading = self._leading_spaces(line)
        fetch_paragraph = match.groupdict().get("fetch") or match.groupdict().get("target")
        eoc_flag = match.group("eoc")

        if not self._previous_output_has_reset(output, stop_flag):
            output.append(f"{leading}MOVE 'N' TO {stop_flag}")

        output.append(f"{leading}PERFORM {fetch_paragraph} UNTIL {eoc_flag} OR")
        output.append(f"{leading}{SW_STATUS_Y_CONTINUATION_INDENT}{stop_flag} = 'Y'")

    def _next_line_is_sw_status_y_continuation(
        self,
        lines: list[str],
        index: int,
    ) -> bool:
        if index + 1 >= len(lines):
            return False

        logical = self._logical(lines[index + 1])
        return bool(SW_STATUS_Y_CONTINUATION_PATTERN.match(logical))

    def _previous_output_has_reset(self, output: list[str], flag: str) -> bool:
        """Check for a still-valid reset in this paragraph's current flow.

        A fixed-size lookback can accidentally reuse a MOVE 'N' from the
        preceding paragraph, or from a previous child-cursor loop. The
        shared early-stop flag is mutable state: once a prior child loop can
        set it to 'Y', a new child loop must reset it again. A reset remains
        valid only until a paragraph boundary, a prior child-fetch loop, or
        a MOVE 'Y' to the flag.
        """
        for line in reversed(output):
            logical = self._logical(line).strip()
            if not logical or logical.startswith(("*", "/")):
                continue

            if re.match(rf"^MOVE\s+['\"]N['\"]\s+TO\s+{re.escape(flag)}\b", logical, re.I):
                return True

            if re.match(
                rf"^MOVE\s+['\"]Y['\"]\s+TO\s+{re.escape(flag)}\.?$",
                logical,
                re.I,
            ):
                return False

            if (
                FETCH_UNTIL_EOC_PATTERN.match(logical)
                or FETCH_UNTIL_EOC_OR_SW_PATTERN.match(logical)
                or FETCH_UNTIL_EOC_FULL_SW_PATTERN.match(logical)
                or re.match(
                    r"^PERFORM\s+[0-9]+-FETCH-[A-Z0-9-]+\s+UNTIL\s+"
                    r"[A-Z0-9-]+-EOC\s+OR\s*$",
                    logical,
                    re.I,
                )
                # A called paragraph can mutate the stop flag even when the
                # assignment is not textually adjacent. Do not assume an
                # earlier reset remains valid across an intervening call.
                or re.match(r"^PERFORM\b", logical, re.I)
            ):
                return False

            if PARAGRAPH_HEADER_PATTERN.match(logical) and logical.endswith("."):
                return False

        return False


    def _append_business_loop_early_stop(
        self,
        output: list[str],
        line: str,
        business_paragraph: str,
        eoc_flag: str,
        stop_flag: str,
    ) -> None:
        leading = self._leading_spaces(line)
        if not self._previous_output_has_reset(output, stop_flag):
            output.append(f"{leading}MOVE 'N' TO {stop_flag}")
        output.append(f"{leading}PERFORM {business_paragraph} UNTIL {eoc_flag} OR")
        output.append(f"{leading}{SW_STATUS_Y_CONTINUATION_INDENT}{stop_flag} = 'Y'")

    def _business_loop_stop_flag(
        self, lines: list[str], business_paragraph: str, eoc_flag: str
    ) -> str | None:
        """Infer the loop's business stop flag without relying on its name."""
        spans = self.cursor_nesting.paragraph_spans(lines)
        span = spans.get(str(business_paragraph or "").strip().upper())
        if span is None:
            return None
        start, end = span
        body = [self._logical(lines[i]).strip() for i in range(start + 1, end + 1)]
        cursor_name = re.sub(r"-EOC$", "", str(eoc_flag or "").strip(), flags=re.I)
        fetch_targets = []
        for item in body:
            match = re.match(r"^PERFORM\s+(?P<target>[A-Z0-9][A-Z0-9-]*)\b", item, re.I)
            if match and match.group("target").upper().endswith(f"-FETCH-{cursor_name}".upper()):
                fetch_targets.append(match.group("target").upper())
        if not fetch_targets or not self._is_nested_business_loop(lines, cursor_name):
            return None

        # Discover by data/control-flow evidence, never by the identifier.
        # The matching FETCH plus nested-loop proof establishes scope; an
        # existing loop read is not required because this pass may be repairing
        # precisely the missing read in the generated output.
        return self.business_flags.discover_unique_yes_flag(
            lines,
            {str(business_paragraph).strip().upper()},
            cursor_name=cursor_name,
            require_control_read=False,
        )

    def _is_nested_business_loop(
        self,
        lines: list[str],
        cursor_name: str,
    ) -> bool:
        """Prove a child cursor is nested under a parent-record loop.

        Supports both architectures used by the converter:
        (1) parent FETCH invokes the child-owning business paragraph, and
        (2) the mainline loops a parent business paragraph while that paragraph
            opens/fetches a child cursor and loops a separate business paragraph.
        """
        spans = self.cursor_nesting.paragraph_spans(lines)
        cursor = str(cursor_name or "").strip().upper()
        open_pattern = re.compile(
            rf"^PERFORM\s+[0-9]+-OPEN-{re.escape(cursor)}\b", re.I
        )
        fetch_pattern = re.compile(
            rf"^PERFORM\s+[0-9]+-FETCH-{re.escape(cursor)}\b", re.I
        )
        for owner, (start, end) in spans.items():
            body = [
                self._logical(lines[i]).strip()
                for i in range(start + 1, end + 1)
            ]
            has_open = any(open_pattern.match(item) for item in body)
            has_fetch = any(fetch_pattern.match(item) for item in body)
            if not (has_open and has_fetch):
                continue

            # A child-owning paragraph is nested if it is called by a parent
            # FETCH success branch (legacy shape) or is itself invoked in a
            # mainline loop controlled by a different cursor's EOC flag.
            if self.cursor_nesting.is_nested_fetch(
                lines, self._fetch_name_for_cursor(lines, cursor)
            ):
                return True

            owner_loop = re.compile(
                rf"^PERFORM\s+{re.escape(owner)}\s+UNTIL\s+"
                rf"(?P<eoc>[A-Z0-9-]+-EOC)\.?$",
                re.I,
            )
            for index, line in enumerate(lines):
                logical = self._logical(line).strip()
                owner_match = owner_loop.match(logical)
                if (
                    owner_match
                    and owner_match.group("eoc").upper() != f"{cursor}-EOC"
                ):
                    return True
                # Fixed-format source may split PERFORM and UNTIL over lines.
                if (
                    re.match(
                        rf"^PERFORM\s+{re.escape(owner)}\s*$",
                        logical,
                        re.I,
                    )
                    and index + 1 < len(lines)
                ):
                    next_logical = self._logical(lines[index + 1]).strip()
                    next_match = re.match(
                        r"^UNTIL\s+(?P<eoc>[A-Z0-9-]+-EOC)\.?$",
                        next_logical,
                        re.I,
                    )
                    if (
                        next_match
                        and next_match.group("eoc").upper() != f"{cursor}-EOC"
                    ):
                        return True
        return False

    def _fetch_name_for_cursor(
        self, lines: list[str], cursor_name: str
    ) -> str:
        """Find a declared fetch paragraph for a cursor without assuming its number."""
        spans = self.cursor_nesting.paragraph_spans(lines)
        suffix = f"-FETCH-{cursor_name}".upper()
        for name in spans:
            if name.endswith(suffix):
                return name
        return ""

    def _fetch_business_flow_stop_flag(
        self, lines: list[str], fetch_paragraph: str
    ) -> str | None:
        """Return a uniquely evidenced flag assigned by successful-fetch flow."""
        spans = self.cursor_nesting.paragraph_spans(lines)
        candidate = str(fetch_paragraph or "").strip().upper()
        span = spans.get(candidate)
        if span is None:
            return None
        start, end = span
        targets: list[str] = []
        in_zero = False
        for index in range(start + 1, min(end + 1, len(lines))):
            statement = self._logical(lines[index]).strip().upper().rstrip(".")
            if re.match(r"^WHEN\s+ZERO\b", statement):
                in_zero = True
                continue
            if re.match(r"^WHEN\b|^END-EVALUATE\b", statement):
                if in_zero:
                    break
                continue
            if in_zero:
                target = self._perform_target(statement)
                if target and target in spans:
                    targets.append(target)
        pending = list(targets)
        visited: set[str] = set()
        while pending:
            paragraph = pending.pop().upper()
            if paragraph in visited or paragraph not in spans:
                continue
            visited.add(paragraph)
            p_start, p_end = spans[paragraph]
            for index in range(p_start + 1, min(p_end + 1, len(lines))):
                statement = self._logical(lines[index]).strip()
                target = self._perform_target(statement)
                if target and target in spans and target not in visited:
                    pending.append(target)
        if not visited:
            return None
        return self.business_flags.discover_unique_yes_flag(
            lines,
            visited,
            require_control_read=False,
        )

    @staticmethod
    def _perform_target(logical: str) -> str | None:
        """Return a local PERFORM start target, including PERFORM THRU forms."""
        match = re.match(
            r"^PERFORM\s+(?P<target>[A-Z0-9][A-Z0-9-]*)"
            r"(?:\s+(?:THRU|THROUGH)\s+[A-Z0-9][A-Z0-9-]*)?\b",
            logical,
            re.I,
        )
        if not match:
            return None
        target = match.group("target").upper()
        # Cursor infrastructure is not a business-flow target for this proof.
        if re.match(r"^\d+-OPEN-", target):
            return None
        if re.match(r"^\d+-CLOSE-", target):
            return None
        return target

    def _is_child_or_nested_fetch(
        self,
        lines: list[str],
        fetch_paragraph: str,
    ) -> bool:
        """Identify child cursors by nesting, not generated paragraph numbers."""
        if not FETCH_PARAGRAPH_NUMBER_PATTERN.match(
            str(fetch_paragraph or "").upper()
        ):
            return False
        return self.cursor_nesting.is_nested_fetch(lines, fetch_paragraph)
