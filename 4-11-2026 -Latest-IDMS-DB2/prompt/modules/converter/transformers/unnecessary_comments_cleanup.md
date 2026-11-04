# `converter/transformers/unnecessary_comments_cleanup.py`

Source: [converter/transformers/unnecessary_comments_cleanup.py](../../../../converter/transformers/unnecessary_comments_cleanup.py) | 295 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `9a59ebafcd225399b57773ecc6f90a4e762ce56828970898f2aefdb7bdcebc3b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Remove unnecessary comment blocks from generated COBOL programs.

## Module-level bindings

`__all__` (L295)

## Import declarations

```python
from __future__ import annotations
import re
from typing import Optional
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/unnecessary_comments_cleanup_composer.py](../composers/unnecessary_comments_cleanup_composer.md)

## Symbol contracts and control points

### `UnnecessaryCommentsCleanup` - L61-L292

```python
class UnnecessaryCommentsCleanup()
```

Remove comment blocks that don't contribute to code understanding.

Declared class/data-model fields:

```python
NO_DB2_PATTERN = re.compile('^\\s*\\*\\s*(?:[-\\w]+\\s*)?(?:no DB2|no columnas?|not found|manual)', flags=re.IGNORECASE | re.MULTILINE)
FRENCH_RESTART_PATTERN = re.compile('^\\s*\\*\\s*(?:RESTART|SI EXISTE|SINON|RECHERCHE)', flags=re.IGNORECASE | re.MULTILINE)
COMMENTED_CODE_BLOCK_PATTERN = re.compile('^\\s*\\*\\s*(?:IF|MOVE|PERFORM|ADD|DO|END-IF|ELSE|UNTIL)', flags=re.IGNORECASE | re.MULTILINE)
DB2_KEEP_PATTERN = re.compile('^\\s*(?:\\d{6})?\\s*\\*\\s*DB2-KEEP', flags=re.IGNORECASE | re.MULTILINE)
KEPT_BLOCK_MESSAGE = 'Kept comment block at lines {start}-{end}; it carries a DB2-KEEP marker and is a decision record, not noise.'
```

### `UnnecessaryCommentsCleanup.__init__` - L96-L97

```python
__init__(self) -> None
```

### `UnnecessaryCommentsCleanup.apply` - L99-L109

```python
apply(self, cobol_text: str) -> tuple[str, list[str]]
```

Remove unnecessary comment blocks from COBOL text.

Observed calls (lexical order): `str`, `self._remove_unnecessary_comment_blocks`.

Control points:

- L104: `if not text`

### `UnnecessaryCommentsCleanup._remove_unnecessary_comment_blocks` - L111-L163

```python
_remove_unnecessary_comment_blocks(self, text: str) -> str
```

Remove comment blocks that don't add value.

Observed calls (lexical order): `text.split`, `len`, `self._is_comment_line`, `block_lines.append`, `self._block_has_keep_marker`, `result.extend`, `self.messages.append`, `self.KEPT_BLOCK_MESSAGE.format`, `self._should_remove_comment_block`, `result.append`, `'\n'.join`.

Control points:

- L117: `while i < len(lines)`
- L121: `if self._is_comment_line(line)`
- L130: `while j < len(lines) and self._is_comment_line(lines[j])`
- L136: `if self._block_has_keep_marker(block_lines)`
- L138: `if len(block_lines) > 1`
- L148: `if self._should_remove_comment_block(block_lines, lines, j)`

### `UnnecessaryCommentsCleanup._block_has_keep_marker` - L165-L169

```python
_block_has_keep_marker(self, block_lines: list[str]) -> bool
```

True when any line in the block is a keep marker.

Observed calls (lexical order): `any`, `self.DB2_KEEP_PATTERN.search`.

### `UnnecessaryCommentsCleanup._is_comment_line` - L171-L195

```python
_is_comment_line(self, line: str) -> bool
```

Check if line is a pure comment line.

Observed calls (lexical order): `len`, `line.lstrip`, `stripped.startswith`.

Control points:

- L179: `if not line or len(line) < 1`
- L183: `if len(line) >= 7 and line[6] == '*'`
- L187: `if line[0] == '*'`
- L192: `if stripped.startswith('*')`

### `UnnecessaryCommentsCleanup._should_remove_comment_block` - L197-L235

```python
_should_remove_comment_block(self, block_lines: list[str], all_lines: list[str], block_end: int) -> bool
```

Determine if a comment block should be removed.

Observed calls (lexical order): `'\n'.join`, `'\n'.join(block_lines).lower`, `len`, `self._is_all_commented_code_description`, `self._is_pure_structure_comment`, `self._is_block_of_commented_code`.

Control points:

- L210: `if 'no db2' in block_text or 'map manually' in block_text`
- L214: `if 'restart' in block_text and 'recherche' in block_text and ('si existe' in block_text)`
- L222: `if len(block_lines) > 2 and self._is_all_commented_code_description(block_lines, all_lines, block_end)`
- L228: `if len(block_lines) > 3 and self._is_pure_structure_comment(block_text)`
- L232: `if self._is_block_of_commented_code(block_lines)`

### `UnnecessaryCommentsCleanup._is_block_of_commented_code` - L237-L263

```python
_is_block_of_commented_code(self, block_lines: list[str]) -> bool
```

Check if block consists entirely of commented-out code statements.

Observed calls (lexical order): `len`, `line.lower`, `any`.

Control points:

- L239: `if len(block_lines) < 2`
- L243: `for line in block_lines`
- L246: `if any((kw in line_lower for kw in ['* move ', '* if ', '* perform ', '* add ', '* until ', '* else', '* end-if', '* move ', '* if ', '* perform ']))`

### `UnnecessaryCommentsCleanup._is_all_commented_code_description` - L265-L286

```python
_is_all_commented_code_description(self, block_lines: list[str], all_lines: list[str], block_end: int) -> bool
```

Check if block only describes commented-out code that follows.

Observed calls (lexical order): `len`, `all_lines[next_idx].strip`, `self._is_comment_line`.

Control points:

- L270: `if block_end >= len(all_lines)`
- L275: `while next_idx < len(all_lines) and (not all_lines[next_idx].strip())`
- L278: `if next_idx >= len(all_lines)`
- L283: `if self._is_comment_line(next_line)`

### `UnnecessaryCommentsCleanup._is_pure_structure_comment` - L288-L292

```python
_is_pure_structure_comment(self, text: str) -> bool
```

Check if comment is just describing structure.

Observed calls (lexical order): `sum`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
