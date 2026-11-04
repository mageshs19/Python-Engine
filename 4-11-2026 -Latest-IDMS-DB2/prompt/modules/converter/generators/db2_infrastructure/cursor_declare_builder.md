# `converter/generators/db2_infrastructure/cursor_declare_builder.py`

Source: [converter/generators/db2_infrastructure/cursor_declare_builder.py](../../../../../converter/generators/db2_infrastructure/cursor_declare_builder.py) | 18 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `af71d9aa2602434449f680a6089684833489c0a76308594362b17ce4c788ab44`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Backward-compatible import point.

## Module-level bindings

`__all__` (L18)

## Import declarations

```python
from converter.generators.db2_infrastructure.cursor_declare import CursorDeclareBuilder
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare/__init__.py](cursor_declare/__init__.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration_generator.py](../cursor_declaration_generator.md)
- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](infrastructure_block_builder.md)
- [tests/cursor_contract/conftest.py](../../../tests/cursor_contract/conftest.md)
- [tests/cursor_where/conftest.py](../../../tests/cursor_where/conftest.md)
- [tests/test_cursor_order_by_retention.py](../../../tests/test_cursor_order_by_retention.md)
- [tests/test_cursor_select_column_parity.py](../../../tests/test_cursor_select_column_parity.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
