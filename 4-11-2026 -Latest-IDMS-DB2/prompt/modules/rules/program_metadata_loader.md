# `rules/program_metadata_loader.py`

Source: [rules/program_metadata_loader.py](../../../rules/program_metadata_loader.py) | 113 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `582f87d583df0c40944deed39e97e63fb5f3a71669f825e1aec569f8d7d5cd6e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Load program metadata (AUTHOR, DATE-WRITTEN) from configuration file.

## Module-level bindings

`__all__` (L109)

## Import declarations

```python
from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import Optional
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_identification_transformer.py](../converter/transformers/cobol_identification_transformer.md)
- [rules/manual_reference_rules.py](manual_reference_rules.md)

## Symbol contracts and control points

### `ProgramMetadataLoader` - L15-L95

```python
class ProgramMetadataLoader()
```

Loads AUTHOR and DATE-WRITTEN configuration from file.

Declared class/data-model fields:

```python
CONFIG_FILE = Path(__file__).parent / 'program_metadata_config.txt'
```

### `ProgramMetadataLoader.load_author` - L21-L28

```python
load_author(cls) -> str
```

Load AUTHOR value from configuration file.

Observed calls (lexical order): `cls._get_config_value`.

### `ProgramMetadataLoader.load_date_written` - L31-L48

```python
load_date_written(cls) -> str
```

Load DATE-WRITTEN value from configuration file.

Observed calls (lexical order): `cls._get_config_value`, `value.upper`, `datetime.now`, `datetime.now().strftime`.

Control points:

- L43: `if value.upper() == 'TODAY'`
- L45: `if value.upper() == 'CURRENT'`

### `ProgramMetadataLoader._get_config_value` - L51-L87

```python
_get_config_value(cls, key: str, default: str='') -> str
```

Read a configuration value from the metadata config file.

Observed calls (lexical order): `cls.CONFIG_FILE.exists`, `open`, `line.split`, `line.split('#')[0].strip`, `config_key.strip`, `config_value.strip`, `config_value.endswith`, `config_value.startswith`.

Control points:

- L61: `if not cls.CONFIG_FILE.exists()`
- L66: `for line in f`
- L69: `if not line or '=' not in line`
- L77: `if config_value.startswith('"') and config_value.endswith('"') or (config_value.startswith("'") and config_value.endswith("'"))`
- L81: `if config_key == key`

### `ProgramMetadataLoader.reload` - L90-L95

```python
reload(cls) -> None
```

Reload configuration from file (clears any cached values).

### `get_author` - L99-L101

```python
get_author() -> str
```

Get configured AUTHOR name.

Observed calls (lexical order): `ProgramMetadataLoader.load_author`.

### `get_date_written` - L104-L106

```python
get_date_written() -> str
```

Get configured DATE-WRITTEN value.

Observed calls (lexical order): `ProgramMetadataLoader.load_date_written`.

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
