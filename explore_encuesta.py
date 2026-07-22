import os, openpyxl

folder = os.path.dirname(os.path.abspath(__file__))
target = None
for fn in os.listdir(folder):
    if fn.lower().endswith('.xlsx'):
        target = os.path.join(folder, fn)
        break

print('Archivo:', target)
wb = openpyxl.load_workbook(target, data_only=True)
print('Hojas:', wb.sheetnames)
for name in wb.sheetnames:
    ws = wb[name]
    print(f'--- {name}: {ws.max_row} filas x {ws.max_column} cols ---')
    for r in range(1, min(4, ws.max_row) + 1):
        print(' ', [ws.cell(row=r, column=c).value for c in range(1, min(ws.max_column, 10) + 1)])
