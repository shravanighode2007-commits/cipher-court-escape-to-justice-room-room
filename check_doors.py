import os, re

scenes = [
    "Assets/Scenes/Level1_Investigation.unity",
    "Assets/Scenes/Level2_Computer.unity",
    "Assets/Scenes/Level3_Evidence.unity",
    "Assets/Scenes/Level4_Archive.unity",
    "Assets/Scenes/Level5_CaseFiles.unity",
    "Assets/Scenes/Level6_FinalVerdict.unity"
]

for sc in scenes:
    if not os.path.exists(sc): continue
    with open(sc, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"=== {os.path.basename(sc)} ===")
    
    # Find all GameObjects with Door or Exit
    for m in re.finditer(r'm_Name:\s*([^\n]+).*?m_LocalPosition:\s*(\{.*?\})', text, re.DOTALL):
        name = m.group(1).strip()
        pos = m.group(2).strip()
        if any(k in name.lower() for k in ['door', 'exit', 'complete']):
            print(f"  {name:25} pos: {pos}")
