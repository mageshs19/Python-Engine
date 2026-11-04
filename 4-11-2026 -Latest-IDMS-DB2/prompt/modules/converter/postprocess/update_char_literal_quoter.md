# `converter/postprocess/update_char_literal_quoter.py`

Source: [converter/postprocess/update_char_literal_quoter.py](../../../../converter/postprocess/update_char_literal_quoter.py) | 176 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `368a7e0f075025965d1f56047b637c6e33f90e720d4967ba6b28aceb0c93ee38`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from patterns.update_char_literal_patterns import END_EXEC_PATTERN, EXEC_SQL_START_PATTERN, MOVE_NUMLIT_ONLY_PATTERN, MOVE_NUMLIT_TO_HOST_OF_GROUP_PATTERN, TO_HOST_OF_GROUP_PATTERN
from rules.update_char_literal_rules import CHAR_DB2_TYPE_PREFIXES, CHAR_LITERAL_QUOTED_DIAGNOSTIC, CHAR_PICTURE_PREFIX
```

## Local dependency notes

- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/update_char_literal_patterns.py](../../patterns/update_char_literal_patterns.md)
- [rules/update_char_literal_rules.py](../../rules/update_char_literal_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)

## Symbol contracts and control points

### `UpdateCharLiteralQuoter` - L18-L176

```python
class UpdateCharLiteralQuoter()
```

Quotes bare numeric literals moved into CHAR/VARCHAR DB2 host variables.

Declared class/data-model fields:

```python
BODY_WIDTH = 65
```

### `UpdateCharLiteralQuoter.__init__` - L33-L34

```python
__init__(self, dclgen_columns: list) -> None
```

Observed calls (lexical order): `self._build_char_host_map`.

### `UpdateCharLiteralQuoter.apply` - L39-L114

```python
apply(self, text: str, diagnostics: list[str] | None=None) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `len`, `self._logical`, `logical.upper`, `EXEC_SQL_START_PATTERN.match`, `output.append`, `END_EXEC_PATTERN.match`, `MOVE_NUMLIT_TO_HOST_OF_GROUP_PATTERN.match`, `one.group`, `self._is_char_host`, `one.group('host').upper`, `one.group('group').upper`, `self._replace_body`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L44: `if not text or not self._char_hosts`
- L59: `while index < len(lines)`
- L65: `if EXEC_SQL_START_PATTERN.match(logical)`
- L67: `if 'END-EXEC' not in upper`
- L73: `if in_exec_sql`
- L75: `if END_EXEC_PATTERN.match(logical)`
- L82: `if one and self._is_char_host(one.group('host'))`
- L95: `if move_only and index + 1 < len(lines)`
- Another 2 conditions/loops exist in this source span.

### `UpdateCharLiteralQuoter._build_char_host_map` - L119-L133

```python
_build_char_host_map(self, dclgen_columns: list) -> dict[str, bool]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `getattr`, `str`, `self._is_char_datatype`, `self._is_char_picture`, `host.upper`.

Control points:

- L121: `for column in dclgen_columns or []`
- L125: `if not host`
- L129: `if self._is_char_datatype(db2_type) or self._is_char_picture(picture)`

### `UpdateCharLiteralQuoter._is_char_host` - L135-L137

```python
_is_char_host(self, host: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.normalize(host).upper`, `self._char_hosts.get`.

### `UpdateCharLiteralQuoter._is_char_datatype` - L139-L141

```python
_is_char_datatype(self, db2_type: str) -> bool
```

Observed calls (lexical order): `str`, `str(db2_type or '').upper`, `str(db2_type or '').upper().replace`, `compact.startswith`.

### `UpdateCharLiteralQuoter._is_char_picture` - L143-L148

```python
_is_char_picture(self, picture: str) -> bool
```

Observed calls (lexical order): `str`, `str(picture or '').strip`, `str(picture or '').strip().upper`, `str(picture or '').strip().upper().lstrip`, `cleaned.startswith`, `cleaned[4:].strip`.

Control points:

- L146: `if cleaned.startswith('PIC ')`

### `UpdateCharLiteralQuoter._logical` - L155-L164

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[7:72].strip`, `body[-8:].strip`, `body[-8:].strip().isdigit`, `body.strip`, `text.strip`.

Control points:

- L157: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L159: `if len(text) > 6 and text[:6].strip().isdigit()`
- L161: `if len(body) >= 8 and body[-8:].strip().isdigit()`

### `UpdateCharLiteralQuoter._replace_body` - L166-L176

```python
_replace_body(self, line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(body or '')[:self.BODY_WIDTH].ljust`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `clean.rstrip`.

Control points:

- L169: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L173: `if len(text) > 6 and text[:6].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
