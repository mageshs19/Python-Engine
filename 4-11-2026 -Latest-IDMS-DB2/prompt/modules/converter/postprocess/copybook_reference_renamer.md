# `converter/postprocess/copybook_reference_renamer.py`

Source: [converter/postprocess/copybook_reference_renamer.py](../../../../converter/postprocess/copybook_reference_renamer.py) | 156 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `ed9c55177eaa3d14fc3a5132ef8579de85b3fda095299aae0666c7f660c616f9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.name_derivation_resolver import NameDerivationResolver
from patterns.copybook_reference_rename_patterns import COPY_NAME_PATTERN, WORD_REFERENCE_PATTERN_TEMPLATE
```

## Local dependency notes

- [converter/services/name_derivation_resolver.py](../services/name_derivation_resolver.md)
- [patterns/copybook_reference_rename_patterns.py](../../patterns/copybook_reference_rename_patterns.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/retrieval/retrieval_program_converter.py](../../runners/retrieval/retrieval_program_converter.md)
- [tests/test_copybook_reference_renamer.py](../../tests/test_copybook_reference_renamer.md)

## Symbol contracts and control points

### `CopybookReferenceRenamer` - L14-L156

```python
class CopybookReferenceRenamer()
```

Renames source copybook references to their derived DB2 names.

### `CopybookReferenceRenamer.__init__` - L47-L48

```python
__init__(self, resolver: NameDerivationResolver | None=None) -> None
```

Observed calls (lexical order): `NameDerivationResolver`.

### `CopybookReferenceRenamer.apply` - L50-L116

```python
apply(self, text: str, diagnostics: list[str] | None=None) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._collect_renames`, `re.compile`, `WORD_REFERENCE_PATTERN_TEMPLATE.format`, `re.escape`, `renames.items`, `set`, `self._is_comment_or_debug`, `output.append`, `pattern.sub`, `COPY_NAME_PATTERN.search`, `self._body`, `copy_match.group`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L55: `if not text`
- L66: `if not renames`
- L84: `for line in lines`
- L85: `if self._is_comment_or_debug(line)`
- L90: `for (pattern, new) in compiled`
- L93: `if new_line != line`
- L99: `if copy_match`
- L101: `if copied in renames.values()`
- Another 2 conditions/loops exist in this source span.

### `CopybookReferenceRenamer._collect_renames` - L119-L134

```python
_collect_renames(self, lines: list[str]) -> dict[str, str]
```

old -> new for every derivable copybook the program COPYs.

Observed calls (lexical order): `self._is_comment_or_debug`, `COPY_NAME_PATTERN.search`, `self._body`, `match.group`, `match.group('name').strip`, `match.group('name').strip().upper`, `self._resolver.is_derivable`, `self._resolver.derive`.

Control points:

- L122: `for line in lines`
- L123: `if self._is_comment_or_debug(line)`
- L126: `if not match`
- L129: `if not name or not self._resolver.is_derivable(name)`
- L132: `if derived and derived != name`

### `CopybookReferenceRenamer._is_comment_or_debug` - L139-L148

```python
_is_comment_or_debug(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text.strip`, `stripped.startswith`, `stripped.upper`, `stripped.upper().startswith`.

Control points:

- L141: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `CopybookReferenceRenamer._body` - L150-L156

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L152: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L154: `if len(text) > 7 and text[:6].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
