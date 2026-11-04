# `converter/generators/restart_infrastructure_fixer.py`

Source: [converter/generators/restart_infrastructure_fixer.py](../../../../converter/generators/restart_infrastructure_fixer.py) | 217 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `2b16aa0a0c57d171be67f4678c177ba64158d01ebda61b71a96cb8b94422d8f0`.

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

### `RestartInfrastructureFixer` - L10-L217

```python
class RestartInfrastructureFixer()
```

Fixes remaining restart infrastructure issues in COBOL programs.

Declared class/data-model fields:

```python
LEGACY_SQLCODE_PATTERN = re.compile('^\\s*(?:\\d{6}\\s+)?IF\\s+NOT\\s+SQLCODE\\s*=\\s*100', flags=re.MULTILINE | re.IGNORECASE)
SELECT_PATTERN = re.compile('^\\s*(?:\\d{6}\\s+)?EXEC\\s+SQL\\s*\\n\\s*(?:\\d{6}\\s+)?SELECT', flags=re.MULTILINE | re.IGNORECASE)
WHERE_PATTERN = re.compile('WHERE\\s+(\\w+)\\s*=', flags=re.IGNORECASE)
```

### `RestartInfrastructureFixer.__init__` - L37-L38

```python
__init__(self) -> None
```

### `RestartInfrastructureFixer.apply` - L40-L65

```python
apply(self, cobol_text: str, program_id: Optional[str]=None) -> tuple[str, list[str]]
```

Apply restart infrastructure fixes to COBOL text.

Observed calls (lexical order): `str`, `self._fix_legacy_sqlcode`, `self._add_sql_location_before_retrieval`, `self._add_restart_control_hints`.

Control points:

- L57: `if not text`

### `RestartInfrastructureFixer._fix_legacy_sqlcode` - L67-L137

```python
_fix_legacy_sqlcode(self, text: str) -> str
```

Convert legacy IF NOT SQLCODE = 100 to EVALUATE SQLCODE.

Observed calls (lexical order): `text.split`, `len`, `re.search`, `re.match`, `indent_match.group`, `max`, `result_lines.append`, `body_line.strip`, `first_six.strip`, `first_six.strip().isdigit`, `cleaned_line.startswith`, `cleaned_line.strip`, `self.messages.append`, `'\n'.join`.

Control points:

- L74: `while i < len(lines)`
- L78: `if re.search('^\\s*(?:\\d{6}\\s+)?IF\\s+NOT\\s+SQLCODE\\s*=\\s*100', line, re.IGNORECASE)`
- L100: `while i < len(lines)`
- L103: `if re.search('END-IF', body_line, re.IGNORECASE)`
- L111: `if body_line.strip()`
- L114: `if len(cleaned_line) > 6`
- L116: `if first_six.strip() and first_six.strip().isdigit()`
- L120: `if not cleaned_line.startswith(' ')`

### `RestartInfrastructureFixer._add_sql_location_before_retrieval` - L139-L193

```python
_add_sql_location_before_retrieval(self, text: str) -> str
```

Add SQL-LOCATION MOVE before retrieval SELECTs that lack it.

Observed calls (lexical order): `text.split`, `len`, `re.search`, `self._is_restart_select`, `max`, `range`, `re.match`, `indent_match.group`, `result_lines.append`, `self.messages.append`, `'\n'.join`.

Control points:

- L145: `while i < len(lines)`
- L149: `if re.search('EXEC\\s+SQL', line, re.IGNORECASE)`
- L155: `while j < len(lines) and j < i + 5`
- L156: `if re.search('^\\s*(?:\\d{6}\\s+)?SELECT', lines[j], re.IGNORECASE)`
- L162: `if found_select`
- L164: `if not self._is_restart_select(line)`
- L167: `for k in range(max(0, i - 3), i)`
- L168: `if re.search('MOVE\\s+[\'\\"].*[\'\\"].*TO\\s+SQL-LOCATION', lines[k], re.IGNORECASE)`
- Another 1 conditions/loops exist in this source span.

### `RestartInfrastructureFixer._add_restart_control_hints` - L195-L213

```python
_add_restart_control_hints(self, text: str, program_id: Optional[str]) -> str
```

Add comments about missing restart control paragraphs.

Observed calls (lexical order): `all`, `self.messages.append`.

Control points:

- L197: `if program_id not in ['VMDZ1526', 'VMDZ1567']`
- L207: `if not all([has_restart_control, has_job_is_restart, has_write_restart])`

### `RestartInfrastructureFixer._is_restart_select` - L215-L217

```python
_is_restart_select(self, line: str) -> bool
```

Check if this is a restart SELECT (700- prefix).

Observed calls (lexical order): `bool`, `re.search`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
