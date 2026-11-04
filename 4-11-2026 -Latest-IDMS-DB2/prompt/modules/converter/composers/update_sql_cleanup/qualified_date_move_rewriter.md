# `converter/composers/update_sql_cleanup/qualified_date_move_rewriter.py`

Source: [converter/composers/update_sql_cleanup/qualified_date_move_rewriter.py](../../../../../converter/composers/update_sql_cleanup/qualified_date_move_rewriter.py) | 213 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `de43e2c5fcd583d5ffdf8d5f5385f894690da2a8a0d9e48d2cb144fadcdf83b6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Applies the DB2 external-date block to QUALIFIED host moves.

## Module-level bindings

`REALIGN_MARKER` (L42), `MESSAGES` (L44), `__all__` (L213)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)
- [tests/update_sql_cleanup/conftest.py](../../../tests/update_sql_cleanup/conftest.md)
- [tests/update_sql_cleanup/test_qualified_date_move_rewriter.py](../../../tests/update_sql_cleanup/test_qualified_date_move_rewriter.md)

## Symbol contracts and control points

### `QualifiedDateMoveRewriter` - L64-L210

```python
class QualifiedDateMoveRewriter()
```

Inserts the date conversion block before a qualified host move.

### `QualifiedDateMoveRewriter.__init__` - L67-L70

```python
__init__(self, owner, date_builder) -> None
```

### `QualifiedDateMoveRewriter.rewrite` - L75-L120

```python
rewrite(self, text: str) -> str
```

Observed calls (lexical order): `str`, `source.strip`, `source.splitlines`, `len`, `self.owner._logical`, `self.owner.EXEC_SQL_START_PATTERN.match`, `self.owner.EXEC_SQL_END_PATTERN.match`, `logical.upper`, `logical.upper().startswith`, `output.append`, `self._match_qualified_move`, `self._block_for`, `output.extend`, `self._note`, `'\n'.join`, `source.endswith`.

Control points:

- L78: `if not source.strip()`
- L87: `while index < len(lines)`
- L91: `if self.owner.EXEC_SQL_START_PATTERN.match(logical)`
- L93: `if self.owner.EXEC_SQL_END_PATTERN.match(logical)`
- L96: `if in_sql or not logical.upper().startswith('MOVE ')`
- L102: `if match is None`
- L108: `if block is None`
- L117: `if converted == 0`

### `QualifiedDateMoveRewriter._match_qualified_move` - L125-L145

```python
_match_qualified_move(self, lines: list[str], index: int)
```

Match on this line, then on this line joined with the next.

Observed calls (lexical order): `self.owner._logical`, `self.owner.MOVE_TO_DCL_HOST_PATTERN.match`, `len`, `nxt.upper`, `nxt.upper().startswith`, `logical.rstrip`, `nxt.strip`.

Control points:

- L130: `if match`
- L133: `if index + 1 >= len(lines)`
- L137: `if not nxt.upper().startswith('OF DCL')`
- L142: `if match`

### `QualifiedDateMoveRewriter._block_for` - L150-L176

```python
_block_for(self, match, line: str, emitted: list[str])
```

Observed calls (lexical order): `match.group`, `str`, `str(match.group('src')).strip`, `NameNormalizer.to_cobol`, `NameNormalizer.normalize`, `self._column_for`, `self._note`, `self.date_builder.is_db2_date_column`, `self._already_realigned`, `self.owner._leading_spaces`, `self.date_builder.date_ymd8_to_db2_external_move`, `list`.

Control points:

- L156: `if not column`
- L160: `if not self.date_builder.is_db2_date_column(column)`
- L163: `if self._already_realigned(emitted)`

### `QualifiedDateMoveRewriter._already_realigned` - L179-L183

```python
_already_realigned(emitted: list[str]) -> bool
```

Observed calls (lexical order): `reversed`, `' '.join`, `str`, `str(previous).upper`, `str(previous).upper().split`.

Control points:

- L180: `for previous in reversed(emitted[-3:])`
- L181: `if REALIGN_MARKER in ' '.join(str(previous).upper().split())`

### `QualifiedDateMoveRewriter._column_for` - L188-L204

```python
_column_for(self, group: str, host: str) -> str
```

Observed calls (lexical order): `getattr`, `repository.tables`, `NameNormalizer.normalize`, `repository.group_for_table`, `repository.columns_for_table`, `NameNormalizer.to_cobol`.

Control points:

- L190: `if repository is None`
- L193: `for table in repository.tables()`
- L194: `if NameNormalizer.normalize(repository.group_for_table(table)) != group`
- L198: `for column in repository.columns_for_table(table)`
- L202: `if current == host`

### `QualifiedDateMoveRewriter._note` - L206-L210

```python
_note(self, key: str, **values) -> None
```

Observed calls (lexical order): `MESSAGES[key].format`, `self.messages.append`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
