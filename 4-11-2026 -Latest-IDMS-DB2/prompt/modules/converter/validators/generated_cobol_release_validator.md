# `converter/validators/generated_cobol_release_validator.py`

Source: [converter/validators/generated_cobol_release_validator.py](../../../../converter/validators/generated_cobol_release_validator.py) | 638 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `b4cc8d06ccd6af9395c664b1529c1b61cb2fa60f5bb3deebb11e8634e5574f85`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Static release gate for generated fixed-format COBOL with embedded DB2 SQL.

## Module-level bindings

`_FIXED` (L27), `_EXEC_SQL` (L28), `_END_EXEC` (L29), `_SQL_SELECT_INTO` (L30)

## Import declarations

```python
from __future__ import annotations
import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from rules.cursor_close_guarantee_rules import NON_PARAGRAPH_SINGLE_WORDS
from converter.services.perform_thru_scope import paragraph_indices, perform_spans
from converter.analyzers.access_error_policy import AccessPattern, classify_access, policy_for
```

## Local dependency notes

- [converter/analyzers/access_error_policy.py](../analyzers/access_error_policy.md)
- [converter/services/perform_thru_scope.py](../services/perform_thru_scope.md)
- [rules/cursor_close_guarantee_rules.py](../../rules/cursor_close_guarantee_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_34_generated_structure.py](../../review/checks/chk_34_generated_structure.md)
- [tests/output_write/test_perform_thru_helper_safety.py](../../tests/output_write/test_perform_thru_helper_safety.md)
- [tests/test_generated_cobol_release_validator.py](../../tests/test_generated_cobol_release_validator.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../tests/test_generic_cursor_numbering_and_perform_integrity.md)
- [tests/test_lrf_cursor_release_gate.py](../../tests/test_lrf_cursor_release_gate.md)
- [tests/test_retrieval_handwritten_obtain_calc_safety.py](../../tests/test_retrieval_handwritten_obtain_calc_safety.md)

## Symbol contracts and control points

### `ValidationIssue` - L20-L24

```python
class ValidationIssue()
```

Declared class/data-model fields:

```python
severity: str
code: str
line: int
message: str
```

### `_line_parts` - L33-L36

```python
_line_parts(line: str) -> tuple[str, str]
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].rstrip`, `line.rstrip`.

Control points:

- L34: `if len(line) >= 7 and line[:6].isdigit()`

### `_is_comment` - L39-L41

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `_line_parts`.

### `_mask_literals_and_inline_comment` - L44-L77

```python
_mask_literals_and_inline_comment(body: str) -> str
```

Blank literals and COBOL inline comments without changing offsets.

Observed calls (lexical order): `list`, `str`, `len`, `range`, `''.join`.

Control points:

- L55: `while i < len(chars)`
- L57: `if quote is not None`
- L59: `if char == quote`
- L60: `if i + 1 < len(chars) and chars[i + 1] == quote`
- L67: `if char in {"'", '"'}`
- L72: `if char == '*' and i + 1 < len(chars) and (chars[i + 1] == '>')`
- L73: `for j in range(i, len(chars))`

### `_sql_list_items` - L80-L83

```python
_sql_list_items(text: str) -> list[str]
```

Split a simple SQL comma list; fail-closed for expressions/aliases.

Observed calls (lexical order): `item.strip`, `item.strip().lstrip`, `item.strip().lstrip(',').strip`, `text.replace`, `text.replace('\n', ' ').split`.

### `validate_generated_cobol` - L86-L610

```python
validate_generated_cobol(text: str, *, path: str='<memory>') -> list[ValidationIssue]
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `enumerate`, `_FIXED.match`, `len`, `ValidationIssue`, `issues.append`, `paragraph_indices`, `perform_spans`, `'\n'.join`, `_line_parts`, `_mask_literals_and_inline_comment`, `_mask_literals_and_inline_comment(_line_parts(line)[1]).upper`, `_is_comment`, `labels.items`, `name.startswith`.
Another 73 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L91: `for (number, line) in enumerate(lines, 1)`
- L92: `if _FIXED.match(line) and len(line) > 80`
- L105: `for (name, index) in labels.items()`
- L106: `if not name.startswith('WRITE-')`
- L108: `if not re.search(f'\\bPERFORM\\s+{re.escape(name)}\\b', executed)`
- L110: `for span in scopes`
- L111: `if span.start_index <= index <= span.end_index`
- L124: `for (number, line) in enumerate(lines, 1)`
- Another 80 conditions/loops exist in this source span.

### `validate_file` - L613-L614

```python
validate_file(path: Path) -> list[ValidationIssue]
```

Observed calls (lexical order): `path.read_text`, `str`, `validate_generated_cobol`.

### `main` - L617-L634

```python
main() -> int
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `Path`, `path.is_file`, `print`, `validate_file`, `all_issues.extend`, `str`, `any`.

Control points:

- L622: `for raw_path in args.paths`
- L624: `if not path.is_file()`
- L629: `if not issues`
- L631: `for (path, issue) in all_issues`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
