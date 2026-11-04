# `converter/generators/db2_infrastructure/sql_location_move_builder.py`

Source: [converter/generators/db2_infrastructure/sql_location_move_builder.py](../../../../../converter/generators/db2_infrastructure/sql_location_move_builder.py) | 95 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `5bfddb74f436ceb04c52caf79d531721f85dbff86bb7fdae78b61955b5c88805`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The one renderer of MOVE ... TO SQL-LOCATION.

## Module-level bindings

`__all__` (L95)

## Import declarations

```python
from __future__ import annotations
from rules.sql_location_rules import EMIT_SQL_LOCATION_WITHOUT_PARAGRAPH_NUMBER, PARAGRAPH_NUMBER_SEPARATOR, SQL_LOCATION_FIELD, SQL_LOCATION_NAME_TEMPLATE, SQL_LOCATION_NUMBER_PAD, SQL_LOCATION_NUMBER_TEMPLATE, SQL_LOCATION_USES_PARAGRAPH_NUMBER
```

## Local dependency notes

- [rules/sql_location_rules.py](../../../rules/sql_location_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](../../composers/update_sql_cleanup/modify_update_rewriter.md)
- [converter/generators/cursor_paragraph/cursor_sql_location.py](../cursor_paragraph/cursor_sql_location.md)
- [converter/generators/sql/sql_statement_builder.py](../sql/sql_statement_builder.md)

## Symbol contracts and control points

### `SqlLocationMoveBuilder` - L42-L92

```python
class SqlLocationMoveBuilder()
```

Renders the SQL-LOCATION move from a paragraph identity.

### `SqlLocationMoveBuilder.paragraph_number` - L46-L57

```python
paragraph_number(paragraph_name: str) -> str
```

The numeric prefix of a paragraph label, or "".

Observed calls (lexical order): `str`, `str(paragraph_name or '').strip`, `name.split`, `head.isdigit`.

Control points:

- L53: `if not name`

### `SqlLocationMoveBuilder.body` - L59-L80

```python
body(self, paragraph_name: str) -> str
```

Un-indented, no period. "" means: emit nothing at all.

Observed calls (lexical order): `str`, `str(paragraph_name or '').strip`, `self.paragraph_number`, `SQL_LOCATION_NUMBER_TEMPLATE.format`, `SQL_LOCATION_NAME_TEMPLATE.format`.

Control points:

- L62: `if not name`
- L67: `if SQL_LOCATION_USES_PARAGRAPH_NUMBER and number`
- L74: `if not EMIT_SQL_LOCATION_WITHOUT_PARAGRAPH_NUMBER`

### `SqlLocationMoveBuilder.sentence` - L82-L92

```python
sentence(self, paragraph_name: str, leading: str='') -> str
```

Full COBOL sentence with its indent and period, or "".

Observed calls (lexical order): `self.body`.

Control points:

- L90: `if not rendered`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
