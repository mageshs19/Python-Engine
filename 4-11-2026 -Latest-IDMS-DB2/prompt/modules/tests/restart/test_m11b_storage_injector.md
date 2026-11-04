# `tests/restart/test_m11b_storage_injector.py`

Source: [tests/restart/test_m11b_storage_injector.py](../../../../tests/restart/test_m11b_storage_injector.py) | 279 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `71eebcf21b98aa22ed3c17f3d595e3e98f3dc8774c7a70fb5d1adca76a134c69`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M11b - placing the restart working storage and its DCLGEN include.

## Module-level bindings

`BARE` (L59), `HEADER_ONLY` (L72), `HEADER_PLUS_MEMBER` (L73)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import pytest
from catalogs.restart_storage_catalog import DATE_GROUP, HELP_GROUP, SWITCH_GROUP
from converter.composers.restart.restart_storage_injector import INCLUDE_NAME_ATTRIBUTES, WORKING_STORAGE_TOKEN, RestartStorageInjector
from converter.generators.restart.restart_config import RestartConfig
```

## Local dependency notes

- [catalogs/restart_storage_catalog.py](../../catalogs/restart_storage_catalog.md)
- [converter/composers/restart/restart_storage_injector.py](../../converter/composers/restart/restart_storage_injector.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)

## Symbol contracts and control points

### `injector` - L80-L81

```python
injector(config, line_utils)
```

Observed calls (lexical order): `RestartStorageInjector`.

### `_logical` - L84-L90

```python
_logical(line_utils, lines)
```

Observed calls (lexical order): `line_utils.logical`, `str`, `str(line_utils.logical(raw) or '').strip`, `str(line_utils.logical(raw) or '').strip().upper`, `' '.join`, `body.split`, `out.append`.

Control points:

- L86: `for raw in lines`
- L88: `if body`

### `_include_member` - L93-L100

```python
_include_member(config) -> str
```

The DCLGEN member, resolved the way production resolves it.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(role, attribute, '') or '').strip`, `str(getattr(role, attribute, '') or '').strip().upper`.

Control points:

- L96: `for attribute in INCLUDE_NAME_ATTRIBUTES`
- L98: `if value`

### `_count_headers` - L103-L104

```python
_count_headers(body, group) -> int
```

Observed calls (lexical order): `len`, `line.startswith`.

### `test_every_group_is_declared` - L110-L113

```python
test_every_group_is_declared(injector, line_utils)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `any`, `line.startswith`.

Control points:

- L112: `for group in (SWITCH_GROUP, HELP_GROUP, DATE_GROUP)`

### `test_the_storage_lands_in_working_storage` - L116-L124

```python
test_the_storage_lands_in_working_storage(injector, line_utils)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `next`, `enumerate`, `l.startswith`.

### `test_the_groups_keep_declaration_order` - L127-L134

```python
test_the_groups_keep_declaration_order(injector, line_utils)
```

All four blocks share one anchor; ties must not reverse them.

Observed calls (lexical order): `_logical`, `injector.inject`, `enumerate`, `l.startswith`, `next`, `sorted`.

### `test_nothing_lands_in_the_file_section` - L137-L149

```python
test_nothing_lands_in_the_file_section(injector, line_utils)
```

VALUE under an FD is illegal, and hides the FD's real record.

Observed calls (lexical order): `_logical`, `injector.inject`, `next`, `enumerate`, `l.startswith`.

Control points:

- L146: `for (index, line) in enumerate(body)`
- L147: `if file_section < index < working`

### `test_the_decision_is_reported` - L152-L154

```python
test_the_decision_is_reported(injector)
```

Observed calls (lexical order): `injector.inject`, `any`.

### `test_the_restart_include_is_emitted` - L160-L168

```python
test_the_restart_include_is_emitted(injector, line_utils, config)
```

The generated SQL moves through the host group; something has to declare it.

Observed calls (lexical order): `_include_member`, `_logical`, `injector.inject`, `l.startswith`, `len`.

### `test_the_include_lands_in_working_storage` - L171-L182

```python
test_the_include_lands_in_working_storage(injector, line_utils, config)
```

Observed calls (lexical order): `_include_member`, `_logical`, `injector.inject`, `next`, `enumerate`, `l.startswith`.

### `test_the_include_is_not_added_twice` - L185-L192

```python
test_the_include_is_not_added_twice(injector, line_utils, config)
```

Observed calls (lexical order): `_include_member`, `injector.inject`, `_logical`, `l.startswith`, `len`, `any`.

### `test_an_include_already_present_is_left_alone` - L195-L204

```python
test_an_include_already_present_is_left_alone(injector, line_utils, config)
```

Observed calls (lexical order): `_include_member`, `_logical`, `injector.inject`, `l.startswith`, `len`.

### `test_an_existing_group_header_is_never_duplicated` - L210-L213

```python
test_an_existing_group_header_is_never_duplicated(injector, line_utils)
```

Holds whether the group is complete or not.

Observed calls (lexical order): `_logical`, `injector.inject`, `_count_headers`.

### `test_an_incomplete_group_is_completed` - L216-L228

```python
test_an_incomplete_group_is_completed(injector, line_utils)
```

Was: 'an existing group is left alone'.

Observed calls (lexical order): `_logical`, `injector.inject`, `len`, `_count_headers`, `any`.

### `test_an_incomplete_group_keeps_its_own_members` - L231-L234

```python
test_an_incomplete_group_keeps_its_own_members(injector, line_utils)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `any`, `_count_headers`.

### `test_a_complete_group_is_left_alone` - L237-L244

```python
test_a_complete_group_is_left_alone(injector, line_utils)
```

A group this composer itself declared is complete by definition.

Observed calls (lexical order): `injector.inject`, `any`.

### `test_the_other_groups_are_still_added` - L247-L249

```python
test_the_other_groups_are_still_added(injector, line_utils)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `any`, `l.startswith`.

### `test_no_working_storage_means_no_insertion` - L255-L258

```python
test_no_working_storage_means_no_insertion(injector, line_utils)
```

Observed calls (lexical order): `l.upper`, `injector.inject`, `any`.

### `test_an_unusable_config_places_nothing` - L261-L267

```python
test_an_unusable_config_places_nothing(role, complete_names, line_utils)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartStorageInjector`, `RestartConfig.build`, `injector.inject`, `any`.

### `test_running_twice_inserts_nothing_the_second_time` - L273-L279

```python
test_running_twice_inserts_nothing_the_second_time(injector)
```

Observed calls (lexical order): `injector.inject`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
