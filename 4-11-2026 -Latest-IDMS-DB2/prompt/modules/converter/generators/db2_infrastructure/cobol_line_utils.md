# `converter/generators/db2_infrastructure/cobol_line_utils.py`

Source: [converter/generators/db2_infrastructure/cobol_line_utils.py](../../../../../converter/generators/db2_infrastructure/cobol_line_utils.py) | 56 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `83f0029c8fc675c3db95a05d945c3b081056e8b107f865656f0674462fbac637`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Stateless COBOL line helpers for DB2 infrastructure generation.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure_generator.py](../db2_infrastructure_generator.md)

## Symbol contracts and control points

### `CobolLineUtils` - L11-L56

```python
class CobolLineUtils()
```

### `CobolLineUtils.logical_line` - L12-L24

```python
logical_line(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `left.strip`, `left.strip().isdigit`, `body.strip`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[6:].strip`, `text.strip`.

Control points:

- L15: `if len(text) >= 80`
- L18: `if left.strip().isdigit()`
- L21: `if len(text) > 6 and text[:6].strip().isdigit()`

### `CobolLineUtils.comment_block` - L26-L27

```python
comment_block(self, title: str) -> list[str]
```

### `CobolLineUtils.comma_lines` - L29-L41

```python
comma_lines(self, items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(item or '').strip`, `enumerate`, `output.append`.

Control points:

- L36: `for (index, item) in enumerate(clean_items)`
- L37: `if index == 0`

### `CobolLineUtils.and_lines` - L43-L53

```python
and_lines(self, items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(item or '').strip`, `enumerate`, `output.append`.

Control points:

- L50: `for (index, item) in enumerate(clean_items)`

### `CobolLineUtils.normalize_include_name` - L55-L56

```python
normalize_include_name(self, value: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
