# `converter/generators/cursor_declaration/__init__.py`

Source: [converter/generators/cursor_declaration/__init__.py](../../../../../converter/generators/cursor_declaration/__init__.py) | 14 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `12c1c34136c0437f17980fd210add6993ee53a574e46863d29631a4f8a826ccd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Legacy cursor declaration generation.

## Module-level bindings

`__all__` (L14)

## Import declarations

```python
from converter.generators.cursor_declaration.cursor_declaration_generator import CursorDeclarationGenerator
```

## Local dependency notes

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](cursor_declaration_generator.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
