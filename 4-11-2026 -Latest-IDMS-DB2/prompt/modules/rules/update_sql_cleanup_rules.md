# `rules/update_sql_cleanup_rules.py`

Source: [rules/update_sql_cleanup_rules.py](../../../rules/update_sql_cleanup_rules.py) | 79 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `f1a91f37668bdf2bd733d1e607e467cb0d48d45b9240a5ecbe1567ec80e46976`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`PROTECTED_BARE_TARGET_PREFIXES` (L11), `UPDATE_AUDIT_PREFIXES` (L30), `INSERT_ONLY_AUDIT_PREFIXES` (L38), `IDENTITY_KEY_PREFIXES` (L42), `UPDATE_QUERYNO` (L54), `USE_EVALUATE_SQLCODE` (L58), `SQLCODE_EVALUATE_PATTERN` (L65), `END_EVALUATE_PATTERN` (L70), `LONE_PERIOD_PATTERN` (L76)

## Import declarations

```python
import re
from rules.key_naming_rules import IDENTITY_KEY_PREFIXES
```

## Local dependency notes

- [rules/key_naming_rules.py](key_naming_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/column_mixin.py](../converter/composers/update_sql_cleanup/column_mixin.md)
- [converter/composers/update_sql_cleanup/key_column_mixin.py](../converter/composers/update_sql_cleanup/key_column_mixin.md)
- [converter/composers/update_sql_cleanup/modify_update_rewriter.py](../converter/composers/update_sql_cleanup/modify_update_rewriter.md)
- [converter/composers/update_sql_cleanup/scan_mixin.py](../converter/composers/update_sql_cleanup/scan_mixin.md)
- [converter/composers/update_sql_cleanup_base.py](../converter/composers/update_sql_cleanup_base.md)
- [converter/generators/sql/sql_statement_builder.py](../converter/generators/sql/sql_statement_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
