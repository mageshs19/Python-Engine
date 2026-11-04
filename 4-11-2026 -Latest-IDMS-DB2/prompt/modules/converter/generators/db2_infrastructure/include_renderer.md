# `converter/generators/db2_infrastructure/include_renderer.py`

Source: [converter/generators/db2_infrastructure/include_renderer.py](../../../../../converter/generators/db2_infrastructure/include_renderer.py) | 181 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `fde0f3667366bb3338eca0cdd79d908f791863de3e108a19462747a45f203c39`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Single source of truth for EXEC SQL INCLUDE emission and detection.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from patterns.db2_include_patterns import END_EXEC_PATTERN, EXEC_SQL_OPEN_PATTERN, INCLUDE_BODY_PATTERN, INCLUDE_NAME_PATTERN, INCLUDE_SINGLE_PATTERN
from rules.db2_include_rules import IND_INCLUDE, IND_INCLUDE_BODY, INCLUDE_BLOCK_BODY_TEMPLATE, INCLUDE_BLOCK_CLOSE, INCLUDE_BLOCK_OPEN, INCLUDE_SINGLE_LINE, INCLUDE_SINGLE_TEMPLATE, INFRASTRUCTURE_INCLUDES
from patterns.sequence_patterns import strip_sequence_numbers
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/db2_include_patterns.py](../../../patterns/db2_include_patterns.md)
- [patterns/sequence_patterns.py](../../../patterns/sequence_patterns.md)
- [rules/db2_include_rules.py](../../../rules/db2_include_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/dclgen_include_cleanup.py](../../composers/cleanup/dclgen_include_cleanup.md)
- [converter/generators/boilerplate_generator.py](../boilerplate_generator.md)
- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](infrastructure_block_builder.md)
- [converter/postprocess/storage_include/storage_include_injector.py](../../postprocess/storage_include/storage_include_injector.md)

## Symbol contracts and control points

### `IncludeRenderer` - L38-L181

```python
class IncludeRenderer()
```

Renders include statements and finds the ones already present.

### `IncludeRenderer.__init__` - L41-L42

```python
__init__(self, line_utils=None) -> None
```

### `IncludeRenderer.render` - L47-L63

```python
render(self, name: str) -> list[str]
```

One include, in the site's canonical shape and indent.

Observed calls (lexical order): `self.normalize`, `INCLUDE_SINGLE_TEMPLATE.format`, `INCLUDE_BLOCK_BODY_TEMPLATE.format`.

Control points:

- L50: `if not clean`
- L53: `if INCLUDE_SINGLE_LINE`

### `IncludeRenderer.render_all` - L65-L77

```python
render_all(self, names: list[str]) -> list[str]
```

Render each distinct include once, order preserved.

Observed calls (lexical order): `set`, `self.normalize`, `seen.add`, `out.extend`, `self.render`.

Control points:

- L70: `for name in names or []`
- L72: `if not clean or clean in seen`

### `IncludeRenderer.existing` - L82-L101

```python
existing(self, lines: list[str]) -> set[str]
```

Every include already present, whichever shape carries it.

Observed calls (lexical order): `set`, `self._logical`, `INCLUDE_SINGLE_PATTERN.match`, `found.add`, `match.group`, `self.normalize`, `INCLUDE_BODY_PATTERN.match`, `found.discard`.

Control points:

- L86: `for line in lines or []`
- L88: `if not logical`
- L92: `if match`
- L97: `if match`

### `IncludeRenderer.counts` - L103-L136

```python
counts(self, lines: list[str]) -> dict[str, int]
```

How many times each include appears. Duplicates show as > 1.

Observed calls (lexical order): `self._logical`, `INCLUDE_SINGLE_PATTERN.match`, `self.normalize`, `single.group`, `totals.get`, `EXEC_SQL_OPEN_PATTERN.match`, `END_EXEC_PATTERN.match`, `INCLUDE_BODY_PATTERN.match`, `body.group`, `totals.pop`.

Control points:

- L108: `for line in lines or []`
- L110: `if not logical`
- L114: `if single`
- L119: `if EXEC_SQL_OPEN_PATTERN.match(logical)`
- L123: `if END_EXEC_PATTERN.match(logical)`
- L127: `if not inside_block`
- L131: `if body`

### `IncludeRenderer.missing` - L138-L155

```python
missing(self, lines: list[str], required: list[str]) -> list[str]
```

Required includes not already present, order preserved.

Observed calls (lexical order): `self.existing`, `set`, `self.normalize`, `seen.add`, `out.append`.

Control points:

- L148: `for name in required or []`
- L150: `if not clean or clean in present or clean in seen`

### `IncludeRenderer.is_infrastructure` - L161-L163

```python
is_infrastructure(name: str) -> bool
```

SQLCA, SQLERRWS, SQLERROR and GEN are not DCLGEN tables.

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.normalize(name).upper`.

### `IncludeRenderer.normalize` - L169-L170

```python
normalize(name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.normalize(str(name or '')).upper`, `str`.

### `IncludeRenderer._logical` - L172-L181

```python
_logical(self, line: str) -> str
```

Strip the sequence area, whatever helper the caller supplied.

Observed calls (lexical order): `getattr`, `callable`, `getter`, `str`, `str(getter(line) or '').strip`, `str(getter(line) or '').strip().upper`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`, `strip_sequence_numbers(str(line or '')).strip().upper`.

Control points:

- L174: `if self.line_utils is not None`
- L176: `if callable(getter)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
