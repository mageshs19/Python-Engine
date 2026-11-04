"""Source-aware, fail-closed COBOL lifecycle standardization.

The composer wraps a recognized legacy main flow in the agreed 0000/1000/2000/3000
lifecycle while preserving the original PERFORM THRU ranges and the original
processing-loop statements. Cursor OPEN/FETCH setup calls are moved out of the
initialization paragraph only when they form a verified trailing setup block;
nested/child cursor work inside business paragraphs is not rewritten.
"""
from __future__ import annotations

import re
from dataclasses import dataclass


def _logical(line: str) -> str:
    text = str(line or "").rstrip()
    if len(text) >= 7 and text[:6].isdigit():
        return text[7:72].strip()
    return text.strip()


def _is_comment(line: str) -> bool:
    text = str(line or "")
    if len(text) >= 7 and text[:6].isdigit() and text[6] in "*/Dd":
        return True
    return text.lstrip().startswith(("*", "/"))


def _is_area_a_paragraph(line: str) -> bool:
    body = _logical(line)
    if not re.fullmatch(r"[A-Z0-9][A-Z0-9-]*\.", body, re.I):
        return False
    raw = str(line or "")
    area = raw[7:72] if len(raw) >= 7 and raw[:6].isdigit() else raw
    return len(area) - len(area.lstrip()) <= 3


def _append_period(line: str) -> str:
    body = _logical(line)
    if not body or body.endswith("."):
        return line
    if len(line) >= 7 and line[:6].isdigit():
        area = line[7:72].rstrip() + "."
        if len(area) > 65:
            raise ValueError("cannot terminate final DISPLAY within fixed-format Area B")
        return line[:7] + area.ljust(65) + line[72:]
    return line.rstrip() + "."


def _render(body: str) -> str:
    # Let the common final resequencer format and sequence generated lines.
    return body


def _perform_thru_lines(start: str, end: str) -> list[str]:
    statement = f"    PERFORM {start} THRU {end}."
    if len(statement) <= 65:
        return [statement]
    first = f"    PERFORM {start} THRU"
    second = f"            {end}."
    if len(first) > 65 or len(second) > 65:
        raise ValueError("PERFORM THRU targets cannot be rendered within fixed-format Area B")
    return [first, second]


@dataclass(frozen=True)
class _Paragraph:
    name: str
    start: int
    end: int


