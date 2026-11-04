"""Remove status guards whose IDMS BIND/READY operation no longer exists.

This pass is intentionally narrow. It removes an IF ERROR-STATUS failure
branch only when the branch's executable body contains both a DISPLAY label
identifying BIND/READY and CALL USERABEN. It never rewrites a status check
that could belong to a live DB2 statement or ordinary business operation.
"""
from __future__ import annotations

import re

from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils

_GUARD = re.compile(r"^IF\s+ERROR-STATUS\s+NOT\s*=\s*(['\"])0000\1\s*\.?$", re.I)
_END_IF = re.compile(r"^END-IF\s*\.?$", re.I)
_CALL_USERABEN = re.compile(r"\bCALL\s+USERABEN\b", re.I)
_DISPLAY_SETUP = re.compile(r"\bDISPLAY\s+(['\"])(?:BIND|READY)\b", re.I)


class OrphanedIdmsStatusGuardCleanup:
    def __init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None = None) -> None:
        self.messages = messages
        self.line_utils = line_utils or CobolCleanupLineUtils()

    def apply(self, text: str) -> str:
        lines = str(text or "").splitlines()
        out: list[str] = []
        removed = 0
        i = 0
        while i < len(lines):
            logical = self.line_utils.logical(lines[i])
            if not _GUARD.fullmatch(logical):
                out.append(lines[i])
                i += 1
                continue
            end = i + 1
            while end < len(lines) and not _END_IF.fullmatch(self.line_utils.logical(lines[end])):
                end += 1
            if end >= len(lines):
                out.append(lines[i])
                i += 1
                continue
            block = "\n".join(self.line_utils.logical(line) for line in lines[i + 1:end])
            # No ELSE or nested conditional is accepted: only a simple, stale
            # IDMS setup-error branch can be removed by this pass.
            safe_shape = not re.search(r"\b(?:ELSE|IF)\b", block, re.I)
            if safe_shape and _CALL_USERABEN.search(block) and _DISPLAY_SETUP.search(block):
                while out and self._is_obsolete_warning(out[-1]):
                    out[-1] = self._blank_comment(out[-1])
                ref = lines[i]
                note = "DB2 NOTE: obsolete IDMS BIND/READY status guard removed."
                if len(ref) >= 80 and ref[:6].isdigit():
                    out.append(f"{ref[:6]}*{note[:65].ljust(65)}{ref[72:80]}")
                else:
                    out.append(f"*> {note}")
                removed += 1
                i = end + 1
                continue
            out.append(lines[i])
            i += 1
        if removed:
            self.messages.add("removed_orphaned_idms_setup_status_guards", count=removed)
        return "\n".join(out).rstrip() + "\n"

    def _is_obsolete_warning(self, line: str) -> bool:
        logical = self.line_utils.logical(line).upper()
        return "ERROR-STATUS IS UNDEFINED AFTER COPYBOOK REMOVAL" in logical or "SHARES A LINE WITH LIVE OPERANDS" in logical

    @staticmethod
    def _blank_comment(line: str) -> str:
        value = str(line or "")
        if len(value) >= 80 and value[:6].isdigit():
            return f"{value[:6]}*{' ' * 65}{value[72:80]}"
        return "*>"
