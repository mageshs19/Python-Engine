# `tests/generated_fields/conftest.py`

Source: [tests/generated_fields/conftest.py](../../../../tests/generated_fields/conftest.py) | 137 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `5d5b939066bf225e0e1b759f29b63b36ed8e116d7d3d9e9c44ae504d09dde4db`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`AREA_A` (L12), `AREA_B` (L13)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.generators.timestamp.cs_program_declarator import CsProgramDeclarator
from converter.services.generated_field_anchor import GeneratedFieldAnchorResolver
```

## Local dependency notes

- [converter/generators/timestamp/cs_program_declarator.py](../../converter/generators/timestamp/cs_program_declarator.md)
- [converter/services/generated_field_anchor.py](../../converter/services/generated_field_anchor.md)

## Symbol contracts and control points

### `_render` - L16-L25

```python
_render(body: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `text.lstrip`, `stripped.endswith`, `stripped.startswith`.

Control points:

- L18: `if not text`
- L21: `if stripped.startswith(('01 ', 'FD ')) or stripped.endswith('SECTION.')`
- L23: `if stripped.endswith('DIVISION.')`

### `program` - L29-L33

```python
program()
```

### `program._program` - L30-L31

```python
_program(lines: list[str]) -> list[str]
```

Observed calls (lexical order): `_render`.

### `resolve` - L37-L43

```python
resolve()
```

### `resolve._resolve` - L38-L41

```python
_resolve(lines: list[str])
```

Observed calls (lexical order): `GeneratedFieldAnchorResolver`, `resolver.resolve`, `list`.

### `declare` - L47-L53

```python
declare()
```

### `declare._declare` - L48-L51

```python
_declare(lines: list[str], program_id: str='VMDZTEST')
```

Observed calls (lexical order): `CsProgramDeclarator`, `declarator.declare`, `list`.

### `bodies` - L57-L61

```python
bodies()
```

### `bodies._bodies` - L58-L59

```python
_bodies(lines: list[str]) -> list[str]
```

Observed calls (lexical order): `line.strip`.

### `with_work_group` - L65-L73

```python
with_work_group() -> list[str]
```

### `with_generated_group` - L77-L87

```python
with_generated_group() -> list[str]
```

### `without_any_known_group` - L91-L99

```python
without_any_known_group() -> list[str]
```

### `with_record_layout` - L103-L117

```python
with_record_layout() -> list[str]
```

### `with_childless_group` - L121-L128

```python
with_childless_group() -> list[str]
```

### `without_working_storage` - L132-L137

```python
without_working_storage() -> list[str]
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
