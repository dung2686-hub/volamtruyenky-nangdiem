import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

targets = ['tvthuong', 'nmbuff', 'cbchuong', 'tnthuong', 'clkiem', 'vdkhik']

for char_id in targets:
    # Right now, they look like 'nlFixed:50},skills:['
    # We need them to be 'nlFixed:50}},skills:['
    pattern = r"({id:'" + char_id + r"'.*?calc:\{.*?nlFixed:[^,\}]+)(\},skills:\[)"
    
    def replacer(match):
        return match.group(1) + '}}' + match.group(2)[1:] # replace },skills:[ with }},skills:[
        
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Restored the second missing closing brace for buildGuide.")
