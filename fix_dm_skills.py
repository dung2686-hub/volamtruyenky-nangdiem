import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate the exact JSON replacement chunks for the characters
dm_updates = {
    'dmno': "[{name:'Bạo Vũ Lê Hoa',type:'Tụ Tiễn',priority:1,desc:'Sát thương dồn nỏ tiễn',level:'9x'},{name:'Tâm Nhãn',type:'Trấn Phái',priority:2,desc:'Tăng chí mạng bạo kích',level:'6x'},{name:'Thiên La Địa Võng',type:'Tụ Tiễn',priority:3,desc:'Chiêu 60 Nỏ tiễn',level:'6x'},{name:'Mạn Thiên Hoa Vũ',type:'Tụ Tiễn',priority:4,desc:'Chiêu 30 Nỏ tiễn',level:'3x'},{name:'Phích lịch đơn',type:'Nhập môn',priority:5,desc:'Cơ bản nhập môn',level:'1x'}]",
    'dmtieu': "[{name:'Cửu Cung Phi Tinh',type:'Phi Tiêu',priority:1,desc:'Tuyệt kỹ phi tiêu 90',level:'9x'},{name:'Tâm Nhãn',type:'Trấn Phái',priority:2,desc:'Trấn phái tăng sát thương',level:'6x'},{name:'Tán Hoa Tiêu',type:'Phi Tiêu',priority:3,desc:'Chiêu 60 Phi tiêu',level:'6x'},{name:'Đoạt Hồn Tiêu',type:'Phi Tiêu',priority:4,desc:'Chiêu 30 phi tiêu',level:'3x'},{name:'Ám khí Đường Môn',type:'Hỗ trợ',priority:5,desc:'Tăng hỏa lực ám khí',level:'1x'}]",
    'dmdao': "[{name:'Nhiếp Hồn Nguyệt Ảnh',type:'Phi Đao',priority:1,desc:'Tuyệt kỹ phi đao 90',level:'9x'},{name:'Tâm Nhãn',type:'Trấn Phái',priority:2,desc:'Trấn phái tăng sát thương',level:'6x'},{name:'Tiểu Lý Phi Đao',type:'Phi Đao',priority:3,desc:'Chiêu 60 Phi đao',level:'6x'},{name:'Truy Tâm Tiễn',type:'Phi Đao',priority:4,desc:'Chiêu 30 Phi đao',level:'3x'},{name:'Phích lịch đơn',type:'Nhập môn',priority:5,desc:'Cơ bản nhập môn',level:'1x'}]",
    'dmbay': "[{name:'Loạn Hoàn Kích',type:'Cạm Bẫy',priority:1,desc:'Bẫy 90 đẩy lùi kẻ địch',level:'9x'},{name:'Tâm Nhãn',type:'Trấn Phái',priority:2,desc:'Tăng bạo kích',level:'6x'},{name:'Lôi Kích Thuật',type:'Cạm Bẫy',priority:3,desc:'Bẫy 50 hệ Lôi',level:'5x'},{name:'Xuyên Tâm Thích',type:'Cạm Bẫy',priority:4,desc:'Bẫy 30',level:'3x'},{name:'Độc Thử Cốt',type:'Cạm Bẫy',priority:5,desc:'Bẫy 20',level:'2x'}]"
}

for char_id, skills_json_str in dm_updates.items():
    pattern = r"({id:'" + char_id + r"',.*?)skills:\[.*?\](.*?\})"
    
    def replace_skills(match):
        return match.group(1) + "skills:" + skills_json_str + match.group(2)
        
    content = re.sub(pattern, replace_skills, content, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated DM skills with OCR accurate image data.")
