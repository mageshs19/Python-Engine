# `converter/composers/output_write/output_write_scanner.py`

Source: [converter/composers/output_write/output_write_scanner.py](../../../../../converter/composers/output_write/output_write_scanner.py) | 107 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `46eca5ced019c87ebf576b0ef4a1eafe5240f58f27c886bb4c084085e10201ad`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Block discovery for the output write extraction.

## Module-level bindings

`__all__` (L107)

## Import declarations

```python
from __future__ import annotations
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from patterns.output_write_paragraph_patterns import END_IF_PATTERN, IF_START_PATTERN, PERFORM_WRITE_PARAGRAPH_PATTERN, PROCEDURE_DIVISION_PATTERN, WRITE_STATEMENT_PATTERN
from rules.output_write_paragraph_rules import IF_SCAN_LIMIT
```

## Local dependency notes

- [converter/composers/output_write/output_write_line_utils.py](output_write_line_utils.md)
- [patterns/output_write_paragraph_patterns.py](../../../patterns/output_write_paragraph_patterns.md)
- [rules/output_write_paragraph_rules.py](../../../rules/output_write_paragraph_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/__init__.py](__init__.md)
- [converter/composers/output_write/output_write_block_finder.py](output_write_block_finder.md)
- [converter/composers/output_write/output_write_eligibility.py](output_write_eligibility.md)
- [converter/composers/output_write/output_write_extractor.py](output_write_extractor.md)
- [converter/composers/output_write_paragraph_composer.py](../output_write_paragraph_composer.md)

## Symbol contracts and control points

### `OutputWriteScanner` - L24-L104

```python
class OutputWriteScanner()
```

Finds the boundaries the extraction needs.

### `OutputWriteScanner.__init__` - L27-L31

```python
__init__(self, line_utils: OutputWriteLineUtils | None=None) -> None
```

Observed calls (lexical order): `OutputWriteLineUtils`.

### `OutputWriteScanner.procedure_division_index` - L34-L38

```python
procedure_division_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `PROCEDURE_DIVISION_PATTERN.match`, `self.lines.logical`.

Control points:

- L35: `for (index, line) in enumerate(lines)`
- L36: `if PROCEDURE_DIVISION_PATTERN.match(self.lines.logical(line))`

### `OutputWriteScanner.is_condition_start` - L42-L43

```python
is_condition_start(logical: str) -> bool
```

Observed calls (lexical order): `IF_START_PATTERN.match`, `bool`.

### `OutputWriteScanner.matching_end_if` - L45-L72

```python
matching_end_if(self, lines: list[str], if_index: int) -> int
```

Index of the END-IF that closes the IF at if_index.

Observed calls (lexical order): `len`, `min`, `range`, `self.lines.is_skippable`, `self.lines.logical`, `self.lines.paragraph_name`, `IF_START_PATTERN.match`, `END_IF_PATTERN.match`.

Control points:

- L50: `for index in range(if_index, limit)`
- L53: `if self.lines.is_skippable(line)`
- L57: `if not logical`
- L60: `if index > if_index and self.lines.paragraph_name(line)`
- L63: `if IF_START_PATTERN.match(logical)`
- L67: `if END_IF_PATTERN.match(logical)`
- L69: `if depth == 0`

### `OutputWriteScanner.write_records` - L75-L85

```python
write_records(self, body: list[str]) -> list[str]
```

Observed calls (lexical order): `self.lines.is_skippable`, `WRITE_STATEMENT_PATTERN.match`, `self.lines.logical`, `match.group`, `out.append`.

Control points:

- L78: `for line in body`
- L79: `if self.lines.is_skippable(line)`
- L82: `if match`

### `OutputWriteScanner.already_extracted` - L87-L92

```python
already_extracted(self, body: list[str]) -> bool
```

True when an earlier pass already replaced this block.

Observed calls (lexical order): `any`, `PERFORM_WRITE_PARAGRAPH_PATTERN.match`, `self.lines.logical`.

### `OutputWriteScanner.paragraph_end_index` - L95-L104

```python
paragraph_end_index(self, lines: list[str], start: int) -> int
```

Index just past the paragraph containing `start`.

Observed calls (lexical order): `len`, `range`, `self.lines.paragraph_name`, `self.lines.is_division_boundary`, `self.lines.logical`.

Control points:

- L97: `for index in range(start + 1, len(lines))`
- L98: `if self.lines.paragraph_name(lines[index])`
- L100: `if self.lines.is_division_boundary(self.lines.logical(lines[index]))`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
