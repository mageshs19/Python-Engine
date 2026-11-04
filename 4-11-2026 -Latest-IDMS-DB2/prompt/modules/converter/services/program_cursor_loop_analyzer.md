# `converter/services/program_cursor_loop_analyzer.py`

Source: [converter/services/program_cursor_loop_analyzer.py](../../../../converter/services/program_cursor_loop_analyzer.py) | 66 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `65e1f7bebc67ec594f2ff9cadd902f5e0f16c43d00c4af8995df128b03bce27e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import IdmsOperation
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.services.name_normalizer import NameNormalizer
from converter.services.program_flow_models import CursorLoop
from rules.program_flow_rules import IDMS_RETRIEVAL_VERBS
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/resolvers/cursor_name_resolver.py](../resolvers/cursor_name_resolver.md)
- [converter/services/name_normalizer.py](name_normalizer.md)
- [converter/services/program_flow_models.py](program_flow_models.md)
- [rules/program_flow_rules.py](../../rules/program_flow_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `ProgramCursorLoopAnalyzer` - L10-L66

```python
class ProgramCursorLoopAnalyzer()
```

Builds cursor-loop diagnostics from parsed IDMS operations.

### `ProgramCursorLoopAnalyzer.__init__` - L17-L21

```python
__init__(self, cursor_name_resolver: CursorNameResolver | None=None) -> None
```

Observed calls (lexical order): `CursorNameResolver`.

### `ProgramCursorLoopAnalyzer.cursor_loops` - L23-L66

```python
cursor_loops(self, operations: list[IdmsOperation]) -> list[CursorLoop]
```

Observed calls (lexical order): `str`, `str(operation.operation or '').upper`, `NameNormalizer.normalize`, `self.cursor_name_resolver.cursor_name_from_table`, `len`, `self.cursor_name_resolver.paragraph_names`, `output.append`, `CursorLoop`.

Control points:

- L30: `for operation in operations`
- L33: `if operation_name not in IDMS_RETRIEVAL_VERBS`
- L39: `if not record_name`
- L44: `if cursor_name not in cursor_order_by_name`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
