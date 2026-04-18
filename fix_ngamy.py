import re
import sys

def go():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        d = f.read()

    nmbuff = r"id:'nmbuff',name:'Nga My',branch:'Support',role:'Healer Tối Thượng',element:'Thủy',emoji:'💚',color:'#3498db',colorGlow:'rgba(52,152,219,0.3)',description:'Trụ cột của mọi Party. SK tăng max, NL vừa đủ. Hồi máu, buff kháng tất cả, hồi sinh đồng đội.',baseStats:{sm:25,tp:25,sk:25,nl:25},buildGuide:{summary:'Thuần đi theo để hỗ trợ team. Chú trọng lớn nhất vào Sinh khí để sống dai.',phases:[{level:'10-30',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Tăng 1đ Mộng Điệp và chiêu hồi máu cơ bản'},{level:'40-60',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Ưu tiên Max Mộng Điệp, sau đó Phật Tâm Từ Hữu'},{level:'80-90+',sm:'Mốc 110',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Nâng SM lên 110 mặc đồ cấp cao, Sinh khí vẫn là chủ đạo'}],calc:{smTarget:110,smReachAt:80,tpRate:[{f:1,t:150,p:0}],nlFixed:50}}"

    nmchuong = r"id:'nmchuong',name:'Nga My',branch:'Chưởng Pháp',role:'Khống Chế Băng',element:'Thủy',emoji:'❄️',color:'#3498db',colorGlow:'rgba(52,152,219,0.3)',description:'Pháp sư Nội Công hệ Thủy áp sát. SK nhiều. Phong Sương Toái Ảnh ném băng đóng băng.',baseStats:{sm:25,tp:25,sk:25,nl:25},buildGuide:{summary:'Nội Công áp sát. Dồn toàn bộ vào Sinh Khí để sinh tồn cận chiến.',phases:[{level:'10-30',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'0',note:'Max Nga My Chưởng Pháp để lấy đam. 1đ Mộng Điệp'},{level:'60',sm:'Theo đồ',tp:'0',sk:'Dồn hết',nl:'0',note:'Bắt buộc Max Trấn Phái Cửu Dương Công ngay lập tức'},{level:'90+',sm:'Mốc 110',tp:'0',sk:'Dồn hết',nl:'0',note:'SM mốc 110 mặc đồ. Nâng ngập skill chiến (Phong Sương, Tứ Tượng)'}],calc:{smTarget:110,smReachAt:90,tpRate:[{f:1,t:150,p:0}],nlFixed:200}}"

    nmkiem = r"id:'nmkiem',name:'Nga My',branch:'Kiếm Pháp',role:'Kiếm Sĩ Băng Sát',element:'Thủy',emoji:'⚔️',color:'#3498db',colorGlow:'rgba(52,152,219,0.3)',description:'Kiếm pháp Ngoại Công hệ Thủy, sát thương băng sát cực lớn, chém đóng băng đối thủ đứng im.',baseStats:{sm:25,tp:25,sk:25,nl:25},buildGuide:{summary:'Ngoại Công cận chiến. SM & TP là quan trọng nhất (đam và chính xác), SK vừa đủ sống sót.',phases:[{level:'10-30',sm:'35-70',tp:'Cần thiết',sk:'Vừa đủ',nl:'0',note:'Dùng Phi Hành, 1đ Mộng Điệp để hồi phục'},{level:'60',sm:'Theo đồ',tp:'Trọng tâm',sk:'Vừa đủ',nl:'0',note:'Bắt buộc Max Trấn Phái Cửu Dương Công ngay lập tức'},{level:'90+',sm:'110+',tp:'Kéo max',sk:'Vừa đủ',nl:'0',note:'Dùng Tam Nga. SM mốc 110 mặc đồ cấp cao, kéo max TP'}],calc:{smTarget:110,smReachAt:90,tpRate:[{f:1,t:150,p:1}],nlFixed:50}}"

    d = re.sub(r'id:\'nmbuff\'.*?calc:\{.*?\}', nmbuff, d, count=1)
    d = re.sub(r'id:\'nmchuong\'.*?calc:\{.*?\}', nmchuong, d, count=1)
    d = re.sub(r'id:\'nmkiem\'.*?calc:\{.*?\}', nmkiem, d, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(d)
    print("Done writing index.html with nga my fixes.")

if __name__ == '__main__':
    go()
