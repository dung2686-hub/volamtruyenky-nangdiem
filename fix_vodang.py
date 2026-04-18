import re

def go():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        d = f.read()

    vdkhik = r"id:'vdkhik',name:'Võ Đang',branch:'Khí (Quyền)',role:'Sấm Sét Nội',element:'Thổ',emoji:'🌀',color:'#9b59b6',colorGlow:'rgba(155,89,182,0.3)',description:'Vua choáng diện rộng, săn boss siêu đỉnh. Thiên Địa Vô Cực. Dùng Tọa Vọng Vô Ngã (khiên mana). SM 70-110, TP 0, Máu 1k5-2k, Dồn full Nội công.',baseStats:{sm:20,tp:15,sk:25,nl:40},buildGuide:{summary:'Quyền Võ Đang cực mạnh Tống Kim và săn Boss. Lấy Tọa Vọng bù máu, bơm căng Nội Công.',phases:[{level:'10-50',sm:'Mốc 70',tp:'0',sk:'Mốc 1k5',nl:'Tăng mạnh',note:'Max VĐ Quyền Pháp. 1đ Thái Cực Quyền tiết kiệm mana.'},{level:'38-60',sm:'Mốc 110',tp:'0',sk:'1k5-2k',nl:'Tăng mạnh',note:'5-15đ Tọa Vọng Vô Ngã. Cấp 60 Max Trấn Phái lập tức.'},{level:'90+',sm:'110 (Mặc đồ)',tp:'0',sk:'Cố định 1k5-2k',nl:'Dồn tất (Gánh sát thương)',note:'Max Thiên Địa Vô Cực (9x). Nội công sinh dam và Shield.'}],calc:{smTarget:110,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:-1}}"

    vdkiem = r"id:'vdkiem',name:'Võ Đang',branch:'Kiếm Pháp',role:'Sát Thủ Nhanh',element:'Thổ',emoji:'🗡️',color:'#9b59b6',colorGlow:'rgba(155,89,182,0.3)',description:'Áp sát chém nhanh, hiệu ứng choáng liên tục. Cần đồ Chuyển Hóa ST=>NL. SM 165-260, TP 100-150, SK dồn điểm, NL 100-150.',baseStats:{sm:20,tp:15,sk:25,nl:40},buildGuide:{summary:'Ngoại công áp sát tốc độ cao. Cầm đồ chuyển hóa ST vào năng lượng, bơm Tọa Vọng và Thất Tinh.',phases:[{level:'10-50',sm:'Tăng mạnh',tp:'Mốc 100',sk:'Vừa đủ',nl:'Mốc 100',note:'Max Võ Đang Kiếm Pháp.'},{level:'60-90',sm:'165-260',tp:'Mốc 150',sk:'Còn lại',nl:'Mốc 150',note:'Max Trấn Phái. TP ~100-150 lấy chính xác. NL 150 đủ xài Khiên.'},{level:'90+',sm:'Mốc 165-260',tp:'100-150',sk:'Dồn tất (Chịu đòn)',nl:'100-150',note:'Max Tam Hoàn Thao Nguyệt. Nâng Tọa Vọng, Thất Tinh Trận.'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:1}],nlFixed:150}}"

    d = re.sub(r'id:\'vdkhik\'.*?calc:\{.*?\}', vdkhik, d, count=1)
    d = re.sub(r'id:\'vdkiem\'.*?calc:\{.*?\}', vdkiem, d, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(d)
    print("Done vodang fixes.")

if __name__ == '__main__':
    go()
