import re

def go():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        d = f.read()

    vdkiem_new = r"id:'vdkiem',name:'Võ Đang',branch:'Kiếm Pháp',role:'Sát Thủ Nhanh',element:'Thổ',emoji:'🗡️',color:'#9b59b6',colorGlow:'rgba(155,89,182,0.3)',description:'Áp sát chém nhanh. Mana là Máu nhờ Tọa Vọng vô ngã. SM 165-260, TP 100-150, NL 100-150. SK ném 0.',baseStats:{sm:20,tp:15,sk:25,nl:40},buildGuide:{summary:'KHÔNG tăng Sinh Khí. Nội Công quan trọng hơn SK vì nuôi Khiên (Mana là máu). SM lấy đam, TP lấy Hit Rate.',phases:[{level:'10-50',sm:'Tăng mạnh',tp:'Mốc 100',sk:'0 / Mốc 1k bảo hiểm',nl:'Dồn điểm (Ưu tiên)',note:'Max Võ Đang Kiếm Pháp. Bơm Nội lực nuôi Khiên.'},{level:'60-90',sm:'165-260',tp:'100-150',sk:'Tối đa 1k-1k2',nl:'100-150',note:'Max Trấn Phái. TP rất cần để đánh không miss.'},{level:'90+',sm:'Mốc 165-260',tp:'100-150',sk:'Còn lại hoặc 0',nl:'100-150',note:'Max Tam Hoàn Thao Nguyệt. Tọa Vọng Vô Ngã max sau cùng lấy rate hấp thụ sát thương cao nhất.'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:1}],nlFixed:150}}"

    d = re.sub(r'id:\'vdkiem\'.*?calc:\{.*?\}', vdkiem_new, d, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(d)
    print("Done v2 fixes for Vo Dang Kiem.")

if __name__ == '__main__':
    go()
