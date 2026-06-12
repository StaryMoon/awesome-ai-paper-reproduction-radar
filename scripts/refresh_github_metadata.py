#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'reproductions.json'
OWNER = os.environ.get('RADAR_GITHUB_OWNER', 'StaryMoon')


def gh_repo_list() -> list[dict]:
    raw = subprocess.check_output(['gh', 'repo', 'list', OWNER, '--limit', '300', '--json', 'name,url,description,stargazerCount,pushedAt,createdAt,repositoryTopics,isPrivate'], text=True)
    return json.loads(raw)


def main() -> None:
    data = json.loads(DATA.read_text(encoding='utf-8'))
    by_name = {item['repo']: item for item in data['papers']}
    for repo in gh_repo_list():
        name = repo['name']
        if name not in by_name or repo.get('isPrivate'):
            continue
        item = by_name[name]
        item['github_url'] = repo.get('url') or item.get('github_url', '')
        item['description'] = repo.get('description') or item.get('description', '')
        item['stars'] = repo.get('stargazerCount', item.get('stars', 0))
        item['pushed_at'] = repo.get('pushedAt', item.get('pushed_at', ''))
        item['created_at'] = repo.get('createdAt', item.get('created_at', ''))
        topics = sorted(t['name'] for t in repo.get('repositoryTopics', []))
        item['tags'] = sorted(set(item.get('tags', []) + topics))[:16]
    data['meta']['generated_at'] = datetime.now(timezone.utc).isoformat()
    data['meta']['repository_count'] = len(data['papers'])
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
