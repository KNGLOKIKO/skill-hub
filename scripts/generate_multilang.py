#!/usr/bin/env python3
"""
Multi-language Skills Data Generator
Generates language-specific data files and HTML content
"""

import os
import json
import re
from datetime import datetime

# Configuration
DATA_DIR = "data"
OUTPUT_DIR = "."

# Translation mappings
TRANSLATIONS = {
    'zh-CN': {
        'title': '开源技能项目精选',
        'subtitle': '500+热门开源技能项目，按Star数排序',
        'stars': '星',
        'language': '语言',
        'topics': '主题',
        'visit': '访问',
        'no_description': '暂无描述',
        'filter_placeholder': '搜索项目...',
        'sort_label': '排序',
        'stars_sort': '按星标',
        'name_sort': '按名称',
        'updated_sort': '按更新',
        'showing': '显示',
        'of': '共',
        'results': '个项目',
        'footer_text': '精选500+热门开源技能项目，按Star数排序，提供中英日多语言简介'
    },
    'zh-TW': {
        'title': '開源技能項目精選',
        'subtitle': '500+熱門開源技能項目，按Star數排序',
        'stars': '星',
        'language': '語言',
        'topics': '主題',
        'visit': '訪問',
        'no_description': '暫無描述',
        'filter_placeholder': '搜尋項目...',
        'sort_label': '排序',
        'stars_sort': '按星標',
        'name_sort': '按名稱',
        'updated_sort': '按更新',
        'showing': '顯示',
        'of': '共',
        'results': '個項目',
        'footer_text': '精選500+熱門開源技能項目，按Star數排序，提供中英日多語言簡介'
    },
    'en': {
        'title': 'Open Source Skill Projects',
        'subtitle': '500+ curated popular open source skill projects, sorted by stars',
        'stars': 'stars',
        'language': 'Language',
        'topics': 'Topics',
        'visit': 'Visit',
        'no_description': 'No description available',
        'filter_placeholder': 'Search projects...',
        'sort_label': 'Sort',
        'stars_sort': 'By Stars',
        'name_sort': 'By Name',
        'updated_sort': 'By Updated',
        'showing': 'Showing',
        'of': 'of',
        'results': 'results',
        'footer_text': 'Curated 500+ popular open source skill projects, sorted by stars, with multilingual descriptions'
    },
    'ja': {
        'title': 'オープンソーススキルプロジェクト',
        'subtitle': '500+厳選された人気のオープンソーススキルプロジェクトをStar数でソート',
        'stars': 'スター',
        'language': '言語',
        'topics': 'トピック',
        'visit': '訪問',
        'no_description': '説明なし',
        'filter_placeholder': 'プロジェクトを検索...',
        'sort_label': '並べ替え',
        'stars_sort': 'スター数順',
        'name_sort': '名前順',
        'updated_sort': '更新日順',
        'showing': '表示中',
        'of': '/',
        'results': '件',
        'footer_text': '500以上の厳選された人気のオープンソーススキルプロジェクトをStar数でソート'
    }
}

def translate_description(description, target_lang):
    """Translate or adapt description for target language"""
    if not description:
        return TRANSLATIONS[target_lang]['no_description']
    
    # Simple language detection and basic translation hints
    # In production, you might want to use a translation API
    return description[:200] + '...' if len(description) > 200 else description

def format_stars(stars_count, lang):
    """Format stars count with language-specific text"""
    return f"{stars_count:,} {TRANSLATIONS[lang]['stars']}"

def format_date(date_str, lang):
    """Format date for target language"""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        if lang == 'zh-CN':
            return dt.strftime('%Y年%m月%d日')
        elif lang == 'zh-TW':
            return dt.strftime('%Y年%m月%d日')
        elif lang == 'ja':
            return dt.strftime('%Y年%m月%d日')
        else:
            return dt.strftime('%Y-%m-%d')
    except:
        return date_str

