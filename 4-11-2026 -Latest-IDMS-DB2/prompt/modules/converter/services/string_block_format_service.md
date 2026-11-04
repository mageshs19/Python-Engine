# `converter/services/string_block_format_service.py`

Source: [converter/services/string_block_format_service.py](../../../../converter/services/string_block_format_service.py) | 106 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `59bdde4254033695fecf870f310adab0498b69e34e0a74c2225c75cb61eaf8a1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> STRING block format service.

## Import declarations

```python
from __future__ import annotations
from patterns.final_feedback_fix_patterns import STRING_END_PATTERN, STRING_INTO_PATTERN, STRING_START_PATTERN
from rules.final_feedback_fix_rules import FINAL_FIX_STRING_CONTINUATION_BODY_INDENT, FINAL_FIX_STRING_INTO_BODY_INDENT, FINAL_FIX_STRING_START_BODY_INDENT
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/final_feedback_fix_rules.py](../../rules/final_feedback_fix_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)

## Symbol contracts and control points

### `StringBlockFormatService` - L25-L106

```python
class StringBlockFormatService()
```

### `StringBlockFormatService.__init__` - L26-L30

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `StringBlockFormatService.apply` - L32-L95

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `self.fixed_format.logical`, `str(logical or '').strip`, `output.append`, `self.fixed_format.is_comment_or_control_line`, `STRING_START_PATTERN.match`, `self._replace_body_when_fits`, `STRING_END_PATTERN.match`, `STRING_INTO_PATTERN.match`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L33: `if not text`
- L40: `for line in lines`
- L44: `if not stripped`
- L48: `if self.fixed_format.is_comment_or_control_line(line)`
- L52: `if STRING_START_PATTERN.match(stripped)`
- L62: `if inside_string and STRING_END_PATTERN.match(stripped)`
- L72: `if inside_string and STRING_INTO_PATTERN.match(stripped)`
- L81: `if inside_string`

### `StringBlockFormatService._replace_body_when_fits` - L97-L106

```python
_replace_body_when_fits(self, line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `self.fixed_format.is_fixed_line`, `len`, `self.fixed_format.replace_body`.

Control points:

- L100: `if not self.fixed_format.is_fixed_line(line)`
- L103: `if len(clean_body) > self.fixed_format.BODY_WIDTH`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
