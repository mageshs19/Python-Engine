# `rules/cursor_declaration_where.py`

Source: [rules/cursor_declaration_where.py](../../../rules/cursor_declaration_where.py) | 77 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `13a1d6ee36471d374db83841b19638505e22f09a74f8f4067f365a1f468bb7bf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> WHERE qualification policy and the operand-parsing vocabulary.

## Module-level bindings

`ENFORCE_WHERE_COLUMN_OWNERSHIP` (L26), `CHILD_JOIN_PREDICATE_TEMPLATE` (L28), `EMIT_DRIVING_KEY_PREDICATE` (L37), `DRIVING_KEY_PREDICATE_TEMPLATE` (L40), `SYMBOL_OPERATORS` (L46), `KEYWORD_OPERATORS` (L58), `OPERAND_QUALIFIER_SEPARATOR` (L61), `HOST_VARIABLE_PREFIX` (L64), `OPERAND_TRIM_CHARACTERS` (L67), `__all__` (L69)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [rules/cursor_declaration_rules.py](cursor_declaration_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
