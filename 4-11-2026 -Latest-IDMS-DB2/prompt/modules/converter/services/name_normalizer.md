# `converter/services/name_normalizer.py`

Source: [converter/services/name_normalizer.py](../../../../converter/services/name_normalizer.py) | 94 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `08c21cc60d0977af0d39c808e56539edf3b11098d041fa854be9f330481c1e0f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic name normalization helper.

## Module-level bindings

`__all__` (L94)

## Import declarations

```python
from patterns.naming_patterns import FOUR_DIGIT_RECORD_SUFFIX_PATTERN, MULTIPLE_UNDERSCORE_PATTERN, NON_COMPACT_NAME_CHARACTER_PATTERN, NON_DB2_NAME_CHARACTER_PATTERN
```

## Local dependency notes

- [patterns/naming_patterns.py](../../patterns/naming_patterns.md)

## Importers (92)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_capture_service.py](../analyzers/field_usage_capture_service.md)
- [converter/analyzers/field_usage_context_mapper.py](../analyzers/field_usage_context_mapper.md)
- [converter/analyzers/lr_access/handwritten_obtain_calc_planner.py](../analyzers/lr_access/handwritten_obtain_calc_planner.md)
- [converter/analyzers/lr_access/lrf_key_binding_planner.py](../analyzers/lr_access/lrf_key_binding_planner.md)
- [converter/analyzers/metadata_service.py](../analyzers/metadata_service.md)
- [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](../analyzers/program_flow/flow_cursor_loop_scanner.md)
- [converter/analyzers/program_flow/flow_models.py](../analyzers/program_flow/flow_models.md)
- [converter/analyzers/program_flow/flow_write_scanner.py](../analyzers/program_flow/flow_write_scanner.md)
- [converter/composers/cleanup/db2_date_output_cleanup.py](../composers/cleanup/db2_date_output_cleanup.md)
- [converter/composers/cleanup/dclgen_include_cleanup.py](../composers/cleanup/dclgen_include_cleanup.md)
- [converter/composers/cleanup/initialize_before_output_cleanup.py](../composers/cleanup/initialize_before_output_cleanup.md)
- [converter/composers/lrf_group_move_decomposer.py](../composers/lrf_group_move_decomposer.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)
- [tests/test_name_normalizer.py](../../tests/test_name_normalizer.md)
- 78 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `NameNormalizer` - L33-L91

```python
class NameNormalizer()
```

### `NameNormalizer.normalize` - L36-L53

```python
normalize(value: str | None) -> str
```

Canonical DB2 identifier: upper case, underscore separated.

Observed calls (lexical order): `str`, `str(value).strip`, `str(value).strip().upper`, `text.replace`, `NON_DB2_NAME_CHARACTER_PATTERN.sub`, `MULTIPLE_UNDERSCORE_PATTERN.sub`, `text.strip`.

Control points:

- L40: `if value is None`
- L45: `if not text`

### `NameNormalizer.to_cobol` - L56-L60

```python
to_cobol(value: str | None) -> str
```

Canonical COBOL identifier: upper case, hyphen separated.

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.normalize(value).replace`.

### `NameNormalizer.to_idms_name` - L63-L73

```python
to_idms_name(value: str | None) -> str
```

IDMS SET / RECORD / AREA name as it must appear in output.

Observed calls (lexical order): `NameNormalizer.to_cobol`.

### `NameNormalizer.compact` - L76-L80

```python
compact(value: str | None) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NON_COMPACT_NAME_CHARACTER_PATTERN.sub`.

### `NameNormalizer.remove_record_suffix` - L83-L91

```python
remove_record_suffix(value: str | None) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `FOUR_DIGIT_RECORD_SUFFIX_PATTERN.sub`.

Control points:

- L88: `if not text`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
