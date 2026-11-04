# `tests/test_schema_driven_4310_generic_rules.py`

Source: [tests/test_schema_driven_4310_generic_rules.py](../../../tests/test_schema_driven_4310_generic_rules.py) | 140 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `1c7bbf9391e3915ec7ea6f4c21860bacdb2be6a9122f3672677f8cfd4c098508`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Production-oriented generic COBOL conversion rules; no program names or fixed business fields.

## Import declarations

```python
from pathlib import Path
from converter.domain.models import DclgenColumn, CopybookField
from converter.repositories.copybook_repository import CopybookRepository
from converter.parsers.copybook_parser import CopybookParser
from converter.composers.schema_date_transfer_composer import SchemaDateTransferComposer
from converter.composers.schema_numeric_key_guard import SchemaNumericKeyGuard
from converter.services.final_generated_output_service import FinalGeneratedOutputService
from converter.composers.paragraph_entry_display_composer import _is_paragraph
from converter.composers.sql_body_area_b_normalizer import SqlBodyAreaBNormalizer
```

## Local dependency notes

- [converter/composers/paragraph_entry_display_composer.py](../converter/composers/paragraph_entry_display_composer.md)
- [converter/composers/schema_date_transfer_composer.py](../converter/composers/schema_date_transfer_composer.md)
- [converter/composers/schema_numeric_key_guard.py](../converter/composers/schema_numeric_key_guard.md)
- [converter/composers/sql_body_area_b_normalizer.py](../converter/composers/sql_body_area_b_normalizer.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [converter/parsers/copybook_parser.py](../converter/parsers/copybook_parser.md)
- [converter/repositories/copybook_repository.py](../converter/repositories/copybook_repository.md)
- [converter/services/final_generated_output_service.py](../converter/services/final_generated_output_service.md)

## Symbol contracts and control points

### `test_date_conversion_uses_dclgen_type_and_copybook_width_with_renamed_business_fields` - L13-L29

```python
test_date_conversion_uses_dclgen_type_and_copybook_width_with_renamed_business_fields()
```

Observed calls (lexical order): `DclgenColumn`, `CopybookField`, `CopybookRepository`, `SchemaDateTransferComposer`, `rule.compose`, `len`.

### `test_date_conversion_refuses_unproven_schema_and_ten_byte_destinations` - L32-L39

```python
test_date_conversion_refuses_unproven_schema_and_ten_byte_destinations()
```

Observed calls (lexical order): `DclgenColumn`, `CopybookField`, `CopybookRepository`, `SchemaDateTransferComposer`, `SchemaDateTransferComposer(cols, repo).compose`.

### `test_copybook_redefines_filler_does_not_expand_storage_size` - L42-L54

```python
test_copybook_redefines_filler_does_not_expand_storage_size()
```

Observed calls (lexical order): `CopybookParser`, `CopybookParser().parse`, `CopybookRepository`, `repo.group_width_for`.

### `test_numeric_refmod_guard_is_proven_by_input_and_dclgen_not_names` - L57-L71

```python
test_numeric_refmod_guard_is_proven_by_input_and_dclgen_not_names()
```

Observed calls (lexical order): `DclgenColumn`, `SchemaNumericKeyGuard`, `composer.compose`.

### `test_numeric_guard_refuses_non_numeric_dclgen_dest_and_unproven_abort_policy` - L74-L83

```python
test_numeric_guard_refuses_non_numeric_dclgen_dest_and_unproven_abort_policy()
```

Observed calls (lexical order): `DclgenColumn`, `SchemaNumericKeyGuard`, `SchemaNumericKeyGuard(cols).compose`, `src.replace`.

### `test_fixed_area_a_scope_terminator_is_not_a_paragraph` - L86-L89

```python
test_fixed_area_a_scope_terminator_is_not_a_paragraph()
```

Observed calls (lexical order): `_is_paragraph`, `'SEARCH-MUTATIES.'.ljust`.

### `test_sql_location_uses_source_proven_query_number_without_undefined_identifier` - L92-L102

```python
test_sql_location_uses_source_proven_query_number_without_undefined_identifier()
```

Observed calls (lexical order): `FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql`.

### `test_no_named_program_parity_override_remains` - L105-L108

```python
test_no_named_program_parity_override_remains()
```

Observed calls (lexical order): `(Path(__file__).resolve().parents[1] / 'converter/composers/manual_storage_parity_composer.py').read_text`, `Path`, `Path(__file__).resolve`.

### `test_symbolic_location_before_singleton_sql_becomes_queryno_without_field_name_patch` - L111-L123

```python
test_symbolic_location_before_singleton_sql_becomes_queryno_without_field_name_patch()
```

Observed calls (lexical order): `FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql`.

### `test_sql_body_area_b_alignment_is_generic_and_token_preserving` - L126-L140

```python
test_sql_body_area_b_alignment_is_generic_and_token_preserving()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `SqlBodyAreaBNormalizer`, `r.compose`, `out.splitlines`, `out.splitlines()[2][7:72].startswith`, `out.splitlines()[3][7:72].startswith`, `all`, `len`.

### `test_sql_body_area_b_alignment_is_generic_and_token_preserving.fixed` - L128-L128

```python
fixed(n, s)
```

Observed calls (lexical order): `s.ljust`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
