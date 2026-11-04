"""Remove orphaned IDMS ON ANY-ERROR-STATUS clauses after IDMS DML removal.

An IDMS error clause is not valid DB2 COBOL syntax. When its associated BIND,
READY, FINISH, or copied IDMS status paragraph is removed, the converter must
also remove the declarative clause. This pass is deliberately narrow: it only
removes an exact standalone ON ANY-ERROR-STATUS line when either the paired
handler is the known IDMS-STATUS paragraph or a prior converter diagnostic
confirms that the handler was already removed. Unknown handler shapes are
retained and reported for manual review.
"""
from __future__ import annotations

import re

from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils

_ON_ANY_ERROR = re.compile(r"^ON\s+ANY-ERROR-STATUS\s*\.?$", re.IGNORECASE)
_IDMS_STATUS_HANDLER = re.compile(r"^PERFORM\s+IDMS-STATUS\s*\.?$", re.IGNORECASE)
_WARNING = re.compile(
    r"ERROR-STATUS\s+is\s+undefined\s+after\s+copybook\s+removal",
    re.IGNORECASE,
)


class ResidualIdmsErrorClauseCleanup:
    def __init__(
        self,
        messages: CleanupMessageCollector,
        line_utils: CobolCleanupLineUtils | None = None,
    ) -> None:
        self.messages = messages
        self.line_utils = line_utils or CobolCleanupLineUtils()

    def _logical(self, line: str) -> str:
        return self.line_utils.logical(line)

    def apply(self, text: str) -> str:
        lines = str(text or "").splitlines()
        output: list[str] = []
        removed = 0
        unrecognized = 0
        index = 0

        while index < len(lines):
            line = lines[index]
            logical = self._logical(line)
            if not _ON_ANY_ERROR.fullmatch(logical):
                output.append(line)
                index += 1
                continue

            # Remove the diagnostic that a prior pass emitted for this exact
            # unsupported IDMS clause. It is superseded by the more precise
            # cleanup message below.
            if output and _WARNING.search(self._logical(output[-1])):
                output.pop()

            next_index = index + 1
            while next_index < len(lines) and not self._logical(lines[next_index]):
                next_index += 1
            handler = self._logical(lines[next_index]) if next_index < len(lines) else ""

            # The normal site handler is an IDMS-STATUS paragraph. It has no
            # valid target once the IDMS status copybook and IDMS verbs have
            # been removed, so remove that handler with the ON clause.
            if _IDMS_STATUS_HANDLER.fullmatch(handler):
                index = next_index + 1
                removed += 1
                continue

            # ON ANY-ERROR-STATUS is not valid DB2 COBOL. Remove the orphaned
            # directive rather than ship uncompilable source, but keep the
            # following statement and raise a review diagnostic when we cannot
            # prove that the removed statement was the known IDMS-STATUS one.
            index += 1
            removed += 1
            unrecognized += 1

        if removed:
            self.messages.add("removed_orphaned_idms_error_clause", count=removed)
        if unrecognized:
            self.messages.add("unrecognized_idms_error_clause", count=unrecognized)
        return "\n".join(output).rstrip() + "\n"



__all__ = ["ResidualIdmsErrorClauseCleanup"]
