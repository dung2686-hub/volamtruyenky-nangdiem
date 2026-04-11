import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Kim
content = re.sub(r"id:'tl(dao|quyen|bong)',.*?baseStats:\{[^\}]+\}", r"id:'tl\g<1>',\g<0>", content, flags=re.DOTALL)
# Wait, a simple string replacement for each branch might be safer.

base_stats = {
    'tldao': '{sm:35,tp:25,sk:25,nl:15}',
    'tlquyen': '{sm:35,tp:25,sk:25,nl:15}',
    'tlbong': '{sm:35,tp:25,sk:25,nl:15}',
    'tvchuy': '{sm:35,tp:25,sk:25,nl:15}',
    'tvthuong': '{sm:35,tp:25,sk:25,nl:15}',
    'tvdao': '{sm:35,tp:25,sk:25,nl:15}',
    
    'ndchuong': '{sm:20,tp:35,sk:20,nl:25}',
    'nddao': '{sm:20,tp:35,sk:20,nl:25}',
    
    'nmkiem': '{sm:20,tp:15,sk:25,nl:40}',
    'nmbuff': '{sm:20,tp:15,sk:25,nl:40}',
    'tydao': '{sm:20,tp:15,sk:25,nl:40}',
    'tysongdao': '{sm:20,tp:15,sk:25,nl:40}',
    
    'cbchuong': '{sm:25,tp:25,sk:25,nl:25}',
    'cbbong': '{sm:25,tp:25,sk:25,nl:25}',
    'tnthuong': '{sm:25,tp:25,sk:25,nl:25}',
    'tndao': '{sm:25,tp:25,sk:25,nl:25}',
    
    'vdkhik': '{sm:20,tp:20,sk:20,nl:40}',
    'vdkiem': '{sm:20,tp:20,sk:20,nl:40}',
    'cldao': '{sm:20,tp:20,sk:20,nl:40}',
    'clkiem': '{sm:20,tp:20,sk:20,nl:40}',
}

for char_id, stat_str in base_stats.items():
    pattern = r"({id:'" + char_id + r"',.*?baseStats:)\{[^\}]+\}"
    def replacer(match):
        return match.group(1) + stat_str
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated base stats based on element rules.")
