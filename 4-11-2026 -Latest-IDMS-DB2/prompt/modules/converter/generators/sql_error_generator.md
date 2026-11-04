# `converter/generators/sql_error_generator.py`

Source: [converter/generators/sql_error_generator.py](../../../../converter/generators/sql_error_generator.py) | 298 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `08d581151098de47855fadb54b8e31912ceec75d2cc46653014fdbad15bc4e67`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generates and ensures the SQLERROR routine.

## Module-level bindings

`LEFT_SEQUENCE_WIDTH` (L70), `RIGHT_SEQUENCE_WIDTH` (L71), `FIXED_LINE_WIDTH` (L72)

## Import declarations

```python
from __future__ import annotations
import re
from patterns.cursor_paragraph_patterns import LEGACY_SQL_ERROR_HEADER_PATTERN, LEGACY_SQL_ERROR_HEADER_REPLACEMENT, LEGACY_SQL_ERROR_PERFORM_PATTERN
from patterns.db2_patterns import END_PROGRAM_PATTERN
from patterns.sql_error_patterns import END_PROGRAM_BOUNDARY_PATTERN, PARAGRAPH_HEADER_PATTERN, SQLERROR_HEADER_ONLY_PATTERN, SQLERROR_PARAGRAPH_PATTERN
from rules.sql_error_rules import EMIT_SQL_ERROR_PARAGRAPH_HEADER, IND_SQL_BODY, IND_STATEMENT, OLD_BLOCK_BODY_TOKENS, SQL_ERROR_BANNER, SQL_ERROR_INCLUDE_NAME, SQL_ERROR_MESSAGES, SQL_ERROR_PARAGRAPH_NAME
```

## Local dependency notes

