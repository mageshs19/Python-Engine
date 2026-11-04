# `converter/transformers/field_reference_replacement_engine.py`

Source: [converter/transformers/field_reference_replacement_engine.py](../../../../converter/transformers/field_reference_replacement_engine.py) | 367 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `0405352625b34472dc83a9f63cd02c955fea97a47a5bafe10431308b38cf4c8a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`UNMAPPED_FIELD_TEMPLATE` (L21), `GROUP_SPLIT_AT_USE_TEMPLATE` (L26), `GROUP_PARTIAL_AT_USE_TEMPLATE` (L31), `__all__` (L365)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.name_normalizer import NameNormalizer
from patterns.field_reference_rewriter_patterns import OF_IN_AFTER_PATTERN, OF_IN_BEFORE_PATTERN, QUALIFIED_REFERENCE_PATTERN
from rules.field_reference_rewriter_rules import PROTECTED_BARE_PREFIXES
```

## Local dependency notes

- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [patterns/field_reference_rewriter_patterns.py](../../patterns/field_reference_rewriter_patterns.md)
- [rules/field_reference_rewriter_rules.py](../../rules/field_reference_rewriter_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference_rewriter.py](field_reference_rewriter.md)

## Symbol contracts and control points

### `FieldReferenceReplacementEngine` - L38-L362

```python
class FieldReferenceReplacementEngine()
```

Rewrites qualified and bare IDMS field references using resolved Sheet Mapping + DCLGEN host-reference maps.

### `FieldReferenceReplacementEngine.__init__` - L97-L119

```python
__init__(self, *, record_field_map: dict[str, dict[str, str]], rewrite_messages: list[str], group_columns: dict[str, dict[str, list[str]]] | None=None, group_issues: dict[str, dict[str, dict[str, list[str]]]] | None=None) -> None
```

Observed calls (lexical order): `set`.

### `FieldReferenceReplacementEngine.rewrite_qualified_references` - L121-L151

```python
rewrite_qualified_references(self, text: str) -> str
```

Observed calls (lexical order): `QUALIFIED_REFERENCE_PATTERN.sub`.

### `FieldReferenceReplacementEngine.rewrite_qualified_references.repl` - L125-L146

```python
repl(match)
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `match.group`, `NameNormalizer.normalize`, `self.target_for_record_field`, `self.report_unmapped_field`, `self.rewrite_messages.append`.

Control points:

- L134: `if not target`

### `FieldReferenceReplacementEngine.report_unmapped_field` - L153-L223

```python
report_unmapped_field(self, *, record: str, field: str) -> None
```

Report a field gap on a record this program DID map.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.field_key`, `self.record_field_map.get`, `self.unmapped_fields.add`, `NameNormalizer.to_cobol`, `self.group_issues.get`, `self.group_issues.get(record_key, {}).get`, `(issue or {}).get`, `self.group_columns.get`, `self.group_columns.get(record_key, {}).get`, `len`, `self.rewrite_messages.append`, `GROUP_SPLIT_AT_USE_TEMPLATE.format`, `', '.join`, `GROUP_PARTIAL_AT_USE_TEMPLATE.format`, `UNMAPPED_FIELD_TEMPLATE.format`.

Control points:

- L171: `if not record_key or not field_key`
- L176: `if not mapped`
- L179: `if field_key in mapped`
- L184: `if marker in self.unmapped_fields`
- L194: `if columns and len(columns) > 1`
- L205: `if columns and unmapped`

### `FieldReferenceReplacementEngine.rewrite_bare_references` - L225-L262

```python
rewrite_bare_references(self, *, text: str, active_record: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.record_field_map.get`, `str`, `sorted`, `field_map.items`, `len`, `NameNormalizer.to_cobol`, `self.is_protected_bare_source_name`, `self.replace_bare_identifier`.

Control points:

- L233: `if not record`
- L238: `if not field_map`
- L243: `for (source_key, target_reference) in sorted(field_map.items(), key=lambda item: len(item[0]), reverse=True)`
- L250: `if not source_name or not target_reference`
- L253: `if source_name in self.local_names or self.is_protected_bare_source_name(source_name)`

### `FieldReferenceReplacementEngine.rewrite_unique_bare_references` - L264-L271

```python
rewrite_unique_bare_references(self, text: str) -> str
```

Observed calls (lexical order): `self.unique_bare_map.items`, `self.is_protected_bare_source_name`, `self.replace_bare_identifier`, `self.unique_date_map.items`.

Control points:

- L265: `for (source, target) in self.unique_bare_map.items()`
- L266: `if not self.is_protected_bare_source_name(source)`
- L268: `if self.allow_unique_dates`
- L269: `for (source, target) in self.unique_date_map.items()`

### `FieldReferenceReplacementEngine.replace_bare_identifier` - L273-L310

```python
replace_bare_identifier(self, *, text: str, source_name: str, target_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `str`, `str(target_name or '').strip`, `re.compile`, `re.escape`, `pattern.sub`.

Control points:

- L283: `if not source or not target`

### `FieldReferenceReplacementEngine.replace_bare_identifier.repl` - L291-L305

```python
repl(match)
```

Observed calls (lexical order): `match.start`, `match.end`, `self.is_part_of_qualified_reference`, `match.group`, `self.rewrite_messages.append`.

Control points:

- L295: `if self.is_part_of_qualified_reference(before_text=before_text, after_text=after_text)`

### `FieldReferenceReplacementEngine.target_for_record_field` - L312-L324

```python
target_for_record_field(self, *, record_name: str, source_field: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.field_key`, `self.record_field_map.get`, `self.record_field_map.get(record, {}).get`.

Control points:

- L321: `if not record or not field`

### `FieldReferenceReplacementEngine.field_key` - L326-L330

```python
field_key(self, value: str) -> str
```

Observed calls (lexical order): `NameNormalizer.to_cobol`.

### `FieldReferenceReplacementEngine.is_protected_bare_source_name` - L332-L345

```python
is_protected_bare_source_name(self, source_name: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `NameNormalizer.to_cobol(source_name).upper`, `source.startswith`.

Control points:

- L338: `if not source`
- L341: `for prefix in PROTECTED_BARE_PREFIXES`
- L342: `if source.startswith(prefix)`

### `FieldReferenceReplacementEngine.is_part_of_qualified_reference` - L347-L362

```python
is_part_of_qualified_reference(self, *, before_text: str, after_text: str) -> bool
```

Observed calls (lexical order): `str`, `str(before_text or '').upper`, `str(after_text or '').upper`, `OF_IN_BEFORE_PATTERN.search`, `OF_IN_AFTER_PATTERN.match`.

Control points:

- L356: `if OF_IN_BEFORE_PATTERN.search(before)`
- L359: `if OF_IN_AFTER_PATTERN.match(after)`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
