# `converter/composers/record_materialisation/record_plan_builder.py`

Source: [converter/composers/record_materialisation/record_plan_builder.py](../../../../../converter/composers/record_materialisation/record_plan_builder.py) | 117 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `386554c8ffc20f53d3cdc6b1eb818ebafd71aff3931782fe41eea645e840bdde`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Assembles a RecordMaterialisationPlan from Sheet Mapping rows.

## Module-level bindings

`__all__` (L117)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_host_resolver import RecordHostResolver
from converter.composers.record_materialisation.record_plan import RecordMaterialisationPlan
from converter.composers.record_materialisation.record_row_reader import RecordRowReader
from rules.record_materialisation_rules import NON_RECORD_NAME_SUFFIXES
```

## Local dependency notes

- [converter/composers/record_materialisation/record_host_resolver.py](record_host_resolver.md)
- [converter/composers/record_materialisation/record_plan.py](record_plan.md)
- [converter/composers/record_materialisation/record_row_reader.py](record_row_reader.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_field_plan.py](record_field_plan.md)
- [converter/composers/record_materialisation_composer.py](../record_materialisation_composer.md)
- [tests/test_record_mapping_failure_contract.py](../../../tests/test_record_mapping_failure_contract.md)

## Symbol contracts and control points

### `RecordMappingLookupError` - L33-L34

```python
class RecordMappingLookupError(RuntimeError)
```

Authoritative mapping read failed; conversion must fail closed.

### `RecordPlanBuilder` - L37-L114

```python
class RecordPlanBuilder()
```

Turns Sheet Mapping rows into a RecordMaterialisationPlan.

### `RecordPlanBuilder.__init__` - L40-L53

```python
__init__(self, *, mapping_repository, table_name_resolver, host_variable_resolver, row_reader: RecordRowReader | None=None) -> None
```

Observed calls (lexical order): `RecordRowReader`, `RecordHostResolver`.

### `RecordPlanBuilder.build` - L56-L88

```python
build(self, record_name: str) -> RecordMaterialisationPlan
```

Observed calls (lexical order): `self.cobol_name`, `RecordMaterialisationPlan`, `self._rows`, `self.hosts.table_for`, `self.hosts.group_for`, `self.rows_reader.read`, `self.hosts.host_for`, `plan.fields.append`, `plan.missing_hosts.append`.

Control points:

- L61: `if not rows`
- L67: `for row in rows`
- L70: `if item is None`
- L77: `if item.requires_host`
- L85: `if item.is_missing_host`

### `RecordPlanBuilder.looks_like_record` - L91-L98

```python
looks_like_record(name: str) -> bool
```

Guard so a LINKAGE work field such as DATE8-LS is not treated as a mapped IDMS record. Suffix driven, so no name is hardcoded.

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `candidate.endswith`.

Control points:

- L96: `if not candidate`

### `RecordPlanBuilder._rows` - L101-L110

```python
_rows(self, record: str) -> list
```

Observed calls (lexical order): `list`, `self.mapping_repository.rows_for_record`, `RecordMappingLookupError`.

Explicit raises: `RecordMappingLookupError(f'Cannot read authoritative mapping rows for record {record}: {exc}')`.

### `RecordPlanBuilder.cobol_name` - L113-L114

```python
cobol_name(value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `str(value or '').strip().upper().replace`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
