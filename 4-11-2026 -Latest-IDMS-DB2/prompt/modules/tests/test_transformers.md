# `tests/test_transformers.py`

Source: [tests/test_transformers.py](../../../tests/test_transformers.py) | 340 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `8e8b321202a218b298b80d7dc2755ccb5a9cd9800c1dc9ee16267717e039f0a3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.generators.sql_error_generator import SqlErrorGenerator
from converter.generators.sql_generator import SqlGenerator
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.transformers.cobol_transformer import CobolTransformer
from converter.transformers.field_reference_rewriter import FieldReferenceRewriter
from converter.transformers.idms_statement_transformer import IdmsStatementTransformer
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/generators/sql_error_generator.py](../converter/generators/sql_error_generator.md)
- [converter/generators/sql_generator.py](../converter/generators/sql_generator.md)
- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../converter/repositories/mapping_repository.md)
- [converter/resolvers/column_name_resolver.py](../converter/resolvers/column_name_resolver.md)
- [converter/resolvers/cursor_name_resolver.py](../converter/resolvers/cursor_name_resolver.md)
- [converter/resolvers/host_variable_resolver.py](../converter/resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../converter/resolvers/table_name_resolver.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)
- [converter/transformers/field_reference_rewriter.py](../converter/transformers/field_reference_rewriter.md)
- [converter/transformers/idms_statement_transformer.py](../converter/transformers/idms_statement_transformer.md)

## Symbol contracts and control points

### `build_transformer_context` - L17-L91

```python
build_transformer_context()
```

Observed calls (lexical order): `MappingRepository`, `SheetMappingRow`, `DclgenRepository`, `DclgenColumn`, `TableNameResolver`, `ColumnNameResolver`, `HostVariableResolver`, `CursorNameResolver`, `SqlGenerator`, `IdmsStatementTransformer`, `SqlErrorGenerator`.

### `test_idms_statement_transformer_converts_obtain_calc` - L94-L107

```python
test_idms_statement_transformer_converts_obtain_calc()
```

Observed calls (lexical order): `build_transformer_context`, `context['statement_transformer'].transform_line`, `'\n'.join`.

### `test_idms_statement_transformer_converts_store_to_insert_or_skips_safely` - L110-L130

```python
test_idms_statement_transformer_converts_store_to_insert_or_skips_safely()
```

Observed calls (lexical order): `build_transformer_context`, `context['statement_transformer'].transform_line`, `'\n'.join`.

### `test_idms_statement_transformer_removes_bind` - L133-L145

```python
test_idms_statement_transformer_removes_bind()
```

Observed calls (lexical order): `build_transformer_context`, `context['statement_transformer'].transform_line`, `'\n'.join`.

### `test_cobol_transformer_converts_program_id_and_idms_statement` - L148-L185

```python
test_cobol_transformer_converts_program_id_and_idms_statement()
```

Observed calls (lexical order): `build_transformer_context`, `CobolTransformer`, `transformer.transform`, `len`, `any`.

### `test_field_reference_rewriter_rewrites_qualified_reference` - L187-L199

```python
test_field_reference_rewriter_rewrites_qualified_reference()
```

Observed calls (lexical order): `build_transformer_context`, `FieldReferenceRewriter`, `rewriter.rewrite`.

### `test_cobol_transformer_never_converts_fixed_format_commented_store` - L203-L225

```python
test_cobol_transformer_never_converts_fixed_format_commented_store()
```

Commented subschema STORE examples must not become executable INSERTs.

Observed calls (lexical order): `build_transformer_context`, `CobolTransformer`, `'\n'.join`, `transformer.transform`.

### `test_cobol_transformer_preserves_idms_abort_cleanup_paragraph` - L228-L257

```python
test_cobol_transformer_preserves_idms_abort_cleanup_paragraph()
```

IDMS-specific status copy may go, but valid COBOL cleanup must survive.

Observed calls (lexical order): `build_transformer_context`, `CobolTransformer`, `'\n'.join`, `transformer.transform`, `converted.count`, `converted.index`.

### `test_empty_idms_abort_paragraph_is_removed_generically` - L260-L286

```python
test_empty_idms_abort_paragraph_is_removed_generically()
```

Observed calls (lexical order): `build_transformer_context`, `CobolTransformer`, `'\n'.join`, `transformer.transform`, `converted.index`.

### `test_idms_abort_paragraph_with_real_cleanup_is_preserved` - L289-L313

```python
test_idms_abort_paragraph_with_real_cleanup_is_preserved()
```

Observed calls (lexical order): `build_transformer_context`, `CobolTransformer`, `'\n'.join`, `transformer.transform`.

### `test_referenced_empty_idms_abort_paragraph_is_preserved` - L316-L340

```python
test_referenced_empty_idms_abort_paragraph_is_preserved()
```

Observed calls (lexical order): `build_transformer_context`, `CobolTransformer`, `'\n'.join`, `transformer.transform`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
