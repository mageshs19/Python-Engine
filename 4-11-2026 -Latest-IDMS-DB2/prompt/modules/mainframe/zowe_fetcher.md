# `mainframe/zowe_fetcher.py`

Source: [mainframe/zowe_fetcher.py](../../../mainframe/zowe_fetcher.py) | 243 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `47f465bb278281a0c93647037ae5b9c0ff398775303d5d7833778123021dbe15`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Program-driven fetch.

## Module-level bindings

`logger` (L54), `_LANDING` (L56)

## Import declarations

```python
from __future__ import annotations
import logging
from pathlib import Path
from mainframe.zowe_libraries import LibrarySearch, application_code, libraries_for
from mainframe.zowe_resolver import ProgramDependencies, resolve_dependencies
from mainframe.zowe_rules import ARTIFACT_COPYBOOK, ARTIFACT_DCLGEN, ARTIFACT_EXTENSIONS, ARTIFACT_LABELS, ARTIFACT_PROGRAM, ARTIFACT_SUBSCHEMA, DIAG_APPLICATION_TEMPLATE, DIAG_DEPENDENCIES_TEMPLATE, DIAG_DERIVED_DCLGEN_TEMPLATE, DIAG_END_FETCH, DIAG_FOUND_TEMPLATE, DIAG_LIBRARY_ORDER_TEMPLATE, DIAG_MAPPING_LOCAL, DIAG_NOT_FOUND_TEMPLATE, DIAG_PROGRAM_LIST_TEMPLATE, DIAG_START_FETCH, DIAG_SUBSCHEMA_DETECTED_TEMPLATE, DIAG_TOTAL_TEMPLATE, TEXT_ENCODING, ZOWE_ERROR_MESSAGES, ZOWE_WARNING_MESSAGES
from mainframe.zowe_workspace import copybook_dir, dclgen_dir, ensure_workspace, program_dir, subschema_dir
from mainframe.zowe_resolver import dclgen_member_for
from mainframe.zowe_rules import DIAG_ELEMENTS_TEMPLATE, DIAG_NO_ELEMENTS_TEMPLATE
from mainframe.zowe_programs import selected_programs
from mainframe.zowe_subschema import element_records_for
```

## Local dependency notes

- [mainframe/zowe_libraries.py](zowe_libraries.md)
- [mainframe/zowe_programs.py](zowe_programs.md)
- [mainframe/zowe_resolver.py](zowe_resolver.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_subschema.py](zowe_subschema.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/__init__.py](__init__.md)
- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)

## Symbol contracts and control points

### `ZoweFetcher` - L64-L239

```python
class ZoweFetcher()
```

### `ZoweFetcher.__init__` - L65-L72

```python
__init__(self, programs: list[str] | None=None) -> None
```

Observed calls (lexical order): `selected_programs`.

### `ZoweFetcher._search` - L75-L84

```python
_search(self, artifact: str) -> LibrarySearch
```

Observed calls (lexical order): `LibrarySearch`, `self.diagnostics.append`, `DIAG_LIBRARY_ORDER_TEMPLATE.format`, `', '.join`.

Control points:

- L76: `if artifact not in self._searches`

### `ZoweFetcher._save` - L86-L100

```python
_save(self, artifact: str, member: str, dataset: str, content: bytes) -> Path
```

Observed calls (lexical order): `_LANDING[artifact]`, `folder.mkdir`, `target.write_bytes`, `self.saved.setdefault`, `self.saved.setdefault(ARTIFACT_LABELS[artifact], []).append`, `self.diagnostics.append`, `DIAG_FOUND_TEMPLATE.format`.

### `ZoweFetcher._fetch_member` - L102-L127

```python
_fetch_member(self, artifact: str, member: str, mandatory: bool) -> bool
```

Observed calls (lexical order): `self._search`, `search.download`, `', '.join`, `self.diagnostics.append`, `DIAG_NOT_FOUND_TEMPLATE.format`, `message.format`, `ValueError`, `self.warnings.append`, `self._save`.

Control points:

- L106: `if not dataset`
- L121: `if mandatory`

Explicit raises: `ValueError(formatted)`.

### `ZoweFetcher._fetch_program` - L130-L152

```python
_fetch_program(self, program: str) -> ProgramDependencies
```

Observed calls (lexical order): `self._search`, `search.download`, `ValueError`, `ZOWE_ERROR_MESSAGES['program_not_found'].format`, `', '.join`, `self._save`, `path.read_text`, `resolve_dependencies`, `self.diagnostics.append`, `DIAG_DEPENDENCIES_TEMPLATE.format`, `len`.

Control points:

- L133: `if not dataset`

Explicit raises: `ValueError(ZOWE_ERROR_MESSAGES['program_not_found'].format(member=program, libraries=', '.join(search.libraries)))`.

### `ZoweFetcher._fetch_dependencies` - L154-L182

```python
_fetch_dependencies(self, deps: ProgramDependencies) -> None
```

Observed calls (lexical order): `self._fetch_member`, `self.diagnostics.append`, `DIAG_SUBSCHEMA_DETECTED_TEMPLATE.format`, `self.saved.get`, `self.warnings.append`, `ZOWE_WARNING_MESSAGES['subschema_not_detected'].format`, `self._dclgen_members`, `DIAG_DERIVED_DCLGEN_TEMPLATE.format`.

Control points:

- L155: `for member in deps.copybooks`
- L159: `if deps.subschema`
- L165: `if self._fetch_member(ARTIFACT_SUBSCHEMA, deps.subschema, False)`
- L175: `for record in deps.records`
- L176: `for member in self._dclgen_members(record, subschema_path)`

### `ZoweFetcher._dclgen_members` - L184-L208

```python
_dclgen_members(self, record: str, subschema_path) -> list[str]
```

Observed calls (lexical order): `element_records_for`, `self.diagnostics.append`, `DIAG_ELEMENTS_TEMPLATE.format`, `', '.join`, `DIAG_NO_ELEMENTS_TEMPLATE.format`, `dclgen_member_for`, `members.append`.

Control points:

- L188: `if subschema_path is not None`
- L191: `if elements`
- L204: `for element in elements`
- L206: `if member and member not in members`

### `ZoweFetcher.fetch_all` - L211-L239

```python
fetch_all(self) -> dict
```

Observed calls (lexical order): `ensure_workspace`, `self.diagnostics.append`, `DIAG_APPLICATION_TEMPLATE.format`, `application_code`, `DIAG_PROGRAM_LIST_TEMPLATE.format`, `', '.join`, `len`, `self._fetch_program`, `self._fetch_dependencies`, `self.saved.values`, `sum`, `DIAG_TOTAL_TEMPLATE.format`.

Control points:

- L224: `for program in self.programs`

### `fetch_zowe_inputs` - L242-L243

```python
fetch_zowe_inputs(source_text: str='') -> dict
```

Observed calls (lexical order): `ZoweFetcher`, `ZoweFetcher().fetch_all`.

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
