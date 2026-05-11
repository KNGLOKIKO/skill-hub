# Skill Hub

Global Open Source Skill Projects Collection — curated 500+ popular open source skill projects, sorted by stars, with multilingual descriptions (CN/EN/JP).

## Overview

Skill Hub is a curated catalog of open source skill projects from the GitHub Skill topic. It features 500+ popular repositories covering AI agent skills, dev tools, automation workflows, and more. Each entry includes multilingual descriptions, star counts, and tech stack information.

## Features

- **500+ Curated Projects** — Sorted by GitHub stars, updated regularly
- **Multilingual Support** — Full UI available in Simplified Chinese, Traditional Chinese, Japanese, and English
- **Smart Search** — Search by name, description, or tags with bilingual support
- **Category Filter** — 20 categories including AI Agent Skills, Dev Tools & CLI, Frontend & UI Design, and more
- **Responsive Design** — Optimized for desktop, tablet, and mobile

## Language Files

| File | Language | Locale |
|------|----------|--------|
| `index.html` | Default entry (zh-CN) | zh-CN |
| `index-zh-CN.html` | 简体中文 | zh-CN |
| `index-zh-TW.html` | 繁體中文 | zh-TW |
| `index-ja.html` | 日本語 | ja |
| `index-en.html` | English | en |

## Project Structure

```
skill-hub/
  index.html                  # Main template (zh-CN)
  index-zh-CN.html            # Chinese (Simplified)
  index-zh-TW.html            # Chinese (Traditional)
  index-ja.html               # Japanese
  index-en.html               # English
  copyright.html              # Legal / copyright page
  README.md                   # English documentation
  README-zh.md                # Chinese documentation
  generate_lang_files.py      # Language file generator
  scripts/                    # Development utilities
    count_lang.py             # Count translation points
    extract_tr.py             # Extract translation pairs
    fix_untranslated.py       # Fix untranslated entries
  docs/                       # Design documentation
    design-spec.md
    implementation-plan.md
```

## Quick Start

1. Open `index.html` in any modern browser
2. The page auto-detects your browser language
3. Use the language dropdown in the header to switch languages
4. Browsing `index-en.html` directly opens the English version

## Development

### Generating Language Files

After modifying `index.html`, regenerate language-specific files:

```bash
python generate_lang_files.py
```

### Utility Scripts

```bash
python scripts/count_lang.py        # Count translation markers
python scripts/extract_tr.py        # Extract all translation pairs
python scripts/fix_untranslated.py  # Fix untranslated project descriptions
```

## Tech Stack

- React 18 (CDN)
- Babel Standalone (JSX transpilation)
- Tailwind CSS (CDN)
- Google AdSense (conditional)
- IntersectionObserver (lazy loading)

## Data Source

All project data is sourced from the [GitHub Skill topic](https://github.com/topics/skill). This site is an independent catalog and is not affiliated with GitHub.

## License

© 2026 Skill Hub. All rights reserved.