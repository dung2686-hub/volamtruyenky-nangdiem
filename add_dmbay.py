import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

dmbay_data = """  {id:'dmbay',name:'Đường Môn',branch:'Bẫy (Boom)',role:'Gài bom thủ cứ điểm',element:'Mộc',emoji:'💣',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Trường phái gài mìn nổ sát thương tức thời siêu khủng. Địch dẫm phải là bay màu.',baseStats:{sm:20,tp:30,sk:20,nl:10},buildGuide:{summary:'SM vừa đủ, dồn cục vào Sinh Khí trâu nhất có thể.',phases:[{level:'1-90',sm:'Mốc Áo',tp:'0',sk:'Dồn hết',nl:'0',note:'Bẫy không cần chính xác nên bỏ qua TP'},{level:'90-150',sm:'165',tp:'0',sk:'Dồn hết',nl:'0',note:'Mê Tung Ảnh thả diều đặt bẫy bất bại'}],calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:0}},skills:[{name:'Loạn Hoàn Kích',type:'Trap 9x',priority:1,desc:'Chuỗi lựu đạn gây đẩy lùi',level:'9x'},{name:'Tâm Nhãn',type:'Trấn Phái',priority:2,desc:'Tăng sinh lực và bạo kích',level:'6x'},{name:'Độc Lôi Trận',type:'Trap Bộc',priority:3,desc:'Bẫy độc rút máu',level:'3x'},{name:'Xuyên Tâm Thích',type:'Trap Choáng',priority:4,desc:'Bẫy dưới chân',level:'1x'},{name:'Độc Thích Cốt',type:'Aura',priority:5,desc:'Aura hệ Mộc',level:'3x'}],equipment:[{stat:'Kỹ năng môn phái',importance:'⭐⭐⭐⭐⭐',note:'Kỹ năng làm bẫy sát thương cực đại'},{stat:'Tốc độ chạy',importance:'⭐⭐⭐⭐',note:'Chạy đặt bẫy lả lướt'}]},
"""

# Find where dmdao is and insert dmbay right after it
# We'll use regex to find dmdao block ending
match = re.search(r"({id:'dmdao'.*?\}),", content)
if match:
    # insert dmbay
    replacement = match.group(0) + "\n" + dmbay_data
    content = content.replace(match.group(0), replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added dmbay successfully!")
else:
    print("Could not find dmdao")