def generate_skill_card(skill, lang):
    """Generate HTML card for a single skill"""
    t = TRANSLATIONS[lang]
    stars = format_stars(skill['stargazers_count'], lang)
    description = translate_description(skill.get('description', ''), lang)
    updated = format_date(skill['updated_at'], lang)
    language = skill.get('language', 'Unknown')
    topics = skill.get('topics', [])[:5]  # Limit to 5 topics
    
    topics_html = ''
    if topics:
        topics_list = ' '.join([f'<span class="inline-block bg-slate-200 text-slate-700 px-2 py-1 rounded text-xs">{topic}</span>' 
                                for topic in topics])
        topics_html = f'<div class="mt-3 flex flex-wrap gap-2">{topics_list}</div>'
    
    return f'''
                <div class="group bg-white rounded-2xl border border-slate-200 p-6 hover:shadow-lg hover:border-blue-300 transition-all hover:-translate-y-1">
                    <div class="flex items-start justify-between mb-3">
                        <h3 class="font-display text-xl font-semibold text-[#0a1b33] group-hover:text-blue-600 transition-colors">
                            <a href="{skill['html_url']}" target="_blank" rel="noopener noreferrer" class="hover:underline">
                                {skill['name']}
                            </a>
                        </h3>
                        <span class="text-yellow-500 font-semibold whitespace-nowrap ml-4">
                            ⭐ {stars}
                        </span>
                    </div>
                    <p class="text-slate-600 text-sm mb-3 line-clamp-2">{description}</p>
                    <div class="flex items-center justify-between text-sm">
                        <div class="flex items-center gap-3">
                            <span class="text-slate-500">{language}</span>
                            <span class="text-slate-400">•</span>
                            <span class="text-slate-400">{updated}</span>
                        </div>
                    </div>
                    {topics_html}
                    <div class="mt-4 pt-4 border-t border-slate-100">
                        <a href="{skill['html_url']}" 
                           target="_blank" 
                           rel="noopener noreferrer"
                           class="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium">
                            {t['visit']}
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                            </svg>
                        </a>
                    </div>
                </div>'''

