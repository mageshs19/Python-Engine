# `tests/test_field_reference_group_issue_scope.py`

Source: [tests/test_field_reference_group_issue_scope.py](../../../tests/test_field_reference_group_issue_scope.py) | 36 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `867bfae41c73e65a124a7b5475ca0879ca0cfefc68715603f0f3984cdbbf144c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.transformers.field_reference_context_builder import FieldReferenceContextBuilder
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../converter/resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)
- [converter/transformers/field_reference_context_builder.py](../converter/transformers/field_reference_context_builder.md)

## Symbol contracts and control points

### `test_group_decomposition_facts_are_stored_without_workbook_wide_warnings` - L9-L36

```python
test_group_decomposition_facts_are_stored_without_workbook_wide_warnings()
```

Observed calls (lexical order): `SheetMappingRow`, `DclgenRepository`, `DclgenColumn`, `MappingRepository`, `TableNameResolver`, `HostVariableResolver`, `FieldReferenceContextBuilder`, `builder.build_reference_maps`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
