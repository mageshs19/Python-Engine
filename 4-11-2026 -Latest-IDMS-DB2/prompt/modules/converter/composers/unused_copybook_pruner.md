# `converter/composers/unused_copybook_pruner.py`

Source: [converter/composers/unused_copybook_pruner.py](../../../../converter/composers/unused_copybook_pruner.py) | 92 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `def6a6f1c1e8218499574e194ca12ec22b4503bd1d3ff282d832442744684e44`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Provenance-driven removal of unused source COPY members.

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.name_derivation_resolver import NameDerivationResolver
```

## Local dependency notes

- [converter/services/name_derivation_resolver.py](../services/name_derivation_resolver.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_generic_unused_copybook_and_group_move.py](../../tests/test_generic_unused_copybook_and_group_move.md)

## Symbol contracts and control points

### `UnusedCopybookPruner` - L15-L92

```python
class UnusedCopybookPruner()
```

Declared class/data-model fields:

```python
_COPY = re.compile('^\\s*COPY\\s+([A-Z][A-Z0-9-]*)\\s*\\.?\\s*$', re.I)
_DECL = re.compile('^\\s*(?:0[1-9]|[1-4][0-9]|66|77|78)\\s+([A-Z][A-Z0-9-]*)\\b', re.I)
_SYMBOL = re.compile('(?<![A-Z0-9-])([A-Z][A-Z0-9-]*)(?![A-Z0-9-])', re.I)
```

### `UnusedCopybookPruner.__init__` - L20-L23

```python
__init__(self, source_members: dict[str, str] | None=None)
```

Observed calls (lexical order): `(source_members or {}).items`, `str`, `str(k).upper`, `NameDerivationResolver`.

### `UnusedCopybookPruner._split` - L26-L29

```python
_split(line: str) -> tuple[str, bool]
```

Observed calls (lexical order): `len`, `line[:6].strip`, `line[:6].strip().isdigit`, `line.lstrip`, `line.lstrip().startswith`.

Control points:

- L27: `if len(line) >= 7 and line[:6].strip().isdigit()`

### `UnusedCopybookPruner.apply` - L31-L92

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `enumerate`, `line.rstrip`, `self._split`, `body.upper`, `body.strip`, `self._COPY.fullmatch`, `match.group`, `match.group(1).upper`, `references.append`, `executable.append`, `' '.join`, `' '.join(executable).upper`, `self._SYMBOL.findall`, `set`, `self.source_members.get`.
Another 14 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L33: `if not text or not self.source_members`
- L39: `for (i, line) in enumerate(lines)`
- L41: `if comment`
- L43: `if 'PROCEDURE DIVISION' in body.upper()`
- L46: `if match and (not procedure)`
- L56: `for (index, member) in references`
- L58: `if not source`
- L61: `for (original, raw) in self.source_members.items()`
- Another 9 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
