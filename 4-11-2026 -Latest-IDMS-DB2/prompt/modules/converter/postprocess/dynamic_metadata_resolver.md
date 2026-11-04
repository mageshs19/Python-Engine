# `converter/postprocess/dynamic_metadata_resolver.py`

Source: [converter/postprocess/dynamic_metadata_resolver.py](../../../../converter/postprocess/dynamic_metadata_resolver.py) | 260 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `59e6a1e78dbbc89a6698172de4b9b3c33ce1dcc0fb5d8e02ba1f0089721f538c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L254)

## Import declarations

```python
from __future__ import annotations
from dataclasses import fields, is_dataclass
from typing import Any
from converter.postprocess.update_cobol_file_resolver import UpdateCobolFileResolver
from converter.postprocess.update_copybook_resolver import UpdateCopybookResolver
from converter.postprocess.update_metadata_models import CobolFileInfo, CopybookRecordInfo, DclgenRoleInfo, UpdateProgramContext
from converter.postprocess.update_restart_dclgen_resolver import UpdateRestartDclgenResolver
from converter.services.name_derivation_resolver import NameDerivationResolver
```

## Local dependency notes

- [converter/postprocess/update_cobol_file_resolver.py](update_cobol_file_resolver.md)
- [converter/postprocess/update_copybook_resolver.py](update_copybook_resolver.md)
- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)
- [converter/postprocess/update_restart_dclgen_resolver.py](update_restart_dclgen_resolver.md)
- [converter/services/name_derivation_resolver.py](../services/name_derivation_resolver.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/cobol_update_standard_generator.py](cobol_update_standard_generator.md)
- [converter/postprocess/storage_include/storage_ws_injector.py](storage_include/storage_ws_injector.md)
- [converter/postprocess/update_business_sql_standardizer.py](update_business_sql_standardizer.md)
- [converter/postprocess/update_main_flow_rewriter.py](update_main_flow_rewriter.md)
- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)
- [converter/postprocess/update_restart_paragraph_manager.py](update_restart_paragraph_manager.md)

## Symbol contracts and control points

### `DynamicMetadataResolver` - L25-L251

```python
class DynamicMetadataResolver()
```

Resolves update-program metadata from parsed COBOL, Copybook, and DCLGEN data.

### `DynamicMetadataResolver.__init__` - L37-L41

```python
__init__(self) -> None
```

Observed calls (lexical order): `UpdateCobolFileResolver`, `UpdateCopybookResolver`, `UpdateRestartDclgenResolver`, `NameDerivationResolver`.

### `DynamicMetadataResolver.resolve` - L43-L207

```python
resolve(self, *, source_cobol: str, generated_cobol: str, copybook_fields: list[Any], dclgen_columns: list[Any], target_program_id: str='', mapping_repository: Any | None=None) -> UpdateProgramContext
```

Observed calls (lexical order): `self.cobol_resolver.resolve_program_id`, `diagnostics.append`, `self.cobol_resolver.parse_cobol_files`, `ValueError`, `self.cobol_resolver.choose_input_file`, `self.copybook_resolver.build_copybook_records`, `len`, `self.cobol_resolver.extract_source_field_references`, `self.cobol_resolver.extract_copy_statements`, `self.copybook_resolver.choose_copybook`, `self.name_derivation_resolver.derive`, `CopybookRecordInfo`, `self.cobol_resolver.resolve_legacy_eof_switch`, `self.restart_dclgen_resolver.resolve_restart_dclgen`, `self._safe_attr`, `self._make_context`.

Control points:

- L67: `if not input_files`
- L104: `if derived_record != input_copybook.record_name or derived_include != input_copybook.include_name`
- L130: `if legacy_eof_switch`
- L140: `if restart_dclgen`
- L191: `if mapping_repository is not None and dclgen_columns`

Explicit raises: `ValueError('Unable to resolve input file from COBOL SELECT/FD/READ.')`.

### `DynamicMetadataResolver._make_context` - L209-L244

```python
_make_context(self, **values: Any) -> UpdateProgramContext
```

Creates UpdateProgramContext while staying compatible with the actual dataclass in update_metadata_models.py.

Observed calls (lexical order): `is_dataclass`, `fields`, `values.items`, `UpdateProgramContext`, `hasattr`, `setattr`.

Control points:

- L226: `if is_dataclass(UpdateProgramContext)`
- L237: `for (key, value) in values.items()`
- L238: `if not hasattr(context, key)`

### `DynamicMetadataResolver._safe_attr` - L246-L251

```python
_safe_attr(self, obj: Any, name: str) -> str
```

Observed calls (lexical order): `getattr`, `str`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
