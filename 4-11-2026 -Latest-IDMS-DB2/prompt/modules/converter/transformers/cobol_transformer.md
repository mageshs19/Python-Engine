# `converter/transformers/cobol_transformer.py`

Source: [converter/transformers/cobol_transformer.py](../../../../converter/transformers/cobol_transformer.py) | 842 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `4499a73608a8af25520d2544e23a0ae6fe4699d635c36b10a5e6f85f6393388c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Converts IDMS COBOL statements to DB2-compatible COBOL.

## Module-level bindings

`BOUNDED_SEARCH_ATTRIBUTE` (L205), `ANALYSER_FAILED_TEMPLATE` (L207), `ANALYSER_RESULT_TEMPLATE` (L211), `__all__` (L840)

## Import declarations

```python
from __future__ import annotations
import re
from converter.domain.models import IdmsOperation
from converter.parsers.cobol_parser import CobolParser
from converter.services.program_name_sync_service import ProgramNameSyncService
from converter.transformers.cobol_identification_transformer import CobolIdentificationTransformer
from converter.transformers.cobol_program_id_transformer import CobolProgramIdTransformer
from converter.transformers.cobol_transformed_line_merger import CobolTransformedLineMerger
from converter.transformers.cobol_transformer_line_utils import CobolTransformerLineUtils
from converter.transformers.idms_residual_cleanup import IdmsResidualCleanup
from converter.transformers.idms_statement_transformer import IdmsStatementTransformer
from patterns.cobol_patterns import DIVISION_PATTERN
from patterns.db2_patterns import SQL_ERROR_PARAGRAPH_PATTERN
from patterns.final_feedback_fix_patterns import DIVISION_SECTION_HEADER_PATTERN, PARAGRAPH_HEADER_PATTERN
from patterns.cobol_transformer_patterns import EXIT_LINE_PATTERN, IDMS_ABORT_PARAGRAPH_PATTERN
from rules.cobol_statement_rules import NON_PARAGRAPH_SINGLE_WORDS
from rules.cobol_transformer_rules import DB2_COMPILER_OPTION_LINE, DEFAULT_SQL_ERROR_PARAGRAPH
from rules.lr_access_rules import ENABLE_BOUNDED_SEARCH_RENDERING, ENABLE_LOOP_REMOVAL
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/parsers/cobol_parser.py](../parsers/cobol_parser.md)
- [converter/services/program_name_sync_service.py](../services/program_name_sync_service.md)
- [converter/transformers/cobol_identification_transformer.py](cobol_identification_transformer.md)
- [converter/transformers/cobol_program_id_transformer.py](cobol_program_id_transformer.md)
- [converter/transformers/cobol_transformed_line_merger.py](cobol_transformed_line_merger.md)
- [converter/transformers/cobol_transformer_line_utils.py](cobol_transformer_line_utils.md)
- [converter/transformers/idms_residual_cleanup.py](idms_residual_cleanup.md)
- [converter/transformers/idms_statement_transformer.py](idms_statement_transformer.md)
- [patterns/cobol_patterns.py](../../patterns/cobol_patterns.md)
- [patterns/cobol_transformer_patterns.py](../../patterns/cobol_transformer_patterns.md)
- [patterns/db2_patterns.py](../../patterns/db2_patterns.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/cobol_statement_rules.py](../../rules/cobol_statement_rules.md)
- [rules/cobol_transformer_rules.py](../../rules/cobol_transformer_rules.md)
- [rules/lr_access_rules.py](../../rules/lr_access_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/test_db2_code_fixes.py](../../tests/test_db2_code_fixes.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `CobolTransformer` - L217-L837

```python
class CobolTransformer()
```

Converts IDMS COBOL statements to DB2-compatible COBOL.

### `CobolTransformer.__init__` - L220-L246

```python
__init__(self, idms_statement_transformer: IdmsStatementTransformer, lr_access_analyser=None) -> None
```

Observed calls (lexical order): `CobolParser`, `CobolTransformerLineUtils`, `CobolProgramIdTransformer`, `CobolIdentificationTransformer`, `ProgramNameSyncService`, `IdmsResidualCleanup`, `CobolTransformedLineMerger`.

### `CobolTransformer.transform` - L251-L524

```python
transform(self, cobol_text: str, target_program_id: str='') -> tuple[str, list[str], list[IdmsOperation]]
```

Observed calls (lexical order): `self.parser.analyze`, `self._detect_sql_error_paragraph`, `self.residual_cleanup.reset`, `self.program_name_sync.reset`, `self._reset_statement_transformer`, `self._publish_bounded_search_records`, `str`, `str(cobol_text or '').splitlines`, `raw_line.rstrip`, `self._is_source_comment_record`, `output_lines.append`, `self.line_utils.logical_line`, `logical.strip`, `self._is_cbl_line`, `validation_messages.append`, `self.line_utils.replace_logical_body`.
Another 28 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L282: `for raw_line in str(cobol_text or '').splitlines()`
- L288: `if self._is_source_comment_record(line)`
- L295: `if not logical_stripped`
- L299: `if self._is_cbl_line(logical_stripped)`
- L325: `if program_id_line is not None`
- L334: `if author_line is not None`
- L343: `if date_written_line is not None`
- L349: `if division_match`
- Another 11 conditions/loops exist in this source span.

### `CobolTransformer._remove_empty_idms_abort_paragraph` - L529-L655

```python
_remove_empty_idms_abort_paragraph(self, text: str) -> str
```

Remove or neutralize residual IDMS-ABORT paragraph labels.

Observed calls (lexical order): `str`, `original.splitlines`, `enumerate`, `IDMS_ABORT_PARAGRAPH_PATTERN.match`, `logical`, `logical(line).upper`, `logical(line).upper().rstrip`, `neutral_name.upper`, `set`, `is_paragraph_header`, `len`, `range`, `value.startswith`, `EXIT_LINE_PATTERN.match`, `exit_indexes.append`, `substantive.append`.
Another 13 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L542: `if not lines`
- L572: `if not abort_indexes`
- L581: `while neutral_name.upper() in used_names`
- L587: `for index in abort_indexes`
- L589: `while end < len(lines) and (not is_paragraph_header(end))`
- L594: `for body_index in range(index + 1, end)`
- L596: `if not value or value.startswith(('*', '/'))`
- L598: `if EXIT_LINE_PATTERN.match(value)`
- Another 7 conditions/loops exist in this source span.

### `CobolTransformer._remove_empty_idms_abort_paragraph.logical` - L545-L546

```python
logical(raw: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical_line`, `self.line_utils.logical_line(raw).strip`.

### `CobolTransformer._remove_empty_idms_abort_paragraph.is_paragraph_header` - L560-L566

```python
is_paragraph_header(index: int) -> bool
```

Observed calls (lexical order): `logical`, `value.startswith`, `re.fullmatch`, `value[:-1].upper`.

Control points:

- L562: `if not value or value.startswith(('*', '/'))`
- L564: `if not re.fullmatch('[A-Z0-9][A-Z0-9-]*\\.', value, re.IGNORECASE)`

### `CobolTransformer._reset_statement_transformer` - L657-L674

```python
_reset_statement_transformer(self) -> None
```

Clear the statement transformer's per-program state.

Observed calls (lexical order): `getattr`, `callable`, `reset`, `hasattr`, `set`.

Control points:

- L667: `if callable(reset)`
- L671: `if hasattr(transformer, 'messages')`
- L673: `if hasattr(transformer, 'unmapped_records')`

### `CobolTransformer._publish_bounded_search_records` - L676-L747

```python
_publish_bounded_search_records(self, *, cobol_text: str, validation_messages: list[str]) -> None
```

Classify LR accesses once, then hand the result to the line pass.

Observed calls (lexical order): `setattr`, `str`, `str(cobol_text or '').upper`, `validation_messages.append`, `self.lr_access_analyser.bounded_searches`, `ANALYSER_FAILED_TEMPLATE.format`, `dict`, `validation_messages.extend`, `getattr`, `list`, `', '.join`, `sorted`, `ANALYSER_RESULT_TEMPLATE.format`, `len`.

Control points:

- L693: `if self.lr_access_analyser is None`
- L700: `if '*DB2: EXPANDED LRF' in str(cobol_text or '').upper()`
- L729: `if ENABLE_BOUNDED_SEARCH_RENDERING and ENABLE_LOOP_REMOVAL`
- L733: `if records`
- L741: `if records`

### `CobolTransformer._is_source_comment_record` - L753-L759

```python
_is_source_comment_record(line: str) -> bool
```

Recognize comments before fixed-format columns are stripped.

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`, `text.lstrip`, `stripped.startswith`.

Control points:

- L756: `if len(text) >= 7 and text[:6].isdigit()`

### `CobolTransformer._is_cbl_line` - L761-L765

```python
_is_cbl_line(self, logical_line: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical_line or '').strip`, `str(logical_line or '').strip().upper`, `str(logical_line or '').strip().upper().startswith`.

### `CobolTransformer._ensure_compiler_option` - L767-L809

```python
_ensure_compiler_option(self, output_lines: list[str], validation_messages: list[str]) -> None
```

Insert the DB2 compiler option when the source carried none.

Observed calls (lexical order): `enumerate`, `self.line_utils.logical_line`, `self.line_utils.logical_line(line).strip`, `self.line_utils.logical_line(line).strip().upper`, `logical.startswith`, `output_lines.insert`, `self.line_utils.replace_logical_body`, `validation_messages.append`.

Control points:

- L787: `for (index, line) in enumerate(output_lines)`
- L790: `if not logical.startswith('IDENTIFICATION DIVISION')`

### `CobolTransformer._detect_sql_error_paragraph` - L811-L820

```python
_detect_sql_error_paragraph(self, cobol_text: str) -> str
```

Observed calls (lexical order): `SQL_ERROR_PARAGRAPH_PATTERN.search`, `str`, `match.group`, `match.group(1).upper`.

Control points:

- L817: `if not match`

### `CobolTransformer._clean_data_declaration_line` - L822-L837

```python
_clean_data_declaration_line(self, line: str) -> str
```

Preserve a COBOL data declaration exactly as authored.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
