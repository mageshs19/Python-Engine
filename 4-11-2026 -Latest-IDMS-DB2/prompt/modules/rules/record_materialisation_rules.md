# `rules/record_materialisation_rules.py`

Source: [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.py) | 255 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `05fceaea78feb65f6292509223dc5547a7b4c696cb9b6b553253c211f1f7664f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`ENFORCE_RECORD_MATERIALISATION` (L8), `REQUIRE_COMPLETE_FIELD_COVERAGE` (L14), `ENFORCE_LENGTH_MATCH` (L19), `LENGTH_TOLERANCE` (L22), `GROUP_PICTURE_TOKENS` (L32), `MOVE_MARKER_TEMPLATE` (L37), `MOVE_INDENT` (L40), `EMIT_DATE_CONVERSION` (L42), `DATE_LOW_VALUE_LITERAL` (L44), `DATE_HIGH_VALUE_LITERAL` (L45), `DATE_HIGH_NUMERIC_LITERAL` (L46), `DATE_CONVERSION_LINE_TEMPLATES` (L48), `DATE_DB2_TYPE_PREFIX` (L65), `NON_DATE_DB2_TYPE_PREFIXES` (L66), `RECORD_MATERIALISATION_MESSAGES` (L71), `ALLOW_LAYOUT_SHORTER_THAN_TARGET` (L106), `EMIT_REMAINDER_FILLER` (L110), `REMAINDER_FILLER_NAME` (L111), `REMAINDER_FILLER_PICTURE_TEMPLATE` (L112), `FILLER_FIELD_NAMES` (L116), `NON_COLUMN_SENTINELS` (L120), `MAX_RECORD_MOVES` (L124), `NON_RECORD_NAME_SUFFIXES` (L129), `RECORD_GROUP_LEVEL_STEP` (L133), `MIN_LEVEL` (L134), `MAX_LEVEL` (L135), `LAYOUT_BODY_WIDTH` (L174), `LAYOUT_BASE_INDENT` (L178), `LAYOUT_LEVEL_STEP` (L182), `LAYOUT_MAX_INDENT_DEPTH` (L185), `LAYOUT_NAME_WIDTH` (L189), `LAYOUT_MIN_NAME_GAP` (L190), `GROUP_ITEM_TEMPLATE` (L194), `ELEMENTARY_ITEM_TEMPLATE` (L195), `REDEFINES_TEMPLATE` (L198), `LAYOUT_MARKER_TEMPLATE` (L200), `MOVE_TEMPLATE` (L202), `MOVE_TARGET_TEMPLATE` (L203), `WRAP_REDEFINES_ENTRY` (L207), `REDEFINES_INLINE_LIMIT` (L211), `REDEFINES_HEAD_TEMPLATE` (L214), `REDEFINES_CONTINUATION_GAP` (L217), `MOVE_CONTINUATION_INDENT` (L222), `MOVE_INLINE_LIMIT` (L225), `EMIT_TARGET_MEASUREMENT` (L255)

## Import declarations

```python
from __future__ import annotations
```

## Importers (18)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_block_writer.py](../converter/composers/record_materialisation/record_block_writer.md)
- [converter/composers/record_materialisation/record_entry_renderer.py](../converter/composers/record_materialisation/record_entry_renderer.md)
- [converter/composers/record_materialisation/record_field.py](../converter/composers/record_materialisation/record_field.md)
- [converter/composers/record_materialisation/record_layout_generator.py](../converter/composers/record_materialisation/record_layout_generator.md)
- [converter/composers/record_materialisation/record_layout_geometry.py](../converter/composers/record_materialisation/record_layout_geometry.md)
- [converter/composers/record_materialisation/record_materialisation_guard.py](../converter/composers/record_materialisation/record_materialisation_guard.md)
- [converter/composers/record_materialisation/record_move_generator.py](../converter/composers/record_materialisation/record_move_generator.md)
- [converter/composers/record_materialisation/record_plan.py](../converter/composers/record_materialisation/record_plan.md)
- [converter/composers/record_materialisation/record_plan_builder.py](../converter/composers/record_materialisation/record_plan_builder.md)
- [converter/composers/record_materialisation/record_redefines_renderer.py](../converter/composers/record_materialisation/record_redefines_renderer.md)
- [converter/composers/record_materialisation/record_row_reader.py](../converter/composers/record_materialisation/record_row_reader.md)
- [converter/composers/record_materialisation_composer.py](../converter/composers/record_materialisation_composer.md)
- [tests/generated_fields/test_db2_code_fixes.py](../tests/generated_fields/test_db2_code_fixes.md)
- [tests/test_db2_code_fixes.py](../tests/test_db2_code_fixes.md)
- [tests/test_mapping_filler_layout_regression.py](../tests/test_mapping_filler_layout_regression.md)
- [tests/test_rules_no_duplicate_constants.py](../tests/test_rules_no_duplicate_constants.md)
- 2 further importers are recorded in [the source manifest](../../source_manifest.json).

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
