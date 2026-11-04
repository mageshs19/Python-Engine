# `rules/cursor_order_cleanup_rules.py`

Source: [rules/cursor_order_cleanup_rules.py](../../../rules/cursor_order_cleanup_rules.py) | 39 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `5750d7ab438b02b4955b5caed58c73224caddf129de657411099c8f58cdcf5cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor ORDER BY cleanup rules.

## Module-level bindings

`ENFORCE_PARENT_CURSOR_ORDER_BY_CLEANUP` (L25), `CURSOR_ORDER_CLEANUP_MESSAGES` (L27)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_order_cleanup_composer.py](../converter/composers/cursor_order_cleanup_composer.md)
- [tests/test_cursor_order_by_retention.py](../tests/test_cursor_order_by_retention.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
