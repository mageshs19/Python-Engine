# `converter/validators/mapping_validator.py`

Source: [converter/validators/mapping_validator.py](../../../../converter/validators/mapping_validator.py) | 81 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `7afd8579ef903b34d73cf352a6bdcfc2109a5b206b65de331d4a65f84472f214`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from rules.validation_rules import MAPPING_VALIDATION_MESSAGES
```

## Local dependency notes

- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [rules/validation_rules.py](../../rules/validation_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_validators.py](../../tests/test_validators.md)

## Symbol contracts and control points

### `MappingValidator` - L7-L81

```python
class MappingValidator()
```

Validates Sheet Mapping and DCLGEN consistency.

### `MappingValidator.__init__` - L14-L22

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository, table_name_resolver: TableNameResolver) -> None
```

### `MappingValidator.validate` - L24-L42

```python
validate(self) -> list[str]
```

Observed calls (lexical order): `self.mapping_repository.count`, `messages.append`, `self.dclgen_repository.count`, `messages.extend`, `self._validate_record_table_resolution`, `self._validate_table_column_resolution`.

Control points:

- L29: `if self.mapping_repository.count() == 0`
- L34: `if self.dclgen_repository.count() == 0`

### `MappingValidator._validate_record_table_resolution` - L44-L59

```python
_validate_record_table_resolution(self) -> list[str]
```

Observed calls (lexical order): `self.mapping_repository.records`, `self.table_name_resolver.table_for_record`, `messages.append`.

Control points:

- L49: `for record in self.mapping_repository.records()`
- L52: `if table`

### `MappingValidator._validate_table_column_resolution` - L61-L81

```python
_validate_table_column_resolution(self) -> list[str]
```

Observed calls (lexical order): `self.mapping_repository.tables`, `self.table_name_resolver.resolve_table`, `self.mapping_repository.db2_columns_for_table`, `messages.append`.

Control points:

- L66: `for table in self.mapping_repository.tables()`
- L69: `if not resolved_table`
- L74: `if columns`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
