"""Generic discovery of COBOL business-control flags.

The analyzer deliberately does not attach meaning to a flag's identifier.
It gathers evidence from assignments, trigger conditions, control-flow reads,
paragraph scope, and cursor relationships. Callers must still prove the
required loop/output relationship before transforming the source.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re

from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.composers.cleanup.cursor_nesting_analyser import CursorNestingAnalyser


_Y_ASSIGNMENT = re.compile(
    r"^MOVE\s+(['\"])(?P<value>[^'\"]+)\1\s+TO\s+(?P<flag>[A-Z][A-Z0-9-]*)\b",
    re.IGNORECASE,
)
_SET_TRUE = re.compile(
    r"^SET\s+(?P<flag>[A-Z][A-Z0-9-]*)\s+TO\s+TRUE\b",
    re.IGNORECASE,
)
_FLAG_DECLARATION = re.compile(
    r"^\s*(?:\d{1,2}\s+)?(?P<flag>[A-Z][A-Z0-9-]*)\s+.*\bPIC\b",
    re.IGNORECASE,
)
_IF_START = re.compile(r"^IF\s+(?P<condition>.+)$", re.IGNORECASE)
_CONDITION_READ = re.compile(
    r"\b(?:IF|UNTIL|WHEN|EVALUATE)\b[^.]*\b(?P<flag>[A-Z][A-Z0-9-]*)\b",
    re.IGNORECASE,
)


@dataclass
class BusinessFlagEvidence:
    name: str
    declared: bool = False
    assignments: list[dict[str, object]] = field(default_factory=list)
    condition_reads: list[dict[str, object]] = field(default_factory=list)
    output_reads: list[dict[str, object]] = field(default_factory=list)

    @property
    def trigger_conditions(self) -> list[str]:
        values: list[str] = []
        for assignment in self.assignments:
            condition = str(assignment.get("condition") or "").strip()
            if condition and condition not in values:
                values.append(condition)
        return values


class BusinessControlFlagAnalyzer:
    """Extract evidence for flags without relying on their names."""

    def __init__(self, line_utils: CobolCleanupLineUtils | None = None) -> None:
        self.line_utils = line_utils or CobolCleanupLineUtils()
        self.cursor_nesting = CursorNestingAnalyser(self.line_utils)

    def analyze(self, text_or_lines: str | list[str]) -> dict[str, BusinessFlagEvidence]:
        lines = text_or_lines.splitlines() if isinstance(text_or_lines, str) else list(text_or_lines)
        spans = self.cursor_nesting.paragraph_spans(lines)
        evidence: dict[str, BusinessFlagEvidence] = {}
        declared: set[str] = set()
        for line in lines:
            logical = self.line_utils.logical(line).strip()
            match = _FLAG_DECLARATION.match(logical)
            if match:
                declared.add(match.group("flag").upper())

        current_paragraph = "<MAINLINE>"
        active_conditions: list[str] = []
        for index, line in enumerate(lines):
            logical = self.line_utils.logical(line).strip()
            if not logical or logical.startswith(("*", "/")):
                continue
            header = logical[:-1].upper() if logical.endswith(".") else ""
            if header in spans:
                current_paragraph = header
                active_conditions = []
                continue

            if_match = _IF_START.match(logical)
            if if_match:
                active_conditions.append(if_match.group("condition").rstrip("."))
            elif re.match(r"^END-IF\b", logical, re.IGNORECASE):
                if active_conditions:
                    active_conditions.pop()
            elif re.match(r"^ELSE\b", logical, re.IGNORECASE):
                if active_conditions:
                    active_conditions[-1] = "ELSE OF (" + active_conditions[-1] + ")"

            assignment = _Y_ASSIGNMENT.match(logical)
            set_true = _SET_TRUE.match(logical)
            name = None
            value = None
            if assignment and assignment.group("value").upper() == "Y":
                name, value = assignment.group("flag").upper(), "Y"
            elif set_true:
                name, value = set_true.group("flag").upper(), "TRUE"
            if name:
                item = evidence.setdefault(name, BusinessFlagEvidence(name=name))
                item.assignments.append({
                    "line": index + 1,
                    "paragraph": current_paragraph,
                    "value": value,
                    "condition": " AND ".join(active_conditions),
                    "statement": logical,
                })

        for name, item in evidence.items():
            item.declared = name in declared

        for index, line in enumerate(lines):
            logical = self.line_utils.logical(line).strip()
            if not logical:
                continue
            for name, item in evidence.items():
                if not re.search(rf"\b{re.escape(name)}\b", logical, re.IGNORECASE):
                    continue
                if re.match(r"^(?:IF|UNTIL|WHEN|EVALUATE)\b", logical, re.IGNORECASE):
                    item.condition_reads.append({"line": index + 1, "statement": logical})
                if re.match(r"^(?:IF|EVALUATE)\b", logical, re.IGNORECASE) and re.search(
                    r"\b(?:WRITE|REWRITE|DISPLAY|PERFORM)\b", logical, re.IGNORECASE
                ):
                    item.output_reads.append({"line": index + 1, "statement": logical})
        return evidence

    def discover_unique_yes_flag(
        self,
        lines: list[str],
        paragraphs: set[str] | list[str] | tuple[str, ...],
        *,
        cursor_name: str | None = None,
        require_control_read: bool = False,
    ) -> str | None:
        """Return one flag only when its assignment is scoped to the requested flow.

        `paragraphs` is the set of business paragraphs reachable in the flow.
        A cursor-specific proof additionally requires a FETCH of that cursor
        in the same flow. Ambiguous candidates intentionally return None.
        """
        evidence = self.analyze(lines)
        allowed = {str(p).upper() for p in paragraphs}
        candidates: list[str] = []
        for name, item in evidence.items():
            scoped_assignments = [
                assignment for assignment in item.assignments
                if str(assignment.get("paragraph", "")).upper() in allowed
            ]
            if not scoped_assignments:
                continue
            if cursor_name:
                suffix = f"-FETCH-{cursor_name}".upper()
                flow_has_fetch = any(
                    str(assignment.get("paragraph", "")).upper() in allowed
                    and suffix in self.line_utils.logical(lines[int(assignment["line"]) - 1]).upper()
                    for assignment in scoped_assignments
                )
                if not flow_has_fetch:
                    # The cursor FETCH may be in another paragraph in the same
                    # owner flow; inspect the allowed paragraph spans as a unit.
                    spans = self.cursor_nesting.paragraph_spans(lines)
                    flow_has_fetch = any(
                        any(
                            suffix in self.line_utils.logical(lines[i]).upper()
                            and re.match(r"^PERFORM\b", self.line_utils.logical(lines[i]).strip(), re.I)
                            for i in range(spans[p][0] + 1, spans[p][1] + 1)
                        )
                        for p in allowed if p in spans
                    )
                if not flow_has_fetch:
                    continue
            if require_control_read and not item.condition_reads:
                continue
            candidates.append(name)
        return candidates[0] if len(candidates) == 1 else None


__all__ = ["BusinessControlFlagAnalyzer", "BusinessFlagEvidence"]
