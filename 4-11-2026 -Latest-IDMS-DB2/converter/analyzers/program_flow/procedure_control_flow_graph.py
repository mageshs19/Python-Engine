"""Read-only, generic COBOL PROCEDURE DIVISION control-flow index.

The index deliberately does not rewrite paragraph names. It resolves local
PERFORM edges and physical THRU ranges, and labels external/ambiguous targets
for review when copybooks or dialect rules prevent a safe local resolution.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from rules.cursor_close_guarantee_rules import NON_PARAGRAPH_SINGLE_WORDS


@dataclass(frozen=True)
class ProcedureNode:
    name: str
    kind: str  # SECTION or PARAGRAPH
    start_line: int
    end_line: int


@dataclass(frozen=True)
class PerformEdge:
    source: str
    line: int
    target: str
    through: str = ""
    inline: bool = False
    resolution: str = "local"  # local, missing, ambiguous, external-or-copybook
    covered_nodes: tuple[str, ...] = ()


@dataclass
class ProcedureControlFlowGraph:
    nodes: list[ProcedureNode] = field(default_factory=list)
    edges: list[PerformEdge] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)

    @property
    def paragraph_names(self) -> list[str]:
        return [n.name for n in self.nodes if n.kind == "PARAGRAPH"]


def _source_body(line: str) -> tuple[str, bool]:
    """Return fixed-format source area and comment status, preserving lines."""
    if len(line) >= 7 and line[:6].isdigit():
        indicator, body = line[6:7], line[7:72]
    else:
        indicator, body = " ", line
    is_comment = indicator in {"*", "/", "D", "d"}
    if is_comment:
        return "", True
    # Mask quoted strings and inline comments so text cannot become syntax.
    chars = list(body)
    quote = None
    i = 0
    while i < len(chars):
        c = chars[i]
        if quote:
            chars[i] = " "
            if c == quote:
                if i + 1 < len(chars) and chars[i + 1] == quote:
                    chars[i + 1] = " "
                    i += 2
                    continue
                quote = None
            i += 1
            continue
        if c in "'\"":
            quote = c
            chars[i] = " "
        elif c == "*" and i + 1 < len(chars) and chars[i + 1] == ">":
            chars[i:] = [" "] * (len(chars) - i)
            break
        i += 1
    return "".join(chars).strip(), False


class ProcedureControlFlowGraphBuilder:
    """Build a paragraph/section graph, optionally expanding procedure COPYbooks.

    Expansion is analysis-only: original files are never rewritten. Only plain
    ``COPY member.`` statements in PROCEDURE DIVISION are expanded. IDMS
    schema/subschema COPY directives and COPY ... REPLACING are deliberately
    left intact because their semantics require dialect-specific handling.
    """

    def __init__(self, copybook_dirs: tuple[str | Path, ...] = ()) -> None:
        self.copybook_dirs = tuple(Path(item) for item in copybook_dirs)
        self._expansion_diagnostics: list[str] = []

    @staticmethod
    def _copy_directive(line: str) -> tuple[str | None, bool]:
        body, comment = _source_body(line)
        if comment:
            return None, False
        # IDMS COPY forms carry schema/subschema qualifiers and are not COBOL
        # procedure copybooks for this local graph.
        match = re.fullmatch(r"COPY\s+([A-Z0-9][A-Z0-9-]*)\s*\.", body, re.I)
        if match:
            return match.group(1).upper(), False
        if re.match(r"COPY\s+(?!IDMS\b)[A-Z0-9][A-Z0-9-]*\b", body, re.I):
            return None, True
        return None, False

    def _find_copybook(self, member: str, source_path: Path | None) -> Path | None:
        roots: list[Path] = []
        if source_path is not None:
            roots.extend([source_path.parent, source_path.parent / "Copybook"])
            for parent in source_path.parents:
                roots.extend([parent / "Copybook", parent / "workspace" / "Copybook"])
        roots.extend(self.copybook_dirs)
        seen: set[Path] = set()
        for root in roots:
            try:
                resolved = root.resolve()
            except OSError:
                continue
            if resolved in seen or not resolved.is_dir():
                continue
            seen.add(resolved)
            for candidate in root.iterdir():
                if candidate.is_file() and candidate.stem.upper() == member and candidate.suffix.lower() in {".cpy", ".cob", ".cbl", ".txt"}:
                    return candidate
        return None

    def _expand_procedure_copybooks(
        self, text: str, source_path: Path | None, stack: tuple[str, ...] = ()
    ) -> str:
        lines = text.splitlines()
        output: list[str] = []
        # A copied member is being inserted at the caller's current location;
        # its paragraph text is therefore already in PROCEDURE DIVISION scope.
        in_procedure = bool(stack)
        for line_no, line in enumerate(lines, 1):
            body, _ = _source_body(line)
            if re.match(r"^PROCEDURE\s+DIVISION\b", body, re.I):
                in_procedure = True
            if not in_procedure:
                output.append(line)
                continue
            member, unsupported = self._copy_directive(line)
            if unsupported:
                self._expansion_diagnostics.append(
                    f"{source_path or '<memory>'}:{line_no}: procedure COPY with REPLACING or unsupported syntax was not expanded"
                )
                output.append(line)
                continue
            if not member:
                output.append(line)
                continue
            if member in stack:
                self._expansion_diagnostics.append(
                    f"{source_path or '<memory>'}:{line_no}: recursive procedure COPY cycle: {' -> '.join((*stack, member))}"
                )
                output.append(line)
                continue
            copy_path = self._find_copybook(member, source_path)
            if copy_path is None:
                self._expansion_diagnostics.append(
                    f"{source_path or '<memory>'}:{line_no}: procedure COPY member {member} not found in configured search paths"
                )
                output.append(line)
                continue
            copy_text = copy_path.read_text(encoding="utf-8", errors="replace")
            output.append(self._expand_procedure_copybooks(copy_text, copy_path, (*stack, member)))
        return "\n".join(output)

    _header = re.compile(r"^(?P<name>[A-Z0-9][A-Z0-9-]*)\.(?:\s*)$", re.I)
    _section = re.compile(r"^(?P<name>[A-Z0-9][A-Z0-9-]*)\s+SECTION\.$", re.I)
    _perform = re.compile(
        r"(?<!END-)\bPERFORM\s+(?P<target>[A-Z0-9][A-Z0-9-]*)"
        r"(?:\s+(?:THRU|THROUGH)\s+(?P<through>[A-Z0-9][A-Z0-9-]*))?\b",
        re.I,
    )
    _inline = re.compile(r"\bPERFORM\s+(?:UNTIL|VARYING)\b", re.I)

    def build(self, source: str | Path) -> ProcedureControlFlowGraph:
        self._expansion_diagnostics = []
        source_path = source if isinstance(source, Path) else None
        if source_path is not None:
            text = source_path.read_text(encoding="utf-8", errors="replace")
        else:
            text = str(source or "")
        text = self._expand_procedure_copybooks(text, source_path)
        lines = text.splitlines()
        bodies: list[str] = []
        header_allowed: list[bool] = []
        in_procedure = False
        for raw in lines:
            body, comment = _source_body(raw)
            if comment:
                bodies.append("")
                header_allowed.append(False)
                continue
            # In fixed format, paragraph/section names must start in Area A
            # (first four source columns after the indicator). Preserve this
            # distinction so a continuation operand such as `LAST-PARA.` in
            # Area B is not mistaken for a duplicate paragraph declaration.
            if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace()):
                source_area = raw[7:72]
            else:
                source_area = raw
            allowed = len(source_area) - len(source_area.lstrip()) <= 3
            if re.match(r"^PROCEDURE\s+DIVISION\b", body, re.I):
                in_procedure = True
            bodies.append(body if in_procedure else "")
            header_allowed.append(allowed)

        raw_nodes: list[tuple[str, str, int]] = []
        for idx, body in enumerate(bodies, 1):
            if not body or not header_allowed[idx - 1]:
                continue
            section = self._section.fullmatch(body)
            if section:
                raw_nodes.append((section.group("name").upper(), "SECTION", idx))
                continue
            header = self._header.fullmatch(body)
            if header:
                name = header.group("name").upper()
                if name not in NON_PARAGRAPH_SINGLE_WORDS:
                    raw_nodes.append((name, "PARAGRAPH", idx))

        nodes: list[ProcedureNode] = []
        section_positions = [i for i, item in enumerate(raw_nodes) if item[1] == "SECTION"]
        for i, (name, kind, start) in enumerate(raw_nodes):
            if kind == "SECTION":
                next_section = next((raw_nodes[pos][2] for pos in section_positions if pos > i), None)
                end_line = (next_section - 1) if next_section is not None else len(lines)
            else:
                end_line = (raw_nodes[i + 1][2] - 1) if i + 1 < len(raw_nodes) else len(lines)
            nodes.append(ProcedureNode(name, kind, start, end_line))
        paragraph_nodes = [n for n in nodes if n.kind == "PARAGRAPH"]
        by_name: dict[str, list[ProcedureNode]] = {}
        for node in nodes:
            by_name.setdefault(node.name, []).append(node)

        edges: list[PerformEdge] = []
        diagnostics: list[str] = list(self._expansion_diagnostics)
        # Join executable bodies so multiline PERFORM ... THRU statements are
        # resolved with the same logic as single-line statements. Keep an
        # offset-to-source-line map for actionable diagnostics.
        joined_parts: list[str] = []
        offset_lines: list[int] = []
        for line_no, body in enumerate(bodies, 1):
            if not body:
                continue
            if joined_parts:
                joined_parts.append(" ")
                offset_lines.append(line_no)
            joined_parts.append(body)
            offset_lines.extend([line_no] * len(body))
        joined = "".join(joined_parts)
        for match in self._perform.finditer(joined):
            # Exclude inline PERFORM UNTIL/VARYING/TIMES control phrases. A
            # paragraph call can still occur later in the same source line.
            prefix = joined[max(0, match.start() - 32):match.start()]
            target = match.group("target").upper()
            if target in {"UNTIL", "VARYING", "TIMES"}:
                continue
            # `PERFORM item OF table TIMES` is a table/inline loop, not a
            # paragraph call. Bound the lookahead to this statement so a
            # later unrelated TIMES loop cannot hide a real PERFORM target.
            statement_tail = joined[match.end():]
            boundary = re.search(r"\.|\bEND-PERFORM\b|(?<!END-)\bPERFORM\b", statement_tail, re.I)
            if boundary:
                statement_tail = statement_tail[:boundary.start()]
            if re.search(r"\bTIMES\b", statement_tail, re.I):
                continue
            line_no = offset_lines[match.start()] if match.start() < len(offset_lines) else 1
            through = (match.group("through") or "").upper()
            targets = by_name.get(target, [])
            ends = by_name.get(through, []) if through else []
            if not targets:
                # SQLERROR is deliberately supplied by `EXEC SQL INCLUDE
                # SQLERROR`; it is not expected to have a local COBOL header.
                if target == "SQLERROR":
                    edges.append(PerformEdge("<MAINLINE>", line_no, target, through, False, "external-or-copybook"))
                else:
                    edges.append(PerformEdge("<MAINLINE>", line_no, target, through, False, "external-or-copybook"))
                    diagnostics.append(f"line {line_no}: PERFORM target {target} not resolved locally; check procedure COPYbooks/expanded source")
                continue
            if len(targets) > 1:
                edges.append(PerformEdge("<MAINLINE>", line_no, target, through, False, "ambiguous"))
                diagnostics.append(f"line {line_no}: PERFORM target {target} has {len(targets)} local definitions")
                continue
            if through:
                if not ends:
                    edges.append(PerformEdge("<MAINLINE>", line_no, target, through, False, "missing"))
                    diagnostics.append(f"line {line_no}: THRU endpoint {through} not resolved locally")
                    continue
                if len(ends) > 1:
                    edges.append(PerformEdge("<MAINLINE>", line_no, target, through, False, "ambiguous"))
                    diagnostics.append(f"line {line_no}: THRU endpoint {through} has {len(ends)} local definitions")
                    continue
                if ends[0].start_line < targets[0].start_line:
                    edges.append(PerformEdge("<MAINLINE>", line_no, target, through, False, "missing"))
                    diagnostics.append(f"line {line_no}: reversed PERFORM THRU range {target} -> {through}")
                    continue
                covered = tuple(n.name for n in paragraph_nodes
                                if targets[0].start_line <= n.start_line <= ends[0].start_line)
            elif targets[0].kind == "SECTION":
                covered = tuple(
                    n.name for n in paragraph_nodes
                    if targets[0].start_line <= n.start_line <= targets[0].end_line
                )
            else:
                covered = (target,)
            edges.append(PerformEdge("<MAINLINE>", line_no, target, through, False, "local", covered))

        # A local label can be referenced from any paragraph; derive source
        # ownership from physical spans rather than assigning every edge to mainline.
        fixed_edges: list[PerformEdge] = []
        for edge in edges:
            owner = next((n.name for n in paragraph_nodes if n.start_line <= edge.line <= n.end_line), "<MAINLINE>")
            fixed_edges.append(PerformEdge(owner, edge.line, edge.target, edge.through,
                                           edge.inline, edge.resolution, edge.covered_nodes))

        duplicates = {name: defs for name, defs in by_name.items() if len(defs) > 1}
        for name, defs in sorted(duplicates.items()):
            kind = "section/paragraph label"
            diagnostics.append(f"duplicate {kind} {name}: lines {', '.join(str(n.start_line) for n in defs)}")

        return ProcedureControlFlowGraph(nodes, fixed_edges, diagnostics)
