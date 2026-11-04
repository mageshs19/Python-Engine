# `rules/restart_standard_rules.py`

Source: [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.py) | 261 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `27d0622d960a7fda6e71b8952cedfd10514e79deb3bbf5a889be0fb49488dc1f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Restart / checkpoint standard constants.

## Module-level bindings

`RESTART_STANDARD_RULES` (L32), `ROLE_CONTROL` (L58), `ROLE_SELECT` (L59), `ROLE_UPDATE` (L60), `ROLE_INSERT` (L61), `ROLE_RESTART_FOUND` (L62), `ROLE_WRITE_RESTART` (L63), `ROLE_COMMIT` (L64), `ROLE_ABEND` (L65), `RESTART_PARAGRAPH_ROLES` (L67), `COMMIT_BLOCK_SCAN_LIMIT` (L80), `SCHEME_SEVEN_SERIES` (L81), `SCHEME_EIGHT_SERIES` (L82), `PARAGRAPH_NUMBER_SCHEMES` (L84), `DEFAULT_PARAGRAPH_SCHEME` (L107), `RESTART_PARAGRAPH_PREFIXES` (L112), `STATUS_INCOMPLETE` (L129), `STATUS_COMPLETE` (L130), `DEFAULT_PHASE_NUMBER` (L132), `SQLCODE_OK` (L134), `SQLCODE_NOT_FOUND` (L135), `COMMIT_FREQUENCY` (L139), `COMMIT_TEST_THRESHOLD` (L140), `EMIT_SQL_LOCATION` (L159), `EMIT_SQL_LOCATION_IN_ERROR_BRANCH` (L160), `SQL_LOCATION_USES_PARAGRAPH_NUMBER` (L161), `ENFORCE_FULL_PAYLOAD_LENGTH_ON_COMMIT` (L175), `REQUIRE_RETENTION_FROM_METADATA` (L184), `APPLIES_TO_UPDATE_PROGRAMS` (L190), `APPLIES_TO_RETRIEVAL_PROGRAMS` (L191), `NOT_APPLICABLE_REASONS` (L193), `RESTART_DIAGNOSTICS` (L211), `__all__` (L228)

## Import declarations

```python
from __future__ import annotations
```

## Importers (22)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [catalogs/restart_paragraph_catalog.py](../catalogs/restart_paragraph_catalog.md)
- [converter/composers/restart/legacy_restart_cleanup.py](../converter/composers/restart/legacy_restart_cleanup.md)
- [converter/composers/restart/process_paragraph_injector.py](../converter/composers/restart/process_paragraph_injector.md)
- [converter/composers/restart/restart_injection_composer.py](../converter/composers/restart/restart_injection_composer.md)
- [converter/generators/restart/restart_config.py](../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_flow_builder.py](../converter/generators/restart/restart_flow_builder.md)
- [converter/generators/restart/restart_main_flow_builder.py](../converter/generators/restart/restart_main_flow_builder.md)
- [converter/generators/restart/restart_name_resolver.py](../converter/generators/restart/restart_name_resolver.md)
- [converter/generators/restart/restart_sql_builder.py](../converter/generators/restart/restart_sql_builder.md)
- [converter/generators/select_paragraph_generator.py](../converter/generators/select_paragraph_generator.md)
- [converter/resolvers/restart_role_resolver.py](../converter/resolvers/restart_role_resolver.md)
- [tests/restart/_checklist.py](../tests/restart/_checklist.md)
- [tests/restart/test_m10c_golden_output.py](../tests/restart/test_m10c_golden_output.md)
- [tests/restart/test_m1_restart_standards.py](../tests/restart/test_m1_restart_standards.md)
- [tests/restart/test_m2_restart_config.py](../tests/restart/test_m2_restart_config.md)
- [tests/restart/test_m4_sql_builder.py](../tests/restart/test_m4_sql_builder.md)
- [tests/restart/test_m5_flow_builder.py](../tests/restart/test_m5_flow_builder.md)
- [tests/restart/test_m6_main_flow_builder.py](../tests/restart/test_m6_main_flow_builder.md)
- [tests/restart/test_m7_process_injector.py](../tests/restart/test_m7_process_injector.md)
- [tests/restart/test_m8_read_paragraph.py](../tests/restart/test_m8_read_paragraph.md)
- [tests/restart/test_m9a_legacy_cleanup.py](../tests/restart/test_m9a_legacy_cleanup.md)
- [tests/restart/test_m9b_injection_composer.py](../tests/restart/test_m9b_injection_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
