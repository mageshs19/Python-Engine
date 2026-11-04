# `converter/composers/update_sql_cleanup/modify_update_rewriter.py`

Source: [converter/composers/update_sql_cleanup/modify_update_rewriter.py](../../../../../converter/composers/update_sql_cleanup/modify_update_rewriter.py) | 510 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `4587c0447edcc6a9e58a517a6ac55abe89d3a8a5e8bdb054bae47211b29201c8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Rewrites generated MODIFY markers into conservative DB2 UPDATE blocks.

## Import declarations

```python
from __future__ import annotations
from converter.composers.update_sql_cleanup.composer_patterns import ANY_DCL_DOT_REFERENCE_PATTERN, ANY_DCL_OF_REFERENCE_PATTERN, MOVE_TO_DCL_DOT_HOST_PATTERN, STRING_INTO_DCL_DOT_HOST_PATTERN, STRING_INTO_DCL_HOST_PATTERN
from converter.generators.db2_infrastructure.sql_location_move_builder import SqlLocationMoveBuilder
from converter.services.name_normalizer import NameNormalizer
from patterns.cobol_cleanup_patterns import PARAGRAPH_HEADER_PATTERN
from rules.cobol_paragraph_scan_rules import NON_PARAGRAPH_SENTENCE_WORDS, PARAGRAPH_SCAN_LIMIT
from rules.sql_location_rules import LEGACY_OPERATION_UPDATE, LEGACY_RECORD_LOCATION_TEMPLATE
from rules.update_sql_cleanup_rules import UPDATE_QUERYNO
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/composer_patterns.py](composer_patterns.md)
- [converter/generators/db2_infrastructure/sql_location_move_builder.py](../../generators/db2_infrastructure/sql_location_move_builder.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)
- [rules/cobol_paragraph_scan_rules.py](../../../rules/cobol_paragraph_scan_rules.md)
- [rules/sql_location_rules.py](../../../rules/sql_location_rules.md)
- [rules/update_sql_cleanup_rules.py](../../../rules/update_sql_cleanup_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup_composer.py](../update_sql_cleanup_composer.md)
- [tests/test_lrf_update_changed_column_scope.py](../../../tests/test_lrf_update_changed_column_scope.md)

## Symbol contracts and control points

### `ModifyUpdateRewriter` - L29-L510

```python
class ModifyUpdateRewriter()
```

### `ModifyUpdateRewriter.__init__` - L30-L32

```python
__init__(self, owner, scanner) -> None
```

### `ModifyUpdateRewriter.rewrite` - L34-L92