class LifecycleStandardizationComposer:
    """Normalize recognized legacy lifecycle flows without rewriting inner loops."""

    def __init__(self) -> None:
        self.messages: list[str] = []

    def compose(self, text: str) -> str:
        self.messages = []
        source = str(text or "")
        if not source:
            return source
        lines = source.splitlines()
        try:
            plan = self._plan(lines)
            if plan is None and any("Lifecycle standardization skipped:" in msg for msg in self.messages):
                return source
            if plan is None:
                # Conservative fallback for a top-level cursor-bounded flow.
                plan = self._plan_cursor_bounded_flow(lines)
            if plan is None and any("Lifecycle standardization skipped:" in msg for msg in self.messages):
                return source
            if plan is None:
                # Generic fallback for a single, explicit mainline processing loop.
                plan = self._plan_mainline_loop_flow(lines)
            if plan is None:
                renamed = self._normalize_timestamp_paragraph(lines)
                renamed = self._normalize_cursor_paragraph_numbers(renamed)
                if renamed == lines:
                    return source
                normalized = "\n".join(renamed)
                return normalized + ("\n" if source.endswith(("\n", "\r")) else "")
            if plan.get("generic_cursor_bounded"):
                result_lines = self._apply_cursor_bounded_flow(lines, plan)
            elif plan.get("generic_mainline_loop"):
                result_lines = self._apply_mainline_loop_flow(lines, plan)
            else:
                result_lines = self._apply(lines, plan)
            result_lines = self._normalize_timestamp_paragraph(result_lines)
            result_lines = self._normalize_cursor_paragraph_numbers(result_lines)
            result = "\n".join(result_lines)
            if source.endswith(("\n", "\r")):
                result += "\n"
            self.messages.append(
                "Lifecycle standardization applied: 0000 main, 1000 initialization, "
                "2000 processing, and 3000 finalization; original business statement "
                "order and SQL error behavior preserved."
            )
            return result
        except (ValueError, IndexError, KeyError) as exc:
            self.messages.append(
                f"Lifecycle standardization skipped safely: {exc}; original flow preserved."
            )
            return source

    def _plan(self, lines: list[str]) -> dict | None:
        pd_idx = next(
            (i for i, line in enumerate(lines)
             if re.match(r"^\s*PROCEDURE\s+DIVISION\b", _logical(line), re.I)),
            -1,
        )
        if pd_idx < 0:
            self.messages.append("Lifecycle standardization skipped: PROCEDURE DIVISION was not found; original flow preserved.")
            return None
        paragraphs = self._paragraphs(lines, pd_idx + 1)
        if not paragraphs:
            self.messages.append("Lifecycle standardization skipped: no local procedure paragraphs were found; original flow preserved.")
            return None
        paragraph_name_list = [p.name.upper() for p in paragraphs]
        if len(paragraph_name_list) != len(set(paragraph_name_list)):
            return self._skip("duplicate paragraph labels make PERFORM resolution ambiguous")
        if any(p.name.upper() == "0000-MAIN-PROCEDURE" for p in paragraphs):
            self.messages.append("Lifecycle standardization skipped: standard main procedure already exists.")
            return None
        reserved = {
            "1000-INITIALIZE-PROGRAM", "2000-PROCESS-PROGRAM",
            "2000-TREAT-PROGRAM", "3000-FINALIZE-PROGRAM",
        }
        if any(p.name.upper() in reserved for p in paragraphs):
            self.messages.append("Lifecycle standardization skipped: partial standard lifecycle labels already exist.")
            return None

        first_para = paragraphs[0].start
        top = [(i, _logical(lines[i])) for i in range(pd_idx + 1, first_para)
               if _logical(lines[i]) and not _is_comment(lines[i])]
        if not top:
            return None

        # Timestamp is optional but, if present in main flow, must occur once.
        timestamps = [(i, m.group(1)) for i, body in top
                      if (m := re.fullmatch(r"PERFORM\s+([A-Z0-9][A-Z0-9-]*)\s*\.?", body, re.I))
                      and "TIMESTAMP" in m.group(1).upper()]
        if len(timestamps) > 1:
            return self._skip("multiple main-flow timestamp calls")

        # Initialization is the first non-timestamp PERFORM THRU before processing.
        thru_statements = []
        continuation_indices: set[int] = set()
        for pos, (line_idx, body) in enumerate(top):
            match = re.fullmatch(
                r"PERFORM\s+([A-Z0-9][A-Z0-9-]*)\s+(?:THRU|THROUGH)\s+([A-Z0-9][A-Z0-9-]*)\s*\.?",
                body, re.I,
            )
            if not match:
                continue
            end_index = line_idx
            end_name = match.group(2)
            if pos + 1 < len(top):
                next_idx, next_body = top[pos + 1]
                until = re.fullmatch(r"UNTIL\s+([A-Z0-9][A-Z0-9-]*)\s*\.?", next_body, re.I)
                if until:
                    thru_statements.append({
                        "start": line_idx, "end": next_idx, "start_name": match.group(1),
                        "end_name": end_name, "until": until.group(1), "is_loop": True,
                    })
                    continuation_indices.add(next_idx)
                    continue
            thru_statements.append({
                "start": line_idx, "end": end_index, "start_name": match.group(1),
                "end_name": end_name, "until": "", "is_loop": False,
            })

        init_candidates = [item for item in thru_statements
                          if not item["is_loop"] and "BEGIN" in item["start_name"].upper()]
        end_candidates = [item for item in thru_statements
                          if not item["is_loop"] and any(token in item["start_name"].upper()
                                                          for token in ("EINDE", "END-PROGRAM", "FINALIZE", "TERMINATE"))]
        loops = [item for item in thru_statements if item["is_loop"]]
        exits = [(i, body) for i, body in top
                 if re.fullmatch(r"(?:GOBACK|STOP\s+RUN)\s*\.?", body, re.I)]
        totals = [(i, body) for i, body in top if re.match(r"DISPLAY\b", body, re.I) and "TOTAL" in body.upper()]
        if len(init_candidates) != 1 or len(end_candidates) != 1 or not loops or len(exits) != 1 or not totals:
            self.messages.append("Legacy lifecycle pattern not matched; attempting conservative cursor-bounded flow detection.")
            return None
        init = init_candidates[0]
        end = end_candidates[0]
        if timestamps and timestamps[0][0] >= init["start"]:
            return self._skip("timestamp call is not before initialization")
        if not (init["start"] < loops[0]["start"] < end["start"] < min(i for i, _ in totals) < exits[0][0]):
            return None
        if any(loop["start"] > end["start"] for loop in loops):
            return self._skip("a processing loop occurs after the finalization call")

        # Main-flow OPEN/FETCH PERFORMs between initialization and the first
        # loop are also processing setup. They are moved in their source order;
        # arbitrary statements in this region remain a hard stop.
        pre_loop_indices = [i for i, _ in top if i < loops[0]["start"]]
        recognized_pre = {item[0] for item in timestamps} | {init["start"]}
        main_setup: list[tuple[int, str]] = []
        by_name = {p.name.upper(): p for p in paragraphs}
        for line_index, body in top:
            if not (init["start"] < line_index < loops[0]["start"]):
                continue
            match = re.fullmatch(r"PERFORM\s+([A-Z0-9][A-Z0-9-]*)\s*\.?", body, re.I)
            if not match:
                return self._skip("unclassified executable statement before processing loop")
            target = match.group(1).upper()
            operation = "OPEN" if "OPEN" in target else "FETCH" if "FETCH" in target else ""
            target_para = by_name.get(target)
            if not operation or target_para is None:
                return self._skip(f"unclassified or unresolved pre-loop statement {body}")
            target_text = " ".join(_logical(line).upper() for line in lines[target_para.start:target_para.end])
            if not re.search(rf"\b{operation}\s+[A-Z][A-Z0-9-]*\b", target_text):
                return self._skip(f"pre-loop target {target} does not contain {operation}")
            main_setup.append((line_index, target))
            recognized_pre.add(line_index)
        if set(pre_loop_indices) != recognized_pre:
            return self._skip("unclassified executable statement before processing loop")
        # There must be no executable statement after finalization other than totals and exit.
        expected_after_end = {end["start"], exits[0][0], *(i for i, _ in totals)}
        actual_after_end = {i for i, _ in top if i >= end["start"]}
        if actual_after_end != expected_after_end:
            return self._skip("unclassified executable statement after finalization call")
        # Every main-flow executable statement is now either init/timestamp, the
        # processing region, finalization, totals, or termination. Multiple
        # processing loops and close/commit/cleanup calls are preserved verbatim.
        if set(pre_loop_indices) | {i for i, _ in top if loops[0]["start"] <= i < end["start"]} | actual_after_end != set(i for i, _ in top):
            return self._skip("main-flow statement classification is incomplete")

        by_name = {p.name.upper(): p for p in paragraphs}
        init_start = init["start_name"].upper()
        init_end = init["end_name"].upper()
        end_start = end["start_name"].upper()
        end_exit = end["end_name"].upper()
        if any(name not in by_name for name in (init_start, init_end, end_start, end_exit)):
            return self._skip("an initialization/finalization PERFORM THRU target is unresolved")
        standardized_begin = self._standard_begin_name(init_start)
        standardized_exit = f"{standardized_begin}-EXIT"
        if standardized_begin in by_name and standardized_begin != init_start:
            return self._skip(f"standardized begin paragraph {standardized_begin} already exists")
        if standardized_exit in by_name and standardized_exit != init_end:
            return self._skip(f"standardized begin exit paragraph {standardized_exit} already exists")
        if not (by_name[init_start].start < by_name[init_end].start and by_name[end_start].start < by_name[end_exit].start):
            return self._skip("initialization/finalization THRU endpoints are out of order")
        for loop in loops:
            loop_start = by_name.get(loop["start_name"].upper())
            loop_end = by_name.get(loop["end_name"].upper())
            if not loop_start or not loop_end:
                return self._skip(f"processing PERFORM THRU target {loop['start_name']} / {loop['end_name']} is unresolved")
            if loop_start.start >= loop_end.start:
                return self._skip(f"processing PERFORM THRU range {loop['start_name']} THRU {loop['end_name']} is out of order")

        # Do not standardize a flow whose numbered paragraph references are
        # already unresolved; wrapping it would hide rather than repair that defect.
        paragraph_names = {p.name.upper() for p in paragraphs}
        numeric_perform = re.compile(r"\bPERFORM\s+(\d{3,6}-[A-Z0-9-]+)\b", re.I)
        source_processing = lines[loops[0]["start"]:end["start"]]
        checked_regions = source_processing + lines[by_name[init_start].start:by_name[init_end].end]
        if timestamps and re.match(r"^\d{3,6}-", timestamps[0][1]) and timestamps[0][1].upper() not in paragraph_names:
            return self._skip(f"timestamp target {timestamps[0][1]} is unresolved")
        for source_line in checked_regions:
            if _is_comment(source_line):
                continue
            for target_match in numeric_perform.finditer(_logical(source_line)):
                target = target_match.group(1).upper()
                if target not in paragraph_names:
                    return self._skip(f"numbered PERFORM target {target} is unresolved")

        # Move only a verified trailing sequence of cursor OPEN/FETCH PERFORMs
        # from the initialization paragraph to processing. Nested cursor calls
        # elsewhere are not inspected or changed.
        init_para, init_exit_para = by_name[init_start], by_name[init_end]
        trailing_cursor_calls: list[tuple[int, str]] = []
        cursor_ops = {p.name.upper(): p for p in paragraphs}
        scan = init_exit_para.start - 1
        while scan > init_para.start:
            body = _logical(lines[scan])
            if not body or _is_comment(lines[scan]):
                scan -= 1
                continue
            perform = re.fullmatch(r"PERFORM\s+([A-Z0-9][A-Z0-9-]*)\s*\.?", body, re.I)
            if not perform:
                break
            target = perform.group(1).upper()
            operation = "OPEN" if "OPEN" in target else "FETCH" if "FETCH" in target else ""
            if not operation:
                break
            target_para = cursor_ops.get(target)
            if not target_para:
                return self._skip(f"trailing cursor setup target {target} is unresolved")
            paragraph_text = " ".join(_logical(line).upper() for line in lines[target_para.start:target_para.end])
            if not re.search(rf"\b{operation}\s+[A-Z][A-Z0-9-]*\b", paragraph_text):
                return self._skip(f"trailing cursor setup target {target} does not contain {operation}")
            trailing_cursor_calls.append((scan, target))
            scan -= 1
        trailing_cursor_calls.reverse()
        # Preserve the setup block as-is and in the same order; it may include
        # a parent cursor followed by an initial fetch, or multiple cursors.
        if trailing_cursor_calls:
            indices = {i for i, _ in trailing_cursor_calls}
            executable_between = [i for i in range(trailing_cursor_calls[0][0], init_exit_para.start)
                                  if _logical(lines[i]) and not _is_comment(lines[i])]
            if set(executable_between) != indices:
                return self._skip("cursor setup calls are not a contiguous trailing initialization block")

        total_indices = [i for i, _ in totals]
        return {
            "pd_idx": pd_idx, "first_para": first_para, "paragraphs": paragraphs,
            "top_indices": {i for i, _ in top}, "timestamp": timestamps[0][1] if timestamps else "",
            "init_start": init_start, "init_end": init_end,
            "end_start": end_start, "end_exit": end_exit,
            "exit_body": exits[0][1].rstrip("."),
            "loop_start": loops[0]["start"], "end_call_start": end["start"],
            "total_indices": total_indices, "total_lines": [lines[i] for i in total_indices],
            "processing_lines": lines[loops[0]["start"]:end["start"]],
            "cursor_setup_indices": [i for i, _ in trailing_cursor_calls],
            "cursor_setup_lines": [lines[i] for i, _ in trailing_cursor_calls],
            "main_setup_lines": [lines[i] for i, _ in main_setup],
            "reference": lines[pd_idx],
        }


    def _plan_cursor_bounded_flow(self, lines: list[str]) -> dict | None:
        """Recognize a conservative non-BEGIN/EINDE mainline by cursor boundaries.

        This fallback deliberately does not infer business logic. It partitions
        the original top-level statements around an explicit OPEN...CLOSE cursor
        sequence, leaving every statement and all paragraph bodies unchanged.
        """
        pd_idx = next(
            (i for i, line in enumerate(lines)
             if re.match(r"^\s*PROCEDURE\s+DIVISION\b", _logical(line), re.I)),
            -1,
        )
        if pd_idx < 0:
            return None
        paragraphs = self._paragraphs(lines, pd_idx + 1)
        if not paragraphs:
            return None
        names = [p.name.upper() for p in paragraphs]
        if len(names) != len(set(names)) or any(
            name in {"0000-MAIN-PROCEDURE", "1000-INITIALIZE-PROGRAM",
                     "2000-PROCESS-PROGRAM", "2000-TREAT-PROGRAM",
                     "3000-FINALIZE-PROGRAM"} for name in names
        ):
            return None
        first_para = paragraphs[0].start
        top = [(i, _logical(lines[i])) for i in range(pd_idx + 1, first_para)
               if _logical(lines[i]) and not _is_comment(lines[i])]
        if not top:
            return None
        # This fallback must not compete with the legacy PERFORM-THRU planner.
        if any(re.search(r"\bPERFORM\s+[A-Z0-9][A-Z0-9-]*\s+(?:THRU|THROUGH)\b", body, re.I)
               for _, body in top):
            return None
        exits = [(i, body) for i, body in top
                 if re.fullmatch(r"(?:GOBACK|STOP\s+RUN)\s*\.?", body, re.I)]
        if len(exits) != 1:
            return None
        by_name = {p.name.upper(): p for p in paragraphs}
        cursor_calls: list[tuple[int, str, str]] = []
        for line_index, body in top:
            match = re.fullmatch(
                r"PERFORM\s+([A-Z0-9][A-Z0-9-]*)(?:\s+UNTIL\s+.+?)?\s*\.?",
                body, re.I,
            )
            if not match:
                continue
            target = match.group(1).upper()
            para = by_name.get(target)
            if not para:
                continue
            para_text = " ".join(_logical(line).upper() for line in lines[para.start:para.end]
                                  if not _is_comment(line))
            operation = next((op for op in ("OPEN", "FETCH", "CLOSE")
                              if op in target and re.search(rf"\b{op}\s+[A-Z][A-Z0-9-]*\b", para_text)), "")
            if operation:
                cursor_calls.append((line_index, target, operation))
        if not cursor_calls:
            return None
        # A cursor lifecycle must start with OPEN and finish with CLOSE. Calls
        # between them are retained in original order; malformed boundaries skip.
        opens = [item for item in cursor_calls if item[2] == "OPEN"]
        closes = [item for item in cursor_calls if item[2] == "CLOSE"]
        if len(opens) != 1 or not closes:
            self.messages.append("Lifecycle standardization skipped: generic cursor flow has ambiguous OPEN/CLOSE boundaries; original flow preserved.")
            return None
        open_idx = opens[0][0]
        close_idx = max(item[0] for item in closes)
        exit_idx, exit_body = exits[0]
        if not (open_idx < close_idx < exit_idx):
            self.messages.append("Lifecycle standardization skipped: cursor lifecycle is not ordered before program termination; original flow preserved.")
            return None
        # Do not allow cursor calls outside the selected processing span, nor
        # another OPEN/CLOSE pattern that would require a nested-flow guess.
        if any(index < open_idx or index > close_idx for index, _, _ in cursor_calls):
            self.messages.append("Lifecycle standardization skipped: cursor calls occur outside the detected processing span; original flow preserved.")
            return None
        if any(re.search(r"\bPERFORM\s+[A-Z0-9][A-Z0-9-]*\s+(?:THRU|THROUGH)\b", body, re.I)
               for _, body in top):
            return None
        return {
            "generic_cursor_bounded": True, "pd_idx": pd_idx, "first_para": first_para,
            "open_idx": open_idx, "close_idx": close_idx, "exit_idx": exit_idx,
            "exit_body": exit_body.rstrip("."),
        }

    def _plan_mainline_loop_flow(self, lines: list[str]) -> dict | None:
        """Split a clearly bounded mainline loop into lifecycle wrappers.

        This is used for legacy flat mainlines and a first MAIN/000-STUUR-style
        controller paragraph. It never rewrites paragraph bodies that contain
        business logic; it only relocates the controller statements around one
        explicit PERFORM ... UNTIL loop. Ambiguous control flow fails closed.
        """
        pd_idx = next(
            (i for i, line in enumerate(lines)
             if re.match(r"^\s*PROCEDURE\s+DIVISION\b", _logical(line), re.I)),
            -1,
        )
        if pd_idx < 0:
            return None
        paragraphs = self._paragraphs(lines, pd_idx + 1)
        names = [p.name.upper() for p in paragraphs]
        if len(names) != len(set(names)) or any(
            name in {"0000-MAIN-PROCEDURE", "1000-INITIALIZE-PROGRAM",
                     "2000-PROCESS-PROGRAM", "3000-FINALIZE-PROGRAM"}
            for name in names
        ):
            return None
        first_para = paragraphs[0] if paragraphs else None
        top_end = first_para.start if first_para else len(lines)
        top_indices = list(range(pd_idx + 1, top_end))

        def executable(index: int) -> bool:
            return bool(_logical(lines[index])) and not _is_comment(lines[index])

        def find_loop(indices: list[int]) -> list[tuple[int, int]]:
            executable_indices = [i for i in indices if executable(i)]
            loops: list[tuple[int, int]] = []
            for pos, index in enumerate(executable_indices):
                body = _logical(lines[index])
                match = re.match(r"^PERFORM\s+([A-Z0-9][A-Z0-9-]*)\b(.*)$", body, re.I)
                if not match or re.search(r"\bTHRU\b|\bTHROUGH\b", body, re.I):
                    continue
                tail = match.group(2)
                if re.search(r"\bUNTIL\b", tail, re.I):
                    loops.append((index, index))
                elif pos + 1 < len(executable_indices) and re.match(
                    r"^UNTIL\b", _logical(lines[executable_indices[pos + 1]]), re.I
                ):
                    loops.append((index, executable_indices[pos + 1]))
            return loops

        flow_kind = "flat"
        controller: _Paragraph | None = None
        flow_indices = top_indices[:]
        loops = find_loop(flow_indices)
        if not loops and first_para:
            body_indices = list(range(first_para.start + 1, first_para.end))
            candidate_loops = find_loop(body_indices)
            terminal_indices = [i for i in body_indices if re.fullmatch(
                r"(?:STOP\s+RUN|GOBACK)\s*\.?", _logical(lines[i]), re.I
            )]
            perform_count = sum(
                1 for i in body_indices
                if re.match(r"^PERFORM\b", _logical(lines[i]), re.I)
            )
            # The terminal plus one explicit loop and multiple controller
            # PERFORMs distinguishes a main controller from business paragraphs.
            if len(candidate_loops) == 1 and len(terminal_indices) == 1 and perform_count >= 2:
                controller = first_para
                flow_kind = "controller_paragraph"
                flow_indices = top_indices + body_indices
                loops = candidate_loops
                # A controller label must not be externally PERFORMed, otherwise
                # removing it could break a valid call path.
                ref = re.compile(rf"\bPERFORM\s+{re.escape(controller.name)}\b", re.I)
                for i, line in enumerate(lines):
                    if i == controller.start or _is_comment(line):
                        continue
                    if ref.search(_logical(line)):
                        return self._skip(f"main controller {controller.name} is referenced elsewhere")
        if len(loops) != 1:
            return None
        loop_start, loop_end = loops[0]

        # Terminal can be in the selected mainline/controller, or in a simple
        # following exit paragraph (for example a paragraph containing STOP RUN).
        terminal_indices = [i for i in flow_indices if executable(i) and re.fullmatch(
            r"(?:STOP\s+RUN|GOBACK)\s*\.?", _logical(lines[i]), re.I
        )]
        exit_paragraph: _Paragraph | None = None
        if len(terminal_indices) == 1:
            exit_index = terminal_indices[0]
            exit_body = _logical(lines[exit_index]).rstrip(".")
        elif not terminal_indices and first_para and controller is None:
            pbody = [i for i in range(first_para.start + 1, first_para.end) if executable(i)]
            if len(pbody) == 1 and re.fullmatch(r"(?:STOP\s+RUN|GOBACK)\s*\.?", _logical(lines[pbody[0]]), re.I):
                exit_paragraph = first_para
                exit_index = pbody[0]
                exit_body = _logical(lines[exit_index]).rstrip(".")
            else:
                return None
        else:
            return None

        # The mainline must have a single ordered loop, and the termination must
        # be after it. Preserve all other statements in their original phase.
        if exit_index < loop_end:
            return self._skip("mainline termination occurs before its processing loop")
        if flow_kind == "controller_paragraph":
            remove_start, remove_end = controller.start, controller.end
        else:
            remove_start, remove_end = -1, -1
        return {
            "generic_mainline_loop": True,
            "pd_idx": pd_idx,
            "first_para": top_end,
            "flow_indices": flow_indices,
            "loop_start": loop_start,
            "loop_end": loop_end,
            "exit_index": exit_index,
            "exit_body": exit_body,
            "controller": controller,
            "remove_start": remove_start,
            "remove_end": remove_end,
            "exit_paragraph": exit_paragraph,
            "flow_kind": flow_kind,
        }

    def _apply_mainline_loop_flow(self, original: list[str], plan: dict) -> list[str]:
        """Wrap a single source-proven mainline loop without changing SQL policy."""
        pd_idx = plan["pd_idx"]
        loop_start = plan["loop_start"]
        loop_end = plan["loop_end"]
        flow_indices = set(plan["flow_indices"])
        exit_index = plan["exit_index"]
        controller = plan["controller"]

        def retained_range(start: int, end: int) -> list[str]:
            return [original[i] for i in range(start, end)
                    if i in flow_indices and not (controller and i == controller.start)
                    and i != exit_index
                    and not (i > exit_index and _logical(original[i]) == ".")]

        # When a controller paragraph was selected, include its statements in
        # the flow while removing only the old controller label/body from the
        # untouched source tail. All source statements are sliced in place.
        init_lines = retained_range(pd_idx + 1, loop_start)
        process_lines = [original[i] for i in range(loop_start, loop_end + 1)]
        finalize_lines = retained_range(loop_end + 1, max(flow_indices) + 1)

        def terminate_last_statement(section: list[str]) -> list[str]:
            executable_section = [i for i, line in enumerate(section)
                                  if _logical(line) and not _is_comment(line)]
            if executable_section:
                last = executable_section[-1]
                section[last] = _append_period(section[last])
            return section

        init_lines = terminate_last_statement(init_lines)
        process_lines = terminate_last_statement(process_lines)
        finalize_lines = terminate_last_statement(finalize_lines)

        generated = [
            "0000-MAIN-PROCEDURE.",
            "    PERFORM 1000-INITIALIZE-PROGRAM.",
            "    PERFORM 2000-PROCESS-PROGRAM.",
            "    PERFORM 3000-FINALIZE-PROGRAM.",
            f"    {plan['exit_body']}.",
            "1000-INITIALIZE-PROGRAM.",
        ]
        generated.extend(init_lines)
        generated.append("2000-PROCESS-PROGRAM.")
        generated.extend(process_lines)
        generated.append("3000-FINALIZE-PROGRAM.")
        generated.extend(finalize_lines)

        if controller:
            tail = original[plan["remove_end"]:]
        else:
            tail = original[plan["first_para"]:]
        return original[:pd_idx + 1] + generated + tail

    def _normalize_cursor_paragraph_numbers(self, lines: list[str]) -> list[str]:
        """Normalize existing cursor operation paragraphs from SQL source evidence.

        Cursor identity comes from DECLARE CURSOR statements and each paragraph's
        actual OPEN/FETCH/CLOSE SQL. Only cursor-operation labels, their PERFORM
        references, and the corresponding SQL-LOCATION values are updated. The
        SQLCODE branches, diagnostics, and SQLERROR calls remain unchanged.
        """
        from rules.cursor_rules import cursor_paragraph_number

        pd_idx = next(
            (i for i, line in enumerate(lines)
             if re.match(r"^\s*PROCEDURE\s+DIVISION\b", _logical(line), re.I)),
            -1,
        )
        if pd_idx < 0:
            return lines
        paragraphs = self._paragraphs(lines, pd_idx + 1)
        operation_labels: list[dict[str, object]] = []
        for para in paragraphs:
            match = re.fullmatch(
                r"(?P<number>\d{3,6})-(?P<operation>OPEN|FETCH|CLOSE)-(?P<suffix>[A-Z0-9-]+)",
                para.name,
                re.I,
            )
            if not match:
                continue
            operation = match.group("operation").upper()
            code_lines = [
                _logical(line) for line in lines[para.start:para.end]
                if not _is_comment(line)
            ]
            # Mask literals so DISPLAY text cannot masquerade as an SQL operation.
            code = " ".join(
                re.sub(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"", " ", body)
                for body in code_lines
            ).upper()
            sql_names = re.findall(
                rf"\b{operation}\s+([A-Z][A-Z0-9-]*)\b", code, re.I
            )
            if len(set(sql_names)) != 1:
                continue
            cursor_name = sql_names[0].upper()
            if cursor_name not in match.group("suffix").upper():
                # Do not infer identity from a paragraph label that disagrees with SQL.
                self.messages.append(
                    f"Cursor numbering retained for {para.name}: SQL cursor {cursor_name} "
                    "does not match its paragraph label."
                )
                return lines
            operation_labels.append({
                "paragraph": para,
                "old_number": int(match.group("number")),
                "operation": operation.lower(),
                "cursor": cursor_name,
                "suffix": match.group("suffix"),
            })

        if not operation_labels:
            return lines

        # The declaration order is authoritative. If the source cannot establish
        # a unique order, preserve the original paragraph numbering and report it.
        executable_source = " ".join(
            re.sub(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"", " ", _logical(line))
            for line in lines[pd_idx + 1:]
            if not _is_comment(line)
        ).upper()
        declarations = re.findall(
            r"\bDECLARE\s+([A-Z][A-Z0-9-]*)\s+CURSOR\b", executable_source, re.I
        )
        declaration_order = list(dict.fromkeys(name.upper() for name in declarations))
        discovered_cursors = list(dict.fromkeys(
            str(item["cursor"]) for item in sorted(
                operation_labels, key=lambda item: item["paragraph"].start
            ) if item["operation"] == "open"
        ))
        if declaration_order:
            if any(cursor not in declaration_order for cursor in discovered_cursors):
                self.messages.append(
                    "Cursor numbering retained: an OPEN cursor is not present in DECLARE CURSOR order."
                )
                return lines
            cursor_order = {name: index + 1 for index, name in enumerate(declaration_order)}
        else:
            if not discovered_cursors or any(
                str(item["cursor"]) not in discovered_cursors for item in operation_labels
            ):
                self.messages.append(
                    "Cursor numbering retained: cursor declaration/order evidence is incomplete."
                )
                return lines
            cursor_order = {name: index + 1 for index, name in enumerate(discovered_cursors)}

        mappings: dict[str, str] = {}
        expected_by_para: dict[str, int] = {}
        cursor_label_names = {str(item["paragraph"].name).upper() for item in operation_labels}
        number_owner: dict[int, str] = {}
        for para in paragraphs:
            numeric = re.match(r"^(\d{3,6})-", para.name)
            if numeric:
                number_owner.setdefault(int(numeric.group(1)), para.name.upper())

        for item in operation_labels:
            cursor = str(item["cursor"])
            if cursor not in cursor_order:
                self.messages.append(
                    f"Cursor numbering retained for {item['paragraph'].name}: no proven cursor order for {cursor}."
                )
                return lines
            expected = cursor_paragraph_number(cursor_order[cursor], str(item["operation"]))
            para = item["paragraph"]
            old_label = para.name.upper()
            new_label = f"{expected}-{str(item['operation']).upper()}-{item['suffix']}".upper()
            if old_label != new_label:
                if any(p.name.upper() == new_label for p in paragraphs if p.name.upper() != old_label):
                    self.messages.append(
                        f"Cursor numbering retained: target paragraph {new_label} already exists."
                    )
                    return lines
                owner = number_owner.get(expected)
                if owner and owner not in cursor_label_names:
                    self.messages.append(
                        f"Cursor numbering retained: number {expected} is already owned by {owner}."
                    )
                    return lines
                mappings[old_label] = new_label
            expected_by_para[old_label] = expected

        result = list(lines)
        # First update paragraph labels and all code references (but never literals).
        if mappings:
            result = result[:pd_idx + 1] + self._replace_identifiers(
                result[pd_idx + 1:], mappings
            )

        # Update SQL-LOCATION only inside the matching cursor operation paragraph.
        # These values identify the operation; changing them preserves the same
        # SQLERROR path and diagnostics while keeping the location accurate.
        renamed_paragraphs = self._paragraphs(result, pd_idx + 1)
        expected_lookup: dict[str, int] = {}
        for item in operation_labels:
            old_name = str(item["paragraph"].name).upper()
            new_name = mappings.get(old_name, old_name)
            expected_lookup[new_name] = expected_by_para[old_name]
        for para in renamed_paragraphs:
            expected = expected_lookup.get(para.name.upper())
            if expected is None:
                continue
            for i in range(para.start, para.end):
                if _is_comment(result[i]):
                    continue
                fixed = len(result[i]) >= 7 and result[i][:6].isdigit()
                start, end = (7, 72) if fixed else (0, len(result[i]))
                body = result[i][start:end]
                body = re.sub(
                    r"(\bMOVE\s+)\d{3,6}(\s+TO\s+SQL-LOCATION\b)",
                    rf"\g<1>{expected}\g<2>",
                    body,
                    flags=re.I,
                )
                if fixed:
                    if len(body.rstrip()) > 65:
                        raise ValueError("SQL-LOCATION update exceeds fixed-format Area B")
                    result[i] = result[i][:7] + body.rstrip().ljust(65) + result[i][72:]
                else:
                    result[i] = body
        return result

    def _normalize_timestamp_paragraph(self, lines: list[str]) -> list[str]:
        """Rename one existing timestamp paragraph to 1100 when that number is free.

        Existing numbered business paragraphs are never displaced. If 1100 is
        already owned by another paragraph, retain the timestamp's original
        number and report the collision rather than renumbering business logic.
        """
        pd_idx = next(
            (i for i, line in enumerate(lines)
             if re.match(r"^\s*PROCEDURE\s+DIVISION\b", _logical(line), re.I)),
            -1,
        )
        if pd_idx < 0:
            return lines
        paragraphs = self._paragraphs(lines, pd_idx + 1)
        timestamps = [p for p in paragraphs if "GET-TIMESTAMP" in p.name.upper()]
        if len(timestamps) != 1:
            if len(timestamps) > 1:
                self.messages.append("Timestamp numbering retained: multiple timestamp paragraphs are present; original names preserved.")
            return lines
        timestamp = timestamps[0]
        target = "1100-GET-TIMESTAMP"
        if timestamp.name.upper() == target:
            return lines
        occupied_1100 = [p for p in paragraphs if p.name.upper().startswith("1100-") and p.name.upper() != timestamp.name.upper()]
        if occupied_1100:
            self.messages.append(
                f"Timestamp numbering retained as {timestamp.name}: 1100 is already used by {occupied_1100[0].name}; existing sub-procedure numbering preserved."
            )
            return lines
        return lines[:pd_idx + 1] + self._replace_identifiers(
            lines[pd_idx + 1:], {timestamp.name: target}
        )

    def _apply_cursor_bounded_flow(self, original: list[str], plan: dict) -> list[str]:
        """Wrap the original mainline slices without changing their statements."""
        pd_idx = plan["pd_idx"]
        paragraphs = self._paragraphs(original, pd_idx + 1)
        first_para = paragraphs[0].start
        # Preserve only the leading banner before the wrapper. Comments and
        # blanks inside each slice stay in their original lifecycle section.
        prefix = []
        for line in original[pd_idx + 1:plan["open_idx"]]:
            if _logical(line) and not _is_comment(line):
                break
            prefix.append(line)
        init_lines = original[pd_idx + 1 + len(prefix):plan["open_idx"]]
        process_lines = original[plan["open_idx"]:plan["close_idx"] + 1]
        finalize_lines = original[plan["close_idx"] + 1:plan["exit_idx"]]
        generated = [
            "0000-MAIN-PROCEDURE.",
            "    PERFORM 1000-INITIALIZE-PROGRAM.",
            "    PERFORM 2000-PROCESS-PROGRAM.",
            "    PERFORM 3000-FINALIZE-PROGRAM.",
            f"    {plan['exit_body']}.",
            "1000-INITIALIZE-PROGRAM.",
        ]
        generated.extend(init_lines)
        generated.extend(["2000-PROCESS-PROGRAM."])
        generated.extend(process_lines)
        generated.append("3000-FINALIZE-PROGRAM.")
        generated.extend(finalize_lines)
        # Replace the original top-level executable flow, leaving all local
        # paragraphs (including nested cursor/business routines) untouched.
        return (original[:pd_idx + 1] + prefix + generated + original[first_para:])

    def _apply(self, original: list[str], plan: dict) -> list[str]:
        lines = list(original)
        pd_idx = plan["pd_idx"]
        first_para = plan["first_para"]
        top_indices = plan["top_indices"]
        # Remove moved cursor setup PERFORM statements from the initialization body.
        for index in sorted(plan["cursor_setup_indices"], reverse=True):
            lines.pop(index)
        # Recalculate the main region after setup calls were removed.
        # Main flow is before the first paragraph and all original executable
        # statements there are replaced by the canonical wrapper structure.
        # The setup lines are moved into 2000-TREAT-PROGRAM before the old loop.
        # Find current PROCEDURE DIVISION and first paragraph after removals.
        pd_idx = next(i for i, line in enumerate(lines) if re.match(r"^\s*PROCEDURE\s+DIVISION\b", _logical(line), re.I))
        paragraphs = self._paragraphs(lines, pd_idx + 1)
        first_para = paragraphs[0].start
        # The old top-level flow is still the region between PD and first paragraph.
        retained_prefix = [line for i, line in enumerate(lines[pd_idx + 1:first_para], pd_idx + 1)
                           if _logical(line) == "" or _is_comment(line)]
        ref = plan["reference"]
        generated = [
            "0000-MAIN-PROCEDURE.",
            "    PERFORM 1000-INITIALIZE-PROGRAM.",
            "    PERFORM 2000-PROCESS-PROGRAM.",
            "    PERFORM 3000-FINALIZE-PROGRAM.",
            f"    {plan['exit_body']}.",
            "1000-INITIALIZE-PROGRAM.",
        ]
        if plan["timestamp"]:
            generated.append(f"    PERFORM {plan['timestamp']}.")
        new_init = self._standard_begin_name(plan["init_start"])
        new_init_exit = f"{new_init}-EXIT"
        generated.extend(_perform_thru_lines(new_init, new_init_exit))
        generated.extend([
            "2000-PROCESS-PROGRAM.",
            "    PERFORM 2000-TREAT-PROGRAM.",
            "2000-TREAT-PROGRAM.",
        ])
        generated.extend(plan["cursor_setup_lines"])
        generated.extend(plan["main_setup_lines"])
        generated.extend(plan["processing_lines"])
        generated.append("3000-FINALIZE-PROGRAM.")
        generated.extend(_perform_thru_lines(plan["end_start"], plan["end_exit"]))
        totals = list(plan["total_lines"])
        if totals:
            totals[-1] = _append_period(totals[-1])
        generated.extend(totals)

        # Strip all old main-flow executable lines, retaining comments/blanks.
        # The old procedure body starts at the first paragraph, so the new
        # wrapper block can safely precede the untouched source paragraphs.
        result = lines[:pd_idx + 1] + retained_prefix + [_render(body) for body in generated] + lines[first_para:]
        rename = {plan["init_end"]: new_init_exit, plan["init_start"]: new_init}
        result_pd = next(i for i, line in enumerate(result)
                         if re.match(r"^\s*PROCEDURE\s+DIVISION\b", _logical(line), re.I))
        result = result[:result_pd + 1] + self._replace_identifiers(result[result_pd + 1:], rename)
        return result

    @staticmethod
    def _standard_begin_name(original: str) -> str:
        """Number an existing BEGIN paragraph as 1200 without inventing one."""
        name = original.upper()
        if name.startswith("1200-"):
            return name
        # A previous generated artifact may already have assigned 1000 to the
        # BEGIN paragraph. Move only that label; keep its body and references.
        base = re.sub(r"^\d{3,6}-", "", name)
        return f"1200-{base}"

    @staticmethod
    def _paragraphs(lines: list[str], start: int) -> list[_Paragraph]:
        starts: list[tuple[str, int]] = []
        for i in range(start, len(lines)):
            if not _is_comment(lines[i]) and _is_area_a_paragraph(lines[i]):
                starts.append((_logical(lines[i])[:-1], i))
        return [
            _Paragraph(name, pos, starts[n + 1][1] if n + 1 < len(starts) else len(lines))
            for n, (name, pos) in enumerate(starts)
        ]

    def _replace_identifiers(self, lines: list[str], mapping: dict[str, str]) -> list[str]:
        out = []
        literal_pattern = re.compile(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"")
        for line in lines:
            if _is_comment(line):
                out.append(line)
                continue
            fixed = len(line) == 80 and line[:6].isdigit() and line[72:80].isdigit()
            start, end = (7, 72) if fixed else (0, len(line))
            body = line[start:end].rstrip() if fixed else line[start:end]
            chunks = []
            cursor = 0
            for match in literal_pattern.finditer(body):
                segment = body[cursor:match.start()]
                chunks.append(self._replace_segment(segment, mapping))
                chunks.append(match.group(0))
                cursor = match.end()
            chunks.append(self._replace_segment(body[cursor:], mapping))
            rewritten = "".join(chunks)
            if fixed:
                if len(rewritten) > 65:
                    raise ValueError("renamed paragraph/reference exceeds fixed-format Area B")
                out.append(line[:7] + rewritten.ljust(65) + line[72:])
            else:
                out.append(rewritten)
        return out

    @staticmethod
    def _replace_segment(segment: str, mapping: dict[str, str]) -> str:
        for old, new in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
            segment = re.sub(rf"(?<![A-Z0-9-]){re.escape(old)}(?![A-Z0-9-])", new, segment, flags=re.I)
        return segment

    def _skip(self, reason: str):
        self.messages.append(f"Lifecycle standardization skipped: {reason}; original flow preserved.")
        return None
