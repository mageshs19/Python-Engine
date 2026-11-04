# `converter/postprocess/restart_logic_generator.py`

Source: [converter/postprocess/restart_logic_generator.py](../../../../converter/postprocess/restart_logic_generator.py) | 368 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `f8a807714701aa499fcbc7036ffc653dd9b9da222ce678e8ef4492508b8cbb74`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Abstract base class for restart logic generation.

## Import declarations

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from converter.postprocess.restart_config import RestartConfig
```

## Local dependency notes

- [converter/postprocess/restart_config.py](restart_config.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/cobol_restart_logic_generator.py](cobol_restart_logic_generator.md)
- [converter/postprocess/restart_logic_pipeline.py](restart_logic_pipeline.md)

## Symbol contracts and control points

### `RestartLogicGenerator` - L22-L368

```python
class RestartLogicGenerator(ABC)
```

Abstract base class for generating restart-aware UPDATE program logic.

### `RestartLogicGenerator.__init__` - L49-L60

```python
__init__(self, config: RestartConfig) -> None
```

Initialize generator with restart configuration.

Observed calls (lexical order): `self._validate_config`.

### `RestartLogicGenerator._validate_config` - L62-L71

```python
_validate_config(self) -> None
```

Validate that config has all required fields.

Observed calls (lexical order): `getattr`, `ValueError`.

Control points:

- L69: `for field in required_fields`
- L70: `if not getattr(self.config, field, None)`

Explicit raises: `ValueError(f'RestartConfig missing required field: {field}')`.

### `RestartLogicGenerator.generate_restart_control_paragraph` - L74-L104

```python
generate_restart_control_paragraph(self) -> str
```

Generate 700-RESTART-CONTROL paragraph.

### `RestartLogicGenerator.generate_select_paragraph` - L107-L135

```python
generate_select_paragraph(self) -> str
```

Generate 700-SELECT-DZ01RSTV paragraph.

### `RestartLogicGenerator.generate_restart_found_paragraph` - L138-L171

```python
generate_restart_found_paragraph(self) -> str
```

Generate 710-JOB-IS-RESTART paragraph.

### `RestartLogicGenerator.generate_write_restart_paragraph` - L174-L203

```python
generate_write_restart_paragraph(self) -> str
```

Generate 720-WRITE-RESTART-REC paragraph.

### `RestartLogicGenerator.generate_commit_paragraph` - L206-L235

```python
generate_commit_paragraph(self) -> str
```

Generate 800-PROCESS-COMMIT paragraph.

### `RestartLogicGenerator.generate_update_paragraph` - L238-L266

```python
generate_update_paragraph(self) -> str
```

Generate 700-UPDATE-DZ01RSTV paragraph.

### `RestartLogicGenerator.generate_insert_paragraph` - L269-L293

```python
generate_insert_paragraph(self) -> str
```

Generate 700-INSERT-DZ01RSTV paragraph.

### `RestartLogicGenerator.generate_abend_paragraph` - L296-L315

```python
generate_abend_paragraph(self) -> str
```

Generate 810000-CALL-USERABEN paragraph.

### `RestartLogicGenerator.generate_all_paragraphs` - L317-L347

```python
generate_all_paragraphs(self) -> dict[str, str]
```

Generate all restart paragraphs.

Observed calls (lexical order): `self.generate_restart_control_paragraph`, `self.generate_select_paragraph`, `self.generate_restart_found_paragraph`, `self.generate_write_restart_paragraph`, `self.generate_commit_paragraph`, `self.generate_update_paragraph`, `self.generate_insert_paragraph`, `self.generate_abend_paragraph`.

### `RestartLogicGenerator.get_paragraph_names` - L349-L368

```python
get_paragraph_names(self) -> dict[str, str]
```

Get mapping of paragraph logical names to actual paragraph names.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
