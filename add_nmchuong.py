import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_char = """  {id:'nmchuong',name:'Nga My',branch:'Chưởng Pháp',role:'Khống Chế Băng',element:'Thủy',emoji:'❄️',color:'#3498db',colorGlow:'rgba(52,152,219,0.3)',description:'Phiên bản pháp sư hệ Thủy với sát thương Nội Công đánh từ xa, nhồi băng đóng băng đối thủ cực khó chịu.',baseStats:{sm:25,tp:25,sk:25,nl:25},buildGuide:{summary:'Thuần Nội Công và Sinh Khí để ném băng cấu rỉa liên tục.',phases:[{level:'1-90',sm:'165',tp:'0',sk:'Vừa đủ',nl:'Dồn hết',note:'Chiêu tốn rất nhiều Mana'},{level:'90-150',sm:'165',tp:'0',sk:'Còn lại',nl:'Dồn hết',note:'Phong Sương Toái Ảnh dồn damage làm chậm'}],calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:200}},skills:[{name:'Phong Sương Toái Ảnh',type:'Chưởng Pháp',priority:1,desc:'Chưởng băng nội công 90',level:'9x'},{name:'Phật Tâm Từ Bi',type:'Trấn Phái',priority:2,desc:'Kháng cực lớn',level:'6x'},{name:'Lưu Thủy',type:'Vòng sáng',priority:3,desc:'Buff tốc chạy',level:'3x'},{name:'Băng Tâm Ngọc Quyết',type:'Hỗ trợ',priority:4,desc:'Buff hồi nội lực KHỦNG',level:'6x'},{name:'Nga My Chưởng Pháp',type:'Cơ bản',priority:5,desc:'Tăng sát thương chưởng',level:'1x'},{name:'Tứ Tượng Đồng Quy',type:'Chưởng',priority:6,desc:'Chiêu 60',level:'6x'}],equipment:[{stat:'Tốc độ xuất chiêu',importance:'⭐⭐⭐⭐⭐',note:'Ra chưởng liên tục nhồi dam'},{stat:'Băng sát Nội công',importance:'⭐⭐⭐⭐',note:'Đóng băng sâu'}]},
"""

# Find nmkiem exactly and append nmchuong after it
pattern = r"({id:'nmkiem'.*?\}\},skills:\[.*?\]\},?)"

def replacer(match):
    return match.group(1) + '\n' + new_char
    
content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added Nga My Chuong to the characters array.")
