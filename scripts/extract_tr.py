import re, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

base = os.path.join(os.path.dirname(__file__), '..', 'index.html')
with open(base, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"lang\s*===\s*'zh'\s*\?\s*('[^']*(?:\\'[^']*)*')\s*:\s*('[^']*(?:\\'[^']*)*')"
matches = re.findall(pattern, content)
print(f"Total translation pairs: {len(matches)}\n")

for i, (zh, en) in enumerate(matches, 1):
    zh_str = zh.strip("'")
    en_str = en.strip("'")
    print(f"{i:2}. ZH: {zh_str[:80]}")
    print(f"    EN: {en_str[:80]}")
    print()