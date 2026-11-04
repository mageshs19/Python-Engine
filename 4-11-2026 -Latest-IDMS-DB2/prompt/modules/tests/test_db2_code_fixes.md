# `tests/test_db2_code_fixes.py`

Source: [tests/test_db2_code_fixes.py](../../../tests/test_db2_code_fixes.py) | 607 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `000e2b222cd12520d72757c044b0b0ab24fe7467d52458be3e425b7a82167682`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regression tests for IDMS-to-DB2 COBOL conversion safety.

## Import declarations

```python
import pytest
from unittest.mock import Mock, patch, MagicMock
from converter.transformers.cobol_transformer import CobolTransformer
from converter.transformers.idms_statement_transformer import IdmsStatementTransformer
from converter.transformers.cobol_transformer_line_utils import CobolTransformerLineUtils
from converter.composers.record_materialisation.record_entry_renderer import RecordEntryRenderer
from rules.record_materialisation_rules import EMIT_REMAINDER_FILLER
from converter.composers.record_materialisation.record_layout_generator import RecordLayoutGenerator
from converter.composers.record_materialisation.record_plan import RecordMaterialisationPlan
from converter.composers.record_materialisation.record_field import RecordFieldPlan
from converter.resolvers.cursor_column_resolver import CursorColumnResolver
```

## Local dependency notes

- [converter/composers/record_materialisation/record_entry_renderer.py](../converter/composers/record_materialisation/record_entry_renderer.md)
- [converter/composers/record_materialisation/record_field.py](../converter/composers/record_materialisation/record_field.md)
- [converter/composers/record_materialisation/record_layout_generator.py](../converter/composers/record_materialisation/record_layout_generator.md)
- [converter/composers/record_materialisation/record_plan.py](../converter/composers/record_materialisation/record_plan.md)
- [converter/resolvers/cursor_column_resolver.py](../converter/resolvers/cursor_column_resolver.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)
- [converter/transformers/cobol_transformer_line_utils.py](../converter/transformers/cobol_transformer_line_utils.md)
- [converter/transformers/idms_statement_transformer.py](../converter/transformers/idms_statement_transformer.md)
- [rules/record_materialisation_rules.py](../rules/record_materialisation_rules.md)

## Symbol contracts and control points

### `TestCobolTransformerCompRemoval` - L11-L36

```python
class TestCobolTransformerCompRemoval()
```

Data declaration cleanup must not change COBOL storage semantics.

### `TestCobolTransformerCompRemoval._transformer` - L15-L24

```python
_transformer()
```

Observed calls (lexical order): `CobolTransformer`, `Mock`, `CobolTransformerLineUtils`.

### `TestCobolTransformerCompRemoval.test_transformer_preserves_comp3_and_initialization` - L26-L28

```python
test_transformer_preserves_comp3_and_initialization(self)
```

Observed calls (lexical order): `self._transformer`, `self._transformer()._clean_data_declaration_line`.

### `TestCobolTransformerCompRemoval.test_transformer_preserves_filler_storage` - L30-L32

```python
test_transformer_preserves_filler_storage(self)
```

Observed calls (lexical order): `self._transformer`, `self._transformer()._clean_data_declaration_line`.

### `TestCobolTransformerCompRemoval.test_transformer_does_not_add_value_to_redefines` - L34-L36

```python
test_transformer_does_not_add_value_to_redefines(self)
```

Observed calls (lexical order): `self._transformer`, `self._transformer()._clean_data_declaration_line`.

### `TestRecordKeySignHandling` - L39-L64

```python
class TestRecordKeySignHandling()
```

Signed fields and packed usage must be preserved in source data.

### `TestRecordKeySignHandling._transformer` - L43-L52

```python
_transformer()
```

Observed calls (lexical order): `CobolTransformer`, `Mock`, `CobolTransformerLineUtils`.

### `TestRecordKeySignHandling.test_plain_signed_integer_preserves_sign_and_comp3` - L54-L56

```python
test_plain_signed_integer_preserves_sign_and_comp3(self)
```

Observed calls (lexical order): `self._transformer`, `self._transformer()._clean_data_declaration_line`.

### `TestRecordKeySignHandling.test_signed_decimal_preserves_sign_and_comp3` - L58-L60

```python
test_signed_decimal_preserves_sign_and_comp3(self)
```

Observed calls (lexical order): `self._transformer`, `self._transformer()._clean_data_declaration_line`.

