# `rules/idms_transformer_rules.py`

Source: [rules/idms_transformer_rules.py](../../../rules/idms_transformer_rules.py) | 41 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a98c30c8879a4f620c8b68e912c18296bd3d7146ef3387c3f34b8d0d9bb08743`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`IDMS_TRANSFORMER_RULES` (L6), `PROCEDURE_DIVISION_NAME` (L15), `OBTAIN_FIRST_KEYWORD` (L18), `SQLCODE_END_TOKEN_REPLACEMENT` (L21), `CONTINUE_STATEMENT` (L24), `SQLCODE_100_IF_OPEN` (L27), `SQLCODE_100_IF_CLOSE` (L28), `SQLCODE_100_CONTINUE_BODY` (L29), `REMOVED_COPYBOOK_FIELDS` (L31), `REMOVED_COPYBOOK_FIELD_RULE` (L37)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/idms_statement/data_statement_converter.py](../converter/transformers/idms_statement/data_statement_converter.md)
- [converter/transformers/idms_statement/transformer_shared_mixin.py](../converter/transformers/idms_statement/transformer_shared_mixin.md)
- [patterns/idms_patterns.py](../patterns/idms_patterns.md)
- [tests/test_on_db_rec_not_found_bare.py](../tests/test_on_db_rec_not_found_bare.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
