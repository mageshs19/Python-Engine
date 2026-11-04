# `mainframe/zowe_patterns.py`

Source: [mainframe/zowe_patterns.py](../../../mainframe/zowe_patterns.py) | 160 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `8b3bd2cc57ff548c970ade82a1363c90b4e9a60564cdff91fa92f464eacd9df0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex patterns used only by the zowe package.

## Module-level bindings

`MEMBER_PATH_PATTERN` (L16), `DATASET_NAME_PATTERN` (L19), `UNSAFE_FILENAME_CHAR_PATTERN` (L25), `COPY_MEMBER_PATTERN` (L29), `COPY_IDMS_LR_PATTERN` (L34), `INCLUDE_DCLGEN_PATTERN` (L39), `OUTPUT_STEM_PATTERN` (L47), `DOTENV_LINE_PATTERN` (L55), `ENV_REFERENCE_PATTERN` (L60), `BARE_ENV_KEY_PATTERN` (L66), `PLAIN_COPY_PATTERN` (L72), `COPY_IDMS_RECORD_PATTERN` (L78), `DB_WITHIN_PATTERN` (L84), `IDMS_VERB_RECORD_PATTERN` (L91), `SOURCE_PROGRAM_ID_PATTERN` (L99), `FIXED_SEQUENCE_PATTERN` (L104), `RECORD_VERSION_SUFFIX_PATTERN` (L108), `SUBSCHEMA_CLAUSE_HEAD_PATTERN` (L114), `ELEMENT_TOKEN_PATTERN` (L119), `NAME_LIST_ONLY_PATTERN` (L122), `LOGICAL_RECORD_PATTERN` (L135), `ELEMENTS_ARE_PATTERN` (L142), `BLOCK_END_PATTERN` (L148), `SUBSCHEMA_CLAUSE_HEAD_PATTERN` (L151), `ELEMENT_TOKEN_PATTERN` (L157), `NAME_LIST_ONLY_PATTERN` (L160)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_client.py](zowe_client.md)
- [mainframe/zowe_env.py](zowe_env.md)
- [mainframe/zowe_resolver.py](zowe_resolver.md)
- [mainframe/zowe_subschema.py](zowe_subschema.md)
- [mainframe/zowe_writer.py](zowe_writer.md)

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
