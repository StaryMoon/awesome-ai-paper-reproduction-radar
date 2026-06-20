# Code Availability Policy

This radar separates paper discovery, official-code indexing, and unofficial starter repositories.

## Status Wording

| Wording | Meaning |
|---|---|
| Official link indexed | The radar has an explicit link to an author or project official implementation. |
| Official link not indexed in this radar yet | The radar currently does not store an official-code URL for this entry. This is not a claim that no official code exists. |
| Unofficial starter | The linked repository is an independent starter or reproduction scaffold and is not maintained by the paper authors unless explicitly stated. |

## Why This Matters

AI papers often move through several public stages: preprint, project page, model card, partial release, full code release, and community reproduction. A useful radar should make those stages easy to scan without overstating what has or has not been released.

## Current Practice

- Paper metadata and starter links are stored in `data/reproductions.json`.
- The README and static HTML page are generated from that data.
- When the radar has not indexed an official-code URL, the README says `Official link not indexed in this radar yet`.
- Daily notes may highlight high-search topics, but they should not present unofficial starters as official code.

## Planned Schema

A future dataset revision should add explicit fields such as:

```json
{
  "official_code_url": "",
  "official_code_status": "not_indexed",
  "starter_type": "unofficial"
}
```

That would make the generated tables easier to filter and less dependent on prose wording.

