# `converter/generators/working_storage_organizer.py`

Source: [converter/generators/working_storage_organizer.py](../../../../converter/generators/working_storage_organizer.py) | 352 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `fa596e6c81f252b3682546906d74211199a8aad490d946b179558f76c142b71b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> WORKING-STORAGE ORGANIZER

## Import declarations

```python
import re
from typing import List, Dict, Set, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
```

## Symbol contracts and control points

### `SectionType` - L37-L48

```python
class SectionType(Enum)
```

Types of WORKING-STORAGE sections.

Declared class/data-model fields:

```python
CONTROL_FIELDS = 1
COUNTER_FIELDS = 2
TIMESTAMP_FIELDS = 3
DATUMVELDEN = 4
DATE_HELPERS = 5
FLAGS = 6
WORK_FIELDS = 7
PARAMETERS = 8
IMPORTS = 9
DCLGEN = 10
```

### `Declaration` - L52-L60

```python
class Declaration()
```

Represents a WORKING-STORAGE declaration.

Declared class/data-model fields:

```python
type: SectionType
content: str
level: int
name: str
```

### `Declaration.__repr__` - L59-L60

```python
__repr__(self)
```

### `WorkingStorageOrganizer` - L63-L335

```python
class WorkingStorageOrganizer()
```

Reorganizes WORKING-STORAGE into standard sections.

Declared class/data-model fields:

```python
SECTION_HEADERS = {SectionType.CONTROL_FIELDS: '*-------- 1. CONTROL FIELDS --------*', SectionType.COUNTER_FIELDS: '*-------- 2. COUNTER FIELDS (Audit) --------*', SectionType.TIMESTAMP_FIELDS: '*-------- 3. TIMESTAMP FIELDS --------*', SectionType.DATUMVELDEN: '*-------- 4. DATE CONVERSION WORK...
SECTION_ORDER = [SectionType.CONTROL_FIELDS, SectionType.COUNTER_FIELDS, SectionType.TIMESTAMP_FIELDS, SectionType.DATUMVELDEN, SectionType.DATE_HELPERS, SectionType.FLAGS, SectionType.WORK_FIELDS, SectionType.PARAMETERS, SectionType.IMPORTS, SectionType.DCLGEN]
WORKING_STORAGE_SECTION = re.compile('WORKING-STORAGE\\s+SECTION\\s*\\.', re.IGNORECASE)
PROCEDURE_DIVISION_PATTERN = re.compile('PROCEDURE\\s+DIVISION\\s*(?:USING.*?)?\\.', re.IGNORECASE | re.DOTALL)
LEVEL_01_PATTERN = re.compile('^\\s*(?:001\\s+)?01\\s+(?P<name>\\w+)', re.IGNORECASE | re.MULTILINE)
COPY_PATTERN = re.compile('^\\s*COPY\\s+\\w+', re.IGNORECASE | re.MULTILINE)
EXEC_SQL_INCLUDE_PATTERN = re.compile('EXEC\\s+SQL\\s+INCLUDE\\s+\\w+\\s+END-EXEC', re.IGNORECASE)
```

### `WorkingStorageOrganizer.__init__` - L118-L121

```python
__init__(self, program_text: str)
```

Initialize with program text.

### `WorkingStorageOrganizer.reorganize` - L123-L144

```python
reorganize(self) -> str
```

Reorganize WORKING-STORAGE into standard sections.

Observed calls (lexical order): `self._extract_working_storage`, `self._categorize_declarations`, `self._generate_organized_sections`, `self._replace_working_storage`.

Control points:

- L132: `if not ws_content`

### `WorkingStorageOrganizer._extract_working_storage` - L146-L164

```python
_extract_working_storage(self) -> Optional[str]
```

Extract WORKING-STORAGE section content.

Observed calls (lexical order): `self.WORKING_STORAGE_SECTION.search`, `ws_match.end`, `self.PROCEDURE_DIVISION_PATTERN.search`, `proc_match.start`, `len`.

Control points:

- L149: `if not ws_match`
- L159: `if proc_match`

### `WorkingStorageOrganizer._categorize_declarations` - L166-L214

```python
_categorize_declarations(self, ws_content: str)
```

Parse and categorize all declarations in WORKING-STORAGE.

Observed calls (lexical order): `ws_content.split`, `line.strip`, `line.strip().startswith`, `current_group.append`, `standalone_fields.append`, `re.match`, `self._categorize_group`, `self._categorize_standalone_fields`, `self.COPY_PATTERN.match`, `self.sections[SectionType.IMPORTS].append`, `self.EXEC_SQL_INCLUDE_PATTERN.search`, `self.sections[SectionType.DCLGEN].append`.

Control points:

- L177: `for line in lines`
- L179: `if not line.strip() or line.strip().startswith('*')`
- L180: `if current_group`
- L182: `if standalone_fields`
- L187: `if re.match('\\s*01\\s+', line)`
- L188: `if current_group`
- L190: `if standalone_fields`
- L195: `if re.match('\\s*(05|10|15|20|25|30)\\s+', line) and (not current_group)`
- Another 7 conditions/loops exist in this source span.

### `WorkingStorageOrganizer._categorize_group` - L216-L260

```python
_categorize_group(self, group_lines: List[str])
```

Categorize a group based on its structure and field names.

Observed calls (lexical order): `re.search`, `name_match.group`, `name_match.group(1).upper`, `'\n'.join`, `any`, `self.sections[section_type].append`.

Control points:

- L229: `if not group_lines`
- L235: `if not name_match`
- L242: `if any((kw in group_name for kw in ['COUNTER', 'COUNT']))`
- L244: `if any((kw in group_name for kw in ['TIMESTAMP', 'TS-']))`
- L246: `if 'DATUM' in group_name`
- L248: `if 'HELPER' in group_name or 'HELP-' in group_name`
- L250: `if 'CS-PROGRAM' in group_content`
- L252: `if any((kw in group_name for kw in ['STATUS', 'FLAG', 'SWITCH']))`
- Another 1 conditions/loops exist in this source span.

### `WorkingStorageOrganizer._categorize_standalone_fields` - L262-L291

```python
_categorize_standalone_fields(self, field_lines: List[str])
```

Categorize standalone level declarations (not in a 01 group).

Observed calls (lexical order): `'\n'.join`, `any`, `self.sections[section_type].append`.

Control points:

- L272: `if not field_lines`
- L279: `if any((kw in field_content for kw in ['COUNTER', 'COUNT', 'WS-NB', 'TOTAL']))`
- L281: `if any((kw in field_content for kw in ['TIMESTAMP', 'TS-']))`
- L283: `if any((kw in field_content for kw in ['DATUM', 'DATE']))`
- L285: `if any((kw in field_content for kw in ['STATUS', 'FLAG', 'SWITCH']))`

### `WorkingStorageOrganizer._generate_organized_sections` - L293-L310

```python
_generate_organized_sections(self) -> str
```

Generate reorganized WORKING-STORAGE section.

Observed calls (lexical order): `output_lines.append`, `'\n'.join`.

Control points:

- L297: `for section_type in self.SECTION_ORDER`
- L298: `if self.sections[section_type]`
- L304: `for declaration in self.sections[section_type]`

### `WorkingStorageOrganizer._replace_working_storage` - L312-L335

```python
_replace_working_storage(self, organized_ws: str) -> str
```

Replace original WORKING-STORAGE with organized version.

Observed calls (lexical order): `self.WORKING_STORAGE_SECTION.search`, `ws_match.start`, `self.PROCEDURE_DIVISION_PATTERN.search`, `end_match.start`, `len`.

Control points:

- L315: `if not ws_match`
- L325: `if end_match`

### `organize_working_storage` - L338-L352

```python
organize_working_storage(program_text: str) -> str
```

Convenience function to organize WORKING-STORAGE into standard sections.

Observed calls (lexical order): `WorkingStorageOrganizer`, `organizer.reorganize`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