### `TestRecordKeySignHandling.test_unsigned_integer_preserves_comp3` - L62-L64

```python
test_unsigned_integer_preserves_comp3(self)
```

Observed calls (lexical order): `self._transformer`, `self._transformer()._clean_data_declaration_line`.

### `TestComp3Removal` - L67-L153

```python
class TestComp3Removal()
```

Test removal of COMP-3 and other binary encoding from field definitions.

### `TestComp3Removal.test_picture_strips_comp3_from_usage` - L70-L88

```python
test_picture_strips_comp3_from_usage(self)
```

COMP-3 should be stripped from PIC clause.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `TestComp3Removal.test_picture_strips_computational_3` - L90-L105

```python
test_picture_strips_computational_3(self)
```

COMPUTATIONAL-3 should also be stripped.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `TestComp3Removal.test_picture_preserves_non_encoding_usage` - L107-L121

```python
test_picture_preserves_non_encoding_usage(self)
```

Non-encoding USAGE clauses (like DISPLAY) should be preserved.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `TestComp3Removal.test_picture_no_value_for_alphanumeric` - L123-L137

```python
test_picture_no_value_for_alphanumeric(self)
```

Alphanumeric fields should not get VALUE ZEROES.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `TestComp3Removal.test_picture_existing_value_preserved` - L139-L153

```python
test_picture_existing_value_preserved(self)
```

If VALUE clause already exists, don't add VALUE ZEROES.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`, `result.count`.

### `TestMaterialisedRemainderFiller` - L156-L185

```python
class TestMaterialisedRemainderFiller()
```

Complete a shorter mapped prefix without inventing mapped fields.

### `TestMaterialisedRemainderFiller.test_remainder_rule_is_enabled` - L159-L161

```python
test_remainder_rule_is_enabled(self)
```

### `TestMaterialisedRemainderFiller.test_filler_sized_from_target_and_mapping_not_program_name` - L163-L176

```python
test_filler_sized_from_target_and_mapping_not_program_name(self)
```

Observed calls (lexical order): `RecordMaterialisationPlan`, `RecordFieldPlan`, `plan.remainder_bytes`, `RecordLayoutGenerator`, `RecordLayoutGenerator().remainder_line`, `len`.

### `TestMaterialisedRemainderFiller.test_exact_fit_never_generates_filler` - L178-L185

```python
test_exact_fit_never_generates_filler(self)
```

Observed calls (lexical order): `RecordFieldPlan`, `RecordMaterialisationPlan`, `RecordLayoutGenerator`, `RecordLayoutGenerator().remainder_line`, `plan.remainder_bytes`.

### `TestSelectColumnOptimization` - L188-L264

```python
class TestSelectColumnOptimization()
```

Test SELECT statement column optimization.

### `TestSelectColumnOptimization.test_cursor_column_filtering_logic` - L191-L214

```python
test_cursor_column_filtering_logic(self)
```

Cursor should select appropriate columns.

Observed calls (lexical order): `CursorColumnResolver._without_audit_columns`.

### `TestSelectColumnOptimization.test_column_deduplication` - L216-L236

```python
test_column_deduplication(self)
```

Duplicate columns should be removed while preserving order.

Observed calls (lexical order): `CursorColumnResolver._unique`, `len`.

### `TestSelectColumnOptimization.test_unnecessary_columns_filtered` - L238-L264

```python
test_unnecessary_columns_filtered(self)
```

Filler and system metadata columns should be removed.

Observed calls (lexical order): `CursorColumnResolver._without_unnecessary_columns`.

### `TestIntegrationFixedFormat` - L267-L296

```python
class TestIntegrationFixedFormat()
```

Test COBOL fixed format compliance.

### `TestIntegrationFixedFormat.test_area_a_b_formatting` - L270-L284

```python
test_area_a_b_formatting(self)
```

Verify Area A/B column alignment.

Observed calls (lexical order): `test_line[7:11].strip`.

### `TestIntegrationFixedFormat.test_paragraph_in_area_a` - L286-L296

```python
test_paragraph_in_area_a(self)
```

Paragraph names should start at column 8 (Area A).

Observed calls (lexical order): `test_line[7:].strip`, `test_line[7:].strip().startswith`.

### `TestEndToEndConversion` - L299-L333

```python
class TestEndToEndConversion()
```

Integration tests for complete conversion pipeline.

### `TestEndToEndConversion.test_field_definition_conversion` - L302-L321

```python
test_field_definition_conversion(self)
```

