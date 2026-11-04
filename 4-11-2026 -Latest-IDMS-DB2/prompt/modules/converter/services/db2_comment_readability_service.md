# `converter/services/db2_comment_readability_service.py`

Source: [converter/services/db2_comment_readability_service.py](../../../../converter/services/db2_comment_readability_service.py) | 149 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `a8dfc99bedf8342c0562044e5e78398ebc44cb7e3877019a55e19557711e7e0f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 comment readability service.

## Import declarations

```python
from __future__ import annotations
from patterns.final_feedback_fix_patterns import DB2_COLON_COMMENT_BODY_PATTERN, DB2_SPACE_COMMENT_BODY_PATTERN
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)

## Symbol contracts and control points

### `Db2CommentReadabilityService` - L19-L149

```python
class Db2CommentReadabilityService()
```

### `Db2CommentReadabilityService.__init__` - L20-L24

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `Db2CommentReadabilityService.apply` - L26-L131

```python
apply(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`, `output.append`, `self.fixed_format.is_fixed_line`, `self.fixed_format.split`, `str(body or '').rstrip`, `str(body or '').rstrip().strip`, `bool`, `DB2_COLON_COMMENT_BODY_PATTERN.match`, `DB2_SPACE_COMMENT_BODY_PATTERN.match`, `DB2_COLON_COMMENT_BODY_PATTERN.sub`, `DB2_COLON_COMMENT_BODY_PATTERN.sub('DB2:', clean_body, count=1).strip`, `self._try_build_fixed_comment_line`, `DB2_SPACE_COMMENT_BODY_PATTERN.sub`, `DB2_SPACE_COMMENT_BODY_PATTERN.sub('DB2 ', clean_body, count=1).strip`, `str(line or '').strip`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L27: `if not text`
- L34: `for line in lines`
- L35: `if not line`
- L40: `if self.fixed_format.is_fixed_line(line)`
- L43: `if indicator != '*'`
- L50: `if not clean_body`
- L62: `if is_colon`
- L73: `if is_space`
- Another 5 conditions/loops exist in this source span.

### `Db2CommentReadabilityService._try_build_fixed_comment_line` - L133-L149

```python
_try_build_fixed_comment_line(self, left: str, right: str, comment_body: str) -> str
```

Observed calls (lexical order): `str`, `str(comment_body or '').strip`, `len`, `self.fixed_format.build`.

Control points:

- L141: `if not clean_body`
- L146: `if len(body) > self.fixed_format.BODY_WIDTH`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
