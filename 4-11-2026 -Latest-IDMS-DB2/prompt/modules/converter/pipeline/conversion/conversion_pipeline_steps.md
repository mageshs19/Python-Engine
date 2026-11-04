# `converter/pipeline/conversion/conversion_pipeline_steps.py`

Source: [converter/pipeline/conversion/conversion_pipeline_steps.py](../../../../../converter/pipeline/conversion/conversion_pipeline_steps.py) | 862 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `d86ca8a348ed817a4e752de9255413bf45885eae1d602f4d5b494996a8faa753`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Helper steps for the CONTENT phase of the IDMS->DB2 conversion.

## Module-level bindings

`RESTART_DCLGEN_MODULE` (L100), `RESTART_DCLGEN_CLASS` (L101), `GATE_LEGACY_RESTART_GENERATOR` (L110), `LEGACY_RESTART_SKIPPED` (L111), `PROGRAM_KIND_ATTRIBUTE` (L121), `PROGRAM_KIND_HANDOFF_OK` (L122), `PROGRAM_KIND_HANDOFF_REFUSED` (L123), `COBOL_TRANSFORMER_KEY` (L132), `STATEMENT_TRANSFORMER_ATTRIBUTE` (L133), `STATEMENT_TRANSFORMER_NAME` (L134), `LRF_EXPANDER_KEY` (L135), `LRF_CALC_RECORDS_ATTRIBUTE` (L136), `LRF_KEY_INPUT_MOVES_ATTRIBUTE` (L137), `LRF_KEY_BINDING_ERRORS_ATTRIBUTE` (L138), `LRF_SELECT_COLUMNS_ATTRIBUTE` (L139), `HANDWRITTEN_CALC_PLANS_ATTRIBUTE` (L140), `CALC_PARENT_RECORDS_ATTRIBUTE` (L141), `STATEMENT_TRANSFORMER_UNREACHABLE` (L143), `LRF_CALC_RECORDS_PUBLISHED` (L148), `LRF_CALC_RECORDS_NONE` (L152), `COMMIT_CLEANUP_MISSING` (L157), `DATE_COMPARE_MISSING` (L161), `__all__` (L842)

## Import declarations

```python
from __future__ import annotations
import re
from converter.domain.models import ConversionInput
from converter.analyzers.lr_access.lrf_key_binding_planner import LrfKeyBindingPlanner
from converter.analyzers.lr_access.handwritten_obtain_calc_planner import HandwrittenObtainCalcPlanner
from converter.pipeline.run import run_stage
from converter.pipeline.stage import Document
from converter.resolvers.program_kind_resolver import ProgramKindResolver
from converter.services.name_normalizer import NameNormalizer
from rules.program_kind_rules import KIND_UPDATE
from converter.resolvers.restart_context_builder import RestartContextBuilder
from converter.generators.restart.restart_totals_resolver import RestartTotalsResolver
from rules.update_restart_rules import UPDATE_RESTART_WS_NAMES
```

## Local dependency notes

- [converter/analyzers/lr_access/handwritten_obtain_calc_planner.py](../../analyzers/lr_access/handwritten_obtain_calc_planner.md)
- [converter/analyzers/lr_access/lrf_key_binding_planner.py](../../analyzers/lr_access/lrf_key_binding_planner.md)
- [converter/domain/models.py](../../domain/models.md)
- [converter/generators/restart/restart_totals_resolver.py](../../generators/restart/restart_totals_resolver.md)
- [converter/pipeline/run.py](../run.md)
- [converter/pipeline/stage.py](../stage.md)
- [converter/resolvers/program_kind_resolver.py](../../resolvers/program_kind_resolver.md)
- [converter/resolvers/restart_context_builder.py](../../resolvers/restart_context_builder.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/program_kind_rules.py](../../../rules/program_kind_rules.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](conversion_pipeline.md)
- [tests/test_lrf_select_projection_analysis.py](../../../tests/test_lrf_select_projection_analysis.md)

