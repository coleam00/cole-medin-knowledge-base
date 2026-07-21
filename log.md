# Log

Append-only ingestion history, newest first. See [SCHEMA.md](SCHEMA.md) §8.

## 2026-07-21

**Creation.** Initial build of the Cole Medin AI Knowledge Base from the full long-form YouTube catalog. Transcripts sourced from the AI Tutor production database (timestamped, immutable) and enriched with publish dates from the YouTube Data API. Concepts and entities mined per-video, then deduplicated into a canonical taxonomy; source/concept/entity pages written and cross-linked; indexes generated and `lint.py` run clean.