def generate_html_content(skills, lang, output_file):
    """Generate complete HTML file for target language"""
    t = TRANSLATIONS[lang]
    
    skills_html = '\n'.join([generate_skill_card(skill, lang) for skill in skills[:100]])
    
    html_content = f'''<!DOCTYPE html>
<html lang="{lang.replace('-', '_')}" style="color-scheme: light;">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']} | Skill Hub</title>
    <meta name="description" content="{t['subtitle']}">
    <meta name="theme-color" content="#0a152d">
    
    <link rel="canonical" href="https://skillhub.example.com/{output_file}">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
    
    <script src="https://cdn.tailwindcss.com"></script>
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        'sans': ['Inter', 'system-ui', 'sans-serif'],
                        'display': ['Outfit', 'system-ui', 'sans-serif'],
                    }},
                    colors: {{
                        'primary': '#0a152d',
                        'accent': '#3b82f6',
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{ font-family: 'Inter', system-ui, sans-serif; background: #f9fafb; }}
        .line-clamp-2 {{
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
    </style>
</head>
<body>
    <!-- Hero Section -->
    <div class="bg-[#0a152d] text-white py-20 px-6">
        <div class="max-w-7xl mx-auto text-center">
            <h1 class="font-display text-4xl md:text-5xl font-bold mb-4">
                {t['title']}
            </h1>
            <p class="text-slate-300 text-lg mb-8">
                {t['subtitle']}
            </p>
        </div>
    </div>
    
    <!-- Filter and Sort Section -->
    <div class="max-w-7xl mx-auto px-6 py-8">
        <div class="flex flex-col md:flex-row gap-4 items-center justify-between mb-8">
            <input type="text" 
                   id="searchInput"
                   placeholder="{t['filter_placeholder']}"
                   class="w-full md:w-96 px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500">
            <select id="sortSelect" 
                    class="px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500">
                <option value="stars">{t['stars_sort']}</option>
                <option value="name">{t['name_sort']}</option>
                <option value="updated">{t['updated_sort']}</option>
            </select>
        </div>
        
        <!-- Stats -->
        <div class="text-slate-600 mb-6" id="statsInfo">
            {t['showing']} <span id="showingCount">0</span> {t['of']} <span id="totalCount">{len(skills)}</span> {t['results']}
        </div>
        
        <!-- Skills Grid -->
        <div id="skillsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {skills_html}
        </div>
    </div>
    
    <!-- Footer -->
    <footer class="bg-slate-900 text-white py-16 mt-20">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center">
                <p class="text-slate-400">{t['footer_text']}</p>
                <p class="text-slate-500 mt-4 text-sm">&copy; 2026 Skill Hub. All rights reserved.</p>
            </div>
        </div>
    </footer>
    
    <!-- JavaScript for filtering and sorting -->
    <script>
        const skills = {json.dumps(skills[:100], ensure_ascii=False)};
        const translations = {json.dumps(TRANSLATIONS[lang], ensure_ascii=False)};
        
        function renderSkills(skillsToRender) {{
            const grid = document.getElementById('skillsGrid');
            const showingCount = document.getElementById('showingCount');
            
            grid.innerHTML = skillsToRender.map(skill => `
                <div class="group bg-white rounded-2xl border border-slate-200 p-6 hover:shadow-lg hover:border-blue-300 transition-all hover:-translate-y-1">
                    <div class="flex items-start justify-between mb-3">
                        <h3 class="font-display text-xl font-semibold text-[#0a1b33] group-hover:text-blue-600 transition-colors">
                            <a href="${{skill.html_url}}" target="_blank" rel="noopener noreferrer" class="hover:underline">
                                ${{skill.name}}
                            </a>
                        </h3>
                        <span class="text-yellow-500 font-semibold whitespace-nowrap ml-4">
                            ⭐ ${{skill.stargazers_count.toLocaleString()}} ${{translations.stars}}
                        </span>
                    </div>
                    <p class="text-slate-600 text-sm mb-3 line-clamp-2">${{skill.description || translations.no_description}}</p>
                    <div class="flex items-center justify-between text-sm">
                        <div class="flex items-center gap-3">
                            <span class="text-slate-500">${{skill.language || 'Unknown'}}</span>
                            <span class="text-slate-400">•</span>
                            <span class="text-slate-400">${{skill.topics ? skill.topics.length : 0}} ${{translations.topics}}</span>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t border-slate-100">
                        <a href="${{skill.html_url}}" 
                           target="_blank" 
                           rel="noopener noreferrer"
                           class="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium">
                            ${{translations.visit}}
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                            </svg>
                        </a>
                    </div>
                </div>
            `).join('');
            
            showingCount.textContent = skillsToRender.length;
        }}
        
        // Search functionality
        document.getElementById('searchInput').addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase();
            const filtered = skills.filter(skill => 
                skill.name.toLowerCase().includes(query) ||
                (skill.description && skill.description.toLowerCase().includes(query)) ||
                (skill.topics && skill.topics.some(t => t.toLowerCase().includes(query)))
            );
            renderSkills(filtered);
        }});
        
        // Sort functionality
        document.getElementById('sortSelect').addEventListener('change', (e) => {{
            const sortBy = e.target.value;
            let sorted = [...skills];
            
            switch(sortBy) {{
                case 'stars':
                    sorted.sort((a, b) => b.stargazers_count - a.stargazers_count);
                    break;
                case 'name':
                    sorted.sort((a, b) => a.name.localeCompare(b.name));
                    break;
                case 'updated':
                    sorted.sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at));
                    break;
            }}
            
            renderSkills(sorted);
        }});
        
        // Initial render
        renderSkills(skills);
    </script>
</body>
</html>'''
    
    return html_content

def main():
    """Main execution function"""
    print("🚀 Starting multi-language content generation...")
    
    # Load skills data
    skills_file = os.path.join(DATA_DIR, 'skills.json')
    
    if not os.path.exists(skills_file):
        print("❌ Skills data file not found. Please run fetch_skills.py first.")
        exit(1)
    
    with open(skills_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    skills = data.get('skills', [])
    print(f"✅ Loaded {len(skills)} skills")
    
    # Generate HTML for each language
    lang_files = {
        'zh-CN': 'index-zh-CN.html',
        'zh-TW': 'index-zh-TW.html',
        'en': 'index-en.html',
        'ja': 'index-ja.html'
    }
    
    for lang, filename in lang_files.items():
        print(f"🌐 Generating {lang} version...")
        html = generate_html_content(skills, lang, filename)
        
        output_path = os.path.join(OUTPUT_DIR, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ Generated: {output_path}")
    
    print("🎉 All language versions generated successfully!")

if __name__ == '__main__':
    main()
