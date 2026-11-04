# `converter/transformers/idms_statement/transformer_shared_mixin.py`

Source: [converter/transformers/idms_statement/transformer_shared_mixin.py](../../../../../converter/transformers/idms_statement/transformer_shared_mixin.py) | 73 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `9ad9165fa0aea3caff8997c6011dbe8dbc441e2e8e0981c755a45f40966f4dcf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from patterns.idms_patterns import DB_END_OF_SET_TOKEN_PATTERN, DB_REC_NOT_FOUND_TOKEN_PATTERN, IDMS_DECLARATIVE_OR_CONTROL_PATTERNS
from rules.conversion_rules import COMMENTED_IDMS_LINE_PREFIX, UNMAPPED_RECORD_MARKER_TEMPLATE
from rules.idms_transformer_rules import CONTINUE_STATEMENT, PROCEDURE_DIVISION_NAME, SQLCODE_END_TOKEN_REPLACEMENT
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/idms_patterns.py](../../../patterns/idms_patterns.md)
- [rules/conversion_rules.py](../../../rules/conversion_rules.md)
- [rules/idms_transformer_rules.py](../../../rules/idms_transformer_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/idms_statement_transformer.py](../idms_statement_transformer.md)

## Symbol contracts and control points

### `TransformerSharedMixin` - L20-L73

```python
class TransformerSharedMixin()
```

Shared helpers used by control/data statement converters.

### `TransformerSharedMixin._keep_and_comment_unmapped` - L27-L43

```python
_keep_and_comment_unmapped(self, record: str, stripped_line: str) -> list[str]
```

Register the record as unmapped and comment the verb line.

Observed calls (lexical order): `NameNormalizer.to_cobol`, `self.unmapped_records.add`, `UNMAPPED_RECORD_MARKER_TEMPLATE.format`.

### `TransformerSharedMixin._removed_idms_executable_lines` - L45-L52

```python
_removed_idms_executable_lines(self, message: str, current_division: str) -> list[str]
```

Control points:

- L50: `if current_division == PROCEDURE_DIVISION_NAME`

### `TransformerSharedMixin._replace_idms_condition_tokens` - L54-L64

```python
_replace_idms_condition_tokens(self, line: str) -> list[str]
```

Observed calls (lexical order): `DB_REC_NOT_FOUND_TOKEN_PATTERN.sub`, `DB_END_OF_SET_TOKEN_PATTERN.sub`.

### `TransformerSharedMixin._is_idms_declarative_or_control_statement` - L66-L73

```python
_is_idms_declarative_or_control_statement(self, upper: str) -> bool
```

Observed calls (lexical order): `any`, `pattern.search`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
