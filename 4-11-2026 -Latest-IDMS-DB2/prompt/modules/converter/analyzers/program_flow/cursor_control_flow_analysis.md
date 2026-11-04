# `converter/analyzers/program_flow/cursor_control_flow_analysis.py`

Source: [converter/analyzers/program_flow/cursor_control_flow_analysis.py](../../../../../converter/analyzers/program_flow/cursor_control_flow_analysis.py) | 274 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `9e413ab54dd4df3537070cfd3d1a50083ae7d95545e4b4805a736b23d6552a1d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Conservative cursor lifecycle/control-flow analysis for COBOL source.

## Module-level bindings

`_CURSOR_DECL` (L19), `_CURSOR_OP` (L20), `_BRANCH` (L21), `_LOOP` (L22), `_SQL_BEGIN` (L23), `_SQL_END` (L24)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path
from converter.analyzers.program_flow.procedure_control_flow_graph import ProcedureControlFlowGraph, ProcedureControlFlowGraphBuilder, _source_body
```

## Local dependency notes

- [converter/analyzers/program_flow/procedure_control_flow_graph.py](procedure_control_flow_graph.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_cursor_control_flow_analysis.py](../../../tests/test_cursor_control_flow_analysis.md)

## Symbol contracts and control points

### `CursorOperationLocation` - L28-L32

```python
class CursorOperationLocation()
```

Declared class/data-model fields:

```python
cursor: str
operation: str
line: int
paragraph: str
```

### `CursorControlFlowReport` - L36-L46

```python
class CursorControlFlowReport()
```

Declared class/data-model fields:

```python
declared_cursors: list[str] = field(default_factory=list)
operations: list[CursorOperationLocation] = field(default_factory=list)
relationships: dict[str, str] = field(default_factory=dict)
diagnostics: list[str] = field(default_factory=list)
graph: ProcedureControlFlowGraph | None = None
```

### `CursorControlFlowReport.operations_for` - L43-L46

```python
operations_for(self, cursor: str, operation: str | None=None) -> list[CursorOperationLocation]
```

Observed calls (lexical order): `cursor.upper`, `operation.upper`.

### `CursorControlFlowAnalyzer` - L49-L274

```python
class CursorControlFlowAnalyzer()
```

Index cursor operations and conservatively characterize their context.

### `CursorControlFlowAnalyzer.__init__` - L52-L53

```python
__init__(self, graph_builder: ProcedureControlFlowGraphBuilder | None=None) -> None
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`.

### `CursorControlFlowAnalyzer.analyze` - L55-L105

```python
analyze(self, source: str | Path) -> CursorControlFlowReport
```

Observed calls (lexical order): `isinstance`, `source.read_text`, `str`, `self.graph_builder.build`, `text.splitlines`, `range`, `set`, `list`, `enumerate`, `_source_body`, `node_by_line.get`, `_SQL_BEGIN.search`, `_SQL_END.search`, `self._collect_sql`, `sql_buffer.append`, `diagnostics.append`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L70: `for (line_no, raw) in enumerate(lines, 1)`
- L72: `if comment`
- L75: `if not in_sql and _SQL_BEGIN.search(body)`
- L78: `if _SQL_END.search(body)`
- L83: `if in_sql`
- L85: `if _SQL_END.search(body)`
- L94: `if in_sql`

### `CursorControlFlowAnalyzer._collect_sql` - L107-L118

```python
_collect_sql(self, buffer, declared, operations) -> None
```

Observed calls (lexical order): `' '.join`, `_CURSOR_DECL.finditer`, `declared.add`, `match.group`, `match.group('name').upper`, `_CURSOR_OP.finditer`, `CursorOperationLocation`, `operations.append`, `match.group('op').upper`.

Control points:

- L111: `for match in _CURSOR_DECL.finditer(statement)`
- L115: `for match in _CURSOR_OP.finditer(statement)`

### `CursorControlFlowAnalyzer._collect_operations` - L120-L126

```python
_collect_operations(self, body, line_no, paragraph, declared, operations) -> None
```

Observed calls (lexical order): `_CURSOR_DECL.finditer`, `declared.add`, `match.group`, `match.group('name').upper`, `_CURSOR_OP.finditer`, `CursorOperationLocation`, `operations.append`, `match.group('op').upper`.

Control points:

- L121: `for match in _CURSOR_DECL.finditer(body)`
- L123: `for match in _CURSOR_OP.finditer(body)`

### `CursorControlFlowAnalyzer._validate_lifecycle` - L128-L145

```python
_validate_lifecycle(self, report: CursorControlFlowReport) -> None
```

Observed calls (lexical order): `report.diagnostics.append`, `ops.count`.

Control points:

- L129: `if not report.declared_cursors`
- L132: `for name in report.declared_cursors`
- L134: `for op in ('OPEN', 'FETCH', 'CLOSE')`
- L136: `if count == 0`
- L138: `if ops.count('FETCH') > 1`
- L141: `for item in report.operations`
- L142: `if item.cursor not in report.declared_cursors`

### `CursorControlFlowAnalyzer._characterize_relationships` - L147-L274

```python
_characterize_relationships(self, lines, node_by_line, graph, report) -> dict[str, str]
```

Observed calls (lexical order): `adjacency.setdefault`, `adjacency.setdefault(edge.source, set()).update`, `set`, `by_cursor.items`, `next`, `'\n'.join`, `'\n'.join(paragraph_lines).upper`, `_source_body`, `_source_body(raw_line)[0].upper`, `_source_body(raw_line)[0].upper().strip`, `re.search`, `successful_branch_lines.append`, `performed_targets.update`, `match.group`, `match.group(1).upper`, `re.finditer`.
Another 20 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L148: `if not report.declared_cursors`
- L156: `for edge in graph.edges`
- L157: `if edge.resolution != 'local'`
- L182: `for (parent_name, sites) in by_cursor.items()`
- L183: `for fetch_site in (site for site in sites if site.operation == 'FETCH')`
- L184: `if fetch_site.paragraph == '<MAINLINE>'`
- L190: `if node is None`
- L201: `for raw_line in paragraph_lines`
- Another 19 conditions/loops exist in this source span.

### `CursorControlFlowAnalyzer._characterize_relationships.reachable` - L161-L170

```python
reachable(source: str) -> set[str]
```

Observed calls (lexical order): `set`, `adjacency.get`, `list`, `pending.pop`, `visited.add`, `pending.extend`.

Control points:

- L164: `while pending`
- L166: `if target in visited`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
