# `converter/composers/cursor_order_cleanup_composer.py`

Source: [converter/composers/cursor_order_cleanup_composer.py](../../../../converter/composers/cursor_order_cleanup_composer.py) | 241 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `d2ef697ea1d7a5ec1b5c98673c0276de082682d8db8a501a934d719666710da6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor ORDER BY cleanup composer.

## Import declarations

```python
from patterns.sequence_patterns import strip_sequence_numbers
from rules.cursor_order_cleanup_rules import CURSOR_ORDER_CLEANUP_MESSAGES, ENFORCE_PARENT_CURSOR_ORDER_BY_CLEANUP
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [rules/cursor_order_cleanup_rules.py](../../rules/cursor_order_cleanup_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/pipeline/registry.py](../pipeline/registry.md)
- [tests/test_cursor_order_by_retention.py](../../tests/test_cursor_order_by_retention.md)

## Symbol contracts and control points

### `CursorOrderCleanupComposer` - L24-L241

```python
class CursorOrderCleanupComposer()
```

### `CursorOrderCleanupComposer.__init__` - L25-L26

```python
__init__(self) -> None
```

### `CursorOrderCleanupComposer.compose` - L31-L82

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self.messages.append`, `self._normalize_line_endings`, `self._normalize_line_endings(text).splitlines`, `len`, `self._is_exec_sql_start`, `output.append`, `self._collect_exec_sql_block`, `self._is_cursor_declare_block`, `output.extend`, `self._clean_declare_block`, `CURSOR_ORDER_CLEANUP_MESSAGES['removed'].format`, `'\n'.join`.

Control points:

- L37: `if not text`
- L40: `if not ENFORCE_PARENT_CURSOR_ORDER_BY_CLEANUP`
- L50: `while index < len(lines)`
- L51: `if not self._is_exec_sql_start(lines[index])`
- L61: `if not self._is_cursor_declare_block(block)`
- L67: `if len(cleaned) != len(block)`
- L73: `if removed`

### `CursorOrderCleanupComposer._normalize_line_endings` - L84-L88

```python
_normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `CursorOrderCleanupComposer._logical` - L90-L94

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

### `CursorOrderCleanupComposer._logical_upper` - L96-L100

```python
_logical_upper(self, line: str) -> str
```

Observed calls (lexical order): `self._logical`, `self._logical(line).upper`.

### `CursorOrderCleanupComposer._is_exec_sql_start` - L102-L106

```python
_is_exec_sql_start(self, line: str) -> bool
```

Observed calls (lexical order): `self._logical_upper`.

### `CursorOrderCleanupComposer._is_exec_sql_end` - L108-L114

```python
_is_exec_sql_end(self, line: str) -> bool
```

Observed calls (lexical order): `self._logical_upper`, `self._logical_upper(line).rstrip`.

### `CursorOrderCleanupComposer._collect_exec_sql_block` - L116-L132

```python
_collect_exec_sql_block(self, lines: list[str], start_index: int) -> tuple[list[str], int]
```

Observed calls (lexical order): `len`, `block.append`, `self._is_exec_sql_end`.

Control points:

- L124: `while index < len(lines)`
- L127: `if self._is_exec_sql_end(lines[index])`

### `CursorOrderCleanupComposer._is_cursor_declare_block` - L134-L144

```python
_is_cursor_declare_block(self, block: list[str]) -> bool
```

Observed calls (lexical order): `self._logical_upper`.

Control points:

- L138: `for line in block`
- L141: `if 'DECLARE ' in logical and ' CURSOR ' in logical`

### `CursorOrderCleanupComposer._cleanup_cursor_declare_block` - L146-L156

```python
_cleanup_cursor_declare_block(self, block: list[str]) -> list[str]
```

Observed calls (lexical order): `self._has_where_clause`, `list`, `self._has_order_by_clause`, `self._remove_order_by_block`.

Control points:

- L150: `if self._has_where_clause(block)`
- L153: `if not self._has_order_by_clause(block)`

### `CursorOrderCleanupComposer._has_where_clause` - L158-L171

```python
_has_where_clause(self, block: list[str]) -> bool
```

Observed calls (lexical order): `self._logical_upper`, `logical.startswith`.

Control points:

- L162: `for line in block`
- L165: `if logical == 'WHERE'`
- L168: `if logical.startswith('WHERE ')`

### `CursorOrderCleanupComposer._has_order_by_clause` - L173-L186

```python
_has_order_by_clause(self, block: list[str]) -> bool
```

Observed calls (lexical order): `self._logical_upper`, `logical.startswith`.

Control points:

- L177: `for line in block`
- L180: `if logical == 'ORDER BY'`
- L183: `if logical.startswith('ORDER BY ')`

### `CursorOrderCleanupComposer._remove_order_by_block` - L188-L211

```python
_remove_order_by_block(self, block: list[str]) -> list[str]
```

Observed calls (lexical order): `self._logical_upper`, `self._is_order_by_start`, `self._is_order_by_end`, `output.append`.

Control points:

- L195: `for line in block`
- L198: `if self._is_order_by_start(logical)`
- L202: `if skipping_order_by`
- L203: `if self._is_order_by_end(logical)`

### `CursorOrderCleanupComposer._is_order_by_start` - L213-L223

```python
_is_order_by_start(self, logical: str) -> bool
```

Observed calls (lexical order): `logical.startswith`.

Control points:

- L217: `if logical == 'ORDER BY'`
- L220: `if logical.startswith('ORDER BY ')`

### `CursorOrderCleanupComposer._is_order_by_end` - L225-L241

```python
_is_order_by_end(self, logical: str) -> bool
```

Observed calls (lexical order): `logical.startswith`.

Control points:

- L229: `if logical == 'FOR READ ONLY'`
- L232: `if logical.startswith('FOR READ ONLY')`
- L235: `if logical == 'END-EXEC'`
- L238: `if logical == 'END-EXEC.'`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
