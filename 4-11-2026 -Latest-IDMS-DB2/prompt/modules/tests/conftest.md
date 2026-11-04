# `tests/conftest.py`

Source: [tests/conftest.py](../../../tests/conftest.py) | 205 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `6bf52d781019878c20d1517382419e56df98240b722f93b46d931cd30205131b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared pytest configuration and fixtures.

## Module-level bindings

`PROJECT_ROOT` (L43), `SRC_DIR` (L44)

## Import declarations

```python
from __future__ import annotations
import sys
from pathlib import Path
import pytest
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.generators.sql_error_generator import SqlErrorGenerator
from converter.generators.sql_generator import SqlGenerator
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.transformers.idms_statement_transformer import IdmsStatementTransformer
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/generators/sql_error_generator.py](../converter/generators/sql_error_generator.md)
- [converter/generators/sql_generator.py](../converter/generators/sql_generator.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/column_name_resolver.py](../converter/resolvers/column_name_resolver.md)
- [converter/resolvers/cursor_name_resolver.py](../converter/resolvers/cursor_name_resolver.md)
- [converter/resolvers/host_variable_resolver.py](../converter/resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)
- [converter/transformers/idms_statement_transformer.py](../converter/transformers/idms_statement_transformer.md)

## Symbol contracts and control points

### `build_sheet_mapping_rows` - L83-L100

```python
build_sheet_mapping_rows() -> list[SheetMappingRow]
```

One mapped IDMS record, VMB-FAR, with a CALC primary key.

Observed calls (lexical order): `SheetMappingRow`.

### `build_dclgen_columns` - L103-L116

```python
build_dclgen_columns() -> list[DclgenColumn]
```

DCLGEN view DZBFARTV for the mapped record.

Observed calls (lexical order): `DclgenColumn`.

### `build_transformer_context` - L119-L171

```python
build_transformer_context() -> dict
```

Fully wired IdmsStatementTransformer plus its collaborators.

Observed calls (lexical order): `MappingRepository`, `build_sheet_mapping_rows`, `DclgenRepository`, `build_dclgen_columns`, `TableNameResolver`, `ColumnNameResolver`, `HostVariableResolver`, `CursorNameResolver`, `SqlGenerator`, `IdmsStatementTransformer`, `SqlErrorGenerator`.

### `transformer_context` - L178-L180

```python
transformer_context() -> dict
```

Fresh transformer context per test. Never shared between tests.

Observed calls (lexical order): `build_transformer_context`.

### `statement_transformer` - L184-L186

```python
statement_transformer(transformer_context) -> IdmsStatementTransformer
```

The wired IdmsStatementTransformer on its own.

### `transform_line` - L190-L205

```python
transform_line(statement_transformer)
```

Convert one IDMS line. Returns (joined_text, opened_set).

### `transform_line._transform` - L193-L203

```python
_transform(line: str, current_division: str='PROCEDURE', sql_error_paragraph: str='SQL-ERROR') -> tuple[str, str]
```

Observed calls (lexical order): `statement_transformer.transform_line`, `'\n'.join`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
