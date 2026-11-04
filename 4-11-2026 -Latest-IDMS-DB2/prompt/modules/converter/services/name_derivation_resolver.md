# `converter/services/name_derivation_resolver.py`

Source: [converter/services/name_derivation_resolver.py](../../../../converter/services/name_derivation_resolver.py) | 40 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `e18ed8e58d710a4ee3990ab398d5f03ee939e8a4e876d84f987bd5a796c59fee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from rules.name_derivation_rules import NAME_DERIVATION_TARGET_MARKER, VM_BD_NAME_PATTERN
```

## Local dependency notes

- [rules/name_derivation_rules.py](../../rules/name_derivation_rules.md)

## Importers (17)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/unused_copybook_pruner.py](../composers/unused_copybook_pruner.md)
- [converter/generators/restart/restart_name_resolver.py](../generators/restart/restart_name_resolver.md)
- [converter/generators/restart/restart_storage_builder.py](../generators/restart/restart_storage_builder.md)
- [converter/postprocess/copybook_reference_renamer.py](../postprocess/copybook_reference_renamer.md)
- [converter/postprocess/dynamic_metadata_resolver.py](../postprocess/dynamic_metadata_resolver.md)
- [converter/services/program_name_sync_service.py](program_name_sync_service.md)
- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [mainframe/verification/copybook_provenance.py](../../mainframe/verification/copybook_provenance.md)
- [mainframe/zowe_manifest.py](../../mainframe/zowe_manifest.md)
- [mainframe/zowe_semantic_release_gate.py](../../mainframe/zowe_semantic_release_gate.md)
- [review/runner/workspace_inputs.py](../../review/runner/workspace_inputs.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [tests/test_name_derivation.py](../../tests/test_name_derivation.md)
- 4 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `NameDerivationResolver` - L9-L40

```python
class NameDerivationResolver()
```

Derives DB2-era COBOL names from the VM...BD... source shape.

### `NameDerivationResolver.derive` - L23-L37

```python
derive(self, name: str) -> str
```

Observed calls (lexical order): `str`, `str(name or '').strip`, `VM_BD_NAME_PATTERN.match`, `match.group`, `f'{prefix}{NAME_DERIVATION_TARGET_MARKER}{site}{tail}'.upper`.

Control points:

- L25: `if not source`
- L29: `if not match`

### `NameDerivationResolver.is_derivable` - L39-L40

```python
is_derivable(self, name: str) -> bool
```

Observed calls (lexical order): `VM_BD_NAME_PATTERN.match`, `bool`, `str`, `str(name or '').strip`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
