import json

with open('encuesta_dump.json', encoding='utf-8') as f:
    d = json.load(f)

data = dict(
    instructores=d['INSTRUCTORES']['values'],
    cursos=d['CURSOS']['values'],
    bases=d['BASES']['values'],
    headers=dict(
        instructores=d['INSTRUCTORES']['header'],
        cursos=d['CURSOS']['header'],
        bases=d['BASES']['header'],
    ),
)
with open('encuesta_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
print('instructores:', len(data['instructores']))
print('cursos:', len(data['cursos']))
print('bases:', len(data['bases']))
