# `converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py) | 192 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `624d5d375bc84634c0b090f6a33b14e3324ce34cf8ef23ceb1ee104b44b9b4dd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders one DECLARE CURSOR statement.

## Module-level bindings

`__all__` (L192)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.cursor_declare.declare_clause_renderer import DeclareClauseRenderer
from converter.generators.db2_infrastructure.cursor_declare.declare_column_ownership import DeclareColumnOwnership
from converter.generators.db2_infrastructure.cursor_declare.declare_diagnostics import DeclareDiagnostics
from converter.generators.db2_infrastructure.cursor_declare.declare_order_by_planner import DeclareOrderByPlanner
from converter.generators.db2_infrastructure.cursor_declare.declare_refusal import DeclareRefusal
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from rules.cursor_declaration_rules import ENFORCE_ORDER_BY_COLUMN_OWNERSHIP, ENFORCE_WHERE_COLUMN_OWNERSHIP, SWEEP_CURSOR_NO_WHERE_TEMPLATE
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare/declare_clause_renderer.py](declare_clause_renderer.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py](declare_column_ownership.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py](declare_diagnostics.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py](declare_order_by_planner.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py](declare_refusal.md)
- [converter/generators/db2_infrastructure/cursor_spec.py](../cursor_spec.md)
- [rules/cursor_declaration_rules.py](../../../../rules/cursor_declaration_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_declare/__init__.py](__init__.md)

## Symbol contracts and control points

### `CursorDeclareBuilder` - L59-L189

```python
class CursorDeclareBuilder()
```

Renders one DECLARE CURSOR statement.

### `CursorDeclareBuilder.__init__` - L62-L80

```python
__init__(self, line_utils, column_name_resolver=None) -> None
```

Observed calls (lexical order): `DeclareDiagnostics`, `DeclareColumnOwnership`, `DeclareOrderByPlanner`, `DeclareRefusal`, `DeclareClauseRenderer`.

### `CursorDeclareBuilder.messages` - L84-L85

```python
messages(self) -> list[str]
```

### `CursorDeclareBuilder.reset` - L87-L96

```python
reset(self) -> None
```

Drop state from the previous program.

Observed calls (lexical order): `self.diagnostics.reset`, `self.ownership.reset`.

### `CursorDeclareBuilder.build` - L101-L147

```python
build(self, spec: CursorSpec, is_last: bool=True) -> list[str]
```

Observed calls (lexical order): `self.refusal.no_cursor_name`, `self.refusal.no_table`, `list`, `self.refusal.no_columns`, `self._conditions`, `set`, `self.ownership.columns_of`, `self.ownership.first_unowned`, `self.refusal.unowned_join_key`, `self._report_where`, `self.order_by.plan`, `self.renderer.render`, `self.diagnostics.log`, `len`, `self.renderer.queryno`.

Control points:

- L102: `if not spec.cursor_name`
- L105: `if not spec.table_name`
- L109: `if not columns`
- L117: `if ENFORCE_WHERE_COLUMN_OWNERSHIP or ENFORCE_ORDER_BY_COLUMN_OWNERSHIP`
- L120: `if ENFORCE_WHERE_COLUMN_OWNERSHIP`
- L122: `if unowned`

### `CursorDeclareBuilder._conditions` - L153-L165

```python
_conditions(spec: CursorSpec) -> list[str]
```

De-duplicated predicates, order preserved.

Observed calls (lexical order): `set`, `list`, `str`, `str(condition or '').strip`, `seen.add`, `out.append`.

Control points:

- L158: `for condition in list(spec.where_conditions or [])`
- L160: `if not value or value in seen`

### `CursorDeclareBuilder._report_where` - L167-L189

```python
_report_where(self, spec: CursorSpec, conditions: list[str]) -> bool
```

Record whether this cursor is qualified, and return it.

Observed calls (lexical order): `self.diagnostics.log`, `len`, `self.diagnostics.add`, `SWEEP_CURSOR_NO_WHERE_TEMPLATE.format`.

Control points:

- L175: `if conditions`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
