import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("{name:'Độc Tật Lê',type:'Khoanh',priority:3,desc:'Cơ bản nỏ độc',level:'1x'}", "{name:'Tích Lịch Đơn',type:'Cơ bản',priority:3,desc:'Cộng hưởng sát thương Ám Khí',level:'1x'}")
content = content.replace("{name:'Đoạt Hồn Tiêu',type:'Tầm xa',priority:3,desc:'Phi tiêu cơ bản',level:'1x'}", "{name:'Tích Lịch Đơn',type:'Cơ bản',priority:3,desc:'Cộng hưởng sát thương Ám Khí',level:'1x'}")
content = content.replace("{name:'Phi Đao Pháp',type:'Căn bản',priority:3,desc:'Phi đao cơ bản',level:'1x'}", "{name:'Tích Lịch Đơn',type:'Cơ bản',priority:3,desc:'Cộng hưởng sát thương Ám Khí',level:'1x'}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Tích Lịch Đơn.")
