# `converter/services/perform_thru_scope.py`

Source: [converter/services/perform_thru_scope.py](../../../../converter/services/perform_thru_scope.py) | 59 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `5db7ca1daa248d0b1e252a7450fc64e90c793ba0dc50caba17fd3afb33311792`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reusable paragraph-range inspection for fixed-format COBOL.

## Module-level bindings

`_HEADER` (L12), `_SPAN` (L13), `_QUOTED` (L14), `_NOT_PARAGRAPHS` (L15)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/output_write_extractor.py](../composers/output_write/output_write_extractor.md)
- [converter/validators/generated_cobol_release_validator.py](../validators/generated_cobol_release_validator.md)
- [tests/output_write/test_perform_thru_helper_safety.py](../../tests/output_write/test_perform_thru_helper_safety.md)

## Symbol contracts and control points

### `PerformSpan` - L18-L22

```python
class PerformSpan()
```

Declared class/data-model fields:

```python
start: str
end: str
start_index: int
end_index: int
```

### `paragraph_indices` - L25-L41

```python
paragraph_indices(lines: list[str]) -> dict[str, int]
```

Observed calls (lexical order): `FixedFormatLineService`, `enumerate`, `fixed.is_comment_or_control_line`, `fixed.logical`, `fixed.logical(line).strip`, `fixed.logical(line).strip().upper`, `logical.startswith`, `_HEADER.fullmatch`, `match.group`, `result.setdefault`.

Control points:

- L29: `for (index, line) in enumerate(lines)`
- L30: `if fixed.is_comment_or_control_line(line)`
- L33: `if logical.startswith('PROCEDURE DIVISION')`
- L36: `if not in_procedure`
- L39: `if match and match.group(1) not in _NOT_PARAGRAPHS`

### `perform_spans` - L44-L59

```python
perform_spans(lines: list[str]) -> list[PerformSpan]
```

Observed calls (lexical order): `FixedFormatLineService`, `paragraph_indices`, `' '.join`, `_QUOTED.sub`, `_QUOTED.sub(' ', fixed.logical(line)).strip`, `_QUOTED.sub(' ', fixed.logical(line)).strip().upper`, `fixed.logical`, `fixed.is_comment_or_control_line`, `_SPAN.finditer`, `match.groups`, `PerformSpan`, `result.append`.

Control points:

- L55: `for match in _SPAN.finditer(code)`
- L57: `if start in labels and end in labels and (labels[start] <= labels[end])`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
