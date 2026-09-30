import re

with open('Assets/Scenes/Level6_FinalVerdict.unity', 'r', encoding='utf-8') as f:
    text = f.read()

objects = text.split('--- !u!')
scripts = []
for obj in objects:
    lines = obj.strip().split('\n')
    header = lines[0]
    m = re.match(r'114\s+&(\d+)', header)
    if not m: continue
    obj_id = m.group(1)
    
    script_guid = ''
    go_id = ''
    for l in lines:
        if 'm_Script:' in l:
            gm = re.search(r'guid:\s*([a-f0-9]+)', l)
            if gm: script_guid = gm.group(1)
        if 'm_GameObject:' in l:
            gm = re.search(r'fileID:\s*(\d+)', l)
            if gm: go_id = gm.group(1)
    
    scripts.append((obj_id, go_id, script_guid))

print(f'Total MonoBehaviours: {len(scripts)}')

# Map guid to script name
import os
guid_to_name = {}
for root, dirs, files in os.walk('Assets'):
    for f in files:
        if f.endswith('.cs.meta'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as mf:
                c = mf.read()
            m = re.search(r'guid:\s*([a-f0-9]+)', c)
            if m:
                guid_to_name[m.group(1)] = f.replace('.cs.meta', '')

for obj_id, go_id, guid in scripts:
    sname = guid_to_name.get(guid, f'Unknown/Package({guid[:8]})')
    print(f"MonoBehaviour &{obj_id} on GO &{go_id} -> {sname}")
