# `runners/audit_cursor_control_ownership.py`

Source: [runners/audit_cursor_control_ownership.py](../../../runners/audit_cursor_control_ownership.py) | 125 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `8599585235bc3c166a966fb05a3e9f31e2aa014a9a7184d6bc524f0b92d0a826`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Audit generated COBOL for paragraph entry displays and cursor ownership.

## Module-level bindings

`PROJECT_ROOT` (L17)

## Import declarations

```python
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from converter.composers.cursor_close_guarantee_composer import CursorCloseGuaranteeComposer
from converter.composers.paragraph_entry_display_composer import _is_paragraph, _logical
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee_composer.py](../converter/composers/cursor_close_guarantee_composer.md)
- [converter/composers/paragraph_entry_display_composer.py](../converter/composers/paragraph_entry_display_composer.md)

## Symbol contracts and control points

### `audit_file` - L30-L87

```python
audit_file(path: Path) -> dict
```

Observed calls (lexical order): `path.read_text`, `text.splitlines`, `next`, `enumerate`, `_logical`, `re.match`, `_is_paragraph`, `len`, `range`, `_logical(lines[next_index]).startswith`, `f"DISPLAY '{name}'.".upper`, `_logical(lines[next_index]).upper`, `missing_displays.append`, `re.findall`, `re.search`, `match.group`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L38: `if procedure is None`
- L43: `for index in headers`
- L46: `while next_index < len(lines) and (not _logical(lines[next_index]) or _logical(lines[next_index]).startswith(('*', '/')))`
- L51: `if next_index >= len(lines) or _logical(lines[next_index]).upper() != expected`
- L56: `for cursor in cursors`
- L58: `for operation in ('OPEN', 'FETCH', 'CLOSE')`

### `main` - L90-L121

```python
main() -> int
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `args.folder.glob`, `sorted`, `parser.error`, `audit_file`, `result.get`, `failures.append`, `result.get('cursor_lifecycle', {}).items`, `all`, `len`, `json.dumps`, `args.output.parent.mkdir`, `args.output.write_text`, `print`.

Control points:

- L96: `if not files`
- L100: `for result in results`
- L101: `if result.get('error')`
- L103: `if result.get('missing_active_exact_name_displays')`
- L105: `if not result.get('cursor_lifecycle_second_pass_idempotent', False)`
- L107: `for (cursor, operations) in result.get('cursor_lifecycle', {}).items()`
- L108: `if not all((operations[op]['paragraph_found'] for op in ('OPEN', 'FETCH', 'CLOSE')))`
- L117: `if args.output`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
