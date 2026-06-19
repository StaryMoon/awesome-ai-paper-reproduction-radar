#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reproductions.json"
COLLECTIONS = ROOT / "data" / "collections.json"
README = ROOT / "README.md"
DOCS = ROOT / "docs" / "index.html"
COLLECTION_DOCS = ROOT / "docs" / "collections"

CATEGORY_ORDER = [
    "Frontier LLMs",
    "Reasoning LLMs",
    "Vision-Language Models",
    "Video and World Models",
    "Generation and Diffusion",
    "3D and Rendering",
    "Robotics and Embodied AI",
    "Image Restoration",
    "Segmentation and Motion",
    "Code Models",
    "Efficient Sequence Models",
    "Other AI Papers",
]

HOT_WITHOUT_CODE_CATEGORIES = [
    "Reasoning LLMs",
    "Video and World Models",
    "Robotics and Embodied AI",
    "Image Restoration",
    "Vision-Language Models",
]

HOT_WITHOUT_CODE_LIMIT = 10


def load() -> tuple[dict, list[dict]]:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    collections = json.loads(COLLECTIONS.read_text(encoding="utf-8"))["collections"]
    return data, collections


def by_repo(papers: list[dict]) -> dict[str, dict]:
    return {item["repo"]: item for item in papers}


def short_tags(tags: list[str], n: int = 5) -> str:
    return ", ".join(tags[:n]) if tags else "-"


def paper_link(item: dict) -> str:
    if item.get("paper_url"):
        label = item.get("arxiv_id") or "Paper"
        return f"[{label}]({item['paper_url']})"
    return "-"


def repo_label(item: dict) -> str:
    return item["repo"].replace("-Unofficial", "")


def table_rows(papers: list[dict], category: str | None = None) -> list[str]:
    rows = []
    for item in papers:
        if category and item.get("category") != category:
            continue
        rows.append(
            "| [{repo}]({url}) | {paper} | {source} | {status} | {tags} |".format(
                repo=repo_label(item),
                url=item["github_url"],
                paper=item["paper_title"].replace("|", "\\|"),
                source=paper_link(item),
                status=item.get("status", "-").replace("|", "/"),
                tags=short_tags(item.get("tags", [])).replace("|", "/"),
            )
        )
    return rows


def render_collection_row(collection: dict) -> str:
    link = f"docs/collections/{collection['id']}.md"
    repos = ", ".join(f"`{name.replace('-Unofficial', '')}`" for name in collection["repos"][:5])
    if len(collection["repos"]) > 5:
        repos += f", +{len(collection['repos']) - 5} more"
    return f"| [{collection['title']}]({link}) | {collection['who']} | {collection['why_now']} | {repos} |"


def why_people_search(item: dict) -> str:
    category = item.get("category", "")
    tags = set(item.get("tags", []))
    if category == "Reasoning LLMs":
        return "Reasoning RL and test-time scaling papers are searched for starter code before official recipes settle."
    if category == "Video and World Models":
        return "Video generation and world-model papers are hard to compare without a runnable interface map."
    if category == "Robotics and Embodied AI":
        return "VLA and robot-policy readers need quick links from papers to action-interface starters."
    if category == "Image Restoration":
        return "Restoration papers attract readers looking for baselines, degradation settings, and PyTorch entrypoints."
    if category == "Vision-Language Models" or "multimodal" in tags:
        return "Multimodal papers move quickly, so readers often search for unified starter repos."
    return "High-interest paper with an unofficial starter that is easier to scan from a single radar."


def hot_without_official_code_rows(papers: list[dict]) -> list[str]:
    selected: list[dict] = []
    for category in HOT_WITHOUT_CODE_CATEGORIES:
        bucket = [
            item for item in papers
            if item.get("category") == category and item.get("github_url") and "unofficial" in item.get("github_url", "").lower()
        ]
        bucket.sort(key=lambda item: (item.get("stars", 0), item.get("pushed_at", ""), item.get("repo", "")), reverse=True)
        selected.extend(bucket[:2])

    seen: set[str] = set()
    rows: list[str] = []
    for item in selected[:HOT_WITHOUT_CODE_LIMIT]:
        if item["repo"] in seen:
            continue
        seen.add(item["repo"])
        rows.append(
            "| {paper} | {topic} | {official} | {starter} | {why} |".format(
                paper=f"[{item['paper_title'].replace('|', '\\|')}]({item['paper_url']})" if item.get("paper_url") else item["paper_title"].replace("|", "\\|"),
                topic=item.get("area_label") or item.get("category", "-"),
                official="Not indexed here yet",
                starter=f"[{repo_label(item)}]({item['github_url']})",
                why=why_people_search(item).replace("|", "/"),
            )
        )
    return rows


