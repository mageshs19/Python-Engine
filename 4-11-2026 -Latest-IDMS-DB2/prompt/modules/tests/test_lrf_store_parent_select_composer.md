# `tests/test_lrf_store_parent_select_composer.py`

Source: [tests/test_lrf_store_parent_select_composer.py](../../../tests/test_lrf_store_parent_select_composer.py) | 92 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `fcb9da161293426fa99ef7b569e9d94c66ce81a8d632fdb531fb1dcd520bd4ea`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.lrf_store_parent_select_composer import LrfStoreParentSelectComposer
```

## Local dependency notes

- [converter/composers/lrf_store_parent_select_composer.py](../converter/composers/lrf_store_parent_select_composer.md)

## Symbol contracts and control points

### `Mapping` - L4-L7

```python
class Mapping()
```

### `Mapping.db2_table_for_record` - L5-L7

```python
db2_table_for_record(self, record)
```

### `Dclgen` - L10-L15

```python
class Dclgen()
```

### `Dclgen.column_names_for_table` - L11-L15

```python
column_names_for_table(self, table)
```

### `TableResolver` - L18-L20

```python
class TableResolver()
```

### `TableResolver.resolve_table` - L19-L20

```python
resolve_table(self, table)
```

Observed calls (lexical order): `{'DZBEFFTB': 'DZBEFFTV', 'DZBEFFTV': 'DZBEFFTV', 'DZEVEFTV': 'DZEVEFTV'}.get`.

### `Hosts` - L23-L33

```python
class Hosts()
```

### `Hosts.host_reference_for_column` - L24-L33

```python
host_reference_for_column(self, table, column)
```

### `SqlGenerator` - L36-L56

```python
class SqlGenerator()
```

Declared class/data-model fields:

```python
mapping_repository = Mapping()
dclgen_repository = Dclgen()
table_name_resolver = TableResolver()
host_variable_resolver = Hosts()
```

### `SqlGenerator.select_by_key` - L42-L56

```python
select_by_key(self, record, *, for_lrf_parent=False)
```

### `test_lrf_store_generates_parent_select_and_gates_child_insert` - L59-L92

```python
test_lrf_store_generates_parent_select_and_gates_child_insert()
```

Observed calls (lexical order): `'\n'.join`, `LrfStoreParentSelectComposer`, `SqlGenerator`, `composer.compose`, `result.index`, `result.split`, `result.split('IF SQLCODE = 0', 1)[1].split`, `any`, `gated.splitlines`, `line.strip`, `line.rstrip`, `line.rstrip().endswith`, `line.strip().upper`, `line.strip().upper().startswith`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
