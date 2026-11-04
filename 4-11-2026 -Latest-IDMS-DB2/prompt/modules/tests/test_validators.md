# `tests/test_validators.py`

Source: [tests/test_validators.py](../../../tests/test_validators.py) | 162 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b11f606cfcf62355aaac500d0f354b0a28dcf45333d52b6e6f2336d31540b1d8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import ConversionInput, DclgenColumn, SheetMappingRow
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.validators.input_validator import InputValidator
from converter.validators.mapping_validator import MappingValidator
from converter.validators.production_validator import ProductionValidator
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)
- [converter/validators/input_validator.py](../converter/validators/input_validator.md)
- [converter/validators/mapping_validator.py](../converter/validators/mapping_validator.md)
- [converter/validators/production_validator.py](../converter/validators/production_validator.md)

## Symbol contracts and control points

### `test_input_validator_detects_missing_inputs` - L10-L17

```python
test_input_validator_detects_missing_inputs()
```

Observed calls (lexical order): `InputValidator`, `ConversionInput`, `validator.validate`.

### `test_input_validator_passes_with_required_inputs` - L20-L31

```python
test_input_validator_passes_with_required_inputs()
```

Observed calls (lexical order): `InputValidator`, `validator.validate`, `ConversionInput`, `SheetMappingRow`, `DclgenColumn`.

### `test_mapping_validator_detects_missing_metadata` - L34-L51

```python
test_mapping_validator_detects_missing_metadata()
```

Observed calls (lexical order): `MappingRepository`, `DclgenRepository`, `TableNameResolver`, `MappingValidator`, `validator.validate`.

### `test_mapping_validator_passes_basic_mapping` - L54-L87

```python
test_mapping_validator_passes_basic_mapping()
```

Observed calls (lexical order): `MappingRepository`, `SheetMappingRow`, `DclgenRepository`, `DclgenColumn`, `TableNameResolver`, `MappingValidator`, `validator.validate`.

### `test_production_validator_detects_missing_db2_tokens` - L90-L98

```python
test_production_validator_detects_missing_db2_tokens()
```

Observed calls (lexical order): `DclgenRepository`, `ProductionValidator`, `validator.validate`.

### `test_production_validator_detects_residual_idms_statement` - L101-L115

```python
test_production_validator_detects_residual_idms_statement()
```

Observed calls (lexical order): `DclgenRepository`, `ProductionValidator`, `validator.validate`, `any`.

### `test_production_validator_accepts_valid_host_reference` - L118-L143

```python
test_production_validator_accepts_valid_host_reference()
```

Observed calls (lexical order): `DclgenRepository`, `DclgenColumn`, `ProductionValidator`, `validator.validate`, `any`.

### `test_host_reference_validation_ignores_fixed_format_right_sequence_area` - L145-L162

```python
test_host_reference_validation_ignores_fixed_format_right_sequence_area()
```

Observed calls (lexical order): `DclgenRepository`, `DclgenColumn`, `ProductionValidator`, `len`, `validator._generated_dclgen_host_references`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
