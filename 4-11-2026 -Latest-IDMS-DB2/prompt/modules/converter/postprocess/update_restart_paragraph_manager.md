# `converter/postprocess/update_restart_paragraph_manager.py`

Source: [converter/postprocess/update_restart_paragraph_manager.py](../../../../converter/postprocess/update_restart_paragraph_manager.py) | 168 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `d025527b87ba8de80057beefa1a79f5ac375038d66d05ef4e41c40a2d2610260`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.cobol_update_standard_generator import CobolUpdateStandardGenerator
from converter.postprocess.dynamic_metadata_resolver import UpdateProgramContext
from converter.postprocess.update_postprocess_line_utils import UpdatePostprocessLineUtils
from rules.update_restart_rules import RESTART_PARAGRAPH_NAMES, UPDATE_RESTART_DIAGNOSTICS, UPDATE_RESTART_WS_NAMES
```

## Local dependency notes

- [converter/postprocess/cobol_update_standard_generator.py](cobol_update_standard_generator.md)
- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)
- [converter/postprocess/update_postprocess_line_utils.py](update_postprocess_line_utils.md)
- [rules/update_restart_rules.py](../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `UpdateRestartParagraphManager` - L17-L168

```python
class UpdateRestartParagraphManager()
```

### `UpdateRestartParagraphManager.__init__` - L18-L25

```python
__init__(self, *, generator: CobolUpdateStandardGenerator, line_utils: UpdatePostprocessLineUtils) -> None
```

### `UpdateRestartParagraphManager.ensure_read_flat_file` - L27-L76

```python
ensure_read_flat_file(self, cobol_text: str, context: UpdateProgramContext, diagnostics: list[str]) -> str
```

Observed calls (lexical order): `self.line_utils.logical_contains`, `diagnostics.append`, `self.generator.read_flat_file`, `self.line_utils.lines`, `self.line_utils.find_paragraph_range`, `paragraph.splitlines`, `self.line_utils.join`, `self.line_utils.procedure_paragraph_insert_line_index`.

Control points:

- L35: `if not self.line_utils.logical_contains(cobol_text, f'01 {switch_group}.')`
- L53: `if existing_range`
- L61: `if insert_index < 0`

### `UpdateRestartParagraphManager.ensure_restart_paragraphs` - L78-L136

```python
ensure_restart_paragraphs(self, cobol_text: str, context: UpdateProgramContext, diagnostics: list[str]) -> str
```

Observed calls (lexical order): `diagnostics.append`, `self.line_utils.logical_contains`, `self.generator.restart_paragraphs`, `restart_code.strip`, `self.line_utils.lines`, `self._remove_existing_restart_paragraphs`, `self.line_utils.procedure_paragraph_insert_line_index`, `restart_code.splitlines`, `self.line_utils.join`.

Control points:

- L84: `if not context.restart_dclgen`
- L91: `if not self.line_utils.logical_contains(cobol_text, f'01 {switch_group}.') or not self.line_utils.logical_contains(cobol_text, f'01 {help_group}.')`
- L106: `if not restart_code.strip()`
- L120: `if insert_index < 0`

### `UpdateRestartParagraphManager._remove_existing_restart_paragraphs` - L138-L168

```python
_remove_existing_restart_paragraphs(self, *, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `list`, `self.line_utils.find_paragraph_range`.

Control points:

- L156: `for paragraph_name in paragraph_names`
- L162: `if not existing_range`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
