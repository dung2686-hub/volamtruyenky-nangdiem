import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_tho = '{sm:20,tp:15,sk:25,nl:40}'

targets = ['vdkhik', 'vdkiem', 'cldao', 'clkiem']

for char_id in targets:
    pattern = r"({id:'" + char_id + r"',.*?baseStats:)\{[^\}]+\}"
    def replacer(match):
        return match.group(1) + correct_tho
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Tho element (Vo Dang, Con Lon) base stats to match screenshot: 20/15/25/40.")
