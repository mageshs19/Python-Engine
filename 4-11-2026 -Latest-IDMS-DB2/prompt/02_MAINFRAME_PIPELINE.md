# Mainframe batch, workspace and transfer lifecycle

## Entrypoint and step order

`python -m mainframe.zowe_pipeline` parses a command and optional inclusive
`--from`/`--to` bounds. `PIPELINE_STEPS` is `fetch, convert, review, upload`.
`init`, `show`, `plan` and `clean` are separate maintenance commands. Exit
constants are `0` (OK), `1` (nothing), and `2` (error). `run_steps` stops at a
FAILED step. SKIPPED and NOTHING do not alone constitute a failure, so examine
the selected range and logs rather than equating an overall message with release.

Use the offline conversion/review range for workspace development:

```bash
python -m mainframe.zowe_pipeline all --from convert --to review
```

## Workspace and immutable inputs

`zowe_workspace.workspace_root()` reads `ZOWE_WORKSPACE_ROOT` through the settings
layer, otherwise uses `mainframe/workspace/`. It exposes Mapping Sheet, Program,
Copybook, DCLGen, Subschema, Output, Review and Logs directories. The normal
runner environment sets `IDMS_INPUT_DIR` to this root, puts repository and `src`
on `PYTHONPATH`, and runs the child from the repository root.

`step_convert` checks mapping/program availability then invokes
`clean_generated()`. Cleanup deletes only managed Output and Review, recreates
them, and leaves input/manual assets intact. Do not replace this with broad
workspace deletion. Documentation cleanup is separate and must never delete
source or manual COBOL.

## Stage contracts

| Stage | Actual responsibility |
|---|---|
| Fetch | `ZoweFetcher.fetch_all()` resolves selected programs and supporting libraries and writes local assets. Connection/library rules live in mainframe settings modules. |
| Convert | Run `runners/convert_programs.py`; choose update/retrieval converters using source evidence; retain logs and candidate files. |
| Review | Run `review/runner/review_file.py` with output, report folder, kind and `--workspace`; then independently call `audit_generated_batch()`. Both must succeed. |
| Upload | Rerun structural and semantic checks even when invoked alone. Preflight derived-copybook dataset configuration before transport. Upload generated copybooks before referring COBOL members. |

`zowe_steps._run()` streams child output into an in-memory transcript and writes
it under workspace Logs; console output is a digest unless verbose. A declared
timeout constant elsewhere does not prove enforcement: inspect `_run` before
claiming subprocess timeout behavior.

## Operational cautions

Never run fetch/upload merely to check documentation. Do not put passwords,
tokens or connection secrets in prompt notes. Preserve exact artifact identity
and dataset member rules; similarly named programs or renamed copybooks must not
be silently merged. Source metadata and derived-copybook provenance are required
for upload approval.

Markdown iteration reports belong in `prompt/temp/`; operational `.log`, `.csv`,
`.json` and candidate `.cbl` artifacts retain their existing workspace locations.
This is a Markdown placement policy, not a relocation of all pipeline outputs.

## Source map

- [CLI and range selection](modules/mainframe/zowe_pipeline.md)
- [Stage implementations](modules/mainframe/zowe_pipeline_steps.md)
- [Subprocess contract](modules/mainframe/zowe_steps.md)
- [Workspace cleanup](modules/mainframe/zowe_workspace.md)
- [Fetch](modules/mainframe/zowe_fetcher.md)
- [Copybook upload preflight](modules/mainframe/zowe_copybook_upload.md)
- [COBOL upload](modules/mainframe/zowe_writer.md)
