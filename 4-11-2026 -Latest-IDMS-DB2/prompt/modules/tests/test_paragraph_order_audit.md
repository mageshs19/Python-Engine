# `tests/test_paragraph_order_audit.py`

Source: [tests/test_paragraph_order_audit.py](../../../tests/test_paragraph_order_audit.py) | 102 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `7cb05e7ffea4902e614aa4c3f4f18e43339eb5f7efe3648627c116c9ae45f39a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.analyzers.program_flow.paragraph_order_audit import ParagraphOrderAuditor
```

## Local dependency notes

- [converter/analyzers/program_flow/paragraph_order_audit.py](../converter/analyzers/program_flow/paragraph_order_audit.md)

## Symbol contracts and control points

### `test_order_audit_allows_generated_paragraphs_between_original_paragraphs` - L4-L21

```python
test_order_audit_allows_generated_paragraphs_between_original_paragraphs()
```

Observed calls (lexical order): `ParagraphOrderAuditor`, `ParagraphOrderAuditor().audit`.

### `test_order_audit_flags_original_business_paragraph_reordering` - L24-L43

```python
test_order_audit_flags_original_business_paragraph_reordering()
```

Observed calls (lexical order): `ParagraphOrderAuditor`, `ParagraphOrderAuditor().audit`.

### `test_order_audit_reports_missing_original_paragraphs_for_review` - L46-L59

```python
test_order_audit_reports_missing_original_paragraphs_for_review()
```

Observed calls (lexical order): `ParagraphOrderAuditor`, `ParagraphOrderAuditor().audit`.

### `test_order_audit_treats_idms_abort_hook_removal_as_intentional` - L63-L81

```python
test_order_audit_treats_idms_abort_hook_removal_as_intentional()
```

Observed calls (lexical order): `ParagraphOrderAuditor`, `ParagraphOrderAuditor().audit`.

### `test_order_audit_does_not_hide_nontrivial_idms_abort_business_body` - L84-L102

```python
test_order_audit_does_not_hide_nontrivial_idms_abort_business_body()
```

Observed calls (lexical order): `ParagraphOrderAuditor`, `ParagraphOrderAuditor().audit`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
