# `converter/generators/db2_infrastructure/cursor_declare/__init__.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/__init__.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/__init__.py) | 13 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `bb60195c3a2195787a909d1f777f0bd08b6064eab7c13c2b47c883f1a7762a4c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DECLARE CURSOR rendering.

## Module-level bindings

`__all__` (L13)

## Import declarations

```python
from converter.generators.db2_infrastructure.cursor_declare.cursor_declare_builder import CursorDeclareBuilder
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](cursor_declare_builder.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_declare_builder.py](../cursor_declare_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
