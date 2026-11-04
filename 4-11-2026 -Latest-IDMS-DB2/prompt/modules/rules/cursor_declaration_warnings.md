# `rules/cursor_declaration_warnings.py`

Source: [rules/cursor_declaration_warnings.py](../../../rules/cursor_declaration_warnings.py) | 74 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `7e15a08819c0c639f6c415c68158d68f6ff84cc970451d6aba84196db3bb8ec1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 WARNING comment blocks emitted in place of a refused cursor.

## Module-level bindings

`WARNING_PREFIX` (L36), `NO_TABLE_LABEL` (L40), `CURSOR_NOT_DECLARED_TEMPLATE` (L42), `UNRESOLVED_JOIN_KEY_LINES` (L46), `MISSING_COLUMNS_LINES` (L51), `UNRESOLVED_JOIN_KEY_TEMPLATE` (L61), `MISSING_COLUMNS_TEMPLATE` (L65), `__all__` (L70)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [rules/cursor_declaration_rules.py](cursor_declaration_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
