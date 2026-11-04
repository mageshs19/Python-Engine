"""Guard non-numeric alphanumeric reference-modification input to DB2 numeric hosts.

The original input may be a PIC X(13) identifier split into a character
part and a numeric one-character discriminator. The numeric discriminator
cannot be moved to a packed/decimal SQL host without validating it first.
This rule keys on the *declared source PIC* and *DCLGEN host PIC*, not a
program ID, field name, or key position.
"""
from __future__ import annotations

import re
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.name_normalizer import NameNormalizer

PATTERN = re.compile(
    r"^MOVE\s+(?P<source>[A-Z0-9-]+)\((?P<offset>\d+):(?P<length>\d+)\)"
    r"\s+TO\s+(?P<host>[A-Z0-9-]+)\s+OF\s+(?P<group>DCL[A-Z0-9-]+)\.$", re.I)

class SchemaNumericKeyGuard:
    def __init__(self, dclgen_columns=()):
        self.columns = list(dclgen_columns or ())
        self.renderer = FixedFormatLineService()
        self.messages: list[str] = []

    @staticmethod
    def _body(line):
        if len(line) >= 7 and line[:6].isdigit():
            return '' if line[6] in '*/Dd' else line[7:72].strip()
        return '' if line.lstrip().startswith(('*','/')) else line.strip()

    def _numeric_host(self, host, group):
        found=[c for c in self.columns
               if NameNormalizer.to_cobol(NameNormalizer.normalize(c.cobol_host_name)) == host
               and 'DCL'+NameNormalizer.to_cobol(NameNormalizer.normalize(c.table_name)) == group]
        if len(found)!=1:
            return False
        picture=found[0].cobol_picture.strip().upper()
        return bool(re.match(r'^S?9(?:\b|\(|V)', picture))

    def compose(self, text):
        self.messages.clear()
        if not text:
            return text
        lines=text.splitlines(); out=[]; declaration={}
        in_procedure=False; i=0; guarded=0
        for line in lines:
            body=self._body(line)
            if re.match(r'^PROCEDURE\s+DIVISION\b',body,re.I):
                in_procedure=True
            if not in_procedure:
                m=re.match(r'^\d{2}\s+([A-Z0-9-]+)\s+PIC\s+(X(?:\(\d+\)|X+))(?=\s|\.)',body,re.I)
                if m:
                    declaration[m.group(1).upper()]=m.group(2).upper()
        if 'PERFORM SQLERROR' not in text.upper():
            # No error policy means an inserted guard cannot fail safely.
            return text
        while i < len(lines):
            body=self._body(lines[i])
            if not re.match(r'^MOVE\s+', body, re.I):
                out.append(lines[i]);i+=1;continue
            j=i;parts=[body]
            while j+1<len(lines) and not parts[-1].endswith('.') and j-i<5:
                next_body=self._body(lines[j+1])
                if not next_body or re.match(r'^(?:MOVE|IF|ELSE|END-|EVALUATE|PERFORM|EXEC)\b',next_body,re.I):
                    break
                j+=1;parts.append(next_body)
            match=PATTERN.fullmatch(' '.join(parts).upper())
            if not match:
                out.append(lines[i]);i+=1;continue
            data=match.groupdict(); source=data['source']; ref=f"{source}({data['offset']}:{data['length']})"
            eligible=source in declaration and self._numeric_host(data['host'],data['group'])
            if not eligible:
                out.extend(lines[i:j+1]);i=j+1;continue
            # Re-guarding an existing explicit numeric check can change scope.
            # The current generated pattern is an unguarded direct MOVE; if it
            # already has a preceding IF, leave its author-defined scope.
            prior=' '.join(self._body(item).upper() for item in lines[max(0,i-3):i])
            if re.search(r'\bIF\s+'+re.escape(ref)+r'\s+IS\s+NUMERIC\b',prior):
                out.extend(lines[i:j+1]);i=j+1;continue
            statements=[f'IF {ref} IS NUMERIC',
                        f'MOVE {ref} TO {data["host"]} OF {data["group"]}',
                        'ELSE',
                        "DISPLAY 'NON-NUMERIC DB2 KEY COMPONENT'",
                        'PERFORM SQLERROR',
                        'END-IF.']
            out.extend(line for statement in statements
                       for line in self.renderer.emit('000000',' ','    '+statement,'00000000'))
            guarded+=1;i=j+1
        if guarded:
            self.messages.append(f'Schema-proven numeric key validation: {guarded}')
        return '\n'.join(out).rstrip()+'\n'

__all__=['SchemaNumericKeyGuard']
