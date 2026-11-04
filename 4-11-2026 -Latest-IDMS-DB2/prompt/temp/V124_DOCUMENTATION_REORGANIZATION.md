# V124 documentation reorganization - iteration evidence

## Scope

Based on the supplied V123 engine ZIP. This is a documentation/workspace
organization change, not a converter repair or production certification.
The original ZIP remains unchanged as rollback evidence.

## Completed

- Deleted all 95 pre-existing Markdown files from this delivered workspace.
- Created root `readme.md` with the mandatory documentation-synchronization and
  `prompt/temp/` placement rules.
- Created 16 permanent navigation/subsystem/workflow/baseline guides.
- Created 1,025 source-linked module notes and 90 package indexes.
- Added a standard-library source-hash/AST documentation maintenance utility.
- Added and ran 16 documentation-tool tests; all passed.
- Changed `pyproject.toml` only to reference the new lowercase readme filename.
- Preserved all 1,025 existing Python files byte-for-byte.
- Preserved every other original non-Markdown file; only that readme metadata
  line changed. Existing source/manual/generated COBOL and mappings are unchanged.

## Verification evidence

[Integrity comparison](documentation_integrity.json),
[documentation check](documentation_check.json),
[tool-test log](documentation_tool_tests.log), and
[deleted Markdown manifest](documentation_reorganization_manifest.json).

The documentation check verifies coverage, source and note hashes, placement and
local links. No conversion, mainframe compile, DB2 execution or full converter
regression run was performed in this documentation-only iteration. Supplied V123
results and open defects remain recorded separately in the permanent baseline.

## Next iteration

Start with `readme.md` and `prompt/00_START_HERE.md`. Open only the relevant guide,
module notes, source and tests. Update affected guide(s), refresh notes, run tests
and check documentation. Put all new temporary Markdown under `prompt/temp/`.
