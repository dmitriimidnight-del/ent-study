# Сборка: python3 build.py math-data.json math.html numbers      (этап 2: одна тема)
#         python3 build.py math-data.json math.html all           (этап 3: все темы)
import json, sys
src, out, *topics = sys.argv[1:]
d = json.load(open(src, encoding='utf-8'))
if topics and topics != ['all']:
    d['lessons'] = [l for l in d['lessons'] if l['topic'] in topics]
tpl = open('app-template.html', encoding='utf-8').read()
js = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
open(out, 'w', encoding='utf-8').write(tpl.replace('/*__DATA__*/null', js))
print(out, len(d['lessons']), 'lessons')
