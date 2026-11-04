# `tests/test_unqualified_field_usage.py`

Source: [tests/test_unqualified_field_usage.py](../../../tests/test_unqualified_field_usage.py) | 42 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `0e646e3452cafcc11ba3a54b2c9e702a268ec036f45c0e8911c7fd7738fe2fac`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.field_usage_analyzer import FieldUsageAnalyzer
from converter.domain.models import SheetMappingRow
from converter.repositories.mapping_repository import MappingRepository
```

## Local dependency notes

- [converter/analyzers/field_usage_analyzer.py](../converter/analyzers/field_usage_analyzer.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)

## Symbol contracts and control points

### `_Tables` - L6-L8

```python
class _Tables()
```

### `_Tables.table_for_record` - L7-L8

```python
table_for_record(self, record)
```

Observed calls (lexical order): `{'VMBEFF': 'DZBEFFTV', 'VMBEVEF': 'DZEVEFTV'}.get`.

### `_analyzer` - L11-L12

```python
_analyzer(rows)
```

Observed calls (lexical order): `FieldUsageAnalyzer`, `MappingRepository`, `_Tables`.

### `test_unqualified_unique_source_fields_are_attributed_to_owning_record` - L15-L28

```python
test_unqualified_unique_source_fields_are_attributed_to_owning_record()
```

Observed calls (lexical order): `SheetMappingRow`, `_analyzer`, `_analyzer(rows).analyze`.

### `test_ambiguous_unqualified_source_field_is_not_guessed` - L31-L42

```python
test_ambiguous_unqualified_source_field_is_not_guessed()
```

Observed calls (lexical order): `SheetMappingRow`, `_analyzer`, `_analyzer(rows).analyze`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
