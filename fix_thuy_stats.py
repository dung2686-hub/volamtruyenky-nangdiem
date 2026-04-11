import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_thuy = '{sm:25,tp:25,sk:25,nl:25}'

targets = ['nmkiem', 'nmbuff', 'tydao', 'tysongdao']

for char_id in targets:
    pattern = r"({id:'" + char_id + r"',.*?baseStats:)\{[^\}]+\}"
    def replacer(match):
        return match.group(1) + correct_thuy
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Thuy element (Nga My, Thuy Yen) base stats to match screenshot: 25/25/25/25.")
