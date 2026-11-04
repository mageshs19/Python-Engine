# `converter/pipeline/conversion/conversion_pipeline.py`

Source: [converter/pipeline/conversion/conversion_pipeline.py](../../../../../converter/pipeline/conversion/conversion_pipeline.py) | 785 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `f4a39b5a7c30bb6ad67c408d29b4afd57b0b83d9b365395b16b4f94d653cbbf0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L785)

## Import declarations

```python
from __future__ import annotations
import os
from converter.analyzers.program_flow_analyzer import ProgramFlowAnalyzer
from converter.composers.lrf_key_binding_composer import LrfKeyBindingComposer
from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter
from converter.composers.lrf_group_move_decomposer import LrfGroupMoveDecomposer
from converter.domain.models import ConversionInput
from converter.pipeline.conversion.conversion_layout_pipeline import ConversionLayoutPipeline
from converter.pipeline.conversion.conversion_pipeline_steps import GATE_LEGACY_RESTART_GENERATOR, LEGACY_RESTART_SKIPPED, RESTART_DCLGEN_CLASS, RESTART_DCLGEN_MODULE, ConversionPipelineSteps
from converter.validators.mapping_scope_filter import MappingScopeFilter
from converter.validators.mapping_validator import MappingValidator
from converter.rules.common_rules import DEFAULT_ENABLE_LRF_SINGLETON_SHORTCUT, ENV_ENABLE_LRF_SINGLETON_SHORTCUT, LABEL_LR_STATUS, LABEL_LRF_READ, LABEL_LRF_UPDATE, LRF_STAGE_FAILED_TEMPLATE, LRF_STAGE_NO_METHOD_TEMPLATE, LRF_STAGE_NOT_WIRED_TEMPLATE, METHOD_APPLY, METHOD_EXPAND, TRANSFORMER_LR_STATUS_REPLACER, TRANSFORMER_LRF_PATH_EXPANDER, TRANSFORMER_LRF_UPDATE_EXPANDER, TRUTHY_CONFIG_VALUES
from converter.composers.lrf_store_parent_select_composer import LrfStoreParentSelectComposer
from converter.composers.cursor_paragraph_numbering_composer import CursorParagraphNumberingComposer
from converter.composers.cleanup.child_fetch_early_stop_cleanup import ChildFetchEarlyStopCleanup
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import NestedParentFetchNormalizer
from converter.composers.cursor_close_guarantee.flat_fetch_drive_normalizer import FlatFetchDriveNormalizer
from converter.composers.manual_storage_parity_composer import ManualStorageParityComposer
from converter.composers.schema_date_transfer_composer import SchemaDateTransferComposer
from converter.composers.schema_numeric_key_guard import SchemaNumericKeyGuard
from converter.composers.unused_copybook_pruner import UnusedCopybookPruner
from converter.services.final_generated_output_service import FinalGeneratedOutputService
from converter.composers.procedure_indent_normalizer import ProcedureIndentNormalizer
from converter.services.final_sequence_resequencer_service import FinalSequenceResequencerService
from converter.composers.sql_body_area_b_normalizer import SqlBodyAreaBNormalizer
from pathlib import Path
import re
```

## Local dependency notes

- [converter/analyzers/program_flow_analyzer.py](../../analyzers/program_flow_analyzer.md)
- [converter/composers/bounded_lrf_singleton_rewriter.py](../../composers/bounded_lrf_singleton_rewriter.md)
- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](../../composers/cleanup/child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/cleanup_message_collector.py](../../composers/cleanup/cleanup_message_collector.md)
- [converter/composers/cursor_close_guarantee/flat_fetch_drive_normalizer.py](../../composers/cursor_close_guarantee/flat_fetch_drive_normalizer.md)
- [converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.py](../../composers/cursor_close_guarantee/nested_parent_fetch_normalizer.md)
- [converter/composers/cursor_paragraph_numbering_composer.py](../../composers/cursor_paragraph_numbering_composer.md)
- [converter/composers/lrf_group_move_decomposer.py](../../composers/lrf_group_move_decomposer.md)
- [converter/composers/lrf_key_binding_composer.py](../../composers/lrf_key_binding_composer.md)
- [converter/composers/lrf_store_parent_select_composer.py](../../composers/lrf_store_parent_select_composer.md)
- [converter/composers/manual_storage_parity_composer.py](../../composers/manual_storage_parity_composer.md)
- [converter/composers/procedure_indent_normalizer.py](../../composers/procedure_indent_normalizer.md)
- [converter/composers/schema_date_transfer_composer.py](../../composers/schema_date_transfer_composer.md)
- [converter/composers/schema_numeric_key_guard.py](../../composers/schema_numeric_key_guard.md)
- [converter/composers/sql_body_area_b_normalizer.py](../../composers/sql_body_area_b_normalizer.md)
- [converter/composers/unused_copybook_pruner.py](../../composers/unused_copybook_pruner.md)
- [converter/domain/models.py](../../domain/models.md)
- [converter/pipeline/conversion/conversion_layout_pipeline.py](conversion_layout_pipeline.md)
- [converter/pipeline/conversion/conversion_pipeline_steps.py](conversion_pipeline_steps.md)
- [converter/rules/common_rules.py](../../rules/common_rules.md)
- [converter/services/final_generated_output_service.py](../../services/final_generated_output_service.md)
- [converter/services/final_sequence_resequencer_service.py](../../services/final_sequence_resequencer_service.md)
- [converter/validators/mapping_scope_filter.py](../../validators/mapping_scope_filter.md)
- [converter/validators/mapping_validator.py](../../validators/mapping_validator.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion_service.py](../conversion_service.md)
- [tests/test_lrf_intermediate_artifact.py](../../../tests/test_lrf_intermediate_artifact.md)

## Symbol contracts and control points

### `ConversionPipeline` - L44-L782

```python
class ConversionPipeline(ConversionPipelineSteps)
```

Runs the CONTENT phase of the IDMS->DB2 conversion.

### `ConversionPipeline._run_pipeline` - L239-L620

```python
_run_pipeline(self, *, conversion_input: ConversionInput, validation_messages: list[str]) -> tuple[str, list, object]
```

Observed calls (lexical order): `self._repositories`, `self._resolvers`, `self._generators`, `self._transformers`, `self._composers`, `self._expand_logical_records`, `self._resolve_program_kind`, `MappingValidator`, `MappingScopeFilter`, `validation_messages.extend`, `mapping_scope_filter.apply`, `mapping_validator.validate`, `self._component_messages`, `self._restart_context`, `self._publish_lr_retrieval_state`, `transformers['cobol'].transform`.
Another 52 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L384: `if date_compare is not None`
- L512: `if reconciled != converted_cobol`
- L555: `if bounded_rewrite.changed`
- L559: `if bounded_rewrite.diagnostic`

### `ConversionPipeline._expand_logical_records` - L625-L687

```python
_expand_logical_records(self, *, conversion_input: ConversionInput, transformers: dict, validation_messages: list[str]) -> str
```

Rewrite LRF syntax into classic IDMS syntax.

Observed calls (lexical order): `str`, `text.strip`, `self._lrf_stage`, `self._dump_expanded`.

Control points:

- L656: `if not text.strip()`

### `ConversionPipeline._dump_expanded` - L690-L730

```python
_dump_expanded(conversion_input: ConversionInput, text: str) -> None
```

Persist the LRF-to-ordinary-IDMS intermediate for every conversion.

Observed calls (lexical order): `os.environ.get`, `os.environ.get('IDMS_DB2_LRF_INTERMEDIATE_DIR', '').strip`, `os.environ.get('DUMP_EXPANDED', '').strip`, `Path`, `Path(configured_folder).expanduser`, `Path(__file__).resolve`, `str`, `str(getattr(conversion_input, 'target_program_id', '') or 'UNKNOWN').strip`, `getattr`, `re.sub`, `folder.mkdir`, `path.write_text`, `RuntimeError`.

Control points:

- L711: `if configured_folder`

Explicit raises: `RuntimeError(f"Could not write LRF-to-IDMS intermediate '{path}': {exc}")`.

### `ConversionPipeline._lrf_stage` - L732-L782

```python
_lrf_stage(self, *, transformers: dict, key: str, method: str, label: str, text: str, validation_messages: list[str]) -> str
```

Run ONE logical-record stage. Reports every way it can decline.

Observed calls (lexical order): `transformers.get`, `validation_messages.append`, `LRF_STAGE_NOT_WIRED_TEMPLATE.format`, `getattr`, `callable`, `LRF_STAGE_NO_METHOD_TEMPLATE.format`, `run`, `self._component_messages`, `validation_messages.extend`, `LRF_STAGE_FAILED_TEMPLATE.format`.

Control points:

- L757: `if component is None`
- L764: `if not callable(run)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
