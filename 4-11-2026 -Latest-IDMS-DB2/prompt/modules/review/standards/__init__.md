# `review/standards/__init__.py`

Source: [review/standards/__init__.py](../../../../review/standards/__init__.py) | 1 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `09337de3334a522c291ce65ae4296d4e0fbc6de20411474451e7dbe549ea7ba8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Expected values and pipeline control. Owned by the COBOL team.

## Importers (35)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_01_line_layout.py](../checks/chk_01_line_layout.md)
- [review/checks/chk_02_db2_infrastructure.py](../checks/chk_02_db2_infrastructure.md)
- [review/checks/chk_03_residual_idms.py](../checks/chk_03_residual_idms.md)
- [review/checks/chk_04_program_header.py](../checks/chk_04_program_header.md)
- [review/checks/chk_05_sql_error_routing.py](../checks/chk_05_sql_error_routing.md)
- [review/checks/chk_06_area_alignment.py](../checks/chk_06_area_alignment.md)
- [review/checks/chk_07_sequence_continuity.py](../checks/chk_07_sequence_continuity.md)
- [review/checks/chk_08_dclgen_include_integrity.py](../checks/chk_08_dclgen_include_integrity.md)
- [review/checks/chk_09_record_retrieval_conversion.py](../checks/chk_09_record_retrieval_conversion.md)
- [review/checks/chk_10_record_modification_conversion.py](../checks/chk_10_record_modification_conversion.md)
- [review/checks/chk_11_sqlcode_commit_conversion.py](../checks/chk_11_sqlcode_commit_conversion.md)
- [review/checks/chk_12_cursor_declaration.py](../checks/chk_12_cursor_declaration.md)
- [tests/test_eoc_vocabulary_agrees_across_the_review_boundary.py](../../tests/test_eoc_vocabulary_agrees_across_the_review_boundary.md)
- 22 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
