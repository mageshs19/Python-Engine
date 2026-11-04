# `converter/composers/record_materialisation/record_host_resolver.py`

Source: [converter/composers/record_materialisation/record_host_resolver.py](../../../../../converter/composers/record_materialisation/record_host_resolver.py) | 90 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `9dc4f4fdb5e7c0e8de2b189beac9f3f9099f9ea5bebd1a63d55c80e1f25582a4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Adapter over the table and host-variable resolvers.

## Module-level bindings

`HOST_PREFIX` (L13), `GROUP_SEPARATOR` (L14), `HOST_OF_GROUP_TEMPLATE` (L15), `__all__` (L90)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_field_plan.py](record_field_plan.md)
- [converter/composers/record_materialisation/record_plan_builder.py](record_plan_builder.md)

## Symbol contracts and control points

### `RecordHostResolver` - L18-L87

```python
class RecordHostResolver()
```

Resolves record -> table -> DCLGEN group -> host reference.

### `RecordHostResolver.__init__` - L21-L28

```python
__init__(self, *, table_name_resolver, host_variable_resolver) -> None
```

### `RecordHostResolver.table_for` - L31-L39

```python
table_for(self, record: str) -> str
```

Observed calls (lexical order): `str`, `self.table_name_resolver.table_for_record`.

Control points:

- L32: `if not record`

### `RecordHostResolver.group_for` - L42-L50

```python
group_for(self, table: str) -> str
```

Observed calls (lexical order): `str`, `self.host_variable_resolver.group_for_table`.

Control points:

- L43: `if not table`

### `RecordHostResolver.host_for` - L53-L71

```python
host_for(self, table: str, column: str) -> str
```

'DA-CRFMAS-479BFAS OF DCLDZBFASTV', or '' when unresolved.

Observed calls (lexical order): `self.host_variable_resolver.host_reference_for_column`, `self.normalize`.

Control points:

- L60: `if not table or not column`

### `RecordHostResolver.normalize` - L75-L87

```python
normalize(reference) -> str
```

Observed calls (lexical order): `str`, `str(reference or '').strip`, `str(reference or '').strip().lstrip`, `text.partition`, `HOST_OF_GROUP_TEMPLATE.format`, `host.strip`, `host.strip().upper`, `group.strip`, `group.strip().upper`, `text.upper`.

Control points:

- L77: `if not text`
- L80: `if GROUP_SEPARATOR in text`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
