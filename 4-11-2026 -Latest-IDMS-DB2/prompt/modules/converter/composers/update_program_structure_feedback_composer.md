# `converter/composers/update_program_structure_feedback_composer.py`

Source: [converter/composers/update_program_structure_feedback_composer.py](../../../../converter/composers/update_program_structure_feedback_composer.py) | 243 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `970d49fcfb78c414fe64f625956cc21dc8a6ac662d379c58ba71aa624650f642`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.update_sql_cleanup_base import UpdateSqlCleanupBase
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/composers/update_sql_cleanup_base.py](update_sql_cleanup_base.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_program_feedback_composer.py](update_program_feedback_composer.md)

## Symbol contracts and control points

### `UpdateProgramStructureFeedbackComposer` - L11-L243

```python
class UpdateProgramStructureFeedbackComposer(UpdateSqlCleanupBase)
```

Fixes update-program structure feedback issues: - DCLGEN INCLUDE placement. - timestamp paragraph fall-through.

### `UpdateProgramStructureFeedbackComposer.compose` - L18-L31

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `output.strip`, `self._move_dclgen_includes_to_infrastructure`, `self._prevent_timestamp_fallthrough`, `output.rstrip`.

Control points:

- L25: `if not output.strip()`

### `UpdateProgramStructureFeedbackComposer._move_dclgen_includes_to_infrastructure` - L33-L73

```python
_move_dclgen_includes_to_infrastructure(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `len`, `self._collect_exec_sql_block`, `output.append`, `self._include_name_from_block`, `self._is_after_procedure`, `includes_to_move.append`, `output.extend`, `self._insert_includes_near_sqlca`, `self.messages.append`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L43: `while index < len(lines)`
- L46: `if not block`
- L53: `if include and include not in {'SQLCA', 'SQLERRWS', 'SQLERROR'}`
- L54: `if self._is_after_procedure(lines, index)`
- L63: `if not includes_to_move`
- L68: `if changed`

### `UpdateProgramStructureFeedbackComposer._prevent_timestamp_fallthrough` - L75-L109

```python
_prevent_timestamp_fallthrough(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `enumerate`, `self._logical`, `self.TIMESTAMP_PARAGRAPH_PATTERN.match`, `self.STOP_RUN_PATTERN.match`, `lines.pop`, `lines.insert`, `self.messages.append`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L83: `for (index, line) in enumerate(lines)`
- L86: `if timestamp_index < 0 and self.TIMESTAMP_PARAGRAPH_PATTERN.match(logical)`
- L89: `if stop_index < 0 and self.STOP_RUN_PATTERN.match(logical)`
- L92: `if timestamp_index < 0 or stop_index < 0`
- L95: `if stop_index < timestamp_index`
- L100: `if stop_index < timestamp_index`

### `UpdateProgramStructureFeedbackComposer._collect_exec_sql_block` - L111-L132

```python
_collect_exec_sql_block(self, lines: list[str], index: int) -> tuple[list[str], int]
```

Observed calls (lexical order): `len`, `self.EXEC_SQL_START_PATTERN.match`, `self._logical`, `output.append`, `self.EXEC_SQL_END_PATTERN.match`.

Control points:

- L116: `if index >= len(lines)`
- L119: `if not self.EXEC_SQL_START_PATTERN.match(self._logical(lines[index]))`
- L124: `while index < len(lines)`
- L129: `if self.EXEC_SQL_END_PATTERN.match(logical)`

### `UpdateProgramStructureFeedbackComposer._include_name_from_block` - L134-L145

```python
_include_name_from_block(self, block: list[str]) -> str
```

Observed calls (lexical order): `self._logical`, `self.INCLUDE_PATTERN.match`, `NameNormalizer.normalize`, `match.group`.

Control points:

- L138: `for line in block`
- L142: `if match`

### `UpdateProgramStructureFeedbackComposer._is_after_procedure` - L147-L156

```python
_is_after_procedure(self, lines: list[str], index: int) -> bool
```

Observed calls (lexical order): `self._logical`, `self._logical(prior).upper`, `self._logical(prior).upper().startswith`.

Control points:

- L152: `for prior in lines[:index]`
- L153: `if self._logical(prior).upper().startswith('PROCEDURE DIVISION')`

### `UpdateProgramStructureFeedbackComposer._insert_includes_near_sqlca` - L158-L196

```python
_insert_includes_near_sqlca(self, lines: list[str], includes: list[str]) -> list[str]
```

Observed calls (lexical order): `'\n'.join`, `self._existing_includes`, `NameNormalizer.normalize`, `unique.append`, `self._include_insert_index`, `include_lines.extend`.

Control points:

- L166: `for include in includes`
- L169: `if not clean`
- L171: `if clean in existing`
- L173: `if clean in unique`
- L178: `if not unique`
- L184: `for include in unique`
- L193: `if insert_index < 0`

### `UpdateProgramStructureFeedbackComposer._include_insert_index` - L198-L225

```python
_include_insert_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `len`, `self._collect_exec_sql_block`, `self._include_name_from_block`, `self.SQL_LOCATION_PATTERN.match`, `self._logical`, `self.LINKAGE_SECTION_PATTERN.match`.

Control points:

- L205: `while index < len(lines)`
- L208: `if block`
- L211: `if include and include != 'SQLERROR'`
- L217: `if self.SQL_LOCATION_PATTERN.match(self._logical(lines[index]))`
- L220: `if self.LINKAGE_SECTION_PATTERN.match(self._logical(lines[index]))`

### `UpdateProgramStructureFeedbackComposer._existing_includes` - L227-L243

```python
_existing_includes(self, text: str) -> set[str]
```

Observed calls (lexical order): `set`, `re.finditer`, `NameNormalizer.normalize`, `match.group`, `output.add`.

Control points:

- L233: `for match in re.finditer('\\bINCLUDE\\s+([A-Z0-9]+)\\b', text, flags=re.IGNORECASE)`
- L240: `if include`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
