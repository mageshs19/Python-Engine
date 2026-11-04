"""Conservative whole-block classifier for expanded IDMS logical-record access.

This analyser is diagnostic-first: unknown or non-inline control flow remains a
cursor walk. It deliberately does not render SQL or delete COBOL statements.
The post-layout singleton rewriter remains the only transformation owner until
all paragraph/THRU patterns have dedicated, tested renderers.
"""
from __future__ import annotations

import re
from collections import Counter

from rules.lr_access_rules import (
    END_OF_SET_CONDITIONS,
    END_OF_SET_STATUS_FIELDS,
    LR_ACCESS_MESSAGES,
)


class LrAccessAnalyser:
    """Classify simple inline bounded searches without mutating source text."""

    # Diagnostic gate for IDMS record/set operations. Match OBTAIN as a verb,
    # not only OBTAIN FIRST/NEXT/CALC: OWNER and direct-record OBTAIN forms are
    # valid IDMS DML and must not disappear from paragraph call-graph analysis.
    # CONNECT/DISCONNECT are included because they mutate set membership and
    # are business side effects that a future block rewriter must preserve.
    _LR_ACCESS_RE = (
        # FIND is an IDMS access verb too. Leaving it out here means a
        # paragraph containing FIND FIRST/NEXT can bypass the paragraph-flow
        # review gate even though the inline source-access scanner recognizes
        # FIND as an access shape. Keep the diagnostic gate aligned with the
        # LRF path expander's supported source verbs.
        r"\b(?:OBTAIN\b|FIND\b|STORE\s+[A-Z][A-Z0-9-]*|"
        r"MODIFY\s+[A-Z][A-Z0-9-]*|ERASE\s+[A-Z][A-Z0-9-]*|"
        r"CONNECT\s+[A-Z][A-Z0-9-]*|DISCONNECT\s+[A-Z][A-Z0-9-]*)\b|"
        r"EXPANDED LRF"
    )

    _FIXED = re.compile(r"^\d{6}([ */D-])?(.*)$", re.I)
    _OBTAIN = re.compile(
        r"\bOBTAIN\s+(?P<kind>FIRST|NEXT)\s+(?P<record>[A-Z][A-Z0-9-]*)"
        r"(?:\s+WITHIN\s+(?P<set>[A-Z][A-Z0-9-]*))?"
        r"(?P<tail>[^.\n]*)",
        re.I,
    )
    _INLINE_LOOP = re.compile(
        r"(?<![A-Z0-9-])PERFORM\s+UNTIL\s+(?P<condition>.*?)\bEND-PERFORM\b",
        re.I | re.S,
    )
    _LITERAL_EQUALITY = re.compile(
        r"\b(?P<field>[A-Z][A-Z0-9-]*)"
        r"(?:\s+(?:OF|IN)\s+[A-Z][A-Z0-9-]*)?\s*"
        r"(?:NOT\s*=|<=|>=|=|<|>)\s*"
        r"(?P<literal>'[^']*'|\"[^\"]*\"|[+-]?\d+)",
        re.I,
    )

    def __init__(self) -> None:
        self.messages: list[str] = []

    @staticmethod
    def _source_area(line: str) -> tuple[str, str]:
        """Return indicator and source area for fixed-format or free text."""
        if len(line) >= 7 and line[:6].isdigit():
            return line[6:7], line[7:72].rstrip()
        return " ", line.rstrip()

    @staticmethod
    def _strip_inline_comment(body: str) -> str:
        """Strip COBOL ``*>`` comments without cutting quoted data literals.

        COBOL permits the inline comment marker in free- and fixed-format
        source. A naive split at ``*>`` corrupts literals such as
        ``DISPLAY 'text *> not a comment'``; scan quote state and honor doubled
        quote delimiters instead.
        """
        quote: str | None = None
        index = 0
        while index < len(body):
            char = body[index]
            if quote:
                if char == quote:
                    # Doubled quote escapes itself inside a COBOL literal.
                    if index + 1 < len(body) and body[index + 1] == quote:
                        index += 2
                        continue
                    quote = None
            elif char in {"'", '"'}:
                quote = char
            elif char == "*" and index + 1 < len(body) and body[index + 1] == ">":
                return body[:index].rstrip()
            index += 1
        return body.rstrip()

    @classmethod
    def _logical_text(cls, text: str) -> str:
        bodies: list[str] = []
        for raw in str(text or "").splitlines():
            indicator, body = cls._source_area(raw)
            if indicator in {"*", "/", "D", "d"}:
                continue
            body = cls._strip_inline_comment(body).strip()
            if not body:
                continue
            if indicator == "-" and bodies:
                # This text is used for diagnostics, not source regeneration.
                # A separator prevents token merging when a COBOL statement is
                # continued across physical lines (for example PERFORM on one
                # line and its paragraph name on the next). A missing separator
                # can hide the PERFORM edge and therefore miss nested LRF work.
                # Literal contents are masked later by the diagnostic scanner.
                bodies[-1] += " " + body
            else:
                bodies.append(body)
        return "\n".join(bodies).upper()

    @staticmethod
    def _is_status_term(term: str) -> bool:
        normalized = re.sub(r"\s+", " ", term.upper()).strip()
        if any(token in normalized for token in END_OF_SET_STATUS_FIELDS):
            return True
        if any(token in normalized for token in END_OF_SET_CONDITIONS):
            return True
        if re.search(r"\b[A-Z0-9-]+-EOC\b", normalized):
            return True
        return False

    @staticmethod
    def _paragraph_labels(text: str) -> list[tuple[int, str, str]]:
        """Return paragraph labels in physical order, retaining duplicate names."""
        reserved = {
            "ACCEPT", "ADD", "CALL", "CLOSE", "COMPUTE", "CONTINUE",
            "DELETE", "DISPLAY", "DIVIDE", "ELSE", "END-EVALUATE",
            "END-IF", "END-PERFORM", "END-READ", "END-STRING",
            "END-UNSTRING", "EVALUATE", "EXIT", "FINISH", "GOBACK",
            "IF", "INITIALIZE", "INSPECT", "MERGE", "MOVE", "MULTIPLY",
            "OPEN", "PERFORM", "READ", "RELEASE", "RETURN", "REWRITE",
            "SEARCH", "SET", "SORT", "START", "STOP", "STRING",
            "SUBTRACT", "UNSTRING", "WRITE",
            # Scope and embedded-language terminators are verbs, not labels.
            "END-ADD", "END-CALL", "END-COMPUTE", "END-DELETE",
            "END-DIVIDE", "END-EVALUATE", "END-EXEC", "END-IF",
            "END-MULTIPLY", "END-PERFORM", "END-READ", "END-RECEIVE",
            "END-RETURN", "END-REWRITE", "END-SEARCH", "END-START",
            "END-STRING", "END-SUBTRACT", "END-UNSTRING", "END-WRITE",
            "END-JSON", "END-XML", "END-DECLARATIVES", "END-OF-PAGE",
            "WHEN", "NOT", "ON", "INVALID", "SIZE", "OVERFLOW",
            "DECLARATIVES",
        }
        lines = text.splitlines()
        procedure_start = next(
            (index for index, line in enumerate(lines)
             if re.search(r"\bPROCEDURE\s+DIVISION\b", line, re.I)),
            None,
        )
        # Isolated diagnostic snippets may omit PROCEDURE DIVISION.
        scan_start = procedure_start + 1 if procedure_start is not None else 0
        labels: list[tuple[int, str, str]] = []
        for index in range(scan_start, len(lines)):
            match = re.fullmatch(r"\s*([A-Z0-9][A-Z0-9-]*)\.\s*(.*?)\s*", lines[index], re.I)
            if not match:
                continue
            name = match.group(1).upper()
            if name in reserved:
                continue
            trailing = match.group(2).strip()
            if name.endswith("-SECTION") and not trailing:
                continue
            labels.append((index, name, trailing))
        return labels

    @staticmethod
    def _section_bodies(text: str) -> list[tuple[int, str, str]]:
        """Return COBOL section bodies in physical order.

        A section includes all paragraphs from its header up to (but not
        including) the next section or division header. Keep duplicate section
        names as separate entries so callers can reject ambiguous targets
        instead of silently selecting one body.
        """
        lines = text.splitlines()
        procedure_start = next(
            (index for index, line in enumerate(lines)
             if re.search(r"\bPROCEDURE\s+DIVISION\b", line, re.I)),
            None,
        )
        scan_start = procedure_start + 1 if procedure_start is not None else 0
        headers: list[tuple[int, str]] = []
        for index in range(scan_start, len(lines)):
            line = lines[index]
            match = re.fullmatch(
                r"\s*([A-Z0-9][A-Z0-9-]*)\s+SECTION\.\s*", line, re.I
            )
            if match:
                headers.append((index, match.group(1).upper()))
                continue
            if re.search(r"\b(?:IDENTIFICATION|ENVIRONMENT|DATA|PROCEDURE)\s+DIVISION\b", line, re.I):
                # A new division is a hard boundary for any preceding section.
                headers.append((index, "__DIVISION_BOUNDARY__"))
        sections: list[tuple[int, str, str]] = []
        for header_index, (line_index, name) in enumerate(headers):
            if name == "__DIVISION_BOUNDARY__":
                continue
            end_index = (
                headers[header_index + 1][0]
                if header_index + 1 < len(headers)
                else len(lines)
            )
            sections.append((line_index, name, "\n".join(lines[line_index + 1:end_index])))
        return sections

    @staticmethod
    def _paragraph_bodies(text: str) -> dict[str, str]:
        """Return paragraph bodies, conservatively unioning duplicate labels.

        Paragraph labels may be alphabetic or numeric-leading. Physical label
        order is retained separately by ``_paragraph_labels`` because a THRU
        range must include duplicate-named paragraphs that occur between its
        endpoints; a name-keyed dictionary alone cannot represent that order.
        """
        lines = text.splitlines()
        labels = LrAccessAnalyser._paragraph_labels(text)
        paragraphs: dict[str, str] = {}
        for label_index, (line_index, name, trailing) in enumerate(labels):
            end_index = labels[label_index + 1][0] if label_index + 1 < len(labels) else len(lines)
            body_lines = ([trailing] if trailing else []) + lines[line_index + 1:end_index]
            body = "\n".join(body_lines)
            if name in paragraphs:
                paragraphs[name] += "\n" + body
            else:
                paragraphs[name] = body
        return paragraphs

    @classmethod
    def _expand_procedure_copybooks(
        cls,
        text: str,
        copybooks: dict[str, str] | None,
    ) -> tuple[str, list[str]]:
        """Expand supplied procedure COPY books for analysis only.

        This deliberately supports only a standalone ``COPY name.`` statement.
        COPY REPLACING has token/pseudo-text semantics and is not approximated: it
        remains in the analysis stream with a diagnostic so callers know that
        control flow is incomplete. Source output is never modified by this step.
        Copybook keys may be supplied with or without a filename extension.
        Recursive includes are supported, with cycle/depth guards.
        """
        def key_for(value: str) -> str:
            name = str(value or "").strip().strip("\"'").upper()
            name = re.sub(r"\.(?:CPY|COPY|COB|CBL)$", "", name, flags=re.I)
            return name

        normalized: dict[str, str] = {}
        for key, value in (copybooks or {}).items():
            normalized[key_for(key)] = str(value or "")

        copy_line = re.compile(
            r"^\s*COPY\s+([A-Z0-9][A-Z0-9-]*)\s*(.*?)\s*\.\s*$", re.I
        )
        procedure_start = next(
            (index for index, line in enumerate(text.splitlines())
             if re.search(r"\bPROCEDURE\s+DIVISION\b", line, re.I)),
            None,
        )
        if procedure_start is None:
            return text, []

        diagnostics: list[str] = []
        lines = text.splitlines()

        def expand_lines(source_lines: list[str], active: tuple[str, ...], depth: int) -> list[str]:
            output: list[str] = []
            for line in source_lines:
                match = copy_line.fullmatch(line)
                if not match:
                    # COPY ... REPLACING must never be treated as a successful
                    # expansion using unmodified copybook text.
                    if re.match(r"^\s*COPY\s+[A-Z0-9][A-Z0-9-]*\b", line, re.I) and re.search(r"\bREPLACING\b", line, re.I):
                        copy_name_match = re.match(r"^\s*COPY\s+([A-Z0-9][A-Z0-9-]*)", line, re.I)
                        copy_name = copy_name_match.group(1).upper() if copy_name_match else "<UNKNOWN>"
                        diagnostics.append(
                            f"LR access: procedure COPY {copy_name} uses REPLACING; "
                            "copybook expansion was not approximated and control flow remains for review."
                        )
                    output.append(line)
                    continue

                name = key_for(match.group(1))
                tail = match.group(2).strip()
                if tail:
                    # Clauses other than the terminating period are unsupported
                    # here; do not silently ignore them.
                    if re.search(r"\bREPLACING\b", tail, re.I):
                        diagnostics.append(
                            f"LR access: procedure COPY {name} uses REPLACING; "
                            "copybook expansion was not approximated and control flow remains for review."
                        )
                    else:
                        diagnostics.append(
                            f"LR access: procedure COPY {name} has unsupported clauses; "
                            "copybook expansion was not attempted and control flow remains for review."
                        )
                    output.append(line)
                    continue
                if name not in normalized:
                    diagnostics.append(
                        f"LR access: procedure COPY {name} is unresolved; "
                        "copybook control flow remains for review."
                    )
                    output.append(line)
                    continue
                if name in active:
                    diagnostics.append(
                        f"LR access: recursive procedure COPY cycle detected at {name}; "
                        "control flow remains for review."
                    )
                    output.append(line)
                    continue
                if depth >= 16:
                    diagnostics.append(
                        f"LR access: procedure COPY expansion exceeded depth limit at {name}; "
                        "control flow remains for review."
                    )
                    output.append(line)
                    continue
                copy_text = cls._logical_text(normalized[name])
                if not copy_text.strip():
                    diagnostics.append(
                        f"LR access: procedure COPY {name} is empty; "
                        "control flow remains for review."
                    )
                    output.append(line)
                    continue
                output.extend(expand_lines(copy_text.splitlines(), active + (name,), depth + 1))
            return output

        expanded = lines[:procedure_start + 1] + expand_lines(
            lines[procedure_start + 1:], (), 0
        )
        return "\n".join(expanded), list(dict.fromkeys(diagnostics))

    @classmethod
    def _has_procedure_copy(cls, text: str) -> bool:
        """Return whether a COPY statement appears in PROCEDURE DIVISION.

        Procedure copybooks can contribute paragraphs or executable statements
        that are not visible in the current source text. If a PERFORM target is
        unresolved, the absence of a visible IDMS verb is therefore not proof
        that the target is side-effect free. Data-division COPY statements are
        deliberately excluded because they normally declare fields rather than
        procedure control flow.
        """
        lines = text.splitlines()
        procedure_start = next(
            (index for index, line in enumerate(lines)
             if re.search(r"\bPROCEDURE\s+DIVISION\b", line, re.I)),
            None,
        )
        if procedure_start is None:
            return False

        literal = re.compile(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"", re.S)
        for line in lines[procedure_start + 1:]:
            # Mask strings so DISPLAY 'COPY PROC-BOOK' is not mistaken for a
            # real compiler COPY statement. Inline comments were already
            # removed by _logical_text before this helper is called.
            code = literal.sub(" ", line)
            if re.search(r"\bCOPY\s+[A-Z0-9][A-Z0-9-]*\b", code, re.I):
                return True
        return False

    @staticmethod
    def _unsupported_loop_diagnostics(text: str) -> list[str]:
        """Explain paragraph/THRU LRF loops that are intentionally not rewritten.

        Resolve called paragraph spans (including nested PERFORM calls) when
        possible. The UNTIL condition alone is not enough: an outer input loop
        may use ``UNTIL EOF`` while its paragraph performs LRF operations.
        Diagnostics remain non-mutating; no loop is removed here.
        """
        has_visible_lr_access = bool(re.search(LrAccessAnalyser._LR_ACCESS_RE, text, re.I))
        has_procedure_copy = LrAccessAnalyser._has_procedure_copy(text)
        # If a procedure copybook is present, unresolved PERFORM targets may
        # be defined there and may contain the LRF operation itself. Continue
        # analysis even without a visible access verb so the unknown target is
        # not incorrectly treated as side-effect free. Ordinary data COPYs do
        # not trigger this conservative path.
        if not has_visible_lr_access and not has_procedure_copy:
            return []

        paragraphs = LrAccessAnalyser._paragraph_bodies(text)
        section_entries = LrAccessAnalyser._section_bodies(text)
        section_counts = Counter(name for _line, name, _body in section_entries)
        duplicate_sections = {name for name, count in section_counts.items() if count > 1}
        sections: dict[str, str] = {}
        for _line, name, body in section_entries:
            if name in sections:
                sections[name] += "\n" + body
            else:
                sections[name] = body
        # Keep physical order, including duplicate labels. A name-keyed map
        # loses repeated paragraphs and can omit an LRF-bearing paragraph from
        # a THRU range when another occurrence appears before the range start.
        names = [name for _line, name, _trailing in LrAccessAnalyser._paragraph_labels(text)]
        name_counts = Counter(names)
        duplicate_names = {name for name, count in name_counts.items() if count > 1}
        diagnostics: list[str] = []
        access_pattern = re.compile(LrAccessAnalyser._LR_ACCESS_RE, re.I)
        perform_pattern = re.compile(
            r"(?<![A-Z0-9-])PERFORM\s+([A-Z0-9][A-Z0-9-]*)"
            r"(?:\s+(?:THRU|THROUGH)\s+([A-Z0-9][A-Z0-9-]*))?", re.I
        )

        def mask_literals(body: str) -> str:
            """Mask quoted literals before recognizing executable COBOL verbs.

            A DISPLAY literal containing text like ``PERFORM X`` or
            ``OBTAIN NEXT`` is data, not control flow. Preserve newlines and
            character positions so paragraph diagnostics remain stable.
            """
            literal = re.compile(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"", re.S)
            return literal.sub(lambda match: re.sub(r"[^\n]", " ", match.group(0)), body)

        def paragraph_tree_has_access(start_names: list[str]) -> bool:
            pending = list(start_names)
            visited: set[str] = set()
            while pending:
                name = pending.pop().upper()
                if name in visited:
                    continue
                # A name-only PERFORM cannot identify which physical occurrence
                # of a duplicate paragraph label is intended. Although the
                # paragraph map conservatively unions duplicate bodies to avoid
                # hiding accesses, that union is not a valid control-flow target
                # for conversion analysis. Report ambiguity before traversing it.
                if name in duplicate_names:
                    diagnostics.append(
                        f"LR access: PERFORM target {name} has duplicate paragraph "
                        "definitions; target resolution is ambiguous and enclosing "
                        "control flow is retained for review."
                    )
                    return True
                # A name used for both a paragraph and a section, or a
                # duplicated section name, cannot be resolved from a name-only
                # PERFORM safely. Do not let a dictionary lookup hide the
                # ambiguity.
                if (name in paragraphs and name in sections) or name in duplicate_sections:
                    diagnostics.append(
                        f"LR access: PERFORM target {name} is ambiguous between COBOL "
                        "paragraph/section definitions; enclosing control flow is "
                        "retained for review."
                    )
                    return True
                if name in paragraphs:
                    body = paragraphs[name]
                elif name in sections:
                    body = sections[name]
                else:
                    # Copybook/partial-source targets may be absent. Unknown
                    # targets cannot be assumed side-effect free.
                    diagnostics.append(
                        f"LR access: PERFORM target {name} cannot be resolved "
                        "to an analyzed paragraph or section; enclosing control flow is "
                        "retained for review."
                    )
                    return True
                visited.add(name)
                body = mask_literals(body)
                if access_pattern.search(body):
                    return True
                for call in perform_pattern.finditer(body):
                    child = call.group(1).upper()
                    end = (call.group(2) or "").upper()
                    if end:
                        # A nested THRU/THROUGH call cannot be reduced to its
                        # first paragraph when either endpoint is unresolved or
                        # the range is reversed: the missing portion may hold
                        # the LRF operation. Treat that uncertainty as a review
                        # hit so an enclosing PERFORM is never classified as
                        # safe merely because the range could not be resolved.
                        if child not in names or end not in names or child in duplicate_names or end in duplicate_names:
                            diagnostics.append(
                                f"LR access: nested PERFORM {child} THRU {end} "
                                "has an unresolved or ambiguous paragraph endpoint; enclosing "
                                "control flow is retained for review."
                            )
                            return True
                        first, last = names.index(child), names.index(end)
                        if first > last:
                            diagnostics.append(
                                f"LR access: nested PERFORM {child} THRU {end} "
                                "has a reversed paragraph range; enclosing "
                                "control flow is retained for review."
                            )
                            return True
                        pending.extend(names[first:last + 1])
                    elif child in paragraphs or child in sections:
                        pending.append(child)
                    else:
                        # An unresolved paragraph call inside a paragraph tree
                        # is not proof that the caller is free of LRF effects.
                        # Preserve the caller and make the uncertainty visible.
                        diagnostics.append(
                            f"LR access: nested PERFORM {child} cannot be resolved; "
                            "enclosing control flow is retained for review."
                        )
                        return True
            return False

        # Scan all paragraph PERFORM calls, not only calls followed by UNTIL.
        # A finite PERFORM A THRU B can still execute an LRF access and must
        # remain on the diagnostic/review path until block-level conversion is
        # implemented. Mask literals so documentation text cannot look like a
        # real PERFORM statement.
        scan_text = mask_literals(text)
        inline_perform_modifiers = {"UNTIL", "VARYING", "WITH", "TEST"}
        # Inline loop forms other than the supported PERFORM UNTIL shape are
        # explicitly review-only when they contain IDMS LR access. They are
        # not paragraph calls and must not be silently ignored.
        inline_loop_start = re.compile(
            r"(?<![A-Z0-9-])PERFORM\s+(?=(?:UNTIL\b|VARYING\b|WITH\s+TEST\b|"
            r"TEST\s+(?:BEFORE|AFTER)\b|[0-9]+\s+TIMES\b))",
            re.I,
        )
        inline_loop_spans: list[tuple[int, int]] = []
        # Pair inline PERFORM scopes with one global stack. Scanning from each
        # start independently can incorrectly let an outer END-PERFORM close
        # an unterminated inner loop, hiding malformed control flow from the
        # safety diagnostics. Paragraph PERFORM calls do not enter this stack.
        loop_tokens = re.compile(
            r"(?<![A-Z0-9-])PERFORM\s+(?=(?:UNTIL\b|VARYING\b|WITH\s+TEST\b|"
            r"TEST\s+(?:BEFORE|AFTER)\b|[0-9]+\s+TIMES\b))|"
            r"\bEND-PERFORM\b",
            re.I,
        )
        inline_loop_stack: list[int] = []
        unmatched_inline_starts: list[int] = []
        for token in loop_tokens.finditer(scan_text):
            if token.group(0).upper().startswith("PERFORM"):
                inline_loop_stack.append(token.start())
            elif inline_loop_stack:
                start = inline_loop_stack.pop()
                inline_loop_spans.append((start, token.end()))
        unmatched_inline_starts.extend(inline_loop_stack)
        # An unmatched inline PERFORM containing direct or indirect LRF work
        # is a malformed/ambiguous scope. Do not silently skip it merely
        # because an END-PERFORM belonging to an inner scope was encountered.
        for start in unmatched_inline_starts:
            tail = scan_text[start:]
            has_access = bool(access_pattern.search(tail))
            if not has_access:
                for call in perform_pattern.finditer(tail):
                    child = call.group(1).upper()
                    range_end = (call.group(2) or "").upper()
                    if child in inline_perform_modifiers:
                        continue
                    if range_end:
                        if (child not in names or range_end not in names
                                or child in duplicate_names or range_end in duplicate_names):
                            has_access = True
                            break
                        first, last = names.index(child), names.index(range_end)
                        called = names[first:last + 1] if first <= last else []
                    else:
                        called = [child]
                    if paragraph_tree_has_access(called):
                        has_access = True
                        break
            if has_access:
                diagnostics.append(
                    "LR access: unmatched inline PERFORM scope contains or may reach "
                    "LRF work; source control flow is retained for review."
                )

        for start, end in inline_loop_spans:
            inline_loop = scan_text[start:end]
            if access_pattern.search(inline_loop):
                diagnostics.append(
                    "LR access: inline PERFORM VARYING/TEST/TIMES loop contains "
                    "LRF work; source control flow is retained for review."
                )
                continue
            # LRF access can be indirect: an inline VARYING/TEST/TIMES loop
            # may call a paragraph whose body performs OBTAIN/STORE/MODIFY/
            # ERASE. Follow paragraph calls and finite THRU ranges just as we
            # do for paragraph-driven outer loops.
            for call in perform_pattern.finditer(inline_loop):
                child = call.group(1).upper()
                range_end = (call.group(2) or "").upper()
                if child in inline_perform_modifiers or (
                    child.isdigit()
                    and re.match(r"\s+TIMES\b", inline_loop[call.end():], re.I)
                ):
                    continue
                if range_end:
                    if (child not in names or range_end not in names
                            or child in duplicate_names or range_end in duplicate_names):
                        diagnostics.append(
                            f"LR access: inline PERFORM loop calls unresolved or ambiguous range "
                            f"{child} THRU {range_end}; source control flow is retained for review."
                        )
                        break
                    first, last = names.index(child), names.index(range_end)
                    if first > last:
                        diagnostics.append(
                            f"LR access: inline PERFORM loop calls reversed range "
                            f"{child} THRU {range_end}; source control flow is retained for review."
                        )
                        break
                    called = names[first:last + 1]
                else:
                    called = [child]
                if paragraph_tree_has_access(called):
                    diagnostics.append(
                        "LR access: inline PERFORM loop calls paragraph(s) that "
                        "reach LRF operations; source control flow is retained for review."
                    )
                    break
        for match in perform_pattern.finditer(scan_text):
            start = match.group(1).upper()
            end = (match.group(2) or "").upper()
            # Inline PERFORM forms begin with syntax modifiers rather than a
            # paragraph name, e.g. PERFORM VARYING ..., PERFORM WITH TEST
            # AFTER UNTIL ..., and PERFORM TEST BEFORE UNTIL ... . Treating
            # these words as paragraph names can miss real paragraph calls
            # later in the same source or emit misleading range diagnostics.
            if start in inline_perform_modifiers:
                continue
            if start.isdigit() and re.match(r"\s+TIMES\b", scan_text[match.end():], re.I):
                continue
            if end:
                label = f"PERFORM {start} THRU {end}"
                if (start in names and end in names
                        and start not in duplicate_names and end not in duplicate_names):
                    first, last = names.index(start), names.index(end)
                    if first <= last:
                        called_paragraphs = names[first:last + 1]
                    else:
                        called_paragraphs = []
                        diagnostics.append(
                            f"LR access: {label} has a reversed paragraph range; "
                            "source control flow is retained for review."
                        )
                else:
                    called_paragraphs = []
                    diagnostics.append(
                        f"LR access: {label} has an unresolved or ambiguous paragraph endpoint; "
                        "source control flow is retained for review."
                    )
            else:
                label = f"PERFORM {start}"
                called_paragraphs = [start]

            reaches_access = paragraph_tree_has_access(called_paragraphs)
            # Some expanded sources no longer contain the original OBTAIN
            # statement in the paragraph fragment supplied to this analyser.
            # An explicit IDMS end-of-set/status UNTIL condition is still a
            # strong signal to retain the paragraph-driven loop for review.
            tail = scan_text[match.end():]
            until = re.match(r"\s+UNTIL\b([^.]*)\.", tail, re.I | re.S)
            condition_has_status = bool(until and re.search(
                r"\b(?:DB-END-OF-SET|ERROR-STATUS|LR-STATUS|DB-STATUS|"
                r"VMBTL|VMBEVEF|VMBEFF)\b",
                until.group(1), re.I,
            ))
            if not reaches_access and not condition_has_status:
                continue
            diagnostics.append(
                f"LR access: {label} is paragraph-driven; business control flow "
                "is retained and singleton loop removal is not attempted."
            )
        return list(dict.fromkeys(diagnostics))

    def bounded_searches(
        self,
        cobol_text: str,
        procedure_copybooks: dict[str, str] | None = None,
    ) -> dict[str, str]:
        """Return proven bounded searches, optionally analyzing supplied procedure COPY books.

        ``procedure_copybooks`` is a mapping of copybook name/path to source text.
        Supplied books are expanded for analysis only; original COBOL generation is
        not modified. Unsupported COPY clauses remain conservative diagnostics.
        """
        self.messages = []
        text = self._logical_text(cobol_text)
        text, copy_diagnostics = self._expand_procedure_copybooks(text, procedure_copybooks)
        self.messages.extend(copy_diagnostics)
        self.messages.extend(self._unsupported_loop_diagnostics(text))
        if "EXPANDED LRF FIRST" not in text and "OBTAIN FIRST" not in text:
            return {}

        loops = list(self._INLINE_LOOP.finditer(text))
        first_accesses = list(self._OBTAIN.finditer(text))
        results: dict[str, str] = {}
        ambiguous: set[str] = set()

        for loop_index, loop in enumerate(loops):
            loop_text = loop.group("condition")
            # A nested inline loop makes the first END-PERFORM ambiguous for
            # this lightweight scanner. Never classify a nested block using a
            # partial span; a full COBOL scope parser must own that rewrite.
            if re.search(r"(?<![A-Z0-9-])PERFORM\s+UNTIL\b", loop_text, re.I):
                self.messages.append(
                    "LR access: nested PERFORM UNTIL detected; bounded-search "
                    "classification omitted and cursor behavior retained."
                )
                continue
            # The NEXT statement is the only executable statement permitted
            # inside this diagnostic classification. Keep condition parsing
            # separate from the loop body so a MOVE/DISPLAY cannot be mistaken
            # for a predicate and silently labelled a bounded search.
            next_access = next(
                (m for m in self._OBTAIN.finditer(loop_text) if m.group("kind").upper() == "NEXT"),
                None,
            )
            if next_access is None:
                continue
            condition = re.sub(r"\s+", " ", loop_text[:next_access.start()]).strip()
            trailing_body = loop_text[next_access.end():].strip().strip(".")
            if trailing_body:
                continue
            # The text before NEXT contains both the UNTIL expression and
            # any statements that precede NEXT. Since this lightweight scanner
            # does not parse the full COBOL condition grammar, reject every
            # recognizable executable verb rather than maintaining a short
            # allowlist that could miss STORE/OBTAIN/PERFORM side effects.
            if re.search(
                r"\b(?:MOVE|DISPLAY|CALL|COMPUTE|ADD|SUBTRACT|MULTIPLY|DIVIDE|"
                r"IF|EVALUATE|WRITE|READ|CONTINUE|PERFORM|OBTAIN|STORE|MODIFY|"
                r"DELETE|EXEC|SQL|GOBACK|STOP|CLOSE|OPEN|EXIT|SET|INITIALIZE|"
                r"STRING|UNSTRING|INSPECT|REWRITE|RELEASE|RETURN|START|SORT|MERGE)\b",
                condition, re.I,
            ):
                continue
            # Only the narrow, proven shape is eligible: a status/EOC guard
            # plus one literal data equality. All other control flow fails shut.
            terms = re.split(r"\b(?:OR|AND)\b", condition, flags=re.I)
            status_terms = [term.strip(" ()") for term in terms if self._is_status_term(term)]
            predicates = list(self._LITERAL_EQUALITY.finditer(condition))
            data_predicates = [
                match for match in predicates
                if not self._is_status_term(match.group(0))
                and match.group("field").upper() not in {"SQLCODE", "ERROR-STATUS", "LR-STATUS", "DB-STATUS"}
            ]
            if not status_terms or len(data_predicates) != 1:
                continue

            # The loop must actually advance an OBTAIN NEXT, and a matching
            # FIRST for that record must precede the loop. This avoids treating
            # unrelated PERFORM UNTIL blocks as LRF access plans.
            loop_start = loop.start()
            next_record = next_access.group("record").upper()
            next_set = (next_access.group("set") or "").upper()
            previous_loop_end = loops[loop_index - 1].end() if loop_index else 0
            first_matches = [
                match for match in first_accesses
                if match.group("kind").upper() == "FIRST"
                and match.group("record").upper() == next_record
                and (not next_set or not match.group("set") or match.group("set").upper() == next_set)
                and previous_loop_end <= match.start() < loop_start
            ]
            if len(first_matches) != 1:
                self.messages.append(
                    LR_ACCESS_MESSAGES["loop_unreadable"].format(
                        record=next_record,
                        within="unknown set",
                        condition=condition,
                    )
                )
                continue

            predicate = data_predicates[0]
            # Preserve the full source predicate for diagnostics. The consumer
            # remains disabled unless both rendering and loop-removal gates are
            # explicitly enabled in rules.
            qualifier = re.search(
                rf"\b{re.escape(predicate.group('field'))}\s+(?:OF|IN)\s+([A-Z][A-Z0-9-]*)",
                condition,
                re.I,
            )
            record = qualifier.group(1).upper() if qualifier else next_record
            predicate_text = predicate.group(0).strip()
            if record in results:
                ambiguous.add(record)
                results.pop(record, None)
                continue
            results[record] = predicate_text

        for record in ambiguous:
            self.messages.append(
                f"LR access: multiple bounded-search sites target {record}; classification omitted."
            )
        if results:
            self.messages.append(
                f"LR access: {len(results)} inline bounded-search record(s) classified; rendering remains gated."
            )
        return results


__all__ = ["LrAccessAnalyser"]
