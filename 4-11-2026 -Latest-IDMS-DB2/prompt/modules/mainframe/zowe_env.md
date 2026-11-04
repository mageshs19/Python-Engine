# `mainframe/zowe_env.py`

Source: [mainframe/zowe_env.py](../../../mainframe/zowe_env.py) | 188 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `ced995de2e4f3064faa3d9ac69ad74d084de6a0745db685064b821e4eb6f3c16`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Loads .env and resolves values per artifact.

## Module-level bindings

`_DOTENV_LOADED` (L37)

## Import declarations

```python
from __future__ import annotations
import os
from pathlib import Path
from mainframe.zowe_patterns import BARE_ENV_KEY_PATTERN, DOTENV_LINE_PATTERN, ENV_REFERENCE_PATTERN
from mainframe.zowe_rules import ARTIFACT_KEY_TEMPLATE, ENV_REFERENCE_MAX_DEPTH, MASKED_VALUE, SENSITIVE_NAMES, SHARED_KEY_TEMPLATE, ZOWE_ERROR_MESSAGES
from dotenv import find_dotenv, load_dotenv
```

## Local dependency notes

- [mainframe/zowe_patterns.py](zowe_patterns.md)
- [mainframe/zowe_rules.py](zowe_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_console.py](zowe_console.md)
- [mainframe/zowe_copybook_upload.py](zowe_copybook_upload.md)
- [mainframe/zowe_programs.py](zowe_programs.md)
- [mainframe/zowe_settings.py](zowe_settings.md)
- [mainframe/zowe_subschema.py](zowe_subschema.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)

## Symbol contracts and control points

### `load_dotenv_once` - L43-L72

```python
load_dotenv_once() -> None
```

Load the project .env exactly once. Never overwrites a real env var.

Observed calls (lexical order): `find_dotenv`, `load_dotenv`, `Path.cwd`, `Path`, `Path(__file__).resolve`, `candidate.is_file`, `candidate.read_text`, `candidate.read_text(encoding='utf-8').splitlines`, `raw_line.strip`, `line.startswith`, `DOTENV_LINE_PATTERN.match`, `match.group`, `match.group('value').strip`, `match.group('value').strip().strip`, `match.group('value').strip().strip('"').strip`, `os.environ.setdefault`.

Control points:

- L46: `if _DOTENV_LOADED`
- L57: `for candidate in (Path.cwd() / '.env', Path(__file__).resolve().parents[1] / '.env')`
- L61: `if not candidate.is_file()`
- L63: `for raw_line in candidate.read_text(encoding='utf-8').splitlines()`
- L65: `if not line or line.startswith('#')`
- L68: `if not match`

### `_expand_once` - L78-L98

```python
_expand_once(key: str, value: str) -> str
```

Replace every reference with that key's raw value.

Observed calls (lexical order): `ENV_REFERENCE_PATTERN.sub`, `ValueError`, `ZOWE_ERROR_MESSAGES['unresolved_reference'].format`.

Control points:

- L92: `if missing`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['unresolved_reference'].format(key=key, missing=missing[0]))`.

### `_expand_once.replace` - L82-L88

```python
replace(match) -> str
```

Observed calls (lexical order): `match.group`, `os.getenv`, `os.getenv(target, '').strip`, `missing.append`.

Control points:

- L85: `if not resolved`

### `_resolve_value` - L101-L124

```python
_resolve_value(key: str, value: str) -> str
```

Expand references, then refuse a bare key name typed by mistake.

Observed calls (lexical order): `str`, `str(value or '').strip`, `ENV_REFERENCE_PATTERN.search`, `ValueError`, `ZOWE_ERROR_MESSAGES['circular_reference'].format`, `_expand_once`, `_expand_once(key, resolved).strip`, `BARE_ENV_KEY_PATTERN.match`, `ZOWE_ERROR_MESSAGES['bare_key_reference'].format`.

Control points:

- L104: `if not resolved`
- L108: `while ENV_REFERENCE_PATTERN.search(resolved)`
- L110: `if depth > ENV_REFERENCE_MAX_DEPTH`
- L118: `if BARE_ENV_KEY_PATTERN.match(resolved)`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['circular_reference'].format(key=key, depth=ENV_REFERENCE_MAX_DEPTH))`; `ValueError(ZOWE_ERROR_MESSAGES['bare_key_reference'].format(key=key, value=resolved))`.

### `_lookup` - L127-L130

```python
_lookup(key: str) -> str
```

Raw value for one key, with references expanded.

Observed calls (lexical order): `load_dotenv_once`, `_resolve_value`, `os.getenv`.

### `setting` - L136-L146

```python
setting(artifact: str, name: str, default: str='') -> str
```

Artifact value, then shared value, then default.

Observed calls (lexical order): `ARTIFACT_KEY_TEMPLATE.format`, `_lookup`, `SHARED_KEY_TEMPLATE.format`.

Control points:

- L139: `if scoped`
- L143: `if shared`

### `setting_int` - L149-L154

```python
setting_int(artifact: str, name: str, default: int) -> int
```

Observed calls (lexical order): `setting`, `int`.

### `setting_bool` - L157-L163

```python
setting_bool(artifact: str, name: str, default: bool) -> bool
```

Observed calls (lexical order): `setting`, `setting(artifact, name).lower`.

Control points:

- L159: `if raw in ('true', '1', 'yes', 'y', 'on')`
- L161: `if raw in ('false', '0', 'no', 'n', 'off')`

### `raw_setting` - L166-L168

```python
raw_setting(key: str, default: str='') -> str
```

A plain key with no artifact scoping, for example ZOWE_LANDING_ROOT.

Observed calls (lexical order): `_lookup`.

### `setting_source` - L171-L181

```python
setting_source(artifact: str, name: str) -> str
```

Which key supplied the value. Used by the show command only.

Observed calls (lexical order): `ARTIFACT_KEY_TEMPLATE.format`, `_lookup`, `SHARED_KEY_TEMPLATE.format`.

Control points:

- L174: `if _lookup(scoped_key)`
- L178: `if _lookup(shared_key)`

### `mask` - L184-L188

```python
mask(name: str, value: str) -> str
```

Never echo a password into a console line or a diagnostic.

Control points:

- L186: `if not value`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
