# Report-only: compare the functions documented in the middleware API reference with the SDK headers.
#   python3 tools/check_api_vs_headers.py docs/zh_CN/software/board/middleware-api <sdk>/platform/include
# A documented function is a heading whose section has a Chinese or English syntax block; a referenced function is any
# ak_*/AK_* call or prototype on the pages (code samples included). Header names are ak_*/AK_* prototypes
# outside comments, plus function-like #define macros. Always exits 0: the output is for the API owners.
import os, re, sys
from collections import defaultdict

DOCS, INCLUDE = sys.argv[1:3]
IDENT = re.compile(r'[A-Za-z_]\w*')

CALL = re.compile(r'\b((?i:ak)_\w+)\s*\((?!\s*\*)')  # not a function-pointer type "AK_S32 (*fp)"
SYNTAX_MARKERS = ('【语法】', '【Syntax】')
documented, referenced = {}, {}  # name -> page
for f in sorted(os.listdir(DOCS)):
    if not f.endswith('.md'):
        continue
    text = open(os.path.join(DOCS, f), encoding='utf-8').read()
    for name in CALL.findall(text):
        referenced.setdefault(name, f)
    sections = re.split(r'^#{1,6} +(.+?)\s*$', text, flags=re.M)
    for title, body in zip(sections[1::2], sections[2::2]):
        name = title.replace('*', '').strip()
        if IDENT.fullmatch(name) and any(marker in body for marker in SYNTAX_MARKERS):
            documented.setdefault(name, f)

declared, macros = {}, set()  # name -> header
for f in sorted(os.listdir(INCLUDE)):
    if not f.endswith('.h'):
        continue
    src = open(os.path.join(INCLUDE, f), encoding='utf-8', errors='replace').read()
    src = re.sub(r'/\*.*?\*/|//[^\n]*', ' ', src, flags=re.S)
    macros.update(re.findall(r'^[ \t]*#[ \t]*define[ \t]+((?i:ak)_\w+)\(', src, flags=re.M))
    src = re.sub(r'^[ \t]*#(?:[^\n]*\\\n)*[^\n]*', ' ', src, flags=re.M)
    for name in re.findall(r'\b((?i:ak)_\w+)\s*\((?!\s*\*)[^;{}]*\)\s*;', src):  # not "AK_S32 (*fp)(...)"
        declared.setdefault(name, f)

known = set(declared) | macros
missing = sorted(set(documented) - known, key=lambda n: (documented[n], n))
stray = sorted(set(referenced) - known - set(documented), key=lambda n: (referenced[n], n))
undocumented = defaultdict(list)
for name in sorted(set(declared) - set(documented)):
    undocumented[declared[name]].append(name)

print(f'documented functions: {len(documented)}; header functions: {len(declared)} (+{len(macros)} macros)')
print(f'\nDocumented (heading with a syntax block) but not in any header ({len(missing)}):')
for n in missing:
    print(f'  {documented[n]}: {n}')
print(f'\nUsed in code samples or prototypes on the pages but not in any header ({len(stray)}):')
for n in stray:
    print(f'  {referenced[n]}: {n}')
print(f'\nDeclared in headers but not documented ({sum(map(len, undocumented.values()))}):')
for header, names in sorted(undocumented.items()):
    print(f'  {header} ({len(names)}): {", ".join(names)}')
