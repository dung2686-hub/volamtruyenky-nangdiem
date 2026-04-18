with open('index.html','r',encoding='utf-8') as f:
    c = f.read()

checks = [
    ("role:'Kiếm Sĩ Băng Sát'", "NM Kiem = Kiem Si Bang Sat"),
    ("role:'Pháp Sư Hỏa Nội'", "TN Dao = Phap Su Hoa Noi"),
    ("smTarget:110,smReachAt:30", "VD Khi smTarget=110"),
    ("smTarget:380,smReachAt:120", "TV Chuy smTarget=380"),
    ("Ngoại Công kiếm băng", "NM Kiem description = Ngoai Cong"),
    ("Nội Công hỏa sát", "TN Dao description = Noi Cong"),
    ("SM 80% SK 20%", "TL Dao description has ratio"),
    ("SM 70% SK 30%", "TL Bong/Quyen description has ratio"),
    ("TP dồn hết", "DM No TP description"),
]

print("=== DATA VERIFICATION ===")
for target, label in checks:
    status = "PASS" if target in c else "FAIL"
    print(f"  [{status}] {label}")

# Count the word 'Ngoại Công' and 'Nội Công' in descriptions
import re
ngoai = len(re.findall(r"description:'[^']*Ngoại Công[^']*'", c))
noi = len(re.findall(r"description:'[^']*Nội Công[^']*'", c))
print(f"\nDescriptions mentioning 'Ngoai Cong': {ngoai}")
print(f"Descriptions mentioning 'Noi Cong': {noi}")
print("=== DONE ===")
