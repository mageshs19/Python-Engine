# `patterns/idms_patterns.py`

Source: [patterns/idms_patterns.py](../../../patterns/idms_patterns.py) | 343 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `f35b98f295800ba06aefe864c1a2010b127793b218db1fc59195f54e30ecc23a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> IDMS regex patterns.

## Module-level bindings

`OBTAIN_CALC_PATTERN` (L71), `OBTAIN_CALC_REVERSED_PATTERN` (L76), `OBTAIN_FIRST_NEXT_PATTERN` (L81), `OBTAIN_OWNER_PATTERN` (L87), `FIND_FIRST_PATTERN` (L94), `FIND_CURRENT_PATTERN` (L100), `STORE_PATTERN` (L106), `MODIFY_PATTERN` (L111), `ERASE_PATTERN` (L116), `CONNECT_STATEMENT_PATTERN` (L121), `DISCONNECT_STATEMENT_PATTERN` (L126), `IDMS_WRITE_VERB_PATTERN` (L135), `READY_PATTERN` (L142), `READY_UPDATE_PATTERN` (L147), `FINISH_PATTERN` (L152), `COMMIT_PATTERN` (L157), `ROLLBACK_PATTERN` (L162), `BIND_STATEMENT_PATTERN` (L167), `USAGE_MODE_PATTERN` (L172), `IDMS_STATUS_PERFORM_PATTERN` (L177), `IDMS_ABORT_PERFORM_PATTERN` (L182), `DB_REC_NOT_FOUND_TOKEN_PATTERN` (L188), `DB_END_OF_SET_TOKEN_PATTERN` (L193), `ON_DB_REC_NOT_FOUND_PATTERN` (L198), `IDMS_CONTROL_SECTION_PATTERN` (L208), `PROTOCOL_PATTERN` (L213), `IDMS_RECORDS_WITHIN_PATTERN` (L218), `SCHEMA_SECTION_PATTERN` (L223), `DB_RECORD_WITHIN_PATTERN` (L228), `COPY_IDMS_PATTERN` (L236), `IDMS_RECORDS_CLAUSE_PATTERN` (L248), `MODE_IS_CLAUSE_PATTERN` (L253), `IDMS_DECLARATIVE_OR_CONTROL_PATTERNS` (L259), `REMOVED_COPYBOOK_FIELD_PATTERN` (L277), `DISPLAY_STATEMENT_PATTERN` (L290), `MOVE_TO_STATEMENT_PATTERN` (L295), `IDMS_STOP_PERFORM_PATTERN` (L300), `__all__` (L305)

## Import declarations

```python
from __future__ import annotations
import re
from rules.idms_transformer_rules import REMOVED_COPYBOOK_FIELDS
```

## Local dependency notes

- [rules/idms_transformer_rules.py](../rules/idms_transformer_rules.md)

## Importers (11)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/unmapped_record_block_composer.py](../converter/composers/unmapped_record_block_composer.md)
- [converter/parsers/cobol_parser.py](../converter/parsers/cobol_parser.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../converter/pipeline/conversion/conversion_component_factory.md)
- [converter/transformers/idms_residual_cleanup.py](../converter/transformers/idms_residual_cleanup.md)
- [converter/transformers/idms_statement/control_statement_converter.py](../converter/transformers/idms_statement/control_statement_converter.md)
- [converter/transformers/idms_statement/data_statement_converter.py](../converter/transformers/idms_statement/data_statement_converter.md)
- [converter/transformers/idms_statement/transformer_shared_mixin.py](../converter/transformers/idms_statement/transformer_shared_mixin.md)
- [review/standards/program_kind_detector.py](../review/standards/program_kind_detector.md)
- [tests/test_imports.py](../tests/test_imports.md)
- [tests/test_patterns.py](../tests/test_patterns.md)
- [tests/test_program_kind_classification.py](../tests/test_program_kind_classification.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
