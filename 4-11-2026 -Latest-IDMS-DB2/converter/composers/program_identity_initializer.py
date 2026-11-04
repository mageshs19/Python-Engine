"""Initialize SQL diagnostic identity at procedure entry, without naming business paragraphs.

Only a literal CS-PROGRAM matching PROGRAM-ID and INCLUDE SQLERRWS justify
this insertion. Existing PROGRAM-NAME assignments are left alone. No labels,
control transfers, declarations, or business values are created or renamed.
"""
from __future__ import annotations
import re
from converter.services.fixed_format_line_service import FixedFormatLineService


def _body(raw: str) -> str:
    if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace()):
        if raw[6] in '*/Dd':
            return ''
        raw = raw[7:72]
    if raw.lstrip().startswith(('*', '/')):
        return ''
    return re.split(r'\*>', raw, maxsplit=1)[0].strip()


class ProgramIdentityInitializer:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def compose(self, text: str) -> str:
        self.messages = []
        lines = text.splitlines()
        bodies = [_body(line) for line in lines]
        procedure = next((i for i, b in enumerate(bodies)
                          if re.match(r'^PROCEDURE\s+DIVISION\b', b, re.I)), None)
        if procedure is None:
            return text
        data = ' '.join(bodies[:procedure])
        code = ' '.join(bodies[procedure:])
        program = re.search(r'\bPROGRAM-ID\.\s*([A-Z0-9-]+)', data, re.I)
        constant = re.search(r'\b(?:0[1-9]|[1-4][0-9]|77)\s+CS-PROGRAM\s+'
                             r'PIC\s+X\(\d+\)\s+VALUE\s+[\'"]([A-Z0-9-]+)[\'"]', data, re.I)
        if not (program and constant and
                program.group(1).upper() == constant.group(1).upper() and
                re.search(r'\bEXEC\s+SQL\s+INCLUDE\s+SQLERRWS\s+END-EXEC\b', data, re.I)):
            return text
        # Do not relocate or override an author-defined identity assignment.
        # A separate review must assess dominance for that more complex case.
        masked = re.sub(r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"", ' ', code)
        if re.search(r'\bTO\s+PROGRAM-NAME\b', masked, re.I):
            return text
        # Procedure header continuations and DECLARATIVES need their own CFG
        # treatment. Refuse to insert into an unproven entry point.
        if not bodies[procedure].endswith('.') or re.search(r'\bDECLARATIVES\b', masked, re.I):
            self.messages.append('Diagnostic identity not inserted: ambiguous procedure entry.')
            return text
        insertion = procedure + 1
        while insertion < len(lines) and not bodies[insertion]:
            insertion += 1
        # Skip an optional first SECTION and then its first paragraph header.
        while insertion < len(lines):
            b = bodies[insertion]
            if re.fullmatch(r'[A-Z0-9][A-Z0-9-]*(?:\s+SECTION)?\.', b, re.I):
                if b.upper() in {'GOBACK.', 'EXIT.', 'CONTINUE.'}:
                    break
                raw = lines[insertion]
                area = raw[7:72] if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace()) else raw
                if len(area) - len(area.lstrip()) > 3:
                    break
                insertion += 1
                while insertion < len(lines) and not bodies[insertion]:
                    insertion += 1
                continue
            break
        rendered = FixedFormatLineService().emit('000000', ' ',
                    '    MOVE CS-PROGRAM TO PROGRAM-NAME', '00000000')
        lines[insertion:insertion] = rendered
        self.messages.append('Diagnostic identity initialized at proven procedure entry.')
        return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
