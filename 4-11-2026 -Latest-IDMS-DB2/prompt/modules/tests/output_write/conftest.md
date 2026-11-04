# `tests/output_write/conftest.py`

Source: [tests/output_write/conftest.py](../../../../tests/output_write/conftest.py) | 106 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `17d45f65087b8d4d469849da08a3e1504f938f4d3035d17244d00a63b7c0d1c2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`AREA_A` (L9), `AREA_B` (L10)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.composers.output_write_paragraph_composer import OutputWriteParagraphComposer
```

## Local dependency notes

- [converter/composers/output_write_paragraph_composer.py](../../converter/composers/output_write_paragraph_composer.md)

## Symbol contracts and control points

### `_render` - L13-L22

```python
_render(body: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `text.lstrip`, `stripped.endswith`.

Control points:

- L15: `if not text`
- L18: `if stripped.endswith('DIVISION.') or stripped.endswith('SECTION.')`
- L20: `if stripped.endswith('.') and ' ' not in stripped`

### `program` - L25-L29

```python
program()
```

### `program._program` - L26-L27

```python
_program(lines: list[str]) -> str
```

Observed calls (lexical order): `'\n'.join`, `_render`.

### `compose` - L33-L38

```python
compose()
```

### `compose._compose` - L34-L36

```python
_compose(text: str)
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `composer.compose`, `list`.

### `bodies` - L42-L50

```python
bodies()
```

### `bodies._bodies` - L43-L48

```python
_bodies(text: str) -> list[str]
```

Observed calls (lexical order): `line.strip`, `str`, `str(text or '').splitlines`.

### `index_of` - L54-L61

```python
index_of()
```

### `index_of._index` - L55-L59

```python
_index(items: list[str], prefix: str) -> int
```

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`, `prefix.upper`.

Control points:

- L56: `for (position, body) in enumerate(items)`
- L57: `if body.upper().startswith(prefix.upper())`

### `single_line_guard` - L65-L75

```python
single_line_guard() -> list[str]
```

### `four_line_guard` - L79-L92

```python
four_line_guard() -> list[str]
```

### `two_writes` - L96-L106

```python
two_writes() -> list[str]
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
