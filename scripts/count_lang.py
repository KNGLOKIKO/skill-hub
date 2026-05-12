import re
import os

base = os.path.join(os.path.dirname(__file__), '..', 'index.html')
with open(base, 'r', encoding='utf-8') as f:
    c = f.read()
zh = len(re.findall(r"lang\s*===\s*'zh'", c))
en = len(re.findall(r"lang\s*===\s*'en'", c))
total = len(re.findall(r"lang\s*===\s*'(?:zh|en)'", c))
toggle = len(re.findall(r'toggleLang', c))
print(f"lang === 'zh': {zh}")
print(f"lang === 'en': {en}")
print(f"total translation points: {total}")
print(f"toggleLang refs: {toggle}")