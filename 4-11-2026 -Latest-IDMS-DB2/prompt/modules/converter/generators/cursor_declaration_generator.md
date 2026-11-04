# `converter/generators/cursor_declaration_generator.py`

Source: [converter/generators/cursor_declaration_generator.py](../../../../converter/generators/cursor_declaration_generator.py) | 14 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `f0a12a2ea532dbdfb0ad52f5a26c4c1b8e42fa0f66f884a7eaeeba7302add873`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Deprecated. Use CursorDeclareBuilder.

## Module-level bindings

`__all__` (L14)

## Import declarations

```python
from converter.generators.db2_infrastructure.cursor_declare_builder import CursorDeclareBuilder as CursorDeclarationGenerator
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare_builder.py](db2_infrastructure/cursor_declare_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
