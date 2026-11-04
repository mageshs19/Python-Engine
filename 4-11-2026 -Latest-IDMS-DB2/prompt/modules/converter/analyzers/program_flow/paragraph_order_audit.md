# `converter/analyzers/program_flow/paragraph_order_audit.py`

Source: [converter/analyzers/program_flow/paragraph_order_audit.py](../../../../../converter/analyzers/program_flow/paragraph_order_audit.py) | 98 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `9b5727b40b655715835594f369932bd4ed8a68f2afec6129fb51579def86e902`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Compare original and converted COBOL paragraph order without rewriting either file.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
import re
from pathlib import Path
from converter.analyzers.program_flow.procedure_control_flow_graph import ProcedureControlFlowGraphBuilder
```

## Local dependency notes

- [converter/analyzers/program_flow/procedure_control_flow_graph.py](procedure_control_flow_graph.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/audit_paragraph_order.py](../../../runners/audit_paragraph_order.md)
- [tests/test_paragraph_order_audit.py](../../../tests/test_paragraph_order_audit.md)

## Symbol contracts and control points

### `ParagraphOrderAudit` - L14-L24

```python
class ParagraphOrderAudit()
```

Declared class/data-model fields:

```python
original_count: int
converted_count: int
shared_in_original_order: tuple[str, ...]
missing_from_converted: tuple[str, ...] = ()
reordered_shared: tuple[str, ...] = ()
diagnostics: tuple[str, ...] = ()
```

### `ParagraphOrderAudit.order_preserved` - L23-L24

```python
order_preserved(self) -> bool
```

### `ParagraphOrderAuditor` - L28-L98

```python
class ParagraphOrderAuditor()
```

Audits source-order retention; it never mutates or renumbers source.

Declared class/data-model fields:

```python
graph_builder: ProcedureControlFlowGraphBuilder = field(default_factory=ProcedureControlFlowGraphBuilder)
```

### `ParagraphOrderAuditor.audit` - L34-L98

```python
audit(self, original: str | Path, converted: str | Path) -> ParagraphOrderAudit
```

Observed calls (lexical order): `self.graph_builder.build`, `original.read_text`, `isinstance`, `str`, `original_text.splitlines`, `node.name.upper`, `all`, `len`, `line[:6].isdigit`, `re.sub`, `re.sub('\\*>.*$', '', line[7:72] if len(line) >= 7 and line[:6].isdigit() else line).strip`, `re.fullmatch`, `enumerate`, `range`, `set`, `tuple`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L63: `if removable_abort_lines`
- L75: `if missing`
- L81: `if shared_original != shared_converted`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
