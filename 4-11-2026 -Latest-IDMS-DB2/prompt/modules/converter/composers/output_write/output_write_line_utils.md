# `converter/composers/output_write/output_write_line_utils.py`

Source: [converter/composers/output_write/output_write_line_utils.py](../../../../../converter/composers/output_write/output_write_line_utils.py) | 137 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `fe337f1e5dc54f99f27fd604029cb75382358993b50989492983b592757c7ef4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Line inspection and cloning for the output write extraction.

## Module-level bindings

`END_SCOPE_PREFIX` (L28), `__all__` (L137)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.output_write_paragraph_patterns import DIVISION_PATTERN, PARAGRAPH_HEADER_PATTERN
from rules.output_write_paragraph_rules import IND_STATEMENT, SCOPE_TERMINATOR_WORDS
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../../services/fixed_format_line_service.md)
- [patterns/output_write_paragraph_patterns.py](../../../patterns/output_write_paragraph_patterns.md)
- [rules/output_write_paragraph_rules.py](../../../rules/output_write_paragraph_rules.md)

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/__init__.py](__init__.md)
- [converter/composers/output_write/output_write_block_finder.py](output_write_block_finder.md)
- [converter/composers/output_write/output_write_eligibility.py](output_write_eligibility.md)
- [converter/composers/output_write/output_write_extractor.py](output_write_extractor.md)
- [converter/composers/output_write/output_write_guard.py](output_write_guard.md)
- [converter/composers/output_write/output_write_renderer.py](output_write_renderer.md)
- [converter/composers/output_write/output_write_scanner.py](output_write_scanner.md)
- [converter/composers/output_write_paragraph_composer.py](../output_write_paragraph_composer.md)

## Symbol contracts and control points

### `OutputWriteLineUtils` - L31-L134

```python
class OutputWriteLineUtils()
```

Shared line helpers. Owns no business decision.

### `OutputWriteLineUtils.__init__` - L34-L38

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `OutputWriteLineUtils.logical` - L41-L43

```python
logical(self, line: str) -> str
```

Uppercased logical line. Matching only.

Observed calls (lexical order): `self.fixed_format.logical`, `self.fixed_format.logical(line).upper`.

### `OutputWriteLineUtils.body_text` - L45-L47

```python
body_text(self, line: str) -> str
```

Logical line in its ORIGINAL case. Rewriting only.

Observed calls (lexical order): `self.fixed_format.logical`.

### `OutputWriteLineUtils.is_skippable` - L49-L50

```python
is_skippable(self, line: str) -> bool
```

Observed calls (lexical order): `self.fixed_format.is_comment_or_control_line`.

### `OutputWriteLineUtils.body_indent` - L52-L53

```python
body_indent(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.body_indent`.

### `OutputWriteLineUtils.executable_lines` - L56-L60

```python
executable_lines(self, body: list[str]) -> list[str]
```

Observed calls (lexical order): `self.body_text`, `self.is_skippable`.

### `OutputWriteLineUtils.last_executable_index` - L62-L69

```python
last_executable_index(self, body: list[str]) -> int
```

Observed calls (lexical order): `len`, `range`, `self.is_skippable`, `self.body_text`.

Control points:

- L63: `for index in range(len(body) - 1, -1, -1)`
- L65: `if self.is_skippable(line)`
- L67: `if self.body_text(line)`

### `OutputWriteLineUtils.paragraph_name` - L72-L86

```python
paragraph_name(self, line: str) -> str
```

Observed calls (lexical order): `self.is_skippable`, `PARAGRAPH_HEADER_PATTERN.match`, `self.logical`, `match.group`, `match.group('name').upper`, `name.startswith`.

Control points:

- L73: `if self.is_skippable(line)`
- L77: `if not match`
- L81: `if name in SCOPE_TERMINATOR_WORDS or name.startswith(END_SCOPE_PREFIX)`

### `OutputWriteLineUtils.paragraph_names` - L88-L92

```python
paragraph_names(self, lines: list[str]) -> set[str]
```

Observed calls (lexical order): `self.paragraph_name`.

### `OutputWriteLineUtils.is_division_boundary` - L95-L96

```python
is_division_boundary(logical: str) -> bool
```

Observed calls (lexical order): `DIVISION_PATTERN.match`, `bool`.

### `OutputWriteLineUtils.template_line` - L100-L101

```python
template_line(lines: list[str], index: int) -> str
```

Observed calls (lexical order): `len`.

### `OutputWriteLineUtils.clone` - L103-L122

```python
clone(self, template: str, body: str, indicator: str | None=None) -> str
```

Build a line borrowing the sequence area of `template`.

Observed calls (lexical order): `self.fixed_format.split`, `self.fixed_format.build_or_none`.

### `OutputWriteLineUtils.replace_body_wrapped` - L124-L125

```python
replace_body_wrapped(self, line: str, body: str) -> list[str]
```

Observed calls (lexical order): `self.fixed_format.replace_body_wrapped`.

### `OutputWriteLineUtils.call_indent` - L127-L134

```python
call_indent(self, lines: list[str], body_start: int) -> str
```

Observed calls (lexical order): `len`, `range`, `self.is_skippable`, `self.body_text`, `self.body_indent`.

Control points:

- L128: `for index in range(body_start, len(lines))`
- L130: `if self.is_skippable(line)`
- L132: `if self.body_text(line)`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
