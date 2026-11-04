# `rules/cursor_declaration_rules.py`

Source: [rules/cursor_declaration_rules.py](../../../rules/cursor_declaration_rules.py) | 188 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `64dd28d022cc9aaf342f098a28db110c36c9d29fe7c93c20f5027c51b143885f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 cursor DECLARE statement rules - single import point.

## Module-level bindings

`__all__` (L113)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_geometry import BODY_FIRST_COLUMN, BODY_LAST_COLUMN, COLUMN_CLAUSE, COLUMN_EXEC, COLUMN_QUERYNO, COLUMN_SELECT_NEXT, COLUMN_WHERE_NEXT, IND_CLAUSE, IND_EXEC, IND_QUERYNO, IND_SELECT_FIRST, IND_SELECT_NEXT, IND_WHERE_NEXT, WARNING_BODY_WIDTH
from rules.cursor_declaration_messages import CURSOR_ORDER_BY_MESSAGES, DECLARATION_MESSAGES, JOIN_MESSAGES, ORDER_BY_KEY_MESSAGES, SWEEP_CURSOR_NO_WHERE_TEMPLATE
from rules.cursor_declaration_order_by import CHILD_CURSOR_KEEPS_ORDER_BY, ENFORCE_ORDER_BY_COLUMN_OWNERSHIP, ENFORCE_ORDER_BY_DEDUPLICATION, ENFORCE_ORDER_BY_RETENTION, ORDER_BY_DEFAULT_DIRECTION, ORDER_BY_DIRECTIONS, ORDER_BY_NARROWING_APPLIES_TO_CHILD, ORDER_BY_PREFER_IDENTITY_KEY, ORDER_BY_SOURCE_CHILD_KEY, ORDER_BY_SOURCE_PARENT_INTENT, ORDER_BY_SOURCE_PRIMARY_KEY, PARENT_CURSOR_KEEPS_ORDER_BY
from rules.cursor_declaration_templates import DECLARE_LINE_TEMPLATE, DECLARE_ON_EXEC_SQL_LINE, EMIT_QUERYNO, END_EXEC, FOR_READ_ONLY, FROM_TEMPLATE, LAST_DECLARATION_TERMINATOR, ORDER_BY_TEMPLATE, QUERYNO_BASE, QUERYNO_FIRST, QUERYNO_FIRST_ORDER, QUERYNO_STEP, QUERYNO_TEMPLATE, SELECT_FIRST_TEMPLATE, SELECT_NEXT_TEMPLATE, WHERE_FIRST_TEMPLATE, WHERE_NEXT_TEMPLATE
from rules.cursor_declaration_warnings import CURSOR_NOT_DECLARED_TEMPLATE, MISSING_COLUMNS_LINES, MISSING_COLUMNS_TEMPLATE, NO_TABLE_LABEL, UNRESOLVED_JOIN_KEY_LINES, UNRESOLVED_JOIN_KEY_TEMPLATE, WARNING_PREFIX
from rules.cursor_declaration_where import CHILD_JOIN_PREDICATE_TEMPLATE, DRIVING_KEY_PREDICATE_TEMPLATE, EMIT_DRIVING_KEY_PREDICATE, ENFORCE_WHERE_COLUMN_OWNERSHIP, HOST_VARIABLE_PREFIX, KEYWORD_OPERATORS, OPERAND_QUALIFIER_SEPARATOR, OPERAND_TRIM_CHARACTERS, SYMBOL_OPERATORS
from rules.record_materialisation_rules import NON_COLUMN_SENTINELS
```

## Local dependency notes

- [rules/cursor_declaration_geometry.py](cursor_declaration_geometry.md)
- [rules/cursor_declaration_messages.py](cursor_declaration_messages.md)
- [rules/cursor_declaration_order_by.py](cursor_declaration_order_by.md)
- [rules/cursor_declaration_templates.py](cursor_declaration_templates.md)
- [rules/cursor_declaration_warnings.py](cursor_declaration_warnings.md)
- [rules/cursor_declaration_where.py](cursor_declaration_where.md)
- [rules/record_materialisation_rules.py](record_materialisation_rules.md)

## Importers (21)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](../converter/generators/cursor_declaration/cursor_declaration_generator.md)
- [converter/generators/cursor_declaration/legacy_clause_renderer.py](../converter/generators/cursor_declaration/legacy_clause_renderer.md)
- [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](../converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.py](../converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py](../converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py](../converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_operand_parser.py](../converter/generators/db2_infrastructure/cursor_declare/declare_operand_parser.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py](../converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py](../converter/generators/db2_infrastructure/cursor_declare/declare_refusal.md)
- [converter/resolvers/cursor_join_resolver.py](../converter/resolvers/cursor_join_resolver.md)
- [converter/resolvers/cursor_order_by_resolver.py](../converter/resolvers/cursor_order_by_resolver.md)
- [converter/resolvers/relationship_key_column_resolver.py](../converter/resolvers/relationship_key_column_resolver.md)
- [tests/cursor_contract/conftest.py](../tests/cursor_contract/conftest.md)
- [tests/cursor_where/_fixtures.py](../tests/cursor_where/_fixtures.md)
- [tests/cursor_where/_support.py](../tests/cursor_where/_support.md)
- [tests/cursor_where/test_declare_clauses.py](../tests/cursor_where/test_declare_clauses.md)
- [tests/cursor_where/test_join_resolver.py](../tests/cursor_where/test_join_resolver.md)
- [tests/test_cursor_order_by_retention.py](../tests/test_cursor_order_by_retention.md)
- [tests/test_rules_no_duplicate_constants.py](../tests/test_rules_no_duplicate_constants.md)
- [tests/test_rules_single_source_of_truth.py](../tests/test_rules_single_source_of_truth.md)
- 1 further importers are recorded in [the source manifest](../../source_manifest.json).

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
