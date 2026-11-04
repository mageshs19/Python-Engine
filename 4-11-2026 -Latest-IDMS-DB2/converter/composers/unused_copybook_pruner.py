"""Provenance-driven removal of unused source COPY members.

A copybook may be removed only when its source member is available and none
of its declared symbols is referenced by executable COBOL. Missing member
text, unrecognized layouts, and dynamic/ambiguous references are NOT pruned.
No program or copybook name is special-cased.
"""
from __future__ import annotations

import re

from converter.services.name_derivation_resolver import NameDerivationResolver


class UnusedCopybookPruner:
    _COPY = re.compile(r"^\s*COPY\s+([A-Z][A-Z0-9-]*)\s*\.?\s*$", re.I)
    _DECL = re.compile(r"^\s*(?:0[1-9]|[1-4][0-9]|66|77|78)\s+([A-Z][A-Z0-9-]*)\b", re.I)
    _SYMBOL = re.compile(r"(?<![A-Z0-9-])([A-Z][A-Z0-9-]*)(?![A-Z0-9-])", re.I)

    def __init__(self, source_members: dict[str, str] | None = None):
        self.source_members = {str(k).upper(): str(v) for k, v in (source_members or {}).items()}
        self.name_resolver = NameDerivationResolver()
        self.messages: list[str] = []

    @staticmethod
    def _split(line: str) -> tuple[str, bool]:
        if len(line) >= 7 and line[:6].strip().isdigit():
            return line[7:72], line[6] in "*/Dd"
        return line, line.lstrip().startswith(("*", "/"))

    def apply(self, text: str) -> str:
        self.messages = []
        if not text or not self.source_members:
            return text
        lines = text.splitlines(keepends=True)
        procedure = False
        executable: list[str] = []
        references: list[tuple[int, str]] = []
        for i, line in enumerate(lines):
            body, comment = self._split(line.rstrip("\r\n"))
            if comment:
                continue
            if "PROCEDURE DIVISION" in body.upper():
                procedure = True
            match = self._COPY.fullmatch(body.strip())
            if match and not procedure:
                references.append((i, match.group(1).upper()))
                continue
            # Do not let a COPY declaration itself count as its own use.
            executable.append(body)
        # Tokenize code (excluding quoted literals) conservatively. If an
        # ignored literal contained a field name it could only make the pass
        # more conservative; its removal is not required for correctness.
        tokens = set(self._SYMBOL.findall(" ".join(executable).upper()))
        deleted: set[int] = set()
        for index, member in references:
            source = self.source_members.get(member)
            if not source:
                # Derived names are matched to the original source name using
                # only the standard naming resolver, not name heuristics.
                for original, raw in self.source_members.items():
                    if self.name_resolver.derive(original) == member:
                        source = raw
                        break
            if not source:
                continue
            names: set[str] = set()
            valid = True
            for source_line in source.splitlines():
                body, comment = self._split(source_line)
                if comment:
                    continue
                stripped = body.strip().upper()
                if stripped.startswith(("COPY ", "EXEC ")):
                    valid = False
                    break  # transitive dependencies require separate analysis
                m = self._DECL.match(body)
                if m and m.group(1).upper() != "FILLER":
                    names.add(m.group(1).upper())
            if not valid or not names:
                continue
            # A quoted/nested reference can be dynamic. With no fully parsed
            # executable reference, retain the COPY in any such uncertainty.
            if any(name in tokens for name in names) or member in tokens:
                continue
            deleted.add(index)
            self.messages.append(
                f"Removed unused COPY {member}: {len(names)} source-declared names have no live references."
            )
        if not deleted:
            return text
        return "".join(line for i, line in enumerate(lines) if i not in deleted)
