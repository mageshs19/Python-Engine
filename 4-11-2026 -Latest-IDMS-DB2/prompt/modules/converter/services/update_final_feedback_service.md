# `converter/services/update_final_feedback_service.py`

Source: [converter/services/update_final_feedback_service.py](../../../../converter/services/update_final_feedback_service.py) | 28 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `1caccc1550746adf7f47b29c02cd33b85b07f2d59c155ab7d888d938b5a7a255`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Backward-compatible wrapper for update COBOL final cleanup.

## Module-level bindings

`__all__` (L26)

## Import declarations

```python
from __future__ import annotations
from converter.services.update_cobol_final_cleanup_service import UpdateCobolFinalCleanupService
```

## Local dependency notes

- [converter/services/update_cobol_final_cleanup_service.py](update_cobol_final_cleanup_service.md)

## Symbol contracts and control points

### `UpdateFinalFeedbackService` - L18-L23

```python
class UpdateFinalFeedbackService(UpdateCobolFinalCleanupService)
```

Backward-compatible alias for UpdateCobolFinalCleanupService.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
