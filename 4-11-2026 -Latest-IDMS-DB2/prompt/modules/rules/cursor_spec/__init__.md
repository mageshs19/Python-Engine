# `rules/cursor_spec/__init__.py`

Source: [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.py) | 9 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `9f8a5dd6ab8d987629f6933d0ff362f65559bae43579e9a3a83e0a730edbf3a6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor specification rules.

## Module-level bindings

`__all__` (L9)

## Import declarations

```python
from rules.cursor_spec.cursor_spec_messages import SPEC_MESSAGES
from rules.cursor_spec.cursor_spec_rules import *
from rules.cursor_spec.cursor_spec_rules import __all__ as _RULES_ALL
```

## Local dependency notes

- [rules/cursor_spec/cursor_spec_messages.py](cursor_spec_messages.md)
- [rules/cursor_spec/cursor_spec_rules.py](cursor_spec_rules.md)

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/spec_factory.py](../../converter/generators/db2_infrastructure/spec_builder/spec_factory.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_fixed_format.py](../../converter/generators/db2_infrastructure/spec_builder/spec_fixed_format.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.py](../../converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.py](../../converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_reporter.py](../../converter/generators/db2_infrastructure/spec_builder/spec_reporter.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.py](../../converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_where_builder.py](../../converter/generators/db2_infrastructure/spec_builder/spec_where_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
