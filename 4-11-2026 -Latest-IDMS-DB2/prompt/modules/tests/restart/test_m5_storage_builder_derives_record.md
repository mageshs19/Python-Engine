# `tests/restart/test_m5_storage_builder_derives_record.py`

Source: [tests/restart/test_m5_storage_builder_derives_record.py](../../../../tests/restart/test_m5_storage_builder_derives_record.py) | 142 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ae5f07cc68686df2eab102ca8a89e71bd52fdf617c3414f9b02537a939d78fd7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M5 regression contract: the switch and its 88-levels are always built from the DERIVED record name.

## Import declarations

```python
from __future__ import annotations
import dataclasses
import pytest
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_storage_builder import RestartStorageBuilder
from converter.generators.restart.restart_config import RestartProgramNames
```

## Local dependency notes

- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_storage_builder.py](../../converter/generators/restart/restart_storage_builder.md)

## Symbol contracts and control points

### `test_switch_and_conditions_use_the_derived_record_name` - L57-L63

```python
test_switch_and_conditions_use_the_derived_record_name(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `builder.eof_switch`, `builder.eof_condition`, `builder.not_eof_condition`.

### `test_an_already_derived_record_name_is_unchanged` - L66-L71

```python
test_an_already_derived_record_name_is_unchanged(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `builder.eof_switch`, `builder.eof_condition`.

### `test_a_non_derivable_record_name_passes_through` - L74-L83

```python
test_a_non_derivable_record_name_passes_through(role, complete_names)
```

A record whose marker is not BD/BZ (e.g. a non-IDMS-origin file name) is not this builder's concern to invent a derivation for. NameDerivationResolver returns it unchanged, so the switch is named after it literally, same as before this fix.

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `builder.eof_switch`, `builder.eof_condition`.

### `test_two_builders_never_disagree_on_the_switch_name` - L90-L99

```python
test_two_builders_never_disagree_on_the_switch_name(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `first.eof_switch`, `second.eof_switch`, `first.eof_condition`, `second.eof_condition`, `first.not_eof_condition`, `second.not_eof_condition`.

### `test_the_switch_and_its_88_levels_are_internally_consistent` - L102-L114

```python
test_the_switch_and_its_88_levels_are_internally_consistent(role, complete_names)
```

Whatever the switch is named, PERFORM...UNTIL and SET are both built from eof_condition()/not_eof_condition() downstream, so the one invariant that actually prevents the runtime hang is: the record fragment inside the switch name equals the record fragment inside the condition names.

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `builder.eof_switch`, `builder.eof_switch().removeprefix`, `builder.eof_condition`, `builder.eof_condition().removesuffix`.

### `test_build_renders_only_the_derived_spelling` - L121-L131

```python
test_build_renders_only_the_derived_spelling(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartStorageBuilder`, `builder.build`, `'\n'.join`.

### `test_an_unusable_config_still_renders_nothing` - L137-L142

```python
test_an_unusable_config_still_renders_nothing(role)
```

Observed calls (lexical order): `RestartConfig.build`, `RestartProgramNames`, `RestartStorageBuilder`, `builder.build`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
