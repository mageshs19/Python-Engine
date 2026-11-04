# `converter/resolvers/cursor_field_usage_column_selector.py`

Source: [converter/resolvers/cursor_field_usage_column_selector.py](../../../../converter/resolvers/cursor_field_usage_column_selector.py) | 226 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `479c3709e5df549ce1980a29522a1ad856d750cbf3e780e7e23e74ddb1c53a3e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.field_usage_analyzer import FieldUsageAnalysis
from converter.repositories.mapping_repository import MappingRepository
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/analyzers/field_usage_analyzer.py](../analyzers/field_usage_analyzer.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/cursor_column_resolver.py](cursor_column_resolver.md)
- [tests/test_cursor_group_projection.py](../../tests/test_cursor_group_projection.md)

## Symbol contracts and control points

### `CursorFieldUsageColumnSelector` - L8-L226

```python
class CursorFieldUsageColumnSelector()
```

Resolves cursor SELECT columns from procedure field usage.

### `CursorFieldUsageColumnSelector.__init__` - L16-L20

```python
__init__(self, mapping_repository: MappingRepository) -> None
```

### `CursorFieldUsageColumnSelector.columns_from_field_usage` - L22-L66

```python
columns_from_field_usage(self, record_name: str, field_usage_analysis: FieldUsageAnalysis | None) -> list[str]
```

Observed calls (lexical order): `field_usage_analysis.usage_by_record.get`, `NameNormalizer.normalize`, `sorted`, `self.column_for_source_or_host_field`, `output.append`, `output.extend`, `self.columns_for_group_field`, `self._unique`.

Control points:

- L27: `if field_usage_analysis is None`
- L34: `if usage is None`
- L41: `for field_name in sorted(usage.all_fields)`
- L47: `if column`

### `CursorFieldUsageColumnSelector.column_for_source_or_host_field` - L68-L112

```python
column_for_source_or_host_field(self, record_name: str, source_or_host_field: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `getattr`, `self.extract_source_field`, `NameNormalizer.to_cobol`.

Control points:

- L76: `if not record or not source`
- L81: `for row in rows`
- L87: `if not target_column`
- L109: `if source in source_candidates`

### `CursorFieldUsageColumnSelector.columns_for_group_field` - L115-L175

```python
columns_for_group_field(self, *, record_name: str, source_group_field: str) -> list[str]
```

Return mapped descendant columns for a source group without a column.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `enumerate`, `getattr`, `str`, `str(getattr(row, 'cobol_zone', '') or '').strip`, `self._level_and_field`, `self.extract_source_field`, `columns.append`, `self._unique`.

Control points:

- L131: `if not record or not source`
- L138: `for (index, row) in enumerate(rows)`
- L141: `if field != source`
- L148: `if target or level is None`
- L153: `if group_index < 0`
- L157: `for row in rows[group_index + 1:]`
- L161: `if level is not None and level <= group_level`
- L172: `if target and source_field`

### `CursorFieldUsageColumnSelector._level_and_field` - L178-L185

```python
_level_and_field(value: str) -> tuple[int | None, str]
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().replace`, `text.split`, `len`, `tokens[0].isdigit`, `NameNormalizer.normalize`, `int`.

Control points:

- L181: `if not tokens`
- L183: `if tokens[0].isdigit() and len(tokens) > 1`

### `CursorFieldUsageColumnSelector.extract_source_field` - L187-L205

```python
extract_source_field(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `text.replace`, `text.split`, `len`, `tokens[0].isdigit`.

Control points:

- L193: `if not text`
- L199: `if tokens and tokens[0].isdigit() and (len(tokens) > 1)`
- L202: `if tokens`

### `CursorFieldUsageColumnSelector._unique` - L207-L226

```python
_unique(self, values: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L214: `for value in values`
- L217: `if not normalized`
- L220: `if normalized in seen`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
