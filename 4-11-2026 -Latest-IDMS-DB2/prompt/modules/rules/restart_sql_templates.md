# `rules/restart_sql_templates.py`

Source: [rules/restart_sql_templates.py](../../../rules/restart_sql_templates.py) | 165 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `e45110247af84f792ea08463e0f20c71b68879ebaa100102f977cc190a260860`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQL fragment vocabulary for the restart / checkpoint statements.

## Module-level bindings

`EXEC_SQL_OPEN` (L58), `EXEC_SQL_CLOSE` (L59), `EVALUATE_OPEN` (L60), `EVALUATE_CLOSE` (L61), `PARAGRAPH_TERMINATOR_LINE` (L62), `BLANK_LINE` (L63), `PARAGRAPH_HEADER` (L69), `DEBUG_TRACE` (L70), `SQL_LOCATION_MOVE` (L71), `SELECT_FIRST_COLUMN` (L77), `SELECT_NEXT_COLUMN` (L78), `SELECT_FIRST_INTO` (L79), `SELECT_NEXT_INTO` (L80), `SELECT_FROM` (L81), `UPDATE_HEADER` (L87), `UPDATE_FIRST_SET` (L88), `UPDATE_NEXT_SET` (L89), `INSERT_HEADER` (L105), `INSERT_VALUES_HOST` (L106), `WHERE_FIRST_PREDICATE` (L112), `WHERE_NEXT_PREDICATE` (L113), `QUERYNO_CLAUSE` (L114), `WHEN_VALUE` (L122), `WHEN_OTHER` (L123), `BRANCH_CONTINUE` (L124), `BRANCH_DISPLAY` (L125), `BRANCH_PERFORM` (L126), `ERROR_TEXT` (L134), `__all__` (L136)

## Import declarations

```python
from __future__ import annotations
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/restart/read_paragraph_builder.py](../converter/generators/restart/read_paragraph_builder.md)
- [converter/generators/restart/restart_flow_builder.py](../converter/generators/restart/restart_flow_builder.md)
- [converter/generators/restart/restart_paragraph.py](../converter/generators/restart/restart_paragraph.md)
- [converter/generators/restart/restart_sql_builder.py](../converter/generators/restart/restart_sql_builder.md)
- [tests/restart/test_m4_sql_builder.py](../tests/restart/test_m4_sql_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
