# `tests/initialization_scope/conftest.py`

Source: [tests/initialization_scope/conftest.py](../../../../tests/initialization_scope/conftest.py) | 161 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `31bef9c76752c6783c5355e8fcebee05f0bcd150ea5c9cf64b12bd20b4d2d955`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`AREA_A` (L10), `AREA_B` (L11)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.initialization.scope_initializer import CursorScopedInitializer
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../../converter/generators/initialization/line_geometry.md)
- [converter/generators/initialization/scope_initializer.py](../../converter/generators/initialization/scope_initializer.md)

## Symbol contracts and control points

### `_render` - L14-L20

```python
_render(body: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `text.endswith`.

Control points:

- L16: `if not text`
- L18: `if text.endswith('.') and ' ' not in text`

### `_fetch_block` - L23-L31

```python
_fetch_block(cursor: str, group: str, field: str) -> list[str]
```

Observed calls (lexical order): `cursor_paragraph_number`.

### `cursor_paragraph_number` - L34-L37

```python
cursor_paragraph_number(cursor: str) -> str
```

Observed calls (lexical order): `{'AAAC1': '720', 'BBBC1': '820', 'CCCC1': '920'}.get`.

### `_drive` - L40-L47

```python
_drive(cursor: str, open_number: str) -> list[str]
```

Observed calls (lexical order): `int`, `str`.

### `program` - L51-L55

```python
program()
```

### `program._program` - L52-L53

```python
_program(lines: list[str]) -> str
```

Observed calls (lexical order): `'\n'.join`, `_render`.

### `run` - L59-L64

```python
run()
```

### `run._run` - L60-L62

```python
_run(text: str)
```

Observed calls (lexical order): `CursorScopedInitializer`, `initializer.process`, `list`.

### `bodies` - L68-L76

```python
bodies()
```

### `bodies._bodies` - L69-L74

```python
_bodies(text: str) -> list[str]
```

Observed calls (lexical order): `LineGeometry.body`, `LineGeometry.split`.

### `index_of` - L80-L87

```python
index_of()
```

### `index_of._index` - L81-L85

```python
_index(items: list[str], prefix: str) -> int
```

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`, `prefix.upper`.

Control points:

- L82: `for (position, body) in enumerate(items)`
- L83: `if body.upper().startswith(prefix.upper())`

### `count_of` - L91-L97

```python
count_of()
```

### `count_of._count` - L92-L95

```python
_count(items: list[str], prefix: str) -> int
```

Observed calls (lexical order): `len`, `b.upper`, `b.upper().startswith`, `prefix.upper`.

### `single_cursor_lines` - L101-L109

```python
single_cursor_lines() -> list[str]
```

Observed calls (lexical order): `_drive`, `_fetch_block`.

### `parent_child_lines` - L113-L123

```python
parent_child_lines() -> list[str]
```

Observed calls (lexical order): `_drive`, `_fetch_block`.

### `three_level_lines` - L127-L139

```python
three_level_lines() -> list[str]
```

Observed calls (lexical order): `_drive`, `_fetch_block`.

### `legacy_startup_lines` - L143-L161

```python
legacy_startup_lines() -> list[str]
```

Observed calls (lexical order): `_drive`, `_fetch_block`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
