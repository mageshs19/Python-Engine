# `tests/restart/test_m11_storage_builder.py`

Source: [tests/restart/test_m11_storage_builder.py](../../../../tests/restart/test_m11_storage_builder.py) | 179 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `937a2fbb26c3fcf6fe5bb8c5a7dd855a1c8c8a78ad1f868efbcf060324530a9a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M11 - the restart working-storage builder.

## Import declarations

```python
from __future__ import annotations
import dataclasses
import pytest
from catalogs.restart_storage_catalog import DATE_GROUP, HELP_GROUP, SWITCH_GROUP
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_storage_builder import RestartStorageBuilder
```

## Local dependency notes

- [catalogs/restart_storage_catalog.py](../../catalogs/restart_storage_catalog.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_storage_builder.py](../../converter/generators/restart/restart_storage_builder.md)

## Symbol contracts and control points

### `builder` - L35-L36

```python
builder(config)
```

Observed calls (lexical order): `RestartStorageBuilder`.

### `lines` - L40-L41

```python
lines(builder)
```

Observed calls (lexical order): `builder.build`, `line.strip`.

### `test_all_three_groups_are_declared` - L47-L49

```python
test_all_three_groups_are_declared(lines)
```

Observed calls (lexical order): `any`, `line.startswith`.

Control points:

- L48: `for group in (SWITCH_GROUP, HELP_GROUP, DATE_GROUP)`

### `test_the_switch_is_named_after_the_record` - L52-L53

```python
test_the_switch_is_named_after_the_record(config, builder)
```

Observed calls (lexical order): `builder.eof_switch`.

### `test_the_conditions_are_named_after_the_record` - L56-L59

```python
test_the_conditions_are_named_after_the_record(config, builder)
```

Observed calls (lexical order): `builder.eof_condition`, `builder.not_eof_condition`.

### `test_both_88_levels_are_declared` - L62-L70

```python
test_both_88_levels_are_declared(builder, lines)
```

Observed calls (lexical order): `any`, `builder.eof_condition`, `line.startswith`, `builder.not_eof_condition`.

### `test_the_eof_condition_carries_the_true_value` - L73-L75

```python
test_the_eof_condition_carries_the_true_value(builder, lines)
```

Observed calls (lexical order): `builder.eof_condition`, `next`.

### `test_the_not_eof_condition_carries_the_false_value` - L78-L82

```python
test_the_not_eof_condition_carries_the_false_value(builder, lines)
```

Observed calls (lexical order): `next`, `builder.not_eof_condition`.

### `test_every_resolved_name_appears` - L85-L96

```python
test_every_resolved_name_appears(config, lines)
```

Observed calls (lexical order): `'\n'.join`.

Control points:

- L88: `for name in (names.restart_record, names.read_count_field, names.restart_key_field, names.input_save_area, names.commit_counter, names.input_counter)`

### `test_no_placeholder_survives` - L99-L102

```python
test_no_placeholder_survives(lines)
```

Observed calls (lexical order): `'\n'.join`.

### `test_the_key_picture_uses_the_measured_size` - L108-L109

```python
test_the_key_picture_uses_the_measured_size(config, lines)
```

Observed calls (lexical order): `any`.

### `test_the_count_picture_uses_the_measured_size` - L112-L113

```python
test_the_count_picture_uses_the_measured_size(config, lines)
```

Observed calls (lexical order): `any`.

### `test_a_shorter_key_produces_a_shorter_field` - L116-L122

```python
test_a_shorter_key_produces_a_shorter_field(role, complete_names)
```

1200 was never a constant; it is this program's measurement.

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `RestartStorageBuilder(RestartConfig.build(role, names)).build`, `'\n'.join`.

### `test_the_save_area_matches_the_key_length` - L125-L129

```python
test_the_save_area_matches_the_key_length(config, lines)
```

The save area is copied into the key; a shorter one truncates.

Observed calls (lexical order): `any`.

### `test_one_missing_name_emits_nothing` - L147-L151

```python
test_one_missing_name_emits_nothing(role, complete_names, field)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `builder.build`, `any`.

### `test_an_unmeasured_size_emits_nothing` - L155-L159

```python
test_an_unmeasured_size_emits_nothing(role, complete_names, field)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `builder.build`, `any`.

### `test_a_refusal_is_never_partial` - L162-L165

```python
test_a_refusal_is_never_partial(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `RestartStorageBuilder(RestartConfig.build(role, names)).build`.

### `test_building_twice_produces_identical_lines` - L171-L174

```python
test_building_twice_produces_identical_lines(config)
```

Observed calls (lexical order): `RestartStorageBuilder`, `RestartStorageBuilder(config).build`.

### `test_the_build_is_reported` - L177-L179

```python
test_the_build_is_reported(builder)
```

Observed calls (lexical order): `builder.build`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
