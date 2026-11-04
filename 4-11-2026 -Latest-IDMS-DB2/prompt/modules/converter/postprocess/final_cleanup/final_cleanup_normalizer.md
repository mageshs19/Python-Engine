# `converter/postprocess/final_cleanup/final_cleanup_normalizer.py`

Source: [converter/postprocess/final_cleanup/final_cleanup_normalizer.py](../../../../../converter/postprocess/final_cleanup/final_cleanup_normalizer.py) | 171 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `a4635e1f3d1d0d2e43aaae1ab25e4d6153b35b2b794f4c6dde6f2ffaf86d794d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.update_final_cleanup_patterns import END_EVALUATE_PATTERN, END_EXEC_PATTERN, EVALUATE_SQLCODE_PATTERN, EXEC_SQL_PATTERN, PARAGRAPH_HEADER_PATTERN, PERFORM_PATTERN, PROCESS_COMMIT_IF_PATTERN, STOP_RUN_PATTERN, UPDATE_PARAGRAPH_PATTERN, WHEN_PATTERN
from rules.update_cobol_final_cleanup_rules import FINAL_CLEANUP_ACTION_INDENT, FINAL_CLEANUP_AREA_B, FINAL_CLEANUP_DOT, FINAL_CLEANUP_SQL_BODY, FINAL_CLEANUP_TOKEN_END_EVALUATE, FINAL_CLEANUP_TOKEN_END_EXEC, FINAL_CLEANUP_TOKEN_END_IF, FINAL_CLEANUP_TOKEN_END_IF_DOT, FINAL_CLEANUP_TOKEN_EVALUATE_SQLCODE, FINAL_CLEANUP_TOKEN_EXEC_SQL, FINAL_CLEANUP_TOKEN_PROCEDURE_DIVISION, FINAL_CLEANUP_TOKEN_STOP_RUN, FINAL_CLEANUP_WHEN_INDENT
```

## Local dependency notes

- [patterns/update_final_cleanup_patterns.py](../../../patterns/update_final_cleanup_patterns.md)
- [rules/update_cobol_final_cleanup_rules.py](../../../rules/update_cobol_final_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_final_cleanup.py](../update_final_cleanup.md)

## Symbol contracts and control points

### `FinalCleanupNormalizer` - L32-L171

```python
class FinalCleanupNormalizer()
```

Normalizes 1100-UPDATE-* paragraphs and PROCEDURE simple blocks.

### `FinalCleanupNormalizer._normalize_update_paragraphs` - L35-L46

```python
_normalize_update_paragraphs(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `list`, `len`, `UPDATE_PARAGRAPH_PATTERN.match`, `self._logical`, `self._paragraph_end_index`, `self._normalize_update_paragraph`.

Control points:

- L38: `while index < len(output)`
- L39: `if not UPDATE_PARAGRAPH_PATTERN.match(self._logical(output[index]))`

### `FinalCleanupNormalizer._normalize_update_paragraph` - L48-L118

```python
_normalize_update_paragraph(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `enumerate`, `self._logical`, `self._is_comment_or_debug`, `output.append`, `EXEC_SQL_PATTERN.match`, `self._replace_body`, `END_EXEC_PATTERN.match`, `logical.rstrip`, `EVALUATE_SQLCODE_PATTERN.match`, `WHEN_PATTERN.match`, `END_EVALUATE_PATTERN.match`.

Control points:

- L53: `for (index, line) in enumerate(lines)`
- L56: `if index == 0 or not logical or self._is_comment_or_debug(line)`
- L60: `if EXEC_SQL_PATTERN.match(logical)`
- L67: `if in_exec_sql and END_EXEC_PATTERN.match(logical)`
- L74: `if in_exec_sql`
- L80: `if EVALUATE_SQLCODE_PATTERN.match(logical)`
- L89: `if in_evaluate and WHEN_PATTERN.match(logical)`
- L95: `if in_evaluate and END_EVALUATE_PATTERN.match(logical)`
- Another 2 conditions/loops exist in this source span.

### `FinalCleanupNormalizer._normalize_procedure_simple_blocks` - L120-L171

```python
_normalize_procedure_simple_blocks(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._logical`, `logical.upper`, `logical.upper().rstrip`, `upper.startswith`, `output.append`, `self._is_comment_or_debug`, `PARAGRAPH_HEADER_PATTERN.match`, `STOP_RUN_PATTERN.match`, `self._replace_body`, `PROCESS_COMMIT_IF_PATTERN.match`, `logical.rstrip`, `PERFORM_PATTERN.match`.

Control points:

- L125: `for line in lines`
- L129: `if upper.startswith(FINAL_CLEANUP_TOKEN_PROCEDURE_DIVISION)`
- L134: `if not in_procedure or self._is_comment_or_debug(line)`
- L138: `if PARAGRAPH_HEADER_PATTERN.match(logical)`
- L143: `if STOP_RUN_PATTERN.match(logical)`
- L149: `if PROCESS_COMMIT_IF_PATTERN.match(logical)`
- L156: `if inside_simple_if and PERFORM_PATTERN.match(logical)`
- L162: `if inside_simple_if and upper.startswith(FINAL_CLEANUP_TOKEN_END_IF)`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
