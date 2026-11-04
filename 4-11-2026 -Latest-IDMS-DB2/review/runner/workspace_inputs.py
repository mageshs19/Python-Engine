"""Read-only, per-program source/metadata adapter for production reviews.

The folder runner must not reuse one source for every output or review without
metadata while claiming a production verdict. Inputs are paired by PROGRAM-ID
and the shared derivation rule, not by timestamp, paragraph prefix or sample ID.
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from pathlib import Path
import re
import tempfile

from converter.parsers.cobol_parser import CobolParser
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.repositories.mapping_repository import MappingRepository
from converter.repositories.dclgen_repository import DclgenRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_derivation_resolver import NameDerivationResolver
from mainframe.verification.copybook_provenance import resolve_copybooks


def _read(path: Path) -> str:
    raw = path.read_bytes()
    try:
        return raw.decode('utf-8-sig')
    except UnicodeDecodeError:
        return raw.decode('latin1')


def _code(text: str) -> str:
    result = []
    for raw in text.splitlines():
        if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace()):
            if raw[6] in '*/Dd':
                continue
            raw = raw[7:72]
        if raw.lstrip().startswith(('*','/')):
            continue
        result.append(raw)
    return '\n'.join(result).upper()


@dataclass
class ReviewInputs:
    source: str
    target_id: str
    mapping_rows: list
    dclgen_columns: list
    copybook_fields: list
    diagnostics: list[str]


class WorkspaceReviewInputs:
    def __init__(self, workspace: Path):
        self.root = Path(workspace)
        self.errors: list[str] = []
        self.mapping = []
        self.columns = []
        self.sources: dict[str,list[tuple[Path,str]]] = {}
        sheets = sorted(p for p in (self.root/'Mapping Sheet').glob('*')
                        if p.suffix.lower() in {'.csv','.xlsx'})
        if len(sheets) != 1:
            self.errors.append(f'Expected one authoritative mapping file, found {len(sheets)}.')
        else:
            self.mapping = SheetMappingParser().parse_uploaded_file(LocalUploadedFile(sheets[0]))
            if not self.mapping:
                self.errors.append('The authoritative mapping file contains no parsed rows.')
        files = sorted(p for p in (self.root/'DCLGen').glob('*') if p.is_file() and
                       p.suffix.lower() in {'.txt','.cpy','.cbl','.cob'})
        for path in files:
            self.columns.extend(DclgenParser().parse(_read(path)))
        if not self.columns:
            self.errors.append('No parsed DCLGEN columns found.')
        resolver = NameDerivationResolver()
        for path in sorted((self.root/'Program').glob('*.cbl')):
            text = _read(path)
            source_id = CobolParser().program_id(text)
            if source_id:
                self.sources.setdefault(resolver.derive(source_id),[]).append((path,text))
        self.tables = TableNameResolver(MappingRepository(self.mapping),DclgenRepository(self.columns))

    def for_program(self, generated: str, source_override: str = '') -> ReviewInputs:
        target = CobolParser().program_id(generated)
        code = _code(generated)
        needs_sql_metadata = bool(re.search(r'\bEXEC\s+SQL\b', code))
        # A non-SQL member has no schema dependency. Its source pairing is
        # still checked below; do not report unused DB2 inputs as blockers.
        notes = list(self.errors) if needs_sql_metadata else []
        source = ''
        candidates = self.sources.get(target,[])
        if source_override:
            source_id = CobolParser().program_id(source_override)
            if NameDerivationResolver().derive(source_id) != target:
                notes.append('Explicit source PROGRAM-ID does not derive to this output PROGRAM-ID.')
            else:
                source = source_override
        elif len(candidates) == 1:
            source = candidates[0][1]
        else:
            notes.append(f'Expected one original source for {target}, found {len(candidates)}.')
        included = set(re.findall(r'\bEXEC\s+SQL\s+INCLUDE\s+([A-Z][A-Z0-9_-]*)\b',code))
        used_tables = set(re.findall(r'\b(?:FROM|JOIN|UPDATE|INSERT\s+INTO)\s+([A-Z][A-Z0-9_]*)\b',code))
        known = {c.table_name.upper() for c in self.columns}
        tables = (included | used_tables) & known
        columns = [c for c in self.columns if c.table_name.upper() in tables]
        source_code = _code(source)
        source_records = {row.cobol_record_idms.upper() for row in self.mapping if row.cobol_record_idms and
                          re.search(r'(?<![A-Z0-9-])'+re.escape(row.cobol_record_idms.upper())+r'(?![A-Z0-9-])',source_code)}
        rows = []
        for row in self.mapping:
            table = self.tables.resolve_table(row.new_db2_record)
            if table not in tables:
                continue
            if source_records and row.cobol_record_idms.upper() not in source_records:
                continue
            # Do not "repair" data types/widths here. Only the existing,
            # schema-proven TB/TV alias resolution is applied for comparison.
            rows.append(replace(row,new_db2_record=table))
        if needs_sql_metadata and not columns:
            notes.append('No relevant DCLGEN columns resolved for the generated SQL member.')
        if needs_sql_metadata and not rows:
            notes.append('No relevant mapping rows resolved for the generated SQL member.')
        fields = []
        if source:
            with tempfile.TemporaryDirectory(prefix='review-copy-provenance-') as tmp:
                copies = resolve_copybooks(source,generated,self.root/'Copybook',Path(tmp))
                notes.extend(copies.errors)
                for p in copies.staged_members:
                    fields.extend(CopybookParser().parse(_read(p)))
                copied = set(re.findall(r'^\s*COPY\s+([A-Z][A-Z0-9-]*)\.',code,re.M))
                for name in copied:
                    matches = [p for p in (self.root/'Copybook').glob('*') if p.is_file() and p.stem.upper()==name]
                    if len(matches)==1:
                        fields.extend(CopybookParser().parse(_read(matches[0])))
        return ReviewInputs(source,target,rows,columns,fields,notes)
