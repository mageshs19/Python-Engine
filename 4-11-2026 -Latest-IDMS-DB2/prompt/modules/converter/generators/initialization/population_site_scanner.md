# `converter/generators/initialization/population_site_scanner.py`

Source: [converter/generators/initialization/population_site_scanner.py](../../../../../converter/generators/initialization/population_site_scanner.py) | 300 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `da9bf57974e6902616f2bb298b841458afceaf43e07021280c57775f239fa866`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Finds the paragraph that POPULATES a DCLGEN group.

## Module-level bindings

`NO_CURSOR` (L62), `MOVE_VERB` (L65), `INITIALIZE_VERB` (L66), `TO_KEYWORD` (L67), `QUALIFIER_OPENERS` (L68), `CONTINUATION_SCAN_LIMIT` (L72), `__all__` (L300)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Set, Tuple
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.initialization.paragraph_index import ParagraphIndex
from patterns.initialization_scope_patterns import COBOL_HOST_GROUP_PATTERN
from rules.initialization_placement_rules import DCLGEN_GROUP_PREFIX, SCOPE_ROW
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [converter/generators/initialization/paragraph_index.py](paragraph_index.md)
- [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)
- [tests/initialization_scope/test_population_scope.py](../../../tests/initialization_scope/test_population_scope.md)

## Symbol contracts and control points

### `InitializationSite` - L76-L93

```python
class InitializationSite()
```

A place where a DCLGEN group must be cleared.

Declared class/data-model fields:

```python
index: int
group: str
indent: str
owner: str
scope: str = SCOPE_ROW
cursor: str = NO_CURSOR
```

### `InitializationSite.is_resolved` - L92-L93

```python
is_resolved(self) -> bool
```

Observed calls (lexical order): `bool`.

### `_Write` - L97-L100

```python
class _Write()
```

Declared class/data-model fields:

```python
index: int
group: str
owner: str
```

### `PopulationSiteScanner` - L103-L297

```python
class PopulationSiteScanner()
```

Locates the one paragraph that fills a per-row DCLGEN buffer.

### `PopulationSiteScanner.__init__` - L106-L112

```python
__init__(self, geometry: Optional[LineGeometry]=None, paragraphs: Optional[ParagraphIndex]=None) -> None
```

Observed calls (lexical order): `LineGeometry`, `ParagraphIndex`.

### `PopulationSiteScanner.sites` - L117-L175

```python
sites(self, lines: List[str], exclude_groups: Optional[Iterable[str]]=None) -> List[InitializationSite]
```

Observed calls (lexical order): `list`, `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `self._writes`, `owners_by_group.setdefault`, `owners_by_group.setdefault(write.group, set()).add`, `set`, `write.owner.upper`, `self._already_initialised`, `self._first_executable_by_paragraph`, `len`, `first_executable.get`, `emitted.add`, `output.append`, `InitializationSite`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L130: `if not writes`
- L134: `for write in writes`
- L145: `for write in writes`
- L148: `if write.group in excluded or write.group in emitted`
- L152: `if len(owners_by_group[write.group]) != 1`
- L156: `if (owner_key, write.group) in already`
- L161: `if anchor < 0`

### `PopulationSiteScanner.groups` - L177-L178

```python
groups(self, lines: List[str]) -> Set[str]
```

Observed calls (lexical order): `self.sites`.

### `PopulationSiteScanner._writes` - L183-L200

```python
_writes(self, lines: List[str]) -> List[_Write]
```

Observed calls (lexical order): `enumerate`, `self.geometry.is_comment_or_blank`, `self._receiving_group`, `self.paragraphs.owner_of`, `_Write`, `output.append`.

Control points:

- L186: `for (index, line) in enumerate(lines)`
- L187: `if self.geometry.is_comment_or_blank(line)`
- L191: `if not group`
- L195: `if not owner`

### `PopulationSiteScanner._already_initialised` - L202-L224

```python
_already_initialised(self, lines: List[str]) -> Set[Tuple[str, str]]
```

Observed calls (lexical order): `set`, `enumerate`, `self.geometry.is_comment_or_blank`, `self._body`, `body.startswith`, `len`, `self._dclgen_group`, `self.paragraphs.owner_of`, `found.add`, `owner.upper`.

Control points:

- L208: `for (index, line) in enumerate(lines)`
- L209: `if self.geometry.is_comment_or_blank(line)`
- L213: `if not body.startswith(INITIALIZE_VERB)`
- L217: `if not group`
- L221: `if owner`

### `PopulationSiteScanner._receiving_group` - L226-L242

```python
_receiving_group(self, lines: List[str], index: int) -> str
```

The DCLGEN group this MOVE writes INTO, or ''.

Observed calls (lexical order): `self._body`, `body.startswith`, `body.rfind`, `len`, `self._dclgen_group`, `self._continuation_group`.

Control points:

- L229: `if not body.startswith(MOVE_VERB)`
- L233: `if cut < 0`
- L237: `if group`

### `PopulationSiteScanner._continuation_group` - L244-L259

```python
_continuation_group(self, lines: List[str], index: int) -> str
```

Observed calls (lexical order): `len`, `self.geometry.is_comment_or_blank`, `self._body`, `tail.startswith`, `self._dclgen_group`.

Control points:

- L248: `while position < len(lines) and scanned < CONTINUATION_SCAN_LIMIT`
- L249: `if self.geometry.is_comment_or_blank(lines[position])`
- L255: `if not tail.startswith(QUALIFIER_OPENERS)`

### `PopulationSiteScanner._dclgen_group` - L261-L272

```python
_dclgen_group(self, text: str) -> str
```

Observed calls (lexical order): `COBOL_HOST_GROUP_PATTERN.search`, `str`, `str(text or '').strip`, `str(text or '').strip().rstrip`, `str(text or '').strip().rstrip('.').split`, `token.upper`, `match.group`, `str(match.group('group') or '').upper`, `group.startswith`.

Control points:

- L263: `if not match`
- L270: `if not group.startswith(DCLGEN_GROUP_PREFIX)`

### `PopulationSiteScanner._first_executable_by_paragraph` - L274-L294

```python
_first_executable_by_paragraph(self, lines: List[str]) -> Dict[str, int]
```

Observed calls (lexical order): `enumerate`, `self.geometry.is_comment_or_blank`, `self.paragraphs.is_paragraph_header`, `self.paragraphs.owner_of`, `owner.upper`.

Control points:

- L280: `for (index, line) in enumerate(lines)`
- L281: `if self.geometry.is_comment_or_blank(line)`
- L283: `if self.paragraphs.is_paragraph_header(line)`
- L287: `if not owner`
- L291: `if key not in first`

### `PopulationSiteScanner._body` - L296-L297

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `' '.join`, `self.geometry.body`, `self.geometry.body(line).upper`, `self.geometry.body(line).upper().split`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
