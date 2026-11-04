# `tests/test_imports.py`

Source: [tests/test_imports.py](../../../tests/test_imports.py) | 40 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `eb4f154fa290b66202eaf338b45c2118270eff829854f5ddc70c7873e83c6f6a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import ConversionInput
from converter.pipeline.conversion_service import ConversionService
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.cobol_parser import CobolParser
from catalogs.sheet_mapping_schema import SHEET_MAPPING_MODEL_FIELD_MAP
from patterns.idms_patterns import OBTAIN_CALC_PATTERN
from rules.authority_rules import INPUT_AUTHORITY_RULES
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.generators.sql_generator import SqlGenerator
from converter.transformers.cobol_transformer import CobolTransformer
from converter.validators.production_validator import ProductionValidator
from converter.composers.cobol_formatter import CobolFormatter
```

## Local dependency notes

- [catalogs/sheet_mapping_schema.py](../catalogs/sheet_mapping_schema.md)
- [converter/composers/cobol_formatter.py](../converter/composers/cobol_formatter.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [converter/generators/sql_generator.py](../converter/generators/sql_generator.md)
- [converter/parsers/cobol_parser.py](../converter/parsers/cobol_parser.md)
- [converter/parsers/copybook_parser.py](../converter/parsers/copybook_parser.md)
- [converter/parsers/dclgen_parser.py](../converter/parsers/dclgen_parser.md)
- [converter/parsers/sheet_mapping_parser.py](../converter/parsers/sheet_mapping_parser.md)
- [converter/pipeline/conversion_service.py](../converter/pipeline/conversion_service.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)
- [converter/validators/production_validator.py](../converter/validators/production_validator.md)
- [patterns/idms_patterns.py](../patterns/idms_patterns.md)
- [rules/authority_rules.py](../rules/authority_rules.md)

## Symbol contracts and control points

### `test_core_imports` - L1-L14

```python
test_core_imports()
```

### `test_clean_architecture_imports` - L17-L24

```python
test_clean_architecture_imports()
```

### `test_layer_imports` - L27-L40

```python
test_layer_imports()
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
