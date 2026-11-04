# `converter/postprocess/restart_config.py`

Source: [converter/postprocess/restart_config.py](../../../../converter/postprocess/restart_config.py) | 205 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `f4cfbd1b872824d8ec38794fac38dc08b2ed93a4584774ef4036105c96ec3f02`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Restart logic configuration - reusable across UPDATE programs.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/cobol_restart_logic_generator.py](cobol_restart_logic_generator.md)
- [converter/postprocess/restart_logic_generator.py](restart_logic_generator.md)
- [converter/postprocess/restart_logic_pipeline.py](restart_logic_pipeline.md)
- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `RestartConfig` - L19-L205

```python
class RestartConfig()
```

Configuration for restart-aware UPDATE program generation.

Declared class/data-model fields:

```python
restart_table_name: str
restart_dclgen_name: str
program_id_field: str = 'NM-ID-RS-PROGRAM'
phase_field: str = 'NB-ID-RS-PHASE'
date_field: str = 'DA-CR-RS'
status_field: str = 'CO-ID-RS'
retention_field: str = 'NB-DAY-RS'
payload_field: str = 'TE-CH-RS-DATA'
payload_text_field: str = 'TE-CH-RS-DATA-TEXT'
payload_length_field: str = 'TE-CH-RS-DATA-LEN'
switch_group: str = 'WS-SWITCHES'
help_group: str = 'HELP-VARIABLE'
restart_record: str = 'WS-RESTART-REC'
read_count: str = 'NB-READ'
restart_key: str = 'KY-RESTART'
input_save_area: str = 'WS-INPUT-KASBONS'
commit_counter: str = 'WS-TELLER'
input_counter: str = 'WS-NB-INPUT-UPD-I'
update_counter: str = 'WS-NB-BFAR-UPD-I'
restart_len: str = 'WS-RESTART-LEN'
commit_frequency: int = 99
status_incomplete: str = '0'
status_complete: str = '1'
default_phase: str = '1'
retention_days: str = '7'
para_restart_control: str = '700-RESTART-CONTROL'
para_job_is_restart: str = '710-JOB-IS-RESTART'
para_write_restart: str = '720-WRITE-RESTART-REC'
para_commit: str = '800-PROCESS-COMMIT'
para_select: str = '700-SELECT-DZ01RSTV'
para_update: str = '700-UPDATE-DZ01RSTV'
para_insert: str = '700-INSERT-DZ01RSTV'
para_abend: str = '810000-CALL-USERABEN'
queryno_select: str = '376'
queryno_update: str = '398'
queryno_insert: str = '413'
eof_switch_flag: str = 'VMDZ205I'
minimum_dclgen_score: int = 10
notes: str = field(default='', metadata={'doc': 'Implementation notes for code review'})
```

### `RestartConfig.from_context` - L112-L123

```python
from_context(cls, context: object) -> RestartConfig
```

Create RestartConfig from UpdateProgramContext.

Observed calls (lexical order): `NotImplementedError`.

Explicit raises: `NotImplementedError('Use direct constructor with resolved metadata')`.

### `RestartConfig.apply_original_names` - L125-L141

```python
apply_original_names(self, original_mapping: dict) -> None
```

Apply original variable names from program source.

Observed calls (lexical order): `original_mapping.items`, `hasattr`, `setattr`.

Control points:

- L139: `for (attr_name, original_name) in original_mapping.items()`
- L140: `if hasattr(self, attr_name)`

### `RestartConfig.detect_from_cobol` - L143-L176

```python
detect_from_cobol(self, cobol_text: str) -> None
```

Auto-detect and apply original variable names from COBOL source.

Observed calls (lexical order): `re.search`, `self.apply_original_names`.

Control points:

- L160: `if re.search('SW-VMDZ205I\\s+PIC\\s+X', cobol_text, re.IGNORECASE)`
- L164: `if re.search('WS-NB-INPUT-UPD-I\\s+PIC', cobol_text, re.IGNORECASE)`
- L168: `if re.search('WS-NB-BFAR-UPD-I\\s+PIC', cobol_text, re.IGNORECASE)`
- L172: `if re.search('WS-RECORD-FOUND\\s+PIC\\s+X', cobol_text, re.IGNORECASE)`
- L175: `if original_mapping`

### `RestartConfig.to_dict` - L178-L198

```python
to_dict(self) -> dict
```

Export config as dictionary for serialization or logging.

### `RestartConfig.__repr__` - L200-L205

```python
__repr__(self) -> str
```

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
