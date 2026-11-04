# `converter/analyzers/field_usage_analyzer.py`

Source: [converter/analyzers/field_usage_analyzer.py](../../../../converter/analyzers/field_usage_analyzer.py) | 175 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `b62e3b51d42fa619b7f602fd8f27c5663d816e63cde59fbc282b1a0526d82858`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L171)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.field_usage_capture_service import FieldUsageCaptureService
from converter.analyzers.field_usage_context_mapper import FieldUsageContextMapper
from converter.analyzers.field_usage_models import FieldUsage, FieldUsageAnalysis
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from patterns.field_usage_analysis_patterns import COMMENT_PATTERN, CONDITION_PATTERN, DIVISION_PATTERN, EXEC_SQL_END_PATTERN, EXEC_SQL_START_PATTERN
from patterns.sequence_patterns import strip_sequence_numbers
```

## Local dependency notes

- [converter/analyzers/field_usage_capture_service.py](field_usage_capture_service.md)
- [converter/analyzers/field_usage_context_mapper.py](field_usage_context_mapper.md)
- [converter/analyzers/field_usage_models.py](field_usage_models.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [patterns/field_usage_analysis_patterns.py](../../patterns/field_usage_analysis_patterns.md)
- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_spec_builder_lrf_patch.py](../generators/db2_infrastructure/cursor_spec_builder_lrf_patch.md)
- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](../generators/db2_infrastructure/spec_builder/cursor_spec_builder.md)
- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [converter/resolvers/cursor_column_resolver.py](../resolvers/cursor_column_resolver.md)
- [converter/resolvers/cursor_field_usage_column_selector.py](../resolvers/cursor_field_usage_column_selector.md)
- [tests/test_unqualified_field_usage.py](../../tests/test_unqualified_field_usage.md)

## Symbol contracts and control points

### `FieldUsageAnalyzer` - L25-L168

```python
class FieldUsageAnalyzer()
```

Generic COBOL field-usage analyzer.

### `FieldUsageAnalyzer.__init__` - L39-L61

```python
__init__(self, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver) -> None
```

Observed calls (lexical order): `FieldUsageContextMapper`, `self.context_mapper.mapping_records`, `self.context_mapper.group_to_record_map`, `FieldUsageCaptureService`, `self.context_mapper.unique_source_field_to_record_map`.

### `FieldUsageAnalyzer.analyze` - L63-L137

```python
analyze(self, cobol_text: str) -> FieldUsageAnalysis
```

Observed calls (lexical order): `FieldUsageAnalysis`, `enumerate`, `str`, `str(cobol_text or '').splitlines`, `strip_sequence_numbers`, `strip_sequence_numbers(raw_line).strip`, `COMMENT_PATTERN.match`, `DIVISION_PATTERN.match`, `division_match.group`, `division_match.group(1).upper`, `EXEC_SQL_START_PATTERN.match`, `self.capture_service.capture_dclgen_references`, `EXEC_SQL_END_PATTERN.match`, `CONDITION_PATTERN.match`, `bool`, `self.capture_service.capture_idms_qualified_references`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L71: `for (line_number, raw_line) in enumerate(str(cobol_text or '').splitlines(), start=1)`
- L77: `if not logical`
- L80: `if COMMENT_PATTERN.match(logical)`
- L85: `if division_match`
- L89: `if EXEC_SQL_START_PATTERN.match(logical)`
- L92: `if inside_exec_sql`
- L100: `if EXEC_SQL_END_PATTERN.match(logical)`
- L105: `if not inside_procedure`

### `FieldUsageAnalyzer._finalize_all_fields` - L139-L148

```python
_finalize_all_fields(self, result: FieldUsageAnalysis) -> None
```

Observed calls (lexical order): `result.usage_by_record.values`, `usage.all_fields.update`.

Control points:

- L143: `for usage in result.usage_by_record.values()`

### `FieldUsageAnalyzer._append_diagnostics` - L150-L168

```python
_append_diagnostics(self, result: FieldUsageAnalysis) -> None
```

Observed calls (lexical order): `result.diagnostics.append`, `len`, `result.usage_by_record.items`, `sorted`.

Control points:

- L159: `for (record_name, usage) in sorted(result.usage_by_record.items())`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
