# `converter/services/update_cobol_final_cleanup_utils.py`

Source: [converter/services/update_cobol_final_cleanup_utils.py](../../../../converter/services/update_cobol_final_cleanup_utils.py) | 69 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `957e35ed33be9266ad462f73ed1bb6d0219d1402dbe2fe62792c5ed6021bb057`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.update_cobol_final_cleanup_rules import PROTECTED_BARE_TARGET_PREFIXES
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [rules/update_cobol_final_cleanup_rules.py](../../rules/update_cobol_final_cleanup_rules.md)

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/update_audit_move_inserter.py](update_audit_move_inserter.md)
- [converter/services/update_cobol_final_cleanup_service.py](update_cobol_final_cleanup_service.md)
- [converter/services/update_cobol_reference_cleanup.py](update_cobol_reference_cleanup.md)
- [converter/services/update_diagnostic_label_normalizer.py](update_diagnostic_label_normalizer.md)
- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)

## Symbol contracts and control points

### `UpdateCobolFinalCleanupUtils` - L11-L69

```python
class UpdateCobolFinalCleanupUtils()
```

Shared fixed-format helper methods for update COBOL final cleanup.

### `UpdateCobolFinalCleanupUtils.__init__` - L16-L20

```python
__init__(self, fixed_format: FixedFormatLineService) -> None
```

### `UpdateCobolFinalCleanupUtils.body_with_existing_indent` - L22-L34

```python
body_with_existing_indent(self, *, original_line: str, new_logical: str) -> str
```

Observed calls (lexical order): `self.fixed_format.body`, `body.lstrip`, `len`, `str`, `str(new_logical or '').strip`.

Control points:

- L31: `if not leading`

### `UpdateCobolFinalCleanupUtils.comment_body_for_line` - L36-L58

```python
comment_body_for_line(self, *, original_line: str, comment_text: str) -> str
```

Return the correct body for a comment line.

Observed calls (lexical order): `str`, `str(comment_text or '').strip`, `text.startswith`, `text[1:].lstrip`, `self.fixed_format.body`, `body.lstrip`, `len`.

Control points:

- L52: `if text.startswith('*')`

### `UpdateCobolFinalCleanupUtils.is_protected_bare_target` - L60-L69

```python
is_protected_bare_target(self, target: str) -> bool
```

Observed calls (lexical order): `str`, `str(target or '').upper`, `any`, `normalized.startswith`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
