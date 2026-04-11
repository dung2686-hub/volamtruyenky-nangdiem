import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

targets = ['tvthuong', 'nmbuff', 'cbchuong', 'tnthuong', 'clkiem', 'vdkhik']

for char_id in targets:
    # Find the chunk starting with char_id and ending with ,skills:
    # We look for the FIRST ',skills:' after the char_id
    pattern = r"({id:'" + char_id + r"'.*?calc:\{.*?nlFixed:[^\}]+)(,skills:\[)"
    
    # We just add a '}' before ',skills:['
    def replacer(match):
        return match.group(1) + '}' + match.group(2)
        
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Restored missing closing braces.")