## Symbol contracts and control points

### `ConversionPipelineSteps` - L167-L839

```python
class ConversionPipelineSteps()
```

What each content-phase step does. Order lives in the pipeline.

### `ConversionPipelineSteps._stage` - L174-L186

```python
_stage(name: str, converted_cobol: str, validation_messages: list[str]) -> str
```

Run one registered stage and drain its diagnostics.

Observed calls (lexical order): `Document`, `run_stage`, `validation_messages.extend`.

### `ConversionPipelineSteps._resolve_program_kind` - L191-L208

```python
_resolve_program_kind(self, *, conversion_input: ConversionInput, source_text: str, validation_messages: list[str]) -> str
```

Measure UPDATE vs RETRIEVAL from the EXPANDED source.

Observed calls (lexical order): `getattr`, `self._input_declares_update`, `ProgramKindResolver`, `ProgramKindResolver().resolve`, `validation_messages.extend`.

Control points:

- L200: `if declared is None`

### `ConversionPipelineSteps._input_declares_update` - L210-L225

```python
_input_declares_update(self, conversion_input: ConversionInput) -> bool | None
```

What the input believes, or None when it is silent.

Observed calls (lexical order): `getattr`, `callable`, `bool`, `probe`.

Control points:

- L220: `if not callable(probe)`

### `ConversionPipelineSteps._hand_off_program_kind` - L227-L257

```python
_hand_off_program_kind(self, *, component, component_name: str, program_kind: str, validation_messages: list[str]) -> None
```

Tell a composer the kind, or report that it will guess.

Observed calls (lexical order): `hasattr`, `validation_messages.append`, `PROGRAM_KIND_HANDOFF_REFUSED.format`, `setattr`, `PROGRAM_KIND_HANDOFF_OK.format`.

Control points:

- L236: `if component is None`
- L239: `if not hasattr(component, PROGRAM_KIND_ATTRIBUTE)`

### `ConversionPipelineSteps._statement_transformer` - L262-L275

```python
_statement_transformer(self, transformers: dict)
```

The IdmsStatementTransformer behind the COBOL transformer.

Observed calls (lexical order): `(transformers or {}).get`, `getattr`.

Control points:

- L271: `if cobol_transformer is None`

### `ConversionPipelineSteps._source_proven_lrf_select_columns` - L278-L384

```python
_source_proven_lrf_select_columns(source_text: str, mapping_repository, record_name: str) -> list[str]
```

