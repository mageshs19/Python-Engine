# `converter/infrastructure/runtime_context.py`

Source: [converter/infrastructure/runtime_context.py](../../../../converter/infrastructure/runtime_context.py) | 78 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `1fd9b3e78fafe54c8ff0eb7f9f1850769fa88ea26a1ac1d4f9789643612893ca`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from dataclasses import dataclass, field
from pathlib import Path
```

## Symbol contracts and control points

### `RuntimeContext` - L6-L78

```python
class RuntimeContext()
```

Runtime context for local executions.

Declared class/data-model fields:

```python
project_root: Path
input_dir: Path
output_dir: Path
sheet_mapping_path: Path | None = None
dclgen_paths: list[Path] = field(default_factory=list)
copybook_paths: list[Path] = field(default_factory=list)
idms_cobol_source_path: Path | None = None
target_program_id: str = ''
auto_fix_pic_length_mismatches: bool = False
```

### `RuntimeContext.ensure_output_dir` - L25-L31

```python
ensure_output_dir(self) -> None
```

Observed calls (lexical order): `self.output_dir.mkdir`.

### `RuntimeContext.validate_required_files` - L33-L67

```python
validate_required_files(self) -> None
```

Observed calls (lexical order): `ValueError`, `self._validate_file_exists`, `enumerate`, `self.ensure_output_dir`.

Control points:

- L36: `if self.sheet_mapping_path is None`
- L39: `if self.idms_cobol_source_path is None`
- L52: `if not self.dclgen_paths`
- L55: `for (index, dclgen_path) in enumerate(self.dclgen_paths, start=1)`
- L61: `for (index, copybook_path) in enumerate(self.copybook_paths, start=1)`

Explicit raises: `ValueError('Sheet Mapping path is required.')`; `ValueError('IDMS COBOL source path is required.')`; `ValueError('At least one DCLGEN file path is required.')`.

### `RuntimeContext._validate_file_exists` - L69-L78

```python
_validate_file_exists(self, file_path: Path, label: str) -> None
```

Observed calls (lexical order): `file_path.exists`, `FileNotFoundError`, `file_path.is_file`.

Control points:

- L74: `if not file_path.exists()`
- L77: `if not file_path.is_file()`

Explicit raises: `FileNotFoundError(f'{label} file not found: {file_path}')`; `FileNotFoundError(f'{label} path is not a file: {file_path}')`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
