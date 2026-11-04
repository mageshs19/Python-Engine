# `tests/test_sql_insert_sequence_metadata.py`

Source: [tests/test_sql_insert_sequence_metadata.py](../../../tests/test_sql_insert_sequence_metadata.py) | 86 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `aad4e20c653b896a5eb85fbc5e4953460a0077536247d47b1bc01d5a3ef59514`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.generators.sql.sql_column_resolver import SqlColumnResolver
from converter.generators.sql.sql_line_builder import SqlLineBuilder
from converter.generators.sql.sql_statement_builder import SqlStatementBuilder
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/generators/sql/sql_column_resolver.py](../converter/generators/sql/sql_column_resolver.md)
- [converter/generators/sql/sql_line_builder.py](../converter/generators/sql/sql_line_builder.md)
- [converter/generators/sql/sql_statement_builder.py](../converter/generators/sql/sql_statement_builder.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../converter/resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)

## Symbol contracts and control points

### `_builder` - L11-L25

```python
_builder(rows, columns)
```

Observed calls (lexical order): `MappingRepository`, `DclgenRepository`, `TableNameResolver`, `SqlColumnResolver`, `HostVariableResolver`, `SqlLineBuilder`, `SqlStatementBuilder`.

### `test_insert_sequence_is_inferred_from_mapping_not_program_or_table_literals` - L28-L62

```python
test_insert_sequence_is_inferred_from_mapping_not_program_or_table_literals()
```

Observed calls (lexical order): `SheetMappingRow`, `DclgenColumn`, `'\n'.join`, `_builder`, `_builder(rows, dclgen_columns).insert`.

### `test_sequence_key_without_supported_sequence_convention_fails_closed` - L65-L86

```python
test_sequence_key_without_supported_sequence_convention_fails_closed()
```

Observed calls (lexical order): `SheetMappingRow`, `DclgenColumn`, `'\n'.join`, `_builder`, `_builder(rows, dclgen_columns).insert`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