```python
rewrite(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `len`, `self.owner._logical`, `self.owner.CONVERTED_MODIFY_PATTERN.match`, `output.append`, `NameNormalizer.normalize`, `match.group`, `self.owner._table_for_record`, `self.owner._db2_primary_key_columns`, `self._changed_columns_after_obtain_calc`, `self._update_columns`, `self.scanner.skip_generated_sql_and_sqlcode`, `output.extend`, `self._conservative_update_block`, `self.owner._leading_spaces`, `self._enclosing_paragraph`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L40: `while index < len(lines)`
- L44: `if not match`
- L65: `if not table or not key_columns or (not update_columns)`
- L86: `if changed`

### `ModifyUpdateRewriter._enclosing_paragraph` - L94-L144

```python
_enclosing_paragraph(self, lines: list[str], index: int) -> str
```

Label of the paragraph containing lines\[index\], or "".

Observed calls (lexical order): `max`, `range`, `self.owner._logical`, `self.owner._logical(lines[position]).strip`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `str`, `str(match.group('name') or '').strip`, `str(match.group('name') or '').strip().upper`.

Control points:

- L129: `for position in range(index - 1, start - 1, -1)`
- L131: `if not logical`
- L135: `if not match`
- L139: `if not name or name in NON_PARAGRAPH_SENTENCE_WORDS`

### `ModifyUpdateRewriter._conservative_update_block` - L145-L231

```python
_conservative_update_block(self, record: str, table: str, update_columns: list[str], key_columns: list[str], leading: str, paragraph: str='') -> list[str]
```

The converted MODIFY block, SQL-LOCATION included.

Observed calls (lexical order): `NameNormalizer.to_cobol`, `str`, `str(paragraph or '').strip`, `LEGACY_RECORD_LOCATION_TEMPLATE.format`, `SqlLocationMoveBuilder`, `SqlLocationMoveBuilder().sentence`, `lines.append`, `lines.extend`, `self.owner._set_lines`, `self.owner._where_lines`.

Control points:

- L188: `if not location`
- L199: `if sql_location`

### `ModifyUpdateRewriter._changed_columns_after_obtain_calc` - L233-L257

```python
_changed_columns_after_obtain_calc(self, record: str, table: str, lines: list[str], modify_index: int) -> list[str]
```

Observed calls (lexical order): `self._is_lrf_expanded_modify`, `self._post_select_scan_start`, `self._changed_columns_in_range`.

### `ModifyUpdateRewriter._post_select_scan_start` - L259-L296

```python
_post_select_scan_start(self, lines: list[str], modify_index: int, *, lrf_update: bool=False) -> int
```

Observed calls (lexical order): `self._paragraph_body_start`, `max`, `range`, `self.owner._logical`, `logical.upper`, `self.owner.EXEC_SQL_END_PATTERN.match`.

Control points:

- L266: `if lrf_update`
- L279: `for index in range(search_start, modify_index)`
- L283: `if self.owner.EXEC_SQL_END_PATTERN.match(logical)`
- L286: `if 'REMOVED OBTAIN CALC SELECT' in upper`
- L289: `if 'DIRECT UPDATE WILL USE MAPPED COMPOSITE KEY' in upper`
- L293: `if latest_boundary >= 0`

### `ModifyUpdateRewriter._is_lrf_expanded_modify` - L298-L327

```python
_is_lrf_expanded_modify(self, lines: list[str], modify_index: int) -> bool
```

Recognize the marker emitted only by the LRF update bridge.

Observed calls (lexical order): `max`, `range`, `self.owner._logical`, `self.owner._logical(lines[index]).strip`, `logical.upper`, `str`, `len`, `upper.startswith`.

Control points:

- L310: `for index in range(modify_index - 1, max(-1, modify_index - 8), -1)`
- L312: `if not logical`
- L316: `if 'EXPANDED LRF MODIFY' in upper`
- L323: `if fixed_comment or upper.startswith(('*', '/'))`

### `ModifyUpdateRewriter._paragraph_body_start` - L329-L350

```python
_paragraph_body_start(self, lines: list[str], modify_index: int) -> int
```

Return the first line in the current paragraph, or a safe fallback.

Observed calls (lexical order): `range`, `self.owner._logical`, `self.owner._logical(lines[index]).strip`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `str`, `str(match.group('name') or '').strip`, `str(match.group('name') or '').strip().upper`, `max`.

Control points:

- L335: `for index in range(modify_index - 1, -1, -1)`
- L337: `if not logical`
- L340: `if not match`
- L344: `if not name or name in NON_PARAGRAPH_SENTENCE_WORDS`

### `ModifyUpdateRewriter._changed_columns_in_range` - L352-L384

```python
_changed_columns_in_range(self, record: str, table: str, lines: list[str], start: int, end: int) -> list[str]
```

Observed calls (lexical order): `set`, `range`, `self.owner._logical`, `logical.upper`, `upper.startswith`, `self._changed_column_from_logical`, `seen.add`, `output.append`, `self.owner._filter_existing_dclgen_columns`.

Control points:

- L364: `for index in range(start, end)`
- L368: `if upper.startswith('STRING ')`
- L377: `if column and column not in seen`
- L381: `if upper.startswith('END-STRING')`

### `ModifyUpdateRewriter._changed_column_from_logical` - L386-L459

```python
_changed_column_from_logical(self, record: str, table: str, logical: str, in_string_block: bool=False) -> str
```

Observed calls (lexical order): `self.owner.MOVE_TO_BARE_FIELD_PATTERN.match`, `NameNormalizer.to_cobol`, `bare_match.group`, `self.owner._column_for_source_field`, `self.owner.MOVE_TO_DCL_HOST_PATTERN.match`, `self._column_for_host`, `NameNormalizer.normalize`, `of_match.group`, `MOVE_TO_DCL_DOT_HOST_PATTERN.match`, `dot_match.group`, `STRING_INTO_DCL_HOST_PATTERN.match`, `string_into_match.group`, `STRING_INTO_DCL_DOT_HOST_PATTERN.match`, `string_dot_match.group`, `logical.upper`, `ANY_DCL_OF_REFERENCE_PATTERN.search`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L394: `if bare_match`
- L399: `if of_match`
- L407: `if dot_match`
- L415: `if string_into_match`
- L425: `if string_dot_match`
- L434: `if in_string_block and 'INTO' in logical.upper()`
- L436: `if generic_of_match`
- L448: `if generic_dot_match`

### `ModifyUpdateRewriter._column_for_host` - L461-L482

```python
_column_for_host(self, table: str, group: str, host: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.owner.dclgen_repository.group_for_table`, `NameNormalizer.to_cobol`, `self.owner.dclgen_repository.columns_for_table`.

Control points:

- L470: `if group != expected_group`
- L475: `for column in self.owner.dclgen_repository.columns_for_table(table)`
- L479: `if current_host == target_host`

### `ModifyUpdateRewriter._update_columns` - L484-L510

```python
_update_columns(self, record: str, table: str, changed_columns: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self.owner._db2_primary_key_columns`, `NameNormalizer.normalize`, `seen.add`, `output.append`, `self.owner._update_audit_columns`, `self.owner._filter_existing_dclgen_columns`.

Control points:

- L496: `for column in changed_columns`
- L498: `if not normalized or normalized in key_columns or normalized in seen`
- L503: `for column in self.owner._update_audit_columns(record, table)`
- L505: `if not normalized or normalized in key_columns or normalized in seen`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
