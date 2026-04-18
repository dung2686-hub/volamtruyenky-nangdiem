import re
import urllib.request
from bs4 import BeautifulSoup

def fetch_kisugame_guide(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        content_div = soup.find('div', {'class': 'td-post-content'})
        if content_div:
            paragraphs = content_div.find_all('p')
            guide = "\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip() != ''])
            return guide
    except Exception as e:
        return str(e)
    return "No content"

# Define the updates based strictly on what's in the Kisugame text 
# For Cai Bang Chuong (from the text read earlier):
# "Từ lv1-lv20: ... nâng vào kỹ năng Cái Bang chưởng pháp và 1 ít kỹ năng Kiến Nhân thần thủ..."
# "Từ lv20-lv60: lv30 có Giáng Long Chưởng... lv50-60 Kháng Long Hữu Hối và Túy Điệp Cuồng Vũ..."
# So no Tàng Long, no NL=0. 

# We will modify the HTML directly using regex like we did before, but using EXACT WORDS from kisugame.

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Cai Bang Chuong phase text based EXACTLY on kisugame
cbchuong_kisutext = [
    "{level:'1-20',sm:'N/A',tp:'N/A',sk:'Tăng max sinh khí',nl:'Cộng 1 ít nếu cần',note:'nâng vào kỹ năng Cái Bang chưởng pháp và 1 ít Kiến Nhân thần thủ để train quái.'}",
    "{level:'21-60',sm:'Đủ mặc đồ',tp:'N/A',sk:'Tăng max sinh khí',nl:'N/A',note:'Lv30 nâng Giáng Long Chưởng, lv40 Hoạt Bát Lưu Thủ, lv50-60 Kháng Long Hữu Hối và Túy Điệp Cuồng Vũ.'}",
    "{level:'95+',sm:'N/A',tp:'N/A',sk:'Tăng max sinh khí',nl:'N/A',note:'Tẩy tủy nâng max Túy Điệp Cuồng Vũ, Tiêu Diêu Công, Cái Bang chưởng, Giáng Long Chưởng, Kháng Long Hữu Hối, Phi Long Tại Thiên'}"
]
cbchuong_note = "'Phần lớn người chơi nhánh này thường sẽ là tăng max vào chỉ số Sinh khí, nhằm tăng thêm sự trâu bò... bạn có thể cộng 1 ít vào nội công, nhưng nếu không tăng sức mạnh sẽ rất khó mặc đồ.'"

cbchuong_phases = "[" + ",".join(cbchuong_kisutext) + "]"

# 2. Update Thien Nhan Mau Phap phase text based EXACTLY on kisugame
tnmau_kisutext = [
    "{level:'1-20',sm:'Tăng nhiều',tp:'0',sk:'0',nl:'0',note:'nâng vào kỹ năng Tàn Dương Như Tuyết từ 6-8 điểm... lv10 cộng max vào kỹ năng Thiên Nhẫn Mâu Pháp'}",
    "{level:'21-60',sm:'Tăng nhiều',tp:'0',sk:'1 ít',nl:'0',note:'Lv30 mở khóa Liệt Hỏa Tình Thiên... lv60 dồn vào Thâu Thiên Hoán Nhật để hút máu/nội lực... lv60 lấy Thiên Ma Giải Thể.'}",
    "{level:'95+',sm:'160',tp:'1 ít',sk:'Tăng max',nl:'Vừa đủ mặc đồ',note:'Sau tẩy tủy: Vân Long Kích, Thiên Ma Giải Thể, Thiên Nhẫn Mâu Pháp, Thâu Thiên Hoán Nhật, Liệt Hỏa Tình Thiên'}"
]
tnmau_note = "'Yêu cầu sức mạnh 160 và Sinh Khí Tăng max, nếu bạn cảm thấy né tránh hoặc tốc đánh chưa đủ có thể cộng 1 ít Thân Pháp, nội công tăng vừa phải đủ mặc đồ.'"
tnthuong_phases = "[" + ",".join(tnmau_kisutext) + "]"


def replace_build_guide(char_id, summary_str, phases_str):
    global content
    pattern = r"({id:'" + char_id + r"',.*?buildGuide:{summary:)[^,]+(,phases:\[.*?\])"
    
    def replacer(match):
        return match.group(1) + summary_str + ",phases:" + phases_str
    
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

replace_build_guide('cbchuong', cbchuong_note, cbchuong_phases)
replace_build_guide('tnthuong', tnmau_note, tnthuong_phases)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Applied strict Kisugame text.")
