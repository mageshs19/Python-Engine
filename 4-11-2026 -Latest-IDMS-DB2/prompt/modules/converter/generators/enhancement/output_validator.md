# `converter/generators/enhancement/output_validator.py`

Source: [converter/generators/enhancement/output_validator.py](../../../../../converter/generators/enhancement/output_validator.py) | 186 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `e347cdf5534b4c68693f7614abe14f03bd647298a4d439bff813c1451acc7812`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`NO_GROUP_INITIALIZED` (L29), `MISSING_SCOPED_INITIALIZE` (L32), `UNRESOLVED_CURSOR` (L35), `INITIALIZE_IN_CURSOR_PARAGRAPH` (L38), `LEGACY_PARAGRAPH_PRESENT` (L41), `MISSING_TIMESTAMP` (L44), `DUPLICATE_TIMESTAMP` (L45), `__all__` (L186)

## Import declarations

```python
from __future__ import annotations
from typing import Dict, List
from converter.generators.initialization.cursor_scope_scanner import CursorScopeScanner
from converter.generators.initialization.diagnostics import InitializationDiagnostics
from converter.generators.initialization.initialize_placer import InitializePlacer
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.initialization.paragraph_index import ParagraphIndex
from patterns.initialization_scope_patterns import CURSOR_PARAGRAPH_HEADER_PATTERN, INITIALIZE_PATTERN, PERFORM_PARAGRAPH_PATTERN
from rules.initialization_placement_rules import DCLGEN_GROUP_PREFIX, STARTUP_PARAGRAPH_NAME, TIMESTAMP_PARAGRAPH_NAME
```

## Local dependency notes

- [converter/generators/initialization/cursor_scope_scanner.py](../initialization/cursor_scope_scanner.md)
- [converter/generators/initialization/diagnostics.py](../initialization/diagnostics.md)
- [converter/generators/initialization/initialize_placer.py](../initialization/initialize_placer.md)
- [converter/generators/initialization/line_geometry.py](../initialization/line_geometry.md)
- [converter/generators/initialization/paragraph_index.py](../initialization/paragraph_index.md)
- [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/converter_pipeline_integration.py](../converter_pipeline_integration.md)
- [converter/generators/enhancement/__init__.py](__init__.md)
- [converter/generators/enhancement/enhancement_pipeline.py](enhancement_pipeline.md)

## Symbol contracts and control points

### `OutputValidator` - L48-L179

```python
class OutputValidator()
```

### `OutputValidator.__init__` - L50-L56

```python
__init__(self) -> None
```

Observed calls (lexical order): `LineGeometry`, `ParagraphIndex`, `CursorScopeScanner`, `InitializePlacer`, `InitializationDiagnostics`.

### `OutputValidator.validate` - L58-L73

```python
validate(self, program_text: str) -> Dict[str, object]
```

Observed calls (lexical order): `self.geometry.split`, `str`, `self._check_groups`, `self._check_scope`, `self._check_cursor_paragraphs`, `self._check_legacy`, `self._check_timestamp`.

Control points:

- L65: `if not lines`

### `OutputValidator._check_groups` - L75-L79

```python
_check_groups(self, lines: List[str], result: Dict) -> None
```

Observed calls (lexical order): `self._initialized_groups`, `result['issues'].append`.

Control points:

- L76: `if self._initialized_groups(lines)`

### `OutputValidator._check_scope` - L81-L96

```python
_check_scope(self, lines: List[str], result: Dict) -> None
```

Observed calls (lexical order): `self.scanner.open_sites`, `result['warnings'].append`, `UNRESOLVED_CURSOR.format`, `self.placer.already_placed`, `result['issues'].append`, `MISSING_SCOPED_INITIALIZE.format`.

Control points:

- L82: `for site in self.scanner.open_sites(lines)`
- L83: `if not site.is_resolved`
- L88: `if self.placer.already_placed(lines, site)`

### `OutputValidator._check_cursor_paragraphs` - L98-L115

```python
_check_cursor_paragraphs(self, lines: List[str], result: Dict) -> None
```

Observed calls (lexical order): `enumerate`, `self.paragraphs.is_paragraph_header`, `self.geometry.body`, `CURSOR_PARAGRAPH_HEADER_PATTERN.match`, `self.paragraphs.span_of`, `self._has_group_initialize`, `result['warnings'].append`, `INITIALIZE_IN_CURSOR_PARAGRAPH.format`, `body.rstrip`.

Control points:

- L103: `for (index, line) in enumerate(lines)`
- L104: `if not self.paragraphs.is_paragraph_header(line)`
- L107: `if not CURSOR_PARAGRAPH_HEADER_PATTERN.match(body)`
- L110: `if self._has_group_initialize(lines, start, end)`

### `OutputValidator._check_legacy` - L117-L124

```python
_check_legacy(self, lines: List[str], result: Dict) -> None
```

Observed calls (lexical order): `self.paragraphs.header_index`, `result['warnings'].append`, `LEGACY_PARAGRAPH_PRESENT.format`.

Control points:

- L118: `if self.paragraphs.header_index(lines, STARTUP_PARAGRAPH_NAME) < 0`

### `OutputValidator._check_timestamp` - L126-L139

```python
_check_timestamp(self, lines: List[str], result: Dict) -> None
```

Observed calls (lexical order): `self.paragraphs.header_index`, `result['warnings'].append`, `MISSING_TIMESTAMP.format`, `self._perform_count`, `DUPLICATE_TIMESTAMP.format`.

Control points:

- L127: `if self.paragraphs.header_index(lines, TIMESTAMP_PARAGRAPH_NAME) < 0`
- L133: `if count > 1`

### `OutputValidator._initialized_groups` - L141-L152

```python
_initialized_groups(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `self.geometry.is_comment_or_blank`, `INITIALIZE_PATTERN.match`, `self.geometry.body`, `match.group`, `match.group('group').upper`, `group.startswith`, `out.append`.

Control points:

- L143: `for line in lines`
- L144: `if self.geometry.is_comment_or_blank(line)`
- L147: `if not match`
- L150: `if group.startswith(DCLGEN_GROUP_PREFIX)`

### `OutputValidator._has_group_initialize` - L154-L168

```python
_has_group_initialize(self, lines: List[str], start: int, end: int) -> bool
```

Observed calls (lexical order): `range`, `self.geometry.is_comment_or_blank`, `INITIALIZE_PATTERN.match`, `self.geometry.body`, `match.group`, `match.group('group').upper`, `match.group('group').upper().startswith`.

Control points:

- L160: `for index in range(start + 1, end + 1)`
- L161: `if self.geometry.is_comment_or_blank(lines[index])`
- L164: `if match and match.group('group').upper().startswith(DCLGEN_GROUP_PREFIX)`

### `OutputValidator._perform_count` - L170-L179

```python
_perform_count(self, lines: List[str], name: str) -> int
```

Observed calls (lexical order): `str`, `str(name or '').upper`, `self.geometry.is_comment_or_blank`, `PERFORM_PARAGRAPH_PATTERN.match`, `self.geometry.body`, `match.group`, `match.group('paragraph').upper`.

Control points:

- L173: `for line in lines`
- L174: `if self.geometry.is_comment_or_blank(line)`
- L177: `if match and match.group('paragraph').upper() == target`

### `validate_output` - L182-L183

```python
validate_output(program_text: str) -> Dict[str, object]
```

Observed calls (lexical order): `OutputValidator`, `OutputValidator().validate`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
