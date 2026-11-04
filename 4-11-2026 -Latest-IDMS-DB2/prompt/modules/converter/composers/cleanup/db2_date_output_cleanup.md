# `converter/composers/cleanup/db2_date_output_cleanup.py`

Source: [converter/composers/cleanup/db2_date_output_cleanup.py](../../../../../converter/composers/cleanup/db2_date_output_cleanup.py) | 388 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `8cc4b2a707caf3bf1aa040521949b3995c7584e2cad401ad54be80f0dd5567d4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 date output cleanup.

## Module-level bindings

`NOT_FOUND` (L107), `DB2_DATE_HOST_PREFIXES` (L109), `OUTPUT_DATE_FIELD_PREFIXES` (L110), `MOVE_VERB` (L119), `BLANKING_MOVE_SOURCES` (L120), `__all__` (L388)

## Import declarations

```python
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.cobol_cleanup_line_utils import CobolCleanupLineUtils
from converter.services.name_normalizer import NameNormalizer
from patterns.cobol_cleanup_patterns import DB2_DATE_MOVE_ONE_LINE_PATTERN
from rules.cobol_cleanup_rules import STATEMENT_CONTINUATION_TOKENS
from rules.db2_output_date_conversion_rules import DB2_OUTPUT_DATE_CONVERSION_LINE_TEMPLATES, DB2_OUTPUT_DATE_HIGH_NUMERIC_LITERAL, DB2_OUTPUT_DATE_HIGH_VALUE_LITERAL, DB2_OUTPUT_DATE_LOW_VALUE_LITERAL, EMIT_OUTPUT_FIELD_BLANKING_MOVE
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup_message_collector.md)
- [converter/composers/cleanup/cobol_cleanup_line_utils.py](cobol_cleanup_line_utils.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [patterns/cobol_cleanup_patterns.py](../../../patterns/cobol_cleanup_patterns.md)
- [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.md)
- [rules/db2_output_date_conversion_rules.py](../../../rules/db2_output_date_conversion_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [converter/composers/late_db2_date_composer.py](../late_db2_date_composer.md)

## Symbol contracts and control points

### `Db2DateOutputCleanup` - L123-L385

```python
class Db2DateOutputCleanup()
```

### `Db2DateOutputCleanup.__init__` - L124-L130

```python
__init__(self, messages: CleanupMessageCollector, line_utils: CobolCleanupLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolCleanupLineUtils`.

### `Db2DateOutputCleanup._logical` - L132-L133

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`.

### `Db2DateOutputCleanup._leading_spaces` - L135-L136

```python
_leading_spaces(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.leading_spaces`.

### `Db2DateOutputCleanup._is_comment_or_blank` - L138-L139

```python
_is_comment_or_blank(self, logical: str) -> bool
```

Observed calls (lexical order): `self.line_utils.is_comment_or_blank`.

### `Db2DateOutputCleanup.convert_db2_date_moves_to_output_dates` - L144-L184

```python
convert_db2_date_moves_to_output_dates(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `self._logical_statements`, `DB2_DATE_MOVE_ONE_LINE_PATTERN.match`, `self._date_conversion_lines`, `self._leading_spaces`, `match.group`, `output.extend`, `self.messages.add`, `self._report`, `len`.

Control points:

- L151: `for (statement, first, last) in self._logical_statements(lines)`
- L152: `if statement`
- L155: `if match`
- L165: `if block`
- L172: `if suppressed`

### `Db2DateOutputCleanup._report` - L189-L220

```python
_report(self, text: str, output: list[str], converted: int, candidates: int, examined: int) -> str
```

Report exactly one of three outcomes and return the result.

Observed calls (lexical order): `self.messages.add`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L202: `if converted`
- L206: `if candidates`

### `Db2DateOutputCleanup._logical_statements` - L225-L255

```python
_logical_statements(self, lines: list[str])
```

Yield (statement_text, first_index, last_index) in source order.

Observed calls (lexical order): `enumerate`, `self._logical`, `self._is_comment_or_blank`, `f'{buffer} {logical}'.strip`, `self._is_complete`, `len`.

Control points:

- L235: `for (index, line) in enumerate(lines)`
- L238: `if not logical or self._is_comment_or_blank(logical)`
- L239: `if first >= 0`
- L245: `if first < 0`
- L250: `if self._is_complete(buffer)`
- L254: `if first >= 0`

### `Db2DateOutputCleanup._is_complete` - L258-L273

```python
_is_complete(buffer: str) -> bool
```

False while the statement ends on a continuation token.

Observed calls (lexical order): `str`, `str(buffer or '').rstrip`, `text.endswith`, `text.split`, `text.split()[-1].upper`, `text.split()[-1].upper().rstrip`.

Control points:

- L266: `if not text`
- L269: `if text.endswith(',')`

### `Db2DateOutputCleanup._should_generate_output_date_conversion` - L278-L309

```python
_should_generate_output_date_conversion(self, field_name: str, target_name: str) -> bool
```

True only for a DB2 date host moved to an output date field.

Observed calls (lexical order): `str`, `str(field_name or '').strip`, `str(field_name or '').strip().upper`, `str(target_name or '').strip`, `str(target_name or '').strip().upper`, `field.startswith`, `target.startswith`.

Control points:

- L294: `if not field or not target`
- L297: `if not field.startswith(DB2_DATE_HOST_PREFIXES)`
- L300: `if not target.startswith(OUTPUT_DATE_FIELD_PREFIXES)`
- L303: `if ' OF DCL' in target`
- L306: `if target.startswith('DCL')`

### `Db2DateOutputCleanup._is_blanking_move` - L312-L334

```python
_is_blanking_move(line: str) -> bool
```

True for "MOVE SPACES TO ...", on the RENDERED line.

Observed calls (lexical order): `str`, `str(line or '').split`, `len`, `words[0].upper`, `words[1].upper`, `f'{words[1]} {words[2]}'.upper`.

Control points:

- L322: `if len(words) < 2 or words[0].upper() != MOVE_VERB`
- L326: `if source in BLANKING_MOVE_SOURCES`
- L330: `if len(words) >= 3`

### `Db2DateOutputCleanup._date_conversion_lines` - L339-L385

```python
_date_conversion_lines(self, leading: str, field: str, group: str, target: str) -> tuple[list[str], int]
```

Render the block. Returns (lines, suppressed_count).

Observed calls (lexical order): `NameNormalizer.to_cobol`, `self._should_generate_output_date_conversion`, `template.format`, `line.strip`, `self._is_blanking_move`, `line.rstrip`, `output.append`.

Control points:

- L355: `if not self._should_generate_output_date_conversion(field_name=field_name, target_name=target_name)`
- L364: `for template in DB2_OUTPUT_DATE_CONVERSION_LINE_TEMPLATES`
- L375: `if not line.strip()`
- L378: `if not EMIT_OUTPUT_FIELD_BLANKING_MOVE and self._is_blanking_move(line.strip())`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
