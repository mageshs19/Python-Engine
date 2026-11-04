# `converter/transformers/idms_statement/data_statement_converter.py`

Source: [converter/transformers/idms_statement/data_statement_converter.py](../../../../../converter/transformers/idms_statement/data_statement_converter.py) | 968 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `1e53694bbe2dd7542b4dd81e3085cb749fabfd591bc9d590a2008c8f07d745c5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`GUARDED_STATEMENT_INDENT` (L55), `NO_OPENED_SET` (L57), `SENTENCE_TERMINATOR` (L62), `GENERATED_COMMENT_PREFIX` (L63), `BOUNDED_SEARCH_ATTRIBUTE` (L67), `PROGRAM_KIND_ATTRIBUTE` (L68), `LRF_CALC_RECORDS_ATTRIBUTE` (L69), `BOUNDED_SEARCH_SELECT_TEMPLATE` (L76), `BOUNDED_SEARCH_PREDICATE_TEMPLATE` (L79), `BOUNDED_SEARCH_ADVANCE_TEMPLATE` (L82), `__all__` (L968)

## Import declarations

```python
from __future__ import annotations
import re
from converter.analyzers.access_error_policy import AccessPattern, classify_access
from converter.resolvers.program_kind_resolver import KIND_RETRIEVAL
from converter.services.name_normalizer import NameNormalizer
from patterns.idms_patterns import ERASE_PATTERN, FIND_CURRENT_PATTERN, FIND_FIRST_PATTERN, MODIFY_PATTERN, OBTAIN_CALC_PATTERN, OBTAIN_CALC_REVERSED_PATTERN, OBTAIN_FIRST_NEXT_PATTERN, ON_DB_REC_NOT_FOUND_PATTERN, STORE_PATTERN
from rules.idms_transformer_messages import CONVERTED_FIND_FIRST_TEMPLATE, CONVERTED_OBTAIN_FIRST_TEMPLATE, CONVERTED_OBTAIN_NEXT_TEMPLATE, DIRECT_UPDATE_COMPOSITE_KEY, FIND_FIRST_OUTSIDE_PROCEDURE_TEMPLATE, LRF_CALC_READ_CONVERTED_TEMPLATE, LRF_CALC_READ_MARKER_TEMPLATE, LRF_CALC_READ_NO_SQL_TEMPLATE, OBTAIN_CALC_OUTSIDE_PROCEDURE_TEMPLATE, OBTAIN_OUTSIDE_PROCEDURE_TEMPLATE, OPERATION_ERASE, OPERATION_MODIFY, OPERATION_STORE, PERFORM_FETCH_CURSOR_TEMPLATE, PERFORM_OPEN_CURSOR_TEMPLATE, REMOVED_FIND_CURRENT_TEMPLATE, REMOVED_OBTAIN_CALC_SELECT_TEMPLATE, RETRIEVAL_OBTAIN_CALC_RETAINED_TEMPLATE, RETRIEVAL_OBTAIN_CALC_RETAINED_DIAGNOSTIC_TEMPLATE, STORE_MODIFY_ERASE_OUTSIDE_PROCEDURE_TEMPLATE
from rules.idms_transformer_rules import CONTINUE_STATEMENT, OBTAIN_FIRST_KEYWORD, PROCEDURE_DIVISION_NAME, SQLCODE_100_CONTINUE_BODY, SQLCODE_100_IF_CLOSE, SQLCODE_100_IF_OPEN
```

## Local dependency notes

- [converter/analyzers/access_error_policy.py](../../analyzers/access_error_policy.md)
- [converter/resolvers/program_kind_resolver.py](../../resolvers/program_kind_resolver.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/idms_patterns.py](../../../patterns/idms_patterns.md)
- [rules/idms_transformer_messages.py](../../../rules/idms_transformer_messages.md)
- [rules/idms_transformer_rules.py](../../../rules/idms_transformer_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/idms_statement_transformer.py](../idms_statement_transformer.md)
- [tests/test_on_db_rec_not_found_bare.py](../../../tests/test_on_db_rec_not_found_bare.md)

## Symbol contracts and control points

### `DataStatementConverterMixin` - L87-L965

```python
class DataStatementConverterMixin()
```

Converts IDMS data-access statements to DB2/cursor COBOL.

### `DataStatementConverterMixin._convert_on_db_rec_not_found` - L297-L317

```python
_convert_on_db_rec_not_found(self, stripped_line)
```

Observed calls (lexical order): `ON_DB_REC_NOT_FOUND_PATTERN.match`, `str`, `str(match.group('statement') or '').strip`, `str(match.group('statement') or '').strip().rstrip`, `str(match.group('statement') or '').strip().rstrip('.').strip`, `match.group`.

Control points:

- L300: `if not match`
- L310: `if not statement`

### `DataStatementConverterMixin._convert_lrf_calc_read` - L322-L433

```python
_convert_lrf_calc_read(self, upper, stripped_line, current_division)
```

Convert an LRF keyed parent access into a keyed SELECT.

Observed calls (lexical order): `str`, `str(getattr(self, PROGRAM_KIND_ATTRIBUTE, '') or '').strip`, `str(getattr(self, PROGRAM_KIND_ATTRIBUTE, '') or '').strip().lower`, `getattr`, `OBTAIN_CALC_PATTERN.search`, `OBTAIN_CALC_REVERSED_PATTERN.search`, `NameNormalizer.normalize`, `match.group`, `NameNormalizer.to_cobol`, `set`, `self.table_name_resolver.table_for_record`, `self._keep_and_comment_unmapped`, `binding_errors.get`, `self._refuse_lrf_calc_read`, `'; '.join`, `list`.
Another 12 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L341: `if current_division != PROCEDURE_DIVISION_NAME`
- L347: `if kind != KIND_RETRIEVAL`
- L353: `if not match`
- L357: `if not record_key`
- L366: `if record_display not in generated and record_key not in generated`
- L369: `if not self.table_name_resolver.table_for_record(record_key)`
- L378: `if binding_error`
- L409: `if not is_executable_select`

### `DataStatementConverterMixin._refuse_lrf_calc_read` - L435-L454

```python
_refuse_lrf_calc_read(self, *, record: str, source_line: str, reason: str) -> list[str]
```

Fail closed when an LRF keyed read cannot be rendered as SQL.

Observed calls (lexical order): `self.messages.append`, `LRF_CALC_READ_NO_SQL_TEMPLATE.format`.

### `DataStatementConverterMixin._convert_handwritten_retrieval_calc_read` - L459-L516

```python
_convert_handwritten_retrieval_calc_read(self, upper, stripped_line, current_division)
```

Convert only a source-proven hand-written retrieval keyed read.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(self, PROGRAM_KIND_ATTRIBUTE, '') or '').strip`, `str(getattr(self, PROGRAM_KIND_ATTRIBUTE, '') or '').strip().lower`, `OBTAIN_CALC_PATTERN.search`, `OBTAIN_CALC_REVERSED_PATTERN.search`, `NameNormalizer.normalize`, `match.group`, `NameNormalizer.to_cobol`, `plans.get`, `list`, `self.sql_generator.select_by_key`, `type`, `'\n'.join`, `'\n'.join((str(line) for line in sql_lines)).upper`, `all`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L470: `if current_division != PROCEDURE_DIVISION_NAME`
- L472: `if str(getattr(self, PROGRAM_KIND_ATTRIBUTE, '') or '').strip().lower() != KIND_RETRIEVAL`
- L475: `if not match`
- L481: `if not plan`
- L501: `if not all((token in sql_text for token in ('EXEC SQL', 'SELECT', 'INTO', 'END-EXEC')))`

