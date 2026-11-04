# `mainframe/zowe_rules.py`

Source: [mainframe/zowe_rules.py](../../../mainframe/zowe_rules.py) | 29 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `dbf5f8d33b5b6146c3fd9ef6b7f220058a9e6d24a40356cdd1843a224360dd45`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Zowe rule constants - facade.

## Import declarations

```python
from __future__ import annotations
from mainframe.zowe_rules_artifacts import *
from mainframe.zowe_rules_config import *
from mainframe.zowe_rules_connection import *
from mainframe.zowe_rules_pipeline import *
from mainframe.zowe_rules_messages import *
```

## Local dependency notes

- [mainframe/zowe_rules_artifacts.py](zowe_rules_artifacts.md)
- [mainframe/zowe_rules_config.py](zowe_rules_config.md)
- [mainframe/zowe_rules_connection.py](zowe_rules_connection.md)
- [mainframe/zowe_rules_messages.py](zowe_rules_messages.md)
- [mainframe/zowe_rules_pipeline.py](zowe_rules_pipeline.md)

## Importers (16)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_client.py](zowe_client.md)
- [mainframe/zowe_commands.py](zowe_commands.md)
- [mainframe/zowe_console.py](zowe_console.md)
- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_fetcher.py](zowe_fetcher.md)
- [mainframe/zowe_libraries.py](zowe_libraries.md)
- [mainframe/zowe_manifest.py](zowe_manifest.md)
- [mainframe/zowe_pipeline.py](zowe_pipeline.md)
- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)
- [mainframe/zowe_programs.py](zowe_programs.md)
- [mainframe/zowe_resolver.py](zowe_resolver.md)
- [mainframe/zowe_settings.py](zowe_settings.md)
- 4 further importers are recorded in [the source manifest](../../source_manifest.json).

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
