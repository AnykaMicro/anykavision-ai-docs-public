# Shared Sphinx configuration for docs/en and docs/zh_CN.
# Build one language with:
#   sphinx-build -W -c docs -D language=en docs/en _build/html/en
#   sphinx-build -W -c docs -D language=zh_CN docs/zh_CN _build/html/zh_CN
from pathlib import Path

from docutils import nodes
from sphinx.errors import ConfigError

project = "AnykaVision AI"
copyright = "2026, Guangzhou Anyka Microelectronics Co., Ltd."
product_version = "V1.00"
version = "1.0.0"
release = version

extensions = ["myst_parser"]
myst_heading_anchors = 3
exclude_patterns = ["**/README.md"]  # folder indexes for GitHub browsing, not site pages

html_theme = "furo"
html_title = f"{project} {product_version} Documentation {release}"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
templates_path = ["_templates"]
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "lang-switch.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}

# Public site root for canonical and alternate-language URLs.
SITE = "https://anykamicro.github.io/anykavision-ai-docs-public/"
html_context = {"site_root": SITE}  # hreflang alternates in _templates/page.html


def _per_language(app, config):
    """docs/<lang> must be built with -D language=<lang>; each build gets its own canonical URL."""
    lang = Path(app.srcdir).name
    if config.language != lang:
        raise ConfigError(f"build docs/{lang} with -D language={lang} (got {config.language!r})")
    config.html_baseurl = f"{SITE}{lang}/"


# Content waiting for Anyka (removed third-party figures, text that needs a rewrite or permission) stays in the
# sources but is left out of the site; build with -t anyka_review to see it. Plain blocks use ```{only} anyka_review.
# A whole section is marked by a (review-only-<name>)= label above its heading: MyST lifts headings out of
# {only}, so those sections are dropped here, before the TOC, search and image collectors read the page.
def _drop_review_only_sections(app, doctree):
    if app.tags.has("anyka_review"):
        return
    for section in list(doctree.findall(nodes.section)):
        if any(name.startswith("review-only-") for name in section["ids"] + section["names"]):
            section.parent.remove(section)


def setup(app):
    app.connect("config-inited", _per_language)
    app.connect("doctree-read", _drop_review_only_sections, priority=100)
