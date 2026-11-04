"""Source-/schema-proven DB2 DATE to legacy eight-byte record moves.

Do not infer DB2 type from a variable *name*.  The DB2 DCLGEN must declare
DATE with an X(10) host, the destination copybook must prove an eight-byte
field, and the source statement must be an unambiguous simple MOVE.

No program, record, table, paragraph, or destination-name exceptions.
"""
from __future__ import annotations

import re
from converter.composers.db2_date_working_storage_manager import Db2DateWorkingStorageManager
from converter.composers.db2_date_line_utils import Db2DateLineUtils
from converter.services.fixed_format_line_service import FixedFormatLineService

MOVE = re.compile(
    r"^MOVE\s+(?P<field>[A-Z0-9-]+)\s+OF\s+(?P<group>DCL[A-Z0-9-]+)"
    r"\s+TO\s+(?P<target>[A-Z0-9-]+)\s+OF\s+(?P<copy>[A-Z0-9-]+)\.$",
    re.I,
)

class SchemaDateTransferComposer:
    def __init__(self, dclgen_columns=(), copybook_repository=None):
        self.dclgen_columns = list(dclgen_columns or ())
        self.copybook_repository = copybook_repository
        self.line_utils = Db2DateLineUtils()
        self.renderer = FixedFormatLineService()
        self.storage = Db2DateWorkingStorageManager()
        self.messages: list[str] = []

    def _schema_date(self, field: str, group: str) -> bool:
        from converter.services.name_normalizer import NameNormalizer
        matches = [c for c in self.dclgen_columns
                   if NameNormalizer.to_cobol(NameNormalizer.normalize(c.cobol_host_name)) == field
                   and "DCL" + NameNormalizer.to_cobol(NameNormalizer.normalize(c.table_name)) == group]
        return len(matches) == 1 and bool(re.match(r"^DATE\b", matches[0].db2_type.upper())) and bool(
            re.match(r"^X\(10\)\.?$", matches[0].cobol_picture.strip().upper())
        )

    def _eight_byte_output(self, target: str) -> bool:
        repo = self.copybook_repository
        if repo is None or repo.find(target) is None:
            return False
        # Explicit 8-byte PIC or a proven 8-byte group, never a guessed width.
        return repo.group_width_for(target) == 8

    @staticmethod
    def _body(line: str) -> str:
        if len(line) >= 7 and line[:6].isdigit():
            if line[6:7] in ("*", "/", "D", "d"):
                return ""
            return line[7:72].strip()
        if line.lstrip().startswith(("*", "/")):
            return ""
        return line.strip()

    def _replacement(self, field, group, target, copy):
        source = f"{field} OF {group}"
        destination = f"{target} OF {copy}"
        statements = [
            "MOVE ZEROES TO DA-CCYYMMDD",
            f"MOVE {source} TO DA-DD-MM-CCYY",
            "EVALUATE TRUE",
            " WHEN DA-DD-MM-CCYY = '01.01.0001'",
            "  MOVE ZEROES TO DA-CCYYMMDD-R",
            " WHEN DA-DD-MM-CCYY = '31.12.9999'",
            "  MOVE '99999999' TO DA-CCYYMMDD-R",
            " WHEN OTHER",
            "  MOVE CCYY OF DA-DD-MM-CCYY TO CCYY OF DA-CCYYMMDD-R",
            "  MOVE MM OF DA-DD-MM-CCYY TO MM OF DA-CCYYMMDD-R",
            "  MOVE DD OF DA-DD-MM-CCYY TO DD OF DA-CCYYMMDD-R",
            "END-EVALUATE",
            f"MOVE DA-CCYYMMDD-R TO {destination}.",
        ]
        return [line for statement in statements
                for line in self.renderer.emit('000000', ' ', '    '+statement, '00000000')]

    def compose(self, text: str) -> str:
        self.messages.clear()
        if not text:
            return text
        lines = text.splitlines()
        converted = []
        output = []
        i = 0
        in_procedure = False
        while i < len(lines):
            body = self._body(lines[i])
            if re.match(r'^PROCEDURE\s+DIVISION\b', body, re.I):
                in_procedure = True
            if not in_procedure or not re.match(r'^MOVE\s+', body, re.I):
                output.append(lines[i]); i += 1; continue
            # Only consume continuation lines that are part of this one MOVE.
            j = i
            parts = [body]
            while j + 1 < len(lines) and not parts[-1].endswith('.') and j-i < 6:
                nxt = self._body(lines[j+1])
                if not nxt or re.match(r'^(?:MOVE|IF|ELSE|END-|EVALUATE|PERFORM|EXEC)\b', nxt, re.I):
                    break
                j += 1; parts.append(nxt)
            match = MOVE.fullmatch(' '.join(parts).upper())
            if not match:
                output.append(lines[i]); i += 1; continue
            info = match.groupdict()
            if not (self._schema_date(info['field'], info['group'])
                    and self._eight_byte_output(info['target'])):
                output.extend(lines[i:j+1]); i = j+1; continue
            replacement = self._replacement(**info)
            output.extend(replacement)
            converted.append((info['field'],info['target']))
            i=j+1
        if converted:
            output = self.storage.ensure_date_working_storage(output, [])
            self.messages.append(f"Schema-proven DB2 DATE output transfers: {len(converted)}")
        return '\n'.join(output).rstrip() + '\n'

__all__=['SchemaDateTransferComposer']
