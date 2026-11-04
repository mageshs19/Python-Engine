# `converter/composers/update_restart_skip_composer.py`

Source: [converter/composers/update_restart_skip_composer.py](../../../../converter/composers/update_restart_skip_composer.py) | 220 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `c6632d6ea4951208e220d67b3d5973215f7d294b33ab254182bf37081330874c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.sequence_patterns import strip_sequence_numbers
from patterns.update_restart_skip_patterns import CONTINUE_PATTERN, CONVERTED_FOR_PATTERN, DB2_COMMENT_PATTERN, END_IF_PATTERN, REMOVED_OBTAIN_CALC_PATTERN, SKIPPED_FOR_PATTERN, SQLCODE_IF_PATTERN
from rules.update_restart_skip_rules import EMIT_MANUAL_REDESIGN_MESSAGE, MANUAL_REDESIGN_MESSAGE_TEMPLATE, MISSING_MAPPING_MARKERS, REPLACEMENT_BLOCK_TEMPLATES, RESTART_CONTROL_HINTS
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [patterns/update_restart_skip_patterns.py](../../patterns/update_restart_skip_patterns.md)
- [rules/update_restart_skip_rules.py](../../rules/update_restart_skip_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/pipeline/registry.py](../pipeline/registry.md)
- [tests/test_update_restart_skip_no_message.py](../../tests/test_update_restart_skip_no_message.md)

## Symbol contracts and control points

### `UpdateRestartSkipComposer` - L21-L220

```python
class UpdateRestartSkipComposer()
```

Cleans generated missing-mapping blocks for unmapped restart/control records.

Declared class/data-model fields:

```python
EMIT_MANUAL_REDESIGN_MESSAGE = EMIT_MANUAL_REDESIGN_MESSAGE
```

### `UpdateRestartSkipComposer.__init__` - L48-L57

```python
__init__(self, emit_manual_redesign_message: bool | None=None) -> None
```

Observed calls (lexical order): `bool`.

Control points:

- L54: `if emit_manual_redesign_message is not None`

### `UpdateRestartSkipComposer.compose` - L58-L107

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self._normalize_line_endings`, `self._normalize_line_endings(text).splitlines`, `len`, `self._logical`, `REMOVED_OBTAIN_CALC_PATTERN.match`, `SKIPPED_FOR_PATTERN.match`, `CONVERTED_FOR_PATTERN.match`, `self._handle_restart_block`, `removed_obtain_match.group`, `skipped_match.group`, `converted_match.group`, `output.append`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L60: `if not text`
- L67: `while index < len(lines)`
- L74: `if removed_obtain_match`
- L84: `if skipped_match`
- L94: `if converted_match`

### `UpdateRestartSkipComposer._handle_restart_block` - L109-L137

```python
_handle_restart_block(self, *, lines: list[str], index: int, output: list[str], record_name: str, require_missing_marker: bool) -> int
```

Observed calls (lexical order): `str`, `str(record_name or '').upper`, `self._looks_like_restart_or_control`, `output.append`, `self._block_end`, `self._contains_missing_mapping_marker`, `output.extend`, `self._replacement_block`, `self._skip_following_sqlcode_blocks`, `self._note_manual_redesign`.

Control points:

- L120: `if not self._looks_like_restart_or_control(record)`
- L126: `if require_missing_marker and (not self._contains_missing_mapping_marker(lines[index:block_end]))`

### `UpdateRestartSkipComposer._block_end` - L139-L162

```python
_block_end(self, lines: list[str], start_index: int) -> int
```

Advance past a generated comment block ending in CONTINUE.

Observed calls (lexical order): `len`, `self._logical`, `DB2_COMMENT_PATTERN.match`, `CONTINUE_PATTERN.match`.

Control points:

- L147: `while index < len(lines)`
- L150: `if not logical`
- L153: `if DB2_COMMENT_PATTERN.match(logical)`
- L156: `if CONTINUE_PATTERN.match(logical)`

### `UpdateRestartSkipComposer._contains_missing_mapping_marker` - L164-L166

```python
_contains_missing_mapping_marker(self, lines: list[str]) -> bool
```

Observed calls (lexical order): `'\n'.join`, `self._logical`, `self._logical(line).upper`, `any`.

### `UpdateRestartSkipComposer._note_manual_redesign` - L168-L185

```python
_note_manual_redesign(self, record_name: str) -> None
```

Record that a restart block was replaced.

Observed calls (lexical order): `str`, `str(record_name or '').strip`, `str(record_name or '').strip().upper`, `MANUAL_REDESIGN_MESSAGE_TEMPLATE.format`, `self.messages.append`.

Control points:

- L176: `if not self.EMIT_MANUAL_REDESIGN_MESSAGE`
- L180: `if not record`
- L184: `if message not in self.messages`

### `UpdateRestartSkipComposer._replacement_block` - L187-L191

```python
_replacement_block(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `template.format`.

### `UpdateRestartSkipComposer._looks_like_restart_or_control` - L193-L195

```python
_looks_like_restart_or_control(self, record_name: str) -> bool
```

Observed calls (lexical order): `str`, `str(record_name or '').upper`, `any`.

### `UpdateRestartSkipComposer._skip_following_sqlcode_blocks` - L197-L205

```python
_skip_following_sqlcode_blocks(self, lines: list[str], start_index: int) -> int
```

Observed calls (lexical order): `len`, `SQLCODE_IF_PATTERN.match`, `self._logical`, `self._skip_if_block`.

Control points:

- L201: `while index < len(lines)`
- L202: `if not SQLCODE_IF_PATTERN.match(self._logical(lines[index]))`

### `UpdateRestartSkipComposer._skip_if_block` - L207-L214

```python
_skip_if_block(self, lines: list[str], start_index: int) -> int
```

Observed calls (lexical order): `len`, `self._logical`, `END_IF_PATTERN.match`.

Control points:

- L209: `while index < len(lines)`
- L212: `if END_IF_PATTERN.match(logical)`

### `UpdateRestartSkipComposer._logical` - L216-L217

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

### `UpdateRestartSkipComposer._normalize_line_endings` - L219-L220

```python
_normalize_line_endings(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
