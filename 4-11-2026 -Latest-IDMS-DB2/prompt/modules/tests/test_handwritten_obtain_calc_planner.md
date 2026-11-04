# `tests/test_handwritten_obtain_calc_planner.py`

Source: [tests/test_handwritten_obtain_calc_planner.py](../../../tests/test_handwritten_obtain_calc_planner.py) | 82 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a67b3c0b8191f50a05ff2871cf86be66250a712065373f8a83b59ff79867e161`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.lr_access.handwritten_obtain_calc_planner import HandwrittenObtainCalcPlanner
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
```

## Local dependency notes

- [converter/analyzers/lr_access/handwritten_obtain_calc_planner.py](../converter/analyzers/lr_access/handwritten_obtain_calc_planner.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../converter/resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)

## Symbol contracts and control points

### `_planner` - L9-L37

```python
_planner()
```

Observed calls (lexical order): `SheetMappingRow`, `MappingRepository`, `DclgenRepository`, `DclgenColumn`, `TableNameResolver`, `HostVariableResolver`, `HandwrittenObtainCalcPlanner`.

### `_source` - L40-L51

```python
_source(key_move='MOVE INPUT-KEY TO KEY-A OF REC-A')
```

### `test_plans_keyed_existence_read_when_all_key_and_status_proofs_exist` - L54-L59

```python
test_plans_keyed_existence_read_when_all_key_and_status_proofs_exist()
```

Observed calls (lexical order): `_planner`, `_planner().plan`, `_source`, `any`.

### `test_refuses_when_any_key_is_not_assigned_before_access` - L62-L65

```python
test_refuses_when_any_key_is_not_assigned_before_access()
```

Observed calls (lexical order): `_planner`, `_planner().plan`, `_source`, `any`.

### `test_refuses_conditional_key_assignment` - L68-L75

```python
test_refuses_conditional_key_assignment()
```

Observed calls (lexical order): `_source`, `_source().replace`, `_planner`, `_planner().plan`, `any`.

### `test_refuses_missing_zero_or_nonzero_status_guard` - L78-L82

```python
test_refuses_missing_zero_or_nonzero_status_guard()
```

Observed calls (lexical order): `_source`, `_source().replace`, `_planner`, `_planner().plan`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
