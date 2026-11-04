# `tests/test_lrf_key_binding_planner.py`

Source: [tests/test_lrf_key_binding_planner.py](../../../tests/test_lrf_key_binding_planner.py) | 88 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ca79b99bc18dcb63f0b7a5ac617b90f9525dc7584fa8f47d859224260e44bac8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.lr_access.lrf_key_binding_planner import LrfKeyBindingPlanner
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.domain.models import CopybookField
from converter.repositories.copybook_repository import CopybookRepository
```

## Local dependency notes

- [converter/analyzers/lr_access/lrf_key_binding_planner.py](../converter/analyzers/lr_access/lrf_key_binding_planner.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/copybook_repository.py](../converter/repositories/copybook_repository.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../converter/resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)

## Symbol contracts and control points

### `_planner` - L9-L36

```python
_planner()
```

Observed calls (lexical order): `SheetMappingRow`, `{'DZBEFFTV': ['CT_RKTPROD_479BEFF', 'NR_IDSTOCK_479BEFF', 'NR_CDSTK_479BEFF', 'NS_DBSTK_479BEFF'], 'DZEVEFT...`, `DclgenColumn`, `columns.extend`, `field.replace`, `MappingRepository`, `DclgenRepository`, `TableNameResolver`, `HostVariableResolver`, `LrfKeyBindingPlanner`.

Control points:

- L27: `for (table, fields) in {'DZBEFFTV': ['CT_RKTPROD_479BEFF', 'NR_IDSTOCK_479BEFF', 'NR_CDSTK_479BEFF', 'NS_DBSTK_479BEFF'], 'DZEVEFTV': ['CT_RKTPROD_479BEFF', 'NR_IDSTOCK_479BEFF', 'N...`

### `test_composite_calc_group_splits_only_when_widths_are_proven` - L39-L50

```python
test_composite_calc_group_splits_only_when_widths_are_proven()
```

Observed calls (lexical order): `_planner`, `planner.plan_parent_input`, `any`, `item.startswith`.

### `test_ambiguous_or_missing_composite_source_fails_closed` - L53-L58

```python
test_ambiguous_or_missing_composite_source_fails_closed()
```

Observed calls (lexical order): `_planner`, `planner.plan_parent_input`, `any`.

### `test_composite_calc_key_uses_copybook_width_when_input_field_is_not_inline` - L63-L88

```python
test_composite_calc_key_uses_copybook_width_when_input_field_is_not_inline()
```

Observed calls (lexical order): `_planner`, `LrfKeyBindingPlanner`, `CopybookRepository`, `CopybookField`, `planner.plan_parent_input`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
