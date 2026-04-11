import re
import json

content = open('index.html', encoding='utf-8').read()
chars = re.findall(r"id:'([^']+)',name:'([^']+)',branch:'([^']+)'", content)
open('chars.txt', 'w', encoding='utf-8').write('\n'.join([f'{c[0]}: {c[1]} - {c[2]}' for c in chars]))
