# `converter/postprocess/update_metadata_models.py`

Source: [converter/postprocess/update_metadata_models.py](../../../../converter/postprocess/update_metadata_models.py) | 128 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `a336b57b82ec18be47598a93da7ea9e734b63af1716a57cb50cb05359f47b0a5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import Any, Optional
```

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)
- [converter/postprocess/restart_role/restart_role_factory.py](restart_role/restart_role_factory.md)
- [converter/postprocess/update_cobol_file_resolver.py](update_cobol_file_resolver.md)
- [converter/postprocess/update_copybook_resolver.py](update_copybook_resolver.md)
- [converter/postprocess/update_restart_dclgen_matcher.py](update_restart_dclgen_matcher.md)
- [converter/postprocess/update_restart_dclgen_resolver.py](update_restart_dclgen_resolver.md)
- [converter/postprocess/update_restart_dclgen_role_builder.py](update_restart_dclgen_role_builder.md)
- [converter/postprocess/update_restart_dclgen_row_mapper.py](update_restart_dclgen_row_mapper.md)
- [converter/postprocess/update_restart_fallback_dclgen.py](update_restart_fallback_dclgen.md)

## Symbol contracts and control points

### `value` - L8-L28

```python
value(item: Any, *names: str, default: Any=None) -> Any
```

Observed calls (lexical order): `isinstance`, `item.get`, `hasattr`, `getattr`.

Control points:

- L13: `if item is None`
- L16: `if isinstance(item, dict)`
- L17: `for name in names`
- L19: `if item_value not in (None, '')`
- L22: `for name in names`
- L23: `if hasattr(item, name)`
- L25: `if item_value not in (None, '')`

### `upper` - L31-L32

```python
upper(value: Any) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`.

### `norm_name` - L35-L39

```python
norm_name(value: Any) -> str
```

Observed calls (lexical order): `upper`, `text.replace`, `re.sub`.

### `sql_name` - L42-L47

```python
sql_name(value: Any) -> str
```

Observed calls (lexical order): `upper`, `text.replace`, `re.sub`, `text.strip`.

### `compact` - L50-L51

```python
compact(value: Any) -> str
```

Observed calls (lexical order): `re.sub`, `upper`.

### `include_from_label` - L54-L60

```python
include_from_label(source_label: str) -> str
```

Observed calls (lexical order): `source_label.replace`, `source_label.replace('\\', '/').split`, `clean.split`, `norm_name`.

Control points:

- L55: `if not source_label`

### `CobolFileInfo` - L64-L69

```python
class CobolFileInfo()
```

Declared class/data-model fields:

```python
name: str
assignment: str = ''
fd_record: str = ''
record_length: int = 0
read_target: str = ''
```

### `CopybookRecordInfo` - L73-L78

```python
class CopybookRecordInfo()
```

Declared class/data-model fields:

```python
include_name: str
record_name: str
source_label: str = ''
fields: set[str] = field(default_factory=set)
estimated_length: int = 0
```

### `DclgenRoleInfo` - L82-L99

```python
class DclgenRoleInfo()
```

Declared class/data-model fields:

```python
table_name: str
include_name: str
host_record_name: str
program_column: str
phase_column: str
date_column: str
status_column: str
retention_column: str
payload_column: str
program_field: str
phase_field: str
date_field: str
status_field: str
retention_field: str
payload_group: str
payload_len_field: str
payload_text_field: str
```

### `UpdateProgramContext` - L103-L128

```python
class UpdateProgramContext()
```

Declared class/data-model fields:

```python
input_file: CobolFileInfo
input_copybook: CopybookRecordInfo
restart_dclgen: Optional[DclgenRoleInfo]
program_id: str
legacy_eof_switch: str = ''
source_program_text: str = ''
diagnostics: list[str] = field(default_factory=list)
```

### `UpdateProgramContext.input_record_name` - L113-L114

```python
input_record_name(self) -> str
```

### `UpdateProgramContext.copybook_include_name` - L117-L118

```python
copybook_include_name(self) -> str
```

### `UpdateProgramContext.record_length` - L121-L128

```python
record_length(self) -> int
```

Control points:

- L122: `if self.input_file.record_length`
- L125: `if self.input_copybook.estimated_length`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
