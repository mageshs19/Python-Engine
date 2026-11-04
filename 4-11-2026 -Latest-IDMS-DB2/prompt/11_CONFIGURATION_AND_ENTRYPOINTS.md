# Configuration, environment, entrypoints and packaging

## Actual entrypoints

| Path / command | Purpose |
|---|---|
| `python -m mainframe.zowe_pipeline ...` | Main batch orchestration |
| `runners/convert_programs.py` | Active kind-routing conversion subprocess |
| `review/runner/review_file.py` | File/folder review subprocess; workspace evidence matters |
| `streamlit run converter/app.py` | Converter UI entrypoint; optional UI dependencies apply |
| `main.py` | Empty in the supplied checkout; not a working converter CLI |
| `prompt/tools/maintain_docs.py` | Documentation-only utility; standard library only |

Read actual imports when choosing settings. `config/path_settings.py` is used by
the active mainframe runner and defaults to `mainframe/workspace`, with
`IDMS_INPUT_DIR` override and layout selection. `converter/config/path_settings.py`
and copies under `config/config/` also exist; some contain older local Windows
paths and split Retrieval/Update directories. They must not be assumed equivalent
to the active path merely because the filenames match.

`ZOWE_WORKSPACE_ROOT` chooses the mainframe workspace. The subprocess adapter
passes its value through `IDMS_INPUT_DIR`, adds repository/`src` search paths and
sets unbuffered Python output. Other Zowe connection/library settings are read
through `zowe_env`, `zowe_settings` and the related rule modules. Do not embed
credentials in prompt files or generation rules.

## Dependency declarations versus installed environment

`pyproject.toml` declares Python `>=3.14`, runtime dependencies including openpyxl,
pdfplumber, pydantic, pydantic-settings and streamlit, and pytest in the dev group.
These are the supplied project's declarations, not a newly validated compatibility
matrix. Do not silently install different versions and claim production support.

The same file currently configures setuptools to discover packages under `src`,
but the supplied repository's active packages are at its root and no `src/` tree
is present. The direct-root CLI uses explicit search paths. Packaging/installability
is therefore an existing unresolved configuration issue; this documentation
release only changes the readme filename reference to `readme.md`.

## Existing Markdown-producing audit

The standalone `runners/audit_ai_standardized_reference.py` still defaults to a
root Markdown report. Its Python source is intentionally unchanged in this
reorganization. Always use its supported destination override under the new
policy:

```bash
python runners/audit_ai_standardized_reference.py \
  --markdown-out prompt/temp/ai_standardized_comparison.md \
  --json-out prompt/temp/ai_standardized_comparison.json
```

`prompt/temp/` must exist before running it. The documentation checker rejects
Markdown created in the root or other directories. All future report-writer code
must use the same policy or expose an appropriate override; never claim the
existing default was changed in this documentation-only release.

## Source map

- [Active path settings](modules/config/path_settings.md)
- [Legacy converter path settings](modules/converter/config/path_settings.md)
- [Zowe environment](modules/mainframe/zowe_env.md)
- [Zowe settings](modules/mainframe/zowe_settings.md)
- [Subprocess environment](modules/mainframe/zowe_steps.md)
- [UI entrypoint](modules/converter/app.md)
- [Comparison audit CLI](modules/runners/audit_ai_standardized_reference.md)
