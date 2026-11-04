# `converter/composers/final_cobol_fix_composer.py`

Source: [converter/composers/final_cobol_fix_composer.py](../../../../converter/composers/final_cobol_fix_composer.py) | 149 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `29e6c7c8fc1cda329acb2e2fae2a099eeefd2f1eb3e8323cd22f3a0c1068bb9e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Final COBOL fix composer.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from rules.final_feedback_fix_rules import DEFAULT_DB2_DATE_EXTERNAL_FORMAT, ORDER_BY_COLUMNS_IN_SELECT_DEFAULT
from converter.services.cobol_area_alignment_service import CobolAreaAlignmentService
from converter.services.cursor_select_minimizer_service import CursorSelectMinimizerService
from converter.services.db2_comment_readability_service import Db2CommentReadabilityService
from converter.services.db2_date_format_service import Db2DateFormatService
from converter.services.final_sequence_resequencer_service import FinalSequenceResequencerService
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.procedure_block_indent_service import ProcedureBlockIndentService
from converter.services.program_name_sync_service import ProgramNameSyncService
from converter.services.string_block_format_service import StringBlockFormatService
from converter.services.update_cobol_final_cleanup_service import UpdateCobolFinalCleanupService
```

## Local dependency notes

- [converter/services/cobol_area_alignment_service.py](../services/cobol_area_alignment_service.md)
- [converter/services/cursor_select_minimizer_service.py](../services/cursor_select_minimizer_service.md)
- [converter/services/db2_comment_readability_service.py](../services/db2_comment_readability_service.md)
- [converter/services/db2_date_format_service.py](../services/db2_date_format_service.md)
- [converter/services/final_sequence_resequencer_service.py](../services/final_sequence_resequencer_service.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [converter/services/procedure_block_indent_service.py](../services/procedure_block_indent_service.md)
- [converter/services/program_name_sync_service.py](../services/program_name_sync_service.md)
- [converter/services/string_block_format_service.py](../services/string_block_format_service.md)
- [converter/services/update_cobol_final_cleanup_service.py](../services/update_cobol_final_cleanup_service.md)
- [rules/final_feedback_fix_rules.py](../../rules/final_feedback_fix_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `FinalCobolFixComposerConfig` - L61-L66

```python
class FinalCobolFixComposerConfig()
```

Declared class/data-model fields:

```python
db2_date_external_format: str = DEFAULT_DB2_DATE_EXTERNAL_FORMAT
require_order_by_columns_in_select: bool = ORDER_BY_COLUMNS_IN_SELECT_DEFAULT
resequence_final_output: bool = True
```

### `FinalCobolFixComposer` - L69-L127

```python
class FinalCobolFixComposer()
```

### `FinalCobolFixComposer.__init__` - L70-L103

```python
__init__(self, config: FinalCobolFixComposerConfig | None=None, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FinalCobolFixComposerConfig`, `FixedFormatLineService`, `ProgramNameSyncService`, `Db2DateFormatService`, `CursorSelectMinimizerService`, `UpdateCobolFinalCleanupService`, `CobolAreaAlignmentService`, `Db2CommentReadabilityService`, `ProcedureBlockIndentService`, `StringBlockFormatService`, `FinalSequenceResequencerService`.

### `FinalCobolFixComposer.compose` - L105-L127

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `self.program_name_sync.sync`, `self.date_format_service.apply`, `self.cursor_select_minimizer.minimize`, `self.update_final_feedback.apply`, `self.area_alignment.align`, `self.comment_readability.apply`, `self.procedure_indent.apply`, `self.string_block_format.apply`, `self.sequence_resequencer.resequence`, `output.rstrip`.

Control points:

- L108: `if not output`
- L124: `if self.config.resequence_final_output`

### `apply_final_cobol_fixes` - L130-L149

```python
apply_final_cobol_fixes(text: str, db2_date_external_format: str | None=None, require_order_by_columns_in_select: bool=ORDER_BY_COLUMNS_IN_SELECT_DEFAULT, resequence_final_output: bool=True) -> str
```

Observed calls (lexical order): `FinalCobolFixComposer`, `FinalCobolFixComposerConfig`, `composer.compose`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
