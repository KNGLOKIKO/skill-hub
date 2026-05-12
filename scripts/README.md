# GitHub Actions Automation

This directory contains scripts and workflows for automatically updating the Skill Hub website with the latest GitHub skills data.

## Scripts

### 1. `fetch_skills.py`

Fetches skill repositories from GitHub API and saves them to `data/skills.json`.

**Usage:**
```bash
python scripts/fetch_skills.py
```

**Environment Variables:**
- `GITHUB_TOKEN` (optional): GitHub Personal Access Token for higher API rate limits

### 2. `generate_multilang.py`

Generates multi-language HTML files from the skills data.

**Usage:**
```bash
python scripts/generate_multilang.py
```

**Output Files:**
- `index-zh-CN.html` (Simplified Chinese)
- `index-zh-TW.html` (Traditional Chinese)
- `index-en.html` (English)
- `index-ja.html` (Japanese)

## GitHub Actions Workflows

### `daily-update.yml`

Runs daily at 00:00 UTC (8:00 AM Beijing Time) to:
1. Fetch latest skills from GitHub API
2. Generate updated HTML files
3. Commit and push changes
4. Trigger Vercel deployment

### `complete-pipeline.yml`

Complete CI/CD pipeline that:
1. Runs daily updates
2. Generates multi-language content
3. Commits changes if data changed
4. Creates deployment summary

## GitHub Actions Setup

The workflows will automatically run based on the schedule. No additional setup is required if you're using GitHub's default `GITHUB_TOKEN`.

For increased API rate limits, you can add a Personal Access Token:

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` scope
3. Go to repository Settings → Secrets
4. Add `GITHUB_TOKEN` secret

## Local Development

To test the scripts locally:

```bash
# Install dependencies
pip install requests

# Fetch skills data
python scripts/fetch_skills.py

# Generate HTML files
python scripts/generate_multilang.py
```

## Workflow Triggers

The automation runs:
- **Scheduled**: Daily at 00:00 UTC
- **Manual**: Via GitHub Actions workflow_dispatch
- **On Push**: When scripts or workflow files change

## Monitoring

Check the status of automated runs:
1. Go to repository Actions tab
2. View workflow runs
3. Check individual job logs

## Data Format

The skills data is stored in JSON format:
```json
{
  "updated_at": "2026-05-12T00:00:00",
  "total_count": 500,
  "skills": [
    {
      "id": 123456,
      "name": "project-name",
      "full_name": "username/project-name",
      "description": "Project description",
      "html_url": "https://github.com/...",
      "stargazers_count": 10000,
      "language": "JavaScript",
      "topics": ["skill", "github-topic"],
      "updated_at": "2026-05-11T12:00:00Z"
    }
  ]
}
```

## Notes

- GitHub API has rate limits (5000 requests/hour for authenticated users)
- The script respects rate limits and adds delays between requests
- Data is cached to avoid unnecessary regeneration
- Only commits changes if actual data changed
