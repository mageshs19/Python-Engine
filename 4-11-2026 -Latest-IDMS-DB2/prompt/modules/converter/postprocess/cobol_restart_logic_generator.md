# `converter/postprocess/cobol_restart_logic_generator.py`

Source: [converter/postprocess/cobol_restart_logic_generator.py](../../../../converter/postprocess/cobol_restart_logic_generator.py) | 349 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `46a79b60249b132ce170af5e77b630274424dcc489e1c3c74541104c96e6ad0d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Concrete COBOL implementation of RestartLogicGenerator.

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.restart_config import RestartConfig
from converter.postprocess.restart_logic_generator import RestartLogicGenerator
```

## Local dependency notes

- [converter/postprocess/restart_config.py](restart_config.md)
- [converter/postprocess/restart_logic_generator.py](restart_logic_generator.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `CobolRestartLogicGenerator` - L21-L349

```python
class CobolRestartLogicGenerator(RestartLogicGenerator)
```

Concrete implementation of restart logic generator for COBOL.

### `CobolRestartLogicGenerator.__init__` - L36-L38

```python
__init__(self, config: RestartConfig) -> None
```

Initialize with restart configuration.

Observed calls (lexical order): `super`, `super().__init__`.

### `CobolRestartLogicGenerator.generate_restart_control_paragraph` - L40-L66

```python
generate_restart_control_paragraph(self) -> str
```

Generate 700-RESTART-CONTROL - Entry point.

### `CobolRestartLogicGenerator.generate_select_paragraph` - L68-L118

```python
generate_select_paragraph(self) -> str
```

Generate 700-SELECT-DZ01RSTV - Query checkpoint table.

### `CobolRestartLogicGenerator.generate_restart_found_paragraph` - L120-L151

```python
generate_restart_found_paragraph(self) -> str
```

Generate 710-JOB-IS-RESTART - Resume or mark complete.

### `CobolRestartLogicGenerator.generate_write_restart_paragraph` - L153-L187

```python
generate_write_restart_paragraph(self) -> str
```

Generate 720-WRITE-RESTART-REC - Create new checkpoint.

### `CobolRestartLogicGenerator.generate_commit_paragraph` - L189-L255

```python
generate_commit_paragraph(self) -> str
```

Generate 800-PROCESS-COMMIT - Periodic checkpoint save.

### `CobolRestartLogicGenerator.generate_update_paragraph` - L257-L307

```python
generate_update_paragraph(self) -> str
```

Generate 700-UPDATE-DZ01RSTV - Update checkpoint.

### `CobolRestartLogicGenerator.generate_insert_paragraph` - L309-L339

```python
generate_insert_paragraph(self) -> str
```

Generate 700-INSERT-DZ01RSTV - Insert new checkpoint.

### `CobolRestartLogicGenerator.generate_abend_paragraph` - L341-L349

```python
generate_abend_paragraph(self) -> str
```

Generate 810000-CALL-USERABEN - Mark complete and exit.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
