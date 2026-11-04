# `converter/generators/db2_infrastructure/cursor_spec_builder.py`

Source: [converter/generators/db2_infrastructure/cursor_spec_builder.py](../../../../../converter/generators/db2_infrastructure/cursor_spec_builder.py) | 7 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `b84d6b6b324eda912f4b9d5833f98ee74020d9cf3d303a8bbee168973d73b8bf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Backward-compatible CursorSpecBuilder import path.

## Module-level bindings

`__all__` (L7)

## Import declarations

```python
from converter.generators.db2_infrastructure.spec_builder import CursorSpecBuilder
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/__init__.py](spec_builder/__init__.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_spec_builder_lrf_patch.py](cursor_spec_builder_lrf_patch.md)
- [converter/generators/db2_infrastructure_generator.py](../db2_infrastructure_generator.md)
- [tests/test_cursor_select_column_parity.py](../../../tests/test_cursor_select_column_parity.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
