# `converter/resolvers/record_context_resolver.py`

Source: [converter/resolvers/record_context_resolver.py](../../../../converter/resolvers/record_context_resolver.py) | 110 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `43e8f0013d0311cb5437c7733b726b9013a7612da0c4c8b68c60b2b62b5e93eb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `RecordContextResolver` - L6-L110

```python
class RecordContextResolver()
```

Resolves active source record context.

### `RecordContextResolver.__init__` - L14-L20

```python
__init__(self, mapping_repository: MappingRepository, dclgen_repository: DclgenRepository) -> None
```

### `RecordContextResolver.known_records` - L22-L25

```python
known_records(self) -> list[str]
```

Observed calls (lexical order): `self.mapping_repository.records`.

### `RecordContextResolver.record_from_text` - L27-L40

```python
record_from_text(self, text: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.known_records`.

Control points:

- L33: `if not normalized_text`
- L36: `for record in self.known_records()`
- L37: `if record and record in normalized_text`

### `RecordContextResolver.record_from_paragraph_name` - L42-L46

```python
record_from_paragraph_name(self, paragraph_name: str) -> str
```

Observed calls (lexical order): `self.record_from_text`.

### `RecordContextResolver.record_from_move_target` - L48-L52

```python
record_from_move_target(self, move_target: str) -> str
```

Observed calls (lexical order): `self.record_from_text`.

### `RecordContextResolver.record_from_initialize_target` - L54-L67

```python
record_from_initialize_target(self, initialize_target: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `text.startswith`, `self.record_from_table`, `self.record_from_text`.

Control points:

- L60: `if not text`
- L63: `if text.startswith('DCL')`

### `RecordContextResolver.record_from_table` - L69-L84

```python
record_from_table(self, table_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.known_records`, `self.mapping_repository.db2_table_for_record`.

Control points:

- L75: `if not table`
- L78: `for record in self.known_records()`
- L81: `if NameNormalizer.normalize(record_table) == table`

### `RecordContextResolver.record_from_dclgen_group` - L86-L98

```python
record_from_dclgen_group(self, group_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `text.startswith`, `self.record_from_table`.

Control points:

- L92: `if not text`
- L95: `if text.startswith('DCL')`

### `RecordContextResolver.context_strength` - L100-L110

```python
context_strength(self, record_name: str) -> int
```

Observed calls (lexical order): `self.mapping_repository.has_record`.

Control points:

- L104: `if not record_name`
- L107: `if self.mapping_repository.has_record(record_name)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
