# `converter/postprocess/update_business_sql_standardizer.py`

Source: [converter/postprocess/update_business_sql_standardizer.py](../../../../converter/postprocess/update_business_sql_standardizer.py) | 270 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `074b1403e236c0e11189c9063d9a995410877f6ccc6b067bf7bb9b4f95ff3f0a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.dynamic_metadata_resolver import UpdateProgramContext
from converter.postprocess.update_business_sql.update_business_sql_line_renderer import UpdateBusinessSqlLineRenderer
from converter.postprocess.update_business_sql.update_paragraph_normalizer import UpdateParagraphNormalizer
from converter.postprocess.update_business_sql.update_sql_block_extractor import UpdateSqlBlockExtractor
from converter.postprocess.update_postprocess_line_utils import UpdatePostprocessLineUtils
from patterns.update_business_sql_patterns import CONVERTED_MODIFY_COMMENT_PATTERN, PERFORM_UPDATE_PARAGRAPH_PATTERN
from patterns.update_main_flow_patterns import PERFORM_UNTIL_LINE_PATTERN
from rules.update_business_sql_rules import DIAG_PROCESS_PARAGRAPH_NOT_FOUND_TEMPLATE, DIAG_PROCESS_PARAGRAPH_UNRESOLVED, LONE_PERIOD, NESTED_INDENT, READ_FLAT_FILE_PARAGRAPH, TOKEN_END_IF, TOKEN_IF, TOKEN_INITIALIZE_DCL, TOKEN_PERFORM
from rules.update_restart_rules import UPDATE_RESTART_DIAGNOSTICS, UPDATE_RESTART_WS_NAMES, UPDATE_SQL_PARAGRAPH_PREFIX
from converter.postprocess.update_business_sql.update_counter_declarer import UpdateCounterDeclarer
```

## Local dependency notes

- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)
- [converter/postprocess/update_business_sql/update_business_sql_line_renderer.py](update_business_sql/update_business_sql_line_renderer.md)
- [converter/postprocess/update_business_sql/update_counter_declarer.py](update_business_sql/update_counter_declarer.md)
- [converter/postprocess/update_business_sql/update_paragraph_normalizer.py](update_business_sql/update_paragraph_normalizer.md)
- [converter/postprocess/update_business_sql/update_sql_block_extractor.py](update_business_sql/update_sql_block_extractor.md)
- [converter/postprocess/update_postprocess_line_utils.py](update_postprocess_line_utils.md)
- [patterns/update_business_sql_patterns.py](../../patterns/update_business_sql_patterns.md)
- [patterns/update_main_flow_patterns.py](../../patterns/update_main_flow_patterns.md)
- [rules/update_business_sql_rules.py](../../rules/update_business_sql_rules.md)
- [rules/update_restart_rules.py](../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `UpdateBusinessSqlStandardizer` - L42-L270

```python
class UpdateBusinessSqlStandardizer(UpdateBusinessSqlLineRenderer, UpdateParagraphNormalizer, UpdateSqlBlockExtractor)
```

Standardizes update-program business SQL structure.

### `UpdateBusinessSqlStandardizer.__init__` - L56-L57

```python
__init__(self, *, line_utils: UpdatePostprocessLineUtils) -> None
```

### `UpdateBusinessSqlStandardizer.standardize` - L59-L117

```python
standardize(self, cobol_text: str, context: UpdateProgramContext, diagnostics: list[str]) -> str
```

Observed calls (lexical order): `diagnostics.append`, `getattr`, `self.line_utils.lines`, `self._resolve_process_paragraph`, `self.line_utils.find_paragraph_range`, `DIAG_PROCESS_PARAGRAPH_NOT_FOUND_TEMPLATE.format`, `self._find_inline_update_block`, `self._extract_inline_update_block`, `self._paragraph_contains_update_perform`, `UpdateCounterDeclarer`, `UpdateCounterDeclarer(self.line_utils).ensure`, `self._cleanup_process_paragraph`, `self._normalize_all_update_paragraphs`, `self.line_utils.join`.

Control points:

- L65: `if not context.restart_dclgen`
- L82: `if not process_paragraph`
- L87: `if not paragraph_range`
- L98: `if block_info`
- L105: `if not self._paragraph_contains_update_perform(lines=lines, start=start, end=end)`

### `UpdateBusinessSqlStandardizer._cleanup_process_paragraph` - L119-L151

```python
_cleanup_process_paragraph(self, *, lines, process_paragraph)
```

Observed calls (lexical order): `self.line_utils.find_paragraph_range`, `enumerate`, `output.append`, `self._logical`, `self._logical(line).strip`, `logical.upper`, `logical.upper().rstrip`, `self._is_comment_line`, `upper.startswith`, `self._active_line_like`, `CONVERTED_MODIFY_COMMENT_PATTERN.match`, `self._normalize_process_commit_block`.

Control points:

- L121: `if not paragraph_range`
- L127: `for (index, line) in enumerate(lines)`
- L128: `if not start < index < end`
- L135: `if upper.startswith(TOKEN_INITIALIZE_DCL) and self._is_comment_line(line)`
- L141: `if CONVERTED_MODIFY_COMMENT_PATTERN.match(logical)`
- L147: `if not paragraph_range`

### `UpdateBusinessSqlStandardizer._normalize_process_commit_block` - L153-L188

```python
_normalize_process_commit_block(self, *, lines, start, end)
```

Observed calls (lexical order): `list`, `self._logical`, `self._logical(output[index]).upper`, `self._logical(output[index]).upper().rstrip`, `logical.startswith`, `self._find_end_if`, `range`, `self._logical(output[block_index]).strip`, `body.upper`, `body.upper().startswith`, `self._active_line_like`, `body.rstrip`.

Control points:

- L157: `while index < end`
- L160: `if not logical.startswith(TOKEN_IF)`
- L163: `if UPDATE_RESTART_WS_NAMES['commit_counter'] not in logical`
- L168: `if block_end < 0`
- L172: `for block_index in range(index, block_end + 1)`
- L174: `if not body`
- L176: `if body.upper().startswith(TOKEN_PERFORM)`

### `UpdateBusinessSqlStandardizer._find_end_if` - L190-L195

```python
_find_end_if(self, *, lines, start, limit)
```

Observed calls (lexical order): `range`, `self._logical`, `self._logical(lines[index]).upper`, `self._logical(lines[index]).upper().rstrip`, `logical.startswith`.

Control points:

- L191: `for index in range(start + 1, limit)`
- L193: `if logical.startswith(TOKEN_END_IF)`

### `UpdateBusinessSqlStandardizer._resolve_process_paragraph` - L197-L245

```python
_resolve_process_paragraph(self, *, lines, input_record_name, diagnostics=None)
```

The driving paragraph of the record loop.

Observed calls (lexical order): `str`, `str(input_record_name or '').strip`, `str(input_record_name or '').strip().upper`, `self._logical`, `self._logical(line).upper`, `self._logical(line).upper().rstrip`, `PERFORM_UNTIL_LINE_PATTERN.search`, `match.group`, `str(match.group('paragraph') or '').strip`, `str(match.group('paragraph') or '').strip().upper`, `diagnostics.append`.

Control points:

- L218: `for line in lines`
- L221: `if not match`
- L225: `if not paragraph or paragraph == READ_FLAT_FILE_PARAGRAPH`
- L228: `if target_eof and target_eof in logical`
- L231: `if not fallback and '-EOF' in logical`
- L235: `if fallback`
- L236: `if diagnostics is not None`

### `UpdateBusinessSqlStandardizer._paragraph_contains_update_perform` - L247-L251

```python
_paragraph_contains_update_perform(self, *, lines, start, end)
```

Observed calls (lexical order): `range`, `PERFORM_UPDATE_PARAGRAPH_PATTERN.match`, `self._logical`.

Control points:

- L248: `for index in range(start + 1, end)`
- L249: `if PERFORM_UPDATE_PARAGRAPH_PATTERN.match(self._logical(lines[index]))`

### `UpdateBusinessSqlStandardizer._paragraph_exists` - L253-L258

```python
_paragraph_exists(self, lines, paragraph_name)
```

Observed calls (lexical order): `str`, `str(paragraph_name or '').strip`, `str(paragraph_name or '').strip().upper`, `str(paragraph_name or '').strip().upper().rstrip`, `self._logical`, `self._logical(line).upper`, `self._logical(line).upper().rstrip`.

Control points:

- L255: `for line in lines`
- L256: `if self._logical(line).upper().rstrip('.') == target`

### `UpdateBusinessSqlStandardizer._update_paragraph_name` - L260-L262

```python
_update_paragraph_name(self, record_name)
```

Observed calls (lexical order): `str`, `str(record_name or '').strip`, `str(record_name or '').strip().upper`, `str(record_name or '').strip().upper().replace`.

### `UpdateBusinessSqlStandardizer._strip_existing_final_period` - L264-L270

```python
_strip_existing_final_period(self, lines)
```

Observed calls (lexical order): `list`, `self._logical`, `output.pop`.

Control points:

- L266: `while output and (not self._logical(output[-1]))`
- L268: `if output and self._logical(output[-1]) == LONE_PERIOD`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
