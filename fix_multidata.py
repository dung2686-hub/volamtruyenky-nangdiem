"""
Fix index.html character data based on multi-source verified information.
Sources: KisuGame, VoLamThienHa, sgame.vn, forumvi.com, community
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = []

# ═══════════════════════════════════════════════════════════
# 1. NGA MY KIẾM - Fix: Nội Công → NGOẠI CÔNG
# VoLamThienHa xác nhận: Kiếm = Ngoại công, cần SM+TP
# ═══════════════════════════════════════════════════════════

# 1a. Role
content = content.replace(
    "{id:'nmkiem',name:'Nga My',branch:'Kiếm Pháp',role:'Băng Sát Nội'",
    "{id:'nmkiem',name:'Nga My',branch:'Kiếm Pháp',role:'Kiếm Sĩ Băng Sát'"
)

# 1b. Description
content = content.replace(
    "description:'Hệ kiếm mang sát thương băng siêu lớn, đóng băng đối thủ đứng im.'",
    "description:'Kiếm pháp Ngoại Công hệ Thủy, sát thương băng sát cực lớn, chém đóng băng đối thủ đứng im.'"
)

# 1c. Build summary
content = content.replace(
    "summary:'Tăng cực nhiều Nội lực. Sinh khí ít.'",
    "summary:'Ngoại Công kiếm băng. SM nhiều (lực tay), TP cần (chính xác), NL vừa đủ dùng skill.'"
)

# 1d. Phases - nmkiem
content = content.replace(
    "phases:[{level:'1-90',sm:'Mốc Áo',tp:'0',sk:'Vừa đủ',nl:'Dồn hết',note:'Skill 9x tốn quá nhiều mana'},{level:'90-150',sm:'165',tp:'0',sk:'Còn lại',nl:'Dồn hết',note:'Tam Ngã Kiếm đóng băng cực sâu'}],calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:150}",
    "phases:[{level:'10-30',sm:'35-70',tp:'Cần thiết',sk:'Vừa đủ',nl:'0',note:'Dùng Phi Hành. 1đ Mộng Điệp hồi máu'},{level:'60',sm:'Theo đồ',tp:'Cần thiết',sk:'Vừa đủ',nl:'0',note:'Bắt buộc Max Trấn Phái Cửu Dương Công ngay lập tức'},{level:'90+',sm:'Mốc 110+',tp:'Dồn nhiều',sk:'Vừa đủ',nl:'0',note:'SM 110 mặc đồ. Dùng Tam Nga, tăng mạnh TP lấy chính xác'}],calc:{smTarget:110,smReachAt:90,tpRate:[{f:1,t:150,p:1}],nlFixed:0}"
)

# ═══════════════════════════════════════════════════════════
# 2. THIÊN NHẪN ĐAO - Fix: Ngoại Công → NỘI CÔNG
# VoLamThienHa: TN Đao/Bùa = 100% Sinh khí
# Thiên Vũ Hỏa Lưu Tinh = Nội Công (mưa lửa từ xa)
# ═══════════════════════════════════════════════════════════

# 2a. Role
content = content.replace(
    "{id:'tndao',name:'Thiên Nhẫn',branch:'Đao Pháp',role:'Kình Lực Ngoại'",
    "{id:'tndao',name:'Thiên Nhẫn',branch:'Đao Pháp',role:'Pháp Sư Hỏa Nội'"
)

# 2b. Description
content = content.replace(
    "description:'Vân Long Kích kết hợp bùa chú bạo kích ngoại công đoạt mạng.'",
    "description:'Pháp sư Nội Công hệ Hỏa, Thiên Vũ Hỏa Lưu Tinh mưa lửa diện rộng, tốn NL cực nhiều.'"
)

# 2c. Build summary - tndao
content = content.replace(
    "summary:'Thêm SM và SK, đánh cận chiến.'",
    "summary:'Nội Công hỏa sát. SK tăng max, SM đủ mặc đồ, không cần TP (chiêu nội không miss).'"
)

# 2d. Phases + calc - tndao
content = content.replace(
    "phases:[{level:'1-90',sm:'260',tp:'150',sk:'Còn lại',nl:'0',note:'Lực tay rất cao'},{level:'90-150',sm:'300',tp:'150',sk:'Còn lại',nl:'0',note:'Vân Long Kích chém lửa đa mục tiêu'}],calc:{smTarget:300,smReachAt:100,tpRate:[{f:1,t:150,p:1}],nlFixed:0}",
    "phases:[{level:'1-90',sm:'Đủ đồ',tp:'0',sk:'Tăng max',nl:'0',note:'Nội Công, chiêu tốn NL nhưng lấy từ trang bị'},{level:'90-150',sm:'165',tp:'0',sk:'Tăng max',nl:'0',note:'Thiên Vũ Hỏa Lưu Tinh mưa lửa diện rộng'}],calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:0}"
)

# 2e. Equipment - tndao
content = content.replace(
    "equipment:[{stat:'Hỏa sát ngoại',importance:'⭐⭐⭐⭐⭐',note:'Gây dame tay cực lớn'},{stat:'Hút HP',importance:'⭐⭐⭐⭐',note:'Sống lâu ra đòn'}]}",
    "equipment:[{stat:'Hỏa sát Nội',importance:'⭐⭐⭐⭐⭐',note:'Tăng sát thương nội công hỏa'},{stat:'Kỹ năng môn phái',importance:'⭐⭐⭐⭐',note:'Tăng dame chiêu'}]}"
)

# ═══════════════════════════════════════════════════════════
# 3. VÕ ĐANG KHÍ - Fix: smTarget 260 → 110
# VoLamThienHa + KisuGame: SM=110 (đủ đồ trấn phái)
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "summary:'Nội lực là Máu + Công.',phases:[{level:'1-90',sm:'110',tp:'0',sk:'0',nl:'Dồn hết',note:'Tọa Vọng Vô Ngã hút sát thương bằng Nội'},{level:'90-150',sm:'165',tp:'0',sk:'0',nl:'Dồn hết',note:'Bác Cấp Nhi Phục lôi đình sát trận'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:0}],nlFixed:-1}",
    "summary:'Nội lực là Máu + Công. SM chỉ cần 110 đủ đồ trấn phái.',phases:[{level:'1-90',sm:'110',tp:'0',sk:'0',nl:'Dồn hết',note:'Tọa Vọng Vô Ngã hút sát thương bằng Nội'},{level:'90-150',sm:'110',tp:'0',sk:'0',nl:'Dồn hết',note:'Bác Cấp Nhi Phục lôi đình sát trận'}],calc:{smTarget:110,smReachAt:30,tpRate:[{f:1,t:150,p:0}],nlFixed:-1}"
)

# ═══════════════════════════════════════════════════════════
# 4. THIÊN VƯƠNG CHÙY - Fix: smTarget 500 → 380
# Cộng đồng: SM 300-380+, SK 150+
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "calc:{smTarget:500,smReachAt:150,tpRate:[{f:90,t:150,p:1}],nlFixed:0}",
    "calc:{smTarget:380,smReachAt:120,tpRate:[{f:90,t:150,p:1}],nlFixed:0}"
)

# ═══════════════════════════════════════════════════════════
# 5. CÁI BANG CHƯỞNG - Phases đã OK (nlFixed:50, SK max)
#    Chỉ cần sửa nhỏ description để rõ hơn
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Phi Long Tại Thiên rượt đuổi mục tiêu, Hỏa sát nội công cực đỉnh, Kháng Long Hữu Hối.'",
    "description:'Phi Long Tại Thiên rượt đuổi mục tiêu, Hỏa sát Nội Công cực đỉnh. Chiêu tốn NL khủng, cần SK max + NL vừa đủ.'"
)

# ═══════════════════════════════════════════════════════════
# 6. CÁI BANG BỔNG - Fix description rõ hơn
# VoLamThienHa: SM 70%, SK 30%
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Trực diện cận chiến, sát thương Bổng cực nhanh và làm đối phương ngộp.'",
    "description:'Ngoại Công cận chiến. SM 70% SK 30%, băng sát ngoại 95-100. Bổng đánh nhanh làm đối phương ngộp.'"
)

# ═══════════════════════════════════════════════════════════
# 7. NGŨ ĐỘC CHƯỞNG - Sửa rõ hơn cơ chế Độc sát
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Sát thương 100% là Độc sát nên k phụ thuộc SM. Chạy quanh ném bùa là bất bại.'",
    "description:'Sát thương Độc (Nội Công) không phụ thuộc SM. SK tăng max, NL ít. Chạy quanh ném chưởng độc bất bại.'"
)

# ═══════════════════════════════════════════════════════════
# 8. NGŨ ĐỘC ĐAO - Sửa rõ description
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Đao chém trên ngựa diện rộng, lấy bùa giảm phòng địch, chửi vô tận máu.'",
    "description:'Pha Ngoại+Độc, đao chém trên ngựa diện rộng, bùa giảm phòng địch. SM cần, SK dồn hết.'"
)

# ═══════════════════════════════════════════════════════════
# 9. NGA MY CHƯỞNG - Sửa rõ là NỘI CÔNG, NL max
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Phiên bản pháp sư hệ Thủy với sát thương Nội Công đánh từ xa, nhồi băng đóng băng đối thủ cực khó chịu.'",
    "description:'Pháp sư Nội Công hệ Thủy áp sát. SK nhiều. Phong Sương Toái Ảnh ném băng đóng băng.'",
)

# Fix Nga My Chuong build
content = content.replace(
    "summary:'Thuần Nội Công và Sinh Khí để ném băng cấu rỉa liên tục.',phases:[{level:'1-90',sm:'165',tp:'0',sk:'Dồn hết',nl:'Khoảng 200 điểm',note:'Chiêu tốn rất nhiều Mana'},{level:'90-150',sm:'165',tp:'0',sk:'Dồn hết',nl:'Kịch trần Huyết',note:'Phong Sương Toái Ảnh dồn damage làm chậm'}],calc:{smTarget:165,smReachAt:60,tpRate:[{f:1,t:150,p:0}],nlFixed:200}",
    "summary:'Nội Công áp sát. Dồn toàn bộ vào Sinh Khí để sinh tồn cận chiến.',phases:[{level:'10-30',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'0',note:'Max Nga My Chưởng Pháp để lấy đam. 1đ Mộng Điệp'},{level:'60',sm:'Theo đồ',tp:'0',sk:'Dồn hết',nl:'0',note:'Bắt buộc Max Trấn Phái Cửu Dương Công ngay lập tức'},{level:'90+',sm:'Mốc 110',tp:'0',sk:'Dồn hết',nl:'0',note:'SM mốc 110 mặc đồ. Nâng ngập skill chiến (Phong Sương, Tứ Tượng)'}],calc:{smTarget:110,smReachAt:90,tpRate:[{f:1,t:150,p:0}],nlFixed:0}"
)

# ═══════════════════════════════════════════════════════════
# 10. NGA MY BUFF - Sửa rõ là SK max
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Trụ cột không thể thiếu của mọi Party. Hồi máu, buff max kháng, hồi sinh.'",
    "description:'Trụ cột của mọi Party. SK tăng max, NL vừa đủ. Hồi máu, buff kháng tất cả, hồi sinh đồng đội.'"
)

# Fix Nga My Buff (Bút/Hỗ Trợ & Chiến) build
content = content.replace(
    "summary:'Tập trung vào việc sống sót để hỗ trợ team. Sinh khí là chủ đạo.',phases:[{level:'10-30',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'1đ Mộng Điệp & hồi máu. (Đường Chiến max Chưởng Pháp)'},{level:'40-60',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Max Mộng Điệp, sau đó Phật Tâm. (Đường Chiến max Trấn phái 60)'},{level:'80-90+',sm:'Mốc 110',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Nâng SM lên 110 mặc đồ cấp cao, dồn Sinh khí để máu trâu'}],calc:{smTarget:110,smReachAt:80,tpRate:[{f:1,t:150,p:0}],nlFixed:50}",
    "summary:'Thuần đi theo để hỗ trợ team. Chú trọng lớn nhất vào Sinh khí để sống dai.',phases:[{level:'10-30',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Tăng 1đ Mộng Điệp và chiêu hồi máu cơ bản'},{level:'40-60',sm:'35-70',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Ưu tiên Max Mộng Điệp, sau đó Phật Tâm Từ Hữu'},{level:'80-90+',sm:'Mốc 110',tp:'0',sk:'Dồn hết',nl:'Vừa đủ',note:'Nâng SM lên 110 mặc đồ cấp cao, Sinh khí vẫn là chủ đạo'}],calc:{smTarget:110,smReachAt:80,tpRate:[{f:1,t:150,p:0}],nlFixed:0}"
)

# ═══════════════════════════════════════════════════════════
# 11. VÕ ĐANG KIẾM - Sửa rõ hơn description
# sgame.vn: SM~220, TP~100, NL~150
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Tốc độ đánh số 1. Phóng kiếm như mưa, rượt mục tiêu k trượt phát nào.'",
    "description:'Pha Ngoại+Nội. SM~220, TP~100-200, NL~150-350. Tọa Vọng shield bằng NL, kiếm phóng như mưa.'"
)

# ═══════════════════════════════════════════════════════════
# 12. CÔN LÔN ĐAO - Sửa rõ Pha Ngoại
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Gió lốc diện rộng phá nát lớp buff đối thủ, cực kì hữu hiệu công thành chiến.'",
    "description:'Pha Ngoại công. SM 260-300, TP~150. Gió lốc diện rộng phá buff đối thủ, cực hiệu quả công thành chiến.'"
)

# ═══════════════════════════════════════════════════════════
# 13. CÔN LÔN KIẾM - Sửa rõ thuần Nội
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Lôi Động Cửu Thiên giáng sét trúng là đứng yên k lối thoát.'",
    "description:'Thuần Nội Công. SM 165 đủ đồ, NL dồn hết. Lôi Động Cửu Thiên giáng sét trúng là đứng yên không lối thoát.'"
)

# ═══════════════════════════════════════════════════════════
# 14. THIẾU LÂM ĐAO - Sửa description rõ cơ chế
# KisuGame: SM 80%, SK 20%, TP&NL = 0
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Cưỡi ngựa chém nhanh, tốc độ di chuyển cao. Dùng để săn các phái máu giấy.'",
    "description:'Ngoại Công kỵ binh. SM 80% SK 20%, TP&NL=0. Cưỡi ngựa chém tầm xa, tốc độ di chuyển cao, săn phái máu giấy.'"
)

# Fix Thiếu Lâm Đao build
content = content.replace(
    "summary:'SM đủ dùng, TP lấy chính xác, còn lại dồn hết SK.',phases:[{level:'1-30',sm:'Mốc 165',tp:'0',sk:'Còn lại',nl:'0',note:'Cấp 1x xài Quyền dọn bãi cực nhanh'},{level:'30-90',sm:'Mốc 210',tp:'1đ/lv',sk:'Dồn hết',nl:'0',note:'Bắt đầu xài Bổng quạt diện rộng rồi cưỡi ngựa chém'},{level:'90-150',sm:'Mốc 260',tp:'Mốc 150',sk:'Dồn hết',nl:'0',note:'Max trâu bò, máu cực to'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:60,t:150,p:1}],nlFixed:0}",
    "summary:'Vua cày cấp, đánh xa diện rộng. Sức mạnh là sát thương chính.',phases:[{level:'10-50',sm:'70-80%',tp:'0',sk:'20-30%',nl:'0',note:'Max TL Đao Pháp. 1đ Ma Ha Vô Lượng'},{level:'60',sm:'70-80%',tp:'0',sk:'20-30%',nl:'0',note:'Max Trấn Phái Như Lai Thiên Diệp ngay lập tức'},{level:'90+',sm:'70-80%',tp:'0',sk:'Máu > 4000',nl:'0',note:'Max Vô Tướng Trảm, sau đó tăng Dịch Cân Kinh'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:60,t:150,p:0}],nlFixed:0}"
)

# ═══════════════════════════════════════════════════════════
# 15. THIẾU LÂM BỔNG - Sửa description rõ cơ chế
# KisuGame: SM 70%, SK 30%, TP 100-150
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Gom quái cực tốt, phản đòn La Hán Trận. Đi đầu chịu đòn cho team.'",
    "description:'Ngoại Công Tank/AoE. SM 60% SK 40%, không cần TP. Gom quái tốt, phản đòn La Hán Trận, đi đầu chịu đòn cho team.'"
)

# Fix Thiếu Lâm Bổng build
content = content.replace(
    "summary:'SK là ưu tiên nhưng bắt buộc phải có TP để không đánh hụt.',phases:[{level:'1-30',sm:'Mốc 100',tp:'Mốc 50',sk:'Còn lại',nl:'0',note:'Nên xài chiêu Quyền 1x để AoE quái nhanh gọn'},{level:'30-90',sm:'Mốc 200',tp:'Mốc 100',sk:'Dồn hết',nl:'0',note:'Chuyển sang Bổng pháp quét diện rộng'},{level:'90-150',sm:'Mốc 260',tp:'Mốc 150',sk:'Dồn hết',nl:'0',note:'Hoành Tảo Lục Hợp chống đánh Miss'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:1}],nlFixed:0}",
    "summary:'Cỗ xe tăng càn quét, gây hiệu ứng choáng trong Tống Kim.',phases:[{level:'10-50',sm:'60%',tp:'0',sk:'40%',nl:'0',note:'Max TL Côn Pháp. 1đ Hoành Tảo Thiên Quân lấy sát thương lan'},{level:'60',sm:'60%',tp:'0',sk:'40%',nl:'0',note:'Max Trấn Phái lấy tốc đánh và sát thương'},{level:'90+',sm:'60%',tp:'0',sk:'Máu 5k-6k+',nl:'0',note:'Max Hoành Tảo Thiên Quân (9x). Hỗ trợ La Hán Trận, Dịch Cân Kinh'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:0}],nlFixed:0}"
)

# ═══════════════════════════════════════════════════════════
# 16. THIẾU LÂM QUYỀN - Sửa description rõ cơ chế
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Chiêu thức liên tục đơn mục tiêu, đấm bất động đối phương. Không thể cưỡi ngựa.'",
    "description:'Ngoại Công bộ binh. Đấm liên hoàn khóa mục tiêu, không cưỡi ngựa. Dồn Sức Mạnh để đam khủng.'"
)

# Fix Thiếu Lâm Quyền build
content = content.replace(
    "summary:'Thiếu lâm quyền đấm rất cần TP để chính xác.',phases:[{level:'1-30',sm:'Mốc 100',tp:'Mốc 50',sk:'Dồn hết',nl:'0',note:'Tận dụng Hàng Long Bất Vũ đánh chùm siêu tốt'},{level:'30-90',sm:'Mốc 200',tp:'Mốc 100',sk:'Dồn hết',nl:'0',note:'Chuyển qua buff La Hán Trận quạt bổng'},{level:'90-150',sm:'Mốc 260',tp:'Mốc 150',sk:'Dồn hết',nl:'0',note:'Tẩy tủy, max Đạt Ma Độ Giang đấm liên hoàn'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:1}],nlFixed:0}",
    "summary:'Tăng Sức mạnh để dọn quái nhanh. Cấp 60+ ưu tiên máu 4k2, còn lại dồn SM.',phases:[{level:'10-20',sm:'Dồn hết',tp:'0',sk:'0',nl:'0',note:'Max Quyền Pháp, Hàng Long Bất Vũ 2 điểm (ít tốn mana)'},{level:'30-50',sm:'70%',tp:'0',sk:'30%',nl:'0',note:'Max La Hán. Bớt 50đ SK nếu không có đồ Kim Phong'},{level:'60-90+',sm:'Dồn hết',tp:'0',sk:'Máu 4k2',nl:'0',note:'Max Như Lai Thiên Diệp (60), rồi tăng Dịch Cân Kinh'}],calc:{smTarget:260,smReachAt:90,tpRate:[{f:1,t:150,p:0}],nlFixed:0}"
)


# ═══════════════════════════════════════════════════════════
# 17. ĐƯỜNG MÔN NỎ - Sửa description rõ TP = sát thương chính
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Sát thương AoE tầm xa cực mạnh. Bạo Vũ Lê Hoa, Thiên La Vạn Tiễn dọn bãi.'",
    "description:'AoE tầm xa cực mạnh. TP dồn hết (sát thương chính), SM 165 đủ đồ. Bạo Vũ Lê Hoa dọn bãi.'"
)

# ═══════════════════════════════════════════════════════════
# 18. ĐƯỜNG MÔN BẪY - Sửa description rõ SK max
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Trường phái gài mìn nổ sát thương tức thời siêu khủng. Địch dẫm phải là bay màu.'",
    "description:'Gài mìn nổ sát thương tức thời. SM 165 đủ đồ, TP=0 (bẫy không miss), SK dồn hết. Địch dẫm = bay màu.'"
)

# ═══════════════════════════════════════════════════════════
# 19. THÚY YÊN ĐAO - Sửa description rõ Ngoại Công 
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Khả năng Tàng hình vô song, bất chợt xuất hiện Đoạt Mạng những phái ít HP.'",
    "description:'Ngoại Công sát thủ. SM~260, TP cần. Tàng hình vô song, bất chợt xuất hiện đoạt mạng phái máu giấy.'"
)

# ═══════════════════════════════════════════════════════════
# 20. THÚY YÊN SONG ĐAO - Sửa description rõ Nội Công
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Đánh hai dao với tầm xa diện rộng, là cỗ máy sát thương Băng của team Thủy.'",
    "description:'Nội Công hệ Thủy. NL dồn hết (70%), SK 30%, SM 165 đủ đồ. Song đao tầm xa, cỗ máy sát thương băng.'"
)

# ═══════════════════════════════════════════════════════════
# 21. THIÊN NHẪN THƯƠNG - Sửa description rõ Ngoại Công
# ═══════════════════════════════════════════════════════════

content = content.replace(
    "description:'Vân long kích có Tốc độ Xuất chiêu nhanh kèm với kỹ năng giật trên từng đòn đánh gây sát thương cực kỳ cao.'",
    "description:'Ngoại Công cận chiến. SM 160, SK tăng max, TP ít. Vân Long Kích tốc xuất chiêu nhanh, giật liên tục sát thương cao.'"
)

# ═══════════════════════════════════════════════════════════
# WRITE
# ═══════════════════════════════════════════════════════════

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] All multi-source fixes applied to index.html!")
print("\nKey changes:")
print("  1. Nga My Kiem: Noi->NGOAI CONG (SM+TP high, NL low)")
print("  2. Thien Nhan Dao: Ngoai->NOI CONG (SK max, SM just enough)")
print("  3. Vo Dang Khi: smTarget 260->110 (VoLamThienHa)")
print("  4. Thien Vuong Chuy: smTarget 500->380 (community)")
print("  5. All descriptions: added Ngoai/Noi Cong labels + stat ratios")
