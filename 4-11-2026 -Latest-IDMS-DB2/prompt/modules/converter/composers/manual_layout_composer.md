# `converter/composers/manual_layout_composer.py`

Source: [converter/composers/manual_layout_composer.py](../../../../converter/composers/manual_layout_composer.py) | 198 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `d20470d27be81d2769b7b9204b8ff10b8fa61bebf04a2531443e1c536feeb795`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
import re
from catalogs.output_sections import DB2_CURSOR_PARAGRAPH_MARKER, DB2_INFRASTRUCTURE_MARKER
from patterns.db2_patterns import END_PROGRAM_PATTERN
```

## Local dependency notes

- [catalogs/output_sections.py](../../catalogs/output_sections.md)
- [patterns/db2_patterns.py](../../patterns/db2_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `ManualLayoutComposer` - L10-L198

```python
class ManualLayoutComposer()
```

Keeps generated DB2 blocks in a manual-style production layout.

### `ManualLayoutComposer.compose` - L27-L55

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self._normalize_line_endings`, `self._normalize_line_endings(text).splitlines`, `self._rstrip_blank_lines`, `self._find_end_program_index`, `self._normalize_generated_block_spacing`, `self._append_end_program`, `'\n'.join`, `self._normalize_blank_lines`, `result.strip`.

Control points:

- L31: `if not text`
- L37: `if not lines`
- L43: `if end_program_index >= 0`
- L49: `if end_program_line`

### `ManualLayoutComposer._normalize_line_endings` - L57-L61

```python
_normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

### `ManualLayoutComposer._normalize_generated_block_spacing` - L63-L82

```python
_normalize_generated_block_spacing(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `str`, `str(line or '').upper`, `self._rstrip_blank_lines`, `output.append`.

Control points:

- L69: `for line in lines`
- L72: `if DB2_INFRASTRUCTURE_MARKER in logical`
- L76: `if DB2_CURSOR_PARAGRAPH_MARKER in logical`

### `ManualLayoutComposer._append_end_program` - L84-L97

```python
_append_end_program(self, lines: list[str], end_program_line: str) -> list[str]
```

Observed calls (lexical order): `self._rstrip_blank_lines`.

Control points:

- L89: `if not end_program_line`
- L94: `if not trimmed`

### `ManualLayoutComposer._find_end_program_index` - L99-L109

```python
_find_end_program_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self._logical_line`, `END_PROGRAM_PATTERN.match`.

Control points:

- L103: `for (index, line) in enumerate(lines)`
- L106: `if END_PROGRAM_PATTERN.match(logical)`

### `ManualLayoutComposer._logical_line` - L111-L120

```python
_logical_line(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self._remove_right_sequence`, `self._remove_left_sequence`, `text.strip`.

### `ManualLayoutComposer._remove_left_sequence` - L122-L131

```python
_remove_left_sequence(self, line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[6:].strip`.

Control points:

- L128: `if len(text) > 6 and text[:6].strip().isdigit()`

### `ManualLayoutComposer._remove_right_sequence` - L133-L148

```python
_remove_right_sequence(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `re.match`, `match.group`, `match.group('body').rstrip`.

Control points:

- L145: `if match`

### `ManualLayoutComposer._rstrip_blank_lines` - L150-L159

```python
_rstrip_blank_lines(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `len`, `str`, `str(lines[index - 1] or '').strip`.

Control points:

- L156: `while index > 0 and (not str(lines[index - 1] or '').strip())`

### `ManualLayoutComposer._lstrip_blank_lines` - L161-L170

```python
_lstrip_blank_lines(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `len`, `str`, `str(lines[index] or '').strip`.

Control points:

- L167: `while index < len(lines) and (not str(lines[index] or '').strip())`

### `ManualLayoutComposer._trim_blank_edges` - L172-L178

```python
_trim_blank_edges(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._lstrip_blank_lines`, `self._rstrip_blank_lines`.

### `ManualLayoutComposer._normalize_blank_lines` - L180-L198

```python
_normalize_blank_lines(self, text: str) -> str
```

Observed calls (lexical order): `str`, `re.sub`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
