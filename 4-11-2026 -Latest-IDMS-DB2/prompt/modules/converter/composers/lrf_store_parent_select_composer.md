# `converter/composers/lrf_store_parent_select_composer.py`

Source: [converter/composers/lrf_store_parent_select_composer.py](../../../../converter/composers/lrf_store_parent_select_composer.py) | 246 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `c11832d316ec1e3d40df7c74287166181f192204dee3629f979145f57169a4ae`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generate the keyed parent read required by an LRF STORE path.

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_lrf_store_parent_select_composer.py](../../tests/test_lrf_store_parent_select_composer.md)

## Symbol contracts and control points

### `LrfStoreParentSelectComposer` - L7-L246

```python
class LrfStoreParentSelectComposer()
```

Declared class/data-model fields:

```python
_MARKER = re.compile('DB2-LRF-STORE-PARENT:\\s*(?P<record>[A-Z][A-Z0-9-]*)', re.I)
```

### `LrfStoreParentSelectComposer.__init__` - L10-L12

```python
__init__(self, *, sql_generator) -> None
```

### `LrfStoreParentSelectComposer._body` - L15-L19

```python
_body(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `text[7:72].strip`, `text.strip`.

Control points:

- L17: `if len(text) >= 7 and text[:6].isdigit()`

### `LrfStoreParentSelectComposer.compose` - L21-L144

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `len`, `self._body`, `self._MARKER.search`, `output.append`, `marker.group`, `marker.group('record').upper`, `next`, `min`, `range`, `re.search`, `any`, `self.messages.append`, `self.sql.select_by_key`, `self._is_comment`.
Another 9 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L26: `while index < len(lines)`
- L29: `if not marker`
- L46: `if insert_start is None`
- L59: `if insert_end_exec is None`
- L78: `if end_evaluate is None or period_line is None`
- L87: `if not parent_select or not any((re.search('\\bSELECT\\b', str(line), re.I) for line in parent_select))`
- L142: `if str(text or '').endswith(('\n', '\r'))`

### `LrfStoreParentSelectComposer._strip_statement_terminators` - L148-L188

```python
_strip_statement_terminators(cls, lines: list[str]) -> list[str]
```

Remove trailing COBOL periods inside a generated nested scope.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `cls._body`, `body.endswith`, `result.append`, `len`, `raw.rfind`.

Control points:

- L155: `for line in lines`
- L158: `if not body.endswith('.')`
- L165: `while index < len(body)`
- L167: `if char == "'"`
- L168: `if quoted and index + 1 < len(body) and (body[index + 1] == "'")`
- L172: `if index == len(body) - 1`
- L176: `if last_char_quoted`
- L184: `if dot_pos >= 0`

### `LrfStoreParentSelectComposer._is_comment` - L191-L195

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L193: `if len(text) >= 7 and text[:6].isdigit() and (text[6] in ('*', '/'))`

### `LrfStoreParentSelectComposer._parent_to_child_key_moves` - L197-L246

```python
_parent_to_child_key_moves(self, parent_record: str, insert_lines: list[str]) -> list[str]
```

Copy shared parent key values into child INSERT host variables.

Observed calls (lexical order): `getattr`, `all`, `self.messages.append`, `' '.join`, `self._body`, `re.search`, `insert_match.group`, `table_resolver.resolve_table`, `value.strip`, `value.strip().upper`, `insert_match.group('columns').split`, `mapping.db2_table_for_record`, `dclgen.column_names_for_table`, `set`, `hosts.host_reference_for_column`, `moves.append`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L204: `if not all((mapping, dclgen, table_resolver, hosts))`
- L216: `if not insert_match`
- L226: `if not parent_table or not child_table`
- L236: `for column in shared_columns`
- L239: `if not source or not target`
- L242: `if not moves`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
