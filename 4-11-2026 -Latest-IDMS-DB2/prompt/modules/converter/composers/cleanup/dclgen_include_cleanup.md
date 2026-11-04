# `converter/composers/cleanup/dclgen_include_cleanup.py`

Source: [converter/composers/cleanup/dclgen_include_cleanup.py](../../../../../converter/composers/cleanup/dclgen_include_cleanup.py) | 252 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `3c1c50e8ee67e575e3fd1f1c857dfcfd1f79e17da98470303da872d2f68cc4a4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DCLGEN include cleanup.

## Module-level bindings

`TOKEN_EXEC_SQL` (L65), `TOKEN_END_EXEC` (L66), `TOKEN_INCLUDE` (L67), `TOKEN_LINKAGE_SECTION` (L71), `TOKEN_PROCEDURE_DIVISION` (L72), `DATA_AREA_BOUNDARIES` (L74)

## Import declarations

```python
from __future__ import annotations
from catalogs.output_sections import DCLGEN_GROUP_PREFIX
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.generators.db2_infrastructure.include_renderer import IncludeRenderer
from converter.repositories.dclgen_repository import DclgenRepository
from converter.services.name_normalizer import NameNormalizer
from patterns.db2_include_patterns import DCLGEN_GROUP_PATTERN
```

## Local dependency notes

- [catalogs/output_sections.py](../../../catalogs/output_sections.md)
- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [converter/generators/db2_infrastructure/include_renderer.py](../../generators/db2_infrastructure/include_renderer.md)
- [converter/repositories/dclgen_repository.py](../../repositories/dclgen_repository.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/db2_include_patterns.py](../../../patterns/db2_include_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)

## Symbol contracts and control points

### `DclgenIncludeCleanup` - L80-L252

```python
class DclgenIncludeCleanup()
```

Adds a missing DCLGEN include, exactly once, inside WORKING-STORAGE.

### `DclgenIncludeCleanup.__init__` - L83-L95

```python
__init__(self, dclgen_repository: DclgenRepository, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`, `IncludeRenderer`.

### `DclgenIncludeCleanup.apply` - L100-L128

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).splitlines`, `self.includes.existing`, `self._referenced_dclgen_tables`, `self.dclgen_repository.has_table`, `include_lines.extend`, `self.includes.render`, `self.messages.add`, `self._db2_include_insert_index`, `'\n'.join`, `text.rstrip`, `'\n'.join(updated).rstrip`.

Control points:

- L101: `if not text`
- L114: `if not missing`
- L118: `for table in missing`
- L124: `if insert_index < 0`

### `DclgenIncludeCleanup._referenced_dclgen_tables` - L133-L166

```python
_referenced_dclgen_tables(self, lines: list[str]) -> list[str]
```

Table names implied by DCLGEN host group references.

Observed calls (lexical order): `set`, `self._logical`, `DCLGEN_GROUP_PATTERN.finditer`, `NameNormalizer.normalize`, `NameNormalizer.normalize(str(match.group('group') or '')).upper`, `match.group`, `str`, `group.startswith`, `len`, `self.includes.is_infrastructure`, `seen.add`, `output.append`.

Control points:

- L141: `for line in lines`
- L143: `if not logical`
- L146: `for match in DCLGEN_GROUP_PATTERN.finditer(logical)`
- L151: `if not group.startswith(DCLGEN_GROUP_PREFIX)`
- L155: `if not table or table in seen`
- L160: `if self.includes.is_infrastructure(table)`

### `DclgenIncludeCleanup._existing_includes` - L168-L173

```python
_existing_includes(self, text: str) -> set[str]
```

Every include already present, whichever shape carries it.

Observed calls (lexical order): `self.includes.existing`, `str`, `str(text or '').splitlines`.

### `DclgenIncludeCleanup._data_area_boundary` - L178-L193

```python
_data_area_boundary(self, lines: list[str]) -> int
```

Index of the first line that ends the DATA DIVISION area.

Observed calls (lexical order): `enumerate`, `self._logical`, `self._logical(line).upper`, `logical.startswith`, `len`.

Control points:

- L185: `for (index, line) in enumerate(lines)`
- L187: `if not logical`
- L190: `if logical.startswith(DATA_AREA_BOUNDARIES)`

### `DclgenIncludeCleanup._db2_include_insert_index` - L195-L246

```python
_db2_include_insert_index(self, lines: list[str]) -> int
```

Insert after the last include INSIDE the data area.

Observed calls (lexical order): `self._data_area_boundary`, `range`, `self._logical`, `self._logical(lines[index]).upper`, `logical.startswith`, `len`.

Control points:

- L213: `for index in range(boundary)`
- L215: `if not logical`
- L218: `if logical.startswith(TOKEN_EXEC_SQL)`
- L222: `if TOKEN_END_EXEC in logical`
- L223: `if include_seen_in_block`
- L229: `if in_exec_sql and TOKEN_INCLUDE in logical`
- L232: `if in_exec_sql and logical.startswith(TOKEN_END_EXEC)`
- L233: `if include_seen_in_block`
- Another 2 conditions/loops exist in this source span.

### `DclgenIncludeCleanup._logical` - L251-L252

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
