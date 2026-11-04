# `converter/postprocess/update_date_host_converter.py`

Source: [converter/postprocess/update_date_host_converter.py](../../../../converter/postprocess/update_date_host_converter.py) | 268 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `e3ff097557725d3954d901319e632109fe5b7273a0432a8f81e158ff279ff489`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L268)

## Import declarations

```python
from __future__ import annotations
from converter.services.db2_date_sentinel_policy import Db2DateSentinelPolicy
from converter.services.name_normalizer import NameNormalizer
from patterns.update_date_host_patterns import END_EXEC_PATTERN, EXEC_SQL_START_PATTERN, MOVE_SOURCE_ONLY_PATTERN, MOVE_TO_HOST_OF_GROUP_PATTERN, TO_HOST_OF_GROUP_PATTERN
from rules.sql_generation_rules import DB2_DATE_NULL_SENTINEL
```

## Local dependency notes

- [converter/services/db2_date_sentinel_policy.py](../services/db2_date_sentinel_policy.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/update_date_host_patterns.py](../../patterns/update_date_host_patterns.md)
- [rules/sql_generation_rules.py](../../rules/sql_generation_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)
- [tests/test_update_date_host_converter.py](../../tests/test_update_date_host_converter.md)

## Symbol contracts and control points

### `UpdateDateHostConverter` - L18-L265

```python
class UpdateDateHostConverter()
```

Converts raw moves into DB2 DATE host variables to the manual date form.

Declared class/data-model fields:

```python
_ALREADY_REALIGNED_SOURCE = 'DADDMMCCYY'
_PROTECTED_SOURCES = ('TSTIMESTAMP', 'CSPROGRAM')
_AUDIT_HOST_PREFIXES = ('TSUPDATE', 'TSCREATE', 'IDUSERID', 'NRUSERID')
BODY_WIDTH = 65
```

### `UpdateDateHostConverter.__init__` - L57-L59

```python
__init__(self, dclgen_columns: list) -> None
```

Observed calls (lexical order): `self._build_date_host_map`.

### `UpdateDateHostConverter.apply` - L64-L150

```python
apply(self, text: str, diagnostics: list[str] | None=None) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `len`, `self._logical`, `logical.upper`, `EXEC_SQL_START_PATTERN.match`, `output.append`, `END_EXEC_PATTERN.match`, `MOVE_TO_HOST_OF_GROUP_PATTERN.match`, `one.group`, `one.group('source').strip`, `one.group('host').upper`, `one.group('group').upper`, `self._should_convert`.
Another 13 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L69: `if not text or not self._date_hosts`
- L86: `while index < len(lines)`
- L91: `if EXEC_SQL_START_PATTERN.match(logical)`
- L92: `if 'END-EXEC' not in upper`
- L98: `if in_exec_sql`
- L100: `if END_EXEC_PATTERN.match(logical)`
- L107: `if one`
- L111: `if self._should_convert(host, source)`
- Another 5 conditions/loops exist in this source span.

### `UpdateDateHostConverter._should_convert` - L155-L170

```python
_should_convert(self, host: str, source: str) -> bool
```

Observed calls (lexical order): `self._is_date_host`, `NameNormalizer.normalize`, `NameNormalizer.normalize(host).upper`, `NameNormalizer.normalize(host).upper().replace`, `host_key.startswith`, `NameNormalizer.to_cobol`, `NameNormalizer.to_cobol(source).upper`, `NameNormalizer.to_cobol(source).upper().replace`, `source.startswith`, `source[0].isdigit`.

Control points:

- L156: `if not self._is_date_host(host)`
- L160: `if host_key.startswith(self._AUDIT_HOST_PREFIXES)`
- L164: `if src_key == self._ALREADY_REALIGNED_SOURCE`
- L166: `if src_key in self._PROTECTED_SOURCES`
- L168: `if not source or source[0].isdigit() or source.startswith("'")`

### `UpdateDateHostConverter._conversion_lines` - L172-L191

```python
_conversion_lines(self, reference_line: str, source: str, host: str, group: str) -> list[str]
```

Observed calls (lexical order): `Db2DateSentinelPolicy`, `sentinel.guard_lines`, `self._sentinel_messages.extend`, `self._replace_body`.

### `UpdateDateHostConverter._build_date_host_map` - L196-L207

```python
_build_date_host_map(self, dclgen_columns: list) -> dict[str, bool]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `getattr`, `str`, `self._is_date_datatype`, `host.upper`.

Control points:

- L198: `for column in dclgen_columns or []`
- L202: `if not host`
- L205: `if self._is_date_datatype(db2_type)`

### `UpdateDateHostConverter._is_date_host` - L209-L211

```python
_is_date_host(self, host: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.normalize(host).upper`, `self._date_hosts.get`.

### `UpdateDateHostConverter._is_date_datatype` - L213-L219

```python
_is_date_datatype(self, db2_type: str) -> bool
```

Observed calls (lexical order): `str`, `str(db2_type or '').upper`, `str(db2_type or '').upper().replace`, `compact.startswith`.

Control points:

- L217: `if compact.startswith('TIMESTAMP') or compact.startswith('TIME')`

### `UpdateDateHostConverter._logical` - L226-L235

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[7:72].strip`, `body[-8:].strip`, `body[-8:].strip().isdigit`, `body.strip`, `text.strip`.

Control points:

- L228: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L230: `if len(text) > 6 and text[:6].strip().isdigit()`
- L232: `if len(body) >= 8 and body[-8:].strip().isdigit()`

### `UpdateDateHostConverter._replace_body` - L237-L265

```python
_replace_body(self, line: str, body: str) -> str
```

Rewrite columns 8-72, keeping both sequence areas in place.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(body or '')[:self.BODY_WIDTH].ljust`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `clean.rstrip`.

Control points:

- L258: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L262: `if len(text) > 6 and text[:6].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
