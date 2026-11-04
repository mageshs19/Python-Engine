# `converter/analyzers/metadata_service.py`

Source: [converter/analyzers/metadata_service.py](../../../../converter/analyzers/metadata_service.py) | 214 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `1a73d2059710c91c150ec5c5740953a4cbe1dbd55ce3efd5bacffc9874db28b7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from collections import defaultdict
from converter.domain.models import RelationshipSummary, RecordSummary, SheetMappingRow
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/output_tabs.py](../ui/output_tabs.md)

## Symbol contracts and control points

### `MetadataService` - L11-L214

```python
class MetadataService()
```

Builds metadata summaries from Sheet Mapping rows.

### `MetadataService.record_summaries` - L22-L66

```python
record_summaries(self, rows: list[SheetMappingRow]) -> list[RecordSummary]
```

Observed calls (lexical order): `defaultdict`, `NameNormalizer.normalize`, `grouped[record].append`, `grouped.items`, `sorted`, `self._first_db2_table`, `output.append`, `RecordSummary`, `len`, `set`.

Control points:

- L28: `for row in rows`
- L31: `if not record`
- L38: `for (record_name, record_rows) in sorted(grouped.items())`

### `MetadataService.column_rows` - L68-L104

```python
column_rows(self, rows: list[SheetMappingRow]) -> list[dict[str, str]]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `output.append`.

Control points:

- L74: `for row in rows`
- L79: `if not record and (not table) and (not column)`

### `MetadataService.relationship_summaries` - L106-L149

```python
relationship_summaries(self, rows: list[SheetMappingRow]) -> list[RelationshipSummary]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `self._infer_parent_record_from_reference`, `seen.add`, `output.append`, `RelationshipSummary`.

Control points:

- L113: `for row in rows`
- L116: `if not relation`
- L134: `if key in seen`

### `MetadataService.mapping_preview_rows` - L151-L182

```python
mapping_preview_rows(self, rows: list[SheetMappingRow]) -> list[dict[str, str]]
```

Observed calls (lexical order): `output.append`.

Control points:

- L157: `for row in rows`

### `MetadataService._first_db2_table` - L184-L194

```python
_first_db2_table(self, rows: list[SheetMappingRow]) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`.

Control points:

- L188: `for row in rows`
- L191: `if table`

### `MetadataService._infer_parent_record_from_reference` - L196-L214

```python
_infer_parent_record_from_reference(self, row: SheetMappingRow) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `normalized.split`, `len`.

Control points:

- L200: `if row.cross_application_db2_table`
- L205: `if not value`
- L211: `if len(parts) >= 2`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
