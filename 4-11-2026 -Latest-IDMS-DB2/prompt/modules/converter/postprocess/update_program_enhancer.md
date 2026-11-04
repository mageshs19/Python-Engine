# `converter/postprocess/update_program_enhancer.py`

Source: [converter/postprocess/update_program_enhancer.py](../../../../converter/postprocess/update_program_enhancer.py) | 515 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `bd9b4e6a2170cd88bc2dfb33f45a59ad2d336cf9b9d397c5341252b33d75435e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Update-program postprocess enhancer.

## Module-level bindings

`PROGRAM_KIND_RETRIEVAL` (L129), `PROGRAM_KIND_UPDATE` (L130), `ROLE_TABLE_FIELD` (L135), `ROLE_HOST_RECORD_FIELD` (L136), `APPLY_GENERIC_RESTART_FRAMEWORK` (L142), `MESSAGES` (L144), `__all__` (L506)

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.cobol_update_standard_generator import CobolUpdateStandardGenerator
from converter.postprocess.dynamic_metadata_resolver import DynamicMetadataResolver
from converter.postprocess.update_business_sql_standardizer import UpdateBusinessSqlStandardizer
from converter.postprocess.update_enhancement_result import EnhancementResult
from converter.postprocess.update_main_flow_rewriter import UpdateMainFlowRewriter
from converter.postprocess.update_postprocess_line_utils import UpdatePostprocessLineUtils
from converter.postprocess.update_restart_paragraph_manager import UpdateRestartParagraphManager
from converter.postprocess.update_storage_include_manager import UpdateStorageIncludeManager
from rules.update_restart_rules import UPDATE_RESTART_DIAGNOSTICS
from converter.repositories.mapping_repository import MappingRepository
from converter.postprocess.restart_config import RestartConfig
from converter.postprocess.restart_logic_pipeline import RestartLogicPipeline
from converter.postprocess.cobol_restart_logic_generator import CobolRestartLogicGenerator
from converter.postprocess.legacy_eof_condition_rewriter import LegacyEofConditionRewriter
from converter.resolvers.program_kind_resolver import ProgramKindResolver
```

## Local dependency notes

- [converter/postprocess/cobol_restart_logic_generator.py](cobol_restart_logic_generator.md)
- [converter/postprocess/cobol_update_standard_generator.py](cobol_update_standard_generator.md)
- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)
- [converter/postprocess/legacy_eof_condition_rewriter.py](legacy_eof_condition_rewriter.md)
- [converter/postprocess/restart_config.py](restart_config.md)
- [converter/postprocess/restart_logic_pipeline.py](restart_logic_pipeline.md)
- [converter/postprocess/update_business_sql_standardizer.py](update_business_sql_standardizer.md)
- [converter/postprocess/update_enhancement_result.py](update_enhancement_result.md)
- [converter/postprocess/update_main_flow_rewriter.py](update_main_flow_rewriter.md)
- [converter/postprocess/update_postprocess_line_utils.py](update_postprocess_line_utils.md)
- [converter/postprocess/update_restart_paragraph_manager.py](update_restart_paragraph_manager.md)
- [converter/postprocess/update_storage_include_manager.py](update_storage_include_manager.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/program_kind_resolver.py](../resolvers/program_kind_resolver.md)
- [rules/update_restart_rules.py](../../rules/update_restart_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)

## Symbol contracts and control points

### `UpdateProgramEnhancer` - L181-L503

```python
class UpdateProgramEnhancer()
```

Update-program postprocess enhancer. Refuses retrieval programs.

### `UpdateProgramEnhancer.__init__` - L184-L205

```python
__init__(self) -> None
```

Observed calls (lexical order): `DynamicMetadataResolver`, `CobolUpdateStandardGenerator`, `UpdatePostprocessLineUtils`, `UpdateStorageIncludeManager`, `UpdateMainFlowRewriter`, `UpdateRestartParagraphManager`, `UpdateBusinessSqlStandardizer`.

### `UpdateProgramEnhancer.enhance` - L210-L360

```python
enhance(self, *, source_cobol: str, converted_cobol: str, copybook_fields: list, dclgen_columns: list, target_program_id: str='', sheet_mapping_rows: list | None=None, program_kind: str='') -> EnhancementResult
```

Observed calls (lexical order): `str`, `str(program_kind or '').strip`, `str(program_kind or '').strip().lower`, `diagnostics.append`, `ProgramKindResolver`, `ProgramKindResolver().is_update`, `diagnostics.extend`, `EnhancementResult`, `MappingRepository`, `self.resolver.resolve`, `self._report_restart_gate`, `self.storage_include_manager.fix_malformed_sqlerror`, `self.storage_include_manager.normalize_program_name`, `self.storage_include_manager.ensure_working_storage`, `self.storage_include_manager.ensure_date_working_storage`, `self.storage_include_manager.ensure_dclgen_include`.
Another 13 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L225: `if not kind`
- L249: `if kind == PROGRAM_KIND_RETRIEVAL`

### `UpdateProgramEnhancer._report_restart_gate` - L366-L403

```python
_report_restart_gate(*, context, dclgen_columns: list, mapping_repository: MappingRepository, diagnostics: list[str]) -> None
```

Say WHY no restart SQL will be generated.

Observed calls (lexical order): `getattr`, `bool`, `any`, `mapping_repository.has_table`, `mapping_repository.tables`, `diagnostics.append`.

Control points:

- L379: `if getattr(context, 'restart_dclgen', None) is not None`
- L388: `if has_dclgen_candidate and mapping_has_hint`

### `UpdateProgramEnhancer._apply_generic_restart_logic` - L408-L465

```python
_apply_generic_restart_logic(self, cobol_source: str, context: object, diagnostics: list[str]) -> str
```

Apply the restart framework, or report why it was not applied.

Observed calls (lexical order): `diagnostics.append`, `self._build_restart_config`, `CobolRestartLogicGenerator`, `RestartLogicPipeline`, `pipeline.is_applicable`, `pipeline.not_applicable_reason`, `pipeline.apply_to_program`, `diagnostics.extend`, `MESSAGES['applied_silently'].format`.

Control points:

- L415: `if not APPLY_GENERIC_RESTART_FRAMEWORK`
- L420: `if restart_config is None`
- L431: `if not pipeline.is_applicable(context)`
- L445: `if not pipeline.diagnostics`

### `UpdateProgramEnhancer._build_restart_config` - L468-L503

```python
_build_restart_config(context: object, diagnostics: list[str]) -> RestartConfig | None
```

The restart config, or None WITH a reason. See CORRECTION 2b.

Observed calls (lexical order): `getattr`, `diagnostics.append`, `str`, `str(getattr(role, ROLE_TABLE_FIELD, '') or '').strip`, `str(getattr(role, ROLE_HOST_RECORD_FIELD, '') or '').strip`, `MESSAGES['names_unresolved'].format`, `RestartConfig`, `config.detect_from_cobol`.

Control points:

- L474: `if role is None`
- L483: `if not table or not host_record`
- L498: `if cobol_source`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
