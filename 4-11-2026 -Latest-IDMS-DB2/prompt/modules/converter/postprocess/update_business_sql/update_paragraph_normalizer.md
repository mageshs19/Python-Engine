# `converter/postprocess/update_business_sql/update_paragraph_normalizer.py`

Source: [converter/postprocess/update_business_sql/update_paragraph_normalizer.py](../../../../../converter/postprocess/update_business_sql/update_paragraph_normalizer.py) | 120 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `87aa2918adafd9c59e5c40d8db54134abdbc54b96e8795e72b7bf25a6bc9a581`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.update_business_sql_patterns import END_EVALUATE_PATTERN, END_EXEC_PATTERN, EVALUATE_SQLCODE_PATTERN, EXEC_SQL_START_PATTERN
from rules.update_business_sql_rules import NESTED_INDENT, UPDATE_SQL_SQL_BODY_INDENT, TOKEN_END_EVALUATE, TOKEN_END_EXEC, TOKEN_EVALUATE_SQLCODE, TOKEN_EXEC_SQL, TOKEN_WHEN, WHEN_INDENT
from rules.update_restart_rules import UPDATE_SQL_PARAGRAPH_PREFIX
```

## Local dependency notes

- [patterns/update_business_sql_patterns.py](../../../patterns/update_business_sql_patterns.md)
- [rules/update_business_sql_rules.py](../../../rules/update_business_sql_rules.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_business_sql_standardizer.py](../update_business_sql_standardizer.md)

## Symbol contracts and control points

### `UpdateParagraphNormalizer` - L22-L120

```python
class UpdateParagraphNormalizer()
```

Normalizes generated update-paragraph indentation.

### `UpdateParagraphNormalizer._normalize_all_update_paragraphs` - L29-L50

```python
_normalize_all_update_paragraphs(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `list`, `len`, `self._logical`, `self._logical(output[index]).upper`, `self._logical(output[index]).upper().rstrip`, `logical.startswith`, `self.line_utils.find_paragraph_range`, `self._normalize_update_paragraph_lines`.

Control points:

- L33: `while index < len(output)`
- L36: `if not logical.startswith(f'{UPDATE_SQL_PARAGRAPH_PREFIX}-')`
- L41: `if not paragraph_range`

### `UpdateParagraphNormalizer._normalize_update_paragraph_lines` - L52-L120

```python
_normalize_update_paragraph_lines(self, paragraph_lines: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `self._logical`, `self._logical(line).strip`, `self._is_comment_line`, `output.append`, `EXEC_SQL_START_PATTERN.match`, `self._active_line_like`, `END_EXEC_PATTERN.match`, `logical.rstrip`, `EVALUATE_SQLCODE_PATTERN.match`, `logical.upper`, `logical.upper().startswith`, `END_EVALUATE_PATTERN.match`.

Control points:

- L60: `for (index, line) in enumerate(paragraph_lines)`
- L63: `if index == 0 or not logical or self._is_comment_line(line)`
- L67: `if EXEC_SQL_START_PATTERN.match(logical)`
- L72: `if in_exec_sql and END_EXEC_PATTERN.match(logical)`
- L77: `if in_exec_sql`
- L86: `if EVALUATE_SQLCODE_PATTERN.match(logical)`
- L93: `if in_evaluate and logical.upper().startswith(TOKEN_WHEN)`
- L102: `if in_evaluate and END_EVALUATE_PATTERN.match(logical)`
- Another 1 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
