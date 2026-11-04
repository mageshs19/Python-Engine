# `converter/repositories/lrf_repository.py`

Source: [converter/repositories/lrf_repository.py](../../../../converter/repositories/lrf_repository.py) | 78 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `beb4fc070bafc406a1dbb55de6ee0365c3ca62f8b76664cab24c20ea9c2c2255`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Read-only lookups over parsed LRF metadata.

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import LogicalRecord, LrfPath
from converter.services.name_normalizer import NameNormalizer
from rules.lrf_rules import PATH_GROUP_ERASE, PATH_GROUP_OBTAIN
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_lrf_keyword_scope_safety.py](../../tests/test_lrf_keyword_scope_safety.md)
- [tests/test_lrf_path_expander.py](../../tests/test_lrf_path_expander.md)
- [tests/test_lrf_update_expander.py](../../tests/test_lrf_update_expander.md)

## Symbol contracts and control points

### `LrfRepository` - L12-L78

```python
class LrfRepository()
```

### `LrfRepository.__init__` - L13-L18

```python
__init__(self, logical_records: list[LogicalRecord] | None=None) -> None
```

Observed calls (lexical order): `list`, `NameNormalizer.normalize`.

### `LrfRepository.is_empty` - L20-L21

```python
is_empty(self) -> bool
```

### `LrfRepository.names` - L23-L24

```python
names(self) -> list[str]
```

### `LrfRepository.get` - L26-L27

```python
get(self, logical_record_name: str) -> LogicalRecord | None
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self._by_name.get`.

### `LrfRepository.element_records` - L29-L31

```python
element_records(self, logical_record_name: str) -> list[str]
```

Observed calls (lexical order): `self.get`, `list`.

### `LrfRepository.path_for_keyword` - L33-L57

```python
path_for_keyword(self, keyword: str, logical_record_name: str | None=None) -> LrfPath | None
```

Resolve a keyword without silently crossing logical-record scope.

Observed calls (lexical order): `NameNormalizer.normalize`, `len`.

Control points:

- L55: `if len(matches) != 1`

### `LrfRepository.obtain_paths` - L59-L60

```python
obtain_paths(self, logical_record_name: str) -> list[LrfPath]
```

Observed calls (lexical order): `self._paths`.

### `LrfRepository.erase_paths` - L62-L63

```python
erase_paths(self, logical_record_name: str) -> list[LrfPath]
```

Observed calls (lexical order): `self._paths`.

### `LrfRepository.owns_record` - L65-L72

```python
owns_record(self, record_name: str) -> list[str]
```

Which logical records include this IDMS record as an element.

Observed calls (lexical order): `NameNormalizer.normalize`, `any`.

### `LrfRepository._paths` - L74-L78

```python
_paths(self, logical_record_name: str, verb: str) -> list[LrfPath]
```

Observed calls (lexical order): `self.get`.

Control points:

- L76: `if not record`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
