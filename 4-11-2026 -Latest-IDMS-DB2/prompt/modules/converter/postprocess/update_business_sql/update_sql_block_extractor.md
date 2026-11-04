# `converter/postprocess/update_business_sql/update_sql_block_extractor.py`

Source: [converter/postprocess/update_business_sql/update_sql_block_extractor.py](../../../../../converter/postprocess/update_business_sql/update_sql_block_extractor.py) | 641 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `0fd6b75e72f80f805ca9c1f2933feb69c71caaed439c58f5b67f01029a4e2b7d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`SENTENCE_TERMINATOR` (L43), `__all__` (L641)

## Import declarations

```python
from __future__ import annotations
from patterns.update_business_sql_patterns import CONTINUE_PATTERN, CONVERTED_MODIFY_COMMENT_PATTERN, DCL_HOST_GROUP_PATTERN, END_EVALUATE_PATTERN, END_EXEC_PATTERN, EVALUATE_SQLCODE_PATTERN, EXEC_SQL_START_PATTERN, EXEC_SQL_UPDATE_PATTERN, PARAGRAPH_HEADER_PATTERN, SQL_LOCATION_UPDATE_PATTERN, WHEN_ZERO_PATTERN
from rules.update_business_sql_rules import ADD_UPDATE_COUNTER_TEMPLATE, COMMIT_CHECK_IF_TEMPLATE, COMMIT_CHECK_PERFORM_TEMPLATE, END_IF_STATEMENT, FINAL_PERIOD_LINE, INITIALIZE_DCL_GROUP_TEMPLATE, NESTED_INDENT, PERFORM_TEMPLATE, SQL_ERROR_PARAGRAPH_NAMES, SQL_ERROR_ROUTINE_MARKER, TOKEN_STAR, DCLGEN_GROUP_PREFIX, DCLGEN_GROUP_SUFFIXES, ENABLE_STRUCTURAL_UPDATE_DETECTION, UPDATE_VERB_LOOKAHEAD
from rules.update_restart_rules import RESTART_PARAGRAPH_NAMES, UPDATE_COMMIT_THRESHOLD, UPDATE_RESTART_DIAGNOSTICS, UPDATE_RESTART_WS_NAMES
```

## Local dependency notes

- [patterns/update_business_sql_patterns.py](../../../patterns/update_business_sql_patterns.md)
- [rules/update_business_sql_rules.py](../../../rules/update_business_sql_rules.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_business_sql_standardizer.py](../update_business_sql_standardizer.md)
- [tests/update_business_sql/test_structural_update_detection.py](../../../tests/update_business_sql/test_structural_update_detection.md)

## Symbol contracts and control points

### `UpdateSqlBlockExtractor` - L46-L638

```python
class UpdateSqlBlockExtractor()
```

Detects and extracts the inline generated UPDATE SQL block.

### `UpdateSqlBlockExtractor._extract_inline_update_block` - L133-L188

```python
_extract_inline_update_block(self, *, lines, process_paragraph, block_info, diagnostics)
```

Observed calls (lexical order): `self._update_paragraph_name`, `self._paragraph_exists`, `diagnostics.append`, `self._replace_update_success_continue`, `self._replacement_in_process`, `self._restart_owns_commit`, `self.line_utils.find_paragraph_range`, `self._ensure_initialize_dcl_group`, `self._build_update_paragraph`, `self._update_paragraph_insert_index`.

Control points:

- L139: `if self._paragraph_exists(lines, update_paragraph)`
- L159: `if process_range`

### `UpdateSqlBlockExtractor._find_inline_update_block` - L190-L261

```python
_find_inline_update_block(self, *, lines, start, end, diagnostics=None, paragraph='')
```

Locate the inline business UPDATE block, or refuse and say so.

Observed calls (lexical order): `range`, `self._logical`, `CONVERTED_MODIFY_COMMENT_PATTERN.match`, `SQL_LOCATION_UPDATE_PATTERN.match`, `comment_match.group`, `str`, `str(comment_match.group('record') or '').strip`, `str(comment_match.group('record') or '').strip().upper`, `location_match.group`, `str(location_match.group('record') or '').strip`, `str(location_match.group('record') or '').strip().upper`, `self._find_sqlcode_evaluate_end`, `self._find_dcl_group`, `self._find_update_block_by_structure`, `self._say`.

Control points:

- L220: `for index in range(start + 1, end)`
- L224: `if not comment_match and (not location_match)`
- L228: `if comment_match`
- L230: `if not record_name and location_match`
- L232: `if not record_name`
- L236: `if location_match and index > start + 1`
- L238: `if CONVERTED_MODIFY_COMMENT_PATTERN.match(previous_logical)`
- L244: `if block_end <= index`
- Another 1 conditions/loops exist in this source span.

### `UpdateSqlBlockExtractor._find_update_block_by_structure` - L263-L287

```python
_find_update_block_by_structure(self, *, lines, start, end)
```

The UPDATE block read from its own shape. No comment needed.

Observed calls (lexical order): `range`, `EXEC_SQL_START_PATTERN.match`, `self._logical`, `self._opens_an_update`, `self._find_sqlcode_evaluate_end`, `self._find_dcl_group`, `self._record_from_group`.

Control points:

- L265: `if not ENABLE_STRUCTURAL_UPDATE_DETECTION`
- L268: `for index in range(start + 1, end)`
- L269: `if not EXEC_SQL_START_PATTERN.match(self._logical(lines[index]))`
- L271: `if not self._opens_an_update(lines=lines, index=index, end=end)`
- L277: `if block_end <= index`
- L282: `if not record_name`

### `UpdateSqlBlockExtractor._opens_an_update` - L289-L298

```python
_opens_an_update(self, *, lines, index, end)
```

True when this EXEC SQL begins an UPDATE statement.

Observed calls (lexical order): `min`, `range`, `self._logical`, `EXEC_SQL_UPDATE_PATTERN.match`, `END_EXEC_PATTERN.match`.

Control points:

- L292: `for position in range(index + 1, limit)`
- L294: `if EXEC_SQL_UPDATE_PATTERN.match(logical)`
- L296: `if END_EXEC_PATTERN.match(logical)`

### `UpdateSqlBlockExtractor._record_from_group` - L301-L315

```python
_record_from_group(dcl_group)
```

DCLDZBFARTV -> DZBFAR. Derived, never invented.

Observed calls (lexical order): `str`, `str(dcl_group or '').strip`, `str(dcl_group or '').strip().upper`, `name.startswith`, `len`, `name.endswith`.

Control points:

- L309: `if not name.startswith(DCLGEN_GROUP_PREFIX)`
- L312: `for suffix in DCLGEN_GROUP_SUFFIXES`
- L313: `if name.endswith(suffix) and len(name) > len(suffix)`

### `UpdateSqlBlockExtractor._say` - L318-L329

```python
_say(diagnostics, key, **values)
```

Report, or stay silent only because no collector was given.

Observed calls (lexical order): `UPDATE_RESTART_DIAGNOSTICS.get`, `diagnostics.append`, `template.format`.

Control points:

- L320: `if diagnostics is None`
- L323: `if not template`

### `UpdateSqlBlockExtractor._find_sqlcode_evaluate_end` - L334-L354

```python
_find_sqlcode_evaluate_end(self, *, lines, start, limit)
```

Observed calls (lexical order): `range`, `self._logical`, `EXEC_SQL_START_PATTERN.match`, `EXEC_SQL_UPDATE_PATTERN.match`, `END_EXEC_PATTERN.match`, `EVALUATE_SQLCODE_PATTERN.match`, `END_EVALUATE_PATTERN.match`, `self._sentence_end`.

Control points:

- L337: `for index in range(start, limit)`
- L339: `if EXEC_SQL_START_PATTERN.match(logical)`
- L342: `if seen_exec_sql and EXEC_SQL_UPDATE_PATTERN.match(logical)`
- L345: `if seen_update and END_EXEC_PATTERN.match(logical)`
- L348: `if seen_end_exec and EVALUATE_SQLCODE_PATTERN.match(logical)`
- L351: `if seen_evaluate and END_EVALUATE_PATTERN.match(logical)`

### `UpdateSqlBlockExtractor._sentence_end` - L356-L388

```python
_sentence_end(self, *, lines, index, limit)
```

End of the SENTENCE that closed at `index`. See CORRECTION 4.

Observed calls (lexical order): `min`, `self._is_comment_line`, `' '.join`, `self._logical`, `str`, `str(self._logical(lines[cursor]) or '').split`, `str(self._logical(lines[cursor]) or '').strip`.

Control points:

- L371: `while cursor < limit`
- L372: `if self._is_comment_line(lines[cursor])`
- L375: `if not body`
- L377: `if body == SENTENCE_TERMINATOR`
- L381: `while cursor < limit`
- L382: `if self._is_comment_line(lines[cursor])`
- L384: `if str(self._logical(lines[cursor]) or '').strip()`

### `UpdateSqlBlockExtractor._replacement_in_process` - L393-L450

```python
_replacement_in_process(self, *, reference_line, update_paragraph, restart_owns_commit: bool=False, diagnostics=None)
```

The call site that replaces the extracted inline UPDATE.

Observed calls (lexical order): `self._active_line_like`, `PERFORM_TEMPLATE.format`, `self._say`, `output.append`, `output.extend`, `COMMIT_CHECK_IF_TEMPLATE.format`, `COMMIT_CHECK_PERFORM_TEMPLATE.format`.

Control points:

- L422: `if restart_owns_commit`

### `UpdateSqlBlockExtractor._restart_owns_commit` - L452-L491

```python
_restart_owns_commit(self, lines) -> bool
```

True when the restart family already performs the commit paragraph.

Observed calls (lexical order): `RESTART_PARAGRAPH_NAMES.get`, `str`, `str(RESTART_PARAGRAPH_NAMES.get('commit', '') or '').upper`, `self._is_comment_line`, `' '.join`, `self._logical`, `str(self._logical(line) or '').upper`, `str(self._logical(line) or '').upper().split`.

Control points:

- L475: `if not commit`
- L480: `for line in lines or []`
- L481: `if self._is_comment_line(line)`
- L485: `if not logical`
- L488: `if target in logical`

### `UpdateSqlBlockExtractor._build_update_paragraph` - L493-L498

```python
_build_update_paragraph(self, *, paragraph_name, extracted_block)
```

Observed calls (lexical order): `self._strip_existing_final_period`, `output.extend`, `output.append`, `self._normalize_update_paragraph_lines`.

### `UpdateSqlBlockExtractor._replace_update_success_continue` - L500-L530

```python
_replace_update_success_continue(self, *, extracted_block)
```

Observed calls (lexical order): `len`, `self._logical`, `WHEN_ZERO_PATTERN.match`, `output.append`, `CONTINUE_PATTERN.match`, `self._active_line_like`, `ADD_UPDATE_COUNTER_TEMPLATE.format`.

Control points:

- L505: `while index < len(extracted_block)`
- L509: `if WHEN_ZERO_PATTERN.match(logical)`
- L511: `if index + 1 < len(extracted_block)`
- L513: `if CONTINUE_PATTERN.match(next_logical)`

### `UpdateSqlBlockExtractor._ensure_initialize_dcl_group` - L535-L579

```python
_ensure_initialize_dcl_group(self, *, lines, start, end, dcl_group, diagnostics=None)
```

Observed calls (lexical order): `notes.append`, `self._initialize_key`, `INITIALIZE_DCL_GROUP_TEMPLATE.format`, `range`, `self._logical`, `self._first_executable_line_index`, `self._active_line_like`.

Control points:

- L540: `if not dcl_group`
- L553: `for index in range(start, end)`
- L554: `if self._initialize_key(self._logical(lines[index])) == wanted`
- L564: `if insert_index < 0`

### `UpdateSqlBlockExtractor._initialize_key` - L582-L591

```python
_initialize_key(text)
```

Whitespace- and terminator-insensitive comparison key.

Observed calls (lexical order): `' '.join`, `str`, `str(text or '').split`, `collapsed.upper`, `collapsed.upper().rstrip`, `collapsed.upper().rstrip(SENTENCE_TERMINATOR).strip`.

### `UpdateSqlBlockExtractor._first_executable_line_index` - L593-L604

```python
_first_executable_line_index(self, *, lines, start, end)
```

Observed calls (lexical order): `range`, `self._logical`, `self._logical(line).strip`, `self._is_comment_line`, `logical.startswith`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L594: `for index in range(start + 1, end)`
- L597: `if not logical or self._is_comment_line(line)`
- L599: `if logical.startswith(TOKEN_STAR)`
- L601: `if PARAGRAPH_HEADER_PATTERN.match(logical)`

### `UpdateSqlBlockExtractor._update_paragraph_insert_index` - L609-L620

```python
_update_paragraph_insert_index(self, lines)
```

Observed calls (lexical order): `self._find_sqlerror_routine_index`, `self.line_utils.find_paragraph_range`, `len`.

Control points:

- L611: `if sqlerror_index >= 0`
- L617: `if restart_abend_range`

### `UpdateSqlBlockExtractor._find_sqlerror_routine_index` - L622-L629

```python
_find_sqlerror_routine_index(self, lines)
```

Observed calls (lexical order): `enumerate`, `self._logical`, `self._logical(line).upper`, `self._logical(line).upper().rstrip`, `set`.

Control points:

- L623: `for (index, line) in enumerate(lines)`
- L625: `if logical in set(SQL_ERROR_PARAGRAPH_NAMES)`
- L627: `if SQL_ERROR_ROUTINE_MARKER in logical`

### `UpdateSqlBlockExtractor._find_dcl_group` - L631-L638

```python
_find_dcl_group(self, lines)
```

Observed calls (lexical order): `self._logical`, `DCL_HOST_GROUP_PATTERN.finditer`, `match.group`, `str`, `str(match.group(0) or '').strip`, `str(match.group(0) or '').strip().upper`.

Control points:

- L632: `for line in lines`
- L634: `for match in DCL_HOST_GROUP_PATTERN.finditer(logical)`
- L636: `if group`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
