# `converter/analyzers/program_flow/procedure_control_flow_graph.py`

Source: [converter/analyzers/program_flow/procedure_control_flow_graph.py](../../../../../converter/analyzers/program_flow/procedure_control_flow_graph.py) | 326 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `8414548410f522698f69a52b5d2086bb62877d1a65a7e49d5c6e7b4fc6450969`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Read-only, generic COBOL PROCEDURE DIVISION control-flow index.

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path
from rules.cursor_close_guarantee_rules import NON_PARAGRAPH_SINGLE_WORDS
```

## Local dependency notes

- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/cursor_control_flow_analysis.py](cursor_control_flow_analysis.md)
- [converter/analyzers/program_flow/paragraph_order_audit.py](paragraph_order_audit.md)
- [runners/audit_procedure_flow.py](../../../runners/audit_procedure_flow.md)
- [tests/test_full_program_representation_audit.py](../../../tests/test_full_program_representation_audit.md)
- [tests/test_procedure_control_flow_graph.py](../../../tests/test_procedure_control_flow_graph.md)

## Symbol contracts and control points

### `ProcedureNode` - L17-L21

```python
class ProcedureNode()
```

Declared class/data-model fields:

```python
name: str
kind: str
start_line: int
end_line: int
```

### `PerformEdge` - L25-L32

```python
class PerformEdge()
```

Declared class/data-model fields:

```python
source: str
line: int
target: str
through: str = ''
inline: bool = False
resolution: str = 'local'
covered_nodes: tuple[str, ...] = ()
```

### `ProcedureControlFlowGraph` - L36-L43

```python
class ProcedureControlFlowGraph()
```

Declared class/data-model fields:

```python
nodes: list[ProcedureNode] = field(default_factory=list)
edges: list[PerformEdge] = field(default_factory=list)
diagnostics: list[str] = field(default_factory=list)
```

### `ProcedureControlFlowGraph.paragraph_names` - L42-L43

```python
paragraph_names(self) -> list[str]
```

### `_source_body` - L46-L78

```python
_source_body(line: str) -> tuple[str, bool]
```

Return fixed-format source area and comment status, preserving lines.

Observed calls (lexical order): `len`, `line[:6].isdigit`, `list`, `''.join`, `''.join(chars).strip`.

Control points:

- L48: `if len(line) >= 7 and line[:6].isdigit()`
- L53: `if is_comment`
- L59: `while i < len(chars)`
- L61: `if quote`
- L63: `if c == quote`
- L64: `if i + 1 < len(chars) and chars[i + 1] == quote`
- L71: `if c in '\'"'`
- L74: `if c == '*' and i + 1 < len(chars) and (chars[i + 1] == '>')`

### `ProcedureControlFlowGraphBuilder` - L81-L326

```python
class ProcedureControlFlowGraphBuilder()
```

Build a paragraph/section graph, optionally expanding procedure COPYbooks.

Declared class/data-model fields:

```python
_header = re.compile('^(?P<name>[A-Z0-9][A-Z0-9-]*)\\.(?:\\s*)$', re.I)
_section = re.compile('^(?P<name>[A-Z0-9][A-Z0-9-]*)\\s+SECTION\\.$', re.I)
_perform = re.compile('(?<!END-)\\bPERFORM\\s+(?P<target>[A-Z0-9][A-Z0-9-]*)(?:\\s+(?:THRU|THROUGH)\\s+(?P<through>[A-Z0-9][A-Z0-9-]*))?\\b', re.I)
_inline = re.compile('\\bPERFORM\\s+(?:UNTIL|VARYING)\\b', re.I)
```

### `ProcedureControlFlowGraphBuilder.__init__` - L90-L92

```python
__init__(self, copybook_dirs: tuple[str | Path, ...]=()) -> None
```

Observed calls (lexical order): `Path`, `tuple`.

### `ProcedureControlFlowGraphBuilder._copy_directive` - L95-L106

```python
_copy_directive(line: str) -> tuple[str | None, bool]
```

Observed calls (lexical order): `_source_body`, `re.fullmatch`, `match.group`, `match.group(1).upper`, `re.match`.

Control points:

- L97: `if comment`
- L102: `if match`
- L104: `if re.match('COPY\\s+(?!IDMS\\b)[A-Z0-9][A-Z0-9-]*\\b', body, re.I)`

### `ProcedureControlFlowGraphBuilder._find_copybook` - L108-L127

```python
_find_copybook(self, member: str, source_path: Path | None) -> Path | None
```

Observed calls (lexical order): `roots.extend`, `set`, `root.resolve`, `resolved.is_dir`, `seen.add`, `root.iterdir`, `candidate.is_file`, `candidate.stem.upper`, `candidate.suffix.lower`.

Control points:

- L110: `if source_path is not None`
- L112: `for parent in source_path.parents`
- L116: `for root in roots`
- L121: `if resolved in seen or not resolved.is_dir()`
- L124: `for candidate in root.iterdir()`
- L125: `if candidate.is_file() and candidate.stem.upper() == member and (candidate.suffix.lower() in {'.cpy', '.cob', '.cbl', '.txt'})`

### `ProcedureControlFlowGraphBuilder._expand_procedure_copybooks` - L129-L169

```python
_expand_procedure_copybooks(self, text: str, source_path: Path | None, stack: tuple[str, ...]=()) -> str
```

Observed calls (lexical order): `text.splitlines`, `bool`, `enumerate`, `_source_body`, `re.match`, `output.append`, `self._copy_directive`, `self._expansion_diagnostics.append`, `' -> '.join`, `self._find_copybook`, `copy_path.read_text`, `self._expand_procedure_copybooks`, `'\n'.join`.

Control points:

- L137: `for (line_no, line) in enumerate(lines, 1)`
- L139: `if re.match('^PROCEDURE\\s+DIVISION\\b', body, re.I)`
- L141: `if not in_procedure`
- L145: `if unsupported`
- L151: `if not member`
- L154: `if member in stack`
- L161: `if copy_path is None`

### `ProcedureControlFlowGraphBuilder.build` - L180-L326

```python
build(self, source: str | Path) -> ProcedureControlFlowGraph
```

Observed calls (lexical order): `isinstance`, `source_path.read_text`, `str`, `self._expand_procedure_copybooks`, `text.splitlines`, `_source_body`, `bodies.append`, `header_allowed.append`, `len`, `raw[:6].isdigit`, `raw[:7].isspace`, `source_area.lstrip`, `re.match`, `enumerate`, `self._section.fullmatch`, `raw_nodes.append`.
Another 35 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L183: `if source_path is not None`
- L192: `for raw in lines`
- L194: `if comment`
- L202: `if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace())`
- L207: `if re.match('^PROCEDURE\\s+DIVISION\\b', body, re.I)`
- L213: `for (idx, body) in enumerate(bodies, 1)`
- L214: `if not body or not header_allowed[idx - 1]`
- L217: `if section`
- Another 22 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
