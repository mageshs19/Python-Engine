# `rules/cursor_select_minimizer_rules.py`

Source: [rules/cursor_select_minimizer_rules.py](../../../rules/cursor_select_minimizer_rules.py) | 40 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `fc1dfd4f9a66890b3bebaecd17917c93c3dc617e102b0be0a75d60978c18f38b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`CURSOR_SELECT_MINIMIZER_RULES` (L12), `SQL_NON_COLUMN_KEYWORDS` (L21), `SELECT_FIRST_ITEM_BODY_PREFIX` (L38), `SELECT_NEXT_ITEM_BODY_PREFIX` (L39), `FETCH_HOST_BODY_PREFIX` (L40)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cursor_select_column_parser.py](../converter/services/cursor_select_column_parser.md)
- [converter/services/cursor_select_fetch_rewriter.py](../converter/services/cursor_select_fetch_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
