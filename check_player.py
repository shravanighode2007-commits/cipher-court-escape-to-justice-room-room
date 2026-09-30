with open('Assets/Scenes/Level1_Investigation.unity', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'm_Name: Player.*?m_LocalPosition:\s*(\{.*?\})', text, re.DOTALL)
if m:
    print('Level 1 Player Position:', m.group(1))

with open('Assets/Scenes/Level6_FinalVerdict.unity', 'r', encoding='utf-8') as f:
    text6 = f.read()
m6 = re.search(r'm_Name: Player.*?m_LocalPosition:\s*(\{.*?\})', text6, re.DOTALL)
if m6:
    print('Level 6 Player Position:', m6.group(1))
