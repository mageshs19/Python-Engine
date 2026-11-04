# `converter/generators/cursor_paragraph/join_key_label_resolver.py`

Source: [converter/generators/cursor_paragraph/join_key_label_resolver.py](../../../../../converter/generators/cursor_paragraph/join_key_label_resolver.py) | 251 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `851cf3848d6497a7c7d6c9825ecc3d4fc8a4eaee96e23f819aaa02eec38be721`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 column -> IDMS COBOL field name, for a job-log label.

## Module-level bindings

`LABEL_FALLBACK_KEY` (L47), `LOOKUP_FAILED_KEY` (L48), `UNKNOWN` (L49), `LEVEL_DIGITS` (L50), `__all__` (L251)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_paragraph_rules import DCLGEN_GROUP_PREFIX, DCLGEN_TABLE_SUFFIX, KEY_DIAGNOSTIC_MESSAGES, MAPPING_TABLE_SEPARATOR, MAPPING_TABLE_SUFFIX, STRIP_REDEFINES_SUFFIX_FROM_KEY_LABEL
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_key_diagnostics.py](cursor_key_diagnostics.md)
- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](cursor_paragraph_body_builder.md)
- [tests/cursor_contract/test_join_key_labels.py](../../../tests/cursor_contract/test_join_key_labels.md)

## Symbol contracts and control points

### `JoinKeyLabelResolver` - L53-L248

```python
class JoinKeyLabelResolver()
```

Resolves one DB2 column to the IDMS COBOL field name it came from.

### `JoinKeyLabelResolver.__init__` - L56-L58

```python
__init__(self, mapping_repository=None) -> None
```

### `JoinKeyLabelResolver.reset` - L60-L67

```python
reset(self) -> None
```

Drop the previous program's diagnostics.

### `JoinKeyLabelResolver.label_for` - L73-L79

```python
label_for(self, table: str, column: str, host: str) -> str
```

Observed calls (lexical order): `self._cobol_field`, `self._report`, `NameNormalizer.to_cobol`.

Control points:

- L75: `if resolved`

### `JoinKeyLabelResolver.table_of` - L82-L88

```python
table_of(group: str) -> str
```

DCLGEN group name -> table name. 'DCLDZBEFFTV' -> 'DZBEFFTV'.

Observed calls (lexical order): `str`, `str(group or '').strip`, `str(group or '').strip().upper`, `str(DCLGEN_GROUP_PREFIX or '').upper`, `text.startswith`, `len`.

Control points:

- L86: `if prefix and text.startswith(prefix)`

### `JoinKeyLabelResolver.candidate_tables` - L91-L111

```python
candidate_tables(table: str) -> list[str]
```

Every spelling of one table, DCLGEN first then Sheet Mapping.

Observed calls (lexical order): `str`, `str(table or '').strip`, `str(table or '').strip().upper`, `str(DCLGEN_TABLE_SUFFIX or '').upper`, `str(MAPPING_TABLE_SUFFIX or '').upper`, `len`, `text.endswith`, `out.append`.

Control points:

- L94: `if not text`
- L103: `for candidate in (f'{base}{mapped}', f'{base}{MAPPING_TABLE_SEPARATOR}{mapped}', base)`
- L108: `if candidate and candidate not in out`

### `JoinKeyLabelResolver._cobol_field` - L117-L136

```python
_cobol_field(self, table: str, column: str) -> str
```

Observed calls (lexical order): `self.candidate_tables`, `getattr`, `self._call`, `self._field_name`.

Control points:

- L118: `if self.mapping_repository is None or not column`
- L121: `for candidate in self.candidate_tables(table)`
- L122: `for probe in ('cobol_field_for_column', 'idms_field_for_column', 'find_cobol_zone')`
- L128: `if method is None`
- L133: `if field`

### `JoinKeyLabelResolver._call` - L138-L166

```python
_call(self, method, table: str, column: str)
```

Invoke one repository accessor by keyword, then positionally.

Observed calls (lexical order): `method`, `self._report_lookup_failure`.

### `JoinKeyLabelResolver._strip_redefines_suffix` - L169-L187

```python
_strip_redefines_suffix(name: str) -> str
```

Drop a trailing REDEFINES marker: NR-ID-STOCK-R1 -> NR-ID-STOCK.

Observed calls (lexical order): `name.rpartition`, `tail[1:].isdigit`.

Control points:

- L177: `if not STRIP_REDEFINES_SUFFIX_FROM_KEY_LABEL`
- L181: `if not separator or not head`
- L184: `if tail[:1] == 'R' and tail[1:].isdigit()`

### `JoinKeyLabelResolver._field_name` - L190-L209

```python
_field_name(value) -> str
```

Drop a COBOL Zone level prefix and terminator.

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().rstrip`, `str(value or '').strip().rstrip('.').strip`, `text.split`, `len`, `parts[0].isdigit`, `' '.join`, `' '.join(parts[1:]).strip`, `text.isdigit`, `NameNormalizer.to_cobol`, `JoinKeyLabelResolver._strip_redefines_suffix`.

Control points:

- L198: `if not text`
- L202: `if len(parts) > 1 and parts[0].isdigit() and (len(parts[0]) <= LEVEL_DIGITS)`
- L205: `if not text or text.isdigit()`

### `JoinKeyLabelResolver._report_lookup_failure` - L215-L229

```python
_report_lookup_failure(self, method, error: Exception) -> None
```

Observed calls (lexical order): `KEY_DIAGNOSTIC_MESSAGES.get`, `getattr`, `str`, `type`, `template.format`, `self.messages.append`.

Control points:

- L220: `if template`
- L228: `if text not in self.messages`

### `JoinKeyLabelResolver._report` - L231-L248

```python
_report(self, table: str, column: str) -> None
```

Observed calls (lexical order): `KEY_DIAGNOSTIC_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L233: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
