# `tests/spec_builder/conftest.py`

Source: [tests/spec_builder/conftest.py](../../../../tests/spec_builder/conftest.py) | 116 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ff8050a1a1d5103ffa20fafcdf7272393b24f41e9c210bcc113e23c7ca1e6503`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixtures for the cursor-spec builder unit-test package.

## Module-level bindings

`CHILD_RECORD` (L18), `PARENT_RECORD` (L19), `CHILD_TABLE` (L20), `PARENT_TABLE` (L21), `KEY_COLUMN` (L22), `ORDER_COLUMN` (L23)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from types import SimpleNamespace
import pytest
from converter.generators.db2_infrastructure.spec_builder.spec_relationship_policy import SpecRelationshipPolicy
from converter.generators.db2_infrastructure.spec_builder.spec_select_augmenter import SpecSelectAugmenter
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.py](../../converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.py](../../converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.md)

## Symbol contracts and control points

### `StubHostVariableResolver` - L26-L38

```python
class StubHostVariableResolver()
```

Returns deterministic DCLGEN host references.

### `StubHostVariableResolver.host_references_for_columns` - L30-L38

```python
host_references_for_columns(table_name: str, columns: list[str]) -> list[str]
```

Observed calls (lexical order): `str`, `str(table_name).upper`, `str(column).replace`.

### `StubLineUtils` - L41-L46

```python
class StubLineUtils()
```

Only the reporter contract is needed.

### `StubLineUtils.normalize_include_name` - L45-L46

```python
normalize_include_name(table_name: str) -> str
```

Observed calls (lexical order): `str`, `str(table_name or '').strip`, `str(table_name or '').strip().upper`.

### `StubWhereBuilder` - L49-L61

```python
class StubWhereBuilder()
```

Keeps relationship-policy tests independent of predicate parsing.

Declared class/data-model fields:

```python
messages: list[str]
```

### `StubWhereBuilder.__init__` - L54-L55

```python
__init__(self) -> None
```

### `StubWhereBuilder.predicates` - L58-L61

```python
predicates(_conditions) -> list[str]
```

### `StubRelationship` - L65-L71

```python
class StubRelationship()
```

Declared class/data-model fields:

```python
parent_record: str = PARENT_RECORD
conditions: list[object] | None = None
```

### `StubRelationship.__post_init__` - L69-L71

```python
__post_init__(self) -> None
```

Observed calls (lexical order): `object`.

Control points:

- L70: `if self.conditions is None`

### `StubRelationshipResolver` - L74-L79

```python
class StubRelationshipResolver()
```

Returns a relationship with one parent-side predicate.

### `StubRelationshipResolver.resolve_for_child_record` - L78-L79

```python
resolve_for_child_record(_record: str) -> StubRelationship
```

Observed calls (lexical order): `StubRelationship`.

### `owner_without_line_utils` - L83-L88

```python
owner_without_line_utils()
```

Minimum owner used to prove reporter creation is lazy.

Observed calls (lexical order): `SimpleNamespace`, `StubHostVariableResolver`, `StubRelationshipResolver`.

### `owner_with_line_utils` - L92-L98

```python
owner_with_line_utils()
```

Owner used by include-name/reporting tests.

Observed calls (lexical order): `SimpleNamespace`, `StubHostVariableResolver`, `StubRelationshipResolver`, `StubLineUtils`.

### `relationship_policy` - L102-L107

```python
relationship_policy()
```

Policy with deterministic relationship and predicate collaborators.

Observed calls (lexical order): `SpecRelationshipPolicy`, `StubRelationshipResolver`, `StubWhereBuilder`.

### `augmenter` - L111-L116

```python
augmenter()
```

Actual select augmenter with only required dependencies.

Observed calls (lexical order): `SpecSelectAugmenter`, `StubHostVariableResolver`, `StubWhereBuilder`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
