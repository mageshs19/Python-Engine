# `converter/transformers/field_reference/field_reference_host_resolver.py`

Source: [converter/transformers/field_reference/field_reference_host_resolver.py](../../../../../converter/transformers/field_reference/field_reference_host_resolver.py) | 65 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `edeb0ebb7865a09af182c6bfc6f8f141ab8bf79c1633f6c8c04ae1ae4cbfbbdb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.services.name_normalizer import NameNormalizer
from patterns.field_reference_rewriter_patterns import HOST_REFERENCE_DOT_PATTERN, HOST_REFERENCE_OF_PATTERN, HOST_REFERENCE_OF_SPLIT_PATTERN
from rules.field_reference_rewriter_rules import HOST_QUALIFIER_CONNECTOR, HOST_OF_GROUP_TEMPLATE, HOST_OF_SPLIT_PART_COUNT, HOST_REFERENCE_LEADING_CHAR
```

## Local dependency notes

- [converter/resolvers/host_variable_resolver.py](../../resolvers/host_variable_resolver.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/field_reference_rewriter_patterns.py](../../../patterns/field_reference_rewriter_patterns.md)
- [rules/field_reference_rewriter_rules.py](../../../rules/field_reference_rewriter_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference_context_builder.py](../field_reference_context_builder.md)

## Symbol contracts and control points

### `FieldReferenceHostResolver` - L18-L65

```python
class FieldReferenceHostResolver()
```

Resolves and formats a DCLGEN host reference for a DB2 column.

### `FieldReferenceHostResolver.__init__` - L25-L26

```python
__init__(self, host_variable_resolver: HostVariableResolver) -> None
```

### `FieldReferenceHostResolver.dclgen_reference_for_column` - L28-L59

```python
dclgen_reference_for_column(self, *, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `self.host_variable_resolver.host_reference_for_column`, `str`, `str(host_reference or '').strip`, `HOST_REFERENCE_OF_PATTERN.search`, `of_match.group`, `self._format`, `HOST_REFERENCE_DOT_PATTERN.search`, `dot_match.group`, `host_reference.lstrip`, `host_reference.lstrip(HOST_REFERENCE_LEADING_CHAR).strip`, `cleaned.upper`, `HOST_REFERENCE_OF_SPLIT_PATTERN.split`, `len`, `NameNormalizer.to_cobol`.

Control points:

- L39: `if not host_reference`
- L45: `if of_match`
- L49: `if dot_match`
- L54: `if HOST_QUALIFIER_CONNECTOR in cleaned.upper()`
- L56: `if len(parts) == HOST_OF_SPLIT_PART_COUNT`

### `FieldReferenceHostResolver._format` - L61-L65

```python
_format(self, host: str, group: str) -> str
```

Observed calls (lexical order): `HOST_OF_GROUP_TEMPLATE.format`, `NameNormalizer.to_cobol`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
