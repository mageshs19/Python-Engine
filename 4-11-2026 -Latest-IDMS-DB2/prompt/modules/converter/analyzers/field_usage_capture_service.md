# `converter/analyzers/field_usage_capture_service.py`

Source: [converter/analyzers/field_usage_capture_service.py](../../../../converter/analyzers/field_usage_capture_service.py) | 263 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `8fde7bf6b3b5c6b29aa3f4917982806a8fcf006a6785fcd1bf481b494471d5f5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.field_usage_models import FieldUsage, FieldUsageAnalysis
from converter.services.name_normalizer import NameNormalizer
from patterns.field_usage_analysis_patterns import DCLGEN_DOT_PATTERN, DCLGEN_OF_PATTERN, BARE_IDENTIFIER_PATTERN, MOVE_PATTERN, QUALIFIED_REFERENCE_PATTERN
from rules.field_usage_rules import DCLGEN_GROUP_PREFIX, OUTPUT_TARGET_PREFIXES
```

## Local dependency notes

- [converter/analyzers/field_usage_models.py](field_usage_models.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/field_usage_analysis_patterns.py](../../patterns/field_usage_analysis_patterns.md)
- [rules/field_usage_rules.py](../../rules/field_usage_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_analyzer.py](field_usage_analyzer.md)

## Symbol contracts and control points

### `FieldUsageCaptureService` - L21-L263

```python
class FieldUsageCaptureService()
```

Captures field usage from individual COBOL logical statements.

### `FieldUsageCaptureService.__init__` - L29-L38

```python
__init__(self, *, mapping_records: set[str], group_to_record: dict[str, str], unique_source_field_to_record: dict[str, str] | None=None) -> None
```

### `FieldUsageCaptureService.capture_idms_qualified_references` - L40-L64

```python
capture_idms_qualified_references(self, *, logical: str, result: FieldUsageAnalysis, is_condition: bool) -> None
```

Observed calls (lexical order): `QUALIFIED_REFERENCE_PATTERN.finditer`, `NameNormalizer.to_cobol`, `match.group`, `NameNormalizer.normalize`, `record_name.startswith`, `self.usage_for_record`, `usage.all_fields.add`, `usage.condition_fields.add`.

Control points:

- L47: `for match in QUALIFIED_REFERENCE_PATTERN.finditer(logical)`
- L51: `if not field_name or not record_name`
- L54: `if record_name.startswith(DCLGEN_GROUP_PREFIX)`
- L57: `if record_name not in self.mapping_records`
- L63: `if is_condition`

### `FieldUsageCaptureService.capture_unqualified_source_references` - L66-L89

```python
capture_unqualified_source_references(self, *, logical: str, result: FieldUsageAnalysis, is_condition: bool) -> None
```

Capture uniquely owned legacy fields used without qualification.

Observed calls (lexical order): `BARE_IDENTIFIER_PATTERN.finditer`, `NameNormalizer.normalize`, `match.group`, `self.unique_source_field_to_record.get`, `self.usage_for_record`, `NameNormalizer.to_cobol`, `usage.all_fields.add`, `usage.condition_fields.add`.

Control points:

- L80: `for match in BARE_IDENTIFIER_PATTERN.finditer(logical)`
- L83: `if not field or not record`
- L88: `if is_condition`

### `FieldUsageCaptureService.capture_dclgen_references` - L91-L110

```python
capture_dclgen_references(self, *, logical: str, result: FieldUsageAnalysis, is_condition: bool, is_output: bool) -> None
```

Observed calls (lexical order): `self._capture_dclgen_of_references`, `self._capture_dclgen_dot_references`.

### `FieldUsageCaptureService.capture_move_usage` - L112-L135

```python
capture_move_usage(self, *, logical: str, result: FieldUsageAnalysis) -> None
```

Observed calls (lexical order): `MOVE_PATTERN.search`, `match.group`, `self._is_output_target`, `self._capture_move_source_usage`, `self._capture_move_target_usage`.

Control points:

- L120: `if not match`

### `FieldUsageCaptureService.usage_for_record` - L137-L147

```python
usage_for_record(self, result: FieldUsageAnalysis, record_name: str) -> FieldUsage
```

Observed calls (lexical order): `NameNormalizer.normalize`, `FieldUsage`.

Control points:

- L144: `if record not in result.usage_by_record`

### `FieldUsageCaptureService._capture_dclgen_of_references` - L149-L172

```python
_capture_dclgen_of_references(self, *, logical: str, result: FieldUsageAnalysis, is_condition: bool, is_output: bool) -> None
```

Observed calls (lexical order): `DCLGEN_OF_PATTERN.finditer`, `NameNormalizer.to_cobol`, `match.group`, `NameNormalizer.normalize`, `self.group_to_record.get`, `self.usage_for_record`, `usage.dclgen_host_fields.add`, `usage.condition_fields.add`, `usage.output_fields.add`.

Control points:

- L157: `for match in DCLGEN_OF_PATTERN.finditer(logical)`
- L162: `if not field_name or not record_name`
- L168: `if is_condition`
- L171: `if is_output`

### `FieldUsageCaptureService._capture_dclgen_dot_references` - L174-L197

```python
_capture_dclgen_dot_references(self, *, logical: str, result: FieldUsageAnalysis, is_condition: bool, is_output: bool) -> None
```

Observed calls (lexical order): `DCLGEN_DOT_PATTERN.finditer`, `NameNormalizer.to_cobol`, `match.group`, `NameNormalizer.normalize`, `self.group_to_record.get`, `self.usage_for_record`, `usage.dclgen_host_fields.add`, `usage.condition_fields.add`, `usage.output_fields.add`.

Control points:

- L182: `for match in DCLGEN_DOT_PATTERN.finditer(logical)`
- L187: `if not field_name or not record_name`
- L193: `if is_condition`
- L196: `if is_output`

### `FieldUsageCaptureService._capture_move_source_usage` - L199-L230

```python
_capture_move_source_usage(self, *, source_text: str, result: FieldUsageAnalysis, is_output: bool) -> None
```

Observed calls (lexical order): `QUALIFIED_REFERENCE_PATTERN.finditer`, `NameNormalizer.to_cobol`, `source_match.group`, `NameNormalizer.normalize`, `record_name.startswith`, `self.usage_for_record`, `usage.move_source_fields.add`, `usage.output_fields.add`, `self.capture_dclgen_references`.

Control points:

- L206: `for source_match in QUALIFIED_REFERENCE_PATTERN.finditer(source_text)`
- L210: `if not field_name or not record_name`
- L213: `if record_name.startswith(DCLGEN_GROUP_PREFIX)`
- L216: `if record_name not in self.mapping_records`
- L222: `if is_output`

### `FieldUsageCaptureService._capture_move_target_usage` - L232-L252

```python
_capture_move_target_usage(self, *, target_text: str, result: FieldUsageAnalysis) -> None
```

Observed calls (lexical order): `QUALIFIED_REFERENCE_PATTERN.finditer`, `NameNormalizer.to_cobol`, `target_match.group`, `NameNormalizer.normalize`, `record_name.startswith`, `self.usage_for_record`, `usage.move_target_fields.add`.

Control points:

- L238: `for target_match in QUALIFIED_REFERENCE_PATTERN.finditer(target_text)`
- L242: `if not field_name or not record_name`
- L245: `if record_name.startswith(DCLGEN_GROUP_PREFIX)`
- L248: `if record_name not in self.mapping_records`

### `FieldUsageCaptureService._is_output_target` - L254-L263

```python
_is_output_target(self, target_text: str) -> bool
```

Observed calls (lexical order): `str`, `str(target_text or '').upper`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
