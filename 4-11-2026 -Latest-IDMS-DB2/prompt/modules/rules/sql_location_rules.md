# `rules/sql_location_rules.py`

Source: [rules/sql_location_rules.py](../../../rules/sql_location_rules.py) | 94 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `e89832c983df4edea7260a98d10f7fa90a3d110c0bd4ea63c919f7de6286ac46`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Single owner of the MOVE ... TO SQL-LOCATION vocabulary.

## Module-level bindings

`SQL_LOCATION_FIELD` (L57), `SQL_LOCATION_USES_PARAGRAPH_NUMBER` (L60), `SQL_LOCATION_NUMBER_PAD` (L64), `SQL_LOCATION_NUMBER_TEMPLATE` (L66), `SQL_LOCATION_NAME_TEMPLATE` (L67), `PARAGRAPH_NUMBER_SEPARATOR` (L70), `EMIT_SQL_LOCATION_WITHOUT_PARAGRAPH_NUMBER` (L74), `LEGACY_RECORD_LOCATION_TEMPLATE` (L78), `LEGACY_OPERATION_UPDATE` (L79), `LEGACY_OPERATION_INSERT` (L80), `LEGACY_OPERATION_DELETE` (L81), `__all__` (L83)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](../converter/composers/update_sql_cleanup/modify_update_rewriter.md)
- [converter/generators/db2_infrastructure/sql_location_move_builder.py](../converter/generators/db2_infrastructure/sql_location_move_builder.md)
- [converter/generators/sql/sql_statement_builder.py](../converter/generators/sql/sql_statement_builder.md)
- [rules/cursor_paragraph_rules.py](cursor_paragraph_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
