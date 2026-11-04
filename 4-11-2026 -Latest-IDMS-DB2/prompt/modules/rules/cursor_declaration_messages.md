# `rules/cursor_declaration_messages.py`

Source: [rules/cursor_declaration_messages.py](../../../rules/cursor_declaration_messages.py) | 213 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `ab944ce12acc19e2358d0660803d8637c0560cbb4b26429d75bfb42106f0de6c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Diagnostic catalogues for cursor declaration, join and ORDER BY.

## Module-level bindings

`DECLARATION_MESSAGES` (L26), `SWEEP_CURSOR_NO_WHERE_TEMPLATE` (L96), `JOIN_MESSAGES` (L101), `CURSOR_ORDER_BY_MESSAGES` (L139), `ORDER_BY_KEY_MESSAGES` (L188), `__all__` (L210)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [rules/cursor_declaration_rules.py](cursor_declaration_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
