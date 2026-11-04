# `converter/generators/control_paragraph_generator.py`

Source: [converter/generators/control_paragraph_generator.py](../../../../converter/generators/control_paragraph_generator.py) | 261 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `7aa4611b7e8f187510582a9951710ff46aba352fc11228590bc9bc03898aaaad`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from typing import Optional
```

## Symbol contracts and control points

### `ControlParagraphGenerator` - L10-L261

```python
class ControlParagraphGenerator()
```

Generates standard COBOL restart control paragraphs.

### `ControlParagraphGenerator.__init__` - L23-L24

```python
__init__(self) -> None
```

### `ControlParagraphGenerator.apply` - L26-L55

```python
apply(self, cobol_text: str, program_id: Optional[str]=None) -> tuple[str, list[str]]
```

Generate control paragraphs if missing.

Observed calls (lexical order): `str`, `self._detect_program_id`, `self._generate_control_paragraphs`, `self.messages.append`.

Control points:

- L43: `if not text`
- L50: `if program_id in ['VMDZ1526', 'VMDZ1567']`

### `ControlParagraphGenerator._detect_program_id` - L57-L64

```python
_detect_program_id(self, cobol_text: str) -> str
```

Detect program ID from COBOL source.

Observed calls (lexical order): `re.search`, `match.group`.

### `ControlParagraphGenerator._generate_control_paragraphs` - L66-L111

```python
_generate_control_paragraphs(self, text: str, program_id: str) -> str
```

Generate 800, 820, 830 control paragraphs.

Observed calls (lexical order): `self._paragraph_exists`, `self.messages.append`, `self._find_program_identifier`, `self._find_date_field`, `self._find_eof_flag`, `self._find_counter_variable`, `self._find_insertion_point`, `paragraphs.append`, `self._build_800_restart_control`, `self._build_810_job_is_restart`, `self._build_820_write_restart_rec`, `self._build_830_process_commit`, `'\n'.join`.

Control points:

- L69: `if self._paragraph_exists(text, '800-RESTART-CONTROL')`
- L82: `if insertion_point == -1`

### `ControlParagraphGenerator._paragraph_exists` - L113-L119

```python
_paragraph_exists(self, text: str, paragraph_name: str) -> bool
```

Check if paragraph already exists.

Observed calls (lexical order): `re.compile`, `re.escape`, `bool`, `pattern.search`.

### `ControlParagraphGenerator._find_program_identifier` - L121-L127

```python
_find_program_identifier(self, text: str, program_id: str) -> str
```

Find program identifier variable (CS-PROGRAM or constant).

Observed calls (lexical order): `re.search`.

Control points:

- L124: `if re.search('CS-PROGRAM.*VALUE\\s+[\'\\"].*[\'\\"]', text, re.IGNORECASE)`

### `ControlParagraphGenerator._find_date_field` - L129-L145

```python
_find_date_field(self, text: str) -> str
```

Find date field in working storage.

Observed calls (lexical order): `re.search`, `match.group`.

Control points:

- L139: `for pattern in patterns`
- L140: `if re.search(pattern, text, re.IGNORECASE)`
- L142: `if match`

### `ControlParagraphGenerator._find_eof_flag` - L147-L162

```python
_find_eof_flag(self, text: str) -> str
```

Find EOF flag in working storage.

Observed calls (lexical order): `re.search`, `match.group`.

Control points:

- L156: `for pattern in patterns`
- L157: `if re.search(pattern, text, re.IGNORECASE)`
- L159: `if match`

### `ControlParagraphGenerator._find_counter_variable` - L164-L181

```python
_find_counter_variable(self, text: str) -> str
```

Find input counter variable.

Observed calls (lexical order): `re.search`, `match.group`.

Control points:

- L167: `if re.search('WS-NB-INPUT-UPD-I', text, re.IGNORECASE)`
- L175: `for pattern in patterns`
- L176: `if re.search(pattern, text, re.IGNORECASE)`
- L178: `if match`

### `ControlParagraphGenerator._find_insertion_point` - L183-L193

```python
_find_insertion_point(self, text: str) -> int
```

Find where to insert control paragraphs.

Observed calls (lexical order): `re.search`, `match.start`, `len`.

Control points:

- L186: `for pattern in ['STOP\\s+RUN', 'END\\s+PROGRAM']`
- L188: `if match`

### `ControlParagraphGenerator._build_800_restart_control` - L195-L212

```python
_build_800_restart_control(self, cs_program: str, date_field: str) -> str
```

Build 800-RESTART-CONTROL paragraph.

### `ControlParagraphGenerator._build_810_job_is_restart` - L214-L225

```python
_build_810_job_is_restart(self) -> str
```

Build 810-JOB-IS-RESTART paragraph (template).

### `ControlParagraphGenerator._build_820_write_restart_rec` - L227-L238

```python
_build_820_write_restart_rec(self) -> str
```

Build 820-WRITE-RESTART-REC paragraph.

### `ControlParagraphGenerator._build_830_process_commit` - L240-L261

```python
_build_830_process_commit(self, eof_flag: str, counter_var: str) -> str
```

Build 830-PROCESS-COMMIT paragraph.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