### `DataStatementConverterMixin._convert_handwritten_calc_status_line` - L518-L559

```python
_convert_handwritten_calc_status_line(self, upper, stripped_line)
```

Translate only the source status guards owned by the active keyed read.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(self, '_active_handwritten_calc_record', '') or '').strip`, `str(stripped_line or '').strip`, `re.match`, `re.search`, `re.subn`, `str(getattr(self, '_active_handwritten_calc_group', '') or '').strip`, `re.escape`, `re.sub`.

Control points:

- L521: `if not record`
- L524: `if not code`
- L528: `if re.match('^[A-Z0-9][A-Z0-9-]*\\.$', code, re.I) or re.search('\\b(?:OBTAIN\\s+(?:FIRST|NEXT|CALC)|FIND\\s+(?:FIRST|NEXT|CURRENT)|STORE|MODIFY|ERASE)\\b', code, re.I)`
- L545: `if count_not_zero or count_zero`
- L551: `if group and re.search('^DISPLAY\\b', rewritten, re.I)`
- L557: `if rewritten != code`

### `DataStatementConverterMixin._convert_obtain_calc` - L564-L634

```python
_convert_obtain_calc(self, upper, stripped_line, current_division, sql_error_paragraph)
```

Observed calls (lexical order): `OBTAIN_CALC_PATTERN.search`, `OBTAIN_CALC_REVERSED_PATTERN.search`, `NameNormalizer.normalize`, `match.group`, `NameNormalizer.to_cobol`, `OBTAIN_CALC_OUTSIDE_PROCEDURE_TEMPLATE.format`, `getattr`, `str`, `str(getattr(self, PROGRAM_KIND_ATTRIBUTE, '') or '').strip`, `str(getattr(self, PROGRAM_KIND_ATTRIBUTE, '') or '').strip().lower`, `set`, `self.messages.append`, `RETRIEVAL_OBTAIN_CALC_RETAINED_DIAGNOSTIC_TEMPLATE.format`, `RETRIEVAL_OBTAIN_CALC_RETAINED_TEMPLATE.format`, `self._keep_and_comment_unmapped`, `self.table_name_resolver.table_for_record`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L575: `if not match`
- L581: `if current_division != PROCEDURE_DIVISION_NAME`
- L596: `if kind == KIND_RETRIEVAL and record_display not in generated and (record_key not in generated)`
- L613: `if not record_key`
- L619: `if not self.table_name_resolver.table_for_record(record_key)`

### `DataStatementConverterMixin._convert_obtain_first_next` - L639-L719

```python
_convert_obtain_first_next(self, upper, stripped_line, current_division)
```

Observed calls (lexical order): `OBTAIN_FIRST_NEXT_PATTERN.search`, `classify_access`, `self._keep_and_comment_unmapped`, `match.group`, `NameNormalizer.normalize`, `NameNormalizer.to_cobol`, `OBTAIN_OUTSIDE_PROCEDURE_TEMPLATE.format`, `self._bounded_search_records`, `self._convert_bounded_search`, `self._resolve_cursor_name`, `self._is_terminated`, `self._terminate`, `CONVERTED_OBTAIN_FIRST_TEMPLATE.format`, `PERFORM_OPEN_CURSOR_TEMPLATE.format`, `PERFORM_FETCH_CURSOR_TEMPLATE.format`, `CONVERTED_OBTAIN_NEXT_TEMPLATE.format`.

Control points:

- L647: `if not match`
- L654: `if access_pattern not in {AccessPattern.LR_OBTAIN_FIRST, AccessPattern.LR_OBTAIN_NEXT}`
- L666: `if current_division != PROCEDURE_DIVISION_NAME`
- L673: `if record_key in self._bounded_search_records()`
- L687: `if not cursor_name`
- L697: `if access_pattern is AccessPattern.LR_OBTAIN_FIRST`

### `DataStatementConverterMixin._bounded_search_records` - L724-L732

```python
_bounded_search_records(self) -> dict
```

Records the analyser classified as bounded searches.

Observed calls (lexical order): `getattr`, `isinstance`.

### `DataStatementConverterMixin._convert_bounded_search` - L734-L792

```python
_convert_bounded_search(self, *, upper: str, stripped_line: str, record_key: str, record_display: str, set_display: str) -> list[str]
```

One singleton SELECT for the FIRST; a note for every NEXT.

Observed calls (lexical order): `str`, `str(self._bounded_search_records().get(record_key, '')).strip`, `self._bounded_search_records`, `self._bounded_search_records().get`, `BOUNDED_SEARCH_ADVANCE_TEMPLATE.format`, `self.table_name_resolver.table_for_record`, `self._keep_and_comment_unmapped`, `list`, `self.sql_generator.select_by_key`, `BOUNDED_SEARCH_SELECT_TEMPLATE.format`, `lines.append`, `BOUNDED_SEARCH_PREDICATE_TEMPLATE.format`, `lines.extend`.

Control points:

- L758: `if OBTAIN_FIRST_KEYWORD not in upper`
- L763: `if not self.table_name_resolver.table_for_record(record_key)`
- L771: `if not statement`
- L786: `if predicate`

### `DataStatementConverterMixin._convert_find_current` - L797-L804

```python
_convert_find_current(self, upper, stripped_line, current_division)
```

Observed calls (lexical order): `FIND_CURRENT_PATTERN.search`, `self._removed_idms_executable_lines`, `REMOVED_FIND_CURRENT_TEMPLATE.format`.

Control points:

- L798: `if not FIND_CURRENT_PATTERN.search(upper)`

### `DataStatementConverterMixin._convert_find_first` - L809-L848

```python
_convert_find_first(self, upper, stripped_line, current_division)
```

Observed calls (lexical order): `FIND_FIRST_PATTERN.search`, `NameNormalizer.normalize`, `match.group`, `NameNormalizer.to_cobol`, `FIND_FIRST_OUTSIDE_PROCEDURE_TEMPLATE.format`, `self._resolve_cursor_name`, `self._keep_and_comment_unmapped`, `self._terminate`, `CONVERTED_FIND_FIRST_TEMPLATE.format`, `PERFORM_OPEN_CURSOR_TEMPLATE.format`, `PERFORM_FETCH_CURSOR_TEMPLATE.format`, `self._is_terminated`.

Control points:

- L812: `if not match`
- L821: `if current_division != PROCEDURE_DIVISION_NAME`
- L830: `if not cursor_name`

### `DataStatementConverterMixin._convert_store_modify_erase` - L853-L896

```python
_convert_store_modify_erase(self, upper, stripped_line, current_division, sql_error_paragraph)
```

Observed calls (lexical order): `pattern.search`, `NameNormalizer.normalize`, `match.group`, `STORE_MODIFY_ERASE_OUTSIDE_PROCEDURE_TEMPLATE.format`, `self._keep_and_comment_unmapped`, `self.table_name_resolver.table_for_record`, `generator_method`.

Control points:

- L860: `for (pattern, operation_name, generator_method) in ((STORE_PATTERN, OPERATION_STORE, self.sql_generator.insert), (MODIFY_PATTERN, OPERATION_MODIFY, self.sql_generator.update), (ERAS...`
- L867: `if not match`
- L872: `if current_division != PROCEDURE_DIVISION_NAME`
- L880: `if not record_key`
- L886: `if not self.table_name_resolver.table_for_record(record_key)`

### `DataStatementConverterMixin._is_terminated` - L902-L904

```python
_is_terminated(stripped_line: str) -> bool
```

True when the SOURCE statement ended in a period.

Observed calls (lexical order): `str`, `str(stripped_line or '').rstrip`, `str(stripped_line or '').rstrip().endswith`.

### `DataStatementConverterMixin._terminate` - L907-L940

```python
_terminate(lines: list[str], terminated: bool) -> list[str]
```

Strip the terminator from EVERY generated statement.

Observed calls (lexical order): `str`, `str(line).rstrip`, `text.lstrip`, `text.lstrip().startswith`, `output.append`, `text.endswith`, `len`.

Control points:

- L923: `if terminated or not lines`
- L928: `for line in lines`
- L931: `if text.lstrip().startswith(GENERATED_COMMENT_PREFIX)`
- L935: `if text.endswith(SENTENCE_TERMINATOR)`

### `DataStatementConverterMixin._resolve_cursor_name` - L945-L965

```python
_resolve_cursor_name(self, record_key: str) -> str
```

Cursor name for a record, or '' when anything is unresolved.

Observed calls (lexical order): `self.table_name_resolver.table_for_record`, `self.cursor_name_resolver.cursor_name_from_table`, `str`, `str(cursor_name or '').strip`.

Control points:

- L953: `if not record_key`
- L958: `if not table_name`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
