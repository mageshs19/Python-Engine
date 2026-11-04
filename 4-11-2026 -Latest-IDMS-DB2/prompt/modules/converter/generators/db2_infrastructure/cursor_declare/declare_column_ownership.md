# `converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py) | 105 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `3f71f0ca42cb4a5bd7f9e265631d97bba042ca71ff8759aac620b4dca0d7ad27`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Which columns does a table own, and is this predicate legal?

## Module-level bindings

`__all__` (L105)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.cursor_declare.declare_diagnostics import DeclareDiagnostics
from converter.generators.db2_infrastructure.cursor_declare.declare_operand_parser import DeclareOperandParser
from rules.cursor_declaration_rules import NO_TABLE_LABEL
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

### `DeclareColumnOwnership` - L25-L102

```python
class DeclareColumnOwnership()
```

Per-table column lookup with a real cache.

### `DeclareColumnOwnership.__init__` - L28-L39

```python
__init__(self, diagnostics: DeclareDiagnostics, column_name_resolver=None) -> None
```

### `DeclareColumnOwnership.reset` - L41-L43

```python
reset(self) -> None
```

A new program may carry a different DCLGEN.

### `DeclareColumnOwnership.columns_of` - L45-L57

```python
columns_of(self, table: str) -> set[str]
```

Uppercased DB2 column names of `table`, or an empty set.

Observed calls (lexical order): `self.diagnostics.log`, `set`, `str`, `str(table).strip`, `str(table).strip().upper`, `self._resolve`.

Control points:

- L47: `if not table`
- L52: `if key in self._cache`

### `DeclareColumnOwnership.first_unowned` - L59-L75

```python
first_unowned(self, conditions: list[str], owned: set[str]) -> str
```

First WHERE left operand not owned by the cursor's table.

Observed calls (lexical order): `DeclareOperandParser.left_operand`, `left.upper`.

Control points:

- L67: `if not conditions or not owned`
- L70: `for condition in conditions`
- L72: `if left and left.upper() not in owned`

### `DeclareColumnOwnership._resolve` - L78-L102

```python
_resolve(self, table: str) -> set[str]
```

Observed calls (lexical order): `self.diagnostics.log`, `set`, `self.column_name_resolver.columns_for_table`, `type`, `str`, `str(column or '').strip`, `str(column or '').strip().upper`.

Control points:

- L79: `if self.column_name_resolver is None`
- L99: `if not owned`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
