# `converter/composers/update_sql_cleanup_base.py`

Source: [converter/composers/update_sql_cleanup_base.py](../../../../converter/composers/update_sql_cleanup_base.py) | 104 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `967f62951a74e5eeefeb7fbf453471f08da6c9da627b84b937cf728681103894`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared base for update-program SQL cleanup composers.

## Import declarations

```python
from __future__ import annotations
from converter.composers.update_sql_cleanup.column_mixin import ColumnMixin
from converter.composers.update_sql_cleanup.key_column_mixin import KeyColumnMixin
from converter.composers.update_sql_cleanup.scan_mixin import ScanMixin
from converter.composers.update_sql_cleanup.sql_line_mixin import SqlLineMixin
from converter.composers.update_sql_cleanup.update_sql_cleanup_patterns import CONVERTED_MODIFY_PATTERN, CONVERTED_OBTAIN_CALC_PATTERN, END_IF_PATTERN, EXEC_SQL_END_PATTERN, EXEC_SQL_START_PATTERN, INCLUDE_PATTERN, LINKAGE_SECTION_PATTERN, MALFORMED_SQLERROR_ENDIF_PATTERN, MOVE_TO_BARE_FIELD_PATTERN, MOVE_TO_DCL_HOST_PATTERN, SQL_LOCATION_PATTERN, SQLCODE_IF_PATTERN, STOP_RUN_PATTERN, TIMESTAMP_PARAGRAPH_PATTERN
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from rules.update_sql_cleanup_rules import IDENTITY_KEY_PREFIXES, INSERT_ONLY_AUDIT_PREFIXES, PROTECTED_BARE_TARGET_PREFIXES, UPDATE_AUDIT_PREFIXES
```

## Local dependency notes

- [converter/composers/update_sql_cleanup/column_mixin.py](update_sql_cleanup/column_mixin.md)
- [converter/composers/update_sql_cleanup/key_column_mixin.py](update_sql_cleanup/key_column_mixin.md)
- [converter/composers/update_sql_cleanup/scan_mixin.py](update_sql_cleanup/scan_mixin.md)
- [converter/composers/update_sql_cleanup/sql_line_mixin.py](update_sql_cleanup/sql_line_mixin.md)
- [converter/composers/update_sql_cleanup/update_sql_cleanup_patterns.py](update_sql_cleanup/update_sql_cleanup_patterns.md)
- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [rules/update_sql_cleanup_rules.py](../../rules/update_sql_cleanup_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_program_structure_feedback_composer.py](update_program_structure_feedback_composer.md)
- [converter/composers/update_sql_cleanup_composer.py](update_sql_cleanup_composer.md)
- [tests/update_sql_cleanup/conftest.py](../../tests/update_sql_cleanup/conftest.md)

## Symbol contracts and control points

### `UpdateSqlCleanupBase` - L65-L104

```python
class UpdateSqlCleanupBase(ScanMixin, KeyColumnMixin, ColumnMixin, SqlLineMixin)
```

Declared class/data-model fields:

```python
CONVERTED_OBTAIN_CALC_PATTERN = CONVERTED_OBTAIN_CALC_PATTERN
CONVERTED_MODIFY_PATTERN = CONVERTED_MODIFY_PATTERN
EXEC_SQL_START_PATTERN = EXEC_SQL_START_PATTERN
EXEC_SQL_END_PATTERN = EXEC_SQL_END_PATTERN
INCLUDE_PATTERN = INCLUDE_PATTERN
SQLCODE_IF_PATTERN = SQLCODE_IF_PATTERN
END_IF_PATTERN = END_IF_PATTERN
MALFORMED_SQLERROR_ENDIF_PATTERN = MALFORMED_SQLERROR_ENDIF_PATTERN
MOVE_TO_BARE_FIELD_PATTERN = MOVE_TO_BARE_FIELD_PATTERN
MOVE_TO_DCL_HOST_PATTERN = MOVE_TO_DCL_HOST_PATTERN
SQL_LOCATION_PATTERN = SQL_LOCATION_PATTERN
LINKAGE_SECTION_PATTERN = LINKAGE_SECTION_PATTERN
TIMESTAMP_PARAGRAPH_PATTERN = TIMESTAMP_PARAGRAPH_PATTERN
STOP_RUN_PATTERN = STOP_RUN_PATTERN
PROTECTED_BARE_TARGET_PREFIXES = PROTECTED_BARE_TARGET_PREFIXES
UPDATE_AUDIT_PREFIXES = UPDATE_AUDIT_PREFIXES
INSERT_ONLY_AUDIT_PREFIXES = INSERT_ONLY_AUDIT_PREFIXES
IDENTITY_KEY_PREFIXES = IDENTITY_KEY_PREFIXES
```

### `UpdateSqlCleanupBase.__init__` - L93-L104

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository, table_name_resolver: TableNameResolver, host_variable_resolver: HostVariableResolver) -> None
```

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
