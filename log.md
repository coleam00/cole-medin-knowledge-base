# Log

Append-only ingestion history, newest first. See [SCHEMA.md](SCHEMA.md) §8.

## 2026-07-21

**Creation.** Initial build of the Cole Medin AI Knowledge Base from the full long-form YouTube catalog. Transcripts sourced from the AI Tutor production database (timestamped, immutable) and enriched with publish dates from the YouTube Data API. Concepts and entities mined per-video, then deduplicated into a canonical taxonomy; source/concept/entity pages written and cross-linked; indexes generated and `lint.py` run clean.

## 2026-07-21 (later)

**Update.** Coverage sweep: scanned all 198 videos for durable ideas lacking a page, canonicalized 342 gap mentions into a deduped add-list, notability-triaged single-video entity candidates (30 sponsor-read/micro-tool candidates rejected), and added 155 new pages (57 concepts, 86 tools, 5 people, 7 organizations) with cited quotes and reciprocal links. Indexes and taxonomy regenerated; lint clean.
