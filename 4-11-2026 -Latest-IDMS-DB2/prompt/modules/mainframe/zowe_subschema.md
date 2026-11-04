# `mainframe/zowe_subschema.py`

Source: [mainframe/zowe_subschema.py](../../../mainframe/zowe_subschema.py) | 144 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `ac91ee42eb2be3a016bc0aa68b979f49b90779e7bfb5e22bcdcf5d2e6839fb54`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Element records of a logical record, read from the subschema source.

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from mainframe.zowe_env import setting
from mainframe.zowe_patterns import BLOCK_END_PATTERN, ELEMENT_TOKEN_PATTERN, ELEMENTS_ARE_PATTERN, LOGICAL_RECORD_PATTERN, NAME_LIST_ONLY_PATTERN, SUBSCHEMA_CLAUSE_HEAD_PATTERN
from mainframe.zowe_rules import ELEMENT_NAME_MIN_LENGTH, NAME_RECORD_PREFIX, SUBSCHEMA_CLAUSE_KEYWORDS, SUBSCHEMA_ELEMENT_NOISE, TEXT_ENCODING
```

## Local dependency notes

- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_patterns.py](zowe_patterns.md)
- [mainframe/zowe_rules.py](zowe_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_fetcher.py](zowe_fetcher.md)

## Symbol contracts and control points

### `record_prefix` - L38-L40

```python
record_prefix() -> str
```

Optional application filter. Blank accepts every record name.

Observed calls (lexical order): `setting`, `setting('', NAME_RECORD_PREFIX, '').strip`, `setting('', NAME_RECORD_PREFIX, '').strip().upper`.

### `starts_new_clause` - L43-L48

```python
starts_new_clause(line: str) -> bool
```

True when the line begins a new subschema DDL clause.

Observed calls (lexical order): `SUBSCHEMA_CLAUSE_HEAD_PATTERN.match`, `str`, `match.group`, `match.group('head').strip`, `match.group('head').strip().upper`.

Control points:

- L46: `if not match`

### `is_name_list` - L51-L57

```python
is_name_list(line: str) -> bool
```

True when the line contains ONLY names and list separators.

Observed calls (lexical order): `NAME_LIST_ONLY_PATTERN.match`, `bool`, `str`, `str(line or '').strip`.

### `is_element_name` - L60-L70

```python
is_element_name(token: str, prefix: str) -> bool
```

Observed calls (lexical order): `str`, `str(token or '').strip`, `str(token or '').strip().upper`, `len`, `name.startswith`.

Control points:

- L62: `if len(name) < ELEMENT_NAME_MIN_LENGTH`
- L64: `if name in SUBSCHEMA_ELEMENT_NOISE`
- L66: `if name in SUBSCHEMA_CLAUSE_KEYWORDS`
- L68: `if prefix and (not name.startswith(prefix))`

### `_collect` - L73-L77

```python
_collect(target: list[str], text: str, prefix: str) -> None
```

Observed calls (lexical order): `ELEMENT_TOKEN_PATTERN.findall`, `str`, `token.strip`, `token.strip().upper`, `is_element_name`, `target.append`.

Control points:

- L74: `for token in ELEMENT_TOKEN_PATTERN.findall(str(text or ''))`
- L76: `if is_element_name(name, prefix) and name not in target`

### `parse_element_records` - L80-L121

```python
parse_element_records(text: str) -> dict[str, list[str]]
```

{logical record name: \[element record names\]}

Observed calls (lexical order): `record_prefix`, `str`, `str(text or '').splitlines`, `raw_line.rstrip`, `LOGICAL_RECORD_PATTERN.match`, `match.group`, `match.group('lr').strip`, `match.group('lr').strip().upper`, `records.setdefault`, `BLOCK_END_PATTERN.match`, `ELEMENTS_ARE_PATTERN.match`, `_collect`, `elements.group`, `is_name_list`, `starts_new_clause`.

Control points:

- L87: `for raw_line in str(text or '').splitlines()`
- L91: `if match`
- L97: `if not current`
- L100: `if BLOCK_END_PATTERN.match(line)`
- L105: `if elements`
- L110: `if not collecting`
- L115: `if starts_new_clause(line) or not is_name_list(line)`

### `element_records_for` - L124-L144

```python
element_records_for(path: Path, logical_record: str) -> list[str]
```

Element records of ONE logical record. Empty when not found.

Observed calls (lexical order): `Path`, `target.is_file`, `parse_element_records`, `target.read_text`, `str`, `str(logical_record or '').strip`, `str(logical_record or '').strip().upper`, `wanted.split`, `records.items`, `name.split`.

Control points:

- L127: `if not target.is_file()`
- L135: `if wanted in records`
- L140: `for (name, elements) in records.items()`
- L141: `if name.split('-')[0] == base`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
