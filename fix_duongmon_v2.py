import re

def go():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        d = f.read()

    dmbay = r"id:'dmbay',name:'Đường Môn',branch:'Bẫy',role:'Bom Nổ Tức Thời',element:'Mộc',emoji:'💣',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Trường phái gài mìn nổ đa dạng. SM 70-110, TP 220, SK 150-170, Không cần vũ khí xịn. Dọn quái cực nhanh.',baseStats:{sm:25,tp:35,sk:25,nl:15},buildGuide:{summary:'Dọn quái bãi siêu nhanh, săn Boss an toàn. Phụ thuộc bẫy nên rải máu cao, không màng vũ khí tốc đánh.',phases:[{level:'10-60',sm:'Mốc 70',tp:'Mốc 100',sk:'Còn lại',nl:'0',note:'Tăng 1 điểm Bẫy Hỏa (Độc Cô Cửu Kiếm). Max ĐM Thân Pháp lấy tốc chạy'},{level:'60-90',sm:'Mốc 110',tp:'Mốc 220',sk:'150-170',nl:'0',note:'Max Trấn Phái (ĐM Toàn Thư). Max Bẫy 9x Loạn Hoàn Kích lấy giật'},{level:'90+',sm:'110',tp:'Mốc 220',sk:'Mốc 150-170',nl:'0',note:'Đạt 220 TP mang Thần Tê Linh. Nhồi 150-170 Sinh Khí vững trụ rải bẫy.'}],calc:{smTarget:110,smReachAt:60,tpRate:[{f:1,t:90,p:2}],nlFixed:0}}"

    dmdao = r"id:'dmdao',name:'Đường Môn',branch:'Phi Đao',role:'Sát Thủ Cận Chiến',element:'Mộc',emoji:'🗡️',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Sát thủ áp sát tốc độ cao. Vũ khí cần Tốc Đánh. SM 110-165, TP max, SK 120-150.',baseStats:{sm:25,tp:35,sk:25,nl:15},buildGuide:{summary:'Áp sát ném dao nhanh, bắt buộc vũ khí Tốc đánh cao. Nhồi Thân pháp kịch kim, máu chỉ đủ 120-150.',phases:[{level:'10-60',sm:'Mốc 70',tp:'Tăng mạnh',sk:'Mốc 120',nl:'0',note:'Max Phi Đao Pháp. Sắm đao Tốc đánh cao xả chiêu.'},{level:'60-90',sm:'110-165',tp:'Kéo max',sk:'120-150',nl:'0',note:'Tăng SM 110-165 lấy thêm vật lý. Máu giấy 120-150 để dồn đam, lách né'},{level:'90+',sm:'165',tp:'Max (Dồn tất)',sk:'Max 150',nl:'0',note:'Max Trấn Phái và Tiểu Lý Phi Đao (9x). TP kịch kim nổ chí mạng'}],calc:{smTarget:165,smReachAt:90,tpRate:[{f:1,t:150,p:3}],nlFixed:0}}"

    dmno = r"id:'dmno',name:'Đường Môn',branch:'Tụ Tiễn/Nỏ',role:'Xạ Thủ Tầm Xa',element:'Mộc',emoji:'🏹',color:'#2ecc71',colorGlow:'rgba(46,204,113,0.3)',description:'Sử dụng nỏ bắn liên hoàn tầm xa. Nỏ yêu cầu Tốc đánh. SM 110, TP max, SK 150.',baseStats:{sm:25,tp:35,sk:25,nl:15},buildGuide:{summary:'Xạ thủ bắn xa liên tục, Nỏ buộc có Tốc đánh. Thân pháp nhồi kịch liệt, máu tròn mốc 150.',phases:[{level:'10-60',sm:'Mốc 70',tp:'Tăng mạnh',sk:'Vừa đủ',nl:'0',note:'Max Tụ Tiễn Pháp lấy dam cơ bản'},{level:'60-90',sm:'Mốc 110',tp:'Kéo max',sk:'Mốc 150',nl:'0',note:'Giữ SM tròn mốc 110 mặc đồ. Bơm SK dừng ở 150 lấy máu vừa đủ'},{level:'90+',sm:'110',tp:'Max (Dồn tất)',sk:'150',nl:'0',note:'Max Trấn Phái và Bạo Vũ Lê Hoa. Kéo TP kịch trần lấy tốc độ và hit rate.'}],calc:{smTarget:110,smReachAt:60,tpRate:[{f:1,t:150,p:3}],nlFixed:0}}"

    d = re.sub(r'id:\'dmbay\'.*?calc:\{.*?\}', dmbay, d, count=1)
    d = re.sub(r'id:\'dmdao\'.*?calc:\{.*?\}', dmdao, d, count=1)
    d = re.sub(r'id:\'dmno\'.*?calc:\{.*?\}', dmno, d, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(d)
    print("Done v2 fixes.")

if __name__ == '__main__':
    go()
