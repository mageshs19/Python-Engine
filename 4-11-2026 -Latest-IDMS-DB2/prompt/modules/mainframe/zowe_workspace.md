# `mainframe/zowe_workspace.py`

Source: [mainframe/zowe_workspace.py](../../../mainframe/zowe_workspace.py) | 95 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `a5d7e3f5228848952a9fa16875cc3f4b409f4c89657c56dd02bb4247b20285a6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Workspace layout. Every run artifact lives under zowe/workspace.

## Module-level bindings

`PACKAGE_DIR` (L21), `PROJECT_ROOT` (L22)

## Import declarations

```python
from __future__ import annotations
import shutil
from pathlib import Path
from mainframe.zowe_env import raw_setting
from mainframe.zowe_rules import WORKSPACE_DIR_NAME, WORKSPACE_ROOT_KEY, WORKSPACE_SUBFOLDERS
```

## Local dependency notes

- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_rules.py](zowe_rules.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/__init__.py](__init__.md)
- [mainframe/zowe_commands.py](zowe_commands.md)
- [mainframe/zowe_fetcher.py](zowe_fetcher.md)
- [mainframe/zowe_manifest.py](zowe_manifest.md)
- [mainframe/zowe_pipeline.py](zowe_pipeline.md)
- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)
- [mainframe/zowe_semantic_release_gate.py](zowe_semantic_release_gate.md)
- [mainframe/zowe_settings.py](zowe_settings.md)
- [mainframe/zowe_steps.py](zowe_steps.md)

## Symbol contracts and control points

### `workspace_root` - L25-L30

```python
workspace_root() -> Path
```

Override with ZOWE_WORKSPACE_ROOT, else zowe/workspace.

Observed calls (lexical order): `raw_setting`, `Path`.

Control points:

- L28: `if configured`

### `mapping_dir` - L34-L35

```python
mapping_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `program_dir` - L38-L39

```python
program_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `copybook_dir` - L42-L43

```python
copybook_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `dclgen_dir` - L46-L47

```python
dclgen_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `subschema_dir` - L50-L51

```python
subschema_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `output_dir` - L54-L55

```python
output_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `review_dir` - L58-L59

```python
review_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `logs_dir` - L62-L63

```python
logs_dir() -> Path
```

Observed calls (lexical order): `workspace_root`.

### `ensure_workspace` - L67-L78

```python
ensure_workspace() -> list[Path]
```

Create every folder. Safe to call repeatedly.

Observed calls (lexical order): `workspace_root`, `folder.exists`, `created.append`, `folder.mkdir`.

Control points:

- L72: `for sub in WORKSPACE_SUBFOLDERS`
- L74: `if not folder.exists()`

### `clean_generated` - L81-L89

```python
clean_generated() -> list[Path]
```

Remove Output and Review. Never touches inputs.

Observed calls (lexical order): `output_dir`, `review_dir`, `folder.exists`, `shutil.rmtree`, `removed.append`, `folder.mkdir`.

Control points:

- L84: `for folder in (output_dir(), review_dir())`
- L85: `if folder.exists()`

### `count_files` - L92-L95

```python
count_files(folder: Path, pattern: str='*') -> int
```

Observed calls (lexical order): `folder.exists`, `folder.glob`, `path.is_file`, `sum`.

Control points:

- L93: `if not folder.exists()`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
