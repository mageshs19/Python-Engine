"""Conservative cursor lifecycle/control-flow analysis for COBOL source.

This is an analysis-only layer: it never rewrites code. It combines cursor SQL
locations with the existing paragraph/PERFORM graph and flags relationships that
cannot be proved from the source rather than guessing from names or counts.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from converter.analyzers.program_flow.procedure_control_flow_graph import (
    ProcedureControlFlowGraph,
    ProcedureControlFlowGraphBuilder,
    _source_body,
)

_CURSOR_DECL = re.compile(r"\bDECLARE\s+(?P<name>[A-Z0-9][A-Z0-9-]*)\s+CURSOR\b", re.I)
_CURSOR_OP = re.compile(r"\b(?P<op>OPEN|FETCH|CLOSE)\s+(?P<name>[A-Z0-9][A-Z0-9-]*)\b", re.I)
_BRANCH = re.compile(r"\b(IF|ELSE|EVALUATE|WHEN|GO\s+TO|GOTO)\b", re.I)
_LOOP = re.compile(r"\b(PERFORM\s+(?:UNTIL|VARYING)|END-PERFORM|PERFORM\s+\d+\s+TIMES)\b", re.I)
_SQL_BEGIN = re.compile(r"\bEXEC\s+SQL\b", re.I)
_SQL_END = re.compile(r"\bEND-EXEC\b", re.I)


@dataclass(frozen=True)
class CursorOperationLocation:
    cursor: str
    operation: str
    line: int
    paragraph: str


@dataclass
class CursorControlFlowReport:
    declared_cursors: list[str] = field(default_factory=list)
    operations: list[CursorOperationLocation] = field(default_factory=list)
    relationships: dict[str, str] = field(default_factory=dict)
    diagnostics: list[str] = field(default_factory=list)
    graph: ProcedureControlFlowGraph | None = None

    def operations_for(self, cursor: str, operation: str | None = None) -> list[CursorOperationLocation]:
        name = cursor.upper()
        op = operation.upper() if operation else None
        return [item for item in self.operations if item.cursor == name and (op is None or item.operation == op)]


class CursorControlFlowAnalyzer:
    """Index cursor operations and conservatively characterize their context."""

    def __init__(self, graph_builder: ProcedureControlFlowGraphBuilder | None = None) -> None:
        self.graph_builder = graph_builder or ProcedureControlFlowGraphBuilder()

    def analyze(self, source: str | Path) -> CursorControlFlowReport:
        text = source.read_text(encoding="utf-8", errors="replace") if isinstance(source, Path) else str(source or "")
        graph = self.graph_builder.build(text)
        lines = text.splitlines()
        node_by_line = {
            line: node.name
            for node in graph.nodes if node.kind == "PARAGRAPH"
            for line in range(node.start_line, node.end_line + 1)
        }
        declared: set[str] = set()
        operations: list[CursorOperationLocation] = []
        diagnostics = list(graph.diagnostics)
        sql_buffer: list[tuple[int, str, str]] = []
        in_sql = False

        for line_no, raw in enumerate(lines, 1):
            body, comment = _source_body(raw)
            if comment:
                continue
            paragraph = node_by_line.get(line_no, "<MAINLINE>")
            if not in_sql and _SQL_BEGIN.search(body):
                in_sql = True
                sql_buffer = [(line_no, body, paragraph)]
                if _SQL_END.search(body):
                    in_sql = False
                    self._collect_sql(sql_buffer, declared, operations)
                    sql_buffer = []
                continue
            if in_sql:
                sql_buffer.append((line_no, body, paragraph))
                if _SQL_END.search(body):
                    in_sql = False
                    self._collect_sql(sql_buffer, declared, operations)
                    sql_buffer = []
                continue
            # Do not scan ordinary COBOL verbs here: OPEN INPUT/OUTPUT and
            # CLOSE file-name are file operations, not DB2 cursor lifecycle.
            # Cursor verbs are collected only inside EXEC SQL blocks.

        if in_sql:
            diagnostics.append(f"line {sql_buffer[0][0]}: EXEC SQL block has no END-EXEC; cursor operation scan may be incomplete")

        report = CursorControlFlowReport(
            declared_cursors=sorted(declared),
            operations=operations,
            diagnostics=diagnostics,
            graph=graph,
        )
        self._validate_lifecycle(report)
        report.relationships = self._characterize_relationships(lines, node_by_line, graph, report)
        return report

    def _collect_sql(self, buffer, declared, operations) -> None:
        statement = " ".join(body for _, body, _ in buffer)
        start_line = buffer[0][0]
        paragraph = buffer[0][2]
        for match in _CURSOR_DECL.finditer(statement):
            declared.add(match.group("name").upper())
        # SQL includes / comments are not operation verbs; SQL statement boundaries
        # ensure we do not mistake host names or comments for cursor actions.
        for match in _CURSOR_OP.finditer(statement):
            operations.append(CursorOperationLocation(
                match.group("name").upper(), match.group("op").upper(), start_line, paragraph
            ))

    def _collect_operations(self, body, line_no, paragraph, declared, operations) -> None:
        for match in _CURSOR_DECL.finditer(body):
            declared.add(match.group("name").upper())
        for match in _CURSOR_OP.finditer(body):
            operations.append(CursorOperationLocation(
                match.group("name").upper(), match.group("op").upper(), line_no, paragraph
            ))

    def _validate_lifecycle(self, report: CursorControlFlowReport) -> None:
        if not report.declared_cursors:
            report.diagnostics.append("No cursor declarations found; cursor lifecycle checks not applicable.")
            return
        for name in report.declared_cursors:
            ops = [item.operation for item in report.operations if item.cursor == name]
            for op in ("OPEN", "FETCH", "CLOSE"):
                count = ops.count(op)
                if count == 0:
                    report.diagnostics.append(f"cursor {name}: no {op} operation found")
            if ops.count("FETCH") > 1:
                # Multiple static FETCH sites can be legitimate (branches/loops).
                report.diagnostics.append(f"cursor {name}: {ops.count('FETCH')} FETCH sites found; validate branch and loop coverage")
        for item in report.operations:
            if item.cursor not in report.declared_cursors:
                report.diagnostics.append(
                    f"line {item.line}: {item.operation} references undeclared cursor {item.cursor}"
                )

    def _characterize_relationships(self, lines, node_by_line, graph, report) -> dict[str, str]:
        if not report.declared_cursors:
            return {}
        by_cursor = {
            name: [item for item in report.operations if item.cursor == name]
            for name in report.declared_cursors
        }
        out: dict[str, str] = {}
        adjacency: dict[str, set[str]] = {}
        for edge in graph.edges:
            if edge.resolution != "local":
                continue
            adjacency.setdefault(edge.source, set()).update(edge.covered_nodes or (edge.target,))

        def reachable(source: str) -> set[str]:
            visited: set[str] = set()
            pending = list(adjacency.get(source, set()))
            while pending:
                target = pending.pop()
                if target in visited:
                    continue
                visited.add(target)
                pending.extend(adjacency.get(target, set()) - visited)
            return visited

        # Infer parent-child only when a FETCH paragraph has a successful-row
        # branch and its resolved PERFORM graph reaches another cursor's OPEN
        # paragraph. This is structural evidence, not a name/declaration-order
        # heuristic. Other relationships remain explicitly uncertain.
        parents: dict[str, set[str]] = {}
        children: dict[str, set[str]] = {}
        open_paragraphs = {
            name: {item.paragraph for item in sites if item.operation == "OPEN"}
            for name, sites in by_cursor.items()
        }
        for parent_name, sites in by_cursor.items():
            for fetch_site in (site for site in sites if site.operation == "FETCH"):
                if fetch_site.paragraph == "<MAINLINE>":
                    continue
                node = next(
                    (n for n in graph.nodes if n.kind == "PARAGRAPH" and n.name == fetch_site.paragraph),
                    None,
                )
                if node is None:
                    continue
                paragraph_lines = lines[node.start_line - 1:node.end_line]
                body = "\n".join(paragraph_lines).upper()
                # A WHEN ZERO anywhere in the paragraph is not sufficient:
                # the child OPEN could be under WHEN OTHER or outside the
                # EVALUATE. Restrict evidence to PERFORM targets inside the
                # successful-row branch, stopping at the next WHEN/END-EVALUATE.
                successful_branch_lines: list[str] = []
                in_success_branch = False
                saw_success_branch = False
                for raw_line in paragraph_lines:
                    source_line = _source_body(raw_line)[0].upper().strip()
                    if re.search(r"\bWHEN\s+(?:ZERO|0)\b", source_line):
                        in_success_branch = True
                        saw_success_branch = True
                        continue
                    if in_success_branch and re.search(
                        r"\b(?:WHEN\b|END-EVALUATE\b)", source_line
                    ):
                        in_success_branch = False
                    if in_success_branch:
                        successful_branch_lines.append(source_line)
                if not saw_success_branch:
                    continue

                performed_targets: set[str] = set()
                for branch_line in successful_branch_lines:
                    performed_targets.update(
                        match.group(1).upper()
                        for match in re.finditer(
                            r"\bPERFORM\s+([A-Z0-9][A-Z0-9-]*)",
                            branch_line,
                        )
                    )
                reached_from_success_branch: set[str] = set()
                for target in performed_targets:
                    # PERFORM targets may be a paragraph that then reaches
                    # the child OPEN paragraph. Use the graph only from those
                    # targets proven to occur in WHEN ZERO, not from every
                    # edge in the FETCH paragraph.
                    reached_from_success_branch.add(target)
                    reached_from_success_branch.update(reachable(target))
                for child_name, child_open_nodes in open_paragraphs.items():
                    if child_name == parent_name:
                        continue
                    if reached_from_success_branch.intersection(child_open_nodes):
                        parents.setdefault(parent_name, set()).add(child_name)
                        children.setdefault(child_name, set()).add(parent_name)

        for name, sites in by_cursor.items():
            loop_lines = []
            branch_lines = []
            for site in sites:
                start = max(0, site.line - 3)
                end = min(len(lines), site.line + 2)
                window = "\\n".join(lines[start:end])
                if _LOOP.search(window):
                    loop_lines.append(site.line)
                if _BRANCH.search(window):
                    branch_lines.append(site.line)
            if name in parents:
                out[name] = (
                    "parent cursor; child cursor(s) reached from successful FETCH branch: "
                    + ", ".join(sorted(parents[name]))
                )
            elif name in children:
                out[name] = (
                    "child cursor; parent cursor(s) proven by successful-FETCH control flow: "
                    + ", ".join(sorted(children[name]))
                )
            elif loop_lines:
                out[name] = "loop-context detected; confirm loop boundaries and repeated OPEN/CLOSE semantics"
            elif branch_lines:
                out[name] = "conditional/branch context detected; verify all execution paths"
            elif len(by_cursor) == 1:
                out[name] = "single cursor; no cross-cursor relationship to infer"
            else:
                out[name] = "multiple cursors present; dependency relationship not proven by local evidence"

        if not parents:
            report.diagnostics.append(
                "Cursor relationships are conservative: no parent-child relationship is inferred from cursor names or declaration order."
            )
        return out
