# `runners/batch/update_postprocess_pipeline.py`

Source: [runners/batch/update_postprocess_pipeline.py](../../../../runners/batch/update_postprocess_pipeline.py) | 127 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `0df84a3b6f7b81dd4dba289659c4ecee734028c0dc6b97261bf50a62b475ef7c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.composers.fixed_format_composer import FixedFormatComposer
from converter.composers.procedure_indent_normalizer import ProcedureIndentNormalizer
from converter.postprocess.update_char_literal_quoter import UpdateCharLiteralQuoter
from converter.postprocess.update_date_host_converter import UpdateDateHostConverter
from converter.postprocess.update_final_cleanup import UpdateFinalCleanup
from converter.postprocess.update_input_record_renamer import UpdateInputRecordRenamer
from converter.postprocess.update_program_enhancer import UpdateProgramEnhancer
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.name_derivation_resolver import NameDerivationResolver
from converter.services.update_audit_move_inserter import UpdateAuditMoveInserter
from converter.services.update_cobol_final_cleanup_utils import UpdateCobolFinalCleanupUtils
from patterns.batch_runner_patterns import COPY_NAME_PATTERN
from rules.batch_runner_messages import DIAG_UPDATE_AUDIT_MOVES, DIAG_UPDATE_ENHANCEMENT_DONE, DIAG_UPDATE_SKIPPED_TEMPLATE
```

## Local dependency notes

- [converter/composers/fixed_format_composer.py](../../converter/composers/fixed_format_composer.md)
- [converter/composers/procedure_indent_normalizer.py](../../converter/composers/procedure_indent_normalizer.md)
- [converter/postprocess/update_char_literal_quoter.py](../../converter/postprocess/update_char_literal_quoter.md)
- [converter/postprocess/update_date_host_converter.py](../../converter/postprocess/update_date_host_converter.md)
- [converter/postprocess/update_final_cleanup.py](../../converter/postprocess/update_final_cleanup.md)
- [converter/postprocess/update_input_record_renamer.py](../../converter/postprocess/update_input_record_renamer.md)
- [converter/postprocess/update_program_enhancer.py](../../converter/postprocess/update_program_enhancer.md)
- [converter/services/fixed_format_line_service.py](../../converter/services/fixed_format_line_service.md)
- [converter/services/name_derivation_resolver.py](../../converter/services/name_derivation_resolver.md)
- [converter/services/update_audit_move_inserter.py](../../converter/services/update_audit_move_inserter.md)
- [converter/services/update_cobol_final_cleanup_utils.py](../../converter/services/update_cobol_final_cleanup_utils.md)
- [patterns/batch_runner_patterns.py](../../patterns/batch_runner_patterns.md)
- [rules/batch_runner_messages.py](../../rules/batch_runner_messages.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [runners/batch/program_converter.py](program_converter.md)

## Symbol contracts and control points

### `derive_input_record_rename` - L34-L53

```python
derive_input_record_rename(converted_cobol: str) -> tuple[str, str]
```

Recover (old, new) input-record names from COPY statements.

Observed calls (lexical order): `NameDerivationResolver`, `COPY_NAME_PATTERN.findall`, `str`, `str(raw or '').strip`, `str(raw or '').strip().upper`, `deriver.is_derivable`, `deriver.derive`.

Control points:

- L44: `for raw in copy_names`
- L46: `if not name`
- L48: `if deriver.is_derivable(name)`
- L50: `if derived != name`

### `apply_update_postprocess` - L56-L127

```python
apply_update_postprocess(*, source_text: str, converted_cobol: str, copybook_fields: list, dclgen_columns: list, target_program_id: str, diagnostics: list[str], logger) -> str
```

Observed calls (lexical order): `UpdateProgramEnhancer`, `enhancer.enhance`, `diagnostics.extend`, `diagnostics.append`, `FixedFormatComposer`, `FixedFormatComposer().format`, `UpdateFinalCleanup`, `UpdateFinalCleanup().apply`, `FixedFormatLineService`, `UpdateAuditMoveInserter`, `UpdateCobolFinalCleanupUtils`, `_audit.insert_update_audit_moves`, `UpdateCharLiteralQuoter`, `UpdateCharLiteralQuoter(dclgen_columns).apply`, `UpdateDateHostConverter`, `UpdateDateHostConverter(dclgen_columns).apply`.
Another 8 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L90: `if with_audit != formatted`
- L104: `if old_record and new_record and (old_record != new_record)`
- L118: `if getattr(_indent, 'messages', None)`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
