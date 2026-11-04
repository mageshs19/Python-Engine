# `converter/ui/conversion_actions.py`

Source: [converter/ui/conversion_actions.py](../../../../converter/ui/conversion_actions.py) | 371 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `64b58ede942bc1231584027be4078ddb8a2a787e5dd51f87a4b9f05e67e86fba`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`_IDMS_WRITE_PATTERN` (L28), `_DB2_WRITE_PATTERN` (L34)

## Import declarations

```python
from __future__ import annotations
import re
from converter.domain.models import ConversionInput
from converter.pipeline.conversion_service import ConversionService
from converter.parsers.cobol_parser import CobolParser
from converter.services.name_derivation_resolver import NameDerivationResolver
from converter.ui.file_name_utils import build_converted_cobol_file_name
from patterns.lrf_patterns import COPY_IDMS_LR_PATTERN
from rules.lrf_rules import DIAG_LRF_NO_RECORDS_IN_SCOPE, DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE, LRF_VALIDATION_MESSAGES
import streamlit as st
from converter.composers.fixed_format_composer import FixedFormatComposer
from converter.composers.procedure_indent_normalizer import ProcedureIndentNormalizer
from converter.postprocess.update_char_literal_quoter import UpdateCharLiteralQuoter
from converter.postprocess.update_date_host_converter import UpdateDateHostConverter
from converter.postprocess.update_final_cleanup import UpdateFinalCleanup
from converter.postprocess.update_input_record_renamer import UpdateInputRecordRenamer
from converter.postprocess.update_program_enhancer import UpdateProgramEnhancer
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.update_audit_move_inserter import UpdateAuditMoveInserter
from converter.services.update_cobol_final_cleanup_utils import UpdateCobolFinalCleanupUtils
from patterns.batch_runner_patterns import COPY_NAME_PATTERN
from converter.postprocess.copybook_reference_renamer import CopybookReferenceRenamer
```

## Local dependency notes

