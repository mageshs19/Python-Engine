# `converter/analyzers/lr_access/lr_access_models.py`

Source: [converter/analyzers/lr_access/lr_access_models.py](../../../../../converter/analyzers/lr_access/lr_access_models.py) | 103 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `6376d47b2d59b9f7a5fc299f1376c1a85e9f7ba19b58552b2715dcfff0ea4f0e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> One classified LR access site. Data only - no parsing, no rendering.

## Module-level bindings

`__all__` (L103)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from rules.lr_access_rules import KIND_BOUNDED_SEARCH, KIND_DEFAULT, KIND_FIRST_ONLY, KIND_KEYED_READ, LOOP_NONE
```

## Local dependency notes

- [rules/lr_access_rules.py](../../../rules/lr_access_rules.md)

## Symbol contracts and control points

### `LrAccessSite` - L31-L100

```python
class LrAccessSite()
```

One LR access and the shape the renderer must produce.

Declared class/data-model fields:

```python
record_name: str = ''
within_name: str = ''
kind: str = KIND_DEFAULT
loop_form: str = LOOP_NONE
first_line: int = 0
next_line: int = 0
loop_header_line: int = 0
loop_end_line: int = 0
loop_condition: str = ''
table_name: str = ''
key_columns: list[str] = field(default_factory=list)
bound_predicates: list[str] = field(default_factory=list)
extra_filters: list[str] = field(default_factory=list)
order_by: list[str] = field(default_factory=list)
not_found_literals: set[str] = field(default_factory=set)
end_of_set_literals: set[str] = field(default_factory=set)
diagnostics: list[str] = field(default_factory=list)
```

### `LrAccessSite.key` - L71-L72

```python
key(self) -> tuple[str, str]
```

### `LrAccessSite.is_singleton` - L75-L81

```python
is_singleton(self) -> bool
```

Renders as one SELECT rather than a cursor.

### `LrAccessSite.removes_loop` - L84-L96

```python
removes_loop(self) -> bool
```

The driving loop has no work left once this is a singleton.

### `LrAccessSite.where_predicates` - L99-L100

```python
where_predicates(self) -> list[str]
```

Observed calls (lexical order): `list`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
