# `converter/validators/mapping_scope_filter.py`

Source: [converter/validators/mapping_scope_filter.py](../../../../converter/validators/mapping_scope_filter.py) | 129 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `2f0fa925f92c8abcd91e8ee73a128d7a0ed42ccd86eba5ce55bb457c9b29d1bc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Scopes mapping validation messages to the program being converted.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from patterns.mapping_scope_patterns import MESSAGE_TABLE_PATTERN, SOURCE_TOKEN_PATTERN
from rules.mapping_scope_rules import DIAG_SCOPE_APPLIED, ENFORCE_MAPPING_SCOPE_FILTER, OUT_OF_SCOPE_TEMPLATE
```

## Local dependency notes

- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/mapping_scope_patterns.py](../../patterns/mapping_scope_patterns.md)
- [rules/mapping_scope_rules.py](../../rules/mapping_scope_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)

## Symbol contracts and control points

### `MappingScopeFilter` - L30-L129

```python
class MappingScopeFilter()
```

Rewrites mapping gaps for tables the program does not reference.

### `MappingScopeFilter.__init__` - L33-L40

```python
__init__(self, mapping_repository, table_name_resolver) -> None
```

### `MappingScopeFilter.apply` - L45-L84

```python
apply(self, messages: list[str], source_text: str) -> list[str]
```

Observed calls (lexical order): `list`, `self._referenced_tables`, `self._table_of`, `out.append`, `OUT_OF_SCOPE_TEMPLATE.format`, `self.messages.append`, `DIAG_SCOPE_APPLIED.format`.

Control points:

- L52: `if not messages or not ENFORCE_MAPPING_SCOPE_FILTER`
- L60: `for message in messages`
- L63: `if not table`
- L69: `if table in referenced`
- L76: `if rewritten`

### `MappingScopeFilter._referenced_tables` - L89-L113

```python
_referenced_tables(self, source_text: str) -> set[str]
```

Tables whose name or mapped record appears in the source.

Observed calls (lexical order): `NameNormalizer.compact`, `match.group`, `SOURCE_TOKEN_PATTERN.finditer`, `str`, `tokens.discard`, `set`, `self._records`, `NameNormalizer.normalize`, `self.table_name_resolver.table_for_record`, `referenced.add`.

Control points:

- L99: `for record in self._records()`
- L103: `if not table`
- L106: `if NameNormalizer.compact(table) in tokens`
- L110: `if NameNormalizer.compact(record) in tokens`

### `MappingScopeFilter._records` - L115-L122

```python
_records(self) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.mapping_repository.records`.

### `MappingScopeFilter._table_of` - L125-L129

```python
_table_of(message: str) -> str
```

Observed calls (lexical order): `MESSAGE_TABLE_PATTERN.search`, `str`, `NameNormalizer.normalize`, `match.group`.

Control points:

- L127: `if not match`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
