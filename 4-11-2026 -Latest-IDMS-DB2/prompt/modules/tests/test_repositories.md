# `tests/test_repositories.py`

Source: [tests/test_repositories.py](../../../tests/test_repositories.py) | 91 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `6018932531674f4ee6ec1889d808ef4460b22b3c0de492994ce46ef29e4d2822`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import CopybookField, DclgenColumn, SheetMappingRow
from converter.repositories.copybook_repository import CopybookRepository
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/copybook_repository.py](../converter/repositories/copybook_repository.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)

## Symbol contracts and control points

### `test_mapping_repository_returns_records` - L7-L18

```python
test_mapping_repository_returns_records()
```

Observed calls (lexical order): `MappingRepository`, `SheetMappingRow`, `repository.records`.

### `test_mapping_repository_finds_rows_for_record` - L21-L35

```python
test_mapping_repository_finds_rows_for_record()
```

Observed calls (lexical order): `MappingRepository`, `SheetMappingRow`, `repository.rows_for_record`, `len`.

### `test_mapping_repository_returns_table_for_record` - L38-L48

```python
test_mapping_repository_returns_table_for_record()
```

Observed calls (lexical order): `MappingRepository`, `SheetMappingRow`, `repository.db2_table_for_record`.

### `test_dclgen_repository_has_table` - L51-L62

```python
test_dclgen_repository_has_table()
```

Observed calls (lexical order): `DclgenRepository`, `DclgenColumn`, `repository.has_table`.

### `test_dclgen_repository_host_for_column` - L65-L76

```python
test_dclgen_repository_host_for_column()
```

Observed calls (lexical order): `DclgenRepository`, `DclgenColumn`, `repository.host_for_column`.

### `test_copybook_repository_finds_field` - L79-L91

```python
test_copybook_repository_finds_field()
```

Observed calls (lexical order): `CopybookRepository`, `CopybookField`, `repository.has_field`, `repository.picture_for`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
