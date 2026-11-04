# `converter/services/final_generated_output_service.py`

Source: [converter/services/final_generated_output_service.py](../../../../converter/services/final_generated_output_service.py) | 387 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `e2b441cadfb41215ccfdc33c2f04b980bbad1749cf7ff3b22afc901bb98f39bf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Final cleanup after every source-to-source generator has completed.

## Module-level bindings

`__all__` (L387)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.paragraph_entry_display_composer import _is_paragraph as _is_cobol_paragraph
from converter.composers.unnecessary_comments_cleanup_composer import UnnecessaryCommentsCleanupComposer
from converter.services.final_sequence_resequencer_service import FinalSequenceResequencerService
from converter.services.program_constant_normalizer import ProgramConstantNormalizer
from converter.composers.program_identity_initializer import ProgramIdentityInitializer
from converter.composers.paragraph_entry_display_composer import ParagraphEntryDisplayComposer
from converter.composers.lifecycle_standardization_composer import LifecycleStandardizationComposer
```

## Local dependency notes

- [converter/composers/lifecycle_standardization_composer.py](../composers/lifecycle_standardization_composer.md)
- [converter/composers/paragraph_entry_display_composer.py](../composers/paragraph_entry_display_composer.md)
- [converter/composers/program_identity_initializer.py](../composers/program_identity_initializer.md)
- [converter/composers/unnecessary_comments_cleanup_composer.py](../composers/unnecessary_comments_cleanup_composer.md)
- [converter/services/final_sequence_resequencer_service.py](final_sequence_resequencer_service.md)
- [converter/services/program_constant_normalizer.py](program_constant_normalizer.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)
- [tests/test_generated_output_final_formatting.py](../../tests/test_generated_output_final_formatting.md)
- [tests/test_generic_final_sql_location_and_timestamp_regression.py](../../tests/test_generic_final_sql_location_and_timestamp_regression.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)
- [tests/test_lifecycle_standardization_composer.py](../../tests/test_lifecycle_standardization_composer.md)
- [tests/test_lifecycle_standardization_six_programs.py](../../tests/test_lifecycle_standardization_six_programs.md)
- [tests/test_manual_storage_parity_composer.py](../../tests/test_manual_storage_parity_composer.md)
- [tests/test_schema_driven_4310_generic_rules.py](../../tests/test_schema_driven_4310_generic_rules.md)

## Symbol contracts and control points

### `_logical` - L22-L26

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `text[7:72].strip`, `text.strip`.

Control points:

- L24: `if len(text) >= 7 and text[:6].isdigit()`

### `_is_fixed_comment` - L29-L31

```python
_is_fixed_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`.

### `_is_comment` - L34-L38

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `_is_fixed_comment`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L36: `if _is_fixed_comment(text)`

### `FinalGeneratedOutputService` - L41-L384

```python
class FinalGeneratedOutputService()
```

### `FinalGeneratedOutputService.__init__` - L42-L43

```python
__init__(self) -> None
```

### `FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql` - L46-L140

```python
_ensure_sql_location_before_runtime_sql(cls, text: str) -> str
```

Set SQL-LOCATION before runtime SQL blocks that lack a local value.

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `len`, `_logical`, `cls._is_area_a_paragraph`, `re.search`, `output.append`, `next`, `range`, `' '.join`, `' '.join(block_lines).upper`, `bool`, `_is_comment`, `re.fullmatch`, `queryno.group`, `replacement.ljust`.
Another 8 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L60: `while index < len(lines)`
- L63: `if cls._is_area_a_paragraph(line)`
- L67: `if not re.search('\\bEXEC\\s+SQL\\b', body, re.I)`
- L76: `if end is None`
- L85: `if runtime and (not non_runtime)`
- L92: `if queryno`
- L95: `if preceding >= 0`
- L97: `if re.fullmatch("MOVE\\s+'[A-Z][A-Z0-9_-]*'\\s+TO\\s+SQL-LOCATION\\.", previous, re.I)`
- Another 3 conditions/loops exist in this source span.

### `FinalGeneratedOutputService._remove_obsolete_lrf_comments` - L143-L211

```python
_remove_obsolete_lrf_comments(text: str) -> str
```

Remove only stale LRF breadcrumbs whose executable SQL now exists.

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `any`, `_logical`, `re.search`, `_is_comment`, `len`, `_is_fixed_comment`, `body.startswith`, `_logical(item).lower`, `' '.join`, `_logical(item).upper`, `bool`, `re.fullmatch`, `re.match`, `output.extend`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L159: `while index < len(lines)`
- L162: `if _is_fixed_comment(line) and body.startswith('=')`
- L166: `if _is_comment(line)`
- L168: `while end < len(lines) and _is_comment(lines[end])`
- L179: `if not block`
- L189: `while next_index < len(lines) and (not _logical(lines[next_index]))`
- L199: `if not stale_lrf_modify and (not orphaned_record_label)`
- L209: `if str(text or '').endswith(('\n', '\r'))`

