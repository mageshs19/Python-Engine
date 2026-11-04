"""Generic normalization of program-name constants in fixed-format COBOL.

Only a CS-* declaration whose VALUE exactly matches PROGRAM-ID is treated as
an alias. If CS-PROGRAM with the same value already exists, the redundant alias
is removed and references are redirected. Otherwise the proven declaration is
renamed in place. Unrelated CS fields are preserved.
"""
from __future__ import annotations

import re


class ProgramConstantNormalizer:
    @staticmethod
    def _split(line: str) -> tuple[str, str, str]:
        if len(line) >= 7 and line[:6].isdigit():
            return line[:6], line[6:7], line[7:72].rstrip()
        return "", " ", line.rstrip()

    @staticmethod
    def _build(seq: str, indicator: str, body: str, tail: str = "") -> str:
        if seq:
            return f"{seq}{indicator}{body:<65}{tail}"
        return body

    @classmethod
    def normalize(cls, text: str) -> str:
        source = str(text or "")
        if not source:
            return source
        lines = source.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        return "\n".join(cls._normalize_lines(lines)).rstrip() + "\n"

    @classmethod
    def _normalize_lines(cls, lines: list[str]) -> list[str]:
        bodies = [cls._split(line)[2] for line in lines]
        joined = "\n".join(bodies)
        program_match = re.search(r"\bPROGRAM-ID\.\s*([A-Z0-9-]+)\b", joined, re.I)
        if not program_match:
            return lines
        program_id = program_match.group(1).upper()
        declaration_pattern = re.compile(
            rf"^\s*(?P<level>\d{{2}})\s+(?P<name>CS-[A-Z0-9-]+)\b"
            rf"(?P<rest>[^\n]*?\bVALUE\s+['\"](?P<value>[A-Z0-9-]+)['\"][^\n]*)$",
            re.I,
        )
        candidates: list[tuple[int, str]] = []
        has_shared_constant = False
        for index, body in enumerate(bodies):
            match = declaration_pattern.match(body)
            if not match:
                continue
            name = match.group("name").upper()
            value = match.group("value").upper()
            if name == "CS-PROGRAM" and value == program_id:
                has_shared_constant = True
            elif name != "CS-PROGRAM" and value == program_id:
                candidates.append((index, name))

        if not candidates:
            return lines

        remove_indexes: set[int] = set()
        replacements: dict[str, str] = {}
        # Keep exactly one canonical declaration. Prefer an existing shared
        # declaration; otherwise rename the first proven alias and remove any
        # additional aliases that carry the same program-id VALUE.
        keep_index = None if has_shared_constant else candidates[0][0]
        for index, name in candidates:
            replacements[name] = "CS-PROGRAM"
            if has_shared_constant or index != keep_index:
                remove_indexes.add(index)
            else:
                seq, indicator, body = cls._split(lines[index])
                body = re.sub(rf"\b{re.escape(name)}\b", "CS-PROGRAM", body, flags=re.I)
                tail = lines[index][72:] if len(lines[index]) > 72 else ""
                lines[index] = cls._build(seq, indicator, body, tail)

        if replacements:
            for index, line in enumerate(lines):
                if index in remove_indexes:
                    continue
                for old_name in replacements:
                    line = re.sub(rf"\b{re.escape(old_name)}\b", "CS-PROGRAM", line, flags=re.I)
                lines[index] = line
        for index in sorted(remove_indexes, reverse=True):
            lines.pop(index)
        return lines


__all__ = ["ProgramConstantNormalizer"]
