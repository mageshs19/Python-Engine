# `converter/postprocess/update_copybook_resolver.py`

Source: [converter/postprocess/update_copybook_resolver.py](../../../../converter/postprocess/update_copybook_resolver.py) | 169 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `0cd1891b5fba1ae7ee9a97a060f1527a3f3a26182752fa08b111b972c47789db`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from typing import Any
from converter.postprocess.update_metadata_models import CobolFileInfo, CopybookRecordInfo, include_from_label, norm_name, upper, value
from patterns.dynamic_metadata_patterns import PIC_LENGTH_RE
```

## Local dependency notes

- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)
- [patterns/dynamic_metadata_patterns.py](../../patterns/dynamic_metadata_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)

## Symbol contracts and control points

### `UpdateCopybookResolver` - L17-L169

```python
class UpdateCopybookResolver()
```

### `UpdateCopybookResolver.build_copybook_records` - L18-L75

```python
build_copybook_records(self, copybook_fields: list[Any]) -> list[CopybookRecordInfo]
```

Observed calls (lexical order): `self._field_level`, `norm_name`, `value`, `upper`, `include_from_label`, `CopybookRecordInfo`, `records.append`, `current.fields.add`, `int`, `self.estimate_pic_length`.

Control points:

- L25: `for item in copybook_fields`
- L38: `if not name`
- L52: `if level == 1 or current is None`

### `UpdateCopybookResolver.choose_copybook` - L77-L132

```python
choose_copybook(self, *, input_file: CobolFileInfo, copybooks: list[CopybookRecordInfo], copy_statements: set[str], source_refs: set[str]) -> CopybookRecordInfo
```

Observed calls (lexical order): `ValueError`, `norm_name`, `copybook.fields.intersection`, `len`, `scored.append`, `scored.sort`.

Control points:

- L85: `if not copybooks`
- L93: `for copybook in copybooks`
- L96: `if read_target and read_target in {copybook.record_name, copybook.include_name}`
- L102: `if fd_record and fd_record in {copybook.record_name, copybook.include_name}`
- L108: `if copybook.include_name in copy_statements`
- L111: `if copybook.record_name in copy_statements`
- L114: `if input_file.record_length and copybook.estimated_length == input_file.record_length`
- L126: `if scored[0][0] <= 0 and len(copybooks) > 1`

Explicit raises: `ValueError('No copybook fields were parsed from uploaded copybook input.')`; `ValueError('Unable to resolve input copybook safely. Multiple copybooks exist and no reliable match was found.')`.

### `UpdateCopybookResolver._field_level` - L134-L149

```python
_field_level(self, item: Any) -> int
```

Observed calls (lexical order): `value`, `int`.

### `UpdateCopybookResolver.estimate_pic_length` - L151-L169

```python
estimate_pic_length(self, pic: Any) -> int
```

Observed calls (lexical order): `upper`, `text.replace`, `text.replace(' ', '').replace`, `PIC_LENGTH_RE.finditer`, `int`, `match.group`.

Control points:

- L157: `if not text`
- L163: `for match in PIC_LENGTH_RE.finditer(text)`
- L166: `if 'COMP-3' in text or 'COMP_3' in text`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
