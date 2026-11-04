# `converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py) | 82 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `25b511923c254631c8608ea9f7128f36db7f69490c34d42365f08579bf87958d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the DB2 WARNING block emitted in place of a refused cursor.

## Module-level bindings

`__all__` (L82)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.cursor_declare.declare_diagnostics import DeclareDiagnostics
from rules.cursor_declaration_rules import MISSING_COLUMNS_LINES, UNRESOLVED_JOIN_KEY_LINES
from rules.db2_infrastructure_rules import MISSING_CURSOR_NAME, MISSING_TABLE_TEMPLATE
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py](declare_diagnostics.md)
- [rules/cursor_declaration_rules.py](../../../../rules/cursor_declaration_rules.md)
- [rules/db2_infrastructure_rules.py](../../../../rules/db2_infrastructure_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](../../cursor_declaration/cursor_declaration_generator.md)
- [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](cursor_declare_builder.md)

## Symbol contracts and control points

### `DeclareRefusal` - L34-L79

```python
class DeclareRefusal()
```

One refusal: a logged reason and the COBOL comment block.

### `DeclareRefusal.__init__` - L37-L38

```python
__init__(self, diagnostics: DeclareDiagnostics) -> None
```

### `DeclareRefusal.no_cursor_name` - L40-L42

```python
no_cursor_name(self) -> list[str]
```

Observed calls (lexical order): `self.diagnostics.log`.

### `DeclareRefusal.no_table` - L44-L46

```python
no_table(self, cursor: str) -> list[str]
```

Observed calls (lexical order): `self.diagnostics.log`, `MISSING_TABLE_TEMPLATE.format`.

### `DeclareRefusal.no_columns` - L48-L52

```python
no_columns(self, cursor: str, table: str) -> list[str]
```

Refusing beats SELECT *: CHK-12.04 forbids selecting every column, and an implicit list breaks FETCH parity.

Observed calls (lexical order): `self.diagnostics.log`, `self.lines`.

### `DeclareRefusal.unowned_join_key` - L54-L66

```python
unowned_join_key(self, cursor: str, column: str, table: str) -> list[str]
```

Observed calls (lexical order): `self.diagnostics.log`, `self.lines`.

### `DeclareRefusal.lines` - L69-L79

```python
lines(templates, **fields) -> list[str]
```

Render a rules-owned multi-line warning block.

Observed calls (lexical order): `str`, `str(template or '').format`, `str(template or '').strip`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
