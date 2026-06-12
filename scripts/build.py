#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'reproductions.json'
README = ROOT / 'README.md'
DOCS = ROOT / 'docs' / 'index.html'
CATEGORY_ORDER = ['Frontier LLMs','Reasoning LLMs','Vision-Language Models','Video and World Models','Generation and Diffusion','3D and Rendering','Robotics and Embodied AI','Image Restoration','Segmentation and Motion','Code Models','Other AI Papers']


def load() -> dict:
    return json.loads(DATA.read_text(encoding='utf-8'))


def short_tags(tags: list[str], n: int = 5) -> str:
    return ', '.join(tags[:n]) if tags else '-'


def paper_link(item: dict) -> str:
    if item.get('paper_url'):
        label = item.get('arxiv_id') or 'Paper'
        return f'[{label}]({item["paper_url"]})'
    return '-'


def table_rows(papers: list[dict], category: str | None = None) -> list[str]:
    rows = []
    for p in papers:
        if category and p.get('category') != category:
            continue
        rows.append('| [{repo}]({url}) | {paper} | {source} | {status} | {tags} |'.format(repo=p['repo'].replace('-Unofficial', ''), url=p['github_url'], paper=p['paper_title'].replace('|', '\\|'), source=paper_link(p), status=p.get('status', '-').replace('|', '/'), tags=short_tags(p.get('tags', [])).replace('|', '/')))
    return rows


def render_readme(data: dict) -> str:
    papers = data['papers']
    counts = Counter(p.get('category', 'Other AI Papers') for p in papers)
    updated = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    by_cat = defaultdict(list)
    for p in papers:
        by_cat[p.get('category', 'Other AI Papers')].append(p)
    lines = ['# Awesome AI Paper Reproduction Radar', '', '<div align="center">', '', '**A searchable radar of high-interest AI papers and unofficial PyTorch reproduction repositories.**', '', f'![Repos](https://img.shields.io/badge/reproductions-{len(papers)}-blue) ![Categories](https://img.shields.io/badge/categories-{len(set(p.get("category", "Other AI Papers") for p in papers))}-purple) ![Updated](https://img.shields.io/badge/updated-{updated}-green) ![License](https://img.shields.io/badge/license-MIT-green)', '', '[Browse table](#repository-radar) · [Searchable HTML](docs/index.html) · [Data JSON](data/reproductions.json) · [Contribute](CONTRIBUTING.md)', '', '</div>', '', '> Maintained by [@StaryMoon](https://github.com/StaryMoon). If this radar helps you find, compare, or start reproducing an AI paper, please consider starring the repository and following my GitHub profile.', '', '## Why This Exists', '', 'AI papers move faster than official code releases. This repository collects paper-to-code reproduction entries in one place so readers can quickly answer three questions:', '', '- Which hot papers already have a public reproduction entry?', '- Where is the paper, PDF, repository, and current implementation interface?', '- Which direction should I inspect next: reasoning, VLM, video, robotics, 3D, restoration, or code models?', '', 'Every linked implementation is clearly marked as **unofficial** and keeps paper citations separate from local experiment logs.', '', '## Radar Snapshot', '', '| Area | Count | Representative repos |', '|---|---:|---|']
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        reps = ', '.join(f'[{p["repo"].replace("-Unofficial", "")}]({p["github_url"]})' for p in by_cat[cat][:5])
        lines.append(f'| {cat} | {counts[cat]} | {reps} |')
    lines += ['', '## Repository Radar', '', 'The full machine-readable dataset lives in [`data/reproductions.json`](data/reproductions.json).', '']
    for cat in CATEGORY_ORDER:
        rows = table_rows(papers, cat)
        if not rows:
            continue
        lines += [f'### {cat}', '', '| Repo | Paper | Source | Implementation status | Tags |', '|---|---|---|---|---|']
        lines.extend(rows)
        lines.append('')
    lines += ['## Search Locally', '', '```bash', 'python scripts/build.py', 'python scripts/refresh_github_metadata.py', '```', '', 'The static page at [`docs/index.html`](docs/index.html) provides a client-side searchable table for all entries.', '', '## Add a Paper', '', 'Open a pull request that edits `data/reproductions.json` and then runs `python scripts/build.py`. Good entries should include:', '', '- paper title and paper URL;', '- repository URL;', '- category and tags;', '- current implementation status;', '- clear unofficial attribution if the repository is not from the paper authors.', '', '## Disclaimer', '', 'This project is an independent index of unofficial paper reproduction repositories. Paper names, datasets, model names, official code, and trademarks belong to their respective owners. Always cite the original papers and check the licenses of official assets before reuse.', '']
    return '\n'.join(lines)


