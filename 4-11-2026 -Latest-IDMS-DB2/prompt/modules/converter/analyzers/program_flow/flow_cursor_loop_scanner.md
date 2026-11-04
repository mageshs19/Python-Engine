# `converter/analyzers/program_flow/flow_cursor_loop_scanner.py`

Source: [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](../../../../../converter/analyzers/program_flow/flow_cursor_loop_scanner.py) | 120 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `bd1ea17e2e76ac2b1b559fb39a5afbf1395cbf3d0605936156849201f2c5dea5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Derives one CursorLoop per IDMS cursor-style operation.

## Module-level bindings

`__all__` (L120)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import CursorLoop
from converter.domain.models import IdmsOperation
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.services.name_normalizer import NameNormalizer
from rules.program_flow_rules import IDMS_RETRIEVAL_VERBS, FLOW_MESSAGES, LOOP_TYPE_CURSOR
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [converter/domain/models.py](../../domain/models.md)
- [converter/resolvers/cursor_name_resolver.py](../../resolvers/cursor_name_resolver.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/program_flow_rules.py](../../../rules/program_flow_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `FlowCursorLoopScanner` - L36-L117

```python
class FlowCursorLoopScanner()
```

Builds CursorLoop values from parsed IDMS operations.

### `FlowCursorLoopScanner.__init__` - L39-L46

```python
__init__(self, cursor_name_resolver: CursorNameResolver | None=None, table_name_resolver=None) -> None
```

Observed calls (lexical order): `CursorNameResolver`.

### `FlowCursorLoopScanner.loops` - L48-L102

```python
loops(self, operations: list[IdmsOperation] | None) -> list[CursorLoop]
```

Observed calls (lexical order): `self._log`, `getattr`, `str`, `str(getattr(operation, 'operation', '') or '').upper`, `NameNormalizer.normalize`, `self._table_for_record`, `self.cursor_name_resolver.cursor_name_from_table`, `len`, `self.cursor_name_resolver.paragraph_names`, `output.append`, `CursorLoop`, `int`.

Control points:

- L51: `if self.table_name_resolver is None`
- L57: `for operation in operations or []`
- L59: `if name not in IDMS_RETRIEVAL_VERBS`
- L65: `if not record`
- L69: `if not table`
- L75: `if cursor not in order_by_cursor`

### `FlowCursorLoopScanner._table_for_record` - L105-L112

```python
_table_for_record(self, record: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `resolver.table_for_record`.

Control points:

- L107: `if resolver is None`

### `FlowCursorLoopScanner._log` - L114-L117

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `FLOW_MESSAGES.get`, `self.diagnostics.append`, `template.format`.

Control points:

- L116: `if template`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
