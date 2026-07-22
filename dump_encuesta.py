# -*- coding: utf-8 -*-
import os, json, openpyxl
from collections import Counter

folder = os.path.dirname(os.path.abspath(__file__))
target = None
for fn in os.listdir(folder):
    if fn.lower().endswith('.xlsx'):
        target = os.path.join(folder, fn)
        break

wb = openpyxl.load_workbook(target, data_only=True)

out = {}
for name in wb.sheetnames:
    ws = wb[name]
    header = ws.cell(row=1, column=1).value
    vals = []
    for r in range(2, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if v is not None:
            vals.append(str(v).strip())
    out[name] = dict(header=header, n=len(vals), values=vals)

with open('encuesta_dump.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

for name, d in out.items():
    print(f'=== {name} ({d["n"]}) — header: {d["header"]!r} ===')
    c = Counter(d['values'])
    dups = [v for v, n in c.items() if n > 1]
    if dups:
        print('  DUPLICADOS:', dups)
    blanks = sum(1 for v in d['values'] if v == '')
    if blanks:
        print('  VALORES VACIOS:', blanks)
    # entradas con digitos sueltos o rarezas
    weird = [v for v in d['values'] if any(ch.isdigit() for ch in v)]
    if weird:
        print('  CONTIENEN DIGITOS:', weird)
    print()
