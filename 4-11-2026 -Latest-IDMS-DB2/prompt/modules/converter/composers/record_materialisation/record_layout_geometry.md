# `converter/composers/record_materialisation/record_layout_geometry.py`

Source: [converter/composers/record_materialisation/record_layout_geometry.py](../../../../../converter/composers/record_materialisation/record_layout_geometry.py) | 147 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `63f85289879a0904e10edad43f466704d4049739237cadd23263b5a93b9a4872`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format geometry for generated data description entries.

## Module-level bindings

`PERIOD` (L44), `__all__` (L147)

## Import declarations

```python
from __future__ import annotations
from rules.record_materialisation_rules import LAYOUT_BASE_INDENT, LAYOUT_BODY_WIDTH, LAYOUT_LEVEL_STEP, LAYOUT_MAX_INDENT_DEPTH, LAYOUT_MIN_NAME_GAP, LAYOUT_NAME_WIDTH, MAX_LEVEL, MIN_LEVEL
```

## Local dependency notes

- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_entry_renderer.py](record_entry_renderer.md)
- [converter/composers/record_materialisation/record_layout_generator.py](record_layout_generator.md)
- [converter/composers/record_materialisation/record_redefines_renderer.py](record_redefines_renderer.md)

## Symbol contracts and control points

### `RecordLayoutGeometry` - L47-L144

```python
class RecordLayoutGeometry()
```

Column arithmetic for one data description entry.

Declared class/data-model fields:

```python
BODY_WIDTH = LAYOUT_BODY_WIDTH
PERIOD = PERIOD
```

### `RecordLayoutGeometry.root` - L55-L57

```python
root(base_indent: str='') -> str
```

The indent of the field being expanded, or Area B.

Observed calls (lexical order): `str`.

### `RecordLayoutGeometry.indent_text` - L60-L63

```python
indent_text(root: str, depth: int) -> str
```

CORRECTION 2. Nesting indent is capped, never unbounded.

Observed calls (lexical order): `int`, `max`, `min`, `str`.

### `RecordLayoutGeometry.name_width` - L67-L86

```python
name_width(cls, *, indent: str, level: str, name: str, picture: str) -> int
```

Padding that keeps the entry inside columns 8-72.

Observed calls (lexical order): `len`, `max`, `min`.

Control points:

- L84: `if available < minimum`

### `RecordLayoutGeometry.gap_before` - L89-L92

```python
gap_before(cls, head: str, picture: str) -> int
```

Spaces between a head fragment and its PICTURE. Never zero.

Observed calls (lexical order): `len`, `max`.

### `RecordLayoutGeometry.terminate` - L96-L101

```python
terminate(body: str) -> str
```

CORRECTION 4. Exactly one period, whatever the template did.

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `text.rstrip`, `text.rstrip(PERIOD).rstrip`.

Control points:

- L99: `if not text`

### `RecordLayoutGeometry.cap` - L105-L117

```python
cap(cls, body: str) -> str
```

Last-resort guard against a body wider than columns 8-72.

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `len`, `text.lstrip`, `text.strip`, `text.strip().split`, `' '.join`.

Control points:

- L108: `if len(text) <= cls.BODY_WIDTH`
- L114: `if len(collapsed) <= cls.BODY_WIDTH`

### `RecordLayoutGeometry.shift` - L121-L126

```python
shift(cls, level: str, amount: int) -> str
```

Rebase a Sheet Mapping level under the record group.

Observed calls (lexical order): `cls.clamp`, `int`, `str`, `str(level).strip`.

### `RecordLayoutGeometry.clamp` - L129-L131

```python
clamp(value: int) -> str
```

Observed calls (lexical order): `int`, `max`, `min`.

### `RecordLayoutGeometry.depth` - L134-L144

```python
depth(stack: list[str], level: str) -> int
```

Nesting depth from the level stack, not a fixed table.

Observed calls (lexical order): `stack.pop`, `len`, `stack.append`.

Control points:

- L140: `while stack and stack[-1] >= level`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
