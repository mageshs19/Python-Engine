# `converter/services/update_cobol_final_cleanup_service.py`

Source: [converter/services/update_cobol_final_cleanup_service.py](../../../../converter/services/update_cobol_final_cleanup_service.py) | 77 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `815908b1ebe81459d6866e25b3e23a32b82c661b9c91f1b6d4cc22c6adc11705`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Update COBOL final cleanup service.

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.update_audit_move_inserter import UpdateAuditMoveInserter
from converter.services.update_cobol_final_cleanup_utils import UpdateCobolFinalCleanupUtils
from converter.services.update_cobol_reference_cleanup import UpdateCobolReferenceCleanup
from converter.services.update_diagnostic_label_normalizer import UpdateDiagnosticLabelNormalizer
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [converter/services/update_audit_move_inserter.py](update_audit_move_inserter.md)
- [converter/services/update_cobol_final_cleanup_utils.py](update_cobol_final_cleanup_utils.md)
- [converter/services/update_cobol_reference_cleanup.py](update_cobol_reference_cleanup.md)
- [converter/services/update_diagnostic_label_normalizer.py](update_diagnostic_label_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)
- [converter/services/update_final_feedback_service.py](update_final_feedback_service.md)

## Symbol contracts and control points

### `UpdateCobolFinalCleanupService` - L34-L77

```python
class UpdateCobolFinalCleanupService()
```

Public service for generic update-program final cleanup.

### `UpdateCobolFinalCleanupService.__init__` - L41-L59

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `UpdateCobolFinalCleanupUtils`, `UpdateCobolReferenceCleanup`, `UpdateAuditMoveInserter`, `UpdateDiagnosticLabelNormalizer`.

### `UpdateCobolFinalCleanupService.apply` - L61-L77

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `self.reference_cleanup.normalize_non_sql_dcl_dot_references`, `self.reference_cleanup.replace_bare_record_initialization`, `self.audit_move_inserter.insert_update_audit_moves`, `self.diagnostic_label_normalizer.normalize_db2_diagnostic_labels`, `output.rstrip`.

Control points:

- L67: `if not output`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
