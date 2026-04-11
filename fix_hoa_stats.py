import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

correct_hoa = '{sm:30,tp:20,sk:30,nl:20}'

targets = ['cbchuong', 'cbbong', 'tnthuong', 'tndao']

for char_id in targets:
    pattern = r"({id:'" + char_id + r"',.*?baseStats:)\{[^\}]+\}"
    def replacer(match):
        return match.group(1) + correct_hoa
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Hoa element (Cai Bang, Thien Nhan) base stats to match screenshot: 30/20/30/20.")
