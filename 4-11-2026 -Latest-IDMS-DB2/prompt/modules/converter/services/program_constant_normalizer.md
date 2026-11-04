# `converter/services/program_constant_normalizer.py`

Source: [converter/services/program_constant_normalizer.py](../../../../converter/services/program_constant_normalizer.py) | 91 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `21225a1910ffdda4c8f62da0e5b1c3e8fe3971c12c28229b832233c847d59934`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic normalization of program-name constants in fixed-format COBOL.

## Module-level bindings

`__all__` (L91)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/manual_storage_parity_composer.py](../composers/manual_storage_parity_composer.md)
- [converter/services/final_generated_output_service.py](final_generated_output_service.md)
- [tests/test_manual_storage_parity_composer.py](../../tests/test_manual_storage_parity_composer.md)

## Symbol contracts and control points

### `ProgramConstantNormalizer` - L13-L88

```python
class ProgramConstantNormalizer()
```

### `ProgramConstantNormalizer._split` - L15-L18

```python
_split(line: str) -> tuple[str, str, str]
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].rstrip`, `line.rstrip`.

Control points:

- L16: `if len(line) >= 7 and line[:6].isdigit()`

### `ProgramConstantNormalizer._build` - L21-L24

```python
_build(seq: str, indicator: str, body: str, tail: str='') -> str
```

Control points:

- L22: `if seq`

### `ProgramConstantNormalizer.normalize` - L27-L32

```python
normalize(cls, text: str) -> str
```

Observed calls (lexical order): `str`, `source.replace`, `source.replace('\r\n', '\n').replace`, `source.replace('\r\n', '\n').replace('\r', '\n').split`, `'\n'.join`, `'\n'.join(cls._normalize_lines(lines)).rstrip`, `cls._normalize_lines`.

Control points:

- L29: `if not source`

### `ProgramConstantNormalizer._normalize_lines` - L35-L88

```python
_normalize_lines(cls, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `cls._split`, `'\n'.join`, `re.search`, `program_match.group`, `program_match.group(1).upper`, `re.compile`, `enumerate`, `declaration_pattern.match`, `match.group`, `match.group('name').upper`, `match.group('value').upper`, `candidates.append`, `set`, `remove_indexes.add`, `re.escape`, `re.sub`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L39: `if not program_match`
- L49: `for (index, body) in enumerate(bodies)`
- L51: `if not match`
- L55: `if name == 'CS-PROGRAM' and value == program_id`
- L57: `if name != 'CS-PROGRAM' and value == program_id`
- L60: `if not candidates`
- L69: `for (index, name) in candidates`
- L71: `if has_shared_constant or index != keep_index`
- Another 5 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
