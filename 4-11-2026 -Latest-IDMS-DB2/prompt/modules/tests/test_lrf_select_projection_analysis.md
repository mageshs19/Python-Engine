# `tests/test_lrf_select_projection_analysis.py`

Source: [tests/test_lrf_select_projection_analysis.py](../../../tests/test_lrf_select_projection_analysis.py) | 134 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ca49fb35aeb9fd8a2b8ac0669e05c971d81a4a19020b85deb0fe3334c0225d3c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Source-driven projection tests for generic LRF keyed parent SELECTs.

## Import declarations

```python
from converter.pipeline.conversion.conversion_pipeline_steps import ConversionPipelineSteps
from converter.domain.models import SheetMappingRow
from converter.repositories.mapping_repository import MappingRepository
from pathlib import Path
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from tests.workspace_fixtures import mapping_export, expanded_program
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/parsers/sheet_mapping_parser.py](../converter/parsers/sheet_mapping_parser.md)
- [converter/pipeline/conversion/conversion_pipeline_steps.py](../converter/pipeline/conversion/conversion_pipeline_steps.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [tests/workspace_fixtures.py](workspace_fixtures.md)

## Symbol contracts and control points

### `test_lrf_projection_uses_only_mapped_fields_referenced_after_keyed_read` - L5-L20

```python
test_lrf_projection_uses_only_mapped_fields_referenced_after_keyed_read(transformer_context)
```

Observed calls (lexical order): `ConversionPipelineSteps._source_proven_lrf_select_columns`.

### `test_lrf_projection_ignores_fields_used_only_before_keyed_read` - L23-L38

```python
test_lrf_projection_ignores_fields_used_only_before_keyed_read(transformer_context)
```

Observed calls (lexical order): `ConversionPipelineSteps._source_proven_lrf_select_columns`.

### `test_keyed_select_projection_and_into_are_aligned` - L41-L55

```python
test_keyed_select_projection_and_into_are_aligned(transformer_context)
```

Observed calls (lexical order): `generator.select_by_key`, `'\n'.join`, `'\n'.join(sql).upper`, `text.split`, `text.split('INTO', 1)[1].split`, `text.count`.

### `test_empty_source_proven_projection_fails_closed` - L58-L66

```python
test_empty_source_proven_projection_fails_closed(transformer_context)
```

Observed calls (lexical order): `generator.select_by_key`, `'\n'.join`, `'\n'.join(sql).upper`.

### `test_group_move_includes_mapped_descendants_but_diagnostic_display_does_not` - L69-L103

```python
test_group_move_includes_mapped_descendants_but_diagnostic_display_does_not()
```

Observed calls (lexical order): `MappingRepository`, `SheetMappingRow`, `ConversionPipelineSteps._source_proven_lrf_select_columns`.

### `test_vmdz4310_projection_is_derived_from_real_mapping_and_expanded_source` - L106-L134

```python
test_vmdz4310_projection_is_derived_from_real_mapping_and_expanded_source()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `mapping_export`, `expanded_program`, `SheetMappingParser`, `SheetMappingParser().parse_uploaded_file`, `_UploadedMapping`, `ConversionPipelineSteps._source_proven_lrf_select_columns`, `source_path.read_text`, `MappingRepository`, `len`.

### `test_vmdz4310_projection_is_derived_from_real_mapping_and_expanded_source._UploadedMapping` - L117-L121

```python
class _UploadedMapping()
```

Declared class/data-model fields:

```python
name = mapping_path.name
```

### `test_vmdz4310_projection_is_derived_from_real_mapping_and_expanded_source._UploadedMapping.getvalue` - L120-L121

```python
getvalue(self)
```

Observed calls (lexical order): `mapping_path.read_bytes`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
