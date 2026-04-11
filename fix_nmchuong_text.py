import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix nmchuong text
pattern = r"({id:'nmchuong'.*?phases:\[\{level:'1-90',sm:'165',tp:'0',sk:)'Vừa đủ'(,nl:)'Dồn hết'(,note:'Chiêu tốn rất nhiều Mana'\},\{level:'90-150',sm:'165',tp:'0',sk:)'Còn lại'(,nl:)'Dồn hết'(,note:'Phong Sương Toái Ảnh dồn damage làm chậm'\})\]"

def replacer(match):
    return match.group(1) + "'Dồn hết'" + match.group(2) + "'Khoảng 200 điểm'" + match.group(3) + "'Dồn hết'" + match.group(4) + "'Kịch trần Huyết'" + match.group(5)
    
content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated text for Nga My Chuong to reflect high Vitality")
