# `converter/composers/cobol_cleanup_composer.py`

Source: [converter/composers/cobol_cleanup_composer.py](../../../../converter/composers/cobol_cleanup_composer.py) | 171 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `8338da4b38ccb5a9bb43ecd330fcf774c9ec939530fc45fd7562af87b2f1d0f5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL post-conversion cleanup composer.

## Import declarations

```python
from converter.composers.fixed_format_composer import FixedFormatComposer
from converter.composers.cleanup.child_fetch_early_stop_cleanup import ChildFetchEarlyStopCleanup
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.composers.cleanup.db2_date_output_cleanup import Db2DateOutputCleanup
from converter.composers.cleanup.dclgen_include_cleanup import DclgenIncludeCleanup
from converter.composers.cleanup.error_status_flag_cleanup import ErrorStatusFlagCleanup
from converter.composers.cleanup.orphaned_idms_status_guard_cleanup import OrphanedIdmsStatusGuardCleanup
from converter.composers.cleanup.initialize_before_output_cleanup import InitializeBeforeOutputCleanup
from converter.composers.cleanup.output_write_placement_cleanup import OutputWritePlacementCleanup
from converter.composers.cleanup.paragraph_terminator_cleanup import ParagraphTerminatorCleanup
from converter.composers.cleanup.residual_idms_comment_cleanup import ResidualIdmsCommentCleanup
from converter.composers.cleanup.residual_idms_error_clause_cleanup import ResidualIdmsErrorClauseCleanup
from converter.repositories.dclgen_repository import DclgenRepository
```

## Local dependency notes

- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](cleanup/child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/cleanup_message_collector.py](cleanup/cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cleanup/cobol_cleanup_line_utils.md)
- [converter/composers/cleanup/db2_date_output_cleanup.py](cleanup/db2_date_output_cleanup.md)
- [converter/composers/cleanup/dclgen_include_cleanup.py](cleanup/dclgen_include_cleanup.md)
- [converter/composers/cleanup/error_status_flag_cleanup.py](cleanup/error_status_flag_cleanup.md)
- [converter/composers/cleanup/initialize_before_output_cleanup.py](cleanup/initialize_before_output_cleanup.md)
- [converter/composers/cleanup/orphaned_idms_status_guard_cleanup.py](cleanup/orphaned_idms_status_guard_cleanup.md)
- [converter/composers/cleanup/output_write_placement_cleanup.py](cleanup/output_write_placement_cleanup.md)
- [converter/composers/cleanup/paragraph_terminator_cleanup.py](cleanup/paragraph_terminator_cleanup.md)
- [converter/composers/cleanup/residual_idms_comment_cleanup.py](cleanup/residual_idms_comment_cleanup.md)
- [converter/composers/cleanup/residual_idms_error_clause_cleanup.py](cleanup/residual_idms_error_clause_cleanup.md)
- [converter/composers/fixed_format_composer.py](fixed_format_composer.md)
- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `CobolCleanupComposer` - L76-L171

```python
class CobolCleanupComposer()
```

### `CobolCleanupComposer.__init__` - L77-L125

```python
__init__(self, dclgen_repository: DclgenRepository) -> None
```

Observed calls (lexical order): `CleanupMessageCollector`, `CobolCleanupLineUtils`, `ResidualIdmsCommentCleanup`, `ResidualIdmsErrorClauseCleanup`, `DclgenIncludeCleanup`, `OrphanedIdmsStatusGuardCleanup`, `ErrorStatusFlagCleanup`, `ChildFetchEarlyStopCleanup`, `OutputWritePlacementCleanup`, `InitializeBeforeOutputCleanup`, `Db2DateOutputCleanup`, `ParagraphTerminatorCleanup`.

### `CobolCleanupComposer.messages` - L128-L129

```python
messages(self) -> list[str]
```

### `CobolCleanupComposer.compose` - L131-L171

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self._collector.reset`, `str`, `output.strip`, `self._residual_comment.remove_residual_idms_comments`, `self._residual_idms_error_clause.apply`, `self._orphaned_status_guard.apply`, `self._dclgen_include.apply`, `self._error_status.replace_error_status_with_flag`, `self._error_status.ensure_sw_status_d_declaration`, `self._child_fetch.ensure_child_fetch_early_stop`, `self._output_write_placement.move_output_write_after_child_loop`, `self._initialize_output.ensure_initialize_before_output_population`, `self._db2_date_output.convert_db2_date_moves_to_output_dates`, `self._paragraph_terminator.ensure_paragraph_termination`, `FixedFormatComposer`, `FixedFormatComposer().format`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L135: `if not output.strip()`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
