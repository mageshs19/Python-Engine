# `mainframe/zowe_commands.py`

Source: [mainframe/zowe_commands.py](../../../mainframe/zowe_commands.py) | 144 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `b4157839d5eaf1ccb7d04d9b6a960359268369c0037cd39ccc97e0dca2f99130`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Non-step commands: init, show, plan, clean.

## Module-level bindings

`NOT_FOUND` (L41), `COBOL_GLOB` (L42)

## Import declarations

```python
from __future__ import annotations
from mainframe.zowe_console import bullets, credentials, header
from mainframe.zowe_libraries import LibrarySearch
from mainframe.zowe_programs import selected_programs
from mainframe.zowe_resolver import resolve_dependencies
from mainframe.zowe_rules import ARTIFACT_COPYBOOK, ARTIFACT_DCLGEN, ARTIFACT_PROGRAM, ARTIFACT_SUBSCHEMA, CLEAN_REMOVED_TEMPLATE, EXIT_NOTHING, EXIT_OK, PIPELINE_TITLE, TEXT_ENCODING, WORKSPACE_CREATED_TEMPLATE, WORKSPACE_READY_TEMPLATE, ZOWE_RULES
from mainframe.zowe_settings import application_code, build_output_profile, build_profiles
from mainframe.zowe_workspace import clean_generated, count_files, ensure_workspace, mapping_dir, output_dir, program_dir, review_dir, workspace_root
```

## Local dependency notes

- [mainframe/zowe_console.py](zowe_console.md)
- [mainframe/zowe_libraries.py](zowe_libraries.md)
- [mainframe/zowe_programs.py](zowe_programs.md)
- [mainframe/zowe_resolver.py](zowe_resolver.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_settings.py](zowe_settings.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_pipeline.py](zowe_pipeline.md)

## Symbol contracts and control points

### `command_init` - L45-L50

```python
command_init() -> int
```

Observed calls (lexical order): `header`, `ensure_workspace`, `WORKSPACE_CREATED_TEMPLATE.format`, `print`, `WORKSPACE_READY_TEMPLATE.format`, `workspace_root`.

Control points:

- L47: `for folder in ensure_workspace()`

### `command_show` - L53-L79

```python
command_show() -> int
```

Observed calls (lexical order): `header`, `print`, `workspace_root`, `application_code`, `count_files`, `mapping_dir`, `program_dir`, `output_dir`, `review_dir`, `build_profiles`, `credentials`, `', '.join`, `build_output_profile`, `bullets`.

Control points:

- L63: `for profile in build_profiles()`

### `command_clean` - L82-L86

```python
command_clean() -> int
```

Observed calls (lexical order): `header`, `clean_generated`, `CLEAN_REMOVED_TEMPLATE.format`, `print`.

Control points:

- L84: `for folder in clean_generated()`

### `_report_one` - L89-L93

```python
_report_one(label: str, member: str, search: LibrarySearch) -> int
```

Print one resolution line. Returns 1 when unresolved.

Observed calls (lexical order): `search.locate`, `print`.

### `command_plan` - L96-L144

```python
command_plan() -> int
```

Resolve every dependency WITHOUT downloading them.

Observed calls (lexical order): `ensure_workspace`, `header`, `application_code`, `print`, `selected_programs`, `', '.join`, `LibrarySearch`, `program_search.download`, `resolve_dependencies`, `content.decode`, `_report_one`, `zip`.

Control points:

- L115: `for program in programs`
- L118: `if not dataset`
- L128: `for member in deps.copybooks`
- L131: `for (record, member) in zip(deps.records, deps.dclgens)`
- L132: `if not member`
- L137: `if deps.subschema`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
