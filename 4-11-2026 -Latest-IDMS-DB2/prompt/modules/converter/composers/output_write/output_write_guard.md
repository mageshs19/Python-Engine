# `converter/composers/output_write/output_write_guard.py`

Source: [converter/composers/output_write/output_write_guard.py](../../../../../converter/composers/output_write/output_write_guard.py) | 147 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `e2169d0ad589c9c3cb5026ca7a34689d372821d3f1c40ba142e538a41e3e506c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Structural safety gate for the output write extraction.

## Module-level bindings

`SINGLE_LINE_CONDITION` (L59), `NOT_A_CONDITION` (L60), `__all__` (L147)

## Import declarations

```python
from __future__ import annotations
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from converter.services.cobol_condition_scanner import CobolConditionScanner
from patterns.output_write_paragraph_patterns import PROCEDURE_DIVISION_PATTERN
```

## Local dependency notes

- [converter/composers/output_write/output_write_line_utils.py](output_write_line_utils.md)
- [converter/services/cobol_condition_scanner.py](../../services/cobol_condition_scanner.md)
- [patterns/output_write_paragraph_patterns.py](../../../patterns/output_write_paragraph_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/__init__.py](__init__.md)
- [tests/test_condition_scanner_measures_multiline.py](../../../tests/test_condition_scanner_measures_multiline.md)

## Symbol contracts and control points

### `OutputWriteGuard` - L63-L144

```python
class OutputWriteGuard()
```

Refuses extraction of a block whose own guard spans lines.

### `OutputWriteGuard.__init__` - L66-L74

```python
__init__(self, line_utils: OutputWriteLineUtils | None=None, condition_scanner: CobolConditionScanner | None=None) -> None
```

Observed calls (lexical order): `OutputWriteLineUtils`, `CobolConditionScanner`.

### `OutputWriteGuard.blocks_candidate` - L79-L81

```python
blocks_candidate(self, lines: list[str], if_index: int) -> bool
```

True when THIS candidate's own condition spans lines.

Observed calls (lexical order): `self.condition_size`.

### `OutputWriteGuard.condition_size` - L83-L96

```python
condition_size(self, lines: list[str], if_index: int) -> int
```

Line count of the condition opening at `if_index`.

Observed calls (lexical order): `len`, `self.condition_scanner.is_condition_start`, `self.condition_scanner.condition_line_count`.

Control points:

- L90: `if not 0 <= if_index < len(lines)`
- L93: `if not self.condition_scanner.is_condition_start(lines[if_index])`

### `OutputWriteGuard.blocks_extraction` - L99-L110

```python
blocks_extraction(self, text: str) -> bool
```

True when ANY PROCEDURE DIVISION IF condition spans lines.

Observed calls (lexical order): `self.widest_condition`.

### `OutputWriteGuard.widest_condition` - L112-L144

```python
widest_condition(self, text: str) -> int
```

Longest PROCEDURE DIVISION IF condition. REPORTING ONLY.

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `str(text or '').replace('\r\n', '\n').replace('\r', '\n').split`, `enumerate`, `self.lines.logical`, `PROCEDURE_DIVISION_PATTERN.match`, `self.lines.is_skippable`, `self.condition_scanner.is_condition_start`, `max`, `self.condition_size`.

Control points:

- L124: `for (index, line) in enumerate(lines)`
- L126: `if not logical`
- L129: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L133: `if not in_procedure`
- L136: `if self.lines.is_skippable(line)`
- L139: `if not self.condition_scanner.is_condition_start(line)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
