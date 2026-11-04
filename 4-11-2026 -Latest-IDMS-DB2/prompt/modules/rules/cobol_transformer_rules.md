# `rules/cobol_transformer_rules.py`

Source: [rules/cobol_transformer_rules.py](../../../rules/cobol_transformer_rules.py) | 52 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `c405595aadfd32fa0628d67c033d6aaf472a99499a895dfa28048d0d6e036b72`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`COBOL_TRANSFORMER_RULES` (L10), `DB2_COMPILER_OPTION_LINE` (L21), `DEFAULT_SQL_ERROR_PARAGRAPH` (L24), `GENERATED_LINE_PREFIXES` (L27), `ENFORCE_PROGRAM_NAME_LITERAL` (L42), `PROGRAM_NAME_LITERAL_MESSAGES` (L44)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_program_id_transformer.py](../converter/transformers/cobol_program_id_transformer.md)
- [converter/transformers/cobol_transformed_line_merger.py](../converter/transformers/cobol_transformed_line_merger.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
