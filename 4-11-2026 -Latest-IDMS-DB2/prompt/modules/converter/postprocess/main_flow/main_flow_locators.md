# `converter/postprocess/main_flow/main_flow_locators.py`

Source: [converter/postprocess/main_flow/main_flow_locators.py](../../../../../converter/postprocess/main_flow/main_flow_locators.py) | 65 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `7161c13c929da3738fac599380a40adfc39ad4de5aaece0cfe7d6bdeaaae185c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.update_main_flow_patterns import OPEN_INPUT_LINE_PATTERN, STOP_RUN_LINE_PATTERN
from rules.update_restart_rules import MAIN_FLOW_LEGACY_RESTART_TOKENS, MAIN_FLOW_LONE_PERIOD, MAIN_FLOW_TOKEN_CLOSE
```

## Local dependency notes

- [patterns/update_main_flow_patterns.py](../../../patterns/update_main_flow_patterns.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_main_flow_rewriter.py](../update_main_flow_rewriter.md)

## Symbol contracts and control points

### `MainFlowLocators` - L14-L65

```python
class MainFlowLocators()
```

Index/region finders and insertion planning for the main flow.

### `MainFlowLocators._find_open_input_index` - L17-L28

```python
_find_open_input_index(self, *, lines, file_name)
```

Observed calls (lexical order): `str`, `str(file_name or '').strip`, `str(file_name or '').strip().upper`, `enumerate`, `OPEN_INPUT_LINE_PATTERN.search`, `self._logical`, `self._logical(line).upper`, `match.group`, `str(match.group('file') or '').strip`, `str(match.group('file') or '').strip().upper`.

Control points:

- L19: `if not target`
- L22: `for (index, line) in enumerate(lines)`
- L24: `if not match`
- L26: `if str(match.group('file') or '').strip().upper() == target`

### `MainFlowLocators._find_close_input_index` - L30-L41

```python
_find_close_input_index(self, *, lines, file_name)
```

Observed calls (lexical order): `str`, `str(file_name or '').strip`, `str(file_name or '').strip().upper`, `enumerate`, `self._logical`, `self._logical(line).upper`, `logical.startswith`.

Control points:

- L32: `if not target`
- L35: `for (index, line) in enumerate(lines)`
- L37: `if not logical.startswith(MAIN_FLOW_TOKEN_CLOSE)`
- L39: `if target in logical`

### `MainFlowLocators._find_stop_run_index` - L43-L47

```python
_find_stop_run_index(self, *, lines, start_index)
```

Observed calls (lexical order): `len`, `range`, `STOP_RUN_LINE_PATTERN.search`, `self._logical`, `self._logical(lines[index]).upper`.

Control points:

- L44: `for index in range(start_index, len(lines))`
- L45: `if STOP_RUN_LINE_PATTERN.search(self._logical(lines[index]).upper())`

### `MainFlowLocators._has_legacy_restart_between` - L49-L54

```python
_has_legacy_restart_between(self, *, lines, start_index, end_index)
```

Observed calls (lexical order): `range`, `self._logical`, `self._logical(lines[index]).upper`, `any`.

Control points:

- L50: `for index in range(start_index, end_index)`
- L52: `if any((token in upper for token in MAIN_FLOW_LEGACY_RESTART_TOKENS))`

### `MainFlowLocators._read_next_insert_plan` - L56-L65

```python
_read_next_insert_plan(self, *, lines, start, end)
```

Observed calls (lexical order): `range`, `self._logical`, `logical.endswith`.

Control points:

- L57: `for index in range(end - 1, start, -1)`
- L59: `if not logical`
- L61: `if logical == MAIN_FLOW_LONE_PERIOD`
- L63: `if logical.endswith('.')`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
