# `converter/postprocess/final_cleanup/final_cleanup_dcl_reference.py`

Source: [converter/postprocess/final_cleanup/final_cleanup_dcl_reference.py](../../../../../converter/postprocess/final_cleanup/final_cleanup_dcl_reference.py) | 151 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `1f0f24928c078186f3108882dc472100b6f396a9505d35425a3a24a89ea127a3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.update_final_cleanup_patterns import END_EXEC_PATTERN, EXEC_SQL_PATTERN, MOVE_TO_DCL_DOT_REFERENCE_PATTERN, NON_SQL_DCL_DOT_REFERENCE_STRICT_PATTERN, TO_DCL_DOT_REFERENCE_PATTERN
from rules.update_cobol_final_cleanup_rules import FINAL_CLEANUP_AREA_B, FINAL_CLEANUP_BODY_WIDTH, FINAL_CLEANUP_DCL_PREFIX, FINAL_CLEANUP_FIELD_OF_GROUP_TEMPLATE, FINAL_CLEANUP_MOVE_TEMPLATE, FINAL_CLEANUP_TOKEN_END_EXEC, FINAL_CLEANUP_TOKEN_MOVE, FINAL_CLEANUP_TOKEN_TO, FINAL_CLEANUP_TO_FIELD_OF_GROUP_TEMPLATE
```

## Local dependency notes

- [patterns/update_final_cleanup_patterns.py](../../../patterns/update_final_cleanup_patterns.md)
- [rules/update_cobol_final_cleanup_rules.py](../../../rules/update_cobol_final_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_final_cleanup.py](../update_final_cleanup.md)

## Symbol contracts and control points

### `FinalCleanupDclReference` - L23-L151

```python
class FinalCleanupDclReference()
```

Rewrites non-SQL DCLGROUP.FIELD references to FIELD OF DCLGROUP.

### `FinalCleanupDclReference._rewrite_non_sql_dcl_dot_references` - L26-L101

```python
_rewrite_non_sql_dcl_dot_references(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._logical`, `logical.upper`, `EXEC_SQL_PATTERN.match`, `output.append`, `END_EXEC_PATTERN.match`, `MOVE_TO_DCL_DOT_REFERENCE_PATTERN.match`, `move_match.group`, `str`, `str(move_match.group('source')).strip`, `move_match.group('field').upper`, `move_match.group('group').upper`, `self._replace_body`, `FINAL_CLEANUP_MOVE_TEMPLATE.format`, `FINAL_CLEANUP_TO_FIELD_OF_GROUP_TEMPLATE.format`, `TO_DCL_DOT_REFERENCE_PATTERN.match`, `to_match.group`.
Another 10 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L30: `for line in lines`
- L34: `if EXEC_SQL_PATTERN.match(logical)`
- L35: `if FINAL_CLEANUP_TOKEN_END_EXEC in upper`
- L42: `if in_exec_sql`
- L44: `if END_EXEC_PATTERN.match(logical)`
- L49: `if move_match`
- L69: `if to_match`
- L83: `if move_rewrite`
- Another 1 conditions/loops exist in this source span.

### `FinalCleanupDclReference._rewrite_move_to_dcl_dot_as_lines` - L103-L143

```python
_rewrite_move_to_dcl_dot_as_lines(self, original_line: str) -> list[str]
```

Observed calls (lexical order): `self._body`, `self._body(original_line).rstrip`, `body.strip`, `stripped.upper`, `upper.startswith`, `self._split_last_to`, `after_to.split`, `group.strip`, `group.strip().upper`, `field.strip`, `field.strip().upper`, `field.endswith`, `field[:-1].strip`, `group.startswith`, `body.lstrip`, `len`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L108: `if not upper.startswith(FINAL_CLEANUP_TOKEN_MOVE)`
- L110: `if FINAL_CLEANUP_TOKEN_TO not in upper`
- L114: `if not before_to or not after_to or '.' not in after_to`
- L122: `if field.endswith('.')`
- L126: `if not group.startswith(FINAL_CLEANUP_DCL_PREFIX) or not field`
- L130: `if not leading`
- L137: `if len(one_line) <= FINAL_CLEANUP_BODY_WIDTH`

### `FinalCleanupDclReference._split_last_to` - L145-L151

```python
_split_last_to(self, text: str) -> tuple[str, str]
```

Observed calls (lexical order): `str`, `str(text or '').upper`, `upper.rfind`, `len`, `text[:index].strip`, `text[index + len(marker):].strip`.

Control points:

- L149: `if index < 0`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