Return mapped columns referenced after an LRF keyed parent read.

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.to_cobol`, `str`, `str(source_text or '').splitlines`, `raw.rstrip`, `len`, `line[:6].strip`, `line[:6].strip().isdigit`, `line.lstrip`, `line.lstrip().startswith`, `line.upper`, `logical_lines.append`, `'\n'.join`, `re.escape`, `re.search`, `access.end`.
Another 24 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L290: `if not record or not record_display`
- L294: `for raw in str(source_text or '').splitlines()`
- L296: `if len(line) > 6 and line[:6].strip().isdigit()`
- L297: `if line[6] in '*/'`
- L300: `if line.lstrip().startswith(('*', '/*'))`
- L305: `if not access`
- L320: `for row in rows`
- L324: `if parts and parts[0].isdigit()`
- Another 12 conditions/loops exist in this source span.

### `ConversionPipelineSteps._publish_lr_retrieval_state` - L386-L529

```python
_publish_lr_retrieval_state(self, *, transformers: dict, program_kind: str, source_text: str, repositories: dict, resolvers: dict, validation_messages: list[str]) -> None
```

Deliver the kind and the LRF keyed-parent records.

Observed calls (lexical order): `self._statement_transformer`, `validation_messages.append`, `self._hand_off_program_kind`, `(transformers or {}).get`, `set`, `getattr`, `setattr`, `LRF_CALC_RECORDS_PUBLISHED.format`, `len`, `', '.join`, `sorted`, `self._source_proven_lrf_select_columns`, `NameNormalizer.normalize`, `NameNormalizer.to_cobol`, `LrfKeyBindingPlanner`, `repositories.get`.
Another 9 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L415: `if statement_transformer is None`
- L439: `if records`
- L455: `for parent in sorted(records)`
- L461: `if not required_columns`
- L487: `for parent in sorted(records)`
- L489: `if diagnostics`
- L491: `if required`
- L493: `if moves`
- Another 3 conditions/loops exist in this source span.

### `ConversionPipelineSteps._restart_dclgen_resolver` - L534-L553

```python
_restart_dclgen_resolver(self, validation_messages: list[str])
```

The resolver that turns DCLGEN columns into a restart role.

Observed calls (lexical order): `__import__`, `getattr`, `getattr(module, RESTART_DCLGEN_CLASS)`, `validation_messages.append`, `type`.

### `ConversionPipelineSteps._restart_context` - L555-L620

```python
_restart_context(self, *, conversion_input: ConversionInput, source_text: str, program_kind: str, validation_messages: list[str])
```

Build the run-scoped restart context, or None with a reason.

Observed calls (lexical order): `RestartTotalsResolver`, `tuple`, `UPDATE_RESTART_WS_NAMES.get`, `str`, `str(UPDATE_RESTART_WS_NAMES.get(key, '') or '').strip`, `resolver.resolve`, `str(source_text or '').splitlines`, `validation_messages.extend`, `RestartContextBuilder`, `self._restart_dclgen_resolver`, `builder.build`.

Control points:

- L595: `if is_update`

### `ConversionPipelineSteps._apply_legacy_restart_generator` - L622-L649

```python
_apply_legacy_restart_generator(self, *, converted_cobol: str, conversion_input: ConversionInput, operations: list, generators: dict, restart_context, validation_messages: list[str]) -> str
```

The LEGACY restart path, run only when nothing better can.

Observed calls (lexical order): `validation_messages.append`, `generators['select_paragraph'].apply`, `validation_messages.extend`.

Control points:

- L639: `if GATE_LEGACY_RESTART_GENERATOR and restart_context is not None`

### `ConversionPipelineSteps._apply_db2_infrastructure` - L654-L752

```python
_apply_db2_infrastructure(self, *, converted_cobol: str, operations: list, generators: dict, composers: dict, validation_messages: list[str], lrf_source_text: str | None=None) -> str
```

Observed calls (lexical order): `generators['db2_infrastructure'].apply`, `validation_messages.extend`, `generators['cursor_paragraph'].apply`, `hasattr`, `generators['cursor_paragraph'].augment_lrf_procedure_division`, `composers['sqlcode_cleanup'].compose`, `self._component_messages`, `self._stage`, `composers.get`, `validation_messages.append`, `date_compare.compose`.

Control points:

- L684: `if hasattr(generators['cursor_paragraph'], 'augment_lrf_procedure_division')`
- L744: `if date_compare is None`

### `ConversionPipelineSteps._apply_cleanup_composers` - L762-L807

```python
_apply_cleanup_composers(self, *, converted_cobol: str, composers: dict, validation_messages: list[str]) -> str
```

Content-level cleanup, before any layout decision is taken.

Observed calls (lexical order): `composers[name].compose`, `validation_messages.extend`, `self._component_messages`.

Control points:

- L797: `for name in ('feedback_cleanup', 'unnecessary_comments_cleanup', 'update_program_feedback')`

### `ConversionPipelineSteps._apply_commit_cleanup` - L809-L839

```python
_apply_commit_cleanup(self, *, converted_cobol: str, composers: dict, program_kind: str, validation_messages: list[str]) -> str
```

Remove a COMMIT from a read-only program - and only then.

Observed calls (lexical order): `composers.get`, `validation_messages.append`, `self._hand_off_program_kind`, `commit_cleanup.compose`, `validation_messages.extend`, `self._component_messages`.

Control points:

- L825: `if commit_cleanup is None`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
