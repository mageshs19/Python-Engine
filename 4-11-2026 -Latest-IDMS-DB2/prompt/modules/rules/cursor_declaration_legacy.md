# `rules/cursor_declaration_legacy.py`

Source: [rules/cursor_declaration_legacy.py](../../../rules/cursor_declaration_legacy.py) | 72 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `d7d51606feaccbda1606ec2246623a1923db9040e71ebba77987fa84cdff2d20`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Literals belonging ONLY to the legacy CursorDeclarationGenerator.

## Module-level bindings

`COLUMN_WHERE_FIRST` (L46), `IND_WHERE_FIRST` (L48), `TABLE_VIEW_SUFFIXES` (L55), `TABLE_PREFIX_LENGTH` (L56), `BANNER_NAME_TRIM` (L57), `FIRST_CURSOR_ORDER` (L66), `__all__` (L68)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_geometry import BODY_FIRST_COLUMN
```

## Local dependency notes

- [rules/cursor_declaration_geometry.py](cursor_declaration_geometry.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](../converter/generators/cursor_declaration/cursor_declaration_generator.md)
- [converter/generators/cursor_declaration/legacy_banner_builder.py](../converter/generators/cursor_declaration/legacy_banner_builder.md)
- [converter/generators/cursor_declaration/legacy_clause_renderer.py](../converter/generators/cursor_declaration/legacy_clause_renderer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
