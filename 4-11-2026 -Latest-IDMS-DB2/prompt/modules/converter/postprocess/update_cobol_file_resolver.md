# `converter/postprocess/update_cobol_file_resolver.py`

Source: [converter/postprocess/update_cobol_file_resolver.py](../../../../converter/postprocess/update_cobol_file_resolver.py) | 409 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `94dab002843d83418fc1502ca9ec1c559f4a0d17ad2383ac2d58fb8894390db6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`EOF_MARKER` (L31), `EOF_TAIL_WINDOW` (L32)

## Import declarations

```python
from __future__ import annotations
from typing import Optional
from converter.postprocess.update_metadata_models import CobolFileInfo, norm_name, upper
from patterns.dynamic_metadata_patterns import COPY_RE, DECLARED_88_RE, EOF_ANY_MOVE_RE, EOF_CONDITION_REF_RE, FD_LINE_RE, FD_RECORD_01_RE, FIELD_USE_RE, MOVE_FIELD_RE, PROGRAM_RE, QUALIFIER_RE, READ_LINE_RE, READ_RE, RECORD_CONTAINS_RE, RELATIONAL_HEAD_RE, SECTION_END_RE, SELECT_LINE_RE, SELECT_RE
```

## Local dependency notes

- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)
- [patterns/dynamic_metadata_patterns.py](../../patterns/dynamic_metadata_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)

## Symbol contracts and control points

### `UpdateCobolFileResolver` - L34-L409

```python
class UpdateCobolFileResolver()
```

### `UpdateCobolFileResolver.resolve_program_id` - L35-L49

```python
resolve_program_id(self, *, generated_cobol: str, source_cobol: str, target_program_id: str) -> str
```

Observed calls (lexical order): `self.logical_statement_text`, `PROGRAM_RE.search`, `match.group`, `upper`.

Control points:

- L42: `for text in [generated_cobol, source_cobol]`
- L46: `if match`

### `UpdateCobolFileResolver.parse_cobol_files` - L51-L69

```python
parse_cobol_files(self, *, source_cobol: str, generated_cobol: str) -> dict[str, CobolFileInfo]
```

Observed calls (lexical order): `self._parse_from_logical_text`, `self._parse_from_physical_lines`.

Control points:

- L59: `for raw_text in [source_cobol, generated_cobol]`

### `UpdateCobolFileResolver.choose_input_file` - L71-L83

```python
choose_input_file(self, files: dict[str, CobolFileInfo]) -> CobolFileInfo
```

Observed calls (lexical order): `files.values`, `iter`, `next`.

Control points:

- L76: `if read_files`
- L80: `if fd_files`

### `UpdateCobolFileResolver.extract_copy_statements` - L85-L94

```python
extract_copy_statements(self, text: str) -> set[str]
```

Observed calls (lexical order): `self.logical_statement_text`, `match.group`, `norm_name`, `COPY_RE.finditer`.

### `UpdateCobolFileResolver.extract_source_field_references` - L96-L109

```python
extract_source_field_references(self, source_cobol: str) -> set[str]
```

Observed calls (lexical order): `set`, `self.logical_statement_text`, `FIELD_USE_RE.finditer`, `match.group`, `norm_name`, `refs.add`, `MOVE_FIELD_RE.finditer`.

Control points:

- L103: `for match in FIELD_USE_RE.finditer(logical_text)`
- L106: `for match in MOVE_FIELD_RE.finditer(logical_text)`

### `UpdateCobolFileResolver.resolve_legacy_eof_switch` - L111-L242

```python
resolve_legacy_eof_switch(self, *, source_cobol: str, generated_cobol: str) -> str
```

The end-of-file CONDITION NAME the SOURCE program used.

Observed calls (lexical order): `self.logical_statement_text`, `match.group`, `norm_name`, `DECLARED_88_RE.finditer`, `EOF_CONDITION_REF_RE.finditer`, `match.end`, `tail.split`, `QUALIFIER_RE.match`, `qualified.end`, `RELATIONAL_HEAD_RE.match`, `_offer`, `EOF_ANY_MOVE_RE.finditer`, `sorted`, `bucket.items`.

Control points:

- L205: `for match in EOF_CONDITION_REF_RE.finditer(source_text)`
- L222: `while qualified`
- L226: `if RELATIONAL_HEAD_RE.match(tail)`
- L231: `for match in EOF_ANY_MOVE_RE.finditer(source_text)`
- L234: `for bucket in (conditions, switches)`
- L235: `if bucket`

### `UpdateCobolFileResolver.resolve_legacy_eof_switch._offer` - L194-L203

```python
_offer(bucket: dict[str, int], raw_name: str) -> None
```

Observed calls (lexical order): `norm_name`, `bucket.get`.

Control points:

- L197: `if not name or EOF_MARKER not in name`
- L200: `if name in generated_only_conditions`

### `UpdateCobolFileResolver._parse_from_logical_text` - L244-L265

```python
_parse_from_logical_text(self, *, files: dict[str, CobolFileInfo], raw_text: str) -> None
```

Observed calls (lexical order): `self.logical_statement_text`, `SELECT_RE.finditer`, `match.group`, `upper`, `CobolFileInfo`, `files.setdefault`, `READ_RE.finditer`.

Control points:

- L252: `for match in SELECT_RE.finditer(text)`
- L257: `for match in READ_RE.finditer(text)`
- L261: `if read_target`

### `UpdateCobolFileResolver._parse_from_physical_lines` - L267-L325

```python
_parse_from_physical_lines(self, *, files: dict[str, CobolFileInfo], raw_text: str) -> None
```

Observed calls (lexical order): `str`, `str(raw_text or '').splitlines`, `self.fixed_format_body_line`, `self.fixed_format_body_line(raw_line).strip`, `SELECT_LINE_RE.search`, `select_match.group`, `upper`, `files.setdefault`, `CobolFileInfo`, `FD_LINE_RE.search`, `fd_match.group`, `RECORD_CONTAINS_RE.search`, `int`, `length_match.group`, `FD_RECORD_01_RE.search`, `record_match.group`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L275: `for raw_line in str(raw_text or '').splitlines()`
- L278: `if not line`
- L283: `if select_match`
- L294: `if fd_match`
- L299: `if current_fd`
- L302: `if length_match`
- L308: `if record_match`
- L312: `if SECTION_END_RE.search(line)`
- Another 2 conditions/loops exist in this source span.

### `UpdateCobolFileResolver.fixed_format_body_text` - L327-L344

```python
fixed_format_body_text(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `self.fixed_format_body_line`, `body.lstrip`, `body.lstrip().startswith`, `output.append`, `'\n'.join`.

Control points:

- L333: `for raw_line in str(text or '').splitlines()`
- L336: `if not body`
- L339: `if body.lstrip().startswith('*') or body.lstrip().startswith('/')`

### `UpdateCobolFileResolver.fixed_format_body_line` - L346-L374

```python
fixed_format_body_line(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `text.strip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[7:72].strip`, `body[-8:].strip`, `body[-8:].strip().isdigit`, `body.strip`.

Control points:

- L352: `if not text.strip()`
- L355: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L358: `if indicator in ('*', '/')`
- L363: `if len(text) > 6 and text[:6].strip().isdigit()`
- L366: `if len(body) >= 8 and body[-8:].strip().isdigit()`
- L369: `if body[:1] in ('*', '/', 'D')`

### `UpdateCobolFileResolver.logical_statement_text` - L376-L409

```python
logical_statement_text(self, text: str) -> str
```

Observed calls (lexical order): `self.fixed_format_body_text`, `body_text.splitlines`, `raw_line.strip`, `buffer.split`, `part.strip`, `statements.append`, `parts[-1].strip`, `'\n'.join`.

Control points:

- L384: `for raw_line in body_text.splitlines()`
- L387: `if not line`
- L390: `if buffer`
- L395: `if '.' in line`
- L398: `for part in parts[:-1]`
- L401: `if clean`
- L406: `if buffer`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
