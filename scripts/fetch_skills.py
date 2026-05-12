#!/usr/bin/env python3
"""
GitHub Skills API Data Fetcher
Fetches ALL skill projects from GitHub API (up to 1000 due to GitHub limits)
"""

import os
import json
import time
import requests
from datetime import datetime

# GitHub API Configuration
GITHUB_API_URL = "https://api.github.com"
TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPOS_PER_PAGE = 100

# GitHub Search API 限制: 最多返回 1000 个结果 (10页 x 100)
MAX_PAGES = 10

# Output files
OUTPUT_DIR = "data"
SKILLS_FILE = f"{OUTPUT_DIR}/skills.json"

def get_headers():
    """Get headers for GitHub API requests"""
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Skill-Hub-Auto-Update'
    }
    if TOKEN:
        headers['Authorization'] = f'token {TOKEN}'
    return headers

def fetch_skills_from_github():
    """Fetch ALL skill repositories from GitHub API"""
    print("🔍 Fetching ALL skills from GitHub API...")
    print(f"📊 Note: GitHub Search API 限制最多返回 1000 个结果")
    
    all_repos = []
    
    for page in range(1, MAX_PAGES + 1):
        url = f"{GITHUB_API_URL}/search/repositories"
        params = {
            'q': 'topic:skill',
            'sort': 'stars',
            'order': 'desc',
            'per_page': REPOS_PER_PAGE,
            'page': page
        }
        
        try:
            print(f"📄 Fetching page {page}/{MAX_PAGES}...")
            
            response = requests.get(url, headers=get_headers(), params=params, timeout=30)
            
            if response.status_code == 403:
                print("⚠️  Rate limit hit, waiting 60 seconds...")
                time.sleep(60)
                page -= 1  # 重试当前页
                continue
            
            if response.status_code == 422:
                print(f"❌ Validation failed: {response.json()}")
                break
            
            if response.status_code != 200:
                print(f"❌ API Error: {response.status_code} - {response.text}")
                break
            
            data = response.json()
            repos = data.get('items', [])
            
            if not repos:
                print("📭 没有更多结果了")
                break
            
            for repo in repos:
                skill_data = {
                    'id': repo['id'],
                    'name': repo['name'],
                    'full_name': repo['full_name'],
                    'description': repo.get('description', ''),
                    'html_url': repo['html_url'],
                    'stargazers_count': repo['stargazers_count'],
                    'language': repo.get('language', 'Unknown'),
                    'topics': repo.get('topics', []),
                    'updated_at': repo['updated_at'],
                    'created_at': repo['created_at'],
                    'fork': repo['fork'],
                    'homepage': repo.get('homepage', ''),
                    'watchers_count': repo.get('watchers_count', 0),
                    'forks_count': repo.get('forks_count', 0),
                    'open_issues_count': repo.get('open_issues_count', 0),
                    'license': repo.get('license', {}).get('name', 'No License') if repo.get('license') else 'No License',
                    'default_branch': repo.get('default_branch', 'master'),
                    'archived': repo.get('archived', False),
                    'disabled': repo.get('disabled', False),
                    'pushed_at': repo.get('pushed_at', '')
                }
                all_repos.append(skill_data)
            
            print(f"✅ Page {page}: 获取 {len(repos)} 个项目, 总计: {len(all_repos)}")
            
            # 检查是否到达 API 限制
            if len(repos) < REPOS_PER_PAGE:
                print("📭 最后一页，已获取所有可用结果")
                break
            
            # 尊重 API 限制，避免被限流
            time.sleep(1)
            
        except requests.exceptions.Timeout:
            print(f"⏱️  Page {page} 请求超时，重试中...")
            page -= 1
            time.sleep(5)
            continue
            
        except Exception as e:
            print(f"❌ Error fetching page {page}: {e}")
            continue
    
    print(f"✅ 总共获取: {len(all_repos)} 个 repositories")
    return all_repos

def generate_translations():
    """Generate translation dictionary for skills"""
    return {
        'zh': {
            'title': '开源技能项目',
            'description': '精选热门开源技能项目',
            'stars': '星标数',
            'language': '语言',
            'topics': '主题标签',
            'visit': '访问',
            'no_description': '暂无描述',
            'updated': '更新时间',
            'filter': '筛选项目...',
            'sort_by': '排序方式',
            'stars_count': '星标数',
            'name': '名称',
            'last_updated': '最近更新',
            'showing': '显示',
            'of': '共',
            'results': '个项目'
        },
        'en': {
            'title': 'Open Source Skill Projects',
            'description': 'Curated popular open source skill projects',
            'stars': 'Stars',
            'language': 'Language',
            'topics': 'Topics',
            'visit': 'Visit',
            'no_description': 'No description',
            'updated': 'Updated',
            'filter': 'Filter projects...',
            'sort_by': 'Sort by',
            'stars_count': 'Stars',
            'name': 'Name',
            'last_updated': 'Last Updated',
            'showing': 'Showing',
            'of': 'of',
            'results': 'results'
        },
        'ja': {
            'title': 'オープンソーススキルプロジェクト',
            'description': '厳選された人気のオープンソーススキルプロジェクト',
            'stars': 'スター数',
            'language': '言語',
            'topics': 'トピック',
            'visit': '訪問',
            'no_description': '説明なし',
            'updated': '更新日時',
            'filter': 'プロジェクトをフィルター...',
            'sort_by': '並べ替え',
            'stars_count': 'スター数',
            'name': '名前',
            'last_updated': '最終更新',
            'showing': '表示中',
            'of': '/',
            'results': '件'
        }
    }

def save_skills_data(skills):
    """Save skills data to JSON file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    data = {
        'updated_at': datetime.now().isoformat(),
        'total_count': len(skills),
        'github_api_limit': 1000,
        'skills': skills,
        'translations': generate_translations()
    }
    
    with open(SKILLS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Skills data saved to {SKILLS_FILE}")

def main():
    """Main execution function"""
    print("🚀 Starting GitHub Skills Data Fetcher...")
    print(f"⏰ Timestamp: {datetime.now().isoformat()}")
    print(f"📡 Target: ALL GitHub skill repositories (up to 1000)")
    
    # Fetch ALL data from GitHub
    skills = fetch_skills_from_github()
    
    if skills:
        # Save data
        save_skills_data(skills)
        print("✅ Data fetch and save completed successfully!")
        print(f"📊 Summary: {len(skills)} skills fetched")
    else:
        print("❌ No data fetched, please check your configuration")
        exit(1)

if __name__ == '__main__':
    main()
