import os, re

mat_dir = 'Assets/CipherCourtPolish/Materials'
for fname in sorted(os.listdir(mat_dir)):
    if fname.endswith('.mat'):
        fpath = os.path.join(mat_dir, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        m = re.search(r'm_Shader:\s*\{fileID:\s*(\d+),\s*guid:\s*([a-f0-9]+)', content)
        shader_guid = m.group(2) if m else 'NONE'
        print(f"{fname:30} : shader guid = {shader_guid}")
