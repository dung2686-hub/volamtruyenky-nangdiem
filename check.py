import re, sys
sys.stdout.reconfigure(encoding='utf-8')
d = open('index.html', encoding='utf-8').read()
ids = ['tlquyen','nmbuff','nmchuong','dmbay','vdkhik']
for x in ids:
    m = re.search(r"id:'" + x + r"'.*?calc:\{(.*?)\}", d)
    print(f"{x}: {m.group(1)}" if m else f"{x}: NOT FOUND")
