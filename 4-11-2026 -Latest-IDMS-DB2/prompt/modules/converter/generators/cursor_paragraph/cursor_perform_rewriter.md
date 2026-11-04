# `converter/generators/cursor_paragraph/cursor_perform_rewriter.py`

Source: [converter/generators/cursor_paragraph/cursor_perform_rewriter.py](../../../../../converter/generators/cursor_paragraph/cursor_perform_rewriter.py) | 182 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `7647adb069b478dbcec192477c8c38210b40bd264dfbc8f940d77d1b20d7b33e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Rewrites PERFORM targets onto generated cursor paragraph names.

## Module-level bindings

`LEGACY_SPEC_KEYS` (L28), `SPEC_KEY_BY_OPERATION` (L34)

## Import declarations

```python
from __future__ import annotations
import re
from patterns.cursor_paragraph_patterns import LEGACY_PERFORM_PATTERN_TEMPLATE, LEGACY_SQL_ERROR_HEADER_PATTERN, LEGACY_SQL_ERROR_HEADER_REPLACEMENT, LEGACY_SQL_ERROR_PERFORM_PATTERN, NUMBERED_PERFORM_PATTERN_TEMPLATE, PERFORM_REPLACEMENT_TEMPLATE, UNNUMBERED_PERFORM_PATTERN_TEMPLATE
from rules.cursor_paragraph_rules import CURSOR_OPERATIONS, SQL_ERROR_PARAGRAPH_NAME
```

## Local dependency notes

- [patterns/cursor_paragraph_patterns.py](../../../patterns/cursor_paragraph_patterns.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph_generator.py](../cursor_paragraph_generator.md)

## Symbol contracts and control points

### `CursorPerformRewriter` - L41-L182

```python
class CursorPerformRewriter()
```

### `CursorPerformRewriter.rewrite` - L43-L83

```python
rewrite(self, text: str, cursor_specs: list[dict[str, object]]) -> str
```

Observed calls (lexical order): `str`, `spec.get`, `str(spec.get('cursor_name', '')).strip`, `str(spec.get(SPEC_KEY_BY_OPERATION[operation], '')).strip`, `self._replace_unnumbered`, `self._replace_numbered`, `self._replace_legacy_spec`.

Control points:

- L50: `for spec in cursor_specs`
- L53: `if not cursor_name`
- L56: `for operation in CURSOR_OPERATIONS`
- L61: `if not target_paragraph`

### `CursorPerformRewriter.normalize_sql_error_references` - L85-L109

```python
normalize_sql_error_references(self, text: str) -> str
```

Rename SQL-ERROR to SQLERROR without changing termination.

Observed calls (lexical order): `str`, `LEGACY_SQL_ERROR_PERFORM_PATTERN.sub`, `match.group`, `LEGACY_SQL_ERROR_HEADER_PATTERN.sub`.

### `CursorPerformRewriter._replace_unnumbered` - L111-L129

```python
_replace_unnumbered(self, text: str, operation: str, cursor_name: str, target_paragraph: str) -> str
```

Observed calls (lexical order): `re.compile`, `UNNUMBERED_PERFORM_PATTERN_TEMPLATE.format`, `re.escape`, `pattern.sub`, `PERFORM_REPLACEMENT_TEMPLATE.format`.

### `CursorPerformRewriter._replace_numbered` - L131-L149

```python
_replace_numbered(self, text: str, operation: str, cursor_name: str, target_paragraph: str) -> str
```

Observed calls (lexical order): `re.compile`, `NUMBERED_PERFORM_PATTERN_TEMPLATE.format`, `re.escape`, `pattern.sub`, `PERFORM_REPLACEMENT_TEMPLATE.format`.

### `CursorPerformRewriter._replace_legacy_spec` - L151-L182

```python
_replace_legacy_spec(self, text: str, spec: dict[str, object]) -> str
```

Observed calls (lexical order): `str`, `spec.get`, `str(spec.get(old_key, '')).strip`, `str(spec.get(new_key, '')).strip`, `re.compile`, `LEGACY_PERFORM_PATTERN_TEMPLATE.format`, `re.escape`, `pattern.sub`, `PERFORM_REPLACEMENT_TEMPLATE.format`.

Control points:

- L158: `for (old_key, new_key) in LEGACY_SPEC_KEYS`
- L162: `if not old_paragraph or not new_paragraph`
- L165: `if old_paragraph == new_paragraph`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
