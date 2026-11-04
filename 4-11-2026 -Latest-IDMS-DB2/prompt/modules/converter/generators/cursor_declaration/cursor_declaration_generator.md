# `converter/generators/cursor_declaration/cursor_declaration_generator.py`

Source: [converter/generators/cursor_declaration/cursor_declaration_generator.py](../../../../../converter/generators/cursor_declaration/cursor_declaration_generator.py) | 265 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `04b2de9c642a626c141e7bbe52a4d2d1e3371a0fd0504065040d2fbf4b96280c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generates DB2 cursor DECLARE statements - LEGACY shape.

## Module-level bindings

`BLOCK_SEPARATOR` (L118), `__all__` (L265)

## Import declarations

```python
from __future__ import annotations
from converter.generators.cursor_declaration.legacy_banner_builder import LegacyBannerBuilder
from converter.generators.cursor_declaration.legacy_clause_renderer import LegacyClauseRenderer
from converter.generators.db2_infrastructure.cursor_declare.declare_column_ownership import DeclareColumnOwnership
from converter.generators.db2_infrastructure.cursor_declare.declare_diagnostics import DeclareDiagnostics
from converter.generators.db2_infrastructure.cursor_declare.declare_order_by_planner import DeclareOrderByPlanner
from converter.generators.db2_infrastructure.cursor_declare.declare_refusal import DeclareRefusal
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from rules.cursor_declaration_legacy import FIRST_CURSOR_ORDER
from rules.cursor_declaration_rules import ENFORCE_ORDER_BY_COLUMN_OWNERSHIP, ENFORCE_WHERE_COLUMN_OWNERSHIP
```

## Local dependency notes

- [converter/generators/cursor_declaration/legacy_banner_builder.py](legacy_banner_builder.md)
- [converter/generators/cursor_declaration/legacy_clause_renderer.py](legacy_clause_renderer.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py](../db2_infrastructure/cursor_declare/declare_column_ownership.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py](../db2_infrastructure/cursor_declare/declare_diagnostics.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py](../db2_infrastructure/cursor_declare/declare_order_by_planner.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py](../db2_infrastructure/cursor_declare/declare_refusal.md)
- [converter/generators/db2_infrastructure/cursor_spec.py](../db2_infrastructure/cursor_spec.md)
- [rules/cursor_declaration_legacy.py](../../../rules/cursor_declaration_legacy.md)
- [rules/cursor_declaration_rules.py](../../../rules/cursor_declaration_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/__init__.py](__init__.md)

## Symbol contracts and control points

### `CursorDeclarationGenerator` - L121-L262

```python
class CursorDeclarationGenerator()
```

Builds the WORKING-STORAGE cursor declaration block.

### `CursorDeclarationGenerator.__init__` - L124-L143

```python
__init__(self, column_name_resolver, diagnostics: list[str] | None=None) -> None
```

Observed calls (lexical order): `DeclareDiagnostics`, `DeclareColumnOwnership`, `DeclareOrderByPlanner`, `DeclareRefusal`, `LegacyBannerBuilder`, `LegacyClauseRenderer`.

Control points:

- L133: `if diagnostics is not None`

### `CursorDeclarationGenerator.messages` - L146-L147

```python
messages(self) -> list[str]
```

### `CursorDeclarationGenerator.reset` - L149-L152

```python
reset(self) -> None
```

Drop state from the previous program.

Observed calls (lexical order): `self.diagnostics.reset`, `self.ownership.reset`.

### `CursorDeclarationGenerator.generate` - L157-L181

```python
generate(self, specs: list[dict[str, object]]) -> list[str]
```

Render every cursor declaration, in cursor order.

Observed calls (lexical order): `len`, `enumerate`, `self._declaration`, `CursorSpec.read`, `lines.append`, `lines.extend`.

Control points:

- L163: `if not specs`
- L169: `for (index, raw) in enumerate(specs)`
- L175: `if not block`
- L177: `if lines`

### `CursorDeclarationGenerator._declaration` - L186-L239

```python
_declaration(self, spec: CursorSpec, cursor_order: int, is_last: bool) -> list[str]
```

Observed calls (lexical order): `self.refusal.no_cursor_name`, `self.refusal.no_table`, `self._unique`, `self.refusal.no_columns`, `set`, `self.ownership.columns_of`, `self.ownership.first_unowned`, `self.refusal.unowned_join_key`, `bool`, `self.order_by.plan`, `self.banner.banner`, `lines.extend`, `self.renderer.render`, `self.diagnostics.log`, `len`, `self.renderer.queryno`.

Control points:

- L192: `if not spec.cursor_name`
- L195: `if not spec.table_name`
- L199: `if not columns`
- L205: `if ENFORCE_WHERE_COLUMN_OWNERSHIP or ENFORCE_ORDER_BY_COLUMN_OWNERSHIP`
- L208: `if ENFORCE_WHERE_COLUMN_OWNERSHIP`
- L210: `if unowned`

### `CursorDeclarationGenerator._unique` - L245-L262

```python
_unique(values) -> list[str]
```

Order preserved, blanks and repeats dropped.

Observed calls (lexical order): `set`, `list`, `str`, `str(value or '').strip`, `seen.add`, `out.append`.

Control points:

- L255: `for value in list(values or [])`
- L257: `if not text or text in seen`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