- [patterns/cursor_paragraph_patterns.py](../../patterns/cursor_paragraph_patterns.md)
- [patterns/db2_patterns.py](../../patterns/db2_patterns.md)
- [patterns/sql_error_patterns.py](../../patterns/sql_error_patterns.md)
- [rules/sql_error_rules.py](../../rules/sql_error_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph_generator.py](cursor_paragraph_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/postprocess/update_storage_include_manager.py](../postprocess/update_storage_include_manager.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../tests/test_generic_cursor_numbering_and_perform_integrity.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `SqlErrorGenerator` - L75-L298

```python
class SqlErrorGenerator()
```

Owns the SQLERROR routine block and legacy-name normalisation.

Declared class/data-model fields:

```python
SQLERROR_PARAGRAPH_NAME = SQL_ERROR_PARAGRAPH_NAME
PARAGRAPH_NAME = SQL_ERROR_PARAGRAPH_NAME
DEFAULT_PARAGRAPH_NAME = SQL_ERROR_PARAGRAPH_NAME
SQLERROR_PARAGRAPH_NAME = SQL_ERROR_PARAGRAPH_NAME
```

### `SqlErrorGenerator.ensure_sql_error_paragraph` - L90-L92

```python
ensure_sql_error_paragraph(self, text: str) -> str
```

Called by orchestration/conversion/conversion_pipeline.py.

Observed calls (lexical order): `self.ensure_paragraph`.

### `SqlErrorGenerator.__init__` - L96-L97

```python
__init__(self) -> None
```

### `SqlErrorGenerator.paragraph_block` - L102-L104

```python
paragraph_block(self) -> str
```

The generated SQLERROR routine as one text block.

Observed calls (lexical order): `'\n'.join`, `self.paragraph_lines`.

### `SqlErrorGenerator.paragraph_lines` - L106-L120

```python
paragraph_lines(self) -> list[str]
```

The generated SQLERROR routine as body lines.

Observed calls (lexical order): `lines.append`.

Control points:

- L114: `if EMIT_SQL_ERROR_PARAGRAPH_HEADER`

### `SqlErrorGenerator.ensure_paragraph` - L125-L146

```python
ensure_paragraph(self, text: str) -> str
```

Normalise legacy names, then guarantee one SQLERROR routine.

Observed calls (lexical order): `self.rename_legacy`, `str`, `output.strip`, `self._has_sqlerror_paragraph`, `self._replace_existing_sqlerror_paragraph`, `self.messages.append`, `self._has_sqlerror_include`, `self._append_routine`.

Control points:

- L130: `if not output.strip()`
- L135: `if self._has_sqlerror_paragraph(output)`
- L140: `if self._has_sqlerror_include(output)`

### `SqlErrorGenerator.ensure` - L149-L150

```python
ensure(self, text: str) -> str
```

Observed calls (lexical order): `self.ensure_paragraph`.

### `SqlErrorGenerator._append_routine` - L152-L160

```python
_append_routine(self, text: str) -> str
```

Observed calls (lexical order): `self.paragraph_block`, `END_PROGRAM_PATTERN.search`, `match.start`, `text.rstrip`.

Control points:

- L156: `if match`

### `SqlErrorGenerator.rename_legacy` - L165-L198

```python
rename_legacy(self, text: str) -> str
```

Rename SQL-ERROR to SQLERROR without touching terminators.

Observed calls (lexical order): `str`, `LEGACY_SQL_ERROR_HEADER_PATTERN.subn`, `LEGACY_SQL_ERROR_PERFORM_PATTERN.subn`, `self.messages.append`, `SQL_ERROR_MESSAGES['renamed_legacy'].format`.

Control points:

- L168: `if not output`
- L190: `if header_count or perform_count`

### `SqlErrorGenerator.rename_legacy._perform` - L181-L183

```python
_perform(match: re.Match) -> str
```

Observed calls (lexical order): `match.group`.

### `SqlErrorGenerator._has_sqlerror_paragraph` - L203-L204

```python
_has_sqlerror_paragraph(self, text: str) -> bool
```

Observed calls (lexical order): `SQLERROR_PARAGRAPH_PATTERN.search`, `bool`, `str`.

### `SqlErrorGenerator._has_sqlerror_include` - L207-L210

```python
_has_sqlerror_include(text: str) -> bool
```

Observed calls (lexical order): `f'INCLUDE {SQL_ERROR_INCLUDE_NAME}'.upper`, `str`, `str(text or '').upper`.

### `SqlErrorGenerator._is_sqlerror_paragraph_header` - L212-L214

```python
_is_sqlerror_paragraph_header(self, line: str) -> bool
```

Observed calls (lexical order): `self._logical_line`, `SQLERROR_HEADER_ONLY_PATTERN.fullmatch`, `bool`.

### `SqlErrorGenerator._is_next_paragraph_or_program_boundary` - L216-L223

```python
_is_next_paragraph_or_program_boundary(self, line: str) -> bool
```

True when the scan has run past the old SQLERROR body.

Observed calls (lexical order): `self._logical_line`, `END_PROGRAM_BOUNDARY_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.fullmatch`, `bool`.

Control points:

- L219: `if not logical`
- L221: `if END_PROGRAM_BOUNDARY_PATTERN.match(logical)`

### `SqlErrorGenerator._line_belongs_to_old_sqlerror_block` - L225-L230

```python
_line_belongs_to_old_sqlerror_block(self, line: str) -> bool
```

True for a body line of a previously generated SQLERROR block.

Observed calls (lexical order): `self._logical_line`, `self._logical_line(line).upper`, `any`.

Control points:

- L228: `if not logical`

### `SqlErrorGenerator._replace_existing_sqlerror_paragraph` - L235-L272

```python
_replace_existing_sqlerror_paragraph(self, text: str) -> str
```

Swap any existing SQLERROR body for the generated routine.

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `len`, `self._is_sqlerror_paragraph_header`, `output.append`, `output.extend`, `self.paragraph_lines`, `self._is_next_paragraph_or_program_boundary`, `self._line_belongs_to_old_sqlerror_block`, `current.strip`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L242: `while index < len(lines)`
- L245: `if not self._is_sqlerror_paragraph_header(line)`
- L256: `while index < len(lines)`
- L259: `if self._is_next_paragraph_or_program_boundary(current)`
- L261: `if self._line_belongs_to_old_sqlerror_block(current)`
- L264: `if not current.strip()`
- L269: `if not replaced`

### `SqlErrorGenerator._logical_line` - L278-L298

```python
_logical_line(line: str) -> str
```

Strip sequence numbers and the indicator, return the body.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(line or '').rstrip('\n').rstrip`, `len`, `text[:LEFT_SEQUENCE_WIDTH].isdigit`, `text[FIXED_LINE_WIDTH - RIGHT_SEQUENCE_WIDTH:FIXED_LINE_WIDTH].isdigit`, `text[LEFT_SEQUENCE_WIDTH + 1:FIXED_LINE_WIDTH - RIGHT_SEQUENCE_WIDTH].strip`, `text[LEFT_SEQUENCE_WIDTH:].strip`, `text.strip`.

Control points:

- L281: `if not text`
- L284: `if len(text) >= FIXED_LINE_WIDTH and text[:LEFT_SEQUENCE_WIDTH].isdigit() and text[FIXED_LINE_WIDTH - RIGHT_SEQUENCE_WIDTH:FIXED_LINE_WIDTH].isdigit()`
- L295: `if text[:LEFT_SEQUENCE_WIDTH].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