- [converter/composers/fixed_format_composer.py](../composers/fixed_format_composer.md)
- [converter/composers/procedure_indent_normalizer.py](../composers/procedure_indent_normalizer.md)
- [converter/domain/models.py](../domain/models.md)
- [converter/parsers/cobol_parser.py](../parsers/cobol_parser.md)
- [converter/pipeline/conversion_service.py](../pipeline/conversion_service.md)
- [converter/postprocess/copybook_reference_renamer.py](../postprocess/copybook_reference_renamer.md)
- [converter/postprocess/update_char_literal_quoter.py](../postprocess/update_char_literal_quoter.md)
- [converter/postprocess/update_date_host_converter.py](../postprocess/update_date_host_converter.md)
- [converter/postprocess/update_final_cleanup.py](../postprocess/update_final_cleanup.md)
- [converter/postprocess/update_input_record_renamer.py](../postprocess/update_input_record_renamer.md)
- [converter/postprocess/update_program_enhancer.py](../postprocess/update_program_enhancer.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [converter/services/name_derivation_resolver.py](../services/name_derivation_resolver.md)
- [converter/services/update_audit_move_inserter.py](../services/update_audit_move_inserter.md)
- [converter/services/update_cobol_final_cleanup_utils.py](../services/update_cobol_final_cleanup_utils.md)
- [converter/ui/file_name_utils.py](file_name_utils.md)
- [patterns/batch_runner_patterns.py](../../patterns/batch_runner_patterns.md)
- [patterns/lrf_patterns.py](../../patterns/lrf_patterns.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/main_tab.py](main_tab.md)
- [tests/test_update_program_detection.py](../../tests/test_update_program_detection.md)

## Symbol contracts and control points

### `resolve_target_program_id` - L41-L51

```python
resolve_target_program_id(source_text: str) -> str
```

Derive the target PROGRAM-ID from the uploaded COBOL source.

Observed calls (lexical order): `CobolParser`, `CobolParser().program_id`, `NameDerivationResolver`, `NameDerivationResolver().derive`.

Control points:

- L49: `if not source_id`

### `_is_update_program` - L54-L59

```python
_is_update_program(source_text: str) -> bool
```

True when the source writes via IDMS (STORE/MODIFY/ERASE) or DB2.

Observed calls (lexical order): `str`, `bool`, `_DB2_WRITE_PATTERN.search`, `_IDMS_WRITE_PATTERN.search`.

### `_require_streamlit` - L65-L71

```python
_require_streamlit()
```

Raise a clear error only when an interactive UI action needs Streamlit.

Observed calls (lexical order): `RuntimeError`.

Control points:

- L67: `if st is None`

Explicit raises: `RuntimeError("Streamlit is required for UI actions. Install the project's runtime dependencies.")`.

### `_logical_records` - L74-L81

```python
_logical_records() -> list
```

LRF logical records currently held in session state.

Observed calls (lexical order): `_require_streamlit`, `list`, `streamlit.session_state.get`.

### `_source_uses_logical_records` - L84-L94

```python
_source_uses_logical_records(source_text: str) -> list[str]
```

Logical record names the SOURCE program copies via COPY IDMS LR.

Observed calls (lexical order): `str`, `str(source_text or '').splitlines`, `COPY_IDMS_LR_PATTERN.search`, `match.group`, `str(match.group('lr') or '').strip`, `str(match.group('lr') or '').strip().upper`, `names.append`.

Control points:

- L87: `for raw_line in str(source_text or '').splitlines()`
- L89: `if not match`
- L92: `if name and name not in names`

### `_narrate_lrf` - L97-L125

```python
_narrate_lrf(*, source_text: str, logical_records: list, diagnostics: list[str]) -> None
```

Record what LRF metadata this conversion will actually see.

Observed calls (lexical order): `', '.join`, `getattr`, `str`, `diagnostics.append`, `DIAG_LRF_RECORDS_IN_SCOPE_TEMPLATE.format`, `len`, `_source_uses_logical_records`.

Control points:

- L109: `if logical_records`
- L124: `if used and (not logical_records)`

### `_apply_update_postprocess` - L128-L241

```python
_apply_update_postprocess(*, source_text: str, converted_cobol: str, copybook_fields: list, dclgen_columns: list, target_program_id: str, diagnostics: list[str]) -> str
```

Run the update-only enhancement pipeline (restart flow, SQLERROR fix, DCLGEN includes, audit moves, CHAR/date host conversion, final cleanup).

Observed calls (lexical order): `UpdateProgramEnhancer`, `UpdateProgramEnhancer().enhance`, `diagnostics.extend`, `FixedFormatComposer`, `FixedFormatComposer().format`, `UpdateFinalCleanup`, `UpdateFinalCleanup().apply`, `FixedFormatLineService`, `UpdateAuditMoveInserter`, `UpdateAuditMoveInserter(fixed_format=_ff, utils=UpdateCobolFinalCleanupUtils(_ff)).insert_update_audit_moves`, `UpdateCobolFinalCleanupUtils`, `UpdateCharLiteralQuoter`, `UpdateCharLiteralQuoter(dclgen_columns).apply`, `UpdateDateHostConverter`, `UpdateDateHostConverter(dclgen_columns).apply`, `NameDerivationResolver`.
Another 12 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L209: `for raw in COPY_NAME_PATTERN.findall(str(with_dates or ''))`
- L211: `if name and deriver.is_derivable(name)`
- L213: `if derived != name`
- L217: `if old_record and new_record and (old_record != new_record)`
- L231: `if getattr(_indent, 'messages', None)`

### `_apply_retrieval_postprocess` - L244-L268

```python
_apply_retrieval_postprocess(*, converted_cobol: str, diagnostics: list[str]) -> str
```

Run the retrieval-only postprocess (rename copybook references).

Observed calls (lexical order): `CopybookReferenceRenamer`, `renamer.apply`, `diagnostics.append`.

### `generate_db2_cobol` - L271-L344

```python
generate_db2_cobol() -> None
```

Observed calls (lexical order): `_validate_generation_inputs`, `resolve_target_program_id`, `_logical_records`, `_narrate_lrf`, `ConversionService`, `service.convert`, `ConversionInput`, `getattr`, `list`, `_is_update_program`, `_apply_update_postprocess`, `_apply_retrieval_postprocess`, `build_converted_cobol_file_name`, `bool`, `st.success`, `_lrf_suffix`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L272: `if not _validate_generation_inputs()`
- L305: `if converted_cobol and _is_update_program(idms_cobol_text)`
- L333: `if st.session_state.generated`

### `_lrf_suffix` - L347-L351

```python
_lrf_suffix(logical_records: list) -> str
```

Short LRF note appended to the success banner.

Observed calls (lexical order): `len`.

Control points:

- L349: `if not logical_records`

### `_validate_generation_inputs` - L354-L371

```python
_validate_generation_inputs() -> bool
```

Observed calls (lexical order): `st.warning`, `st.error`, `st.session_state.idms_cobol_text.strip`.

Control points:

- L355: `if not st.session_state.loaded`
- L359: `if not st.session_state.sheet_mapping_rows`
- L363: `if not st.session_state.dclgen_columns`
- L367: `if not st.session_state.idms_cobol_text.strip()`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
