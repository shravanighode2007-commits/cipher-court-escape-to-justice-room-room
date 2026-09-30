with open('Assets/Scenes/Level6_FinalVerdict.unity', 'r', encoding='utf-8') as f:
    text = f.read()

import re

objects = text.split('--- !u!')
print(f'Total blocks: {len(objects)}')

go_map = {}
tr_map = {}
mr_map = {}

for obj in objects:
    lines = obj.strip().split('\n')
    header = lines[0]
    m = re.match(r'(\d+)\s+&(\d+)', header)
    if not m: continue
    type_id, obj_id = int(m.group(1)), m.group(2)

    if type_id == 1:
        name = ''
        active = 1
        for l in lines:
            if 'm_Name:' in l: name = l.split(':', 1)[1].strip()
            if 'm_IsActive:' in l: active = int(l.split(':', 1)[1].strip())
        go_map[obj_id] = {'name': name, 'active': active}
    
    elif type_id == 4:
        go_id = ''
        pos = ''
        scale = ''
        father = ''
        for l in lines:
            if 'm_GameObject:' in l:
                gm = re.search(r'fileID:\s*(\d+)', l)
                if gm: go_id = gm.group(1)
            if 'm_LocalPosition:' in l: pos = l.split(':', 1)[1].strip()
            if 'm_LocalScale:' in l: scale = l.split(':', 1)[1].strip()
            if 'm_Father:' in l:
                fm = re.search(r'fileID:\s*(\d+)', l)
                if fm: father = fm.group(1)
        tr_map[obj_id] = {'go_id': go_id, 'pos': pos, 'scale': scale, 'father': father}

    elif type_id == 23:
        go_id = ''
        enabled = 1
        mats = []
        for l in lines:
            if 'm_GameObject:' in l:
                gm = re.search(r'fileID:\s*(\d+)', l)
                if gm: go_id = gm.group(1)
            if 'm_Enabled:' in l: enabled = int(l.split(':', 1)[1].strip())
            if 'guid:' in l:
                mats.append(l.strip())
        mr_map[obj_id] = {'go_id': go_id, 'enabled': enabled, 'mats': mats}

print(f'GameObjects: {len(go_map)}, Transforms: {len(tr_map)}, MeshRenderers: {len(mr_map)}')

for mr_id, mr in mr_map.items():
    go_info = go_map.get(mr['go_id'], {'name': 'UNKNOWN', 'active': 0})
    name = go_info['name']
    print(f"GO: {name} (active={go_info['active']}, mr_enabled={mr['enabled']}), mats={mr['mats']}")