def render_readme(data: dict, collections: list[dict]) -> str:
    papers = data["papers"]
    counts = Counter(p.get("category", "Other AI Papers") for p in papers)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        by_cat[paper.get("category", "Other AI Papers")].append(paper)

    lines = [
        "# Awesome AI Paper Reproduction Radar",
        "",
        '<div align="center">',
        "",
        "**A searchable radar of high-interest AI papers and unofficial PyTorch reproduction repositories.**",
        "",
        "Find hot AI papers, code status, and unofficial reproduction starters in one searchable radar.",
        "",
        f"![Repos](https://img.shields.io/badge/reproductions-{len(papers)}-blue) "
        f"![Collections](https://img.shields.io/badge/curated_tracks-{len(collections)}-purple) "
        f"![Updated](https://img.shields.io/badge/updated-{updated}-green) "
        "![License](https://img.shields.io/badge/license-MIT-green)",
        "",
        "[Browse table](#repository-radar) · [Curated tracks](#curated-tracks) · "
        "[Latest daily note](docs/daily/2026-06-19.md) · "
        "[Searchable HTML](docs/index.html) · [Data JSON](data/reproductions.json) · [Contribute](CONTRIBUTING.md)",
        "",
        "</div>",
        "",
        "> Maintained by [@StaryMoon](https://github.com/StaryMoon). If this radar helps you find, compare, or start reproducing an AI paper, please consider starring the repository and following my GitHub profile.",
        "",
        "## What Makes This Different",
        "",
        "Most paper lists are either raw link dumps or single-topic awesome lists. This radar is built around three more useful layers:",
        "",
        "- **Searchable data layer**: every entry is stored in `data/reproductions.json` for scripting, filtering, and reuse.",
        "- **Curated tracks**: papers are grouped by research intent, not only by repo name or conference.",
        "- **Implementation-status view**: each entry points to paper, repo, tags, and current reproduction interface in one table.",
        "- **Daily metadata refresh**: GitHub Actions can refresh stars, topics, and push timestamps without manual bookkeeping.",
        "",
        "Every linked implementation is clearly marked as **unofficial** and keeps paper citations separate from local experiment logs.",
        "",
        "## Latest Daily Radar Note",
        "",
        "- [2026-06-19](docs/daily/2026-06-19.md) — a search-facing triage note for reasoning LLMs, video/world models, robotics/VLA, multimodal generation, and restoration starters.",
        "",
        "## Hot Papers Without Official Code Indexed Yet",
        "",
        "This section highlights papers where the radar currently indexes an unofficial starter but no official-code link. It is meant for readers deciding what to read, reproduce, or watch next.",
        "",
        "| Paper | Venue / topic | Official code status | Unofficial starter | Why people search it |",
        "|---|---|---|---|---|",
    ]
    lines.extend(hot_without_official_code_rows(papers))

    lines += [
        "",
        "## Radar Snapshot",
        "",
        "| Area | Count | Representative repos |",
        "|---|---:|---|",
    ]

    for category in CATEGORY_ORDER:
        if category not in by_cat:
            continue
        reps = ", ".join(f"[{repo_label(p)}]({p['github_url']})" for p in by_cat[category][:5])
        lines.append(f"| {category} | {counts[category]} | {reps} |")

    lines += [
        "",
        "## Curated Tracks",
        "",
        "These are the buy-in oriented collections: each one explains who should care, why the area is hot, and which repos form a readable route through the topic.",
        "",
        "| Track | Good for | Why now | Representative repos |",
        "|---|---|---|---|",
    ]
    lines.extend(render_collection_row(collection) for collection in collections)

    lines += [
        "",
        "## Repository Radar",
        "",
        "The full machine-readable dataset lives in [`data/reproductions.json`](data/reproductions.json).",
        "",
    ]
    for category in CATEGORY_ORDER:
        rows = table_rows(papers, category)
        if not rows:
            continue
        lines += [
            f"### {category}",
            "",
            "| Repo | Paper | Source | Implementation status | Tags |",
            "|---|---|---|---|---|",
        ]
        lines.extend(rows)
        lines.append("")

    lines += [
        "## Search Locally",
        "",
        "```bash",
        "python scripts/build.py",
        "python scripts/refresh_github_metadata.py",
        "```",
        "",
        "The static page at [`docs/index.html`](docs/index.html) provides a client-side searchable table for all entries.",
        "",
        "## Add a Paper",
        "",
        "Open a pull request that edits `data/reproductions.json` and then runs `python scripts/build.py`. Good entries should include:",
        "",
        "- paper title and paper URL;",
        "- repository URL;",
        "- category and tags;",
        "- current implementation status;",
        "- clear unofficial attribution if the repository is not from the paper authors.",
        "",
        "## Disclaimer",
        "",
        "This project is an independent index of unofficial paper reproduction repositories. Paper names, datasets, model names, official code, and trademarks belong to their respective owners. Always cite the original papers and check the licenses of official assets before reuse.",
        "",
    ]
    return "\n".join(lines)


