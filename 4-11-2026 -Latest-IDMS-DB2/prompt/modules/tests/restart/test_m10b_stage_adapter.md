# `tests/restart/test_m10b_stage_adapter.py`

Source: [tests/restart/test_m10b_stage_adapter.py](../../../../tests/restart/test_m10b_stage_adapter.py) | 188 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `0782a047eed552fc7f1675111a26b98fbda11073f7517fa63f8905120a137e57`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M10b - RestartStageAdapter.

## Module-level bindings

`RECORD` (L30), `RETENTION` (L31), `TOTALS` (L32), `WORKING_STORAGE` (L33), `INCLUDE_TEMPLATE` (L34)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import types
import pytest
from catalogs.restart_paragraph_catalog import RestartDclgenRole
from converter.composers.restart.restart_stage_adapter import RestartRunContext, RestartStageAdapter
from converter.resolvers.restart_role_resolver import SITE_AUTHORITY_FIELD
```

## Local dependency notes

- [catalogs/restart_paragraph_catalog.py](../../catalogs/restart_paragraph_catalog.md)
- [converter/composers/restart/restart_stage_adapter.py](../../converter/composers/restart/restart_stage_adapter.md)
- [converter/resolvers/restart_role_resolver.py](../../converter/resolvers/restart_role_resolver.md)

## Symbol contracts and control points

### `_Mapping` - L37-L45

```python
class _Mapping()
```

### `_Mapping.__init__` - L38-L39

```python
__init__(self, table: str) -> None
```

### `_Mapping.db2_table_for_record` - L41-L42

```python
db2_table_for_record(self, record_name: str) -> str
```

### `_Mapping.has_table` - L44-L45

```python
has_table(self, table_name: str) -> bool
```

Observed calls (lexical order): `self.table.upper`, `table_name.upper`.

### `dclgen` - L49-L57

```python
dclgen(role)
```

A DCLGEN role carrying the same spellings as the M2 fixture.

Observed calls (lexical order): `dataclasses.fields`, `getattr`, `values.pop`, `types.SimpleNamespace`.

Control points:

- L52: `for item in dataclasses.fields(RestartDclgenRole)`
- L53: `if item.name == SITE_AUTHORITY_FIELD`

### `source_text` - L61-L69

```python
source_text(source_lines, role)
```

Observed calls (lexical order): `str`, `str(role.table_name).upper`, `list`, `any`, `str(line).upper`, `enumerate`, `INCLUDE_TEMPLATE.format`, `out.insert`, `'\n'.join`.

Control points:

- L64: `if not any((table in str(line).upper() for line in out))`
- L65: `for (index, line) in enumerate(out)`
- L66: `if WORKING_STORAGE in str(line).upper()`

### `context` - L73-L79

```python
context(dclgen)
```

Observed calls (lexical order): `RestartRunContext`.

### `adapter` - L83-L88

```python
adapter(line_utils, context, role)
```

Observed calls (lexical order): `RestartStageAdapter`, `_Mapping`.

### `test_the_adapter_has_the_pipeline_shape` - L94-L96

```python
test_the_adapter_has_the_pipeline_shape(adapter)
```

Observed calls (lexical order): `callable`, `isinstance`.

### `test_compose_returns_text_not_a_tuple` - L99-L100

```python
test_compose_returns_text_not_a_tuple(adapter, source_text)
```

Observed calls (lexical order): `adapter.compose`, `isinstance`.

### `test_the_restart_family_is_injected` - L103-L106

```python
test_the_restart_family_is_injected(adapter, source_text, role)
```

Observed calls (lexical order): `adapter.compose`.

### `test_the_supplied_totals_are_carried_through` - L109-L110

```python
test_the_supplied_totals_are_carried_through(adapter, source_text)
```

Observed calls (lexical order): `TOTALS[0].strip`, `adapter.compose`.

### `test_the_role_resolution_is_reported` - L113-L115

```python
test_the_role_resolution_is_reported(adapter, source_text)
```

Observed calls (lexical order): `adapter.compose`, `any`.

### `test_the_injection_is_reported` - L118-L120

```python
test_the_injection_is_reported(adapter, source_text)
```

Observed calls (lexical order): `adapter.compose`, `any`.

### `test_no_context_is_a_reported_wiring_gap` - L126-L129

```python
test_no_context_is_a_reported_wiring_gap(line_utils, source_text)
```

Observed calls (lexical order): `RestartStageAdapter`, `adapter.compose`, `any`.

### `test_a_retrieval_program_is_untouched` - L132-L138

```python
test_a_retrieval_program_is_untouched(line_utils, context, source_text, role)
```

Observed calls (lexical order): `RestartStageAdapter`, `dataclasses.replace`, `_Mapping`, `adapter.compose`.

### `test_a_retrieval_program_is_never_asked_for_a_role` - L141-L150

```python
test_a_retrieval_program_is_never_asked_for_a_role(line_utils, context, source_text)
```

Three refusals for a correct program is noise, not a diagnostic.

Observed calls (lexical order): `RestartStageAdapter`, `dataclasses.replace`, `adapter.compose`, `any`.

### `test_a_missing_retention_leaves_the_program_unchanged` - L153-L162

```python
test_a_missing_retention_leaves_the_program_unchanged(line_utils, context, source_text, role)
```

Observed calls (lexical order): `RestartStageAdapter`, `dataclasses.replace`, `_Mapping`, `adapter.compose`, `any`.

### `test_an_unmapped_record_leaves_the_program_unchanged` - L165-L173

```python
test_an_unmapped_record_leaves_the_program_unchanged(line_utils, context, source_text, role)
```

Observed calls (lexical order): `RestartStageAdapter`, `dataclasses.replace`, `_Mapping`, `adapter.compose`.

### `test_running_twice_produces_identical_output` - L179-L181

```python
test_running_twice_produces_identical_output(adapter, source_text)
```

Observed calls (lexical order): `adapter.compose`.

### `test_messages_do_not_accumulate_across_runs` - L184-L188

```python
test_messages_do_not_accumulate_across_runs(adapter, source_text)
```

Observed calls (lexical order): `adapter.compose`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
