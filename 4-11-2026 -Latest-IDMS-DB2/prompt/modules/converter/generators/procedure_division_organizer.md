# `converter/generators/procedure_division_organizer.py`

Source: [converter/generators/procedure_division_organizer.py](../../../../converter/generators/procedure_division_organizer.py) | 212 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `717fb6f18e0f94016e7cff50c4caaa064b91de2bfce6115c78e63a9806bc42a5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> PROCEDURE DIVISION ORGANIZER

## Import declarations

```python
import re
from typing import List, Tuple, Optional, Dict, Set
from dataclasses import dataclass
from patterns.cobol_patterns import PARAGRAPH_PATTERN, PROCEDURE_DIVISION_PATTERN
```

## Local dependency notes

- [patterns/cobol_patterns.py](../../patterns/cobol_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_procedure_division_organizer_safety.py](../../tests/test_procedure_division_organizer_safety.md)

## Symbol contracts and control points

### `Paragraph` - L58-L67

```python
class Paragraph()
```

Represents a COBOL paragraph.

Declared class/data-model fields:

```python
name: str
number: str
content: str
start_pos: int
end_pos: int
```

### `Paragraph.__repr__` - L66-L67

```python
__repr__(self)
```

### `ProcedureDivisionOrganizer` - L70-L195

```python
class ProcedureDivisionOrganizer()
```

Organizes PROCEDURE DIVISION with standard flow.

Declared class/data-model fields:

```python
TIMESTAMP_PARAGRAPH_TEMPLATE = '600-GET-TIMESTAMP.\n *DB2: Generic timestamp capture (same in all programs)\n MOVE FUNCTION CURRENT-DATE TO TS-SYSTEM.\n MOVE CC OF TS-SYSTEM TO CC OF TS-TIMESTAMP.\n MOVE YY OF TS-SYSTEM TO YY OF TS-TIMESTAMP.\n MOVE MM OF TS-SYSTEM TO MM OF TS-TIMESTAMP.\n MOVE D...
DISPLAY_TOTALS_TEMPLATE = "500-DISPLAY-TOTALS.\n *DB2: Display audit information and counters\n PERFORM 600-GET-TIMESTAMP.\n DISPLAY 'Program ended at : ' TS-TIMESTAMP.\n DISPLAY 'TOTAL RECORDS PROCESSED: TBD'.\n ."
PARAGRAPH_NUM_PATTERN = re.compile('^(\\d{3,6})-', re.MULTILINE)
STOP_RUN_PATTERN = re.compile('^\\s*STOP\\s+RUN\\s*\\.', re.IGNORECASE | re.MULTILINE)
PERFORM_PATTERN = re.compile('PERFORM\\s+(\\d{3,6}-\\w+)', re.IGNORECASE)
OPEN_CURSOR_PATTERN = re.compile('^(\\d{3,6})-\\w*OPEN', re.IGNORECASE | re.MULTILINE)
FETCH_CURSOR_PATTERN = re.compile('^(\\d{3,6})-\\w*FETCH', re.IGNORECASE | re.MULTILINE)
CLOSE_CURSOR_PATTERN = re.compile('^(\\d{3,6})-\\w*CLOSE', re.IGNORECASE | re.MULTILINE)
```

### `ProcedureDivisionOrganizer.__init__` - L104-L110

```python
__init__(self, program_text: str)
```

Initialize with program text.

### `ProcedureDivisionOrganizer.organize` - L112-L136

```python
organize(self) -> str
```

Organize PROCEDURE DIVISION with standard flow.

Observed calls (lexical order): `PROCEDURE_DIVISION_PATTERN.search`, `proc_match.end`, `self._extract_paragraphs`, `self._build_organized_structure`.

Control points:

- L122: `if not proc_match`

### `ProcedureDivisionOrganizer._extract_paragraphs` - L138-L175

```python
_extract_paragraphs(self)
```

Extract all paragraphs from PROCEDURE DIVISION.

Observed calls (lexical order): `PARAGRAPH_PATTERN.finditer`, `match.group`, `self.PARAGRAPH_NUM_PATTERN.match`, `num_match.group`, `para_starts.append`, `match.start`, `enumerate`, `len`, `Paragraph`, `self.paragraphs.append`.

Control points:

- L145: `for match in PARAGRAPH_PATTERN.finditer(text_after_pd)`
- L159: `for (i, para_info) in enumerate(para_starts)`
- L160: `if i + 1 < len(para_starts)`

### `ProcedureDivisionOrganizer._build_organized_structure` - L177-L195

```python
_build_organized_structure(self) -> str
```

Keep source control flow intact instead of fabricating a template.

Observed calls (lexical order): `self.messages.append`.

### `organize_procedure_division` - L198-L212

```python
organize_procedure_division(program_text: str) -> str
```

Convenience function to organize PROCEDURE DIVISION.

Observed calls (lexical order): `ProcedureDivisionOrganizer`, `organizer.organize`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
