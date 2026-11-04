# `rules/cursor_declaration_geometry.py`

Source: [rules/cursor_declaration_geometry.py](../../../rules/cursor_declaration_geometry.py) | 62 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `70cf5993271e5877990d53c07ec6e96ab23407af73c76e466169da6ca511845c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format geometry for a generated DECLARE CURSOR.

## Module-level bindings

`BODY_FIRST_COLUMN` (L31), `BODY_LAST_COLUMN` (L32), `WARNING_BODY_WIDTH` (L36), `COLUMN_EXEC` (L39), `COLUMN_CLAUSE` (L40), `COLUMN_SELECT_NEXT` (L41), `COLUMN_WHERE_NEXT` (L42), `COLUMN_QUERYNO` (L43), `IND_EXEC` (L45), `IND_CLAUSE` (L46), `IND_SELECT_FIRST` (L50), `IND_SELECT_NEXT` (L52), `IND_WHERE_NEXT` (L53), `IND_QUERYNO` (L54), `__all__` (L56)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [rules/cursor_declaration_legacy.py](cursor_declaration_legacy.md)
- [rules/cursor_declaration_rules.py](cursor_declaration_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
