"""Generic program-constant normalization and cursor WITH HOLD policy.

No program-specific working-storage reparenting, field-type coercion, or
manual-reference copybook deletion is permitted.  Those changes must be
proved by the input DCLGEN and copybook metadata in dedicated passes.
"""
from __future__ import annotations

import re



class ManualStorageParityComposer:
    _BODY_START = 7
    _BODY_END = 72

    @staticmethod
    def _split(line: str) -> tuple[str, str, str]:
        if len(line) >= 7 and line[:6].isdigit():
            return line[:6], line[6:7], line[7:72].rstrip()
        return "", " ", line.rstrip()

    @staticmethod
    def _build(seq: str, indicator: str, body: str, tail: str = "") -> str:
        prefix = f"{seq}{indicator}" if seq else ""
        if seq:
            # A generated fixed-format record must include columns 73-80.
            # An empty tail previously produced a 72-column line. The next
            # formatter treated its sequence prefix as *source code* and
            # emitted "000680 01 WS-VAR." inside the COBOL body.
            # Use a neutral identification placeholder; final resequencing
            # owns the actual right-hand sequence numbers.
            return f"{prefix}{body:<65}{tail or '00000000'}"
        return body

    def compose(self, text: str) -> str:
        if not text:
            return ""
        lines = str(text).replace("\r\n", "\n").replace("\r", "\n").split("\n")
        lines = self._normalize_program_constant(lines)
        lines = self._remove_hold_when_no_commit(lines)
        return "\n".join(lines).rstrip() + "\n"


    def _normalize_program_constant(self, lines: list[str]) -> list[str]:
        """Delegate generic program-name normalization to the shared service."""
        from converter.services.program_constant_normalizer import ProgramConstantNormalizer

        return ProgramConstantNormalizer._normalize_lines(lines)

    def _remove_hold_when_no_commit(self, lines: list[str]) -> list[str]:
        """Remove WITH HOLD unless that cursor spans a transaction boundary.

        A COMMIT elsewhere in the program is not sufficient reason to retain
        WITH HOLD. The relevant question is whether a COMMIT/ROLLBACK can occur
        between OPEN and CLOSE of the declared cursor. If control-flow markers
        are incomplete and a transaction boundary exists, retain WITH HOLD
        conservatively rather than silently changing cursor semantics.
        """
        code_lines = []
        for line in lines:
            _, indicator, body = self._split(line)
            if indicator in {"*", "/"} or body.lstrip().startswith("*"):
                continue
            code_lines.append(body)
        code = "\n".join(code_lines).upper()
        declarations = list(re.finditer(
            r"\bDECLARE\s+([A-Z0-9-]+)\s+CURSOR\s+WITH\s+HOLD\s+FOR\b",
            code,
            re.I,
        ))
        if not declarations:
            return lines

        # Position map is based on the original physical lines so edits can be
        # applied without reformatting or changing source sequence fields.
        full_text = code
        has_transaction = bool(re.search(r"\bEXEC\s+SQL\s+(?:COMMIT|ROLLBACK)\b", code))
        for i, line in enumerate(lines):
            seq, indicator, body = self._split(line)
            match = re.search(
                r"\bDECLARE\s+([A-Z0-9-]+)\s+CURSOR\s+WITH\s+HOLD\s+FOR\b",
                body,
                re.I,
            )
            if not match:
                continue
            cursor = match.group(1).upper()
            keep_hold = False
            if has_transaction:
                opens = [m.start() for m in re.finditer(rf"\bOPEN\s+{re.escape(cursor)}\b", full_text)]
                closes = [m.start() for m in re.finditer(rf"\bCLOSE\s+{re.escape(cursor)}\b", full_text)]
                if not opens or not closes:
                    keep_hold = True  # incomplete evidence: fail safe
                else:
                    for open_pos in opens:
                        close_pos = next((pos for pos in closes if pos > open_pos), None)
                        if close_pos is None:
                            keep_hold = True
                            break
                        lifecycle = full_text[open_pos:close_pos]
                        if re.search(r"\bEXEC\s+SQL\s+(?:COMMIT|ROLLBACK)\b", lifecycle):
                            keep_hold = True
                            break
            if not keep_hold:
                body = re.sub(r"\s+WITH\s+HOLD(?=\s+FOR\b)", "", body, flags=re.I)
                lines[i] = self._build(seq, indicator, body, line[72:] if len(line) > 72 else "")
        return lines


__all__ = ["ManualStorageParityComposer"]