### `FinalGeneratedOutputService._remove_consumed_extra_filter_comments` - L214-L255

```python
_remove_consumed_extra_filter_comments(text: str) -> str
```

Drop generated cursor-WHERE notes only after SQL consumed the filter.

Observed calls (lexical order): `str`, `match.group`, `re.finditer`, `block.upper`, `re.sub`, `source.splitlines`, `_logical`, `_is_comment`, `re.search`, `output.append`, `re.split`, `condition.upper`, `re.findall`, `all`, `value.upper`, `'\n'.join`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L228: `for line in source.splitlines()`
- L230: `if not _is_comment(line) or not re.search('add to the generated cursor WHERE', body, re.I)`
- L242: `for block in normalized_blocks`
- L244: `if all((token and token in block for token in normalized_identifiers)) and all((re.sub('[^A-Z0-9]', '', value.upper()) in block for value in literal_values))`
- L249: `if not consumed`
- L253: `if source.endswith(('\n', '\r'))`

### `FinalGeneratedOutputService._normalize_lrf_error_conditions` - L258-L287

```python
_normalize_lrf_error_conditions(text: str) -> str
```

Normalize the converted form of `IF ... OR 'LR-ERROR'`.

Observed calls (lexical order): `re.compile`, `str`, `str(text or '').splitlines`, `len`, `line[:6].isdigit`, `line[7:72].strip`, `condition.match`, `'IF SQLCODE NOT = 0'.ljust`, `line.strip`, `output.append`, `'\n'.join`, `str(text or '').endswith`.

Control points:

- L270: `for line in str(text or '').splitlines()`
- L271: `if len(line) >= 7 and line[:6].isdigit()`
- L273: `if condition.match(body)`
- L281: `if condition.match(body)`
- L285: `if str(text or '').endswith(('\n', '\r'))`

### `FinalGeneratedOutputService._remove_empty_sqlcode_guards` - L290-L315

```python
_remove_empty_sqlcode_guards(text: str) -> str
```

Remove a generated SQLCODE IF only when it has no executable body.

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `enumerate`, `_logical`, `re.fullmatch`, `output.append`, `_is_comment`, `len`, `FinalGeneratedOutputService._is_area_a_paragraph`, `'\n'.join`, `str(text or '').endswith`.

Control points:

- L301: `for (index, line) in enumerate(lines)`
- L303: `if not re.fullmatch('IF\\s+SQLCODE\\s+NOT\\s*=\\s*0\\.?', body, re.I)`
- L307: `while next_index < len(lines) and (not _logical(lines[next_index]) or _is_comment(lines[next_index]))`
- L309: `if next_index < len(lines) and FinalGeneratedOutputService._is_area_a_paragraph(lines[next_index])`
- L313: `if str(text or '').endswith(('\n', '\r'))`

### `FinalGeneratedOutputService._is_area_a_paragraph` - L318-L321

```python
_is_area_a_paragraph(line: str) -> bool
```

Observed calls (lexical order): `_is_cobol_paragraph`.

### `FinalGeneratedOutputService._remove_resolved_status_warning` - L324-L342

```python
_remove_resolved_status_warning(text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `'\n'.join`, `_is_comment`, `_logical`, `re.sub`, `re.search`, `len`, `_logical(lines[index]).upper`, `_logical(lines[index]).upper().startswith`, `output.append`, `text.endswith`.

Control points:

- L328: `if re.search('(?<![A-Z0-9-])ERROR-STATUS(?![A-Z0-9-])', active, re.I)`
- L332: `while index < len(lines)`
- L333: `if _is_comment(lines[index]) and _logical(lines[index]).upper().startswith('DB2 WARNING: ERROR-STATUS IS UNDEFINED AFTER COPYBOOK REMOVAL')`
- L336: `if index < len(lines) and _is_comment(lines[index]) and _logical(lines[index]).upper().startswith('SHARES A LINE WITH LIVE OPERANDS; LEFT FOR MANUAL REVIEW.')`

### `FinalGeneratedOutputService.apply` - L344-L384

```python
apply(self, text: str, *, standardize_lifecycle: bool=False) -> str
```

Observed calls (lexical order): `str`, `self._ensure_sql_location_before_runtime_sql`, `self._remove_obsolete_lrf_comments`, `self._remove_consumed_extra_filter_comments`, `self._normalize_lrf_error_conditions`, `self._remove_empty_sqlcode_guards`, `self._remove_resolved_status_warning`, `UnnecessaryCommentsCleanupComposer`, `cleanup.cleanup_generated_narration`, `self.messages.extend`, `ProgramConstantNormalizer.normalize`, `ProgramIdentityInitializer`, `identity.compose`, `LifecycleStandardizationComposer`, `lifecycle.compose`, `ParagraphEntryDisplayComposer`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L347: `if not source`
- L369: `if standardize_lifecycle`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
