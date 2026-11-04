"""Normalize SQL body geometry after late SQL generation, without editing tokens.

A line generated as `   SELECT` sits in COBOL Area A in fixed format;
SQL bodies belong in Area B.  This pass only adds whitespace to SQL body
lines when the entire logical line still fits in columns 8-72.
"""
from __future__ import annotations
import re

class SqlBodyAreaBNormalizer:
    def __init__(self, min_indent=4):
        self.min_indent=min_indent
        self.messages: list[str]=[]

    def compose(self,text):
        self.messages.clear()
        if not text:return text
        output=[];in_procedure=False;in_sql=False;fixed=0;unresolved=0
        for line in text.splitlines():
            is_fixed=len(line)>=80 and line[:6].isdigit() and line[72:80].isdigit()
            if not is_fixed or line[6] in ('*','/','D','d'):
                output.append(line);continue
            body=line[7:72]
            upper=body.strip().upper()
            if re.match(r'^PROCEDURE\s+DIVISION\b',upper):
                in_procedure=True
            if in_procedure and re.match(r'^EXEC\s+SQL\b',upper):
                in_sql=True
            elif in_sql and upper and not re.match(r'^END-EXEC\b',upper):
                leading=len(body)-len(body.lstrip())
                if leading<self.min_indent:
                    newbody=' '*self.min_indent+body.strip()
                    if len(newbody)<=65:
                        line=line[:7]+newbody.ljust(65)+line[72:]
                        fixed+=1
                    else:
                        unresolved+=1
            if in_sql and re.search(r'\bEND-EXEC\b',upper):
                in_sql=False
            output.append(line)
        if fixed:self.messages.append(f'SQL body Area B alignment: {fixed} line(s)')
        if unresolved:self.messages.append(f'SQL body Area B alignment unproven: {unresolved} line(s)')
        return '\n'.join(output).rstrip()+'\n'

__all__=['SqlBodyAreaBNormalizer']