def render_site(data: dict) -> str:
    papers_json = json.dumps(data['papers'], ensure_ascii=False)
    updated = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    return '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome AI Paper Reproduction Radar</title>
  <style>
    :root { color-scheme: light; --fg:#17202a; --muted:#667085; --line:#e6e8ee; --bg:#f7f8fb; --card:#ffffff; --accent:#2457ff; }
    * { box-sizing: border-box; }
    body { margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; color:var(--fg); background:var(--bg); }
    header { padding:48px 24px 28px; background:#fff; border-bottom:1px solid var(--line); }
    .wrap { max-width:1180px; margin:0 auto; }
    h1 { margin:0 0 10px; font-size:clamp(30px,5vw,56px); letter-spacing:0; }
    p { color:var(--muted); line-height:1.6; }
    .bar { display:flex; gap:12px; flex-wrap:wrap; margin-top:24px; }
    input, select { border:1px solid var(--line); background:#fff; border-radius:8px; padding:12px 14px; font-size:15px; min-height:44px; }
    input { flex:1 1 360px; }
    select { flex:0 0 240px; }
    main { padding:24px; }
    .stats { display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:12px; margin-bottom:18px; }
    .stat { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px; }
    .stat b { display:block; font-size:28px; }
    .table { overflow:auto; background:var(--card); border:1px solid var(--line); border-radius:8px; }
    table { width:100%; border-collapse:collapse; min-width:980px; }
    th, td { padding:13px 14px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }
    th { position:sticky; top:0; background:#fbfcff; font-size:13px; color:#475467; }
    a { color:var(--accent); text-decoration:none; }
    .tag { display:inline-block; margin:0 5px 5px 0; padding:3px 7px; border-radius:999px; background:#eef2ff; color:#3445a8; font-size:12px; }
    .muted { color:var(--muted); }
    footer { padding:24px; color:var(--muted); }
  </style>
</head>
<body>
  <header><div class="wrap"><h1>Awesome AI Paper Reproduction Radar</h1><p>A searchable radar of high-interest AI papers and unofficial PyTorch reproduction repositories. Updated ''' + updated + '''.</p><div class="bar"><input id="q" placeholder="Search paper, repo, area, tag, arXiv id..." autofocus><select id="cat"><option value="">All categories</option></select></div></div></header>
  <main class="wrap"><section class="stats"><div class="stat"><span class="muted">Repositories</span><b id="count">0</b></div><div class="stat"><span class="muted">Categories</span><b id="cats">0</b></div><div class="stat"><span class="muted">Tracked Stars</span><b id="stars">0</b></div></section><section class="table"><table><thead><tr><th>Repository</th><th>Paper</th><th>Category</th><th>Source</th><th>Status</th><th>Tags</th></tr></thead><tbody id="rows"></tbody></table></section></main>
  <footer class="wrap">Maintained by <a href="https://github.com/StaryMoon">@StaryMoon</a>. All implementation links are unofficial unless stated otherwise.</footer>
<script>
const papers = ''' + papers_json + ''';
const q = document.getElementById('q');
const cat = document.getElementById('cat');
const rows = document.getElementById('rows');
const cats = [...new Set(papers.map(p => p.category || 'Other AI Papers'))].sort();
cat.innerHTML += cats.map(c => `<option value="${c}">${c}</option>`).join('');
document.getElementById('count').textContent = papers.length;
document.getElementById('cats').textContent = cats.length;
document.getElementById('stars').textContent = papers.reduce((s,p)=>s+(p.stars||0),0);
function esc(s) { return String(s || '').replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }
function render() {
  const query = q.value.toLowerCase().trim();
  const c = cat.value;
  const filtered = papers.filter(p => {
    const hay = [p.repo,p.paper_title,p.category,p.area_label,p.arxiv_id,(p.tags||[]).join(' ')].join(' ').toLowerCase();
    return (!c || p.category === c) && (!query || hay.includes(query));
  });
  rows.innerHTML = filtered.map(p => `<tr><td><a href="${p.github_url}">${esc(p.repo.replace('-Unofficial',''))}</a><br><span class="muted">${esc(p.description)}</span></td><td>${esc(p.paper_title)}</td><td>${esc(p.category)}</td><td>${p.paper_url ? `<a href="${p.paper_url}">${esc(p.arxiv_id || 'Paper')}</a>` : '-'}</td><td>${esc(p.status)}</td><td>${(p.tags||[]).slice(0,8).map(t=>`<span class="tag">${esc(t)}</span>`).join('')}</td></tr>`).join('');
}
q.addEventListener('input', render); cat.addEventListener('change', render); render();
</script>
</body>
</html>
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = load()
    readme = render_readme(data)
    site = render_site(data)
    if args.check:
        ok = README.exists() and DOCS.exists() and README.read_text(encoding='utf-8') == readme and DOCS.read_text(encoding='utf-8') == site
        raise SystemExit(0 if ok else 1)
    README.write_text(readme, encoding='utf-8')
    DOCS.write_text(site, encoding='utf-8')

if __name__ == '__main__':
    main()
