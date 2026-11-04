# `converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py) | 163 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `865f8b1d2930921adfc2da91e7fa92c28f2910886726815f1e9efaadb23773b8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Decides which ORDER BY entries survive into the declaration.

## Module-level bindings

`__all__` (L163)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.cursor_declare.declare_diagnostics import DeclareDiagnostics
from converter.generators.db2_infrastructure.cursor_declare.declare_operand_parser import DeclareOperandParser
from rules.cursor_declaration_rules import CHILD_CURSOR_KEEPS_ORDER_BY, ENFORCE_ORDER_BY_COLUMN_OWNERSHIP, ENFORCE_ORDER_BY_DEDUPLICATION, ENFORCE_ORDER_BY_RETENTION, NON_COLUMN_SENTINELS, PARENT_CURSOR_KEEPS_ORDER_BY
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py](declare_diagnostics.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_operand_parser.py](declare_operand_parser.md)
- [rules/cursor_declaration_rules.py](../../../../rules/cursor_declaration_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](../../cursor_declaration/cursor_declaration_generator.md)
- [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](cursor_declare_builder.md)

## Symbol contracts and control points

### `DeclareOrderByPlanner` - L47-L160

```python
class DeclareOrderByPlanner()
```

Filters the resolved ORDER BY entries of one cursor.

### `DeclareOrderByPlanner.__init__` - L50-L51

```python
__init__(self, diagnostics: DeclareDiagnostics) -> None
```

### `DeclareOrderByPlanner.plan` - L53-L83

```python
plan(self, spec, has_where: bool, owned: set[str]) -> list[str]
```

Observed calls (lexical order): `str`, `str(column or '').strip`, `list`, `self.diagnostics.log`, `self._deduplicated`, `self._owned`, `self._legacy_keep`, `len`.

Control points:

- L60: `if not entries`
- L64: `if ENFORCE_ORDER_BY_DEDUPLICATION`
- L67: `if ENFORCE_ORDER_BY_COLUMN_OWNERSHIP`
- L70: `if not entries`
- L74: `if not ENFORCE_ORDER_BY_RETENTION and (not self._legacy_keep(has_where))`

### `DeclareOrderByPlanner._deduplicated` - L86-L116

```python
_deduplicated(self, entries: list[str], spec) -> list[str]
```

First entry for a column wins.

Observed calls (lexical order): `set`, `DeclareOperandParser.order_by_column`, `DeclareOperandParser.order_by_column(entry).upper`, `kept.append`, `self.diagnostics.log`, `seen.add`.

Control points:

- L95: `for entry in entries`
- L99: `if not key`
- L103: `if key in seen`

### `DeclareOrderByPlanner._owned` - L118-L151

```python
_owned(self, entries: list[str], spec, owned: set[str]) -> list[str]
```

Keep only entries whose COLUMN belongs to the FROM table.

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `DeclareOperandParser.order_by_column`, `column.upper`, `bool`, `self.diagnostics.log`, `kept.append`.

Control points:

- L132: `for entry in entries`
- L139: `if unreadable or unowned`

### `DeclareOrderByPlanner._legacy_keep` - L154-L160

```python
_legacy_keep(has_where: bool) -> bool
```

Reachable only when retention is off for a deliberate diff.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
