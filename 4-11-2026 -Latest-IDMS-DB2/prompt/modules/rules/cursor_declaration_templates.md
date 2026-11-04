# `rules/cursor_declaration_templates.py`

Source: [rules/cursor_declaration_templates.py](../../../rules/cursor_declaration_templates.py) | 79 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `d2231b211ad0c1850c2cd024344b102fcf0d0ba7308dc50a20b757afc569b931`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Clause text and QUERYNO for a generated DECLARE CURSOR.

## Module-level bindings

`DECLARE_ON_EXEC_SQL_LINE` (L41), `DECLARE_LINE_TEMPLATE` (L43), `SELECT_FIRST_TEMPLATE` (L44), `SELECT_NEXT_TEMPLATE` (L45), `FROM_TEMPLATE` (L46), `WHERE_FIRST_TEMPLATE` (L47), `WHERE_NEXT_TEMPLATE` (L48), `ORDER_BY_TEMPLATE` (L49), `FOR_READ_ONLY` (L50), `END_EXEC` (L51), `LAST_DECLARATION_TERMINATOR` (L56), `EMIT_QUERYNO` (L63), `QUERYNO_TEMPLATE` (L65), `QUERYNO_FIRST` (L67), `QUERYNO_STEP` (L68), `QUERYNO_FIRST_ORDER` (L69), `QUERYNO_BASE` (L70), `__all__` (L72)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [rules/cursor_declaration_rules.py](cursor_declaration_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
