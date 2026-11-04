# `converter/postprocess/restart_logic_pipeline.py`

Source: [converter/postprocess/restart_logic_pipeline.py](../../../../converter/postprocess/restart_logic_pipeline.py) | 345 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `9c724ed869c244e3216bd6e51d5aa7ea897517ec5e5df4070e3f1af6a1496dbb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Pipeline stage for injecting restart logic into UPDATE programs.

## Import declarations

```python
from __future__ import annotations
from typing import Optional
from converter.postprocess.restart_config import RestartConfig
from converter.postprocess.restart_logic_generator import RestartLogicGenerator
from converter.postprocess.update_postprocess_line_utils import UpdatePostprocessLineUtils
```

## Local dependency notes

- [converter/postprocess/restart_config.py](restart_config.md)
- [converter/postprocess/restart_logic_generator.py](restart_logic_generator.md)
- [converter/postprocess/update_postprocess_line_utils.py](update_postprocess_line_utils.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `RestartLogicPipeline` - L29-L345

```python
class RestartLogicPipeline()
```

Pipeline stage for injecting restart-aware UPDATE logic.

### `RestartLogicPipeline.__init__` - L65-L88

```python
__init__(self, config: RestartConfig, generator: RestartLogicGenerator, line_utils: UpdatePostprocessLineUtils) -> None
```

Initialize restart logic pipeline.

Observed calls (lexical order): `ValueError`.

Control points:

- L82: `if not config or not generator or (not line_utils)`

Explicit raises: `ValueError('config, generator, and line_utils are required')`.

### `RestartLogicPipeline.is_applicable` - L90-L128

```python
is_applicable(self, context: object) -> bool
```

Check if restart logic should be applied to this program.

Observed calls (lexical order): `hasattr`, `self.diagnostics.append`.

Control points:

- L106: `if not hasattr(context, 'program_kind')`
- L108: `if context.program_kind != 'update'`
- L115: `if not hasattr(context, 'restart_dclgen') or not context.restart_dclgen`
- L120: `if hasattr(context.restart_dclgen, 'score')`
- L121: `if context.restart_dclgen.score < self.config.minimum_dclgen_score`

### `RestartLogicPipeline.not_applicable_reason` - L130-L137

```python
not_applicable_reason(self) -> str
```

Return reason why restart logic was not applicable.

### `RestartLogicPipeline.apply_to_program` - L139-L197

```python
apply_to_program(self, cobol_source: str, context: object) -> str
```

Apply restart logic to UPDATE program source.

Observed calls (lexical order): `self.diagnostics.clear`, `self.is_applicable`, `self.diagnostics.append`, `self._validate_cobol_structure`, `self.generator.generate_all_paragraphs`, `len`, `self._inject_restart_paragraphs`.

Control points:

- L170: `if not self.is_applicable(context)`

### `RestartLogicPipeline._validate_cobol_structure` - L199-L226

```python
_validate_cobol_structure(self, cobol_source: str) -> None
```

Validate that COBOL source has required structure for restart injection.

Observed calls (lexical order): `self.line_utils.lines`, `self.line_utils.find_paragraph_range`, `ValueError`, `self.line_utils.logical_contains`.

Control points:

- L215: `if not self.line_utils.find_paragraph_range(lines, 'MAIN-PROCESS')`
- L220: `if not self.line_utils.logical_contains(cobol_source, f'01 {switch_group}.')`
- L225: `if not self.line_utils.logical_contains(cobol_source, f'01 {help_group}.')`

Explicit raises: `ValueError('No main PROCEDURE DIVISION paragraph found')`; `ValueError(f'Missing {switch_group} group in WORKING-STORAGE')`; `ValueError(f'Missing {help_group} group in WORKING-STORAGE')`.

### `RestartLogicPipeline._inject_restart_paragraphs` - L228-L274

```python
_inject_restart_paragraphs(self, cobol_source: str, paragraphs: dict[str, str]) -> str
```

Inject restart paragraphs into COBOL source.

Observed calls (lexical order): `self.line_utils.lines`, `self._find_paragraph_insertion_point`, `ValueError`, `'\n\n'.join`, `paragraphs.values`, `self.line_utils.join`, `self._inject_restart_control_call`.

Control points:

- L256: `if insert_line < 0`
- L271: `if '700-RESTART-CONTROL' not in updated_text`

Explicit raises: `ValueError('Could not find safe paragraph insertion point')`.

### `RestartLogicPipeline._find_paragraph_insertion_point` - L276-L297

```python
_find_paragraph_insertion_point(self, lines: list[str]) -> int
```

Find the line where new paragraphs should be inserted.

Observed calls (lexical order): `len`, `range`, `lines[i].upper`.

Control points:

- L292: `for i in range(len(lines) - 1, -1, -1)`
- L294: `if 'END PROGRAM' in line_upper`

### `RestartLogicPipeline._inject_restart_control_call` - L299-L345

```python
_inject_restart_control_call(self, cobol_source: str) -> str
```

Inject restart control call into MAIN-PROCESS paragraph.

Observed calls (lexical order): `self.line_utils.lines`, `self.line_utils.find_paragraph_range`, `ValueError`, `lines[first_statement].strip`, `lines[first_statement].strip().startswith`, `self.line_utils.join`.

Control points:

- L321: `if not main_range`
- L328: `while first_statement < end_line and (lines[first_statement].strip().startswith('*') or not lines[first_statement].strip())`

Explicit raises: `ValueError('MAIN-PROCESS paragraph not found')`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