def render_collection_doc(collection: dict, papers_by_repo: dict[str, dict]) -> str:
    lines = [
        f"# {collection['title']}",
        "",
        collection["hook"],
        "",
        f"**Good for:** {collection['who']}",
        "",
        f"**Why now:** {collection['why_now']}",
        "",
        "## Route",
        "",
        "| Repo | Paper | Source | Tags |",
        "|---|---|---|---|",
    ]
    for repo in collection["repos"]:
        item = papers_by_repo.get(repo)
        if not item:
            continue
        lines.append(
            "| [{repo}]({url}) | {paper} | {source} | {tags} |".format(
                repo=repo_label(item),
                url=item["github_url"],
                paper=item["paper_title"].replace("|", "\\|"),
                source=paper_link(item),
                tags=short_tags(item.get("tags", [])).replace("|", "/"),
            )
        )
    lines += [
        "",
        "## Suggested Reading Flow",
        "",
        "1. Start from the first two repositories to understand the main architectural vocabulary.",
        "2. Read the middle entries as design variants and ablations.",
        "3. Use the later entries to compare adjacent tasks, data assumptions, or evaluation setups.",
        "",
        "[Back to radar](../../README.md)",
        "",
    ]
    return "\n".join(lines)


def render_site(data: dict, collections: list[dict]) -> str:
    papers_json = json.dumps(data["papers"], ensure_ascii=False)
    collections_json = json.dumps(collections, ensure_ascii=False)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome AI Paper Reproduction Radar</title>
  <style>
    :root {{ color-scheme: light; --fg:#17202a; --muted:#667085; --line:#e6e8ee; --bg:#f7f8fb; --card:#ffffff; --accent:#2457ff; }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; color:var(--fg); background:var(--bg); }}
    header {{ padding:48px 24px 28px; background:#fff; border-bottom:1px solid var(--line); }}
    .wrap {{ max-width:1180px; margin:0 auto; }}
    h1 {{ margin:0 0 10px; font-size:clamp(30px,5vw,56px); letter-spacing:0; }}
    h2 {{ margin:32px 0 14px; }}
    p {{ color:var(--muted); line-height:1.6; }}
    .bar {{ display:flex; gap:12px; flex-wrap:wrap; margin-top:24px; }}
    input, select {{ border:1px solid var(--line); background:#fff; border-radius:8px; padding:12px 14px; font-size:15px; min-height:44px; }}
    input {{ flex:1 1 360px; }}
    select {{ flex:0 0 240px; }}
    main {{ padding:24px; }}
    .stats, .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:12px; margin-bottom:18px; }}
    .stat, .card {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px; }}
    .stat b {{ display:block; font-size:28px; }}
    .card h3 {{ margin:0 0 8px; font-size:16px; }}
    .table {{ overflow:auto; background:var(--card); border:1px solid var(--line); border-radius:8px; }}
    table {{ width:100%; border-collapse:collapse; min-width:980px; }}
    th, td {{ padding:13px 14px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }}
    th {{ position:sticky; top:0; background:#fbfcff; font-size:13px; color:#475467; }}
    a {{ color:var(--accent); text-decoration:none; }}
    .tag {{ display:inline-block; margin:0 5px 5px 0; padding:3px 7px; border-radius:999px; background:#eef2ff; color:#3445a8; font-size:12px; }}
    .muted {{ color:var(--muted); }}
    footer {{ padding:24px; color:var(--muted); }}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>Awesome AI Paper Reproduction Radar</h1>
      <p>Find hot AI papers, code status, and unofficial reproduction starters in one searchable radar. Updated {updated}.</p>
      <div class="bar">
        <input id="q" placeholder="Search paper, repo, area, tag, arXiv id..." autofocus>
        <select id="cat"><option value="">All categories</option></select>
      </div>
    </div>
  </header>
  <main class="wrap">
    <section class="stats">
      <div class="stat"><span class="muted">Repositories</span><b id="count">0</b></div>
      <div class="stat"><span class="muted">Categories</span><b id="cats">0</b></div>
      <div class="stat"><span class="muted">Curated Tracks</span><b id="tracks">0</b></div>
    </section>
    <h2>Curated Tracks</h2>
    <section class="cards" id="collectionCards"></section>
    <h2>Repository Radar</h2>
    <section class="table">
      <table>
        <thead><tr><th>Repository</th><th>Paper</th><th>Category</th><th>Source</th><th>Status</th><th>Tags</th></tr></thead>
        <tbody id="rows"></tbody>
      </table>
    </section>
  </main>
  <footer class="wrap">Maintained by <a href="https://github.com/StaryMoon">@StaryMoon</a>. All implementation links are unofficial unless stated otherwise.</footer>
<script>
const papers = {papers_json};
const collections = {collections_json};
const q = document.getElementById('q');
const cat = document.getElementById('cat');
const rows = document.getElementById('rows');
const cards = document.getElementById('collectionCards');
const cats = [...new Set(papers.map(p => p.category || 'Other AI Papers'))].sort();
cat.innerHTML += cats.map(c => `<option value="${{c}}">${{c}}</option>`).join('');
document.getElementById('count').textContent = papers.length;
document.getElementById('cats').textContent = cats.length;
document.getElementById('tracks').textContent = collections.length;
function esc(s) {{ return String(s || '').replace(/[&<>"']/g, m => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[m])); }}
cards.innerHTML = collections.map(c => `<article class="card"><h3><a href="collections/${{c.id}}.md">${{esc(c.title)}}</a></h3><p>${{esc(c.hook)}}</p><p class="muted">${{esc(c.why_now)}}</p></article>`).join('');
function render() {{
  const query = q.value.toLowerCase().trim();
  const c = cat.value;
  const filtered = papers.filter(p => {{
    const hay = [p.repo,p.paper_title,p.category,p.area_label,p.arxiv_id,(p.tags||[]).join(' ')].join(' ').toLowerCase();
    return (!c || p.category === c) && (!query || hay.includes(query));
  }});
  rows.innerHTML = filtered.map(p => `<tr><td><a href="${{p.github_url}}">${{esc(p.repo.replace('-Unofficial',''))}}</a><br><span class="muted">${{esc(p.description)}}</span></td><td>${{esc(p.paper_title)}}</td><td>${{esc(p.category)}}</td><td>${{p.paper_url ? `<a href="${{p.paper_url}}">${{esc(p.arxiv_id || 'Paper')}}</a>` : '-'}}</td><td>${{esc(p.status)}}</td><td>${{(p.tags||[]).slice(0,8).map(t=>`<span class="tag">${{esc(t)}}</span>`).join('')}}</td></tr>`).join('');
}}
q.addEventListener('input', render); cat.addEventListener('change', render); render();
</script>
</body>
</html>
'''


def write_collection_docs(data: dict, collections: list[dict]) -> None:
    papers_by_repo = by_repo(data["papers"])
    if COLLECTION_DOCS.exists():
        shutil.rmtree(COLLECTION_DOCS)
    COLLECTION_DOCS.mkdir(parents=True)
    for collection in collections:
        (COLLECTION_DOCS / f"{collection['id']}.md").write_text(
            render_collection_doc(collection, papers_by_repo),
            encoding="utf-8",
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data, collections = load()
    readme = render_readme(data, collections)
    site = render_site(data, collections)

    if args.check:
        ok = (
            README.exists()
            and DOCS.exists()
            and README.read_text(encoding="utf-8") == readme
            and DOCS.read_text(encoding="utf-8") == site
        )
        raise SystemExit(0 if ok else 1)

    README.write_text(readme, encoding="utf-8")
    DOCS.write_text(site, encoding="utf-8")
    write_collection_docs(data, collections)


if __name__ == "__main__":
    main()
