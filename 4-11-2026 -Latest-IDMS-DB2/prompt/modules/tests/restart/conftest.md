# `tests/restart/conftest.py`

Source: [tests/restart/conftest.py](../../../../tests/restart/conftest.py) | 167 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `030b5b2a578073d4d6859f90e93a54d57bcfbb70beb442f7aeee92e9563a2930`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared fixtures for the restart module tests.

## Module-level bindings

`SEQ` (L15), `IND` (L16), `BODY_END` (L17), `INDICATORS` (L22), `COMMENT_INDICATORS` (L25)

## Import declarations

```python
from __future__ import annotations
import pytest
from catalogs.restart_paragraph_catalog import production_restart_role
from converter.generators.restart.restart_config import RestartConfig, RestartProgramNames
```

## Local dependency notes

- [catalogs/restart_paragraph_catalog.py](../../catalogs/restart_paragraph_catalog.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)

## Symbol contracts and control points

### `FixedFormatLineUtils` - L28-L84

```python
class FixedFormatLineUtils()
```

Minimal stand-in for the shared retrieval line utility.

### `FixedFormatLineUtils.logical` - L59-L72

```python
logical(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:SEQ].isdigit`, `text.strip`, `FixedFormatLineUtils._is_sequence_only`.

Control points:

- L62: `if len(text) > IND and text[:SEQ].isdigit() and (text[SEQ] in INDICATORS)`
- L67: `if text[SEQ] in COMMENT_INDICATORS`

### `FixedFormatLineUtils.is_comment` - L75-L76

```python
is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').lstrip`, `str(line or '').lstrip().startswith`.

### `FixedFormatLineUtils._is_sequence_only` - L79-L84

```python
_is_sequence_only(body: str) -> bool
```

Exactly SEQ digits, with an optional period, is not COBOL.

Observed calls (lexical order): `str`, `str(body or '').strip`, `candidate.endswith`, `candidate.isdigit`, `len`.

Control points:

- L82: `if candidate.endswith('.')`

### `line_utils` - L88-L89

```python
line_utils()
```

Observed calls (lexical order): `FixedFormatLineUtils`.

### `role` - L93-L94

```python
role()
```

Observed calls (lexical order): `production_restart_role`.

### `complete_names` - L98-L118

```python
complete_names()
```

Observed calls (lexical order): `RestartProgramNames`.

### `config` - L122-L123

```python
config(role, complete_names)
```

Observed calls (lexical order): `RestartConfig.build`.

### `source_lines` - L127-L167

```python
source_lines()
```

A minimal update program in fixed format.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
