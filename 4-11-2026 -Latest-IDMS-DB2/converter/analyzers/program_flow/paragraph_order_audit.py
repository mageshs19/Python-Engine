"""Compare original and converted COBOL paragraph order without rewriting either file."""
from __future__ import annotations

from dataclasses import dataclass, field
import re
from pathlib import Path

from converter.analyzers.program_flow.procedure_control_flow_graph import (
    ProcedureControlFlowGraphBuilder,
)


@dataclass(frozen=True)
class ParagraphOrderAudit:
    original_count: int
    converted_count: int
    shared_in_original_order: tuple[str, ...]
    missing_from_converted: tuple[str, ...] = ()
    reordered_shared: tuple[str, ...] = ()
    diagnostics: tuple[str, ...] = ()

    @property
    def order_preserved(self) -> bool:
        return not self.reordered_shared


@dataclass
class ParagraphOrderAuditor:
    """Audits source-order retention; it never mutates or renumbers source."""
    graph_builder: ProcedureControlFlowGraphBuilder = field(
        default_factory=ProcedureControlFlowGraphBuilder
    )

    def audit(self, original: str | Path, converted: str | Path) -> ParagraphOrderAudit:
        original_graph = self.graph_builder.build(original)
        converted_graph = self.graph_builder.build(converted)
        original_names = original_graph.paragraph_names
        converted_names = converted_graph.paragraph_names

        # IDMS-ABORT is a runtime hook removed by the IDMS-to-DB2 conversion.
        # Treat its removal as intentional only when the source paragraph has
        # no business body (blank/comment lines and EXIT/CONTINUE/period only).
        # A non-trivial IDMS-ABORT body remains visible to the parity audit.
        original_text = (
            original.read_text(encoding="utf-8", errors="replace")
            if isinstance(original, Path) else str(original or "")
        )
        original_lines = original_text.splitlines()
        abort_nodes = [
            node for node in original_graph.nodes
            if node.kind == "PARAGRAPH" and node.name.upper() == "IDMS-ABORT"
        ]
        removable_abort_lines = {
            line_no
            for node in abort_nodes
            if all(
                not (body := re.sub(r"\*>.*$", "", line[7:72] if len(line) >= 7 and line[:6].isdigit() else line).strip())
                or re.fullmatch(r"(?:EXIT|CONTINUE)\s*\.?", body, re.I)
                for line_no, line in enumerate(original_lines[node.start_line:node.end_line], node.start_line + 1)
            )
            for line_no in range(node.start_line, node.end_line + 1)
        }
        if removable_abort_lines:
            original_names = [
                node.name for node in original_graph.nodes
                if node.kind == "PARAGRAPH"
                and not (node.name.upper() == "IDMS-ABORT" and node.start_line in removable_abort_lines)
            ]
        converted_set = set(converted_names)
        original_set = set(original_names)
        shared_original = tuple(name for name in original_names if name in converted_set)
        shared_converted = tuple(name for name in converted_names if name in original_set)
        missing = tuple(name for name in original_names if name not in converted_set)
        diagnostics: list[str] = []
        if missing:
            diagnostics.append(
                "original paragraphs absent from converted source; review whether removal was intentional: "
                + ", ".join(missing)
            )
        reordered: tuple[str, ...] = ()
        if shared_original != shared_converted:
            reordered = tuple(
                f"{index + 1}:{left}->{right}"
                for index, (left, right) in enumerate(zip(shared_original, shared_converted))
                if left != right
            )
            diagnostics.append(
                "shared original business paragraphs changed physical order; preserve original IDMS order: "
                + ", ".join(reordered)
            )
        return ParagraphOrderAudit(
            original_count=len(original_names),
            converted_count=len(converted_names),
            shared_in_original_order=shared_original,
            missing_from_converted=missing,
            reordered_shared=reordered,
            diagnostics=tuple(diagnostics),
        )
