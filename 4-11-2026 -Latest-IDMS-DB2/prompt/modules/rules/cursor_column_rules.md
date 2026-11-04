# `rules/cursor_column_rules.py`

Source: [rules/cursor_column_rules.py](../../../rules/cursor_column_rules.py) | 139 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `ad942179b7aab62ba9359605b14a3129f474189687116bae4f81704d16acdcf1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`CURSOR_COLUMN_SELECT_RULES` (L11), `CURSOR_COLUMN_ORDER_RULES` (L21), `ORDER_HINT_WORDS` (L28), `DESC_HINT_WORDS` (L37), `ENFORCE_FULL_RECORD_SELECT` (L50), `CURSOR_COLUMN_MESSAGES` (L57), `ENFORCE_ORDER_BY_COLUMN_VALIDATION` (L81), `NON_COLUMN_SENTINELS` (L84), `EMIT_ORDER_BY_DIRECTION` (L103), `ORDER_BY_DIRECTION_ASC` (L105), `ORDER_BY_DIRECTION_DESC` (L106), `EMIT_EXPLICIT_ASC` (L110), `DESC_HINT_FIELDS` (L114), `CURSOR_ORDER_BY_MESSAGES` (L116)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/cursor_column_resolver.py](../converter/resolvers/cursor_column_resolver.md)
- [converter/resolvers/cursor_order_by_resolver.py](../converter/resolvers/cursor_order_by_resolver.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
