# `mainframe/zowe_programs.py`

Source: [mainframe/zowe_programs.py](../../../mainframe/zowe_programs.py) | 54 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `6ff22458d28740da6cc5d91587340a3f9c0ce7df8649f6be8852f7e7bd824c5b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The program array that drives the batch.

## Module-level bindings

`PACKAGE_DIR` (L19)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from mainframe.zowe_env import setting
from mainframe.zowe_rules import DEFAULT_PROGRAM_LIST_FILE, LIBRARY_SEPARATOR, NAME_PROGRAM_LIST_FILE, NAME_PROGRAMS, PROGRAM_LIST_COMMENT, ZOWE_ERROR_MESSAGES
```

## Local dependency notes

- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_rules.py](zowe_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/__init__.py](__init__.md)
- [mainframe/zowe_commands.py](zowe_commands.md)
- [mainframe/zowe_fetcher.py](zowe_fetcher.md)

## Symbol contracts and control points

### `program_list_file` - L22-L25

```python
program_list_file() -> Path
```

Observed calls (lexical order): `setting`, `Path`, `candidate.is_absolute`.

### `selected_programs` - L28-L38

```python
selected_programs() -> list[str]
```

Inline ZOWE_PROGRAMS wins; otherwise the list file is read.

Observed calls (lexical order): `setting`, `_clean`, `inline.split`, `program_list_file`, `path.is_file`, `path.read_text`, `path.read_text(encoding='utf-8').splitlines`, `ValueError`, `ZOWE_ERROR_MESSAGES['no_programs'].format`.

Control points:

- L31: `if inline`
- L35: `if path.is_file()`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['no_programs'].format(file=path))`.

### `_clean` - L41-L54

```python
_clean(values) -> list[str]
```

Observed calls (lexical order): `str`, `str(raw or '').strip`, `line.startswith`, `line.upper`, `out.append`, `ValueError`, `ZOWE_ERROR_MESSAGES['no_programs'].format`, `program_list_file`.

Control points:

- L43: `for raw in values`
- L45: `if not line or line.startswith(PROGRAM_LIST_COMMENT)`
- L48: `if name not in out`
- L50: `if not out`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['no_programs'].format(file=program_list_file()))`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
