# `tests/generated_output/test_cursor_block_shape.py`

Source: [tests/generated_output/test_cursor_block_shape.py](../../../../tests/generated_output/test_cursor_block_shape.py) | 241 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ac664866a47c59c29a2a8c99988c68124c95679748072fcca2a81110c2ccd34f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`SQL_LOCATION_SUFFIX` (L8), `EXEC_SQL` (L9), `END_EXEC` (L10), `QUERYNO_TOKEN` (L11), `DECLARE_TOKEN` (L12), `CURSOR_TOKEN` (L13), `PERFORM_TOKEN` (L14)

## Import declarations

```python
from __future__ import annotations
import pytest
```

## Symbol contracts and control points

### `_sql_cursor_names` - L16-L39

```python
_sql_cursor_names(bodies: list[str], verb: str) -> set[str]
```

Observed calls (lexical order): `verb.upper`, `set`, `body.strip`, `body.strip().upper`, `text.startswith`, `text.split`, `len`, `found.add`, `parts[1].rstrip`.

Control points:

- L21: `for body in bodies`
- L24: `if text.startswith(EXEC_SQL)`
- L28: `if text.startswith(END_EXEC)`
- L32: `if not inside or not text.startswith(token)`
- L36: `if len(parts) == 2`

### `_sql_blocks` - L42-L83

```python
_sql_blocks(bodies: list[str]) -> list[list[str]]
```

Every EXEC SQL ... END-EXEC block, opening line included.

Observed calls (lexical order): `body.strip`, `body.strip().upper`, `text.startswith`, `blocks.append`, `current.append`.

Control points:

- L56: `for body in bodies`
- L59: `if text.startswith(EXEC_SQL)`
- L61: `if END_EXEC in text`
- L69: `if not inside`
- L72: `if text.startswith(END_EXEC)`
- L80: `if current`

### `_is_declare_block` - L86-L89

```python
_is_declare_block(block: list[str]) -> bool
```

Observed calls (lexical order): `any`.

### `_entry_move` - L92-L103

```python
_entry_move(bodies: list[str], index: int) -> bool
```

Observed calls (lexical order): `range`, `bodies[position].strip`, `bodies[position].strip().upper`, `text.rstrip`, `text.rstrip('.').endswith`, `text.endswith`.

Control points:

- L93: `for position in range(index, -1, -1)`
- L95: `if text.rstrip('.').endswith(SQL_LOCATION_SUFFIX)`
- L97: `if text.endswith('.') and ' ' not in bodies[position] and (text not in {'END-EXEC.', 'END-EVALUATE.', 'END-IF.', 'END-PERFORM.'})`

### `_context` - L106-L111

```python
_context(bodies: list[str], index: int, before: int=14) -> str
```

Observed calls (lexical order): `max`, `'\n'.join`, `len`, `min`, `range`.

### `test_every_sqlcode_error_branch_sets_sql_location` - L114-L148

```python
test_every_sqlcode_error_branch_sets_sql_location(generated_bodies)
```

Every WHEN OTHER branch must be traceable to a SQL-LOCATION.

Observed calls (lexical order): `enumerate`, `body.strip`, `body.strip().upper`, `text.startswith`, `generated_bodies[index + 1].strip`, `generated_bodies[index + 1].strip().upper`, `branch.rstrip`, `branch.rstrip('.').endswith`, `_entry_move`, `_sqlcode_owner_is_performed`, `_context`.

Control points:

- L124: `for (index, body) in enumerate(generated_bodies)`
- L127: `if text.startswith('EVALUATE SQLCODE')`
- L130: `if text.startswith('EVALUATE') or text.startswith('END-EVALUATE')`
- L133: `if not inside or text != 'WHEN OTHER'`

### `test_every_declare_carries_a_queryno` - L151-L187

```python
test_every_declare_carries_a_queryno(generated_bodies)
```

A cursor DECLARE must carry its own QUERYNO.

Observed calls (lexical order): `_is_declare_block`, `_sql_blocks`, `pytest.skip`, `any`, `line.startswith`, `len`, `QUERYNO_TOKEN.strip`.

Control points:

- L174: `if not blocks`

### `test_every_opened_cursor_is_closed` - L190-L196

```python
test_every_opened_cursor_is_closed(generated_bodies)
```

Observed calls (lexical order): `_sql_cursor_names`, `pytest.skip`.

Control points:

- L194: `if not opened`

### `test_file_close_is_not_counted_as_a_cursor` - L199-L202

```python
test_file_close_is_not_counted_as_a_cursor(generated_bodies)
```

Observed calls (lexical order): `_sql_cursor_names`, `name.endswith`, `name.startswith`.

Control points:

- L201: `for name in closed`

### `_opening_evaluate` - L204-L209

```python
_opening_evaluate(bodies: list[str], index: int) -> int
```

Index of the EVALUATE SQLCODE that opens the block holding `index`.

Observed calls (lexical order): `range`, `bodies[position].strip`, `bodies[position].strip().upper`, `bodies[position].strip().upper().startswith`.

Control points:

- L206: `for position in range(index, -1, -1)`
- L207: `if bodies[position].strip().upper().startswith('EVALUATE SQLCODE')`

### `_sqlcode_owner_is_performed` - L212-L241

```python
_sqlcode_owner_is_performed(bodies: list[str], index: int) -> bool
```

True when the SQLCODE under test was set in ANOTHER paragraph.

Observed calls (lexical order): `_opening_evaluate`, `range`, `bodies[position].strip`, `bodies[position].strip().upper`, `text.startswith`.

Control points:

- L234: `if opening <= 0`
- L237: `for position in range(opening - 1, -1, -1)`
- L239: `if text`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
