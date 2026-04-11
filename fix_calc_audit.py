import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

updates = {
    # 1. tvthuong needs TP to not miss
    'tvthuong': r"smTarget:350,smReachAt:100,tpRate:\[\{f:1,t:150,p:1\}\]",
    
    # 2. nmbuff is female only, SM target should be 165 (not 260)
    'nmbuff': r"smTarget:165,smReachAt:60,tpRate:\[\{f:1,t:150,p:0\}\]",
    
    # 3. cbchuong is male only, SM target should be 260 (not 165)
    'cbchuong': r"smTarget:260,smReachAt:90,tpRate:\[\{f:1,t:150,p:0\}\]",
    
    # 4. tnthuong is typically male, SM target 260
    'tnthuong': r"smTarget:260,smReachAt:90,tpRate:\[\{f:1,t:150,p:0\}\]",
    
    # 5. clkiem is typically male, SM target 260
    'clkiem': r"smTarget:260,smReachAt:90,tpRate:\[\{f:1,t:150,p:0\}\]",
    
    # 6. vdkhik is typically male, SM target 260
    'vdkhik': r"smTarget:260,smReachAt:90,tpRate:\[\{f:1,t:150,p:0\}\]"
}

for char_id, new_calc_core in updates.items():
    # We find the calc block and replace only the smTarget/smReachAt/tpRate section, leaving nlFixed intact
    # Find the calc block
    pattern = r"({id:'" + char_id + r"'.*?calc:\{)(.*?nlFixed:[^\}]+\})"
    
    def replacer(match):
        prefix = match.group(1)
        # Extract the old nlFixed part to preserve it
        old_calc_inner = match.group(2)
        nl_match = re.search(r'(nlFixed:[^\}]+)', old_calc_inner)
        nl_fixed = nl_match.group(1) if nl_match else "nlFixed:0"
        
        # We need to construct the new inner string manually as python string manipulation or regex
        # The new string is what we mapped in the updates dict + nlFixed
        new_inner = new_calc_core.replace('\\', '') + ',' + nl_fixed
        return prefix + new_inner
        
    content = re.sub(pattern, replacer, content, flags=re.IGNORECASE|re.DOTALL)

# Let's adjust the `phases` text for these updated configurations to match the new targets.
# For nmbuff, change 'Mốc 260' to 'Mốc 165'
content = re.sub(r"(id:'nmbuff'.*?sm:')Mốc 260", r"\g<1>Mốc 165", content, flags=re.DOTALL)
# For cbchuong, change 'Mốc 165' to 'Mốc 260'
content = re.sub(r"(id:'cbchuong'.*?sm:')Mốc 165", r"\g<1>Mốc 260", content, flags=re.DOTALL)
# For clkiem, change 'Mốc 165' to 'Mốc 260'
content = re.sub(r"(id:'clkiem'.*?sm:')Mốc 165", r"\g<1>Mốc 260", content, flags=re.DOTALL)
# For tnthuong, change 'Mốc 165' to 'Mốc 260'
content = re.sub(r"(id:'tnthuong'.*?sm:')Mốc 165", r"\g<1>Mốc 260", content, flags=re.DOTALL)
# For vdkhik, change 'Mốc 165' to 'Mốc 260'
content = re.sub(r"(id:'vdkhik'.*?sm:')Mốc 165", r"\g<1>Mốc 260", content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Audited and fixed bugs in the calc algorithms algorithm for 6 branches.")
