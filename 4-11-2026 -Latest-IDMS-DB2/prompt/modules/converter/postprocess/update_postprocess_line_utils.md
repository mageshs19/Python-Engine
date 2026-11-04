# `converter/postprocess/update_postprocess_line_utils.py`

Source: [converter/postprocess/update_postprocess_line_utils.py](../../../../converter/postprocess/update_postprocess_line_utils.py) | 232 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `d06d495f0b10c577ac08c1b03c018b27584cbe23247a77763e2d2d23059e0695`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format line access for the update post-process.

## Module-level bindings

`LINE_ENDINGS` (L74), `SEQUENCE_WIDTH` (L75), `INDICATOR_COLUMN` (L76), `BODY_FIRST_INDEX` (L77), `BODY_LAST_INDEX` (L78), `COMMENT_INDICATORS` (L79), `BLANK_INDICATOR` (L80), `__all__` (L232)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.update_restart_patterns import COPY_INCLUDE_TOKEN_PATTERN_TEMPLATE, END_PROGRAM_PATTERN, LINKAGE_SECTION_PATTERN, PARAGRAPH_HEADER_PATTERN, PROCEDURE_DIVISION_PATTERN, WORKING_STORAGE_SECTION_PATTERN
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/update_restart_patterns.py](../../patterns/update_restart_patterns.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/restart_logic_pipeline.py](restart_logic_pipeline.md)
- [converter/postprocess/update_business_sql_standardizer.py](update_business_sql_standardizer.md)
- [converter/postprocess/update_main_flow_rewriter.py](update_main_flow_rewriter.md)
- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)
- [converter/postprocess/update_restart_paragraph_manager.py](update_restart_paragraph_manager.md)
- [converter/postprocess/update_storage_include_manager.py](update_storage_include_manager.md)

## Symbol contracts and control points

### `UpdatePostprocessLineUtils` - L83-L229

```python
class UpdatePostprocessLineUtils()
```

### `UpdatePostprocessLineUtils.__init__` - L84-L85

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `UpdatePostprocessLineUtils.lines` - L90-L96

```python
lines(self, text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `str(text or '').replace('\r\n', '\n').replace('\r', '\n').splitlines`.

### `UpdatePostprocessLineUtils.join` - L98-L99

```python
join(self, lines: list[str]) -> str
```

Observed calls (lexical order): `'\n'.join`, `'\n'.join(lines).rstrip`.

### `UpdatePostprocessLineUtils.is_sequenced` - L101-L106

```python
is_sequenced(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:SEQUENCE_WIDTH].strip`, `text[:SEQUENCE_WIDTH].strip().isdigit`.

### `UpdatePostprocessLineUtils.indicator` - L108-L112

```python
indicator(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.is_sequenced`.

Control points:

- L110: `if not self.is_sequenced(text)`

### `UpdatePostprocessLineUtils.is_comment` - L114-L115

```python
is_comment(self, line: str) -> bool
```

Observed calls (lexical order): `self.indicator`.

### `UpdatePostprocessLineUtils.logical` - L117-L124

```python
logical(self, line: str) -> str
```

Columns 8-72, indicator excluded. ONE rule, no heuristics.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.is_sequenced`, `text.strip`, `text[BODY_FIRST_INDEX:BODY_LAST_INDEX].strip`.

Control points:

- L121: `if not self.is_sequenced(text)`

### `UpdatePostprocessLineUtils.logical_text` - L126-L129

```python
logical_text(self, cobol_text: str) -> str
```

Observed calls (lexical order): `'\n'.join`, `self.lines`, `self.logical`.

### `UpdatePostprocessLineUtils.logical_contains` - L131-L138

```python
logical_contains(self, cobol_text: str, expected: str) -> bool
```

Observed calls (lexical order): `str`, `str(expected or '').strip`, `str(expected or '').strip().upper`, `self.lines`, `self.logical`, `self.logical(line).upper`.

Control points:

- L133: `if not target`
- L135: `for line in self.lines(cobol_text)`
- L136: `if target in self.logical(line).upper()`

### `UpdatePostprocessLineUtils.contains_copy` - L140-L150

```python
contains_copy(self, cobol_text: str, include_name: str) -> bool
```

Observed calls (lexical order): `str`, `str(include_name or '').strip`, `str(include_name or '').strip().upper`, `re.compile`, `COPY_INCLUDE_TOKEN_PATTERN_TEMPLATE.format`, `re.escape`, `bool`, `pattern.search`, `self.logical_text`.

Control points:

- L142: `if not target`

### `UpdatePostprocessLineUtils.replace_body` - L155-L183

```python
replace_body(self, reference_line: str, body: str) -> str
```

`reference_line` with columns 8-72 replaced by `body`.

Observed calls (lexical order): `str`, `str(reference_line or '').rstrip`, `self.is_sequenced`, `text.rstrip`, `self.fixed_format.split`, `self.fixed_format.build_or_none`.

Control points:

- L169: `if not self.is_sequenced(reference)`

### `UpdatePostprocessLineUtils.data_division_insert_line_index` - L188-L198

```python
data_division_insert_line_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `LINKAGE_SECTION_PATTERN.match`, `self.logical`, `PROCEDURE_DIVISION_PATTERN.match`, `WORKING_STORAGE_SECTION_PATTERN.match`.

Control points:

- L189: `for (index, line) in enumerate(lines)`
- L190: `if LINKAGE_SECTION_PATTERN.match(self.logical(line))`
- L192: `for (index, line) in enumerate(lines)`
- L193: `if PROCEDURE_DIVISION_PATTERN.match(self.logical(line))`
- L195: `for (index, line) in enumerate(lines)`
- L196: `if WORKING_STORAGE_SECTION_PATTERN.match(self.logical(line))`

### `UpdatePostprocessLineUtils.procedure_paragraph_insert_line_index` - L200-L207

```python
procedure_paragraph_insert_line_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `END_PROGRAM_PATTERN.match`, `self.logical`, `PROCEDURE_DIVISION_PATTERN.match`, `len`.

Control points:

- L201: `for (index, line) in enumerate(lines)`
- L202: `if END_PROGRAM_PATTERN.match(self.logical(line))`
- L204: `for line in lines`
- L205: `if PROCEDURE_DIVISION_PATTERN.match(self.logical(line))`

### `UpdatePostprocessLineUtils.find_paragraph_range` - L209-L229

```python
find_paragraph_range(self, lines: list[str], paragraph_name: str) -> tuple[int, int] | None
```

Observed calls (lexical order): `str`, `str(paragraph_name or '').upper`, `str(paragraph_name or '').upper().rstrip`, `enumerate`, `self.logical`, `self.logical(line).upper`, `self.logical(line).upper().rstrip`, `len`, `self.logical(lines[end]).strip`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L216: `for (index, line) in enumerate(lines)`
- L217: `if self.logical(line).upper().rstrip('.') != target`
- L221: `while end < len(lines)`
- L223: `if end > index + 1 and PARAGRAPH_HEADER_PATTERN.match(next_logical)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
