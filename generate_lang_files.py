import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

configs = {
    'zh-CN': {
        'file': 'index-zh-CN.html',
        'html_lang': 'zh-CN',
        'title': 'Skill Hub - 开源技能项目汇总 | 500+热门项目精选',
        'meta_desc': 'Skill Hub 为你精选全球热门开源技能项目，涵盖编程、AI、Agent等方向，按Star数排序，提供中英日多语言简介，快速找到优质开源资源。',
        'og_locale': 'zh_CN',
        'og_alternates': '<meta property="og:locale:alternate" content="zh_TW">\n    <meta property="og:locale:alternate" content="ja_JP">\n    <meta property="og:locale:alternate" content="en_US">',
        'canonical': 'index-zh-CN.html',
    },
    'zh-TW': {
        'file': 'index-zh-TW.html',
        'html_lang': 'zh-TW',
        'title': 'Skill Hub - 開源技能專案彙整 | 500+熱門專案精選',
        'meta_desc': 'Skill Hub 為你精選全球熱門開源技能專案，涵蓋程式設計、AI、Agent等方向，按Star數排序，提供中英日多語言簡介，快速找到優質開源資源。',
        'og_locale': 'zh_TW',
        'og_alternates': '<meta property="og:locale:alternate" content="zh_CN">\n    <meta property="og:locale:alternate" content="ja_JP">\n    <meta property="og:locale:alternate" content="en_US">',
        'canonical': 'index-zh-TW.html',
    },
    'ja': {
        'file': 'index-ja.html',
        'html_lang': 'ja',
        'title': 'Skill Hub - オープンソーススキルプロジェクト集 | 人気プロジェクト500+選',
        'meta_desc': 'Skill Hubでは、プログラミング・AI・Agentなどの人気オープンソーススキルプロジェクトを厳選。Star数順で表示し、中日英多言語の紹介を提供。',
        'og_locale': 'ja_JP',
        'og_alternates': '<meta property="og:locale:alternate" content="zh_CN">\n    <meta property="og:locale:alternate" content="zh_TW">\n    <meta property="og:locale:alternate" content="en_US">',
        'canonical': 'index-ja.html',
    },
    'en': {
        'file': 'index-en.html',
        'html_lang': 'en',
        'title': 'Skill Hub - Open Source Skill Projects | 500+ Curated Projects',
        'meta_desc': 'Skill Hub curates popular open source skill projects in programming, AI, agents and more. Sorted by stars, with multilingual descriptions to help you find top open source resources.',
        'og_locale': 'en_US',
        'og_alternates': '<meta property="og:locale:alternate" content="zh_CN">\n    <meta property="og:locale:alternate" content="zh_TW">\n    <meta property="og:locale:alternate" content="ja_JP">',
        'canonical': 'index-en.html',
    },
}

TITLE_OLD = '<title>Skill Hub - 开源技能项目汇总 | 500+热门项目精选</title>'
META_DESC_OLD = '<meta name="description" content="Skill Hub 为你精选全球热门开源技能项目，涵盖编程、AI、Agent等方向，按Star数排序，提供中英日多语言简介，快速找到优质开源资源。">'
OG_TITLE_OLD = '<meta property="og:title" content="Skill Hub - 开源技能项目汇总 | 500+热门项目精选">'
OG_DESC_OLD = '<meta property="og:description" content="Skill Hub 为你精选全球热门开源技能项目，涵盖编程、AI、Agent等方向，按Star数排序，提供中英日多语言简介，快速找到优质开源资源。">'
OG_LOCALE_OLD = '<meta property="og:locale" content="zh_CN">'
OG_ALTERNATES_OLD = '<meta property="og:locale:alternate" content="zh_TW">\n    <meta property="og:locale:alternate" content="ja_JP">\n    <meta property="og:locale:alternate" content="en_US">'
CANONICAL_OLD = '<link rel="canonical" href="https://skillhub.example.com/index-zh-CN.html">'

for lang_key, cfg in configs.items():
    c = template

    c = c.replace('<html lang="zh-CN" style="color-scheme: light;">', f'<html lang="{cfg["html_lang"]}" style="color-scheme: light;">')
    c = c.replace(TITLE_OLD, f'<title>{cfg["title"]}</title>')
    c = c.replace(META_DESC_OLD, f'<meta name="description" content="{cfg["meta_desc"]}">')
    c = c.replace(OG_TITLE_OLD, f'<meta property="og:title" content="{cfg["title"]}">')
    c = c.replace(OG_DESC_OLD, f'<meta property="og:description" content="{cfg["meta_desc"]}">')
    c = c.replace(OG_LOCALE_OLD, f'<meta property="og:locale" content="{cfg["og_locale"]}">')
    c = c.replace(OG_ALTERNATES_OLD, cfg['og_alternates'])
    c = c.replace(CANONICAL_OLD, f'<link rel="canonical" href="https://skillhub.example.com/{cfg["canonical"]}">')

    with open(cfg['file'], 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Generated: {cfg['file']} (lang={cfg['html_lang']})")

print("\nAll 4 language files generated successfully!")