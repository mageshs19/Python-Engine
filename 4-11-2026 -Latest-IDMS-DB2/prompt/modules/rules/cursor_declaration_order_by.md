# `rules/cursor_declaration_order_by.py`

Source: [rules/cursor_declaration_order_by.py](../../../rules/cursor_declaration_order_by.py) | 56 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `456c86c5ac42719674b31f7c196838bc0e1a5665f3a8e343c5ac86b5879dc973`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`PARENT_CURSOR_KEEPS_ORDER_BY` (L10), `CHILD_CURSOR_KEEPS_ORDER_BY` (L11), `ENFORCE_ORDER_BY_RETENTION` (L14), `ENFORCE_ORDER_BY_COLUMN_OWNERSHIP` (L19), `ENFORCE_ORDER_BY_DEDUPLICATION` (L23), `ORDER_BY_DIRECTIONS` (L25), `ORDER_BY_DEFAULT_DIRECTION` (L28), `ORDER_BY_PREFER_IDENTITY_KEY` (L32), `ORDER_BY_NARROWING_APPLIES_TO_CHILD` (L36), `ORDER_BY_SOURCE_PRIMARY_KEY` (L39), `ORDER_BY_SOURCE_PARENT_INTENT` (L40), `ORDER_BY_SOURCE_CHILD_KEY` (L41), `__all__` (L43)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [rules/cursor_declaration_rules.py](cursor_declaration_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
