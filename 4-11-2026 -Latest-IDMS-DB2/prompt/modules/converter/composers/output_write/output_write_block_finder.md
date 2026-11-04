# `converter/composers/output_write/output_write_block_finder.py`

Source: [converter/composers/output_write/output_write_block_finder.py](../../../../../converter/composers/output_write/output_write_block_finder.py) | 104 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `d23fe818e534878dc6afff7e92e9111995aa1e392a15af5dc5a6378229156778`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`UNNAMED_PARAGRAPH` (L16), `__all__` (L104)

## Import declarations

```python
from __future__ import annotations
from collections.abc import Iterator
from dataclasses import dataclass
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from converter.composers.output_write.output_write_scanner import OutputWriteScanner
from converter.services.cobol_condition_scanner import CobolConditionScanner
```

## Local dependency notes

- [converter/composers/output_write/output_write_line_utils.py](output_write_line_utils.md)
- [converter/composers/output_write/output_write_scanner.py](output_write_scanner.md)
- [converter/services/cobol_condition_scanner.py](../../services/cobol_condition_scanner.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/__init__.py](__init__.md)
- [converter/composers/output_write/output_write_eligibility.py](output_write_eligibility.md)
- [converter/composers/output_write_paragraph_composer.py](../output_write_paragraph_composer.md)
- [tests/test_condition_scanner_measures_multiline.py](../../../tests/test_condition_scanner_measures_multiline.md)

## Symbol contracts and control points

### `CandidateBlock` - L20-L49

```python
class CandidateBlock()
```

Declared class/data-model fields:

```python
if_index: int = -1
end_index: int = -1
paragraph: str = ''
condition_end: int = -1
```

### `CandidateBlock.has_resolved_condition` - L27-L30

```python
has_resolved_condition(self) -> bool
```

Control points:

- L28: `if self.condition_end < self.if_index`

### `CandidateBlock.condition_line_count` - L33-L36

```python
condition_line_count(self) -> int
```

Control points:

- L34: `if not self.has_resolved_condition`

### `CandidateBlock.body_start` - L39-L42

```python
body_start(self) -> int
```

Control points:

- L40: `if self.has_resolved_condition`

### `CandidateBlock.source` - L45-L46

```python
source(self) -> str
```

### `CandidateBlock.body` - L48-L49

```python
body(self, lines: list[str]) -> list[str]
```

### `OutputWriteBlockFinder` - L52-L101

```python
class OutputWriteBlockFinder()
```

### `OutputWriteBlockFinder.__init__` - L54-L64

```python
__init__(self, line_utils: OutputWriteLineUtils | None=None, scanner: OutputWriteScanner | None=None, condition_scanner: CobolConditionScanner | None=None) -> None
```

Observed calls (lexical order): `OutputWriteLineUtils`, `OutputWriteScanner`, `CobolConditionScanner`.

### `OutputWriteBlockFinder.candidates` - L66-L101

```python
candidates(self, lines: list[str]) -> Iterator[CandidateBlock]
```

Observed calls (lexical order): `self.scanner.procedure_division_index`, `len`, `self.lines.logical`, `self.lines.is_division_boundary`, `self.lines.paragraph_name`, `self.scanner.is_condition_start`, `self.scanner.matching_end_if`, `CandidateBlock`, `self.conditions.condition_end_index`.

Control points:

- L68: `if start < 0`
- L74: `while index < len(lines)`
- L77: `if self.lines.is_division_boundary(logical)`
- L81: `if header`
- L86: `if not self.scanner.is_condition_start(logical)`
- L91: `if end_index >= 0`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
