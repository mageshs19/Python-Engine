# `config/logging_settings.py`

Source: [config/logging_settings.py](../../../config/logging_settings.py) | 23 lines.
Owning logic guide: [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../11_CONFIGURATION_AND_ENTRYPOINTS.md).
Source SHA-256: `ba11333c73d526459498d615b20317408e708027f42c0339786f7f4dda6d6d50`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Logging settings.

## Module-level bindings

`LOG_FILE_PREFIX` (L9), `LOG_DATE_TIME_FORMAT` (L12), `LOG_MESSAGE_FORMAT` (L15), `LOG_DATE_FORMAT` (L18), `DEFAULT_LOG_LEVEL` (L21)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/infrastructure/logger_factory.py](../converter/infrastructure/logger_factory.md)

## Change responsibility

After modifying this Python file, review [prompt/11_CONFIGURATION_AND_ENTRYPOINTS.md](../../11_CONFIGURATION_AND_ENTRYPOINTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
