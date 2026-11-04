# `converter/composers/update_sql_cleanup/bare_move_rewriter.py`

Source: [converter/composers/update_sql_cleanup/bare_move_rewriter.py](../../../../../converter/composers/update_sql_cleanup/bare_move_rewriter.py) | 159 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `1328b792f973dea6e8b80d1869fa022ecb530ea57ade74aaf06f21fafdac058f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Rewrites bare 'MOVE ... TO field' targets before a MODIFY into DB2 host moves.

## Module-level bindings

`QUALIFIER_CONNECTORS` (L47), `CONTINUATION_SCAN_LIMIT` (L51), `MESSAGES` (L53), `__all__` (L159)

## Import declarations

```python
from __future__ import annotations
from converter.composers.update_sql_cleanup.date_move_builder import DateMoveBuilder
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/date_move_builder.py](date_move_builder.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)
- [tests/update_sql_cleanup/test_bare_move_rewriter_host_form.py](../../../tests/update_sql_cleanup/test_bare_move_rewriter_host_form.md)

## Symbol contracts and control points

### `BareMoveRewriter` - L65-L156

```python
class BareMoveRewriter()
```

### `BareMoveRewriter.__init__` - L66-L69

```python
__init__(self, owner, scanner, date_builder: DateMoveBuilder) -> None
```

### `BareMoveRewriter.rewrite` - L71-L137

```python
rewrite(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `enumerate`, `self.owner._logical`, `self.owner.MOVE_TO_BARE_FIELD_PATTERN.match`, `output.append`, `NameNormalizer.to_cobol`, `match.group`, `self.owner._is_protected_bare_target`, `self._is_qualified_on_continuation`, `self.owner.messages.append`, `MESSAGES['qualified_continuation'].format`, `self.scanner.next_modify_record`, `self.owner._table_for_record`, `self.owner._column_for_source_field`, `self.owner._host_reference_cobol`, `self.owner._leading_spaces`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L76: `for (index, line) in enumerate(lines)`
- L80: `if not match`
- L86: `if self.owner._is_protected_bare_target(target)`
- L91: `if self._is_qualified_on_continuation(lines, index)`
- L101: `if not record`
- L108: `if not table or not column`
- L114: `if not host_cobol`
- L121: `if self.date_builder.is_db2_date_column(column)`
- Another 1 conditions/loops exist in this source span.

### `BareMoveRewriter._is_qualified_on_continuation` - L142-L156

```python
_is_qualified_on_continuation(self, lines: list[str], index: int) -> bool
```

True when the next logical line opens with OF or IN.

Observed calls (lexical order): `len`, `min`, `range`, `self.owner._logical`, `str`, `str(self.owner._logical(lines[offset]) or '').strip`, `body.upper`, `body.upper().startswith`.

Control points:

- L150: `for offset in range(index + 1, limit)`
- L152: `if not body`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
