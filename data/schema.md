# Data Schema

`data/reproductions.json` is the source of truth for the radar.

Important fields:

- `repo`: GitHub repository name.
- `github_url`: Repository URL.
- `paper_title`: Paper or technical report title.
- `paper_url`: Original paper URL.
- `arxiv_id`: arXiv identifier when available.
- `category`: High-level research direction.
- `status`: Short implementation status.
- `tags`: Search/filter tags.
- `stars`, `created_at`, `pushed_at`: GitHub metadata refreshed by `scripts/refresh_github_metadata.py`.
