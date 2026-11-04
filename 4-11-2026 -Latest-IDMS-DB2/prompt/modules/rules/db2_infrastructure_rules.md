# `rules/db2_infrastructure_rules.py`

Source: [rules/db2_infrastructure_rules.py](../../../rules/db2_infrastructure_rules.py) | 163 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `76fde80bdc4d940122495e76a3ab093210c27779323339540aed07fed9da17df`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 infrastructure block rules.

## Module-level bindings

`ENFORCE_AREA_B_SQL_INDENT` (L83), `IND_EXEC` (L85), `IND_SQL_BODY` (L86), `IND_SELECT_FIRST` (L87), `IND_SELECT_NEXT` (L88), `IND_WHERE_NEXT` (L89), `IND_88_LEVEL` (L90), `TOKEN_EXEC_SQL` (L95), `TOKEN_END_EXEC` (L96), `TOKEN_SELECT` (L97), `TOKEN_WHERE` (L98), `TOKEN_ORDER_BY` (L99), `TOKEN_FOR_READ_ONLY` (L100), `DECLARE_TEMPLATE` (L102), `FROM_TEMPLATE` (L103), `SELECT_ITEM_FIRST_TEMPLATE` (L104), `SELECT_ITEM_NEXT_TEMPLATE` (L105), `SELECT_ALL` (L106), `FLAG_NAME_TEMPLATE` (L111), `NOT_EOC_TEMPLATE` (L112), `EOC_TEMPLATE` (L113), `FLAG_DECLARATION_TEMPLATE` (L115), `CONDITION_TEMPLATE` (L116), `VALUE_NOT_EOC` (L118), `VALUE_EOC` (L119), `SQL_LOCATION_DECLARATION_TEMPLATE` (L124), `MISSING_CURSOR_NAME` (L131), `MISSING_TABLE_TEMPLATE` (L134)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_rules import EMIT_QUERYNO, QUERYNO_BASE, QUERYNO_FIRST, QUERYNO_FIRST_ORDER, QUERYNO_STEP, QUERYNO_TEMPLATE
```

## Local dependency notes

- [rules/cursor_declaration_rules.py](cursor_declaration_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.py](../converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py](../converter/generators/db2_infrastructure/cursor_declare/declare_refusal.md)
- [converter/generators/db2_infrastructure/cursor_flag_builder.py](../converter/generators/db2_infrastructure/cursor_flag_builder.md)
- [converter/generators/db2_infrastructure/sql_location_builder.py](../converter/generators/db2_infrastructure/sql_location_builder.md)
- [tests/test_rules_single_source_of_truth.py](../tests/test_rules_single_source_of_truth.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
