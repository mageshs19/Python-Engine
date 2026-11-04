# `mainframe/zowe_manifest.py`

Source: [mainframe/zowe_manifest.py](../../../mainframe/zowe_manifest.py) | 120 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `f3706fad00da1a4597e91de256fff347528e9e7c0f9f9e81506ea4ba9b70835a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Per-execution program manifest for monitoring.

## Module-level bindings

`PROGRAM_GLOB` (L39), `TEXT_ENCODING` (L40), `__all__` (L117)

## Import declarations

```python
from __future__ import annotations
from datetime import datetime
from pathlib import Path
from converter.parsers.cobol_parser import CobolParser
from converter.services.name_derivation_resolver import NameDerivationResolver
from mainframe.zowe_resolver import resolve_dependencies
from mainframe.zowe_rules import MANIFEST_CELL_SEPARATOR, MANIFEST_EMPTY_CELL, MANIFEST_FILE_NAME_TEMPLATE, MANIFEST_HEADER, MANIFEST_ROW_TEMPLATE, MANIFEST_TIMESTAMP_FORMAT
from mainframe.zowe_workspace import program_dir, review_dir
```

## Local dependency notes

- [converter/parsers/cobol_parser.py](../converter/parsers/cobol_parser.md)
- [converter/services/name_derivation_resolver.py](../converter/services/name_derivation_resolver.md)
- [mainframe/zowe_resolver.py](zowe_resolver.md)
- [mainframe/zowe_rules.py](zowe_rules.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)

## Symbol contracts and control points

### `_cell` - L43-L52

```python
_cell(values) -> str
```

Render a list (or scalar) cell, using \[\] for anything empty.

Observed calls (lexical order): `isinstance`, `values.strip`, `str`, `str(v).strip`, `MANIFEST_CELL_SEPARATOR.join`.

Control points:

- L45: `if isinstance(values, str)`
- L50: `if not names`

### `_derive_db2_program_id` - L55-L59

```python
_derive_db2_program_id(source_text: str) -> str
```

Observed calls (lexical order): `CobolParser`, `CobolParser().program_id`, `NameDerivationResolver`, `NameDerivationResolver().derive`.

Control points:

- L57: `if not source_id`

### `_program_sources` - L62-L66

```python
_program_sources() -> list[Path]
```

Observed calls (lexical order): `program_dir`, `folder.is_dir`, `folder.glob`, `p.is_file`, `sorted`.

Control points:

- L64: `if not folder.is_dir()`

### `build_manifest_rows` - L69-L90

```python
build_manifest_rows() -> list[str]
```

Return one formatted manifest row per readable program source.

Observed calls (lexical order): `_program_sources`, `source_path.read_text`, `resolve_dependencies`, `rows.append`, `MANIFEST_ROW_TEMPLATE.format`, `source_path.stem.upper`, `_cell`, `_derive_db2_program_id`.

Control points:

- L72: `for source_path in _program_sources()`

### `write_execution_manifest` - L93-L114

```python
write_execution_manifest() -> tuple[Path | None, int]
```

Write the per-execution manifest to the Review folder.

Observed calls (lexical order): `build_manifest_rows`, `review_dir`, `review_folder.mkdir`, `datetime.now`, `datetime.now().strftime`, `MANIFEST_FILE_NAME_TEMPLATE.format`, `'\n'.join`, `manifest_path.write_text`, `len`.

Control points:

- L100: `if not rows`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
