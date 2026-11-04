# `converter/repositories/copybook_repository.py`

Source: [converter/repositories/copybook_repository.py](../../../../converter/repositories/copybook_repository.py) | 248 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `62f9d56364759691f37d538090b52b156eacb9258839922252b365b554affd36`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
import re
from converter.domain.models import CopybookField
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_copybook_redefines_metadata.py](../../tests/test_copybook_redefines_metadata.md)
- [tests/test_generic_unused_copybook_and_group_move.py](../../tests/test_generic_unused_copybook_and_group_move.md)
- [tests/test_lrf_key_binding_planner.py](../../tests/test_lrf_key_binding_planner.md)
- [tests/test_repositories.py](../../tests/test_repositories.md)
- [tests/test_schema_driven_4310_generic_rules.py](../../tests/test_schema_driven_4310_generic_rules.md)

## Symbol contracts and control points

### `CopybookRepository` - L7-L248

```python
class CopybookRepository()
```

Repository wrapper for optional copybook fields.

### `CopybookRepository.__init__` - L12-L16

```python
__init__(self, fields: list[CopybookField] | None=None) -> None
```

### `CopybookRepository.all` - L18-L21

```python
all(self) -> list[CopybookField]
```

Observed calls (lexical order): `list`.

### `CopybookRepository.count` - L23-L26

```python
count(self) -> int
```

Observed calls (lexical order): `len`.

### `CopybookRepository.names` - L28-L37

```python
names(self) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `sorted`.

### `CopybookRepository.find` - L39-L52

```python
find(self, field_name: str) -> CopybookField | None
```

Observed calls (lexical order): `NameNormalizer.normalize`.

Control points:

- L45: `if not target`
- L48: `for field in self.fields`
- L49: `if NameNormalizer.normalize(field.name) == target`

### `CopybookRepository.picture_for` - L54-L63

```python
picture_for(self, field_name: str) -> str
```

Observed calls (lexical order): `self.find`.

Control points:

- L60: `if field is None`

### `CopybookRepository.usage_for` - L65-L74

```python
usage_for(self, field_name: str) -> str
```

Observed calls (lexical order): `self.find`.

Control points:

- L71: `if field is None`

### `CopybookRepository.occurs_for` - L76-L85

```python
occurs_for(self, field_name: str) -> str
```

Observed calls (lexical order): `self.find`.

Control points:

- L82: `if field is None`

### `CopybookRepository.redefines_for` - L88-L90

```python
redefines_for(self, field_name: str) -> str
```

Observed calls (lexical order): `self.find`, `getattr`, `str`, `str(getattr(field, 'redefines', '') or '').strip`, `str(getattr(field, 'redefines', '') or '').strip().upper`.

### `CopybookRepository.effective_picture_for` - L92-L105

```python
effective_picture_for(self, field_name: str) -> str
```

Return a field PIC or the PIC of its REDEFINES base, if provable.

Observed calls (lexical order): `str`, `str(field_name or '').strip`, `str(field_name or '').strip().upper`, `set`, `seen.add`, `self.find`, `getattr`, `str(getattr(field, 'picture', '') or '').strip`, `str(getattr(field, 'picture', '') or '').strip().upper`, `str(getattr(field, 'redefines', '') or '').strip`, `str(getattr(field, 'redefines', '') or '').strip().upper`.

Control points:

- L96: `while current and current not in seen`
- L99: `if field is None`
- L102: `if picture`

### `CopybookRepository.group_width_for` - L107-L159

```python
group_width_for(self, field_name: str) -> int
```

Compute a group width from its non-redefined descendants when possible.

Observed calls (lexical order): `self.find`, `self.effective_picture_for`, `self._picture_width`, `enumerate`, `next`, `int`, `str`, `len`, `getattr`, `str(getattr(field, 'redefines', '') or '').strip`, `str(getattr(field, 'picture', '') or '').strip`.

Control points:

- L110: `if target is None`
- L113: `if effective`
- L122: `while index < len(self.fields)`
- L129: `if level <= target_level`
- L131: `if str(getattr(field, 'redefines', '') or '').strip()`
- L134: `while index < len(self.fields)`
- L140: `if child_level <= base_level`
- L144: `if str(getattr(field, 'picture', '') or '').strip()`
- Another 2 conditions/loops exist in this source span.

### `CopybookRepository._picture_width` - L162-L173

```python
_picture_width(picture: str) -> int
```

Observed calls (lexical order): `str`, `str(picture or '').upper`, `str(picture or '').upper().replace`, `re.sub`, `int`, `match.group`, `sum`.

### `CopybookRepository.direct_children_for` - L175-L223

```python
direct_children_for(self, field_name: str) -> list[CopybookField]
```

Return direct layout children of a group, excluding REDEFINES branches.

Observed calls (lexical order): `self.find`, `enumerate`, `next`, `int`, `str`, `len`, `getattr`, `str(getattr(field, 'redefines', '') or '').strip`, `children.append`.

Control points:

- L178: `if target is None`
- L187: `while index < len(self.fields)`
- L194: `if level <= target_level`
- L196: `if str(getattr(field, 'redefines', '') or '').strip()`
- L199: `while index < len(self.fields)`
- L205: `if child_level <= branch_level`
- L214: `while index < len(self.fields)`
- L220: `if child_level <= branch_level`

### `CopybookRepository.parent_for` - L225-L242

```python
parent_for(self, field_name: str) -> CopybookField | None
```

Return the nearest preceding lower-level field in the flattened layout.

Observed calls (lexical order): `self.find`, `enumerate`, `next`, `int`, `str`, `reversed`.

Control points:

- L228: `if target is None`
- L235: `for candidate in reversed(self.fields[:target_index])`
- L240: `if candidate_level < target_level`

### `CopybookRepository.has_field` - L244-L248

```python
has_field(self, field_name: str) -> bool
```

Observed calls (lexical order): `self.find`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
