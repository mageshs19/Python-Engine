# `converter/composers/db2_date_comparison_composer.py`

Source: [converter/composers/db2_date_comparison_composer.py](../../../../converter/composers/db2_date_comparison_composer.py) | 162 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `7bf67f795fa5e9ec70a1dd7e61736ddce8df56a2eeaac8d620161fd147876820`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date comparison composer.

## Module-level bindings

`__all__` (L162)

## Import declarations

```python
from __future__ import annotations
from converter.composers.db2_date_comparison_rewriter import Db2DateComparisonRewriter
from converter.composers.db2_date_condition_assembler import Db2DateConditionAssembler
from converter.composers.db2_date_field_detector import Db2DateFieldDetector
from converter.composers.db2_date_line_utils import Db2DateLineUtils
from converter.composers.db2_date_working_storage_manager import Db2DateWorkingStorageManager
from rules.db2_date_conversion_rules import DB2_DATE_COMPARISON_WS_MARKER, DB2_DATE_MESSAGES, ENFORCE_DATE_COMPARISON_CONVERSION
```

## Local dependency notes

- [converter/composers/db2_date_comparison_rewriter.py](db2_date_comparison_rewriter.md)
- [converter/composers/db2_date_condition_assembler.py](db2_date_condition_assembler.md)
- [converter/composers/db2_date_field_detector.py](db2_date_field_detector.md)
- [converter/composers/db2_date_line_utils.py](db2_date_line_utils.md)
- [converter/composers/db2_date_working_storage_manager.py](db2_date_working_storage_manager.md)
- [rules/db2_date_conversion_rules.py](../../rules/db2_date_conversion_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_db2_date_comparison.py](../../tests/test_db2_date_comparison.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)

## Symbol contracts and control points

### `Db2DateComparisonComposer` - L66-L159

```python
class Db2DateComparisonComposer()
```

Declares date helpers and converts every DATE host comparison.

Declared class/data-model fields:

```python
WS_MARKER = DB2_DATE_COMPARISON_WS_MARKER
```

### `Db2DateComparisonComposer.__init__` - L71-L90

```python
__init__(self) -> None
```

Observed calls (lexical order): `Db2DateLineUtils`, `Db2DateConditionAssembler`, `Db2DateFieldDetector`, `Db2DateWorkingStorageManager`, `Db2DateComparisonRewriter`.

### `Db2DateComparisonComposer.compose` - L95-L146

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `self.line_utils.normalize_line_endings`, `self.line_utils.normalize_line_endings(text).splitlines`, `self.field_detector.date_fields_used_in_comparisons`, `self.field_detector.shared_date_helpers_used_in_procedure`, `self.messages.append`, `'\n'.join`, `'\n'.join(lines).rstrip`, `self.working_storage_manager.ensure_date_working_storage`, `DB2_DATE_MESSAGES['helpers_declared'].format`, `len`, `self.comparison_rewriter.rewrite_date_comparisons`, `self._rewriter_messages`, `self.messages.extend`.

Control points:

- L98: `if not text`
- L101: `if not ENFORCE_DATE_COMPARISON_CONVERSION`
- L106: `if not lines`
- L119: `if not date_fields and (not shared_helpers_used)`
- L126: `if date_fields or shared_helpers_used`
- L132: `if date_fields`
- L142: `if date_fields`

### `Db2DateComparisonComposer._rewriter_messages` - L151-L159

```python
_rewriter_messages(self) -> list[str]
```

Drain the rewriter's diagnostics, blank entries removed.

Observed calls (lexical order): `getattr`, `str`, `str(message or '').strip`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