Test complete field definition transformation.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `TestEndToEndConversion.test_generated_output_structure` - L323-L333

```python
test_generated_output_structure(self)
```

Verify generated output matches expected DB2 COBOL format.

### `test_picture_strips_comp3_from_usage` - L340-L358

```python
test_picture_strips_comp3_from_usage(self)
```

COMP-3 should be stripped from PIC clause.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `test_picture_strips_computational_3` - L360-L375

```python
test_picture_strips_computational_3(self)
```

COMPUTATIONAL-3 should also be stripped.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `test_picture_preserves_non_encoding_usage` - L377-L391

```python
test_picture_preserves_non_encoding_usage(self)
```

Non-encoding USAGE clauses (like DISPLAY) should be preserved.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `test_picture_no_value_for_alphanumeric` - L393-L407

```python
test_picture_no_value_for_alphanumeric(self)
```

Alphanumeric fields should not get VALUE ZEROES.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `test_picture_existing_value_preserved` - L409-L423

```python
test_picture_existing_value_preserved(self)
```

If VALUE clause already exists, don't add VALUE ZEROES.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`, `result.count`.

### `TestMaterialisedRemainderFiller` - L426-L455

```python
class TestMaterialisedRemainderFiller()
```

Complete a shorter mapped prefix without inventing mapped fields.

### `TestMaterialisedRemainderFiller.test_remainder_rule_is_enabled` - L429-L431

```python
test_remainder_rule_is_enabled(self)
```

### `TestMaterialisedRemainderFiller.test_filler_sized_from_target_and_mapping_not_program_name` - L433-L446

```python
test_filler_sized_from_target_and_mapping_not_program_name(self)
```

Observed calls (lexical order): `RecordMaterialisationPlan`, `RecordFieldPlan`, `plan.remainder_bytes`, `RecordLayoutGenerator`, `RecordLayoutGenerator().remainder_line`, `len`.

### `TestMaterialisedRemainderFiller.test_exact_fit_never_generates_filler` - L448-L455

```python
test_exact_fit_never_generates_filler(self)
```

Observed calls (lexical order): `RecordFieldPlan`, `RecordMaterialisationPlan`, `RecordLayoutGenerator`, `RecordLayoutGenerator().remainder_line`, `plan.remainder_bytes`.

### `TestSelectColumnOptimization` - L458-L534

```python
class TestSelectColumnOptimization()
```

Test SELECT statement column optimization.

### `TestSelectColumnOptimization.test_cursor_column_filtering_logic` - L461-L484

```python
test_cursor_column_filtering_logic(self)
```

Cursor should select appropriate columns.

Observed calls (lexical order): `CursorColumnResolver._without_audit_columns`.

### `TestSelectColumnOptimization.test_column_deduplication` - L486-L506

```python
test_column_deduplication(self)
```

Duplicate columns should be removed while preserving order.

Observed calls (lexical order): `CursorColumnResolver._unique`, `len`.

### `TestSelectColumnOptimization.test_unnecessary_columns_filtered` - L508-L534

```python
test_unnecessary_columns_filtered(self)
```

Filler and system metadata columns should be removed.

Observed calls (lexical order): `CursorColumnResolver._without_unnecessary_columns`.

### `TestIntegrationFixedFormat` - L537-L566

```python
class TestIntegrationFixedFormat()
```

Test COBOL fixed format compliance.

### `TestIntegrationFixedFormat.test_area_a_b_formatting` - L540-L554

```python
test_area_a_b_formatting(self)
```

Verify Area A/B column alignment.

Observed calls (lexical order): `test_line[7:11].strip`.

### `TestIntegrationFixedFormat.test_paragraph_in_area_a` - L556-L566

```python
test_paragraph_in_area_a(self)
```

Paragraph names should start at column 8 (Area A).

Observed calls (lexical order): `test_line[7:].strip`, `test_line[7:].strip().startswith`.

### `TestEndToEndConversion` - L569-L603

```python
class TestEndToEndConversion()
```

Integration tests for complete conversion pipeline.

### `TestEndToEndConversion.test_field_definition_conversion` - L572-L591

```python
test_field_definition_conversion(self)
```

Test complete field definition transformation.

Observed calls (lexical order): `Mock`, `RecordEntryRenderer.picture_of`.

### `TestEndToEndConversion.test_generated_output_structure` - L593-L603

```python
test_generated_output_structure(self)
```

Verify generated output matches expected DB2 COBOL format.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
