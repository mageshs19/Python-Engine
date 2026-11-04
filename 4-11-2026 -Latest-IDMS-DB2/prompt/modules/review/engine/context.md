# `review/engine/context.py`

Source: [review/engine/context.py](../../../../review/engine/context.py) | 113 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `bbb308c4f55ed960f17bbdbe8ebc9cd66af4169045ba0a7d9be008e25bb01d81`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The single input object for a code review run. Data only.

## Module-level bindings

`KIND_RETRIEVAL` (L21), `KIND_UPDATE` (L22), `KIND_UNKNOWN` (L23), `VALID_KINDS` (L25), `__all__` (L106)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
```

## Importers (10)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/engine/__init__.py](__init__.md)
- [review/engine/check_base.py](check_base.md)
- [review/engine/reviewer.py](reviewer.md)
- [review/runner/review_file.py](../runner/review_file.md)
- [review/standards/program_kind_detector.py](../standards/program_kind_detector.md)
- [review/ui/review_panel.py](../ui/review_panel.md)
- [tests/test_business_parity_review_rules_v128.py](../../tests/test_business_parity_review_rules_v128.md)
- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)
- [tests/test_program_kind_detector.py](../../tests/test_program_kind_detector.md)
- [tests/test_review_kind_wiring.py](../../tests/test_review_kind_wiring.md)

## Symbol contracts and control points

### `normalise_kind` - L28-L31

```python
normalise_kind(value: str) -> str
```

Returns a known kind, or KIND_UNKNOWN when the value is not recognised.

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`.

### `ReviewContext` - L35-L103

```python
class ReviewContext()
```

Immutable-by-convention input for one program review.

Declared class/data-model fields:

```python
program_name: str = ''
program_kind: str = KIND_UNKNOWN
target_program_id: str = ''
source_file: str = ''
converted_cobol: str = ''
source_cobol: str = ''
sheet_mapping_rows: list = field(default_factory=list)
dclgen_columns: list = field(default_factory=list)
copybook_fields: list = field(default_factory=list)
require_metadata: bool = False
metadata_diagnostics: list[str] = field(default_factory=list)
```

### `ReviewContext.__post_init__` - L50-L59

```python
__post_init__(self) -> None
```

Observed calls (lexical order): `str`, `normalise_kind`, `list`.

### `ReviewContext.has` - L62-L71

```python
has(self, name: str) -> bool
```

True when the named input was supplied and is non-empty.

Observed calls (lexical order): `hasattr`, `str`, `getattr`, `isinstance`, `bool`, `value.strip`.

Control points:

- L64: `if not hasattr(self, str(name))`
- L67: `if isinstance(value, str)`
- L69: `if isinstance(value, (list, tuple, dict, set))`

### `ReviewContext.missing` - L73-L78

```python
missing(self, names) -> list[str]
```

Inputs a check declared in NEEDS that were not supplied.

Observed calls (lexical order): `self.has`, `str`.

### `ReviewContext.is_retrieval` - L82-L83

```python
is_retrieval(self) -> bool
```

### `ReviewContext.is_update` - L86-L87

```python
is_update(self) -> bool
```

### `ReviewContext.has_source` - L90-L91

```python
has_source(self) -> bool
```

Observed calls (lexical order): `bool`, `self.source_cobol.strip`.

### `ReviewContext.has_metadata` - L94-L97

```python
has_metadata(self) -> bool
```

Observed calls (lexical order): `bool`.

### `ReviewContext.describe` - L99-L103

```python
describe(self) -> str
```

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
