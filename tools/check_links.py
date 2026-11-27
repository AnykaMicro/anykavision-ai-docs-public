# Relative-link check, stdlib only. Run after building both languages:
#   python3 tools/check_links.py . _build/html
# Checks the Markdown sources as GitHub renders them (links, images, #anchors, README files Sphinx skips,
# ASCII-only paths under docs/, no unreferenced images) and every relative href/src in the built site,
# including the language switcher and #anchors. External URLs are not fetched.
import os, re, sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

REPO, SITE = sys.argv[1:3]
FENCED = re.compile(r'^[ \t]*(?:```|~~~).*?^[ \t]*(?:```|~~~)[^\n]*$', re.S | re.M)
CODE = re.compile(FENCED.pattern + r'|`[^`\n]+`', re.S | re.M)  # fenced and inline code: no links inside
LINK = re.compile(r'!?\[[^\]]*\]\(([^)\s]+)\)|<(?:a|img)\s[^>]*?(?:href|src)="([^"]+)"')
HEADING = re.compile(r'^#{1,6} +(.+?)\s*$', re.M)
TARGET = re.compile(r'^\(([\w-]+)\)=\s*$', re.M)  # MyST explicit target
CONFLICT = re.compile(r'^(?:<{7}\s|={7}$|>{7}\s)', re.M)  # Git merge conflict markers
IMG_EXT = ('.png', '.jpg', '.jpeg', '.svg', '.gif')
errors = []


def anchors(path):  # GitHub / MyST heading slugs plus explicit targets
    text = FENCED.sub('', open(path, encoding='utf-8').read())
    slugs = {re.sub(r'[^\w\- ]', '', re.sub(r'[*`]', '', h).lower()).replace(' ', '-') for h in HEADING.findall(text)}
    return slugs | set(TARGET.findall(text))


md_files, images, used, checked = [], set(), set(), 0
labels = set()  # MyST explicit targets: [text](#label) resolves to them from any page
site_dir = os.path.abspath(SITE)  # the built site may live inside the repo (CI assembles _site there)
for d, dirs, fs in os.walk(REPO):
    dirs[:] = [x for x in dirs if x not in ('.git', '_build', '_site', '.venv', 'node_modules')
               and os.path.abspath(os.path.join(d, x)) != site_dir]
    for f in fs:
        p = os.path.join(d, f)
        rel = os.path.relpath(p, REPO)
        if rel.startswith('docs') and not rel.isascii():
            errors.append(f'non-ASCII path: {rel}')
        if f.endswith('.md'):
            md_files.append(p)
        elif f.lower().endswith(IMG_EXT):
            images.add(os.path.normpath(p))

for p in md_files:
    labels.update(TARGET.findall(open(p, encoding='utf-8').read()))
for p in md_files:
    raw = open(p, encoding='utf-8').read()
    if CONFLICT.search(raw):
        errors.append(f'merge conflict marker: {os.path.relpath(p, REPO)}')
    for m in LINK.finditer(CODE.sub('', raw)):
        url = m.group(1) or m.group(2)
        if re.match(r'[a-z]+:', url):
            continue
        checked += 1
        path, _, frag = unquote(url).partition('#')
        target = os.path.normpath(os.path.join(os.path.dirname(p), path)) if path else p
        where = f'{os.path.relpath(p, REPO)} -> {url}'
        if not os.path.exists(target):
            errors.append(f'missing target: {where}')
        elif frag and target.endswith('.md') and frag not in anchors(target) and (path or frag not in labels):
            errors.append(f'missing anchor: {where}')
        used.add(target)
errors += [f'unreferenced image: {os.path.relpath(i, REPO)}' for i in sorted(images - used)]
print(f'markdown: {len(md_files)} files, {checked} relative links')


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        self.refs += [v for k, v in attrs if k in ('href', 'src') and v]
        self.ids.update(v for k, v in attrs if k == 'id' and v)


pages = {}
for d, _, fs in os.walk(SITE):
    for f in fs:
        if f.endswith('.html'):
            p = os.path.normpath(os.path.join(d, f))
            pages[p] = Page()
            pages[p].feed(open(p, encoding='utf-8').read())
links = 0
for p, page in pages.items():
    for url in page.refs:
        u = urlsplit(url)
        if u.scheme or u.netloc or not (u.path or u.fragment):
            continue
        links += 1
        target = os.path.normpath(os.path.join(os.path.dirname(p), unquote(u.path))) if u.path else p
        if os.path.isdir(target):
            target = os.path.join(target, 'index.html')
        where = f'{os.path.relpath(p, SITE)} -> {url}'
        if not os.path.exists(target):
            errors.append(f'site: {where}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'site: missing anchor: {where}')  # e.g. a link into a section left out of the build
if not pages:
    errors.append(f'no HTML pages under {SITE}: build the site first')
print(f'site: {len(pages)} HTML pages, {links} relative links and anchors')

for e in errors:
    print('ERROR', e)
sys.exit(1 if errors else 0)
