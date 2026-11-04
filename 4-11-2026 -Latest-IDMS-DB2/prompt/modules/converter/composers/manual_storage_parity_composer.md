# `converter/composers/manual_storage_parity_composer.py`

Source: [converter/composers/manual_storage_parity_composer.py](../../../../converter/composers/manual_storage_parity_composer.py) | 111 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `f635dbae90f231e2a442f2296add44c9cbbbdc8de110521ce64702993b9e13dd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic program-constant normalization and cursor WITH HOLD policy.

## Module-level bindings

`__all__` (L111)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.program_constant_normalizer import ProgramConstantNormalizer
```

## Local dependency notes

- [converter/services/program_constant_normalizer.py](../services/program_constant_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_manual_storage_parity_composer.py](../../tests/test_manual_storage_parity_composer.md)

## Symbol contracts and control points

### `ManualStorageParityComposer` - L13-L108

```python
class ManualStorageParityComposer()
```

Declared class/data-model fields:

```python
_BODY_START = 7
_BODY_END = 72
```

### `ManualStorageParityComposer._split` - L18-L21

```python
_split(line: str) -> tuple[str, str, str]
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].rstrip`, `line.rstrip`.

Control points:

- L19: `if len(line) >= 7 and line[:6].isdigit()`

### `ManualStorageParityComposer._build` - L24-L34

```python
_build(seq: str, indicator: str, body: str, tail: str='') -> str
```

Control points:

- L26: `if seq`

### `ManualStorageParityComposer.compose` - L36-L42

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._normalize_program_constant`, `self._remove_hold_when_no_commit`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L37: `if not text`

### `ManualStorageParityComposer._normalize_program_constant` - L45-L49

```python
_normalize_program_constant(self, lines: list[str]) -> list[str]
```

Delegate generic program-name normalization to the shared service.

Observed calls (lexical order): `ProgramConstantNormalizer._normalize_lines`.

### `ManualStorageParityComposer._remove_hold_when_no_commit` - L51-L108

```python
_remove_hold_when_no_commit(self, lines: list[str]) -> list[str]
```

Remove WITH HOLD unless that cursor spans a transaction boundary.

Observed calls (lexical order): `self._split`, `body.lstrip`, `body.lstrip().startswith`, `code_lines.append`, `'\n'.join`, `'\n'.join(code_lines).upper`, `list`, `re.finditer`, `bool`, `re.search`, `enumerate`, `match.group`, `match.group(1).upper`, `m.start`, `re.escape`, `next`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L61: `for line in lines`
- L63: `if indicator in {'*', '/'} or body.lstrip().startswith('*')`
- L72: `if not declarations`
- L79: `for (i, line) in enumerate(lines)`
- L86: `if not match`
- L90: `if has_transaction`
- L93: `if not opens or not closes`
- L96: `for open_pos in opens`
- Another 3 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
