import re
import sys

def go():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        d = f.read()

    dmbay = r"id:'dmbay',name:'Đường Môn',branch:'Bẫy',role:'Bom Nổ Tức Thời',element:'Mộc',emoji:'💣',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Trường phái gài mìn nổ đa dạng. SM 110 mốc đồ, TP 220, SK cao chống đột tử. Dọn quái cực nhanh, săn Boss siêu an toàn.',baseStats:{sm:25,tp:35,sk:25,nl:15},buildGuide:{summary:'Dọn quái bãi siêu nhanh, săn Boss an toàn bằng bẫy Hỏa (Độc Cô Cửu Kiếm).',phases:[{level:'10-60',sm:'Mốc 70',tp:'Mốc 100',sk:'Còn lại',nl:'0',note:'Tăng 1 điểm Bẫy Hỏa (Độc Cô Cửu Kiếm). Max ĐM Thân Pháp lấy tốc chạy'},{level:'60-90',sm:'Mốc 110',tp:'Mốc 220',sk:'150-170',nl:'0',note:'Max Trấn Phái (ĐM Toàn Thư). Max Bẫy 9x Loạn Hoàn Kích lấy giật'},{level:'90+',sm:'110',tp:'Kéo max',sk:'Dồn hết để máu >2k',nl:'0',note:'Kéo Thân pháp max bing để tăng đam và né tránh, còn lại dồn máu'}],calc:{smTarget:110,smReachAt:60,tpRate:[{f:1,t:150,p:2}],nlFixed:0}}"

    dmdao = r"id:'dmdao',name:'Đường Môn',branch:'Phi Đao',role:'Sát Thủ Cận Chiến',element:'Mộc',emoji:'🗡️',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Sát thủ áp sát, ném phi đao tốc độ đánh cực cao, sát thương đột biến. SM 110, TP kéo max, SK vừa đủ.',baseStats:{sm:25,tp:35,sk:25,nl:15},buildGuide:{summary:'Lối chơi áp sát ném dao nhanh (max tốc 100), cần Thân pháp cực cao để không hụt.',phases:[{level:'10-60',sm:'Mốc 70',tp:'Tăng mạnh',sk:'Vừa đủ',nl:'0',note:'Max Phi Đao Pháp, tăng tốc đánh. Máu giấy nên nâng cẩn thận'},{level:'60-90',sm:'Mốc 110',tp:'Mốc 220',sk:'150-170',nl:'0',note:'Max Trấn Phái. Dồn điểm SK để đạt 1k5-2k máu chống đột tử'},{level:'90+',sm:'110',tp:'Kéo max',sk:'Vừa đủ',nl:'0',note:'Max Tiểu Lý Phi Đao (9x) nhảy chí mạng cực cao. Kéo full Thân Pháp'}],calc:{smTarget:110,smReachAt:60,tpRate:[{f:1,t:150,p:3}],nlFixed:0}}"

    dmno = r"id:'dmno',name:'Đường Môn',branch:'Tụ Tiễn/Nỏ',role:'Xạ Thủ Tầm Xa',element:'Mộc',emoji:'🏹',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Sử dụng nỏ bắn liên hoàn tầm xa diện rộng. Tốc độ ra chiêu nhanh nhất Đường Môn.',baseStats:{sm:25,tp:35,sk:25,nl:15},buildGuide:{summary:'Xạ thủ Tống Kim bảo kê bãi train. Tầm đánh cực xa, xả tiễn liên tục.',phases:[{level:'10-60',sm:'Mốc 70',tp:'Tăng mạnh',sk:'Vừa đủ',nl:'0',note:'Max Tụ Tiễn Pháp lấy dam cơ bản'},{level:'60-90',sm:'Mốc 110',tp:'Mốc 220',sk:'150-170',nl:'0',note:'Max Trấn Phái. Bơm SK lên 1k5 máu tránh đột tử'},{level:'90+',sm:'110',tp:'Kéo max',sk:'Vừa đủ',nl:'0',note:'Max Bạo Vũ Lê Hoa (9x) bắn 10 tia. Cày TP cực cao để lấy dam/chính xác'}],calc:{smTarget:110,smReachAt:60,tpRate:[{f:1,t:150,p:3}],nlFixed:0}}"

    dmtieu = r"id:'dmtieu',name:'Đường Môn',branch:'Phi Tiêu',role:'Ám Khí Bạo Kích',element:'Mộc',emoji:'🎯',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Phóng tiêu ám khí, cấu rỉa liên tục từ xa. Máu giấy đam to, cần micro.',baseStats:{sm:25,tp:35,sk:25,nl:15},buildGuide:{summary:'Ám Khí (Phi Tiêu). Dồn Thân Pháp lấy lực tay & cực kỳ dồn SK để khỏi nằm sấp.',phases:[{level:'10-60',sm:'Mốc 70',tp:'Tăng mạnh',sk:'Vừa đủ',nl:'0',note:'Max Ám Khí Pháp thuật'},{level:'60-90',sm:'Mốc 110',tp:'Mốc 220',sk:'150-170',nl:'0',note:'Max Trấn Phái. Ưu tiên SK đạt ngưỡng 1k5 máu'},{level:'90+',sm:'110',tp:'Kéo max',sk:'Vừa đủ',nl:'0',note:'Max Cửu Cung Phi Tinh (9x). Kéo max TP lấy hit rate an toàn'}],calc:{smTarget:110,smReachAt:60,tpRate:[{f:1,t:150,p:3}],nlFixed:0}}"

    d = re.sub(r'id:\'dmbay\'.*?calc:\{.*?\}', dmbay, d, count=1)
    d = re.sub(r'id:\'dmdao\'.*?calc:\{.*?\}', dmdao, d, count=1)
    d = re.sub(r'id:\'dmno\'.*?calc:\{.*?\}', dmno, d, count=1)
    d = re.sub(r'id:\'dmtieu\'.*?calc:\{.*?\}', dmtieu, d, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(d)
    print("Done writing index.html with duong mon fixes.")

if __name__ == '__main__':
    go()
