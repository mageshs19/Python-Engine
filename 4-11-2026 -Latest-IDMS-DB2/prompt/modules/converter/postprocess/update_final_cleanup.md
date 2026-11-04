# `converter/postprocess/update_final_cleanup.py`

Source: [converter/postprocess/update_final_cleanup.py](../../../../converter/postprocess/update_final_cleanup.py) | 156 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `0b3f4ed0bda508ee3dd63a8e6273ae4cd4d287e8e7086eb4ccab47b3394bd28d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import os
from converter.postprocess.final_cleanup.final_cleanup_dcl_reference import FinalCleanupDclReference
from converter.postprocess.final_cleanup.final_cleanup_line_utils import FinalCleanupLineUtils
from converter.postprocess.final_cleanup.final_cleanup_normalizer import FinalCleanupNormalizer
from patterns.update_final_cleanup_patterns import CONVERTED_MODIFY_COMMENT_PATTERN, DCL_REFERENCE_PATTERN, INITIALIZE_DCL_PATTERN, MOVE_SPACES_TO_BARE_RECORD_PATTERN
from rules.update_cobol_final_cleanup_rules import FINAL_CLEANUP_MAX_CONSECUTIVE_BLANKS
import sys
import re
```

## Local dependency notes

- [converter/postprocess/final_cleanup/final_cleanup_dcl_reference.py](final_cleanup/final_cleanup_dcl_reference.md)
- [converter/postprocess/final_cleanup/final_cleanup_line_utils.py](final_cleanup/final_cleanup_line_utils.md)
- [converter/postprocess/final_cleanup/final_cleanup_normalizer.py](final_cleanup/final_cleanup_normalizer.md)
- [patterns/update_final_cleanup_patterns.py](../../patterns/update_final_cleanup_patterns.md)
- [rules/update_cobol_final_cleanup_rules.py](../../rules/update_cobol_final_cleanup_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)
- [tests/test_update_char_literal_quoter.py](../../tests/test_update_char_literal_quoter.md)
- [tests/test_update_final_cleanup_dcl_dot.py](../../tests/test_update_final_cleanup_dcl_dot.md)

## Symbol contracts and control points

### `UpdateFinalCleanup` - L25-L156

```python
class UpdateFinalCleanup(FinalCleanupLineUtils, FinalCleanupDclReference, FinalCleanupNormalizer)
```

Final update-only cleanup after fixed-format resequencing.

### `UpdateFinalCleanup.apply` - L40-L64

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `len`, `print`, `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `str(text or '').replace('\r\n', '\n').replace('\r', '\n').splitlines`, `self._remove_duplicate_includes`, `self._remove_leftover_modify_comments`, `self._rewrite_non_sql_dcl_dot_references`, `self._remove_obsolete_bare_record_initializes`, `self._normalize_update_paragraphs`, `self._normalize_procedure_simple_blocks`, `self._normalize_excess_blank_lines`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L44: `if not text`

### `UpdateFinalCleanup._remove_duplicate_includes` - L66-L98

```python
_remove_duplicate_includes(self, lines: list[str]) -> list[str]
```

Remove duplicate EXEC SQL INCLUDE statements.

Observed calls (lexical order): `len`, `print`, `enumerate`, `re.search`, `match.group`, `match.group(1).upper`, `output.append`.

Control points:

- L81: `for (i, line) in enumerate(lines)`
- L84: `if match`
- L86: `if include_name in seen_includes`

### `UpdateFinalCleanup._remove_leftover_modify_comments` - L100-L110

```python
_remove_leftover_modify_comments(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._body`, `self._body(line).strip`, `str`, `CONVERTED_MODIFY_COMMENT_PATTERN.search`, `output.append`.

Control points:

- L102: `for line in lines`
- L105: `if CONVERTED_MODIFY_COMMENT_PATTERN.search(logical)`
- L107: `if CONVERTED_MODIFY_COMMENT_PATTERN.search(raw)`

### `UpdateFinalCleanup._remove_obsolete_bare_record_initializes` - L112-L140

```python
_remove_obsolete_bare_record_initializes(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self._paragraph_ranges`, `any`, `INITIALIZE_DCL_PATTERN.match`, `self._logical`, `DCL_REFERENCE_PATTERN.search`, `range`, `MOVE_SPACES_TO_BARE_RECORD_PATTERN.match`, `remove_indexes.add`, `enumerate`.

Control points:

- L117: `for (start, end) in self._paragraph_ranges(lines)`
- L128: `if not has_dcl_initialize or not has_dcl_usage`
- L131: `for index in range(start + 1, end)`
- L132: `if MOVE_SPACES_TO_BARE_RECORD_PATTERN.match(self._logical(lines[index]))`
- L135: `if not remove_indexes`

### `UpdateFinalCleanup._normalize_excess_blank_lines` - L142-L156

```python
_normalize_excess_blank_lines(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._logical`, `output.append`.

Control points:

- L146: `for line in lines`
- L147: `if self._logical(line)`
- L153: `if blank_count <= FINAL_CLEANUP_MAX_CONSECUTIVE_BLANKS`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
