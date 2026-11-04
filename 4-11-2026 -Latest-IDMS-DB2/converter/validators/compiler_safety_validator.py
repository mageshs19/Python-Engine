"""Static preflight checks for common COBOL/DB2 compile failures.

These checks are deliberately conservative: they report only structural
problems that can be established from generated source, and do not claim to
replace the DB2 precompiler or IBM Enterprise COBOL compiler.
"""
from __future__ import annotations

import re

_FIXED_LINE = re.compile(r"^\d{6}[ */Dd-]?")
_LEVEL_ENTRY = re.compile(r"^\s*(?:0[1-9]|[1-4]\d|66|77|88)\s+", re.I)
_CURSOR_DECLARE = re.compile(r"\bDECLARE\s+([A-Z0-9_-]+)\s+CURSOR\b", re.I)
_FETCH = re.compile(r"\bFETCH\s+([A-Z0-9_-]+)\b", re.I)
_HOST = re.compile(r":\s*[A-Z][A-Z0-9_-]*(?:\.[A-Z][A-Z0-9_-]*)?", re.I)


class CompilerSafetyValidator:
    """Find source-level hazards before submitting a mainframe compile."""

    def validate(self, cobol_text: str) -> list[str]:
        text = str(cobol_text or "")
        if not text.strip():
            return ["Compiler preflight: source is empty."]

        logical_lines = [self._logical(line) for line in text.splitlines()]
        lines = self._mask_executable_lines(logical_lines)
        messages: list[str] = []
        messages.extend(self._redefines_value(lines))
        messages.extend(self._sql_block_balance(lines))
        messages.extend(self._sqlcode_sentence_terminators(lines))
        messages.extend(self._cursor_fetch_parity(lines))
        return messages

    @staticmethod
    def _logical(line: str) -> str:
        """Return executable-area text, excluding fixed-format metadata/comments."""
        raw = str(line or "").rstrip("\r\n")
        if len(raw) >= 7 and raw[:6].isdigit():
            indicator = raw[6:7]
            if indicator in {"*", "/", "D", "d"}:
                return ""
            return raw[7:72]
        return raw

    @staticmethod
    def _mask_executable_lines(lines: list[str]) -> list[str]:
        """Mask literals, inline comments and SQL comments without shifting columns.

        The compiler preflight is lexical, so tokens such as END-EXEC inside
        a string or comment must not alter SQL block balance or cursor parsing.
        Block-comment state is carried across physical lines.
        """
        result: list[str] = []
        in_block_comment = False
        for line in lines:
            chars = list(str(line or ""))
            quote: str | None = None
            i = 0
            while i < len(chars):
                if in_block_comment:
                    if i + 1 < len(chars) and chars[i] == "*" and chars[i + 1] == "/":
                        chars[i] = chars[i + 1] = " "
                        in_block_comment = False
                        i += 2
                    else:
                        chars[i] = " "
                        i += 1
                    continue

                char = chars[i]
                if quote is not None:
                    chars[i] = " "
                    if char == quote:
                        if i + 1 < len(chars) and chars[i + 1] == quote:
                            chars[i + 1] = " "
                            i += 2
                            continue
                        quote = None
                    i += 1
                    continue

                if char in {"'", '"'}:
                    quote = char
                    chars[i] = " "
                    i += 1
                    continue
                if i + 1 < len(chars) and char == "/" and chars[i + 1] == "*":
                    chars[i] = chars[i + 1] = " "
                    in_block_comment = True
                    i += 2
                    continue
                if i + 1 < len(chars) and char == "-" and chars[i + 1] == "-":
                    for j in range(i, len(chars)):
                        chars[j] = " "
                    break
                if i + 1 < len(chars) and char == "*" and chars[i + 1] == ">":
                    for j in range(i, len(chars)):
                        chars[j] = " "
                    break
                i += 1
            result.append("".join(chars))
        return result

    def _redefines_value(self, lines: list[str]) -> list[str]:
        messages: list[str] = []
        declaration: list[str] = []
        start_line = 0

        def check() -> None:
            if not declaration:
                return
            joined = " ".join(declaration)
            if re.search(r"\bREDEFINES\b", joined, re.I) and re.search(
                r"\bVALUE(?:S)?\b", joined, re.I
            ):
                messages.append(
                    "Compiler preflight: REDEFINES declaration has a VALUE "
                    f"clause near line {start_line}; a redefined item must not "
                    "be initialized independently."
                )

        for number, line in enumerate(lines, start=1):
            if not line or line.startswith("*") or line.startswith("/"):
                continue
            if _LEVEL_ENTRY.match(line):
                check()
                declaration = [line]
                start_line = number
            elif declaration:
                declaration.append(line)
        check()
        return messages

    @staticmethod
    def _sql_block_balance(lines: list[str]) -> list[str]:
        messages: list[str] = []
        open_count = 0
        for number, line in enumerate(lines, start=1):
            if not line or line.startswith("*") or line.startswith("/"):
                continue
            upper = line.upper()
            opens = len(re.findall(r"\bEXEC\s+SQL\b", upper))
            closes = len(re.findall(r"\bEND-EXEC\b", upper))
            open_count += opens - closes
            if open_count < 0:
                messages.append(
                    f"Compiler preflight: END-EXEC without matching EXEC SQL near line {number}."
                )
                open_count = 0
        if open_count:
            messages.append(
                f"Compiler preflight: {open_count} EXEC SQL block(s) lack END-EXEC."
            )
        return messages

    @staticmethod
    def _sqlcode_sentence_terminators(lines: list[str]) -> list[str]:
        """Flag periods that terminate an EVALUATE SQLCODE before END-EVALUATE.

        A period in a WHEN branch closes the COBOL sentence and can make the
        following END-EVALUATE an orphan. Generated SQL handlers must use the
        paragraph-level period after END-EVALUATE instead.
        """
        messages: list[str] = []
        active: list[tuple[int, bool]] = []
        for number, line in enumerate(lines, start=1):
            if not line or line.startswith(("*", "/")):
                continue
            upper = line.upper()
            if re.search(r"\bEVALUATE\s+SQLCODE\b", upper):
                active.append((number, False))
                continue
            if not active:
                continue
            if re.search(r"\bEND-EVALUATE\b", upper):
                active.pop()
                continue
            # Ignore periods inside quoted literals. Only a statement-ending
            # period in the executable body is relevant to COBOL scope.
            without_literals = re.sub(r"'(?:''|[^'])*'", "''", upper)
            if re.search(r"\.\s*$", without_literals):
                start_line, _ = active[-1]
                messages.append(
                    "Compiler preflight: sentence-ending period inside EVALUATE SQLCODE "
                    f"near line {number} (block starts at line {start_line}); check END-EVALUATE scope."
                )
        return messages

    def _cursor_fetch_parity(self, lines: list[str]) -> list[str]:
        """Compare each simple cursor SELECT column count with its FETCH host count."""
        sql_blocks: list[str] = []
        current: list[str] = []
        inside = False
        for line in lines:
            if not line or line.startswith("*") or line.startswith("/"):
                continue
            upper = line.upper()
            if not inside and re.search(r"\bEXEC\s+SQL\b", upper):
                inside = True
                current = [line]
            elif inside:
                current.append(line)
            if inside and re.search(r"\bEND-EXEC\b", upper):
                sql_blocks.append(" ".join(current))
                current = []
                inside = False

        declared: dict[str, int] = {}
        fetched: dict[str, int] = {}
        for block in sql_blocks:
            declare = _CURSOR_DECLARE.search(block)
            if declare:
                cursor = declare.group(1).upper()
                select = re.search(r"\bSELECT\s+(.*?)\s+FROM\b", block, re.I)
                if select:
                    count = self._top_level_items(select.group(1))
                    if count:
                        declared[cursor] = count
            fetch = _FETCH.search(block)
            if fetch:
                cursor = fetch.group(1).upper()
                into = re.search(r"\bINTO\b(.*?)\bEND-EXEC\b", block, re.I)
                if into:
                    fetched[cursor] = len(_HOST.findall(into.group(1)))

        messages: list[str] = []
        for cursor, selected in declared.items():
            fetched_count = fetched.get(cursor)
            if fetched_count is not None and selected != fetched_count:
                messages.append(
                    f"Compiler preflight: cursor {cursor} selects {selected} column(s) "
                    f"but FETCH binds {fetched_count} host variable(s)."
                )
        return messages

    @staticmethod
    def _top_level_items(select_list: str) -> int:
        """Count comma-separated SELECT expressions, ignoring nested commas."""
        text = str(select_list or "").strip()
        if not text:
            return 0
        depth = 0
        quoted = False
        commas = 0
        i = 0
        while i < len(text):
            char = text[i]
            if char == "'":
                if quoted and i + 1 < len(text) and text[i + 1] == "'":
                    i += 2
                    continue
                quoted = not quoted
            elif not quoted:
                if char == "(":
                    depth += 1
                elif char == ")":
                    depth = max(0, depth - 1)
                elif char == "," and depth == 0:
                    commas += 1
            i += 1
        return commas + 1


__all__ = ["CompilerSafetyValidator"]
