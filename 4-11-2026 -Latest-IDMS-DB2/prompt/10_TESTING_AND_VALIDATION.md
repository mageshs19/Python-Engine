# Testing and what each result establishes

## Evidence levels

| Check | Establishes | Does not establish |
|---|---|---|
| Documentation hashes / links / AST | Notes cover current source and navigate correctly | Semantic accuracy or production readiness |
| Python parse/compile | Python source syntax is valid for that interpreter | Correct conversion or COBOL syntax |
| Python regression suite | Executed tests met assertions | All business paths, real DB2 behavior or scalability |
| Static COBOL/release review | Implemented checks passed with supplied evidence | Mainframe compile/link or external include behavior |
| Predicate model | Tested model agrees for its stated assumptions | Actual DB2 host-format/null behavior |
| Actual binary file comparison | Supplied files match byte count/order/content | Untested datasets, error/restart paths |
| Native precompile/compile and differential runs | Evidence from the tested target environment/cases | Universal correctness of future unseen programs |

## Local commands

```bash
python prompt/tools/maintain_docs.py check
python -m unittest discover -s prompt/tools -p 'test_*.py'
python -m pytest -p no:cacheprovider -o addopts= -q tests
python -m mainframe.zowe_pipeline all --from convert --to review
```

Disable pytest's cache provider when following the strict Markdown placement
policy: its default cache can create `.pytest_cache/README.md` outside `prompt/`.
Store scratch Markdown and iteration reports only in `prompt/temp/`. Non-Markdown
machine evidence may stay in the existing workspace/report directories.

The conversion command clears generated Output and Review; preserve required
baseline evidence before rerunning, not by editing generated COBOL. Tests that
need fixtures should use stable source fixtures rather than relying on stale
output artifacts surviving cleanup.

## Regression selection

Start with the owning module note's importing tests and the relevant package
index. Imports are only a discovery hint: fixtures, subprocess tests, dynamic
imports and indirect calls can add coverage. Add renamed synthetic cases and
negative/refusal cases for generic rules, then rerun all six samples for shared
changes. Test unsupported/ambiguous metadata without silently weakening the gate.

Review raw results, exit code, skipped tests and the environment. Do not report
success from a progress bar without a completed result. Keep historical and fresh
results clearly separated.

## Mainframe record comparison

Once manual and generated programs have run against the same approved data and
parameters, use the existing binary comparator. The 530-byte size below belongs
to the archived 7200 example; use the actual contract for other programs.

```bash
python -m mainframe.verification.fixed_record_diff \
  --manual manual_form.fb \
  --generated generated_form.fb \
  --record-size 530 \
  --report form_diff.json
```

Supply actual fixed-record bytes, not text-mode conversions or screenshots.
Validate row order, packed fields, padding, date sentinels and counters as well as
record counts. Native DB2 precompile, COBOL compile/link, external includes and
restart/error-path runs remain required for release.

## Source map

- [Tests package index](index/tests.md)
- [Fixed-record comparator](modules/mainframe/verification/fixed_record_diff.md)
- [Archive predicate model](modules/mainframe/verification/archive_date_predicate.md)
- [Review engine](modules/review/engine/reviewer.md)
- [Current evidence](13_CURRENT_BASELINE_AND_OPEN_ISSUES.md)

## V129 reproducible integration fixtures
Integration tests discover the authoritative mapping export and current generated candidates through tests/workspace_fixtures.py instead of naming absent historical timestamp files. Expanded integration inputs come from the current Output/LRF artifacts. Generate the offline workspace first. Use an explicit writable --basetemp and TEMP/TMP in restricted Windows environments. New renamed synthetic cases cover unique/ambiguous/local references, date metadata, quoted strings, repeated rewriting, implicit scope termination, orphan terminators and resolved status warnings.

The post-field-resolution date pass has a continuation-line and idempotence regression case.
